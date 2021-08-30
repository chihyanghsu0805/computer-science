"""Run Tests."""

from bubble_sort import bubble_sort
from selection_sort import selection_sort

ARR = [5, 4, 3, 2, 1]


def test_bubble_sort():
    """Test Bubble Sort."""
    assert bubble_sort(ARR) == sorted(ARR)


def test_selection_sort():
    """Test Selection Sort."""
    assert selection_sort(ARR) == sorted(ARR)
