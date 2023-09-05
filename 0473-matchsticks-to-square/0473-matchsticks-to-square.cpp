class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        sort(matchsticks.begin(), matchsticks.end(), greater<>());
        int sum = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if (sum % 4) return false;
        int target = sum / 4;
        vector<int> sides = {0, 0, 0, 0};

        function<bool(int)> backtrack = [&](int i) {
            if (i >= matchsticks.size()) {
                return true;
            }

            for (int j = 0; j < 4; j++) {
                if (sides[j] + matchsticks[i] > target) continue;

                sides[j] += matchsticks[i];
                if (backtrack(i + 1)) return true;
                sides[j] -= matchsticks[i];
            }

            return false;
        };

        return backtrack(0);
    }
};