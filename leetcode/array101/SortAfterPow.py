from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda x: x ** 2, nums))
        return sorted(nums)
