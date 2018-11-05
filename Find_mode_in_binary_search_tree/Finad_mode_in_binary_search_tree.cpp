//
//  Finad_mode_in_binary_search_tree.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/2.
//

#include<iostream>
#include<vecotr>
/**
 * Definition for a binary tree node.
*/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        
        unordered_map<int, int> map;
        inorder(root, m, mx);
        
        for()
        
    }
    
private:
    void inorder(TreeNode* node, unordered_map<int, int>& m, int& mx) {
        
        if (!node) return;
        inorder(node->left, m, mx);
        mx = max(mx, ++m[node->val]);
        inorder(node->right, m, mx);
    }
};
