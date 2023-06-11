# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
def longest_palindrome(s: str) -> str:
    longest = ''
    for i in range(len(s)):
        left = s[:i]
        right = s[i:]
        reversed_l = left[::-1]
        reversed_r = right[::-1]
        if left == reversed_l and len(left) > len(longest):
            longest = left
        elif right == reversed_r and len(right) > len(longest):
            longest = right
    return longest


# array = []
# word = 'babad'
# for i in range(len(word)):
#     piece = word[i:]
#     array.append(longest_palindrome(piece))
# print(max(array, key=len))


# Good solution:
def lp_gs(s: str) -> str:
    result = ''
    if len(s) == 1:
        return s
    get_index = get_index_even_size if len(s) % 2 == 0 else get_index_odd_size
    for i in range(len(s)):
        left_index, right_index = get_index(i)
        while left_index >= 0 and right_index < len(s):
            left_char = s[left_index]
            right_char = s[right_index]
            sl = slice(left_index, right_index + 1)
            if left_char == right_char and len(s[sl]) > len(result):
                result = s[sl]
            else:
                if len(s) == 2:
                    return s[0]
                break
            right_index += 1
            left_index -= 1
    return result


def get_index_odd_size(i) -> tuple:
    return i - 1, i + 1


def get_index_even_size(i) -> tuple:
    return i, i + 1


print(lp_gs('fkgabb'))
