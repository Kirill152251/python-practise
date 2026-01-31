def first_non_repeating_char(word: str) -> str:
    ht = {}
    for char in word:
        ht[char] = ht.get(char, 0 ) + 1
    for k, v in ht.items():
        if v == 1:
            return k
    return None
    

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""