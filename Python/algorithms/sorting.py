""" Sorting algorithms
    - Bubble Sort
        - Time Complexity: O(n^2)
    - Insertion Sort
    - Quick Sort
    Description:
        Bubble Sort: 
            - Time Complexity: O(n^2)
        Insertion Sort:
            - Time Complexity: O(n^2)
        Quick Sort:
            - Time Complexity: O(n log n) 
"""


def site_swap(lst, index1, index2):
    """ Swap two elements in a list """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


def bubble_sort(lst: list[int, float]):
    """ Iterate through the list
    If the item is lower than the previous item, then you swap the order
    """
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for index in range(1, len(lst)):
            if lst[index] < lst[index-1]:
                lst[index], lst[index-1] = lst[index-1], lst[index]
                is_swapped = True
    return lst


items = [6, 7, 2, 8, 4, 6, 3, 6, 5, 8, 4]
items = bubble_sort(items)
print(items)


def insertion_sort(lst: list[int, float]):
    """ Iterate through the list
    If the item is lower than the previous item, then you swap the order
    """
    for index in range(1, len(lst)):
        current = lst[index]
        position = index
        while position > 0 and lst[position-1] > current:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = current
    return lst


def quick_sort(lst: list[int, float]):
    """ Quick Sort
        - Time Complexity: O(n log n)
        - Space Complexity: O(n)
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [item for item in lst if item < pivot]
    middle = [item for item in lst if item == pivot]
    right = [item for item in lst if item > pivot]
    return quick_sort(left) + middle + quick_sort(right)
