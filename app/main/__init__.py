from flask import Blueprint
main = Blueprint ('main', __name__)
from . import views

def create_app(config_name):
   app=Flask(__name__)
   
   #create the app configuration
   app.config.from_object(config_options[config_name])
   
   #Registrering the blueprint
   from . main import main as main_blueprint
   app.register_blueprint(main_blueprint)
   
   return app 