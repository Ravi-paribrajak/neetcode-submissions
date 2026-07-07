class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arr_size = len(nums)

        for i in range(arr_size - 1):
            for j in range(arr_size):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False
