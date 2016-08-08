from flask import Flask, render_template

app = Flask(__name__)

# Normal analytics graphs
@app.route("/")
def home():
    return render_template("index.html")

# Recommend products based on other products
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")

# Recommend products based on other products
@app.route("/forecast")
def forecast():
    return render_template("forecast.html")

if __name__ == "__main__":
    app.run(debug=True)
