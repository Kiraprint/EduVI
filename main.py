from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
import datetime
'''
import homeworks_resources
app.config['SECRET_KEY'] = 'R27yufghz1321'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
api = Api(app)
# для списка объектов
api.add_resource(homeworks_resources.HomeworksListResources, '/api/v2/homeworks')
# для одного объекта
api.add_resource(homeworks_resources.HomeworkResources, '/api/v2/news/<int:homeworks_id>')
'''
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'R27yufghz1321'

def main():
    # db_session.global_init("db/homeworks.db")
    app.run()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    main()
