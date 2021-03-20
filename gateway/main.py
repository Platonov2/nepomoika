import re

import requests
from flask import Flask, Response
from flask import jsonify
from flask import request
from hashlib import sha256

from server import server
from relationDB.models import db
from relationDB.repositories.userRepository import create_new_user, get_user_by_login, get_user_role
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

SITE_NAME = "http://backend:5000/"


@server.route('/admin/<path:path>', methods=["POST", "GET"])
@jwt_required()
def admin_access(path):
    current_identity = get_jwt_identity()
    user_role = get_user_role(current_identity)
    if user_role.role_name == "admin":
        if request.method == 'GET':
            resp = requests.get(f'{SITE_NAME}{path}', params=request.args)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
        if request.method == 'POST':
            resp = requests.post(f'{SITE_NAME}{path}', json=request.get_json())
            excluded_headers = ['content - encoding', 'content - length', 'transfer - encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
    else:
        return jsonify({"msg": "go away from here"}), 401


@server.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username is not None and password is not None:
        user = get_user_by_login(username)
        if user.password == sha256(password.encode('utf-8')).hexdigest():
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        return jsonify({"msg": "Wrong username or password"}), 401
    return jsonify({"msg": "Bad username or password"}), 401


@server.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    role = request.json.get("role", None)
    if username is not None and password is not None:
        if role is None:
            role = "user"
        create_new_user(username, password, role)
        return jsonify({"msg": "succ"}), 200

    return jsonify({"msg": "Bad username or password"}), 401


@server.route("/test", methods=["GET"])
@jwt_required()
def optionally_protected():
    current_identity = get_jwt_identity()
    if current_identity:
        return jsonify(logged_in_ass=current_identity)
    else:
        return jsonify({"msg": "go away from here"}), 401


if __name__ == "__main__":
    db.create_all()
    server.run(host='0.0.0.0', port=5000)