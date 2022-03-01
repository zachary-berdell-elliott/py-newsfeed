from flask import Flask
import os
from dotenv import load_dotenv

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
    
  return app
