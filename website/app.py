from __future__ import division
from flask import Flask, render_template
import database as DB
from model import Model
import json
import numpy as np
import simplejson

app = Flask(__name__)
# Load data from csv file
db = DB.load_data("../BASEVENTAS2010A2015.csv")
model = Model(db)


# Normal analytics graphs
@app.route("/")
def home():
    return render_template("index.html")


# Recommend products based on other products
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


# Recommend products based on other products
@app.route("/forecast", defaults={'product_id': None})
@app.route("/forecast/<product_id>")
def forecast(product_id):
    if product_id:
        a, b = model.predict_product(product_id)
        a = a.reset_index()
        b = b.reset_index()

        a['FECHA'] = a['FECHA'].astype(np.int64) / 1e6
        b['index'] = b['index'].astype(np.int64) / 1e6

        results = {}
        results["history"] = a.values.tolist()
        results["prediction"] = b.values.tolist()
        results["description"] = "description"

        return simplejson.dumps(results, ignore_nan=True)
    else:
        return render_template("forecast.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
