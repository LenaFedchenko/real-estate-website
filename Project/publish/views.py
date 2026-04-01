import flask, os
from Project.db import DATA_BASE
from .models import Flat
import flask_login


def render_publish():
    if flask_login.current_user.is_authenticated:
        if flask.request.method == "POST":
            try:
                city = flask.request.form["city"]
                district = flask.request.form["district"]
                address = flask.request.form["address"]
                floor = flask.request.form["floor"]
                area = flask.request.form["area"]
                price = flask.request.form["price"]

                property_type = flask.request.form["property_type"]
                rooms = flask.request.form["rooms"]

                deal_type = flask.request.form["deal_type"]
                owner_type = flask.request.form["owner_type"]

                owner_name = flask.request.form["owner_name"]
                owner_phone = flask.request.form["owner_phone"]
                owner_email = flask.request.form["owner_email"]

                images = flask.request.files.getlist("images")
                # print(images)
                path = os.path.abspath(os.path.join(__file__, "..", "static", "images", "media"))
                imgs = ""
                for file in images:
                    if file.filename != "":
                        file.save(f"{path}/{file.filename}")
                        imgs+= "|" + file.filename

                post_flat = Flat(
                    city= city,
                    district= district,
                    address= address,
                    floor= floor,
                    area= area,
                    price= price,
                    property_type= property_type,
                    rooms=rooms,
                    deal_type= deal_type,
                    owner_type= owner_type,
                    owner_name= owner_name,
                    owner_phone= owner_phone,
                    owner_email= owner_email,
                    images= imgs
                )
                DATA_BASE.session.add(post_flat)
                DATA_BASE.session.commit()
                return flask.redirect("/")
            except:
                error_text = "Заповніть усі поля"
                return flask.render_template("publish.html", error_text= error_text)
        else:
            return flask.render_template("publish.html")
    else:
        text_registration = "Щоб викласти нерухомість зареєструйтесь або увійдіть у акаунт"
        return flask.render_template("publish.html", text= text_registration)