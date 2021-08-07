//
//  binary_tree_level_order_traversal.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/13.
//

#include<iostream>
#include<queue>
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
    vector<vector<int> > levelOrder(TreeNode* root) {
        vector<vector<int> > ans;
        if(!root) return ans;
        
        queue<TreeNode *> bag;
        bag.push(root);
        while(!bag.empty()){
            vector<int> level;
            int size = bag.size();
            for(int i = 0; i < size; ++i){
                TreeNode *current = bag.front();
                bag.pop();
                level.push_back(current->val);
                if(current->left) bag.push(current->left);
                if(current->right) bag.push(current->right);
            }
            ans.push_back(level);
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
    TreeNode *nodeA = new TreeNode(3);
    TreeNode *nodeB = new TreeNode(9);
    TreeNode *nodeC = new TreeNode(20);
    TreeNode *nodeD = new TreeNode(15);
    TreeNode *nodeE = new TreeNode(7);
    
    nodeA->left = nodeB;
    nodeA->right = nodeC;
    nodeC->left = nodeD;
    nodeC->right = nodeE;
    
    Show(nodeA);
    vector<vector<int> > result;
    Solution ans;
    
    result = ans.levelOrder(nodeA);
    
    
    cout<<endl;
    cout<<"Result:"<<endl;
 
    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result[i].size(); j++){
            cout << result[i][j]<< "\t";
        }
        cout<<endl;
    }
    
    
    return 0;
}
