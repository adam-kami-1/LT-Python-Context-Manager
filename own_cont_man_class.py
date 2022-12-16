"""Context manager for data container implemented with class."""

import typing
import types
from data_container import DataContainer


ExceptionType = typing.Optional[typing.Type[BaseException]]
ExceptionValue = typing.Optional[BaseException]
TracebackType = typing.Optional[types.TracebackType]


class DataContainerSession:
    """Context manager for data container.

    Args:
        name: Name of the text file used by DataContainer.
    """

    def __init__(self, name: str):
        """Construct context manager."""
        self.data = DataContainer(name)

    def __enter__(self) -> 'DataContainer':
        """Context manager entry point."""
        self.data.load()
        print(str(self.data))
        return self.data

    def __exit__(self,
                 exc_type: ExceptionType,
                 exc_value: ExceptionValue,
                 traceback: TracebackType) -> bool:
        """Context manager exit point.

        Args:
            exc_type: _description_
            exc_value: _description_
            traceback: _description_

        Returns:
            True if exception in with body should be ignored.
            False if exception should be reraised.
        """
        # Free/close resources
        print(str(self.data))
        self.data.save()
        # Serve exception
        if exc_type is ValueError:
            return True
        if exc_type:
            print("exc_type", repr(exc_type))
            print("exc_value", repr(exc_value))
            print("traceback", repr(traceback))
        return False


with DataContainerSession("test2-class.txt") as obj:
    while True:
        entry_key = int(input("Enter integer key: "))
        entry_value = input("Enter value (not empty line of text): ")
        assert entry_value, "Invalid value"
        obj.add_entry(entry_key, entry_value)
