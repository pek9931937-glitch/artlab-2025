from flask import Flask, render_template

app = Flask(__name__)

# 학생 이름 목록 (페이지 이동 순서)
students = [
    # 1학년 (11명)
    "곽민지", "김채영", "양희욱", "이현준", "이진주",
    "김민재", "윤종민", "서희", "이승재", "이난영", "조현아",
    # 2학년 (3명)
    "김건우", "민희윤", "배소윤",
    # 3학년 (1명)
    "김경원",
]


@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/student/<name>")
def student_page(name):
    prev_name = None
    next_name = None

    if name in students:
        idx = students.index(name)
        if idx > 0:
            prev_name = students[idx - 1]
        if idx < len(students) - 1:
            next_name = students[idx + 1]

    return render_template(
        "student.html",
        name=name,
        prev_name=prev_name,
        next_name=next_name,
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)



