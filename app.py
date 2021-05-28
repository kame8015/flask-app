import os
from flask import Flask, request, redirect, url_for, send_from_directory
from flask.helpers import flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENTIONS = set(["png", "jpg", "jpeg", "gif"])
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    # 許可された拡張子だと1、でなければ0
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENTIONS


@app.route("/uploads/<filename>")
def uploaded_files(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/", methods=["GET", "POST"])
def upload_files():
    if request.method == "POST":
        # データの取り出し
        files = request.files.getlist("upload_files")
        for file in files:
            # ファイル名がなかったとき
            if file.filename == "":
                flash("ファイルがありません")
                return redirect(request.url)
            print(file.filename)
            # ファイルのチェック
            if file and allowed_file(file.filename):
                # 危険な文字を削除(サニタイズ処理)
                filename = secure_filename(file.filename)
                # ファイルの保存
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                # アップロード後のページに転送
                # return redirect(url_for("uploaded_files", filename=filename))
        return redirect(request.url)
    return """
    <!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>
                ファイルをアップロードして判定しよう
            </title>
        </head>
        <body>
            <h1>
                ファイルをアップロードして判定しよう
            </h1>
            <form method = post enctype = multipart/form-data>
                <p><input type=file name = upload_files multiple>
                <input type = submit value = Upload>
            </form>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host=os.getenv("APP_ADDRESS", "localhost"), port=8000)
