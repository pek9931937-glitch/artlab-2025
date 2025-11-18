from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지
@app.route("/")
def index():
    return render_template("index.html")

# 민재 페이지
@app.route("/minjae")
def minjae():
    return render_template("minjae.html")

if __name__ == "__main__":
    app.run()
