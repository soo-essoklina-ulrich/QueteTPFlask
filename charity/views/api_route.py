from flask import jsonify

from charity.data import projets
from charity import charity_api
from charity.controllers.categoriesController import CategorieController
from charity.controllers.projetController import projetController

categorie_controller = CategorieController()
projet_controller = projetController()


@charity_api.route('/data')
def index():
    return jsonify({"projets": projets})


@charity_api.route("/add-c", methods=["POST"])
def add_categories():
    return categorie_controller.create()


@charity_api.route("/list-c", methods=["GET"])
def list_categories():
    return categorie_controller.all()


@charity_api.route("/update-c", methods=["PUT"])
def update_categories():
    return categorie_controller.update()


@charity_api.route("/delete-c", methods=["DELETE"])
def delete_categories():
    return categorie_controller.delete()


@charity_api.route("/add-p", methods=["POST"])
def add_projet():
    return projet_controller.create()


@charity_api.route("/list-p", methods=["GET"])
def list_projet():
    return projet_controller.all()


@charity_api.route("/update-p", methods=["PUT"])
def update_projet():
    return projet_controller.update()


@charity_api.route("/delete-p", methods=["DELETE"])
def delete_projet():
    return projet_controller.delete()
