def max_heapify(A: list, n: int, i: int):
    """
    Subroutine to manipulate heaps when max-heap property is violated at index i.
    Left and right subtrees are assumed to be max-heaps.
    """
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A: list):
    " Build a max heap from an arbitrary list"
    size = len(A)
    for i in range(int(size/2) - 1, -1, -1):
        max_heapify(A, size, i)


def heap_sort(A: list):
    " Heap sort algorithm implementation from the book Introduction to Algorithms by Cormen et. al."
    build_max_heap(A)
    size = len(A)
    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        size -= 1
        max_heapify(A, size, 0)


def is_max_heap(A: list):
    "Test that checks if a list has max heap property"
    size = len(A)
    checks = []
    for i in range(int(size/2) - 1, -1, -1):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size:
            max_child = A[l]
        if r < size and A[r] > A[l]:
            max_child = A[r]
        checks.append(A[i] >= max_child)
    return all(checks)


if __name__ == '__main__':

    a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    max_heapify(a, len(a), 1)
    assert a == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1], "max_heapify fails"

    a = [10, 4, 14, 3, 16, 1, 2, 8, 9, 7]
    build_max_heap(a)
    assert is_max_heap(a), "build_max fails"

    a = [10, 4, 14, 3, 16, 1, 2, 8, 9, 7]
    heap_sort(a)
    assert a == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16], "heap_sort fails"
