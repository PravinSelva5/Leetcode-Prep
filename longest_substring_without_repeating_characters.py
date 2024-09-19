class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_substring_len = 0
        left = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_substring_len = max(max_substring_len, right - left + 1)
        

        return max_substring_len