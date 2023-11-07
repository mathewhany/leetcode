class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<long> freq(*max_element(nums.begin(), nums.end()) + 1);
        for (int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++;
        }
        
        vector<long> dp(freq.size());
        for (int i = 0; i < freq.size(); i++) {
            dp[i] = max(
                (i >= 2 ? dp[i -  2] : 0) + freq[i] * i,
                (i >= 1) ? dp[i - 1] : 0
            );
        }

        return dp[freq.size() - 1];
    }
};