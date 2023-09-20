class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> dp(nums1.size() + 1, vector<int>(nums2.size() + 1, 0));

        for (int i = nums1.size() - 1; i >= 0; i--) {
            for (int j = nums2.size() - 1; j >= 0; j--) {
                dp[i][j] = max({ 
                    dp[i][j],
                    nums1[i] == nums2[j] ? 1 + dp[i + 1][j + 1] : 0, 
                    dp[i][j + 1], 
                    dp[i + 1][j] 
                });
            }
        }

        return dp[0][0];
    }
};