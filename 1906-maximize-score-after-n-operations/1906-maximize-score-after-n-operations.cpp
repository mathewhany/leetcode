class Solution {
public:
    int maxScore(vector<int>& nums) {
        int n = nums.size() / 2;
        vector<vector<long>> memo(n + 1, vector<long>(1 << (2 * n), 0));
        vector<vector<bool>> visited(n + 1, vector<bool>(1 << (2 * n), false));

        function<long(int, int)> dp = [&](int i, int mask) {
            if (i > n) {
                return 0l;
            }

            if (visited[i][mask]) return memo[i][mask];


            long best = 0;

            for (int j = 0; j < 2 * n; j++) {
                for (int k = 0; k < 2 * n; k++) {
                    int jMask = 1 << j;
                    int kMask = 1 << k;
                    if (jMask & kMask || ((jMask | kMask) & mask)) continue;

                    int newMask = jMask | kMask | mask;
                    long score = i * __gcd(nums[j], nums[k]);

                    best = max(
                        score + dp(i + 1, newMask),
                        best
                    );
                }
            }

            visited[i][mask] = true;
            memo[i][mask] = best;

            return best;
        };

        return dp(1, 0);
    }
};