//
//  Merge_two_sorted_linked_lists.cpp
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

class Solution1 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        if(!l1) return l2;
        if(!l2) return l1;
        
        ListNode *merge = new ListNode(0), *temp = merge;
        while(l1 && l2){
            cout << "l1 = "<< l1->val << " " <<  "l2 = "<< l2->val << " " <<endl;
            if(l1->val < l2->val){
               temp->next = l1;
               l1 = l1 ? l1->next : NULL;
            }
            else{
                temp->next = l2;
                l2 = l2 ? l2->next : NULL;
            }
            temp = temp->next;
        }
        temp->next = l1 ? l1 : l2;

        return merge->next;
    }
};

class Solution2 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1) return l2;
        if(!l2) return l1;
        
        if(l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};

class Solution{
public:
    ListNode *mergeTwoLists(ListNode* l1, ListNode* l2) {
        if((!l1) || (l2 && l1->val > l2->val)) swap(l1, l2);
        if(l1) l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    }
    
};



int main(){
    
    ListNode *a = new ListNode(2), *temp_a = a;
    
    temp_a->next = new ListNode(4);
    temp_a = temp_a->next;
    temp_a->next = new ListNode(7);
    
    ListNode *b = new ListNode(5), *temp_b = b;
    temp_b->next = new ListNode(6);
    temp_b = temp_b->next;
    temp_b->next = new ListNode(8);
    
    Solution object;
    ListNode *ans = object.mergeTwoLists(a, b);
    
   
    cout << "printing ans " << endl;
    while(ans){ //traversal
        cout << ans->val << " " << endl;
        ans = ans->next;
    }
}

