def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if arr[min_idx] < arr[i]:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


numbers = [2, 7, 4, 9, 2, 1, 6, 8, 3, 0, 5]
selection_sort(numbers)
print(numbers)
