from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:  return False

        flag = False
        for idx in range(0, len(arr) - 1):
            if flag == False and arr[idx] > arr[idx + 1]:
                flag = True
            elif flag == False and arr[idx] >= arr[idx + 1]:
                return False
            elif flag == True and arr[idx] <= arr[idx + 1]:
                return False
        return flag


solution = Solution()
solution.validMountainArray([0, 3, 2, 1])
