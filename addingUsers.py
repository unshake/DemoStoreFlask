from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Users, Products, ShoppingCart, Base

engine = create_engine('sqlite:///demostore_flask.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#----------Store items----------------

# Polo_Shirt

storeProduct1 = Products(name="Polo Shirt", id = "PS1", description = "Some polo type shirt", 
                     price = 10, size = "M", brand = "Nautica", color = "Navy" )

session.add(storeProduct1)
session.commit()

storeProduct2 = Products(name="Denim Jeans", id = "PS2", description = "Some denim jeans", 
                     price = 20, size = "32x32", brand = "GAP", color = "Blue" )

session.add(storeProduct2)
session.commit()





#-------------------Users Registration--------------------------
user1 = Users(name="Edgar Martinez", id = "monolet@hotmail.com", password = "monolet", carrito_total = 0)

session.add(user1)
session.commit()

user2 = Users(name="Rene Mejia", id="monolet@gmail.com", password="monolet", carrito_total=0)
session.add(user2)
session.commit()

