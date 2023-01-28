# python libs
from flask import Flask
from dotenv import load_dotenv
from os import getenv

# app modules
from src.utils.environment import EnvironmentWrapper

# app configs
from src.modules.config.production import ProductionConfig
from src.modules.config.development import DevelopmentConfig

# create app instance
app = Flask(__name__)
with EnvironmentWrapper('SECRET_KEY') as _sk:
    app.config['secret_key'] = _sk

# init app config
if (not app.debug):
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# run views
import src.views