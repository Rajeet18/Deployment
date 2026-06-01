from fastapi import FastAPI
import joblib

app = FastAPI()

model=joblib.load("diabetes_model.joblib")

@app.get("/")
def home():
    return {"message": "loan API is Running"}

# cd API
#  python -m uvicorn loan:app --reload