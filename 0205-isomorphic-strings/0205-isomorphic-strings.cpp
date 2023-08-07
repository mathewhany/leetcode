class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_set<char> setS(s.begin(), s.end());
        unordered_set<char> setT(t.begin(), t.end());
        unordered_set<string> setST;

        for (int i = 0; i < s.size(); i++) {
            ;

            setST.insert(string { s[i], ',', t[i] });    
        }

        return setS.size() == setT.size() && setT.size() == setST.size();
    }
};