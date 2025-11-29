//  Depth first search(DFS)
//  Minimum_depth_of_binary_tree.cpp
//
//
//  Created by Wen-Ting Wang on 2018/11/2.
//

#include<iostream>

using namespace std;


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
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(!root->left && !root->right) return 1;

        if(!root->left) return minDepth(root->right) + 1;
        else if(!root->right) return minDepth(root->left) +1;
        else return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};

//top-down
//ref http://www.voidcn.com/article/p-mquqvehe-bez.html
void Show(TreeNode *t) {
    if (!t) return;

    cout << t->val << " ";
    Show(t->left);
    Show(t->right);
}


int main(){

    TreeNode *root = new TreeNode(3);

    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Show(root);
    Solution ans;

    cout <<"\n The answer: " <<  ans.minDepth(root)<<endl;

    return 0;
}
