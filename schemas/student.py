from ma import ma
from models.student import StudentModel


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = StudentModel
        dump_only = ("id",)
#        load_only = ("school",)
        include_fk = True