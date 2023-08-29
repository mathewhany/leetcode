/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    unordered_map<string, int> counts;
    vector<TreeNode*> duplicates;

public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        dfs(root);
        return duplicates;
    }

private:
    string dfs(TreeNode* node) {
        if (!node) return "-";

        string left = dfs(node->left);
        string right = dfs(node->right);

        string current = "(" + to_string(node->val) + " " + left + " " + right + ")";

        counts[current]++;

        if (counts[current] == 2) {
            duplicates.push_back(node);
        }

        return current;
    }
};