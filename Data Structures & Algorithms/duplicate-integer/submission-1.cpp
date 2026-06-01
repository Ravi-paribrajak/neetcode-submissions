class Solution {
   public:
    bool hasDuplicate(vector<int>& nums) {
        bool isDuplicate = false;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if(isDuplicate) break;
        }
        return isDuplicate;
    }
};