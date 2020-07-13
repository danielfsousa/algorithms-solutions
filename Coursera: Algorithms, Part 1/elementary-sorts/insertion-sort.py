def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


numbers = [2, 7, 4, 9, 2, 1, 6, 8, 3, 0, 5]
insertion_sort(numbers)
print(numbers)
