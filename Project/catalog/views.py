import flask
from Project.config_page import config_page
from publish.models import Flat
from flask import request
from Project.db import DATA_BASE
import flask_login
import os

def render_catalog():
    cities = []
    page = request.args.get("page", 1, type=int)
    selected_city = request.args.get("city", "all")

    # новые параметры
    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)

    if min_price is not None and min_price < 0:
        min_price = 0

    if max_price is not None and max_price < 0:
        max_price = 0

    if min_price is not None and max_price is not None and min_price > max_price:
        min_price, max_price = max_price, min_price

    query = Flat.query

    # фильтр по городу
    if selected_city != "all":
        query = query.filter(Flat.city == selected_city)

    # фильтр по цене
    if min_price is not None:
        query = query.filter(Flat.price >= min_price)

    if max_price is not None:
        query = query.filter(Flat.price <= max_price)

    pagination = query.paginate(page=page, per_page=5)

    filter_args = {}
    if selected_city != "all":
        filter_args["city"] = selected_city
    if min_price is not None:
        filter_args["min_price"] = min_price
    if max_price is not None:
        filter_args["max_price"] = max_price

    # список уникальных городов
    for flat in Flat.query.all():
        if flat.city not in cities:
            cities.append(flat.city)

    return flask.render_template(
        "catalog.html",
        products=pagination.items,
        pagination=pagination,
        categories=cities,
        selected_city=selected_city,
        min_price=min_price,
        max_price=max_price,
        filter_args=filter_args
    )

def render_admin():
    if flask_login.current_user.is_authenticated and flask_login.current_user.isAdmin:
        page = request.args.get("page", 1, type=int)
        pagination = Flat.query.paginate(page=page, per_page=5)

        if flask.request.method == "POST":
            city = flask.request.form["city"]
            flat = Flat.query.filter_by(city=city).first()
            if not flat:
                images = flask.request.files.getlist("images")  # Поддержка нескольких файлов
                image_names = []
                for image in images:
                    save_path = os.path.abspath(
                        os.path.join(__file__, "..", "static", "media", image.filename)
                    )
                    image.save(save_path)
                    image_names.append(image.filename)

                flat = Flat(
                    city=city,
                    district=flask.request.form.get("district"),
                    address=flask.request.form.get("address"),
                    floor=flask.request.form.get("floor"),
                    area=flask.request.form.get("area"),
                    price=flask.request.form.get("price"),
                    property_type=flask.request.form.get("property_type"),
                    rooms=flask.request.form.get("rooms", 0),
                    deal_type=flask.request.form.get("deal_type"),
                    owner_type=flask.request.form.get("owner_type", ""),
                    owner_name=flask.request.form.get("owner_name", ""),
                    owner_phone=flask.request.form.get("owner_phone", ""),
                    owner_email=flask.request.form.get("owner_email", ""),
                    images="|".join(image_names)
                )
                DATA_BASE.session.add(flat)
                DATA_BASE.session.commit()

        return flask.render_template(
            "admin.html",
            products=pagination.items,
            pagination=pagination,
            text="hello, Lena"
        )
    else:
        return "404"

def delete_product():
    if not (flask_login.current_user.is_authenticated and flask_login.current_user.isAdmin):
        return flask.redirect("/login/")

    id = request.args.get("id", type=int)
    flat = Flat.query.get(id)
    if flat:
        DATA_BASE.session.delete(flat)
        DATA_BASE.session.commit()
    return flask.redirect("/admin/")

@config_page(name="product.html")
def render_product_by_id(id: int):
    flat = Flat.query.get(id)
    return {
        "message": "Successfully",
        "product": flat
    }
