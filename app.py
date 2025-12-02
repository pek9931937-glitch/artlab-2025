import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# -----------------------------
#  학생 목록 (학년 + 학번 + 이름)
# -----------------------------
STUDENTS = [
    # 1학년
    {"grade": 1, "id": "10103", "name": "곽민지"},
    {"grade": 1, "id": "10108", "name": "김채영"},
    {"grade": 1, "id": "10115", "name": "양희욱"},
    {"grade": 1, "id": "10123", "name": "이현준"},
    {"grade": 1, "id": "10224", "name": "이진주"},
    {"grade": 1, "id": "10304", "name": "김민재"},
    {"grade": 1, "id": "10318", "name": "윤종민"},
    {"grade": 1, "id": "10611", "name": "서희"},
    {"grade": 1, "id": "10616", "name": "이승재"},
    {"grade": 1, "id": "10820", "name": "이난영"},
    {"grade": 1, "id": "10832", "name": "조현아"},
    # 2학년
    {"grade": 2, "id": "20203", "name": "김건우"},
    {"grade": 2, "id": "20210", "name": "민희윤"},
    {"grade": 2, "id": "21013", "name": "배소윤"},
    # 3학년
    {"grade": 3, "id": "31131", "name": "김경원"},
]

# 정렬(학년 → 학번)
STUDENTS.sort(key=lambda s: (s["grade"], s["id"]))


def slug_of(student):
    """URL용 슬러그: 예) 10103-곽민지"""
    return f'{student["id"]}-{student["name"]}'


def find_student_by_slug(slug):
    for s in STUDENTS:
        if slug_of(s) == slug:
            return s
    return None


# -----------------------------
#  라우트
# -----------------------------
@app.route("/")
def index():
    # 학년별 그룹
    grouped = {1: [], 2: [], 3: []}
    for s in STUDENTS:
        grouped[s["grade"]].append(s)

    return render_template(
        "index.html",
        grouped=grouped,
        slug_of=slug_of,
    )


@app.route("/student/<slug>")
def student_page(slug):
    student = find_student_by_slug(slug)
    if not student:
        abort(404)

    # 이전/다음 학생 찾기
    idx = STUDENTS.index(student)
    prev_student = STUDENTS[idx - 1] if idx > 0 else None
    next_student = STUDENTS[idx + 1] if idx < len(STUDENTS) - 1 else None

    # 현재는 예시용 더미 데이터 (이미지 파일 넣으면 image 필드에 경로 지정하면 됨)
    artworks = [
        {
            "no": 1,
            "title": "1번 작품 제목입니다.",
            "description": "이 영역에는 1번 작품에 대한 제목과 상세한 설명이 들어갈 예정입니다. 지금은 예시 문장으로 채워져 있습니다.",
            "placeholder_label": "1번 작품 (이미지 자리)",
            "image": None,  # 실제 이미지 파일 사용 시 예: url_for('static', filename='art/10103_1.jpg')
        },
        {
            "no": 2,
            "title": "2번 작품 제목입니다.",
            "description": "이 영역에는 2번 작품에 대한 제목과 상세한 설명이 들어갈 예정입니다. 지금은 예시 문장으로 채워져 있습니다.",
            "placeholder_label": "2번 작품 (이미지 자리)",
            "image": None,
        },
    ]

    return render_template(
        "student.html",
        student=student,
        artworks=artworks,
        prev_student=prev_student,
        next_student=next_student,
        slug_of=slug_of,
    )


# -----------------------------
#  Render 실행 설정
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Render에서 반드시 host=0.0.0.0 / 지정 포트 사용
    app.run(host="0.0.0.0", port=port, debug=False)
