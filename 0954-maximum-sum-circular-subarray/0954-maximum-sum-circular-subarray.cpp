class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        vector<long> prefix, dp;
        long prefixSum = 0, suffixSum = 0;
        long dpBest = INT_MIN;

        for (int i = 0; i < n; i++) { 
            prefixSum += nums[i];

            if (i == 0) {
                prefix.push_back(prefixSum);
                dp.push_back(nums[i]);
            } else {
                prefix.push_back(
                    max(prefix[i - 1], prefixSum)
                );
                dp.push_back(max(dp[i - 1] + nums[i], long(nums[i])));
            }

            dpBest = max(dpBest, dp[i]);
        }

        long suffix = INT_MIN;
        long best = dpBest;
        for (int i = 0; i < n; i++) {
            best = max(best, prefix[nums.size() - 1 - i] + suffix);
            suffixSum += nums[nums.size() - 1 - i];
            suffix = max(suffix, suffixSum);
        }

        return best;
    }
};