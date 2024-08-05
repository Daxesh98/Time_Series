import pandas as pd



def load_data(data_path):
    df = pd.read_csv(data_path)
    
    print("Print Head",df.head())
    
    print("Data Shape",df.shape)
    
    print("Check data type",df.dtypes)
    
    # Convert 'Date' to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Check the datatype
    print(df.dtypes)
    
    return df