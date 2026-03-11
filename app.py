from flask import Flask, render_template, request
from flood_prediction import predict_m, predict_a
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        mode = request.form["mode"]

        if mode == "auto":

            city = request.form["city"]
            result = predict_a(city)

        else:

            max_temp = float(request.form["max_temp"])
            min_temp = float(request.form["min_temp"])
            rainfall = float(request.form["rainfall"])
            humidity = float(request.form["humidity"])
            wind_speed = float(request.form["wind_speed"])

            result = predict_m(
                max_temp,
                min_temp,
                rainfall,
                humidity,
                wind_speed
            )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)