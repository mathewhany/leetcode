class Solution {
public:
    int profitableSchemes(int N, int minProfit, vector<int>& group, vector<int>& profit) {
        vector<vector<vector<long>>> memo(group.size(), vector<vector<long>>(N + 1, vector<long>(minProfit + 1, -1)));
        int mod = 1e9 + 7;

        function<long(int, int, int)> dp = [&] (int i, int n, int p) {
            if (i >= group.size()) {
                if (p == minProfit) {
                    return 1l;
                } else {
                    return 0l;
                }
            }

            if (memo[i][n][p] != -1) return memo[i][n][p];

            long ans = dp(i + 1, n, p);

            if (group[i] <= n) {
                ans = (ans + dp(i + 1, n - group[i], min(profit[i] + p, minProfit))) % mod;
            }

            memo[i][n][p] = ans;

            return ans;
        };

        return dp(0, N, 0);
    }
};