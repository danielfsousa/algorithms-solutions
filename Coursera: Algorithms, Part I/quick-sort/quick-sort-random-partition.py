from random import randrange


def shuffle(arr):
    N = len(arr)
    for i in range(N):
        r = randrange(i, N)
        arr[i], arr[r] = arr[r], arr[i]


def quick_sort(arr):
    def partition(arr, low, high):
        i = low
        j = high
        while True:
            # find item on left to swap
            while arr[i] <= arr[low]:
                i += 1
                if i == high:
                    break
            # find item on right to swap
            while arr[low] <= arr[j]:
                j -= 1
                if j == low:
                    break
            # check if pointers cross
            if i >= j:
                break
            # swap
            arr[i], arr[j] = arr[j], arr[i]
        # swap with partitioning item
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def sort(arr, low, high):
        if high <= low:
            return
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p + 1, high)

    shuffle(arr)
    sort(arr, low=0, high=len(arr) - 1)


numbers = [2, 0, 1, 8, 2, 4, 6, 3, 9, 5, 7, 3]
quick_sort(numbers)
print(numbers)
