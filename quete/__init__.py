from flask import Blueprint, jsonify
from quete.data import projets

quete_bp = Blueprint('quete', __name__)


@quete_bp.route("/data", methods=['GET'])
def get_data():
    return jsonify({'data': projets})
