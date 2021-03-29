import re

import requests
from flask import Flask, Response
from flask import jsonify
from flask import request
from hashlib import sha256

from server import server
from relationDB.models import db
from relationDB.repositories.userRepository import UserRepository
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# ADMIN_MODULE_ADDRESS = "http://backend:5000/admin/"
# CATALOG_MODULE_ADDRESS = "http://backend:5000/"


# @server.route('/admin/<path:path>', methods=["POST", "GET"])
# @jwt_required()
# def admin_access(path):
#     current_identity = get_jwt_identity()
#     user_role = UserRepository.get_user_role(current_identity)
#     if user_role.role_name == "admin":
#         if request.method == 'GET':
#             headers = {'content-type': 'application/json'}
#             resp = requests.get(f'{ADMIN_MODULE_ADDRESS}{path}', params=request.args, headers=headers)
#             excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#             headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#             response = Response(resp.content, resp.status_code, headers)
#             return response
#         if request.method == 'POST':
#             resp = requests.post(f'{ADMIN_MODULE_ADDRESS}{path}', json=request.get_json())
#             excluded_headers = ['content - encoding', 'content - length', 'transfer - encoding', 'connection']
#             headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#             response = Response(resp.content, resp.status_code, headers)
#             return response
#     else:
#         return jsonify({"msg": "go away from here"}), 401
#
#
# @server.route('/catalog/<path:path>', methods=["GET"])
# @jwt_required()
# def catalog_access(path):
#     current_identity = get_jwt_identity()
#     user_role = UserRepository.get_user_role(current_identity)
#     if user_role.role_name == "user" or user_role.role_name == "admin":
#         if request.method == 'GET':
#             resp = requests.get(f'{CATALOG_MODULE_ADDRESS}{path}', params=request.args)
#             excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#             headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#             response = Response(resp.content, resp.status_code, headers)
#             return response
#     else:
#         return jsonify({"msg": "go away from here"}), 401

BACKEND_ADDRESS = "http://backend:5000/"
CART_ADDRESS = "http://cart:5000/"
ORDER_ADDRESS = "http://order:5000/"


@server.route('/catalog/<path:path>', methods=["POST", "GET"])
@jwt_required()
def catalog_access(path):
    current_identity = get_jwt_identity()
    headers = get_headers_with_user_id_and_role_from_identity(current_identity)

    return redirect_method(BACKEND_ADDRESS + "/catalog/", path, headers)


@server.route('/admin/<path:path>', methods=["POST", "GET"])
@jwt_required()
def admin_access(path):
    current_identity = get_jwt_identity()
    headers = get_headers_with_user_id_and_role_from_identity(current_identity)

    return redirect_method(BACKEND_ADDRESS + "/admin/", path, headers)


@server.route('/cart/<path:path>', methods=["POST", "GET"])
@jwt_required()
def cart_access(path):
    current_identity = get_jwt_identity()
    headers = get_headers_with_user_id_and_role_from_identity(current_identity)

    return redirect_method(CART_ADDRESS + "/cart/", path, headers)


@server.route('/order/<path:path>', methods=["POST", "GET"])
@jwt_required()
def order_access(path):
    current_identity = get_jwt_identity()
    headers = get_headers_with_user_id_and_role_from_identity(current_identity)

    return redirect_method(ORDER_ADDRESS + "/order/", path, headers)


def get_headers_with_user_id_and_role_from_identity(current_identity) -> {}:
    user_role = UserRepository.get_user_role(current_identity)
    user = UserRepository.get_user_by_login(current_identity)
    return {'x-user-role': user_role.role_name, 'x-user-id': user.id}


def redirect_method(server_address, url_path, headers) -> Response:
    if request.method == 'GET':
        resp = requests.get(server_address + url_path, params=request.args, headers=headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    if request.method == 'POST':
        resp = requests.post(server_address + url_path, params=request.args, json=request.get_json(), headers=headers)
        excluded_headers = ['content - encoding', 'content - length', 'transfer - encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response


@server.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username is not None and password is not None:
        if UserRepository.compare_user_pass(username, password):
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
        UserRepository.create_new_user(username, password, role)
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