import flask
from Project.config_page import config_page
from .models import Product
from flask import request
from Project.db import DATA_BASE
import flask_login
import os

def render_catalog():
    categories = []
    page = request.args.get("page", 1, type= int)
    queryParam = request.args.get("category")
    query = Product.query
    if flask.request.method == "POST":
        if queryParam == "filter":
            category = request.form.get("categories")
            if category != "all":
                query = query.filter(Product.category == category)
            else:
                query = query.all()
    pagination = query.paginate(page=page, per_page=3)
    for product in Product.query.all():
        if product.category not in categories:
            categories.append(product.category)
    return flask.render_template("catalog.html", products=pagination.items, pagination= pagination, categories=categories)

def render_admin():
    if flask_login.current_user.is_authenticated and flask_login.current_user.isAdmin:
        page = request.args.get("page", 1, type= int)
        pagination = Product.query.paginate(page=page, per_page=3)
        if flask.request.method == "POST":
            city = flask.request.form["city"]
            product = Product.query.filter_by(city= city).first()
            if not product:
                image = flask.request.files["image"]
                image.save(os.path.abspath(os.path.join(__file__, "..", "static", "media", f"{image.filename}")))
                product = Product(
                    city= city, 
                    price = flask.request.form["price"],
                    old_price = flask.request.form["old_price"],
                    image_url = image.filename,
                    category = flask.request.form["category"],
                    distric = flask.request.form["distric"],
                    adress = flask.request.form["adress"],
                    floor = flask.request.form["floor"],
                    square = flask.request.form["square"],
                    rooms = flask.request.form["rooms"],
                    buy_rent = flask.request.form["buy_rent"],
                    owner = flask.request.form["owner"],
                    name_owner = flask.request.form["name_owner"],
                    email_owner = flask.request.form["email_owner"],
                    phone_owner = flask.request.form["phone_owner"]
                )
                DATA_BASE.session.add(product)
                DATA_BASE.session.commit()
        return flask.render_template("admin.html", products=pagination.items, pagination= pagination, text= "hello, Lena")
    else:
        return "404"
def delete_product():
    id = request.args.get(key= "id", type= int)
    product = Product.query.get(ident=id)
    if product:
        DATA_BASE.session.delete(product)
        DATA_BASE.session.commit()
    return flask.redirect("/admin/")

@config_page(name="product.html")
def render_product_by_id(id: int):
    product = Product.query.get(ident=id)
    return {
        "product": product
    }