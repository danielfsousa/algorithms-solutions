def recursive_merge_sort(arr):
    def sort(arr, aux, low, high):
        if high <= low:
            return
        mid = (low + high) // 2
        sort(arr, aux, low, mid)
        sort(arr, aux, mid + 1, high)
        if arr[mid] <= arr[mid + 1]:
            return
        merge(arr, aux, low, mid, high)

    def merge(arr, aux, low, mid, high):
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

    sort(arr, aux=arr.copy(), low=0, high=len(arr) - 1)


numbers = [2, 0, 1, 8, 2, 4, 6, 3, 9, 5, 7, 3]
recursive_merge_sort(numbers)
print(numbers)
