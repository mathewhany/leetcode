class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int, int> numToFreq;
        for (int i = 0; i < nums.size(); i++) numToFreq[nums[i]]++;
        
        vector<long> freqs;
        vector<long> uniqueNums;
        int n = numToFreq.size();
        for (auto const &[num, freq] : numToFreq) {
            freqs.push_back(freq);
            uniqueNums.push_back(num);
        }

        vector<long> dp(n + 1, 0);

        for (int i = n - 1; i >= 0; i--) {
            long num  = uniqueNums[i];
            long freq = freqs[i];

            if (i == n - 1) {
                dp[i] = num * freq;
            } else {
                dp[i] = max(
                    dp[i + 1],
                    num * freq + dp[num + 1 == uniqueNums[i + 1] ? i + 2 : i + 1]
                );
            }
        }

        return dp[0];
    }
};