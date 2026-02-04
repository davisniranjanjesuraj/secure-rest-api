from flask import Blueprint, request, jsonify
from app.models import User
from app.extensions import db
from flask_jwt_extended import create_access_token
from app.utils.validators import validate_user_payload
from app.utils.logger import logger

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if not validate_user_payload(data):
        return jsonify({"error": "Invalid input"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User exists"}), 409

    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    logger.info(f"User registered: {data['username']}")
    return jsonify({"message": "User created"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if not user or not user.check_password(data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    logger.info(f"User logged in: {user.username}")
    return jsonify(access_token=token)
