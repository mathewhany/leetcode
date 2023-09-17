class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        int n = nums.size();
        stack<pair<int, long>> s;

        long ans = 0;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            long sum = 0;
            while (s.size() && s.top().first >= num) {
                ans = max(
                    ans,
                    (sum + s.top().second) * s.top().first
                );
                sum += s.top().second;
                s.pop();
            }
            sum += num;
            s.push(make_pair(num, sum));
        }
        long sum = 0;
        while (s.size()) {
            sum += s.top().second;
            ans = max(
                sum * s.top().first,
                ans
            );
            s.pop();
        }

        return ans % int(1e9 + 7);
    }
};