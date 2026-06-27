class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            item = nums[mid]

            if item == target:
                return mid
            elif item > target:
                high = mid - 1
            else:
                low = mid + 1
        if item > target:
            return mid
        else:
            return mid + 1
        