class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        nexts = 1

        while nexts < len(nums):
            if nums[prev] == nums[nexts]:
                nums.pop(nexts)
            else:
                prev += 1
                nexts += 1
            

        return len(nums)
