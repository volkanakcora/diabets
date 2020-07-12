import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from warnings import filterwarnings

filterwarnings('ignore')

df = pd.read_csv("diabetes.csv")
df1 = df.copy()

y = df["Outcome"]
X = df.drop(["Outcome", "Pregnancies", "BloodPressure", "SkinThickness"], axis=1)

data = [[148],[0],[33.6],[0.627],[50]]
data = pd.DataFrame(data).T


def prediction(data):
    loj = LogisticRegression(solver="liblinear")
    loj_model = loj.fit(X, y)
    prediction = loj_model.predict(data)
    return prediction

# data = pd.DataFrame(data).T how the input should e-be
