from flask import Blueprint, jsonify
from user_service import get_users

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify({"users": users})
