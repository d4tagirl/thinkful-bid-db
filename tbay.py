from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://Daniela@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, desc

class Item(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String)
  start_time = Column(DateTime, default=datetime.utcnow)

  bids = relationship("Bid", backref="items")
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class User(Base):
  __tablename__ = "users"
    
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)

  bids = relationship("Bid", backref="users")
  items = relationship("Item", backref="users")


class Bid(Base):
  __tablename__ = "bids"
    
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  price = Column(Float, nullable=False)

  item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


Base.metadata.create_all(engine)

# Checking

lola = User(username="lola", password="lalala")
john = User(username="john", password="jojo")
suzy = User(username="suzy", password="jeje")
baseball = Item(name="baseball", users=lola)
bid_john = Bid(username="john", password="jojo", price=15, items=baseball, users=lola)
bid_suzy = Bid(username="suzy", password="jeje", price=12, items=baseball, users=lola)

session.add_all([lola, john, suzy, baseball, bid_john, bid_suzy])
session.commit()

our_user = session.query(Bid).order_by(desc("price")).first()

print("The highest bid was from "+our_user.username+" and he ofered "+str(our_user.price)+" dollars.")