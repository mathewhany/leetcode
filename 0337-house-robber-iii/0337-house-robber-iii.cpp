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
public:
    int rob(TreeNode* root) {
        function<pair<int, int>(TreeNode*)> dfs = [&](TreeNode* node) {
            if (!node) return make_pair(0, 0);

            auto [withLeft, withoutLeft] = dfs(node->left);
            auto [withRight, withoutRight] = dfs(node->right);

            return make_pair(
                max(node->val + withoutLeft + withoutRight, withLeft + withRight),
                withLeft + withRight
            );
        };
        
        auto [with, without] = dfs(root);

        return max(with, without);
    }
};