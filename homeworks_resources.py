from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data import db_session
from data.homework import Homework


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('is_published', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)


def abort_if_homework_not_found(homework_id):
    session = db_session.create_session()
    homework = session.query(Homework).get(homework_id)
    if not homework:
        abort(404, message=f"Homework {homework_id} not found")


class HomeworkResources(Resource):
    def get(self, homework_id):
        abort_if_homework_not_found(homework_id)
        session = db_session.create_session()
        news = session.query(Homework).get(homework_id)
        return jsonify({'news': news.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, homework_id):
        abort_if_homework_not_found(homework_id)
        session = db_session.create_session()
        homework = session.query(Homework).get(homework_id)
        session.delete(homework)
        session.commit()
        return jsonify({'success': 'OK'})

class HomeworksListResources(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(Homework).all()
        return jsonify({'news': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        homework = Homework(
            subject=args['subject'],
            task=args['task'],
            teacher_id=args['teacher_id'],
            grade_id = args["grade_id"]
        )
        session.add(homework)
        session.commit()
        return jsonify({'success': 'OK'})