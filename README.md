# Flask Backend for House Price Prediction

This is a simple python program which has the following files with the specified functionalities:
- data.py: It serves as the main flask file. It routes the backend to port 5000 of the localhost (if running on local).
- login.py: It serves as the "database" for the backend. It has two functions add_cred and check_cred.
  - add_cred: It adds a username, password pair to the database.
  - check_cred: It checks whether the passed username, password pair are present in the database or not.
- model.joblib; It is a ML model trained on the dataset hosuing_price_dataset.csv.
- ml_model.py: It is the python code for developing model.joblib ML model.
- predict.py: It takes the model.joblib ML model and uses it to predict the house pricing for the input dataset (examples).

---

## Expected Inputs

The backend expects inputs for the following functions as follows:
- For adding credentials, a json formatted data consisting of username, password and login keys are required. Login key is supposed to be 0 for adding credentials.
- For checking credentials, a json formatted data consisting of username, password and login keys are required. Login key is supposed to be 1 for checking credentials.
- For predicting the price of a house, a json formatted data should consist of SquareFeet, Bedrooms, Neighborhood and Bathrooms keys.

---

## Expected Outputs
The backend return the following json formatted responses:
- It returns login key with value True for successful addition of credentials and correct credentials.
- It returns login key with value False for incorrect credentials.
- It returns Prediction key with the value as the predicted house price.

---

The dataset housing_price_dataset.csv has been obtained from [kaggle](https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data). All credit for the dataset belongs to the rightful creator.
