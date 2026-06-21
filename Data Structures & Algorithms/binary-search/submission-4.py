class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            item = nums[mid]
            if(item == target):
                return mid
            elif item > target:
                high = mid - 1
            else: 
                low = mid + 1
        return -1
        