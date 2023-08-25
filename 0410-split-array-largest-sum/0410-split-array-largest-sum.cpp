class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int lo = 0;
        int hi = 1e9;
        int ans = INT_MAX;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (ok(mid, k, nums)) {
                hi = mid - 1;
                ans = mid;
            } else {
                lo = mid + 1;
            }
        }

        return ans;
    }

private:
    bool ok(int target, int k, vector<int>& nums) {
        int currentSum = 0;
        int count = 1;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > target) return false;
            
            if (currentSum + nums[i] <= target) {
                currentSum += nums[i];
            } else {
                currentSum = nums[i];
                count++;
            }
        }

        return count <= k;
    }
};