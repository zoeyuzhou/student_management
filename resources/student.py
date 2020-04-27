from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from models.student import StudentModel
from schemas.student import StudentSchema


student_schema = StudentSchema()
student_list_schema = StudentSchema(many=True)

class Student(Resource):
    @classmethod
    def get(cls, _id: str):
        student = StudentModel.find_by_id(_id)
        if student:
            return student_schema.dump(student), 200

        return {"message": "Student not found."}, 400

    @classmethod
#    @fresh_jwt_required
    def post(cls, _id: int):
        if StudentModel.find_by_id(_id):
            return {"message": "Student already exists."}, 400

        student_json = request.get_json()
#        student_json["id"] = _id

        student = student_schema.load(student_json)

        try:
            student.save_to_db()
        except:
            return {"message": "Errors on creating student."}, 500

        return student_schema.dump(student), 201

    @classmethod
    @jwt_required
    def delete(cls, _id: int):
        student = StudentModel.find_by_id(_id)
        if student:
            student.delete_from_db()
            return {"message": "Student is deleted."}, 200

        return {"message": "Student not found"}, 404

    @classmethod
    @fresh_jwt_required
    def put(cls, _id:int):
        student_json = request.get_json()
        student = student_schema.load(student_json)

        student = StudentModel.find_by_id(_id)
        if student:
            student = student_schema.load(student_json)

        student.save_to_db()
        return student_schema.dump(student), 200


class StudentList(Resource):
    @classmethod
    def get(cls):
        return {"students": student_list_schema.dump(StudentModel.find_all())}, 200



