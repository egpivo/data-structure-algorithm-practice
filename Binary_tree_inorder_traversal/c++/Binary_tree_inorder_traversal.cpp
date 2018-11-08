//
//  Binary_tree_inorder_traversal.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/7.
//

#include<iostream>
#include<stack>
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(!root) return ans;
        
        stack<TreeNode *> stackBag;
        TreeNode *current = root;
        
        while(current || !stackBag.empty()){
            
            while(current) { // search the left leaf
                stackBag.push(current);
                current = current->left;
            }
            current = stackBag.top();
            stackBag.pop();
            ans.push_back(current->val);
            
            current = current->right; // if left node is gone
        }
        return ans;
        
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
    TreeNode *nodeA = new TreeNode(1);
    TreeNode *nodeB = new TreeNode(2);
    TreeNode *nodeC = new TreeNode(3);
    TreeNode *nodeD = new TreeNode(4);
    TreeNode *nodeE = new TreeNode(5);
    TreeNode *nodeF = new TreeNode(6);
    
    nodeA->left = nodeB;
    nodeA->right = nodeC;
    nodeB->left = nodeD;
    nodeB->right = nodeE;
    nodeC->right = nodeF;
    
    Show(nodeA);
    vector<int> result, result2;
    Solution ans;
    
    result = ans.inorderTraversal(nodeA);
    
    
    cout<<endl;
    cout<<"Result1:"<<endl;
    for(int i = 0; i < 6; ++i)
        cout<<result[i]<<endl;
    
    
    
    return 0;
}
