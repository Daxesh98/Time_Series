import pandas as pd

def forecast_arima_model(ar_model, steps=2):
    
    # Forecasting
    forecast = ar_model.get_forecast(steps=steps)
    ypred = forecast.predicted_mean
    conf_int = forecast.conf_int(alpha=0.05)
    
    return ypred, conf_int

def create_prediction_dataframe(ypred, conf_int):
    # creating a new Dataframe dp with the prediction values.
    Date = pd.Series(['2024-01-01', '2024-02-01'])
    price_actual = pd.Series(['184.40','185.04'])
    price_predicted = pd.Series(ypred.values)
    lower_int = pd.Series(conf_int['lower AAPL'].values)
    upper_int = upper_series = pd.Series(conf_int['upper AAPL'].values)

    dp = pd.DataFrame([Date, price_actual, lower_int, price_predicted, upper_int], index =['Date','price_actual', 'lower_int', 'price_predicted', 'upper_int']).T
    dp = dp.set_index('Date')
    dp.index = pd.to_datetime(dp.index)
    return dp
