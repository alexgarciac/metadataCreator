from flask import Flask

appl = Flask(__name__)
appl.config.from_object('config')

from app import views
