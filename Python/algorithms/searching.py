""" Searching algorithms
    - Linear Search
    - Binary Search
    Description:
        Linear Search:
            - Time Complexity: O(n)
            - Space Complexity: O(1)
        Binary Search:
            - Time Complexity: O(log n)
            - Space Complexity: O(1)
"""

"""
Searching algorithms

    Linear Search
    Binary Search

Description:
This module provides implementations of two searching algorithms:
linear search and binary search.

Linear Search:
Linear search is a simple search algorithm that sequentially checks
each element of a list until it finds an element that matches the search
value or exhausts the list. It has a time complexity of O(n), which means
that the time it takes to search a list of size n grows linearly with the
size of the list. The space complexity of linear search is O(1), which
means that the algorithm requires a constant amount of memory, regardless of
the size of the list.

Binary Search:
Binary search is a more efficient search algorithm that works on sorted lists.
It repeatedly divides the search interval in half until the
target value is found or the search interval is empty.
It has a time complexity of O(log n), which means that the time it takes
to search a sorted list of size n grows logarithmically with the size of
the list. The space complexity of binary search is O(1),
which means that the algorithm requires a constant amount of memory,
regardless of the size of the list.

Functions:
This module provides the following functions for searching a list:

    linear_search(lst, search):
    This function searches for the first occurrence of the search value
    in the given list using a linear search algorithm.
    If the search value is found, the function returns the index of the first
    occurrence of the search value in the list. If the search value is not
    found, the function returns -1.

    binary_search(lst, search):
    This function searches for the first occurrence of the search value in
    the given sorted list using a binary search algorithm.
    If the search value is found,
    the function returns the index of the first occurrence
    of the search value in the list.
    If the search value is not found, the function returns -1.
"""


def linear_search(lst, search):
    for index in range(len(lst)):
        if lst[index] == search:
            return index
    return -1


def binary_search(lst, search):
    """ Binary Search
        - Time Complexity: O(log n)
        - Space Complexity: O(1)
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        # mid is the middle index of the list
        mid = (left + right) // 2
        if lst[mid] == search:
            return mid
        elif lst[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1
