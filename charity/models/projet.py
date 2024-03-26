from extensions import db


class Projet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    categorie = db.relationship('Categories', backref=db.backref('projet', lazy=True))
