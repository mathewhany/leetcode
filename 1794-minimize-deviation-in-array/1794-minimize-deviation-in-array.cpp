class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        int n = nums.size();
        int maxVal = INT_MIN;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;
        
        for (int i = 0; i < n; i++) {
            int value = nums[i];
            int limit = nums[i] % 2 == 0 ? nums[i] : nums[i] * 2;

            while (value % 2 == 0) {
                value /= 2;
            }

            maxVal = max(maxVal, value);
            queue.push(make_pair(value, limit));
        }

        int ans = INT_MAX;

        while (true) {
            auto [minVal, minLimit] = queue.top();
            
            ans = min(ans, maxVal - minVal);

            if (minVal * 2 > minLimit) {
                break;
            } else if (minVal * 2 > maxVal) {
                maxVal = minVal * 2;
            }

            queue.pop();
            queue.push(make_pair(minVal * 2, minLimit));
        }

        return ans;
    }
};