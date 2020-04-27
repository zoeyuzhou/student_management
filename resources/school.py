from flask_restx import Resource
from models.school import SchoolModel
from schemas.school import SchoolSchema

school_schema = SchoolSchema()
school_schema_list = SchoolSchema(many=True)


class School(Resource):
    @classmethod
    def get(cls, _id: int):
        school = SchoolModel.find_by_id(_id)
        if school:
            return school_schema.dump(school), 200

        return {"message": "School Not Found."}, 404

    @classmethod
    def post(cls, _id: int):
        if SchoolModel.find_by_id(_id):
            return {"message": "School already exists."}, 400

        school_json = request.get_json()
        school = school_schema.load(school_json)
        try:
            school.save_to_db()
        except:
            return {"message": "Error in adding school"}, 500

        return school_schema.dump(school), 201

    @classmethod
    def delete(cls):
        pass


class SchoolList(Resource):
    @classmethod
    def get(cls):
        return {"schools": school_schema_list.dump(SchoolModel.find_all())}, 200