class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = 0;
        for (const auto &s : stones) sum += s;

        vector<vector<int>> memo(sum / 2 + 1, vector<int>(stones.size() + 1, 0));
        vector<vector<bool>> visited(sum / 2 + 1, vector<bool>(stones.size() + 1, false));
        
        return sum - 2 * dp(stones, sum / 2, 0, 0, memo, visited);
    }

private:
    int dp(vector<int>& stones, int bound, int sum, int i, vector<vector<int>>& memo, vector<vector<bool>>& visited) {
        if (visited[sum][i]) return memo[sum][i];

        if (i >= stones.size()) return sum;

        visited[sum][i] = true;

        if (stones[i] + sum > bound) {
            memo[sum][i] = dp(stones, bound, sum, i + 1, memo, visited);
            return memo[sum][i];
        }

        memo[sum][i] = max(
            dp(stones, bound, sum + stones[i], i + 1, memo, visited),
            dp(stones, bound, sum, i + 1, memo, visited)
        );

        return memo[sum][i];
    }
};