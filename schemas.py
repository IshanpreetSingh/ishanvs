from pydantic import BaseModel

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class CustomerCreate(CustomerBase):
    pass

class AccountBase(BaseModel):
    customer_id: int
    account_balance: float

class AccountCreate(AccountBase):
    pass

class ShoppingCartBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int

class ShoppingCartCreate(ShoppingCartBase):
    pass

class TransactionBase(BaseModel):
    cart_id: int
    payment_amount: float

class TransactionCreate(TransactionBase):
    pass