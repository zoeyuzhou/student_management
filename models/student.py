from db import db
from typing import List
from ma import ma


class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(80), nullable=False)
    given_name = db.Column(db.String(80), nullable=False)

    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), nullable=False)
    school = db.relationship("SchoolModel")

    @classmethod
    def find_all(cls) -> List["StudentModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "StudentModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = StudentModel
 #       dump_only = ("id",)
        load_only = ("id",)