class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        l = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1

            seen[char] = i
            max_length = max(max_length, i - l + 1)
            
        return max_length