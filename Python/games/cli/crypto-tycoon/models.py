from SQLalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from SQLalchemy.orm import relationship
from SQLalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable = False, unique = True)
    balance = Column(Float(), nullable = False, default = 0)
    acquired_assets_id = Column(ForeignKey("acquired_assets.id"), nullable = False)

class AquiredAsset(Base):
    __tablename__ = 'acquired_assets'
    id = Column(Integer(), primary_key = True)
    asset_id = Column(ForeignKey("assets.id"), nullable = False)
    account_id = Column(ForeignKey("accounts.id"), nullable = False)
    quantity = Column(Integer(), nullable = False, default = 0)

class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable = False, unique = True)

class Market(Base):
    __tablename__ = 'markets'
    id = Column(Integer(), primary_key = True)
    asset_id = Column(ForeignKey("assets.id"), nullable = False)
    price = Column(Float(), nullable = False, default = 0)
    