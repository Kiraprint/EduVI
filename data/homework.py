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

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    grade_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("grades.id"))
    grade = orm.relation('Grade')
