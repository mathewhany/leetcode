class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        long total = 0;
        long best = 0;

        for (int i = 0; i < nums.size(); i++) {
            total += nums[i];
            long size = i - left + 1;
            long target = nums[i];
            long diff = target * size - total;

            while (diff > k) {
                total -= nums[left];
                left++;
                size--;
                diff = target * size - total;
            }

            best = max(best, size);
        }

        return best;
    }
};