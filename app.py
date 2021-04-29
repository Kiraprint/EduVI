import datetime

from flask import Flask, render_template, redirect, abort
from flask_login import LoginManager, login_user
from flask_wtf.csrf import CSRFProtect

from data import db_session
from data.user import User
from forms.loginform import LoginForm

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
    if form.is_submitted():
        if form.submitl.data and all(map(lambda x: x.data, (form.emaill, form.passwordl))):
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect("/")
            return render_template('login.html', message="Incorrect login or password", form=form)

        elif form.submit.data and all(map(lambda x: x.data,
                                          (form.email, form.name, form.surname,
                                           form.password, form.password_again))):
            if form.password.data != form.password_again.data:
                return render_template('login.html',
                                       form=form,
                                       message="Match the passwords")
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('login.html',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = User(
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            login_user(user)
            return redirect("/")
        else:
            abort(404)

    return render_template('login.html', form=form)


if __name__ == '__main__':
    main()
