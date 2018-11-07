//
//  Binary_tree_preorder_traveral.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/4.
//

#include<iostream>
#include<vector>
#include<stack>
#include<queue>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {};
};

class Solution{
public:
    vector<int> preorderTraversal(TreeNode* root){
        
        vector<int> ans;
        if (!root) return ans;
   
        stack<TreeNode *> temp;
        temp.push(root);
        
        while(!temp.empty()){
            TreeNode *top = temp.top();
            temp.pop();
            ans.push_back(top->val);
            if(top->right)
               temp.push(top->right);
            if(top->left)
                temp.push(top->left);
           
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

    result = ans.preorderTraversal(nodeA);
    

    cout<<endl;
    cout<<"Result1:"<<endl;
    for(int i = 0; i < 6; ++i)
        cout<<result[i]<<endl;
    

    
    return 0;
}
