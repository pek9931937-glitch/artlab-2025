import os
import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "likes.db")

# 학생 정보 (학번, 이름)
students = [
    # 1학년 (11명)
    ("10103", "곽민지"),
    ("10108", "김채영"),
    ("10115", "양희욱"),
    ("10123", "이현준"),
    ("10224", "이진주"),
    ("10304", "김민재"),
    ("10318", "윤종민"),
    ("10611", "서희"),
    ("10616", "이승재"),
    ("10820", "이난영"),
    ("10832", "조현아"),
    # 2학년 (3명)
    ("20203", "김건우"),
    ("20210", "민희윤"),
    ("21013", "배소윤"),
    # 3학년 (1명)
    ("31131", "김경원"),
]

# URL용 ID (예: "10108-김채영")
student_ids = [f"{num}-{name}" for num, name in students]


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS likes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            art_num INTEGER NOT NULL,
            ip TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.before_first_request
def before_first_request():
    init_db()


def get_client_ip():
    # Render 등 프록시 환경 고려
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.remote_addr or "unknown"


@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/student/<student_id>")
def student_page(student_id):
    if student_id not in student_ids:
        return "Not Found", 404

    idx = student_ids.index(student_id)
    num, name = students[idx]

    prev_id = prev_label = None
    next_id = next_label = None

    if idx > 0:
        prev_num, prev_name = students[idx - 1]
        prev_id = student_ids[idx - 1]
        prev_label = f"{prev_num} {prev_name}"

    if idx < len(students) - 1:
        next_num, next_name = students[idx + 1]
        next_id = student_ids[idx + 1]
        next_label = f"{next_num} {next_name}"

    return render_template(
        "student.html",
        student_id=student_id,
        num=num,
        name=name,
        prev_id=prev_id,
        next_id=next_id,
        prev_label=prev_label,
        next_label=next_label,
    )


# ---------- 좋아요 API ----------

@app.route("/api/likes/<student_id>", methods=["GET"])
def api_get_likes(student_id):
    """특정 학생 페이지의 작품 1,2에 대한 전체 좋아요 개수 + 현재 IP의 상태 반환"""
    if student_id not in student_ids:
        return jsonify({"error": "not found"}), 404

    ip = get_client_ip()
    conn = get_db()
    cur = conn.cursor()

    # 전체 카운트
    cur.execute(
        "SELECT art_num, COUNT(*) as cnt FROM likes WHERE student_id = ? GROUP BY art_num",
        (student_id,),
    )
    counts_raw = cur.fetchall()
    counts = {row["art_num"]: row["cnt"] for row in counts_raw}

    # 현재 IP가 누른 상태
    cur.execute(
        "SELECT art_num FROM likes WHERE student_id = ? AND ip = ?",
        (student_id, ip),
    )
    my_rows = cur.fetchall()
    my_likes = {row["art_num"]: True for row in my_rows}

    conn.close()

    # 항상 1,2 키가 있도록 채워 넣기
    data = {
        "counts": {
            1: counts.get(1, 0),
            2: counts.get(2, 0),
        },
        "my_likes": {
            1: my_likes.get(1, False),
            2: my_likes.get(2, False),
        },
    }
    return jsonify(data)


@app.route("/api/like", methods=["POST"])
def api_toggle_like():
    """좋아요 토글: 없으면 추가, 있으면 삭제 (IP 기준 1인 1회)"""
    data = request.get_json(silent=True) or {}
    student_id = data.get("student_id")
    art_num = data.get("art_num")

    if student_id not in student_ids:
        return jsonify({"error": "not found"}), 404
    try:
        art_num = int(art_num)
    except (TypeError, ValueError):
        return jsonify({"error": "bad art_num"}), 400
    if art_num not in (1, 2):
        return jsonify({"error": "bad art_num"}), 400

    ip = get_client_ip()
    conn = get_db()
    cur = conn.cursor()

    # 이미 눌렀는지 확인
    cur.execute(
        "SELECT id FROM likes WHERE student_id = ? AND art_num = ? AND ip = ?",
        (student_id, art_num, ip),
    )
    row = cur.fetchone()

    if row:
        # 이미 있으면 삭제 = 좋아요 취소
        cur.execute("DELETE FROM likes WHERE id = ?", (row["id"],))
        liked = False
    else:
        # 없으면 추가
        cur.execute(
            "INSERT INTO likes (student_id, art_num, ip) VALUES (?, ?, ?)",
            (student_id, art_num, ip),
        )
        liked = True

    # 현재 카운트 다시 계산
    cur.execute(
        "SELECT COUNT(*) as cnt FROM likes WHERE student_id = ? AND art_num = ?",
        (student_id, art_num),
    )
    cnt_row = cur.fetchone()
    count = cnt_row["cnt"] if cnt_row else 0

    conn.commit()
    conn.close()

    return jsonify({"liked": liked, "count": count})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
