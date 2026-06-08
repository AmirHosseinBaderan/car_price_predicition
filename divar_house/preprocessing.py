import pandas as pd
from utils import clean_price,extract_city,clean_bool

def preprocess(df:pd.DataFrame):
    #Price
    df["Price"] = df["Price"].apply(clean_price)
    
    # Bools 
    bool_cols = ["Warehouse", "Parking", "Elevator"]
    
    for col in bool_cols:
        df[col] = df[col].apply(clean_bool)
        
    
    # drop raw text
    df = df.drop(columns=["Address"])
    
    # Features
    X = df.drop(columns=["Price"])
    y = df["Price"]
        
    return X,y