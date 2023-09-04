class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> pq;
        if (a > 0) pq.emplace(a, 'a');
        if (b > 0) pq.emplace(b, 'b');
        if (c > 0) pq.emplace(c, 'c');
        
        string ans = "";
        pair<int, char> blocked;
        bool hasBlocked = false;

        while (pq.size()) {
            auto [f, c] = pq.top();
            pq.pop();
            ans += c;
            
            if (hasBlocked) {
                pq.push(blocked);
                hasBlocked = false;
            }

            if (f > 1) {
                if (ans.size() >= 2 && ans[ans.size() - 2] == c) {
                    blocked = make_pair(f - 1, c);
                    hasBlocked = true;
                } else {
                    pq.emplace(f - 1, c);
                }
            }
        }

        return ans;
    }
};