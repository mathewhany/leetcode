class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> freq;
        priority_queue<pair<int, char>> pq;
        for (auto const &c : s) freq[c]++;
        for (auto const &[c, f] : freq) pq.emplace(f, c);

        string ans = "";
        pair<int, char> prev;
        bool hasPrev = false;

        while (pq.size()) {
            auto [f, c] = pq.top();
            pq.pop();
            ans += c;

            if (hasPrev) {
                pq.push(prev);
            }

            prev = make_pair(f - 1, c);
            hasPrev = f - 1 > 0;
        }

        return hasPrev ? "" : ans;
    }
};