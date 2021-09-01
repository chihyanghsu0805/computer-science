"""Run Tests."""

from copy import deepcopy

from bubble_sort import bubble_sort
from counting_sort import counting_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

ARR = [5, 4, 3, 2, 1]


def test_counting_sort():
    """Test Counting Sort."""
    assert counting_sort(ARR) == sorted(ARR)


def test_bubble_sort():
    """Test Bubble Sort."""
    dummy = deepcopy(ARR)
    bubble_sort(dummy)
    assert dummy == sorted(ARR)


def test_merge_sort():
    """Test Merge Sort."""
    dummy = deepcopy(ARR)
    merge_sort(dummy)
    assert dummy == sorted(ARR)


def test_quick_sort():
    """Test Merge Sort."""
    dummy = deepcopy(ARR)
    quick_sort(dummy)
    assert dummy == sorted(ARR)


def test_selection_sort():
    """Test Selection Sort."""
    dummy = deepcopy(ARR)
    selection_sort(dummy)
    assert dummy == sorted(ARR)
