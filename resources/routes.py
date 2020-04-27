from .user import User, UserRegister, UserLogin, UserLogout, TokenRefresh
from .school import School, SchoolList
from .student import Student, StudentList


def initialize_routes(api):
    api.add_resource(Student, "/student/<int:_id>")
    api.add_resource(StudentList, "/students")
    api.add_resource(User, "/user/<string:username>")
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")
    api.add_resource(TokenRefresh, "/refresh")
    api.add_resource(School, "/school/<int:_id>")
    api.add_resource(SchoolList, "/schools")