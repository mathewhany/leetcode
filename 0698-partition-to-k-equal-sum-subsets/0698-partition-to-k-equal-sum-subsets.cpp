class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k) return false;
        int target = sum / k;
        int n = nums.size();

        vector<int> groups(k, 0);

        bool visited[17][17][1 << 16];
        bool memo[17][17][1 << 16];
        memset(visited, false, sizeof(visited));
        memset(memo, false, sizeof(visited));

        function<bool(int, int, int)> backtrack = [&](int i, int j, int mask) {
            if (visited[i][j][mask]) return memo[i][j][mask];

            if (j >= k) {
                return true;
            }

            if (i >= n) {
                if (groups[j] == target) {
                    bool ans = backtrack(0, j + 1, mask);
                    visited[i][j][mask] = true;
                    memo[i][j][mask] = ans;
                    return ans;
                }

                return false;
            }

            bool ans = backtrack(i + 1, j, mask);

            if (ans) return true;

            if (((1 << i) & mask) == 0) {
                groups[j] += nums[i];
                ans = backtrack(i + 1, j, mask | (1 << i));
                groups[j] -= nums[i];
            }

            visited[i][j][mask] = true;
            memo[i][j][mask] = ans;

            return ans;
        };

        return backtrack(0, 0, 0);
    }
};