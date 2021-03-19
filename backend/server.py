from flask import Flask
import os
from flask_cors import CORS

server = Flask(__name__)
cors = CORS(server, resources={r"/*": {"origins": "*"}}) #127.0.0.1 gateway
server.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + os.environ["POSTGRES_USER"] + \
                                           ":" + os.environ["POSTGRES_PASSWORD"] + "@" + os.environ["POSTGRES_HOST"] \
                                           + ":" + os.environ["POSTGRES_PORT"] + "/" + os.environ["POSTGRES_DB"]
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

