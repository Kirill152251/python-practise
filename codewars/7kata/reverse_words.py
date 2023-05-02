# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the
# string should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    parts = []
    word = ''
    spaces = ''
    for char in text:
        if char != ' ':
            word += char
            if spaces != '':
                parts.append(spaces)
                spaces = ''
        else:
            if spaces == '':
                parts.append(word)
                word = ''
            spaces += ' '
    if word != '':
        parts.append(word)
    if spaces != '':
        parts.append(spaces)
    final = list(map(lambda item: item[::-1], parts))
    return ''.join(final)


def reverse_words_best_solution(string: str):
    return ' '.join(s[::-1] for s in string.split(' '))


print(reverse_words(input()))
