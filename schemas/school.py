from ma import ma
from models.school import SchoolModel
from schemas.student import StudentSchema


class SchoolSchema(ma.ModelSchema):
    students = ma.Nested(StudentSchema, many=True)

    class Meta:
        model = SchoolModel
        dump_only = ("id",)
        include_fk = True