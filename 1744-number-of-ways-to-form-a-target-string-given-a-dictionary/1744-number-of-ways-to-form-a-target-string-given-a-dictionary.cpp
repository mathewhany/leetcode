class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int mod = 1e9 + 7;
        unordered_map<int, unordered_map<char, int>> letterFreq;
        int maxJ = 0;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words[i].size(); j++) {
                letterFreq[j][words[i][j]]++;
                maxJ = max(j, maxJ);
            }
        }

        vector<vector<long>> memo(maxJ + 1, vector<long>(target.size() + 1, -1));

        function<long(int, int)> dp = [&] (int i, int j) {
            if (j >= target.size()) {
                return 1l;
            }
            if (i > maxJ) {
                return 0l;
            }
            if (memo[i][j] != -1) return memo[i][j];
            long ans = dp(i + 1, j) % mod;

            if (letterFreq[i][target[j]] > 0) {
                ans += (letterFreq[i][target[j]] * dp(i + 1, j + 1)) % mod;
            }
            memo[i][j] = ans % mod;
            return memo[i][j];
        };

        return dp(0, 0);
    }
};