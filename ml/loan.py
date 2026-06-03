from fastapi import FastAPI
import joblib

app = FastAPI()

model=joblib.load("Loan_approval_model.joblib")

@app.get("/")
def home():
    return {"message": "loan REJECT"}

# cd API
#  python -m uvicorn loan:app --reload