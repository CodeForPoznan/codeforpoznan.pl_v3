import os
import sys
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

from flask_migrate import init, stamp, migrate, upgrade
from serverless_wsgi import handle_request

from backend.app import create_app


def api(event, context):
    event["headers"]["Host"] = os.environ["BASE_URL"]
    print("REQUEST: ", event)
    return handle_request(create_app(), event, context)


def migration(event, context):
    out, err = wrap_io(migrate)

    if "Please use the 'init' command" in err:
        wrap_io(init)
        out, err = wrap_io(migrate)

    if "Target database is not up to date" in err:
        wrap_io(stamp)
        wrap_io(migrate)
        out, err = wrap_io(upgrade)

    return {"stdout": out, "stderr": err}


# TODO: rewrite as contextmanager?
def wrap_io(fn: callable) -> (str, str):
    out = StringIO()
    err = StringIO()

    # noinspection PyBroadException
    try:
        with redirect_stderr(err):
            with redirect_stdout(out):
                with create_app().app_context():
                    print(f"Running {fn.__name__}")
                    fn()

    # catch-all case for potential SystemExit(1)
    except BaseException:
        pass

    out = out.getvalue()
    err = err.getvalue()

    # print captured outputs
    sys.stdout.write(f"stdout: {out}")
    sys.stderr.write(f"stderr: {err}")

    # a cheap state caching trick, but does the job
    wrap_io._out = getattr(wrap_io, "_out", "") + out
    wrap_io._err = getattr(wrap_io, "_err", "") + err
    out, err = wrap_io._out, wrap_io._err

    return out, err
