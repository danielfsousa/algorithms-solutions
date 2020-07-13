'''
Counting inversions. An inversion in an array a[] is a pair of entries
a[i] and a[j] such that i < j but a[i] > a[j]. Given an array,
design a linearithmic algorithm to count the number of inversions.
'''


def count_inversions(arr):
    N = len(arr)
    aux = arr.copy()

    def count_and_sort(arr):
        count = 0
        sz = 1
        while sz < N:
            low = 0
            while low < N - sz:
                mid = low + sz - 1
                high = min(low + sz + sz, N - 1)
                count += merge(arr, low, mid, high)
                low += sz + sz
            sz += sz
        return count

    def merge(arr, low, mid, high):
        # copy main list to auxiliary
        for n in range(low, high + 1):
            aux[n] = arr[n]

        count = 0
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > high:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
                count += mid - i + 1
        return count

    return count_and_sort(arr)


nums = [9, 2, 4, 1, 3, 5]
print(count_inversions(nums))  # 3 inversions (2,1; 4,1; 4,3)
