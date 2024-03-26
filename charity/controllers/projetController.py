from urllib import request

from flask import jsonify
from sqlalchemy.testing import db

from charity.models import projet

class projetController:
    def __init__(self):
        self.projet_model = projet

    def create(self):
        try:
            data = request.get_json()
            nouveau_projet = self.projet_model(libelle=data['libelle'], description=data['description'], categorie_id=data['categorie_id'], image=data['image'])
            db.session.add(nouveau_projet)
            db.session.commit()
            return jsonify({' message': 'Nouveau projet créé avec succès'}), 201
        except KeyError:
            return jsonify({' message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        projets = self.projet_model.query.all()
        return jsonify([projet.serialize() for projet in projets]), 200

    def update(self):
        try:
            data = request.get_json()
            projet = self.projet_model.query.filter_by(id=data['id']).first()
            projet.libelle = data['libelle']
            projet.description = data['description']
            projet.categorie_id = data['categorie_id']
            db.session.commit()
            return jsonify({'message': 'Projet mis à jour avec succès'}), 200
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self):
        try:
            data = request.get_json()
            projet = self.projet_model.query.filter_by(id=data['id']).first()
            db.session.delete(projet)
            db.session.commit()
            return jsonify({'message': 'Projet supprimé avec succès'}), 200
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500