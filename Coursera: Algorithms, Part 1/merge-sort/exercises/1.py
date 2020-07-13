'''
Merging with smaller auxiliary array.
Suppose that the subarray a[0] to a[n−1] is sorted and the subarray
a[n] to a[2∗n−1] is sorted. How can you merge the two subarrays so that
a[0] to a[2∗n−1] is sorted using an auxiliary array of length nnn (instead of 2n2n2n)?
'''


def merge_subarrays(arr):
    low = 0
    high = len(arr) - 1
    mid = low + high // 2
    aux = arr[:mid+1]

    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid:
            arr[k] = arr[j]
            j += 1
        elif j > high:
            arr[k] = arr[i]
            i += 1
        elif aux[i] < arr[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1


nums = [40, 61, 70, 71, 99, 20, 51, 55, 75, 100]
merge_subarrays(nums)
print(nums)
