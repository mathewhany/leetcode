class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<unordered_set<string>> groups(26);

        for (int i = 0; i < ideas.size(); i++) {
            char prefix = ideas[i][0];
            string suffix = ideas[i].substr(1);
            
            groups[prefix - 'a'].insert(suffix);
        }

        long ans = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = i + 1; j < 26; j++) {
                long count1 = 0, count2 = 0;

                for (auto const suffix : groups[i]) {
                    if (groups[j].find(suffix) == groups[j].end()) {
                        count1++;
                    }
                }

                for (auto const suffix : groups[j]) {
                    if (groups[i].find(suffix) == groups[i].end()) {
                        count2++;
                    }
                }

                ans += count1 * count2;
            }
        }

        return ans * 2;
    }
};