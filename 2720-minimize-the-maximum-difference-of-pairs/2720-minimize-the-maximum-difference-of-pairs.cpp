class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());
        int lo = 0, hi = nums[nums.size() - 1];
        int ans;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;            
            int pairCount = 0;

            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] - nums[i - 1] <= mid ) {
                    pairCount++;
                    i++;
                }
            }

            if (pairCount >= p) {
                hi = mid - 1;
                ans = mid;
            } else {
                lo = mid + 1;
            }
        }

        return ans;
    }
};