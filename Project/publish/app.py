import flask

publish = flask.Blueprint(
    name= 'publish',
    import_name= 'publish',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/publish/static'
)