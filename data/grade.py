import sqlalchemy
from sqlalchemy import orm
import datetime

from data.db_session import SqlAlchemyBase


class Grade(SqlAlchemyBase):
    __tablename__ = 'grades'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    association_table = sqlalchemy.Table(
        'association',
        SqlAlchemyBase.metadata,
        sqlalchemy.Column('user', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('users.id')),
        sqlalchemy.Column('grades', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('grades.id'))
    )