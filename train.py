import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv('Spend_Data.csv')

X = data[['Age', 'Gender', 'Income']]
y = data['MonthlySpend']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'spend_model.pkl')
print("Model saved successfully.")