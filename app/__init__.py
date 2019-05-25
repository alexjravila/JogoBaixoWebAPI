from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import app_foo
    app.register_blueprint(app_foo, url_prefix="/foo")

    return app