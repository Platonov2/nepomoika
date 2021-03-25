from flask import Flask
import os
from flask_cors import CORS

server = Flask(__name__)
cors = CORS(server, resources={r"/*": {"origins": "*"}})
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

