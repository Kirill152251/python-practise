def isPalindrome(s: str) -> bool:
    arr = [letter.lower() for letter in s if letter.isalnum()]
    new_s = ''.join(arr)
    return new_s == new_s[::-1]

test = 'A man, a plan, a canal: Panama'
print(isPalindrome(test))