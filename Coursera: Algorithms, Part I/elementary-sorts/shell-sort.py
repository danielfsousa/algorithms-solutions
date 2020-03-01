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


numbers = [2, 7, 4, 9, 2, 1, 6, 8, 3, 0, 5]
shell_sort(numbers)
print(numbers)
