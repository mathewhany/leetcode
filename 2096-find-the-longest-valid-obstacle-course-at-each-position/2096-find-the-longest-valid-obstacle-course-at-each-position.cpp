class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        vector<int> dp;
        vector<int> lengths;

        for (int i = 0; i < obstacles.size(); i++) {
            int lo = 0;
            int hi = dp.size() - 1;
            int ans = -1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (dp[mid] > obstacles[i]) {
                    hi = mid - 1;
                    ans = mid;
                } else {
                    lo = mid + 1;
                }
            }
            if (ans == -1) {
                dp.push_back(obstacles[i]);
                lengths.push_back(dp.size());
            } else {
                dp[ans] = obstacles[i];
                lengths.push_back(ans + 1);
            }
        }

        return lengths;
    }
};