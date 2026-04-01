from Project.db import DATA_BASE


class Flat(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key= True)
    city = DATA_BASE.Column(DATA_BASE.String(50), nullable= False)
    district = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    address = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    floor = DATA_BASE.Column(DATA_BASE.Integer, default=False)
    area = DATA_BASE.Column(DATA_BASE.Integer, default=False)
    price = DATA_BASE.Column(DATA_BASE.Integer, default=False)
    property_type = DATA_BASE.Column(DATA_BASE.String, default=False)
    rooms = DATA_BASE.Column(DATA_BASE.Integer, default=False)
    deal_type = DATA_BASE.Column(DATA_BASE.String, default=False)
    owner_type = DATA_BASE.Column(DATA_BASE.String, default=False)
    owner_name = DATA_BASE.Column(DATA_BASE.String(15), default=False)
    owner_phone = DATA_BASE.Column(DATA_BASE.Integer, default=False)
    owner_email = DATA_BASE.Column(DATA_BASE.String, default=False)
    images = DATA_BASE.Column(DATA_BASE.String, default=False)
    describe = DATA_BASE.Column(DATA_BASE.String, default=False)