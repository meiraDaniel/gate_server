from flaskapi import db


class Tour(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    tour_name = db.Column(db.String(20), unique=True, nullable=False)
    place = db.Column(db.String(20), nullable=False)
    activities = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    number_days = db.Column(db.Integer, nullable=False)
    number_people = db.Column(db.Integer, nullable=False, default=2)
    isSummer = db.Column(db.Boolean, nullable=False, default=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    sale = db.Column(db.Boolean, nullable=False, default=False)
    clients = db.relationship('Client', backref='tour', lazy=True)


    def __repr__ (self):
        return f"Tour ('{self.tour_name}', '{self.place}', '{self.image_file}')"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # def teste(self, filterList):
    #     teste_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #     return dict(filter(lambda elem: elem[0] not in filterList, teste_dict.items()))



class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    stars = db.Column(db.Integer, nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)


    def __repr__ (self):
        return f"Post ('{self.name}', '{self.stars}')"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# tour_1 = Tour(tour_name='Auckland Adventure', place='Auckland, New Zealand', activities='Skydive,Bungee Jump', price=580.99, number_days=2, number_people=1)
# tour_2 = Tour(tour_name='Auckland Vintage', place='Auckland, New Zealand', activities='City Tours,Wine Tasting,Food Tasting,Museums,Sailing', price=1450, number_days=4)
# tour_3 = Tour(tour_name='Wild Auckland', place='Auckland, New Zealand', activities='Surf,Hiking,Trails,Sailing,Camping,Ka', price=2320, number_days=5, number_people=4)
# tour_4 = Tour(tour_name='LOTR Basic', place='Rotorua, New Zealand', activities='City Tour,Hiking,Boat Rides,Trails,Food Tasting,Maori Culture', price=3135, number_days=6, number_people=4)
# tour_5 = Tour(tour_name='LOTR Premium', place='Rotorua, New Zealand', activities='City Tour,Trails,Climbing,Sailing,Maori Culture,Kayak,CampingWine Tasting,Food Tasting', price=4850, number_days=12, number_people=4)


# client_1 = Client(name='Ligia Souza', comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", stars=5,tour_id=1)
# client_2 = Client(name='Daniel Meira', comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", stars=5,tour_id=8)
# client_3 = Client(name='Joselito Inverts', comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", stars=4,tour_id=5)
# client_4 = Client(name='Frank Bruxels', comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", stars=5,tour_id=3)
# client_5 = Client(name='Taylor Swift', comment="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", stars=5,tour_id=7)

