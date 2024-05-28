from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pydantic import BaseModel
from typing import List

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

balance = 10000
transactions = []  


class Transaction(BaseModel):
    date: datetime
    account_number: str
    amount: int
    type: str


class TransactionResponse(BaseModel):
    transactions: List[Transaction]


class TransactionRequest(BaseModel):
    amount: int

@app.get("/balance")
def get_balance():
    return {"balance": balance}

@app.get("/transactions", response_model=TransactionResponse)
def get_transactions():
    return {"transactions": transactions}

@app.get("/deposit")
def deposit(amount: int = Query(..., ge=0)):
    global balance
    global transactions
    balance += amount
    transaction = Transaction(
        date=datetime.now(),
        account_number="708886389",  
        amount=amount,
        type="CR"  
    )
    transactions.append(transaction)
    return {"balance": balance}

@app.get("/withdraw")
def withdraw(amount: int = Query(..., ge=0)):
    global balance
    global transactions
    if amount > balance:
        raise HTTPException(status_code=400, detail="Not Enough funds!")
    balance -= amount
    transaction = Transaction(
        date=datetime.now(),
        account_number="708886389",  
        amount=amount,
        type="DR" 
    )
    transactions.append(transaction)
    return {"balance": balance}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
