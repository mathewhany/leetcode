class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        val = 0

        for i in range(len(s)):
            if i < len(s) - 1 and sym_to_val[s[i]] < sym_to_val[s[i + 1]]:
                val -= sym_to_val[s[i]]
            else:
                val += sym_to_val[s[i]]
        
        return val
