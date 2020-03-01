def quicksort(arr):
    if len(arr) < 2:
        return arr
    left = []
    pivot = arr[0]
    right = []
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [pivot] + quicksort(right)


def quicksort2(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr[1:] if i > pivot]
    return quicksort2(less) + [pivot] + quicksort2(more)


list = [3, 7, 4, 6, 0, 1, 5, 9, 8, 2]
print(quicksort(list))
print(quicksort2(list))
# print([1, 2, 3] + [4] + [5, 6])
