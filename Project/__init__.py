from .urls import *
from .settings import project



project.register_blueprint(blueprint= home.home)
project.register_blueprint(blueprint= publish.publish)