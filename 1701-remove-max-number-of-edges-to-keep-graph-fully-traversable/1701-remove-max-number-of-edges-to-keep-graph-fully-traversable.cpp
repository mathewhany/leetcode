class UnionFind {
public:
    UnionFind(int n) : nodeToParent(vector(n, -1)), rank(vector(n, 0)), count(n) {
    }

    int findRoot(int node) {
        int parent = nodeToParent[node];
        
        if (parent == -1) return node;

        int root = findRoot(parent);
        nodeToParent[node] = root;

        return root;
    }

    void unionRoots(int node1, int node2) {
        int root1 = findRoot(node1), root2 = findRoot(node2);
        if (root1 == root2) return;
        count--;
        
        int rank1 = rank[root1], rank2 = rank[root2];

        if (rank1 == rank2) {
        nodeToParent[root1] = root2;
        rank[root2]++;
        } else if (rank1 < rank2) {
        nodeToParent[root2] = root1;
        rank[root1]++;
        } else {
        nodeToParent[root1] = root2;
        rank[root2]++;
        }
    }

    bool isConnected(int node1, int node2) {
        return findRoot(node1) == findRoot(node2);
    }

    int getCount() {
        return count;
    }
private:
    int count;
    vector<int> nodeToParent;
    vector<int> rank;
};

#define TYPE_ALICE 1
#define TYPE_BOB 2
#define TYPE_BOTH 3

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        unordered_set<int> nodes;
        for (int i = 0; i < edges.size(); i++) {
            edges[i][1]--;
            edges[i][2]--;
            nodes.insert(edges[i][1]);
            nodes.insert(edges[i][2]);
        }
        UnionFind ufAlice(nodes.size()), ufBob(nodes.size());
        int edgesUsed = 0;

        for (int i = 0; i < edges.size(); i++) {
            if (edges[i][0] == TYPE_BOTH) {
                bool edgeUsed = false;
                if (!ufAlice.isConnected(edges[i][1], edges[i][2])) {
                    ufAlice.unionRoots(edges[i][1], edges[i][2]);
                    edgeUsed = true;
                }
                if (!ufBob.isConnected(edges[i][1], edges[i][2])) {
                    ufBob.unionRoots(edges[i][1], edges[i][2]);
                    edgeUsed = true;
                }
                if (edgeUsed) edgesUsed++;
            }
        }

        for (int i = 0; i < edges.size(); i++) {
            if (edges[i][0] == TYPE_ALICE) {
                if (!ufAlice.isConnected(edges[i][1], edges[i][2])) {
                    ufAlice.unionRoots(edges[i][1], edges[i][2]);
                    edgesUsed++;
                }
            } else if (edges[i][0] == TYPE_BOB) {
                if (!ufBob.isConnected(edges[i][1], edges[i][2])) {
                    ufBob.unionRoots(edges[i][1], edges[i][2]);
                    edgesUsed++;
                }
            }
        }

        if (ufAlice.getCount() != 1 || ufBob.getCount() != 1) {
            return -1;
        }

        return edges.size() - edgesUsed;
    }
};