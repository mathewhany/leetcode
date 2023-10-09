class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        for (int i = 0; i < n; i++) {
            nums[i] += nums[n + i] << 16;
        }
        // 0 1 2 3 4 5
        for (int i = nums.size() - 1; i >= 0 ; i -= 2) {
            nums[i] = nums[(i - 1) / 2] >> 16;
            nums[i - 1] = nums[(i - 1) / 2] & (0x0000FFFF);   
        }
        return nums;
    }
};