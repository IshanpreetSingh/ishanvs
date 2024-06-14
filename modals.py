from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 
from database import Base

class Customer(Base):
    _tablename_ = "Customer"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    password = Column(String(100))

class Account(Base):
    _tablename_ = "Account"
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_id'))
    account_balance = Column(DECIMAL(10, 2))

    customer = relationship("Customer", back_populates="accounts")

class Product(Base):
    _tablename_ = "Product"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100))
    unit_price = Column(DECIMAL(10, 2))

class ShoppingCart(Base):
    _tablename_ = "ShoppingCart"
    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_id'))
    product_id = Column(Integer, ForeignKey('Product.product_id'))
    quantity = Column(Integer)

    customer = relationship("Customer", back_populates="shopping_carts")
    product = relationship("Product")

class Transaction(Base):
    _tablename_ = "Transaction"
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('ShoppingCart.cart_id'))
    payment_amount = Column(DECIMAL(10, 2))
    transaction_date = Column(TIMESTAMP, server_default=func.now())

    shopping_cart = relationship("ShoppingCart", back_populates="transactions")
model.py