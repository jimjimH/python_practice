from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            goal = target - v
            if goal in dic:
                return [dic[goal], i]
            else:
                if not dic.get(v):
                    dic[v] = i
