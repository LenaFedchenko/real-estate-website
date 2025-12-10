import flask, flask_login

def config_page(name: str, redirect_to: str = ""):
    def render_template(function: object):
        def processor(*args, **kwargs):
            context = function(*args, **kwargs)
            if context["message"] == "Успішно":
                return flask.redirect(redirect_to)
            return flask.render_template(
                template_name_or_list= name,
                current_user= flask_login.current_user,
                **context
            )
        return processor
    return render_template
