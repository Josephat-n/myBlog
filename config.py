import os

class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):   
   pass
   
class DevConfig(Config):  
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njoro:njoro@localhost/blog' 
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
