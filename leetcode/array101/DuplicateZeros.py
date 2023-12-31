from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        result = []
        for x in arr:
            result.append(x)
            if x == 0:
                result.append(0)

        arr[:] = result[:len(arr)]



solution_ = Solution()

solution_.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
