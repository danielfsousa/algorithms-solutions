from random import shuffle


def partition(arr, left, right):
    lt = left
    gt = right
    i = left
    pivot = arr[left]
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def sort(arr, left, right):
    if left >= right:
        return
    lt, gt = partition(arr, left, right)
    sort(arr, left, lt - 1)
    sort(arr, gt + 1, right)


def quick_sort(arr):
    shuffle(arr)
    sort(arr, left=0, right=len(arr) - 1)


numbers = [2, 0, 1, 8, 2, 4, 6, 3, 9, 5, 7, 3, 9, 8]
quick_sort(numbers)
print(numbers)
