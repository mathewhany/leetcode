class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        unordered_set<int> daysSet;
        for (auto const &day : days) daysSet.insert(day);

        int lastDay = days[days.size() - 1];

        vector<int> dp(lastDay + 1 + 30, 0);

        for (int i = lastDay; i >= 0; i--) {
            if (daysSet.count(i)) {
                dp[i] = min(
                    {
                        costs[0] + dp[i + 1],
                        costs[1] + dp[i + 7],
                        costs[2] + dp[i + 30]
                    }
                );
            } else {
                dp[i] = dp[i + 1];
            }
        }

        return dp[0];
    }
};