from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "Нет файла"

        file = request.files["file"]

        if file.filename == "":
            return "Файл не выбран"

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        prediction = "Возможен дефект — требуется проверка"
        return render_template("index.html", filename=file.filename, prediction=prediction)

    return render_template("index.html")
