from flask import jsonify, request, Blueprint
from datetime import datetime
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from matplotlib.pylab import rcParams

@user_bp.route('/arima', methods=['GET'])
def arima_time_series():
    df = pd.read_csv('household_power_consumption.txt', sep=';', parse_dates={'datetime': ['Date', 'Time']},
                     infer_datetime_format=True,
                     low_memory=False, na_values=['nan', '?'])
    df = df.set_index('datetime')

    # filling nan with mean in any column
    for j in range(0, len(df.columns)):
        df.iloc[:, j] = df.iloc[:, j].fillna(df.iloc[:, j].mean())
    # resampling
    df[:200].resample('30 s').interpolate(method='linear').head()
    dataset = df.resample('W').sum()[1:-1]
    rollingmean = dataset.rolling(window=14).mean()
    rollingstd = dataset.rolling(window=14).std()

    # users = UserService.get_all_users()
    # return jsonify(users), 200


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Implement other CRUD operations and routes