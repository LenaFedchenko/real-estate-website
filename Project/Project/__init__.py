from .urls import *
from .settings import *
from .db import*
from .loadenv import execute
from home.models import User
# add registration blueprint
from .config_page import config_page
from .loginmanager import *




project.register_blueprint(blueprint= home.home)
project.register_blueprint(blueprint= publish.publish)
project.register_blueprint(blueprint= catalog.catalog)