# Link: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    # Bruteforce
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Dict (HashTable)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indexes = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_with_indexes:
                return [nums_with_indexes[target - nums[i]], i]
            nums_with_indexes[nums[i]] = i
        return []


s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0,1]
assert s.twoSum([3,2,4], 6) == [1,2]
assert s.twoSum([3,3], 6) == [0,1]