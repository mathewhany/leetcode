class Solution {
public:
    int rearrangeSticks(int n, int k) {    
        vector<vector<long>> memo(n + 1, vector<long>(k + 1, -1));
        long ans = dp(n, k, memo);

        return ans % int(1e9 + 7);
    }

private:
    long dp(int n, int k, vector<vector<long>>& memo) {
        if (memo[n][k] != -1) return memo[n][k];

        if (n < k) return -1;

        if (n == k) return 1;

        if (k == 0) return -1;

        long opt1 = dp(n - 1, k - 1, memo);
        long opt2 = dp(n - 1, k, memo);

        long ans = 0;
        if (opt1 >= 0) ans += opt1;
        if (opt2 >= 0) ans += (n - 1) * opt2;
        
        ans %= int(1e9 + 7);

        memo[n][k] = ans;

        return ans;
    }
};