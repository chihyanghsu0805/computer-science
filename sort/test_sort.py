"""Run Tests."""

from bubble_sort import bubble_sort

ARR = [5, 4, 3, 2, 1]


def test_bubble_sort():
    """Test Bubble Sort."""
    assert bubble_sort(ARR) == sorted(ARR)
