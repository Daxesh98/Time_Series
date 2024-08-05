import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

def plot_lineplot(df):
    # Univariate analysis - We will only use 'Apple' variable.
    df = df.iloc[:-2, 0:2]

    # Set the 'Date' column as index
    df = df.set_index('Date')

    # Create seaborn lineplot
    plot = sns.lineplot(df['AAPL'])

    # Rotate x-axis labels
    plot.set_xticklabels(plot.get_xticklabels(), rotation=90)

    plt.show()

def plot_decomposition(df):
    # Set the 'Date' column as index
    df = df.set_index('Date')
    
    # Handle missing values
    df = df.dropna()

    # Decomposition
    decomposed = seasonal_decompose(df['AAPL'])

    trend = decomposed.trend
    seasonal = decomposed.seasonal
    residual = decomposed.resid

    # Plotting
    plt.figure(figsize=(12,8))
    plt.subplot(411)
    plt.plot(df['AAPL'], label='Original', color='black')
    plt.legend(loc='upper left')
    plt.subplot(412)
    plt.plot(trend, label='Trend', color='red')
    plt.legend(loc='upper left')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonal', color='blue')
    plt.legend(loc='upper left')
    plt.subplot(414)
    plt.plot(residual, label='Residual', color='black')
    plt.legend(loc='upper left')
    plt.show()
    
def plot_acf_pacf(df):   
    # for finding p,q using PACF and ACF plots respectively
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    plt.rcParams.update({'figure.figsize':(7,4), 'figure.dpi':80})

    # plot ACF
    plot_acf(df['AAPL'].dropna());

    # plot PACF
    plot_pacf(df['AAPL'].dropna(), lags=11);

    plt.show()
    
def plot_differenced_series(DS):
    # Plot the differenced series
    plt.plot(DS)
    plt.title('1st order differenced series')
    plt.xlabel('Date')
    plt.xticks(rotation=30)
    plt.ylabel('Price (USD)')
    plt.show()
    
def plot_model_performance(data, dp):
    # Plot
    dp['lower_int'] = pd.to_numeric(dp['lower_int'])
    dp['upper_int'] = pd.to_numeric(dp['upper_int'])
    
    # Plot actual values
    plt.plot(data['AAPL'], label='Actual')
    
    # Plot predicted values
    plt.plot(dp['price_predicted'], color='orange', label='Prediction')
    
    # Plot confidence intervals
    plt.fill_between(dp.index,
                     dp['lower_int'],
                     dp['upper_int'],
                     color='k', alpha=.15, label='Confidence Interval')

    plt.title('Model Performance')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend(loc='lower right')
    plt.xticks(rotation=30)
    plt.show()
    
    
def plot_model_performance_bivariate(data, dpx, lower_int, upper_int):
   
    #Plot the ARIMAX model performance.
    plt.figure(figsize=(12, 6))
    plt.plot(data['AAPL'], label='Actual')
    plt.plot(dpx['price_predicted'], color='orange', label='Forecasted')
    plt.fill_between(dpx.index, lower_int, upper_int, color='k', alpha=.15)
    
    plt.title('ARIMAX Model Performance')
    plt.legend(loc='lower right')
    plt.xlabel('Date')
    plt.xticks(rotation=30)
    plt.ylabel('Price (USD)')
    plt.show()