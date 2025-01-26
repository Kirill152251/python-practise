def qsort(arr: list):
    """nlog(n)"""
    if len(arr) < 2:
        return arr
    base = arr.pop(0)
    smaller = [item for item in arr if item <= base]
    greater = [item for item in arr if item > base]
    return qsort(smaller) + [base] + qsort(greater)


ls = [24, 15, -51, 153, 1, 1, 3413, 13, 13]
print(qsort(ls))
