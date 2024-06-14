from sqlalchemy.orm import Session
import model

def create_customer(db: Session, first_name: str, last_name: str, email: str, password: str):
    new_customer = model.Customer(first_name=first_name, last_name=last_name, email=email, password=password)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def create_account(db: Session, customer_id: int, account_balance: float):
    new_account = model.Account(customer_id=customer_id, account_balance=account_balance)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def add_to_cart(db: Session, customer_id: int, product_id: int, quantity: int):
    new_item = model.ShoppingCart(customer_id=customer_id, product_id=product_id, quantity=quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def delete_from_cart(db: Session, cart_id: int):
    item = db.query(model.ShoppingCart).filter(model.ShoppingCart.cart_id == cart_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

def process_payment(db: Session, cart_id: int, payment_amount: float):
    new_transaction = model.Transaction(cart_id=cart_id, payment_amount=payment_amount)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction