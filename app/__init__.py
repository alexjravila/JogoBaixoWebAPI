from connexion.resolver import RestyResolver
import connexion

def create_app(test_config=None):
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('swagger.yml')

    return app