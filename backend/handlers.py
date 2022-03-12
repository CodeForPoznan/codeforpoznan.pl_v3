import os

from flask_migrate import init, stamp, upgrade
from serverless_wsgi import handle_request

from backend.app import create_app
from backend.helpers import wrap_io


def api(event, context):
    event["headers"]["Host"] = os.environ["BASE_URL"]
    print("REQUEST: ", event)
    return handle_request(create_app(), event, context)


def migration(event, context):
    with create_app().app_context():
        # db commands can exit with os.exit(1) - we _have_ to catch that
        with wrap_io(catch=BaseException) as (out, err):

            upgrade()

            if "Please use the 'init' command" in err():
                init()
                upgrade()

            if "Target database is not up to date" in err():
                stamp()
                upgrade()

    return {"stdout": out(), "stderr": err()}
