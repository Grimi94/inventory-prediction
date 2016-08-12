import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from numpy import inf

FROM = "2013"
TO = "2016"
# predicion time in months
PREDICTION_TIME = 4

class Model(object):
    def __init__(self, df):
        """
        Initializes our model class
        """
        self._df = df
        self._ts = self.__get_ts(df)

    def __calculate_extra_cols(self, df):
        """
        Calculates extra columns (only used when revenue wants to be plotted)
        """
        df['total_price'] =  df['CPRECIO'] * df['#UNIDADES'] * df['CTIPOCAM01']
        return df

    def __get_ts(self, df):
        """
        Transforms the raw dataframe into a dataframe indexed by time
        """
        ts = df.set_index("FECHA")[["#UNIDADES", "IDPRODUCTO"]]
        units_ts = ts[["#UNIDADES", "IDPRODUCTO"]]
        return units_ts

    def __get_product_ts(self, product_id):
        """
        From the dataframe it selects the product_id and transforms it
        into a resampled time series
        """
        d_range_s = FROM
        d_range_e = TO
        resample = "W"
        new_ts = self._ts[self._ts["IDPRODUCTO"] == product_id]["#UNIDADES"]
        ts = new_ts[d_range_s:d_range_e].resample(resample).mean().fillna(1)
        ts = np.log(ts)
        ts[ts == -inf] = 0
        return ts

    def predict_product(self, product_id):
        """
        Receives a product id and predicts
        """
        product_ts = self.__get_product_ts(product_id)

        model = SARIMAX(product_ts, order=(0,1,2),
                        time_varying_regression=True,
                        mle_regression=False,
                        trend='n',
                        seasonal_order=(1,1,1,11)).fit()
        steps = PREDICTION_TIME * 4
        forecast = model.get_forecast(steps=steps, dynamic=True)
        history = product_ts[(product_ts.index > "2015") & (product_ts.index < "2016")]
        history = history.fillna(0)
        # Output
        predicted_mean = forecast.predicted_mean
        conf_int = forecast.conf_int()
        return np.exp(history), np.exp(predicted_mean), np.exp(conf_int)
        # return history, predicted_mean, conf_int




