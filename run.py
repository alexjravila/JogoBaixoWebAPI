from app import create_app

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    "https://2f2ee0c9056b413a8523f41f9621af99@sentry.io/1493413",
    integrations=[FlaskIntegration()],
)


create_app().run(host='0.0.0.0', port=5000, debug=True)