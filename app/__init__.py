from flask import Flask
from app.models import db, Fooditems
from app.routes.routes import routes_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)

    with app.app_context():

        app.register_blueprint(routes_bp)

        db.create_all()

    return app
