class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        bool skip = false;
        int ans = 0;

        for (auto const& x : flowerbed) {
            if (skip) {
                skip = false;
                continue;
            }

            if (x == 1) {
                ans += count / 2;
                count = 0;
                skip = true;
            } else {
                count += 1;
            }
        }

        return ans + (count + 1) / 2 >= n;   
    }
};