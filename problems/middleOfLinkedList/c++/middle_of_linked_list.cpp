#include<iostream>

using namespace std;
/**
 * Definition for singly-linked list.
 */
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;

        while(fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;

        }
        return slow;
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
    ListNode* head = createList(A,5);

    Solution ans;
    ListNode* answer = ans.middleNode(head);

    ListNode *p = answer;
    while(p){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;

    return 0;
}