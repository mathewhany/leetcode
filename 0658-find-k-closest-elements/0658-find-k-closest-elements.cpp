class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int lo = 0;
        int hi = arr.size() - k;
        int ans = 0;

        function<bool(int)> ok = [&] (int mid) {
            if (mid + k >= arr.size()) return false;
            
            if (x >= arr[mid + k]) return true;

            if (x <= arr[mid]) return false;

            return arr[mid + k] - x  < x - arr[mid];
        };

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (ok(mid)) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
                ans = mid;
            }
        }

        vector<int> ansVec;
        for (int i = 0; i < k; i++) {
            ansVec.push_back(arr[ans + i]);
        }

        return ansVec;
    }
};