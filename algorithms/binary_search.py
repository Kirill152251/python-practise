def binary_search(data_structure, item):
    low = 0
    high = len(data_structure) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = data_structure[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
    return None


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(ls, 10))
