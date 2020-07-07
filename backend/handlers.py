import os
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

from flask_migrate import migrate
from serverless_wsgi import handle_request

import app.create_app


def api(event, context):
    event["headers"]["Host"] = os.environ["BASE_URL"]
    print("REQUEST: ", event)
    return handle_request(app.create_app(), event, context)


def migration(event, context):
    stdout = StringIO()
    stderr = StringIO()

    with redirect_stderr(stderr):
        with redirect_stdout(stdout):
            migrate()

    return {
        "stdout": stdout.getvalue(),
        "stderr": stderr.getvalue(),
    }
