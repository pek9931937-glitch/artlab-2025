from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# ------------------------------
# 학생 데이터
# ------------------------------
students = {
    "1학년": [
        ("10103", "곽민지"), ("10108", "김채영"), ("10115", "양희옥"),
        ("10123", "이현준"), ("10224", "이진주"),
        ("10304", "김민재"), ("10318", "윤종민"),
        ("10611", "서희"), ("10616", "이승재"),
        ("10820", "이난영"), ("10832", "조현아")
    ],
    "2학년": [
        ("20203", "김건우"), ("20210", "민희윤"), ("21013", "배소윤")
    ],
    "3학년": [
        ("31131", "김경원")
    ]
}

# ------------------------------
# 홈
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html", students=students)

# ------------------------------
# 개별 학생 페이지
# ------------------------------
@app.route("/student/<id>/<name>")
def student(id, name):
    return render_template("student.html", id=id, name=name)

# ------------------------------
# Render 호환 서버 실행
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
