class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.size() <= 2) return true;

        bool used = false;

        for (int i = 0; i < nums.size() - 2; i++) {
            bool inv1 = nums[i] <= nums[i + 1];
            bool inv2 = nums[i + 1] <= nums[i + 2];
            bool inv3 = nums[i] <= nums[i + 2];

            if (inv1 && inv2 && inv3) continue;

            if (!inv1 && !inv2 && !inv3) return false;

            if (used) return false;

            if (inv3) {
                nums[i + 1] = nums[i];
                used = true;
            } else if (inv1) {
                nums[i + 2] = nums[i + 1];
                used = true;
            } else {
                used = true;
            }
        }

        return true;
    }
};