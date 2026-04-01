import flask
import random
import flask
from Project.db import DATA_BASE
from .models import User
from Project.config_page import config_page
import flask_login
from flask_mail import Message
from Project.settings import mail
from publish.models import Flat

def render_home():
    if flask_login.current_user.is_authenticated and flask_login.current_user.isAdmin:
        flats = Flat.query.all()
        flats_list = []
        # list_img = []
        for flat in flats:
            # img = flat.images.split("|")
            flats_list.append(flat)
        return flask.render_template("home.html", text= "hello, Lena", flats_list= flats_list)
    else:
        flats = Flat.query.all()
        flats_list = []
        # list_img = []
        for flat in flats:
            # img = flat.images.split("|")
            flats_list.append(flat)
        return flask.render_template("home.html", flats_list= flats_list)


def render_login():
    if flask.request.method == "POST":
        name = flask.request.form["username"]
        password = flask.request.form["password"]
        users = User.query.all()
        for user in users:
            if user.username == name and user.password == password:
                flask_login.login_user(user)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template("login.html")
    else:
        return flask.redirect("/")    


@config_page(name= "register.html", url= "/verify")
def render_register():
    message = ""
    if flask.request.method == 'POST':
        name = flask.request.form["username"]
        email = flask.request.form["email"]
        password = flask.request.form["password"]
        confirm_password = flask.request.form["confirm_password"]
        flask.session["name"] = name
        flask.session["email"] = email
        flask.session["password"] = password

        user_email = User.query.filter_by(email= email).first()
        if user_email is None :
            if password == confirm_password:


                #ПЕРВОЕ
                str_code = ''
                for num in range(6):
                    random_num = random.randint(0,9)
                    str_code += str(random_num)
                
                msg = Message(
                        'Hello',
                        recipients= [email],
                        sender="lenafedchenko07@gmail.com",
                        body=str_code
                    )
                # Отправляет созданное письмо через почтовый сервер, который ты настроила ранее.
                mail.send(msg)
                # пробуем перенаправить
                #ПЕРВОЕ

                # Эта строка сохраняет сгенерированный код в сессию пользователя, чтобы потом можно было его проверить.
                flask.session["verify_code"] = str_code

                message = "Успішно"
                
            else:
                message = "Паролі не співпадають"
        else:
            message = "Такий користувач вже існує"


    return {"message": message}

def logout():
    flask.session.clear()
    return flask.redirect("/")

def verify_code():
    if flask.request.method == 'POST':
        code = ''
        # добавляем начения из формы
        for num in flask.request.form.values():
            code += num
        if flask.session.get("verify_code") == code:
            user = User(
                    username = flask.session.get("name"),
                    email = flask.session.get("email"),
                    password = flask.session.get("password")
                )
            DATA_BASE.session.add(user)
            DATA_BASE.session.commit()
            return flask.redirect("/")

    return flask.render_template("verify.html")

def render_profile():
    if not flask_login.current_user.is_authenticated:
        return flask.redirect("/login")  # если не вошел, редирект на логин

    # # Данные для шаблона
    user_flats = User.query.filter_by(email = flask_login.current_user.email).first()
    flats_of_user = Flat.query.filter_by(owner_email = flask_login.current_user.email).all()
    print(flats_of_user)
    return flask.render_template("profile.html", user_flats= user_flats, flats_of_user= flats_of_user)