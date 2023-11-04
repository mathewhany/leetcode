class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        vector<vector<int>> graph(bombs.size());
        for (int i = 0; i < bombs.size(); i++) {
            for (int j = i + 1; j < bombs.size(); j++) {
                int x1 = bombs[i][0];
                int x2 = bombs[j][0];
                int y1 = bombs[i][1];
                int y2 = bombs[j][1];
                long r1 = bombs[i][2];
                long r2 = bombs[j][2];

                long dx = x1 - x2;
                long dy = y1 - y2;

                long d_sq = dx * dx + dy * dy;

                if (d_sq <= r1 * r1) {
                    graph[i].push_back(j);
                }
                if (d_sq <= r2 * r2) {
                    graph[j].push_back(i);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < bombs.size(); i++) {
            vector<bool> inPath(bombs.size());
            ans = max(dfs(i, inPath, graph), ans);
        }

        return ans;
    }

    int dfs(int i, vector<bool>& inPath, vector<vector<int>>& graph) {
        if (inPath[i]) return 0;

        inPath[i] = true;

        int count = 1;
        for (const auto &j : graph[i]) {
            count += dfs(j, inPath, graph);
        }

        return count;
    };
};