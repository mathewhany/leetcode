class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        unordered_map<int, vector<int>> detonationMap;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int bomb1X = bombs[i][0];
                int bomb1Y = bombs[i][1];
                long bomb1R = bombs[i][2];
                int bomb2X = bombs[j][0];
                int bomb2Y = bombs[j][1];
                long bomb2R = bombs[j][2];

                long dx = bomb1X - bomb2X;
                long dy = bomb1Y - bomb2Y;

                long d = dx * dx + dy * dy;

                if (bomb1R * bomb1R >= d) {
                    detonationMap[i].push_back(j);
                }

                if (bomb2R * bomb2R >= d) {
                    detonationMap[j].push_back(i);
                }
            }
        }

        long ans = INT_MIN;

        for (int i = 0; i < n; i++) {
            vector<bool> visited(n, false);
            ans = max(ans, dfs(detonationMap, i, visited));
        }

        return ans;
    }

    long dfs(unordered_map<int, vector<int>>& detonationMap, int i, vector<bool>& visited) {
        if (visited[i]) return 0;

        visited[i] = true;

        long count = 1;
        
        for (auto const& nextBomb : detonationMap[i]) {
            count += dfs(detonationMap, nextBomb, visited);
        }
        
        return count;
    }
};