"""Chdir context manager."""

import contextlib
import os


@contextlib.contextmanager
def chdir(path: str):
    """_summary_.

    Args:
        path: _description_
    """
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    except Exception as exc:
        print("exc_type", repr(exc.__class__))
        print("exc_value", repr(exc))
        print("traceback", repr(exc.__traceback__))
    finally:
        os.chdir(cwd)


print("\nBefore context")
print(os.listdir())
with chdir(".."):
    print("\nInside context")
    print(os.listdir())
print("\nAfter context")
print(os.listdir())
