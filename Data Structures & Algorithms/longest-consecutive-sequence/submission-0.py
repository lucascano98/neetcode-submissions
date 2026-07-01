class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            curr = num
            streak = 0
            if curr - 1 in num_set:
                continue

            while curr in num_set:
                streak += 1
                curr += 1

            longest = max(longest, streak)

        return longest