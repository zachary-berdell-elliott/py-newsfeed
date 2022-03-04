from app.routes import home, dashboard
from flask import Flask
import os
from dotenv import load_dotenv
from app.db import init_db

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY=os.getenv('SECRET')
  )

  @app.route('/hello')
  def hello():
    return 'hello world'

  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  init_db(app)
    
  return app
