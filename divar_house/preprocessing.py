import pandas as pd
from utils import clean_price,extract_city

def preprocess(df:pd.DataFrame):
    #Price
    df["Price"] = df["Price"].apply(clean_price)
    
    # Bools 
    bool_cols = ["Warehouse", "Parking", "Elevator"]
    
    for col in bool_cols:
        df[col] = df[col].astype(int)
        
    # city 
    df["City"] = df["City"].apply(extract_city)
    
    # drop raw text
    df = df.drop(columns=["Address"])
    
    # Features
    X = df.drop(columns=["Price"])
    y = df["Price"]
    
    # one-hot encode city
    X = pd.get_dummies(X,columns=["City"],drop_first=True)
    
    return X,y