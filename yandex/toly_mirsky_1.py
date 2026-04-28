# Дан массив натуральных чисел и числа могут повторяться
# Необходимо выбрать из них k чисел так, чтобы разность максимального
# из выбранных была минимальной
# вернуть эту разность

def solution(arr: list, k: int) -> int:
    arr.sort()
    res = float('inf') 
    left = 0
    right = k - 1
    while right < len(arr):
        res = min(arr[right] - arr[left], res)
        left += 1
        right += 1
    return res

array = [10, 100, 300, 200, 1000, 20, 30]
array2 = [1, 10, 12, 20]
k = 3 # -> 20
print(solution(array, k))
print(solution(array2, k))