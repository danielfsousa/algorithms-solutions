def count(arr):
    if len(arr) == 1:
        return 1
    mid = round(len(arr) / 2)
    return count(arr[:mid]) + count(arr[mid:])


def count2(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


print(count([1, 2, 3, 4, 5, 6, 7, 8]))
print(count2([1, 2, 3, 4, 5, 6, 7, 8]))
