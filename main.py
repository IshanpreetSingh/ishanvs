from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

balance = 10000

@app.get("/balance")
def get_balance():
    return {"balance": balance}

@app.get("/deposit")
def deposit(amount: int = Query(..., ge=0)):
    global balance
    balance += amount
    return {"balance": balance}

@app.get("/withdraw")
def withdraw(amount: int = Query(..., ge=0)):
    global balance
    if amount > balance:
        raise HTTPException(status_code=400, detail="Not Enough funds!")
    balance -= amount
    return {"balance": balance}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
