from extensions import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    desciption = db.Column(db.String(255), nullable=False)
