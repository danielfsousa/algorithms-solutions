'''
Permutation.
Given two integer arrays of size n,design a subquadratic algorithm
to determine whether one is a permutation of the other.
That is, do they contain exactly the same entries
but, possibly, in a different order.
'''


def shell_sort(arr):
    N = len(arr)

    # 3x+1 increment sequence
    h = 1
    while h < N / 3:
        h = 3 * h + 1

    # h-sort the array
    while h >= 1:
        for i in range(h, N):
            j = i
            while (j >= h and arr[j] < arr[j - h]):
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = round(h / 3)


def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = items[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def is_permutation(a, b):
    shell_sort(a)
    shell_sort(b)
    return a == b


permutation = [[2, 1, 3, 4, 5], [3, 2, 4, 1, 5]]
not_permutation = [[8, 2, 9, 4, 10], [1, 2, 3, 4, 5]]
not_permutation2 = [[1, 2, 3, 4, 5, 5], [1, 2, 3, 4, 5]]

print(is_permutation(*permutation))       # True
print(is_permutation(*not_permutation))   # False
print(is_permutation(*not_permutation2))  # False
