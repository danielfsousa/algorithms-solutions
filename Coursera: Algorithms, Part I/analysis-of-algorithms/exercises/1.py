'''
3-SUM in quadratic time. Design an algorithm for the 3-SUM problem that
takes time proportional to n^2 in the worst case.
You may assume that you can sort the nnn integers in time proportional
to n^2 or better.
'''


def binary_search(arr, i):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = arr[mid]
        if guess == i:
            return True
        if guess < i:
            low = mid + 1
        else:
            high = mid - 1
    return False


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for el in arr[1:]:
        if el <= pivot:
            left.append(el)
        if el > pivot:
            right.append(el)

    return quick_sort(left) + [pivot] + quick_sort(right)


def three_sum(numbers):
    sorted = quick_sort(numbers)
    count = 0
    for i, inum in enumerate(sorted):
        for j, jnum in enumerate(sorted):
            if i == j:
                continue
            wanted_num = -(inum + jnum)
            if (inum < jnum) and (jnum < wanted_num) and binary_search(sorted, wanted_num):
                count += 1
    return count


numbers = [30, -40, -20, -10, 40, 0, 10, 5]
print(three_sum(numbers))
