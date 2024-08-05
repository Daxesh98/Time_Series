import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from src.data.make_dataset import load_data
from src.visualization.visualize import plot_lineplot, plot_decomposition, plot_acf_pacf,plot_differenced_series,plot_model_performance, plot_model_performance_bivariate
from statsmodels.tsa.stattools import adfuller
from src.models.train_model import train_arima_model
from src.models.forecast_model import forecast_arima_model,create_prediction_dataframe


if __name__=="__main__":
    #Load Data
    data_path = "data\\raw\\AAPL.csv"
    df =load_data(data_path)
    
    # Print the dataset
    print(df.head())

    # Plot Lineplot
    plot_lineplot(df)
    
    # Plot Decomposition
    plot_decomposition(df)
    
    # Plot ACF and PACF
    plot_acf_pacf(df)


    # Perform ADF test
    results = adfuller(df['AAPL'].dropna())  # Drop NaN values if any
    print('p-value:', results[1])
    print('Critical Values:', results[4])
    
    # 1st order differencing
    v1 = df['AAPL'].diff().dropna()

    # adf test on the new series. if p value < 0.05 the series is stationary
    results1 = adfuller(v1)
    print('p-value:', results1[1]) # adf, pvalue, usedlag_, nobs_, critical_values_, icbest_
    
   
    # Plot the differenced series
    plot_differenced_series(v1)
    
    # the mean for above series is
    (v1.values).mean()
    
        # Train ARIMA model
    ar_model = train_arima_model(df)
    
    
# Forecasting
    ypred, conf_int = forecast_arima_model(ar_model, steps=2)
    print("Forecasted values:\n", ypred)
    print("Confidence intervals:\n", conf_int)
    
        # Create DataFrame with forecasted values and confidence intervals
    dp = create_prediction_dataframe(ypred, conf_int)
    print("Prediction DataFrame:\n", dp)
    
    df = df.set_index('Date')
    
    dp.index = pd.to_datetime(dp.index)
    # Plot Model Performance
    plot_model_performance(df, dp)    
    
    