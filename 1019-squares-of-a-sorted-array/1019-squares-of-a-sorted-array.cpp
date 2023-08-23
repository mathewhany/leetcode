class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        vector<int> ans;

        while (left <= right) {
            if (abs(nums[right]) > abs(nums[left])) {
                ans.push_back(nums[right] * nums[right]);
                right--;
            } else {
                ans.push_back(nums[left] * nums[left]);
                left++;
            }
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};