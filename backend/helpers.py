import traceback
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr, contextmanager

import requests


@contextmanager
def wrap_io(catch=Exception) -> (callable, callable):
    """
    Capture stdout and stderr in the current process.
    Will release the captured handles on `__exit__`.
    Returns two functions for getting the values of streams.
    """
    out, err = StringIO(), StringIO()

    # noinspection PyBroadException
    try:
        with redirect_stderr(err):
            with redirect_stdout(out):
                yield out.getvalue, err.getvalue
    except catch:
        err.write(traceback.format_exc())


def ask_for_temporary_mail():
    json = {"requestor": "nodemailer", "version": "6.5.0"}
    resp = requests.post("https://api.nodemailer.com/user", json=json)

    if resp.status_code != 200:
        return {}

    data = resp.json()
    return {
        "server": data["smtp"]["host"],
        "port": data["smtp"]["port"],
        "username": data["user"],
        "password": data["pass"],
        "web_server": data["web"] + "/message/",
    }
