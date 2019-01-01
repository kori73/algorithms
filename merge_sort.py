""" Merge sort Python implementation.
    For more details see Introduction to Algorithms by Cormen et. al. """

from math import inf, ceil

def merge(collection, p, q, r):
    """ Merge subroutine"""
    left = collection[p:q]
    left.append(inf)
    right = collection[q:r]
    right.append(inf)
    i = j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            collection[k] = left[i]
            i += 1
        else:
            collection[k] = right[j]
            j += 1
    return collection

def merge_sort(collection, p=None, r=None):
    """ Applies merge sort to a subset of collection.
        p and r defines the subset:
        p: Starting index of the subset, q: length of the subset
    """

    if p is None:
        p = 0
    if r is None:
        r = len(collection)

    if p + 1 < r:
        q = ceil((p + r)/2)

        merge_sort(collection, p, q)
        merge_sort(collection, q, r)
        merge(collection, p, q, r)

if __name__ == "__main__":
    # Test 1 for Merge subroutine
    A1 = [5, 6, 7, 8, 25, 32]
    A2 = [10, 20, 30]
    A3 = [200, 100, 90]
    A = A3 + A1 + A2

    s = merge(A, 3, 9, 12)
    print(s)
    # Test 2
    A1 = [5, 6, 7, 8, 25, 32]
    A2 = [10, 20, 30]
    A3 = [200, 100, 90, 800]
    A = A1 + A2 + A3

    s = merge(A, 0, 6, 9)
    print(s)

    # merge sort test 1
    A = [4, 3, 2, 4, 5, 3, 6, 7, 10, 1]
    merge_sort(A)
    print(A)

    #merge sort test 2
    A = [1.1, 3.2, 0.5, -5.2, -100, 100, 5, 3, 3, 25, -777]
    merge_sort(A)
    print(A)
