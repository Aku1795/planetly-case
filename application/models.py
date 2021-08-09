import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class TemperatureByTimeAndCity(db.Model):
    __tablename__ = 'temperatures_by_time_and_city'
    date = db.Column(db.DateTime)
    avg_temperature = db.Column(db.Float)
    avg_temperature_uncertainty = db.Column(db.Float)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.String(100))