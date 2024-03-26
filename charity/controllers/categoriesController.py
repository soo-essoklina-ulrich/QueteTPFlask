from urllib import request

from flask import jsonify
from sqlalchemy.testing import db

from charity.models import categories


class CategorieController:
    def __init__(self):
        self.categories_model = categories

    def create(self):
        try:
            data = request.get_json()
            nouvelle_categorie = self.categories_model(libelle=data['libelle'])
            db.session.add(nouvelle_categorie)
            db.session.commit()
            return jsonify({' message': 'Nouvelle catégorie créée avec succès'}), 201
        except KeyError:
            return jsonify({' message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        categories = self.categories_model.query.all()
        return jsonify([categorie.serialize() for categorie in categories]), 200

    def update(self):
        try:
            data = request.get_json()
            categorie = self.categories_model.query.filter_by(id=data['id']).first()
            categorie.libelle = data['libelle']
            db.session.commit()
            return jsonify({'message': 'Catégorie mise à jour avec succès'}), 200
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self):
        try:
            data = request.get_json()
            categorie = self.categories_model.query.filter_by(id=data['id']).first()
            db.session.delete(categorie)
            db.session.commit()
            return jsonify({'message': 'Catégorie supprimée avec succès'}), 200
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
