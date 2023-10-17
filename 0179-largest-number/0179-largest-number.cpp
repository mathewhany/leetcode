class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [&] (int const &a, int const &b) {
            return to_string(a) + to_string(b) > to_string(b) + to_string(a);
        });

        if (nums.size() && nums[0] == 0) return "0";

        stringstream ans;
        for (int i = 0; i < nums.size(); i++) ans << to_string(nums[i]);

        return ans.str();
    }
};