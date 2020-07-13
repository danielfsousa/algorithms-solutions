'''
Intersection of two sets. Given two arrays a[] and b[],
each containing n distinct 2D points in the plane,
design a subquadratic algorithm to count the number of points
that are contained both in array a[] and array b[].
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


def intersection(a, b):
    shell_sort(b)
    return {n for n in a if binary_search(b, n) is not None}


a = [1, 2, 4, 9, 4, 7, 5]
b = [8, 2, 9, 4, 10]

print(intersection(a, b))  # [9, 2, 4]
