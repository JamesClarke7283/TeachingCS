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
