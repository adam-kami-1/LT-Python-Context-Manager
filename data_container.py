"""Simple data container."""


class DataContainer:
    """_summary_.

    Args:
        name: Name of the text file used to store data.
    """

    DataType = dict[int, str]

    def __init__(self, name: str):
        """Create DataContainer object."""
        self._name = name
        self._data: DataContainer.DataType = {}

    def load(self):
        """Load container data from file."""
        try:
            with open(self._name, mode="r", encoding="utf8") as file:
                for line in file:
                    key, value = line.split(maxsplit=1)
                    self.add_entry(int(key), value[0:-1])
        except FileNotFoundError:
            # Ignore missing file
            pass

    def save(self):
        """Save container data to file."""
        with open(self._name, mode="w", encoding="utf8") as file:
            for _key, _value in self._data.items():
                print(F"{_key} {_value}", file=file)

    def add_entry(self,
                  key: int,
                  value: str) -> None:
        """_summary_.

        Args:
            key: Entry key.
            value: Entry value
        """
        self._data[key] = value

    def __str__(self) -> str:
        """_summary_."""
        res = ""
        for _key, _value in self._data.items():
            res += F"{_key}: {_value!r}\n"
        return res
