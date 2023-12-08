//
//  binary_tree_postorder_traversal.cpp
//
//
//  Created by Wen-Ting Wang on 2018/11/8.
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
    vector<int> postorderTraversal(TreeNode* root) {

        vector<int> ans;

        if(!root) return ans;
        stack<TreeNode *> bag;
        TreeNode *head = root;

        bag.push(root);

        while(!bag.empty()){
            TreeNode *current = bag.top();

            if((!current->left && !current->right) || (current->left == head) || (current->right == head)){
                ans.push_back(current->val);
                bag.pop();
                head = current;
            }
            else{
                if(current->right) bag.push(current->right);
                if(current->left) bag.push(current->left);
            }

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

    result = ans.postorderTraversal(nodeA);


    cout<<endl;
    cout<<"Result1:"<<endl;
    for(int i = 0; i < 6; ++i)
        cout<<result[i]<<endl;



    return 0;
}
