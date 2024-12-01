from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask() -> str:
	return "hello flask!" # ブラウザに hello flask を表示する

