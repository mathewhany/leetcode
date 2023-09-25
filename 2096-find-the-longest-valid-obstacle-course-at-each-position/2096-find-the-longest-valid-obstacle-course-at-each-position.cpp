class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        vector<int> dp, ans;

        for (int i = 0; i < obstacles.size(); i++) {
            if (dp.empty() || dp[dp.size() - 1] <= obstacles[i]) {
                dp.push_back(obstacles[i]);
                ans.push_back(dp.size());
            } else {
                int idx = upper_bound(dp.begin(), dp.end(), obstacles[i]) - dp.begin();
                ans.push_back(idx + 1);
                dp[idx] = obstacles[i];
            }
        }

        return ans;
    }
};