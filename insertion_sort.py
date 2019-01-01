""" Insertion sort algorithm Python implementation.
    For more details see Introduction to Algorithms by Cormen et. al. """

def insertion_sort(collection):
    """Insertion Sort Algorithm, theta(n^2)"""
    n = len(collection)
    for j in range(1, n):
        key = collection[j]
        i = j-1
        while i >= 0 and collection[i] > key:
            collection[i + 1] = collection[i]
            i = i - 1
        collection[i + 1] = key
    return collection

if __name__ == '__main__':
    import numpy as np
    results = []
    for i in range(100):
        length = np.random.randint(1000)
        array = np.random.rand(length)
        s_array = insertion_sort(array)
        res = all(s_array[i] < s_array[i+1] for i in range(len(s_array) - 1))
        results.append(res)
print(results)
