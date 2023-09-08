class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        unordered_map<int, int> node1Dist;
        unordered_map<int, int> node2Dist;
        
        int curr1 = node1;
        int dist1 = 0;

        while (curr1 != -1 && node1Dist.count(curr1) == 0) {
            node1Dist[curr1] = dist1++;
            curr1 = edges[curr1];
        }

        int curr2 = node2;
        int dist2 = 0;

        while (curr2 != -1 && node2Dist.count(curr2) == 0) {
            node2Dist[curr2] = dist2++;
            curr2 = edges[curr2];
        }

        int bestNode = -1;
        int bestDist = INT_MAX;

        for (const auto &[node1, dist1] : node1Dist) {
            if (node2Dist.count(node1)) {
                int dist2 = node2Dist[node1];
                int maxDist = max(dist1, dist2);
                if (maxDist == bestDist) {
                    bestNode = bestNode == -1 ? node1 : min(bestNode, node1);
                } else if (maxDist < bestDist) {
                    bestNode = node1;
                    bestDist = maxDist;
                }
            }
        }

        return bestNode;
    }
};