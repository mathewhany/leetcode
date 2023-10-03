class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> r, d;
        for (int i = 0; i < senate.size(); i++) {
            if (senate[i] == 'R') {
                r.push(i);
            } else {
                d.push(i);
            }
        }

        int i = senate.size();
        while (r.size() && d.size()) {
            if (r.front() < d.front()) {
                d.pop();
                r.pop();
                r.push(i);
            } else {
                r.pop();
                d.pop();
                d.push(i);
            }

            i++;
        }

        if (r.size()) {
            return "Radiant";
        } else {
            return "Dire";
        }
    }
};