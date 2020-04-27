from db import db
from typing import List


class SchoolModel(db.Model):
    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    students = db.relationship("StudentModel", lazy=True)

    @classmethod
    def find_all(cls) -> List["SchoolModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "SchoolModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

