class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k == 0) return 1;

        vector<double> dp(n + 1, 0);
        dp[0] = 1.0;
        double window = 1.0;
        double windowStart = 0;

        for (int i = 1; i <= n; i++) {
            dp[i] += window / maxPts;
            if (i < k) {
                window += dp[i];
            } 
            if (windowStart <= i - maxPts) {
                window -= dp[windowStart++];
            }
            if (window == 0) {
                break;
            }
        }

        double ans = 0;
        for (int i = k; i <= n; i++) {
            ans += dp[i];
        }
        return ans;
    }
};