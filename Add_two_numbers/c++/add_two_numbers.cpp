//
//  add_two_numbers.cpp
//
//  By `linked list`
//  Created by Wen-Ting Wang on 2018/10/24.
//

#include <iostream>
using std::cout;
using std::endl;

/* Definition for singly-linked list.*/

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL){};
};

class Solution{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2){
        
        ListNode *list = new ListNode(0), *temp = list;
        int sum, rest = 0;
        
        while(l1 || l2 || rest){
            sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + rest;
            rest = sum / 10;
            temp->next = new ListNode(sum%10);
            temp = temp->next;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
        }
        return list->next;
    }
};

int main(){
    
    ListNode *a = new ListNode(2), *temp_a = a;
    ListNode *b = new ListNode(5), *temp_b = b;
    
    temp_a->next = new ListNode(4);
    temp_a = temp_a->next;
    temp_a->next = new ListNode(3);
    
    temp_b->next = new ListNode(6);
    temp_b = temp_b->next;
    temp_b->next = new ListNode(4);
    
    Solution object;
    ListNode *ans = object.addTwoNumbers(a, b);
    
    cout << "printing a " << endl;
    while(a){ //traversal
        cout << a->val << " " << endl;
        a = a->next;
    }
    
    cout << "printing b " << endl;
    while(b){ //traversal
        cout << b->val << " " << endl;
        b = b->next;
    }
    
    cout << "printing ans " << endl;
    while(ans){ //traversal
        cout << ans->val << " " << endl;
        ans = ans->next;
    }
}






