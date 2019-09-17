from database_setup import User, Base, CategoryItem, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Jennie',
    email='JennieKone@gmail.com',
    picture='https://img.com/sdf'
)

session.add(user1)
session.commit()

category1 = Category(
    name='Snowboarding',
    user=user1
)

session.add(category1)
session.commit()

item1 = CategoryItem(
    name='Goggles',
    description='Famous Goggles mask to protect your eyes!',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name='Snowboard',
    description='To enjoy sliding on the snow!',
    category=category1,
    user=user1
)

session.add(item2)
session.commit()


category2 = Category(
    name='Soccer',
    user=user1
)

session.add(category2)
session.commit()

item1 = CategoryItem(
    name='Two shinguards',
    description='Shinguards!',
    category=category2,
    user=user1
)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name='Soccer cleats',
    description='for soccer only!',
    category=category2,
    user=user1
)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name='Jersey',
    description=' A football team!',
    category=category2,
    user=user1
)

session.add(item3)
session.commit()

category3 = Category(
    name='Baseball',
    user=user1
)

session.add(category3)
session.commit()

item1 = CategoryItem(
    name='Bat',
    description='a baseball ball!',
    category=category3,
    user=user1
)

session.add(item1)
session.commit()

category4 = Category(
    name='Basketball',
    user=user1
)

session.add(category4)
session.commit()

category5 = Category(
    name='Frisbee',
    user=user1
)

session.add(category5)
session.commit()

item1 = CategoryItem(
    name='Frisbee',
    description='a Frisbee ball!',
    category=category5,
    user=user1
)

session.add(item1)
session.commit()

category6 = Category(
    name='Hockey',
    user=user1
)

session.add(category6)
session.commit()

item1 = CategoryItem(
    name='Stick',
    description='a Hockey stick!',
    category=category6,
    user=user1
)

session.add(item1)
session.commit()

print('Finished populating the database!')