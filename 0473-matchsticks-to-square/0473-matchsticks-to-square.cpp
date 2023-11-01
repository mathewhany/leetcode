class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        sort(matchsticks.begin(), matchsticks.end(), less<int>());
        int n = matchsticks.size();
        int sum = 0;
        for (int i = 0; i < n; i++) sum += matchsticks[i];
        if (sum % 4) return false;
        int sideLen = sum / 4;

        vector<int> sides(4, 0);

        function<bool(int, int)> backtrack = [&] (int i, int j) {
            if (i >= n) {                if (j >= 4) return true;
                if (sides[j] < sideLen) return false;
                return backtrack(0, j + 1);
            }

            if (backtrack(i + 1, j)) return true;


            if (matchsticks[i] > 0 && matchsticks[i] + sides[j] <= sideLen) {
                int stick = matchsticks[i];
                sides[j] += stick;
                matchsticks[i] = 0;
                if (backtrack(i + 1, j)) return true;
                matchsticks[i] = stick;
                sides[j] -= stick;
            }

            return false;
        };

        return backtrack(0, 0);
    }
};