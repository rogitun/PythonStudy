from typing import List
import math


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        cons = 0
        for val in nums:
            if val == 1:
                cons += 1
                max_num = max(max_num, cons)
            else:
                cons = 0
        return max_num


solution = Solution()

res = solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])

print(res)
