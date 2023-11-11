class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        long sumLargest = 0, sumSmallest = 0, total = 0, smallest = LONG_MAX, largest = LONG_MIN;

        for (int i = 0; i < nums.size(); i++) {
            long n = nums[i];
            sumLargest = max(n, sumLargest + n);
            largest = max(sumLargest, largest);
            sumSmallest = min(n, sumSmallest + n);
            smallest = min(sumSmallest, smallest);
            total += n;
        }

        return max(
            largest,
            total != smallest ? total - smallest : LONG_MIN
        );
    }
};