import flask

catalog = flask.Blueprint(
    name="catalog",
    import_name="catalog",
    template_folder="templates",
    static_folder="static",
    static_url_path="/catalog/static"
)