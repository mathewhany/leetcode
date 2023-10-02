class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        long sum = 0;
        int ans = INT_MIN;

        for (int i = 0; i < nums.size(); i++) {
            int count = i + 1;
            sum += nums[i];
            ans = max(ans, int((sum + i) / (i + 1)));
        }

        return ans;
    }
};