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

@app.route("/")
def home():
    """
    Simple analytics graphs
    """
    return render_template("index.html")


@app.route("/recommend")
def recommend():
    """
    Recommend products based on other products
    """
    return render_template("recommend.html")


@app.route("/forecast", defaults={'product_id': None})
@app.route("/forecast/<product_id>")
def forecast(product_id):
    """
    Forecasts a product and sends back the information as json
    """
    if product_id:
        res, pred, conf = model.predict_product(product_id)
        res = res.reset_index()
        pred = pred.reset_index()
        conf = conf.reset_index()

        # Transform Timestamp into unix time
        res['FECHA'] = res['FECHA'].astype(np.int64) / 1e6
        pred['index'] = pred['index'].astype(np.int64) / 1e6
        conf['index'] = conf['index'].astype(np.int64) / 1e6

        # Prepare results dictionary
        results = {}
        results["history"] = res.values.tolist()
        results["prediction"] = pred.values.tolist()
        results["confidence"] = conf.values.tolist()
        results["description"] = "description"

        return simplejson.dumps(results, ignore_nan=True)
    else:
        return render_template("forecast.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
