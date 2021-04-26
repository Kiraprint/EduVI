import sqlalchemy
from sqlalchemy import orm
import datetime

from data.db_session import SqlAlchemyBase


class Homework(SqlAlchemyBase):
    __tablename__ = 'homeworks'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    subject = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    task = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    post_date = sqlalchemy.Column(sqlalchemy.Date, default=datetime.datetime.now())
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("teachers.id"))
    grade_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("grade_id"))

    grade = orm.relation('Grade')
    teacher = orm.relation('Teacher')
