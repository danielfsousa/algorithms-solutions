def bottom_up_merge_sort(arr):
    N = len(arr)
    aux = arr.copy()

    def sort(arr):
        sz = 1
        while sz < N:
            low = 0
            while low < N - sz:
                merge(arr, low, low + sz - 1, min(low + sz + sz - 1, N - 1))
                low += sz + sz
            sz += sz

    def merge(arr, low, mid, high):
        # copy main list to auxiliary
        for x in range(low, high + 1):
            aux[x] = arr[x]

        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > high:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1

    sort(arr)


numbers = [2, 0, 1, 8, 2, 4, 6, 3, 9, 5, 7, 3]
bottom_up_merge_sort(numbers)
print(numbers)
