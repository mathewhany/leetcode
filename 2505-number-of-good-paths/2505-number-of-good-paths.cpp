class UnionFind {
public:
  UnionFind(int n) : nodeToParent(vector(n, -1)), rank(vector(n, 0)) {
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

private:
  vector<int> nodeToParent;
  vector<int> rank;
};

class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
      int n = vals.size();

      vector<vector<int>> nodeToNeighbors(n);
      for (int i = 0; i < edges.size(); i++) {
        nodeToNeighbors[edges[i][0]].push_back(edges[i][1]);
        nodeToNeighbors[edges[i][1]].push_back(edges[i][0]);
      }

      map<int, vector<int>> valToNodes;
      for (int i = 0; i < n; i++) valToNodes[vals[i]].push_back(i);

      UnionFind uf(n);

      long ans = n;

      for (auto const &[val, nodes] : valToNodes) {
        unordered_map<int, int> rootToValCount;
        for (auto const &node : nodes) {
          rootToValCount[uf.findRoot(node)] = 1;
        }
        for (auto const &node : nodes) {
          for (auto const& neighbor : nodeToNeighbors[node]) {
            if (vals[neighbor] <= vals[node]) {
              int neighborRoot = uf.findRoot(neighbor);
              int nodeRoot = uf.findRoot(node);
              if (neighborRoot == nodeRoot) continue;
              int neighborCount = rootToValCount[neighborRoot];
              int nodeCount = rootToValCount[nodeRoot];
              uf.unionRoots(node, neighbor);
              int newRoot = uf.findRoot(node);
              rootToValCount.erase(neighborRoot);
              rootToValCount.erase(nodeRoot);
              rootToValCount[newRoot] += neighborCount + nodeCount;
            }
          }
        }
        for (auto const &[root, valCount] : rootToValCount) {
          ans += ((valCount - 1) * valCount) / 2;
        }
      }

      return ans;
    }
};