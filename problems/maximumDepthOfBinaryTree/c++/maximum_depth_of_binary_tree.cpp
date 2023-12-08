//
//  Maximum_depth_of_binary_tree.cpp
//  DFS problem
//
//  Created by Wen-Ting Wang on 2018/11/14.
//

#include <iostream>
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
    int maxDepth(TreeNode* root) {

        if(!root) return 0;
        else if(!root->left && !root->right) return 1;
        else
            return max(maxDepth(root->left), maxDepth(root->right)) + 1;
     /* redundat code
     //   if(root->left && root->right) return max(maxDepth(root->left), maxDepth(root->right)) + 1;
     //   else if(root->left) return maxDepth(root->left) + 1;
     //   else return maxDepth(root->right)+1;
      */
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

    cout <<"\n The answer: " <<  ans.maxDepth(root)<<endl;

    return 0;
}
