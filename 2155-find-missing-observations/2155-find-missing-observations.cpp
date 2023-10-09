class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int mSum = 0;
        int m = rolls.size();

        for (int i = 0; i < rolls.size(); i++) {
            mSum += rolls[i];
        }

        vector<int> ans;

        int nSum = mean * (n + m) - mSum;

        if (nSum / n > 0 && nSum / n < 6 || nSum / n == 6 && nSum % n == 0) {
            for (int i = 0; i < n; i++) {
                ans.push_back(nSum / n);
            }
            for (int i = 0; i < nSum % n; i++) {
                ans[i]++;
            }
        }

        return ans;
    }
};