from functools import wraps

import flask, flask_login

def config_page(name: str, url: str = None):
    def render_template(function: object):
        @wraps(function)
        def processor(*args, **kwargs):
            context: dict = function(*args, **kwargs)
            if isinstance(context, flask.Response):
                return context
            if context.get("message") == "Successfully" and url:
                return flask.redirect(url)
            return flask.render_template(
                template_name_or_list= name,
                current_user= flask_login.current_user,
                **context
            )
        return processor
    return render_template
