class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<int> ans;

        int start = 0;
        int end = nums.size() - 1;

        while (start < end) {
            ans.push_back(nums[start++]);
            ans.push_back(nums[end--]);
        }

        if (start == end) {
            ans.push_back(nums[start]);
        }

        return ans;
    }
};