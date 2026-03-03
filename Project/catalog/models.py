from Project.db import DATA_BASE

class Product(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key= True)
    city = DATA_BASE.Column(DATA_BASE.String(100), nullable=False)
    price = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    old_price = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    image_url = DATA_BASE.Column(DATA_BASE.String(100), nullable=False)
    category = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    distric = DATA_BASE.Column(DATA_BASE.String(500), nullable=False)
    adress = DATA_BASE.Column(DATA_BASE.String(500), nullable=False)
    floor = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    square = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    rooms = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    buy_rent = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    owner = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    name_owner = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    email_owner = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    phone_owner = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
