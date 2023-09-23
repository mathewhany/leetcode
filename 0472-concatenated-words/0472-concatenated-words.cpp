class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        sort(words.begin(), words.end(), [] (const string& a, const string& b) {
            return a.size() < b.size();
        });

        unordered_set<string> shorterWords;
        unordered_map<string, bool> memo;

        function<bool(string&)> canBeConstructedFromShorterWords = [&] (string& word) {
            if (memo.count(word)) return memo[word];
            
            if (word.size() == 0) return true;

            for (int j = word.size(); j >= 1; j--) {
                string prefix = word.substr(0, j);
                string suffix = word.substr(j, word.size() - j);

                if (shorterWords.count(prefix)) {
                    if (shorterWords.count(suffix) || canBeConstructedFromShorterWords(suffix)) {
                        memo[word] = true;
                        return true;
                    }
                }
            }

            memo[word] = false;
            return false;
        };

        vector<string> ans;
        for (int i = 0; i < words.size(); i++) {
            if (canBeConstructedFromShorterWords(words[i])) {
                ans.push_back(words[i]);
            }
            shorterWords.insert(words[i]);
        }

        return ans;
    }
};