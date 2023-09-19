class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> length(n, 0), cnt(n, 0);

        for (int i = 0; i < n; i++) {
            int maxLength = 0;
            int maxLengthCnt = 1;

            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    if (length[j] > maxLength) {
                        maxLength = length[j];
                        maxLengthCnt = cnt[j];
                    } else if (length[j] == maxLength) {
                        maxLengthCnt += cnt[j];
                    }
                }
            }

            length[i] = maxLength + 1;
            cnt[i] = maxLengthCnt;
        }

        int maxLen = 0;
        int maxLenCnt = 1;

        for (int i = 0; i < n; i++) {
            if (length[i] == maxLen) {
                maxLenCnt += cnt[i];
            } else if (length[i] > maxLen) {
                maxLen = length[i];
                maxLenCnt = cnt[i];
            }
        }
        
        return maxLenCnt;
    }
};