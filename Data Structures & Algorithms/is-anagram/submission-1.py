class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts:
                return False
            counts[char] = counts.get(char) - 1

        if any(value != 0 for value in counts.values()):
            return False

        return True