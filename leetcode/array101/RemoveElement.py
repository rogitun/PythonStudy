from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        origin = len(nums)
        i = 0
        res = 0
        while i < origin:
            if nums[i] == val:
                nums.pop(i)
                nums.append(-1)
                res += 1
            else:
                i += 1
        return origin - res


solution = Solution()

solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
