from db import db
from ma import ma
from typing import List
from models.student import StudentSchema


class SchoolModel(db.Model):
    __table__ = "schools"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    students = db.relationship("StudentModel", lazy="dynamic")

    @classmethod
    def find_by_id(cls, _id:int) -> "SchoolModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["SchoolModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete()
        db.session.commit()


class SchoolSchema(ma.ModelSchema):
    students = ma.Nested(StudentSchema, many=True)

    class Meta:
        model = SchoolModel
        dump_only = ("id",)
        include_fk = True
