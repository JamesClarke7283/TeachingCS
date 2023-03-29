from models import Base, Account, Asset, Market, AcquiredAsset
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import exit
from random import randint
# Create a database engine, specify the database type and the path to the database file
engine = create_engine('sqlite:///crypto_tycoon.db', echo=False)

# Create a session which will be used to interact with the database, and it binds to the engine
Session = sessionmaker(bind=engine)

# Create the database tables for all the models
Base.metadata.create_all(engine)


def init_account(session, name="John Doe"):
    user = session.query(Account).filter_by(name=name).first()
    if user is None:
        user = Account(name=name, balance=10000)
        session.add(user)
        session.commit()
    return user


def init_crypto_assets(session):
    if session.query(Asset).count() == 0:
        a1 = Asset(name="Bitcoin")
        a2 = Asset(name="Monero")
        a3 = Asset(name="Etherium")

        session.add_all([a1, a2, a3])
        session.commit()

def init_markets(session):
    if session.query(Market).count() == 0:
        m1 = Market(asset_id=1, price=1000)
        m2 = Market(asset_id=2, price=100)
        m3 = Market(asset_id=3, price=500)
        session.add_all([m1, m2, m3])
        session.commit()

def randomize_prices(session):
    market_assets = session.query(Market).all()
    for asset in market_assets:
        asset.price = randint(1, 10000)
    session.commit()


class UserInterface:

    def __init__(self, session, account):
        self.option_selected = None
        self.session = session
        self.account = account

    def main_menu(self):
        print(f"Balance: ${self.account.balance}")
        print("(1) Buy")
        print("(2) Sell")
        print("(3) View portfolio")
        print("(4) Quit")
        self.option_selected = int(input("Enter your choice: "))
        match self.option_selected:
                case 1:
                    self.buy_asset()
                case 2:
                    self.sell_asset()
                case 3:
                    self.view_portfolio(self.account)
                case 4:
                    print("Bye!")
                    exit(0)

    def _asset_menu(self, is_buy=True):
        asset_state = "Buy" if is_buy else "Sell"
        assets = self.session.query(Asset).all()
         
        for asset in assets:
            market_asset = self.session.query(Market).filter_by(asset_id=asset.id).first()
            print(f"{asset.id}. {asset_state} {asset.name}: Price:\t${market_asset.price}")
        count = self.session.query(Asset).count()
        print(f"{count+1}. Exit")
        self.option_selected = int(input("Enter your choice: "))
    
    def buy_asset(self):
        self._asset_menu(is_buy=True)
        asset_bought = self.session.query(Asset).filter_by(id=self.option_selected).first()
        if asset_bought is not None:
            market = self.session.query(Market).filter_by(asset_id=asset_bought.id).first()
            if market is not None:
                print(f"Price: {market.price}")
                quantity = int(input("Enter quantity: "))
                if self.account.balance >= market.price * quantity:
                    self.account.balance -= market.price * quantity
                    acquired_asset = self.session.query(AcquiredAsset).filter_by(account_id=self.account.id, asset_id=asset_bought.id).first()
                    if acquired_asset is not None:
                        acquired_asset.quantity += quantity
                    else:
                        acquired_asset = AcquiredAsset(account_id=self.account.id, asset_id=asset_bought.id, quantity=quantity)
                        self.session.add(acquired_asset)
                    self.session.commit()
                    print("Transaction successful")
                else:
                    print("Insufficient balance")
        self.selected_option = None
    
    def sell_asset(self):
        self._asset_menu(is_buy=False)
        asset_sold = self.session.query(Asset).filter_by(id=self.option_selected).first()
        if asset_sold is not None:
            acquired_asset = self.session.query(AcquiredAsset).filter_by(account_id=self.account.id, asset_id=asset_sold.id).first()
            if acquired_asset is not None:
                market = self.session.query(Market).filter_by(asset_id=asset_sold.id).first()
                if market is not None:
                    self.account.balance += market.price * acquired_asset.quantity
                    self.session.delete(acquired_asset)
                    self.session.commit()
                    print("Transaction successful")
        self.option_selected = None
    
    def view_portfolio(self, account: Account):
        acquired_asset = self.session.query(AcquiredAsset).filter_by(account_id=account.id).all()
        print("Assets")
        print("=" * 20)
        for asset in acquired_asset:
            print(f"{asset.asset.name}: {asset.quantity}")
        print("=" * 20)


def main():
    while True:
        with Session() as session:
            account = init_account(session)
            init_crypto_assets(session)
            init_markets(session)
            ui = UserInterface(session, account)
            if ui.option_selected is None:
                ui.main_menu()
            randomize_prices(session)


if __name__ == "__main__":
    main()
