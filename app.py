from flask import Flask, render_template, request
from model import predict_image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return render_template("index.html")

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html")

    image_bytes = file.read()

    label, probability, confidence = predict_image(image_bytes)

    return render_template(
        "index.html",
        label=label,
        probability=round(probability, 4),
        confidence=round(confidence, 4)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)