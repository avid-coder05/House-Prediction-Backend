import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from joblib import dump

df=pd.read_csv("housing_price_dataset.csv")
suburb=df["Neighborhood"]=="Suburb"
rural=df["Neighborhood"]=="Rural"
urban=df["Neighborhood"]=="Urban"
suburb=suburb.astype(int)
rural=rural.astype(int)
urban=urban.astype(int)

df.drop("Neighborhood", axis=1, inplace=True)
df.drop("YearBuilt", axis=1, inplace=True)
df.insert(2, "Suburb", 0)
df.insert(3, "Rural", 0)
df.insert(4, "Urban", 0)

df["Suburb"]=df["Suburb"]|suburb
df["Rural"]=df["Rural"]|rural
df["Urban"]=df["Urban"]|urban

x=df.drop("Price", axis=1)
y=df["Price"]

x_tra,x_tst,y_tra,y_tst=train_test_split(x, y, test_size=0.1, random_state=42)

model_1=Lasso(alpha=220)
model_1.fit(x_tra, y_tra)

dump(model_1, "model.joblib")