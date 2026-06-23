class Solution:
    def findMin(self, nums: List[int]) -> int:
       current_min = nums[0]

       for i in range(len(nums)):
            if(nums[i] < current_min):
                current_min = nums[i]
       return current_min