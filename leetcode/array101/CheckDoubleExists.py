from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for idx in range(0, len(arr)):
            start = 0
            end = len(arr) - 1
            std = arr[idx] * 2
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == std and idx != mid:
                    return True
                elif arr[mid] > std:
                    end = mid - 1
                else:
                    start = mid + 1

        return False


solution = Solution()
solution.checkIfExist([-2, 0, 10, -19, 4, 6, -8])
