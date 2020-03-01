from random import shuffle


def partition(arr, low, high):
    left = low
    right = high
    while True:
        # find item on left to swap
        while arr[left] <= arr[low]:
            left += 1
            if left == high:
                break
        # find item on right to swap
        while arr[low] <= arr[right]:
            right -= 1
            if right == low:
                break
        # check if pointers cross
        if left >= right:
            break
        # swap
        arr[left], arr[right] = arr[right], arr[left]
    # swap with partitioning item
    arr[low], arr[right] = arr[right], arr[low]
    return right


def select(arr, num, low, high):
    while high > low:
        p = partition(arr, low, high)
        if p < num:
            low = p + 1
        elif p > num:
            high = p - 1
        else:
            return arr[num]
    return arr[num]


def quick_select(arr, num):
    shuffle(arr)
    return select(arr, num, low=0, high=len(arr) - 1)


numbers = [2, 0, 1, 8, 2, 4, 15, 3, 9, 5, 7, 3, 8]
max_index = len(numbers) - 1
print(max_index)  # 12
print(quick_select(numbers, max_index))  # 15
