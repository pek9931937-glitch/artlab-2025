from flask import Flask, render_template
import os

app = Flask(__name__)

# 학생 정보 (학번, 이름)
students = [
    # 1학년
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
    # 2학년
    ("20203", "김건우"),
    ("20210", "민희윤"),
    ("21013", "배소윤"),
    # 3학년
    ("31131", "김경원"),
]

student_ids = [f"{num}-{name}" for num, name in students]


@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/student/<student_id>")
def student_page(student_id):
    if student_id not in student_ids:
        return "Not Found", 404

    idx = student_ids.index(student_id)
    num, name = students[idx]

    prev_id = student_ids[idx - 1] if idx > 0 else None
    next_id = student_ids[idx + 1] if idx < len(student_ids) - 1 else None

    prev_name = students[idx - 1][1] if idx > 0 else None
    next_name = students[idx + 1][1] if idx < len(student_ids) - 1 else None

    return render_template(
        "student.html",
        student_id=student_id,
        num=num,
        name=name,
        prev_id=prev_id,
        next_id=next_id,
        prev_name=prev_name,
        next_name=next_name,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
