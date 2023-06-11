# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# def longest_palindrome(s: str) -> str:
#     longest = ''
#     for i in range(len(s)):
#         left = s[:i]
#         right = s[i:]
#         reversed_l = left[::-1]
#         reversed_r = right[::-1]
#         if left == reversed_l and len(left) > len(longest):
#             longest = left
#         elif right == reversed_r and len(right) > len(longest):
#             longest = right
#     return longest


# array = []
# word = 'babad'
# for i in range(len(word)):
#     piece = word[i:]
#     array.append(longest_palindrome(piece))
# print(max(array, key=len))


# Good solution:
def lp(s):
    res_text = ""
    res = 0

    for i in range(len(s)):
        for left, right in (i, i), (i, i + 1):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res:
                    res_text = s[left:right+1]
                    res = len(res_text)
                left -= 1
                right += 1

    return res_text


print(lp('asa'))
