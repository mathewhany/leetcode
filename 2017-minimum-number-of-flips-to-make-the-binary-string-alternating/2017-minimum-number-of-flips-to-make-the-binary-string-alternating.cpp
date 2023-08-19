class Solution {
public:
    int minFlips(string s) {
        string alternating01 = "";
        string alternating10 = "";

        for (int i = 0; i < 2 * s.size(); i++) {
            if (i % 2 == 0) {
                alternating01 += "0";
                alternating10 += "1";
            } else {
                alternating01 += "1";
                alternating10 += "0";
            }
        }

        int flips01 = 0;
        int flips10 = 0;

        int ans = INT_MAX;

        for (int i = 0; i < 2 * s.size() - 1; i++) {
            if (i < s.size()) {
                if (s[i] != alternating01[i]) {
                    flips01++;
                }

                if (s[i] != alternating10[i]) {
                    flips10++;
                }
            } else {
                if (s[i - s.size()] != alternating01[i - s.size()]) {
                    flips01--;
                }

                if (s[i - s.size()] != alternating10[i - s.size()]) {
                    flips10--;
                }

                if (s[i % s.size()] != alternating01[i]) {
                    flips01++;
                }

                if (s[i % s.size()] != alternating10[i]) {
                    flips10++;
                }
            }

            if (i >= s.size() - 1) {
                ans = min(ans, min(flips01, flips10));
            }
        }

        return ans;
    }
};