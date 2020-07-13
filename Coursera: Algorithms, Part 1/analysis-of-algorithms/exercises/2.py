'''
Search in a bitonic array. An array is bitonic if it is comprised of an increasing sequence of integers
followed immediately by a decreasing sequence of integers.
Write a program that, given a bitonic array of nnn distinct integer values,
determines whether a given integer is in the array
    Standard version: Use ∼3lg⁡n compares in the worst case.
    Signing bonus: Use ∼2lg⁡n compares in the worst case
(and prove that no algorithm can guarantee to perform fewer than ∼2lg⁡n compares in the worst case).
'''


def binary_search(arr, i, order='asc'):
    low = 0
    high = len(arr) - 1
    def compare(guess, i): return guess < i if order == 'asc' else guess > i

    while low <= high:
        mid = round((low + high) / 2)
        guess = arr[mid]
        if guess == i:
            return mid
        if compare(guess, i):
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_max(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = arr[mid]
        prev = arr[mid - 1]
        next = arr[mid + 1]

        if guess > prev and guess > next:
            return mid
        if guess > prev and guess < next:
            low = mid + 1
        elif guess < prev and guess > next:
            high = mid - 1


def search_bitonic(arr, i):
    max_idx = find_max(arr)
    arr1 = arr[:max_idx + 1]
    arr2 = arr[max_idx + 1:]

    if binary_search(arr1, i) > -1 or binary_search(arr2, i, 'desc') > -1:
        return True
    else:
        return False


bitonic_array = [1, 3, 5, 8, 20, 22, 25, 33, 15, 5, 2]
num = 33
print(search_bitonic(bitonic_array, num))
