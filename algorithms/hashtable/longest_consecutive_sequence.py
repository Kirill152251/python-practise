def longest_consecutive_sequence(arr: list[int]) -> int:
    set1 = set(arr)
    max_counter = 0
    for i in arr:
        counter = 0
        while True:
            if i + counter in set1:
                counter += 1
                max_counter = max(max_counter, counter)
            else:
                break
    return max_counter


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""