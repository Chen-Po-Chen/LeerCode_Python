# 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    for k in range(len(nums)):
                        if k != i and k != j:
                            if nums[i]+nums[j]+nums[k] == 0:
                                candidate = [nums[i],nums[j],nums[k]]
                                candidate.sort()
                                if candidate not in output:
                                    output.append(candidate)
        return output