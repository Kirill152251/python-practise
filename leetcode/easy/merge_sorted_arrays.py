from itertools import chain


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    return sorted(list(chain(nums1[:m], nums2[:n])))



arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 7900, 6,56145,61,2456,-6242]

x = merge(arr1, 2, arr2, 7)
print(x)
