import os

from flask import Flask
from .models import db, User, Role
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mailman import Mail
from instance.config import config

migrate=Migrate()
csrf=CSRFProtect()
security=Security()
mail=Mail()
login_manager=LoginManager()

def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config['development'])
    else:
        # load the test config if passed in
        app.config.from_object(config['testing'])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app