class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        long windowSum = 0;
        int windowStart = 0;
        int best = 0;

        for (int i = 0; i < nums.size(); i++) {
            windowSum += nums[i];
            long required = long(i - windowStart + 1) * nums[i] - windowSum;
            while (required > k) {
                windowSum -= nums[windowStart];
                windowStart++;
                required = long(i - windowStart + 1) * nums[i] - windowSum;
            }
            best = max(best, i - windowStart + 1);
        }

        return best;
    }
};