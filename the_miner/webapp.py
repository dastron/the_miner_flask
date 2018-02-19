from flask import Flask, render_template, flash
from flask_login import LoginManager, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import flask_restless
import os
from config import config
from celery.schedules import crontab
from the_miner.celery_task import make_celery

# GLOBAL
global counter
counter = 0
global SensorAvg
SensorAvg = [0, 0, 0, 0, 0, 0]
global SensorGPIO
SensorGPIO = [5, 6, 13, 19, 26, 21]
global ChangeSense
ChangeSense = [0, 0, 0, 0, 0, 0]

config_name = os.getenv('BOILER_CONFIG', 'default')


def auth_func(*args, **kw):
    if not current_user.is_authenticated:
        raise ProcessingException(
            description='Not authenticated! Log in at http://localhost:5000/login', code=401)


# 1) create the flask application.
app = Flask(__name__)


app.config.from_object(config[config_name])

# 2) Set up the database. We can now import this anywhere.
database = SQLAlchemy(app)

# 3) Init Celery(app)
celery = make_celery(app)


# 4) Start Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# 5) Load App Blueprints
from the_miner.mod_miner.controllers import mod_miners as miner_module
from the_miner.mod_auth.controllers import mod_auth as auth_module

# 6) Register blueprint(s)
app.register_blueprint(miner_module)
app.register_blueprint(auth_module)

# Load User into


# @login_manager.user_loader
# def load_user(userid):
#     from the_miner.models import User
#     return User.query.get(userid)


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/secret')
@login_required
def secret():
    flash('Sending')
    return render_template('start.html')


@app.route('/h')
def heart():
    return 'alive'


@celery.task
def test(arg):
    print(arg)


@celery.task
def checkGPIO(arg):
    # from the_miner.service import poll_gpio
    from the_miner.service.google_sheets import fetch
    # poll_gpio()
    fetch()
    print(arg)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print('Loaded')

    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    sender.add_periodic_task(10.0, checkGPIO.s(
        'hello'), name='Check GPIO Status')


def setup_app(config_name, app, database):
    """
    # Creates a JSON:API compliant REST application.

    :param config_name str: String name of the config.
    :param app: The application.
    :param database: SQLAlchemy database.
    """

    # 0) Import models. SQLAlchemy requires this during app initialization.
    import models

    # 2) Set up CORS.
    CORS(app)

    # 3) Get JSON: API compliant endpoints, based on models.
    apimanager = flask_restless.APIManager(
        app,
        flask_sqlalchemy_db=database)

    apimanager.create_api(models.Miner, methods=['GET', 'POST', 'DELETE'])
    return apimanager


if __name__ == '__main__':
    app.run()
