from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app.extensions import db

user_bp = Blueprint("users", __name__)

@user_bp.route("/me", methods=["GET"])
@jwt_required()
def profile():
    user_id = int(get_jwt_identity())  
    user = db.session.get(User, user_id)

    return jsonify({
        "id": user.id,
        "username": user.username
    })
