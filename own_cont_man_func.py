"""Context manager for data container implemented with generator function."""

import typing
import contextlib
from data_container import DataContainer


ExceptionValue = typing.Optional[BaseException]


@contextlib.contextmanager
def data_container(name: str):
    """Context manager for data container.

    Args:
        name: Name of the text file used by DataContainer.

    Raises:
        exc_value: _description_

    Yields:
        _description_
    """
    exc_value: ExceptionValue = None
    data = DataContainer(name)
    data.load()
    print(str(data))
    try:
        yield data
    except ValueError:
        pass
    except Exception as exc:
        print("exc_type", repr(exc.__class__))
        print("exc_value", repr(exc))
        print("traceback", repr(exc.__traceback__))
        exc_value = exc
    finally:
        print(str(data))
        data.save()
    if exc_value:
        raise exc_value


with data_container("test2-func.txt") as obj:
    while True:
        entry_key = int(input("Enter integer key: "))
        entry_value = input("Enter value (not empty line of text): ")
        assert entry_value, "Invalid value"
        obj.add_entry(entry_key, entry_value)
