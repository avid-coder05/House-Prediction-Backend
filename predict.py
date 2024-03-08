import pandas as pd
from sklearn.linear_model import Lasso
from joblib import load

model=load("model.joblib")
neigh=["Suburb", "Rural", "Urban"]

def predict_price(data):

    for i in data.keys():
        data[i] = [data[i]]

    df = pd.DataFrame(data)

    for i in range(3):
        df.insert(2+i, neigh[i], int(neigh[i] == df["Neighborhood"][0]))

    df.drop("Neighborhood", axis=1, inplace=True)

    pred = model.predict(df)
    return pred[0]