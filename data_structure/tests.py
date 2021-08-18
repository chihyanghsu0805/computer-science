"""Run Tests."""
from __future__ import absolute_import, print_function

from hash_table import HashTable


def test_hashtable():
    """Test HashTable."""
    ht1 = HashTable()
    ht1.add("a", "apple")
    assert ht1.get("a") == "apple"

    ht2 = HashTable()
    ht2["a"] = "apple"
    assert ht2["a"] == "apple"
