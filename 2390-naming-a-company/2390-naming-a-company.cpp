class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        unordered_set<string> prefix_to_suffixes[26];

        for (auto const &idea : ideas) {
            int prefix = idea[0] - 'a';
            string suffix = idea.substr(1);
        
            prefix_to_suffixes[prefix].insert(suffix);
        }

        long ans = 0;

        for (int i = 0; i < 26; i++) {
            for (int j = i + 1; j < 26; j++) {
                long c1 = 0;
                long c2 = 0;

                for (auto const& suffix : prefix_to_suffixes[i]) {
                    if (!prefix_to_suffixes[j].count(suffix)) c1++;
                }
                for (auto const& suffix : prefix_to_suffixes[j]) {
                    if (!prefix_to_suffixes[i].count(suffix)) c2++;
                }
                ans += c1 * c2;
            }
        }

        return ans * 2;
    }
};