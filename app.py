from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
from blacklist import BLACKLIST
from resources.student import Student, StudentList
from resources.school import School, SchoolList
from resources.user import User, UserRegister, UserLogin, UserLogout, TokenRefresh

app = Flask(__name__)
# app.config.from_object('config.Config')

sqllite_str = "sqlite:///data.db"
'''


local_mysql_str = "mysql+pymysql://zoe:Passmy1!@127.0.0.1:3306/STUDENT_SYSTEM"
'''
app.config["SQLALCHEMY_DATABASE_URI"] = sqllite_str
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["PROPAGATE_EXCEPTION"] = True
app.config["JWT_BLACKLIST_ENABLE"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]

app.secret_key = "zhouz"


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


api.add_resource(Student, "/student/<int:_id>")
api.add_resource(StudentList, "/students")
api.add_resource(User, "/user/<string:username>")
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(School, "/school/<int:_id>")
api.add_resource(SchoolList, "/schools")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
