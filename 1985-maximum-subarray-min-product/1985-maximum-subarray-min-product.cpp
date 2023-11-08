class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        stack<pair<int, long>> st;
        long best = 0;

        for (int i = 0; i < nums.size(); i++) {
            long sum = 0;
            while (st.size() && st.top().first >= nums[i]) {
                auto &[min, subSum] = st.top(); st.pop();
                sum += subSum;
                best = max(best, min * sum);
            }
            sum += nums[i];
            st.push(make_pair(nums[i], sum));
        }

        long sum = 0;
        while (st.size()) {
            auto &[min, subSum] = st.top(); st.pop();
            sum += subSum;
            best = max(best, min * sum);
        }

        return best % int(1e9 + 7);
    }
};