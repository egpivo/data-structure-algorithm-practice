//
//  invert_a_binary_tree.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/10/31.
//

#include<iostream>
#include<vector>

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
    TreeNode* invertTree(TreeNode* root) {
        
        if(!root) return NULL;
        
        TreeNode *temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
        return root;
    }
};

// ref: https://stackoverflow.com/questions/34077497/how-to-print-out-a-binary-tree-in-order
void inorder(TreeNode* node)
{
    if (!node) return;// end the recursion if node == nullptr
        
    inorder(node->left);            // display the left subtree
    std::cout << node->val << " "; // display the current node
    inorder(node->right);           // display the right subtree
}

//top-down
//ref http://www.voidcn.com/article/p-mquqvehe-bez.html
void Show(TreeNode *t) {
    if (!t) return;
    
    cout << t->val << " ";
    Show(t->left);
    Show(t->right);
}

TreeNode *Insert(int x, TreeNode *root) {
    
    if (root == NULL) {
        root = new TreeNode(0);//(TreeNode *)malloc(sizeof(struct TreeNode));
        if (root == NULL) return NULL;
        else{
            root->val = x;
            root->left = NULL;
            root->right = NULL;
        }
        
    }
    else{
        if (x < root->val) root->left=Insert(x,root->left);
        else if (x > root->val) root->right=Insert(x,root->right);
    }
    return root;
}

int main(){
    
    vector<int> num; //c++11 = {4,2,7,1,3,6,9};
    num.push_back(4);
    num.push_back(2);
    num.push_back(7);
    num.push_back(1);
    num.push_back(3);
    num.push_back(6);
    num.push_back(9);
    
    TreeNode* root = NULL;
    
    //for (auto s1 = num.begin(); s1 != num.end(); ++s1) { //c++11
    for(int i = 0; i < num.size(); ++i){
        root = Insert(num[i],root);
    }
    Show(root);
    Solution ans;
    ans.invertTree(root);
    cout <<"\n The answer: " << endl;
    Show(root);
    
    //TreeNode *root = new TreeNode(4);
    
    //root->left = new TreeNode(2);
    //root->left->left = new TreeNode(1);
    //root->left->right = new TreeNode(3);
    //root->right = new TreeNode(7);
    //root->right->left = new TreeNode(6);
    //root->right->right = new TreeNode(9);
    //inorder(root);
    
    return 0;
}




