from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db_session():
    db = None
    try:
        db = get_db()
        yield db
    finally:
        db.close()

@app.post("/customers/")
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db_session)):
    return crud.create_customer(db=db, **customer.dict())

@app.post("/accounts/")
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db_session)):
    return crud.create_account(db=db, **account.dict())

@app.post("/cart/")
def add_to_cart(cart_item: schemas.ShoppingCartCreate, db: Session = Depends(get_db_session)):
    return crud.add_to_cart(db=db, **cart_item.dict())


@app.post("/cart/delete")
def delete_from_cart(cart_id: int, db: Session = Depends(get_db_session)):
    success = crud.delete_from_cart(db=db, cart_id=cart_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}


@app.post("/payment/")
def process_payment(transaction: schemas.TransactionCreate, db: Session = Depends(get_db_session)):
    return crud.process_payment(db=db, **transaction.dict())
main.py