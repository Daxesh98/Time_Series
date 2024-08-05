# Time Series Forecasting with ARIMA Model**
==============================
ARIMA - Auto Regressive Integrated Moving Average

An ARIMA model is characterized by 3 terms: p, d, q
<br><br>
* **AR (p) Autoregression:** An auto regressive AR(p) term refers to the number of lags of Y to be used as predictors. In other words, the number of terms that are used from the past values in the time series for forecasting the future values. It's the part of the model that captures the relationship between a current observation and its predecessors. A high *p* value can indicate a strong influence of past values on current values.
<br><br>
* **I (d) Integration:** This parameter indicates the number of times the original time series data should be differenced to make it stationary. Stationarity is a critical aspect of time series analysis where the statistical properties of the series (mean, variance) do not change over time. Differencing is a method of transforming a non-stationary time series into a stationary one by subtracting the previous observation from the current observation. The *d* value helps in removing trends and seasonal structures from the time series, making it easier to model.
<br><br>
* **MA (q) Moving Average:**  ‘q’ is the order of the ‘Moving Average’ (MA) term. 'q' refers to the number of past errors (residuals) that are used to improve forecasts. The MA component models the relationship between an observation and a residual error from a moving average model applied to lagged observations. In simpler terms, it accounts for the influence of past prediction errors on the current observation. The errors referred to here are the differences between the actual values and the predictions that a simple moving average model would have made. The choice of *q* has a direct impact on how the ARIMA model predicts future values by considering how past errors influence current predictions. It helps in capturing the autocorrelation in the residuals of the series that is not explained by the autoregressive (AR) part.

### Model Types:

**ARIMA** - Non-seasonal auto regressive integrated moving average

**SARIMA** - Seasonal ARIMA

**SARIMAX** - Seasonal ARIMA with exogenous variable
A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
