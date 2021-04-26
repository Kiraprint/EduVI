from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import datetime

import homeworks_resources
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'R27yufghz1321'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
api = Api(app)
# для списка объектов
api.add_resource(homeworks_resources.HomeworksListResources, '/api/v2/homeworks')
# для одного объекта
api.add_resource(homeworks_resources.HomeworkResources, '/api/v2/news/<int:homeworks_id>')

def main():
    db_session.global_init("db/homeworks.db")
    app.run()


if __name__ == '__main__':
    main()
