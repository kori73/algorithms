""" Binary search algorithm Python implementation 
    For more details see Introduction to Algorithms by Cormen et. al.
"""
from math import floor

def binary_search(collection, element, start=None, end=None):
    """ Applies binary search to collection. """

    if start is None:
        start = 0
    if end is None:
        end = len(collection)

    # Assert that the array is sorted
    assert all([collection[i] <= collection[i+1] for i in range(len(collection)-1)]), "Array must be sorted."

    mid = floor((start + end)/2)

    if element == collection[mid]:
        print("Found at {0}".format(mid))
    elif element < collection[mid]:
        binary_search(collection, element, start=start, end=mid-1)
    elif element > collection[mid]:
        binary_search(collection, element, start=mid+1, end=end)

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [1, 3, 4, 5,6]
    z = [3, 4,5 , 6, 7]
    t = [-1, 0, 1, 3, 5]
    v = [-1, 1,2, 2.5, 3]
    xx = [0, 1, 2, 3, 4, 5, 6, 8]
    z= [-1, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7]
    binary_search(x, 3)
    binary_search(y, 3)
    binary_search(z, 3)
    binary_search(t, 3)
    binary_search(v, 3)
    binary_search(xx, 3)

