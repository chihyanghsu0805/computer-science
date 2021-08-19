"""Run Tests."""
from __future__ import absolute_import, print_function

from array_list import ArrayList
from hash_table import HashTable


def test_hashtable():
    """Test HashTable."""
    ht1 = HashTable()
    ht1.add("a", "apple")
    assert ht1.get("a") == "apple"

    ht2 = HashTable()
    ht2["a"] = "apple"
    assert ht2["a"] == "apple"


def test_arraylist():
    """Test ArrayList."""
    arr = ArrayList()
    assert arr.max_size == 2
    assert arr.current_size == 0

    arr.add(1)
    arr.add(1.1)
    arr.add(-1)
    assert arr.max_size == 4
    assert arr.current_size == 3

    assert arr.get(1) == 1.1
    arr.delete(1)
    assert arr.current_size == 2
    assert arr.array == [1, -1, None, None]
