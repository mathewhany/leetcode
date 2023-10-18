class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int prev = INT_MIN;
        bool used = false;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                if (used) return false;

                if (prev > nums[i + 1]) {
                    nums[i + 1] = nums[i];
                } else {
                    nums[i] = prev;
                }
                used = true;   
            }
            prev = nums[i];
        }

        return true;
    }
};