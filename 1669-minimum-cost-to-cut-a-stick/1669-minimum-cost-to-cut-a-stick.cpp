class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        sort(cuts.begin(), cuts.end());
        vector<int> extendedCuts;
        extendedCuts.push_back(0);
        for(int i = 0; i < cuts.size(); i++) {
            extendedCuts.push_back(cuts[i]);
        }
        extendedCuts.push_back(n);

        vector<vector<long>> memo(extendedCuts.size(), vector<long>(extendedCuts.size(), -1));
        function<long(int, int)> dp = [&] (int start, int end) {
            if (start + 1 == end) {
                return 0l;
            }

            if (memo[start][end] != -1) return memo[start][end];

            long ans = INT_MAX;
            for (int i = start + 1; i < end; i++) {
                ans = min(ans, + extendedCuts[end] - extendedCuts[start] + dp(start, i) + dp(i, end));
            }

            memo[start][end] = ans;
            return ans;
        };

        return dp(0, extendedCuts.size() - 1);
    }
};