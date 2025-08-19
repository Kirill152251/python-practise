# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Hash Table, String, Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_len = 0
        hash_table = set()
        while right < len(s):
            if s[right] not in hash_table:
                hash_table.add(s[right])
                right += 1
                max_len = max(max_len, len(hash_table))
            else:
                hash_table.remove(s[left])
                left += 1

        return max_len 



if __name__ == "__main__":
    s = "abcfcqwerctyu"
    print(Solution().lengthOfLongestSubstring(s)) # -> abc