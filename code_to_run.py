from tbay import User, Item, Bid, session

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
session.add(beyonce)

patricia = User(username="paty", password="lola")
session.add(patricia)

session.commit()

# Returns a list of all of the user objects
# Note that user objects won't display very prettily by default -
# you'll see their type (User) and their internal identifiers.

session.query(User).all() # Returns a list of all of the user objects

# Returns the first user
session.query(User.username).first()

# Finds the user with the primary key equal to 1
session.query(User).get(1)

# Returns a list of all of the usernames in ascending order
session.query(User.username).order_by(User.username).all()

# # Returns the description of all of the basesballs
# session.query(Item.description).filter(Item.name == "baseball").all()

# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
# session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()

# updating a row
user = session.query(User).first()
user.username = "solange"
session.commit()


user = session.query(User).filter(User.password == "lola").first()
user.username = "jess"
session.commit()

# Deleting rows

user = session.query(User).first()
session.delete(user)
session.commit()