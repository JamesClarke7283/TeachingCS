from models import Base, Account
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Create a database engine, specify the database type and the path to the database file
engine = create_engine('sqlite:///crypto_tycoon.db', echo=False)

# Create a session which will be used to interact with the database, and it binds to the engine
Session = sessionmaker(bind=engine)

# Create the database tables for all the models
Base.metadata.create_all(engine)


def init_account(session, name="John Doe"):
    user = session.query(Account).filter_by(name=name).first()
    if user is None:
        user = Account(name=name, balance=1000)
        session.add(user)
        session.commit()
    return user


def main():
    with Session() as session:
        init_account(session)


if __name__ == "__main__":
    main()
