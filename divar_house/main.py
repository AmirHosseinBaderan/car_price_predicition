import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import median_absolute_error,mean_squared_error

from preprocessing import preprocess
from model import build_model
from utils import format_toman

#load data 
df = pd.read_csv("./houses_cleaned.csv",low_memory=False)
print("Dataset shape : ",df.shape)

print(df.head())

# clean + features
X,y = preprocess(df)

# train / test split 
x_train,x_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# scaling 
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# model
model = build_model()
model.fit(x_train,y_train)

# evaludation 
preds = model.predict(x_test)

mae = median_absolute_error(y_test,preds)
rmsa = np.sqrt(mean_squared_error(y_test,preds))

print("Results")
print(f"MAE : {mae}")
print(f"RMSA : {rmsa}")

# test
sample = pd.DataFrame([{
    "Area": 90,
    "Construction": 1393,
    "Room": 2,
    "Warehouse": 1,
    "Parking": 0,
    "Elevator": 1,
    "City_tehran": 1
}])

# aling cols 
sample = sample.reindex(columns=X.columns,fill_value=0)
sample = scaler.transform(sample)

price = model.predict(sample)

print(f"Predicted price : {format_toman(price[0])}")