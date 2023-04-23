"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)

@api.route("/token", methods=['POST'])
def generate_toke():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    mail = User.query.filter_by(username=username, password=password).first()
    if user is None:
        return jsonify({"msg": "Wrong email or password"}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(create_access_token=access_token)

@api.route('/hello', methods=['GET'])
@jwt_required()
def handle_hello():
    email = get_jwt_identity()
    return f"Welcome, {email}"