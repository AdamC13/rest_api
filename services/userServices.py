from sqlalchemy.orm import Session
from database import db
from models.user import User
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token

# Create a function that takes in customer data and creates a new customer in db
def save(customer_data):
    # Open a session
    with Session(db.engine) as session:
        with session.begin():
            # Create a new instance of Customer
            new_customer = User(username=customer_data['username'], role=customer_data['role'], password=generate_password_hash(customer_data['password']))
            # Add and commit to the database
            session.add(new_customer)
            session.commit()
        # After committing the session, the new_customer object may have become detatched
        # Refresh the object to ensure it is still attached to the session
        session.refresh(new_customer)
        return new_customer
    
def fetch_all(page=1, per_page=10):
    query = select(User).offset((page-1) * per_page).limit(per_page)
    customers = db.session.execute(query).scalars().all()
    return customers

def get_token(username, password):
    # Query the customer table for that username
    query = db.select(User).where(User.username == username)
    customer = db.session.execute(query).scalars().first()
    if customer is not None and check_password_hash(customer.password, password):
        # Create a token with the customer's id
        auth_token = encode_token(customer.id)
        return auth_token
    else:
        return None