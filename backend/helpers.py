import traceback
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr, contextmanager


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
