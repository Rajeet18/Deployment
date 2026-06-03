from fastapi import FastAPI
import joblib

app = FastAPI()

model=joblib.load("Loan_approval_model.joblib")

@app.get("/")
def home():
    return {"message": "loan approval for yes or no"}

# cd API
#  python -m uvicorn loan:app --reload