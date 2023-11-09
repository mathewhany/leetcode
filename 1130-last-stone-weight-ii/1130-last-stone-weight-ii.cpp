class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = accumulate(stones.begin(), stones.end(), 0);
        int target = sum / 2;

        vector<vector<long>> memo(stones.size() + 1, vector<long>(sum + 1, -1));

        long ans = dp(stones, 0, 0, target, memo);

        return sum - 2 * ans;
    }

    int dp(vector<int>& stones, int i, long current, int target, vector<vector<long>>& memo) {
        if (memo[i][current] != -1) return memo[i][current];

        if (i >= stones.size()) return current;

        long without = dp(stones, i + 1, current, target, memo);
        long with = current + stones[i] <= target ? dp(stones, i + 1, current + stones[i], target, memo) : 0;

        long ans = max(without, with);
        memo[i][current] = ans;

        return ans;
    }
};