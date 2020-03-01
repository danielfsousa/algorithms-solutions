def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = items[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 9, 3, 5, 0, 4, 2, 6, 7, 8]
print(binary_search(list, 3))
