class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0
        k = 0

        while ptr < len(nums):
            if nums[ptr] != val:
                nums[k] = nums[ptr]
                k += 1
            ptr += 1
           
        return k

        