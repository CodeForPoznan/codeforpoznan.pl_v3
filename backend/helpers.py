import traceback
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr, contextmanager
from typing import Optional

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


def ask_for_temporary_mail() -> Optional[dict]:
    """
    Return dict with connection info for ethereal.mail or None if failed.
    """
    json = {"requestor": "nodemailer", "version": "6.5.0"}
    resp = requests.post("https://api.nodemailer.com/user", json=json)

    if resp.status_code == 200:
        data = resp.json()
        try:
            return {
                "MAIL_SERVER": data["smtp"]["host"],
                "MAIL_PORT": data["smtp"]["port"],
                "MAIL_USERNAME": data["user"],
                "MAIL_PASSWORD": data["pass"],
                "MAIL_WEB_URL": data["web"] + "/message/",
            }
        except KeyError:
            pass
