class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> zippedNums;
        int n = nums1.size();
        for (int i = 0; i < n; i++) zippedNums.push_back(make_pair(nums2[i], nums1[i]));

        sort(zippedNums.begin(), zippedNums.end(), greater<>());
        priority_queue<int, vector<int>, greater<int>> window;
        long currentSum = 0;
        long ans = LONG_MIN;
        for (int i = 0; i < n; i++) {
            auto [currentMin, currentVal] = zippedNums[i];
            
            if (window.size() == k) {
                currentSum -= window.top();
                window.pop();
            }

            window.push(currentVal);
            currentSum += currentVal;

            if (window.size() == k) {
                ans = max(ans, currentMin * currentSum);
            }
        }

        return ans;
    }
};