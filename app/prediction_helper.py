import pandas as pd
from joblib import load

model_rest=load("artifacts\model_rest.joblib")
model_young=load("artifacts\model_young.joblib")

scaler_rest=load("artifacts\scaler_rest.joblib")
scaler_young=load("artifacts\scaler_young.joblib")


def predict():
    pass