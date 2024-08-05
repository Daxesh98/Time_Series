import statsmodels
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(df):
    
    print("Statsmodels version:", statsmodels.__version__)
    
    # ARIMA Model with order (1,1,1)
    arima = ARIMA(df['AAPL'], order=(1,1,1))
    ar_model = arima.fit()
    
    # Print summary of the model
    print(ar_model.summary())
    
    return ar_model