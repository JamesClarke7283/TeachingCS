from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import argparse

# Create a database engine, specify the database type and the path to the database file
engine = create_engine('sqlite:///example.db', echo=False)

# Create a session which will be used to interact with the database, and it binds to the engine
Session = sessionmaker(bind=engine)

# Create a base class for the models, which will be used to create the database tables
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, email='{self.email}')>"


# Create the database tables for all the models
Base.metadata.create_all(engine)


def get_id_by_email(email):
    """Gets the ID of a user by their email
    We first create a session object, which will be used to interact with the database.
    We then get the user object from the database.
    Finally, we close the session, which will release the resources used by the session.
    """
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    session.close()
    return user.id


def add_user(name, age, email):
    """Adds new users to the database
    We first create a session object, which will be used to interact with the database.
    We then create a new user object, and add it to the session.
    We then commit the session, which will save the changes to the database.
    Finally, we close the session, which will release the resources used by the session.
    """
    session = Session()
    user = User(name=name, age=age, email=email)
    session.add(user)
    session.commit()
    session.close()


def update_user(email_address, new_name=None, new_age=None, new_email=None):
    """Updates existing users in the database
    We first create a session object, which will be used to interact with the database.
    We then get the user object from the database, and update the attributes.
    We then commit the session, which will save the changes to the database.
    Finally, we close the session, which will release the resources used by the session.
    """
    id = get_id_by_email(email_address)
    session = Session()
    user = session.query(User).get(id)
    if name:
        user.name = new_name
    if age:
        user.age = new_age
    if email:
        user.email = new_email
    session.commit()
    session.close()


def delete_user(email_address):
    id = get_id_by_email(email_address)
    session = Session()
    user = session.query(User).get(id)
    session.delete(user)
    session.commit()
    session.close()


parser = argparse.ArgumentParser(description='Interact with a database of users')
parser.add_argument('--add', nargs=3, metavar=('name', 'age',
                    'email'), help='Add a new user to the database')
parser.add_argument('--update', nargs='+', metavar=('email_address'),
                    help='Update an existing user in the database')
parser.add_argument('--delete', nargs=1, metavar=('email_address'),
                    help='Delete an existing user from the database')
parser.add_argument('--list', action='store_true',
                    help='List all users in the database')

args = parser.parse_args()

if args.add:
    add_user(*args.add)

if args.update:
    email_address = args.update[0]
    updates = args.update[1:]
    name = age = email = None
    for update in updates:
        key, value = update.split('=')
        if key == 'name':
            name = value
        elif key == 'age':
            age = int(value)
        elif key == 'email':
            email = value
    update_user(email_address, name=name, age=age, email=email)

if args.delete:
    delete_user(args.delete[0])

if args.list:
    session = Session()
    users = session.query(User).all()
    for user in users:
        print(user)
    session.close()
