from flask import Flask, render_template, redirect, request, jsonify
from flask_login import LoginManager, login_user
from flask_wtf.csrf import CSRFProtect
import datetime
from data import db_session
from data.user import User
from  forms.loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'R27yufghz1321'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
csrf = CSRFProtect()
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/homeworks.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    main()
