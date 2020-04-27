from flask import Flask, jsonify
from flask_restx import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
from blacklist import BLACKLIST
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_object('config.Config')

api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmellow_validation(err):
    return jsonify(err.message), 400


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token("jti") in BLACKLIST


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    initialize_routes(api)
    app.run(port=5000, debug=True)
