"""Create HashTable Class."""
# https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/

from __future__ import absolute_import, print_function

from typing import Any


class HashTable(object):
    """Create HashTable Class.

    Args:
        object ([type]): object.
    """

    def __init__(self, length: int = 2):
        """Initialize class.

        Args:
            length (int, optional): length of array. Defaults to 2.
        """
        self.array = [None] * 4

    def __setitem__(self, key: str, value: any):
        """Set item.

        Args:
            key (str): input key.
            value (any): input value.
        """
        self.add(key, value)

    def __getitem__(self, key: str) -> any:
        """Get item.

        Args:
            key (str): inpute key.

        Returns:
            any: value.
        """
        return self.get(key)

    def hash(self, key: str) -> int:
        """Compute hash index for key.

        Args:
            key (str): input key.

        Returns:
            int: hash index
        """
        length = len(self.array)
        return hash(key) % length

    def add(self, key: str, value: Any) -> None:
        """Add key and value to hash table.

        Args:
            key (str): input key.
            value (Any): input value.
        """
        index = self.hash(key)
        if self.array[index] is not None:

            for kvp in self.array[index]:

                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])

        else:
            self.array[index] = []
            self.array[index].append([key, value])

        if self.is_full():
            self.double()

    def get(self, key: str) -> Any:
        """Get value from HashTable with key.

        Args:
            key (str): input key.

        Raises:
            KeyError: key is not in HashTable.
            KeyError: key is not in HashTable.

        Returns:
            Any: value.
        """
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for k, v in self.array[index]:
                if k == key:
                    return v

            raise KeyError()

    def is_full(self) -> bool:
        """Determine whether array reaches half capacity to avoid collision.

        Returns:
            bool: True if array is half capacity, otherwise False.
        """
        count = 0
        for i in self.array:
            if i:
                count += 1

        return count == len(self.array) / 2

    def double(self) -> None:
        """Double the array size."""
        array_length = len(self.array)
        ht2 = HashTable(length=array_length * 2)
        for i in range(array_length):
            if not self.array[i]:
                continue
            for k, v in self.array[i]:
                ht2.add(k, v)
        self.array = ht2
