from flask import Flask, render_template
import os

app = Flask(__name__)

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


@app.route("/")
def home():
    # 메인에서 학년별로 잘라 쓰기 때문에 전체 students만 넘기면 됨
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
