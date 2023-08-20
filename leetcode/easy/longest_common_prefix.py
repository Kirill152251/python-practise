class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word = sorted(strs, key=lambda x: len(x))[0]
        flag = False
        result = ''
        for index, letter in enumerate(shortest_word):
            for value in strs:
                l = value[index]
                if letter == l:
                    flag = True
                else:
                    flag = False
                    return result
            if flag:
                result += letter 
        return result


print(Solution.longestCommonPrefix(Solution, ["cir", "car"]))
