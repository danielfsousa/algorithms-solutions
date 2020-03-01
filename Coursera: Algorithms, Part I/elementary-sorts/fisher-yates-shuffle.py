from random import randrange


def shuffle(arr):
    N = len(arr)
    for i in range(N):
        r = randrange(i, N)
        arr[i], arr[r] = arr[r], arr[i]


numbers = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(numbers)
print(numbers)
