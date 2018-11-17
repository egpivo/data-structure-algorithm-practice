//
//  Remove_nth_node_from_end_of_list.cpp
//
//
//  Created by Wen-Ting Wang on 2018/10/31.
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

/* another way
class Solution{
public:
    ListNode* removeNthFromEnd(ListNode* head, int n){
        
        if(!head->next) return NULL;
        int length = 0;
        ListNode *tmp = root;
        
        while(tmp){
            tmp = tmp->next;
            length ++;
        }
        
        if(length == n) return head->next;
        else{
            ListNode* current = head;
            for(int i = 0; i < length - n - 1; ++i)
                current = current->next;
            current->next = current->next->next;
            return head;
        }
    }
    
}
*/

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(!head->next) return NULL;
        
        ListNode *keep = head, *move = head;
        
        for(int i = 0; i < n; ++i) move = move->next;
        if(!move) return head->next;
        
        while(move->next){
            move = move->next;
            keep = keep->next;
        }
        keep->next = keep->next->next;
        
        return head;
    }
};


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




int main() {
    
    int A[] = {1,2,4,7,9};
    
    
    ListNode* temp = createList(A,5);
    
    Solution ans;
    ListNode *head = ans.removeNthFromEnd(temp, 1);
    
    ListNode *p = head;
    while(p){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;
    
    return 0;
}

