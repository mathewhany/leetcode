class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.size()) return "0";

        vector<int> st;

        for (int i = 0; i < num.size(); i++) {
            int n = num[i] - '0';

            while (k > 0 && st.size() && st[st.size() - 1] > n) {
                st.pop_back();
                k--;
            }

            st.push_back(n);
        }

        while (k > 0) {
            st.pop_back();
            k--;
        }
        
        string ans;
        bool isPrefix = true;

        for (int i = 0; i < st.size(); i++) {
            if (isPrefix) {
                if (st[i]) {
                    isPrefix = false;
                    ans += to_string(st[i]);
                }
            } else {
                ans += to_string(st[i]);
            }
        }

        if (!ans.size()) return "0";

        return ans;
    }
};