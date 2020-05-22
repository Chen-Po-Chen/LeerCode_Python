# Next Permutation

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1, 2, 3 → 1, 3, 2
# 3, 2, 1 → 1, 2, 3
# 1, 1, 5 → 1, 5, 1

class Solution:
    
    def max_from_right(self, nums):
        j = len(nums) - 1
        while j > 0:
            if nums[j - 1] < nums[j]:
                return j
            j -= 1
        return 0
    
    def swap_candidate(self, nums, x):
        j = len(nums) - 1
        while j>=0 and nums[j] <= x:
            j -= 1
        return j
    
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peek = self.max_from_right(nums)
        if peek == 0:
            return nums.sort()
        
        i, x = peek - 1, nums[peek-1]
        j = self.swap_candidate(nums, x)
        nums[i], nums[j] = nums[j], nums[i]
        nums[peek:] = reversed(nums[peek:])