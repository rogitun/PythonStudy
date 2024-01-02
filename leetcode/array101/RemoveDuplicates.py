from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while True:
            if (i + 1) >= len(nums): break
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)


solution = Solution()
solution.removeDuplicates([1, 1, 2])
