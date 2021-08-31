"""Run Tests."""

from copy import deepcopy

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort

ARR = [5, 4, 3, 2, 1]


def test_bubble_sort():
    """Test Bubble Sort."""
    assert bubble_sort(ARR) == sorted(ARR)


def test_merge_sort():
    """Test Merge Sort."""
    dummy = deepcopy(ARR)
    merge_sort(dummy)
    assert dummy == sorted(ARR)


def test_selection_sort():
    """Test Selection Sort."""
    assert selection_sort(ARR) == sorted(ARR)
