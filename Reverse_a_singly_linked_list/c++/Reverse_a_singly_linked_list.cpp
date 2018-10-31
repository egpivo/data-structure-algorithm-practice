//
//  Reverse_a_singly_linked_list.cpp
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

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *forward = NULL;
        
        while(head){
            ListNode *temp = head->next;
            head->next = forward;
            forward = head;
            head = temp;
        }
        head = forward;

        return(head);
    }
};


int main(){
    ListNode *a = new ListNode(1), *temp_a = a;
    
    temp_a->next = new ListNode(2);
    temp_a = temp_a->next;
    temp_a->next = new ListNode(3);
    temp_a = temp_a->next;
    temp_a->next = new ListNode(4);
    temp_a = temp_a->next;
    temp_a->next = new ListNode(5);
   
    
    Solution object;
    ListNode *ans = object.reverseList(a);
    
   
    cout << "printing ans " << endl;
    while(ans){ //traversal
        cout << ans->val << " " << endl;
        ans = ans->next;
    }
    
    return 0;
}


