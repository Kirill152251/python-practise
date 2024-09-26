def wordBreak(s: str, wordDict: list[str]) -> bool:
    while wordDict:
        temp_str = s
        for word in wordDict:
            if word in temp_str and temp_str.startswith(word):
                temp_str = temp_str.replace(word, "")
        if temp_str == "":
            return True
        else:
            wordDict.remove(wordDict[0])
    return False

if __name__ == "__main__":
    s = "cbca"
    wordDict = ["bc","ca"]
    print(wordBreak(s, wordDict))