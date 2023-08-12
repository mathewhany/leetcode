class Solution {
public:
    int partitionString(string s) {
        int minCount = 1;
        unordered_set<char> window;

        for (int i = 0; i < s.size(); i++) {
            if (window.count(s[i])) {
                window.clear();
                minCount += 1;
            }
            
            window.insert(s[i]);    
        }

        return minCount;
    }
};