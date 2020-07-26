import joblib
import json
import numpy as np

global model
global columns
model=joblib.load("model/house_price_model")
print(model)

with open("model/columns.json",'r') as f:
    columns=json.loads(f.read())
print(len(columns["columns"]))


def get_loc():
    return columns["columns"][3:]

def estimate(data):
    x=np.zeros(len(columns["columns"]))
    x[0]=data[1]
    x[1]=data[3]
    x[2]=data[2]
    try:
        x[columns["columns"].index(data[0].lower())]=1
    except:
        pass
    return str(model.predict([x])[0])

print(estimate(['indira nagar',1000,2,2]))


