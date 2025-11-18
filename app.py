from flask import Flask, render_template

app = Flask(__name__)

# 학생 리스트
students = [
    "곽민지", "김채영", "양희욱", "이현준", "윤종민",
    "서희", "이승재", "이나연", "조현아",
    "김건우", "민희윤", "배소윤",
    "김경원"
]

@app.route("/")
def home():
    return render_template("index.html", students=students)

# 자동 라우팅: /student/이름
@app.route("/student/<name>")
def student_page(name):
    return render_template("student.html", name=name)

if __name__ == "__main__":
    app.run()
