from flask import Flask
from db import db
from apis.user_loan import blp as userLoanBluprint
from flask_smorest import Api


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTION"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///loan.db"
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()



    api.register_blueprint(userLoanBluprint)

    return app

