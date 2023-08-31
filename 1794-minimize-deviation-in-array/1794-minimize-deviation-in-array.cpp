class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        int n = nums.size();
        int minVal = INT_MAX;
        priority_queue<int> pq;
        
        for (int i = 0; i < n; i++) {
            int value = nums[i] % 2 == 1 ? nums[i] * 2 : nums[i];
            minVal = min(minVal, value);
            pq.push(value);
        }

        int ans = pq.top() - minVal;
        while (pq.top() % 2 == 0) {
            int val = pq.top() / 2;
            minVal = min(minVal, val); 
            pq.pop();
            pq.push(val);
            ans = min(ans, pq.top() - minVal);
        }

        return ans;
    }
};