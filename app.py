from flask import Flask, render_template, request
from flood_prediction import predict
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    res = ""
    if request.method == "POST":
        city = request.form["city"]
        res=city
        res= predict(city)
        print(res)
    return render_template("index.html", result=res)

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True,host="0.0.0.0", port=port)