class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());

        int lo = 0;
        int hi = 1e9;
        int ans = -1;

        function<bool(int)> ok = [&](int thresh) {
            int count = 0;
            for (int i = 0; i < nums.size() - 1; i++) {
                if (nums[i + 1] - nums[i] <= thresh) {
                    count++;
                    i++;
                }
            }
            return count >= p;
        };

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (ok(mid)) {
                hi = mid - 1;
                ans = mid;
            } else {
                lo = mid + 1;
            }
        }

        return ans;
    }
};