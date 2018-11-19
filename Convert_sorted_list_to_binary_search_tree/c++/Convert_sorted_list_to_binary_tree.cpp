//
//  Convert_sorted_list_to_binary_tree.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/19.
//

#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

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
    TreeNode* sortedListToBST(ListNode* head) {
        
        if(!head) return NULL;
        if(!head->next) return new TreeNode(head->val);
        
        ListNode *first = head;
        ListNode *second = head;
        ListNode *third = second;
        
        while(first->next && first->next->next){
            third = second;
            second = second->next;     //one-step move
            first = first->next->next; //two-step move
        }
        
        first = second->next; //for right subtree
        third->next = NULL;   //for left subtree
        
        TreeNode *current = new TreeNode(second->val); //central point
        if(head != second) current->left = sortedListToBST(head);
        current->right = sortedListToBST(first);
        
        return current;
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
//    作者：SunnyYoona
//    来源：CSDN
//    原文：https://blog.csdn.net/sunnyyoona/article/details/42462457
ListNode* createList(int *A, int n){
    
    if(n <= 0) return NULL;
    
    ListNode *head = new ListNode(A[0]), *temp = head;
    
    for(int i = 1; i < n; i++){
        ListNode *input = new ListNode(A[i]);
        temp->next = input;
        temp = temp->next;
    }
    
    return head;
    
}




int main(){
   
    int A[] = {-10, -3, 0, 5, 9};
    ListNode* head = createList(A,5);
    TreeNode *result;
    Solution ans;
    
    result = ans.sortedListToBST(head);
    Show(result);
    
    return 0;
}
