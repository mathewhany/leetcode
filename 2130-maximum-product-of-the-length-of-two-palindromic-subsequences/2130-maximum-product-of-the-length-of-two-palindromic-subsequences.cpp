class Solution {
public:
    int maxProduct(string s) {
        unordered_map<int, int> palindromeToLength;

        for (int i = 1; i < 1 << s.size(); i++) {
            string candidate = "";

            for (int j = 0; j < s.size(); j++) {
                if (i & (1 << j)) {
                    candidate += s[j];
                }
            }
            
            bool isPalindrome = true;
            for (int j = 0; j < candidate.size() / 2; j++) {
                if (candidate[j] != candidate[candidate.size() - 1 - j]) {
                    isPalindrome = false;
                    break;
                }
            }

            if (isPalindrome) {
                palindromeToLength[i] = candidate.size();
            }
        }

        int best = 0;

        for (auto const &[palindrome1, length1] : palindromeToLength) {
            for (auto const &[palindrome2, length2] : palindromeToLength) {
                if (!(palindrome1 & palindrome2)) {
                    best = max(best, length1 * length2);
                }
            }
        }

        return best;
    }
};