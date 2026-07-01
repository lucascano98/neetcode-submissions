class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(numbers):
            complementary = target - v
            if complementary in seen:
                return sorted([seen[complementary], i + 1])

            seen[v] = i + 1