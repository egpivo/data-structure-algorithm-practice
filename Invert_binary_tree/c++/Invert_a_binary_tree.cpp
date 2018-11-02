//
//  Invert_a_binary_tree.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/10/31.
//

#include <stdio.h>

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
    TreeNode* invertTree(TreeNode* root) {
        
        TreeNode *temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(tmp);
        
        return root;
    }
};
