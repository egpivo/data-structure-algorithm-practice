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

class Solution{
public:
    ListNode* reverseList(ListNode* head){
        ListNode* current = head;
        ListNode* forward = nullptr;

        while(current){
            ListNode* previous = current->next;
            current->next = forward;
            forward = current;
            current = previous;
        }
        return forward;
    }
};

int main(){
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next ->next = new ListNode(3);

    Solution object;
    ListNode* ans = object.reverseList(head);
    cout << "printing ans " << endl;
    while(ans){
        cout << ans->val << " " << endl;
        ans = ans->next;
    }
}
