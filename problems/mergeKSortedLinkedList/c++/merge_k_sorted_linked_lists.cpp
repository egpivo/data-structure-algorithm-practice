//
//  Merge_k_sorted_linked_lists.cpp
//
//
//  Created by Wen-Ting Wang on 2018/10/31.
//

#include <iostream>
#include <vector>
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        ListNode *temp = NULL;

        for(int i = 0; i < n; ++i){
            temp = mergeTwoLists(temp, lists[i]);
        }

        return temp;
    }

private:
    ListNode* mergeTwoLists(ListNode *l1, ListNode *l2){
        if(!l1 || (l2 && l1->val > l2->val)) swap(l1, l2);
        if(l1) l1->next = mergeTwoLists(l1->next, l2);
        return l1;
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
    int B[] = {3,5,8,10,11,12};
    int C[] = {15,16,17,23};

    ListNode* head1 = createList(A,5);
    ListNode* head2 = createList(B,6);
    ListNode* head3 = createList(C,4);

    vector<ListNode*> lists;

    lists.push_back(head1);
    lists.push_back(head2);
    lists.push_back(head3);

    Solution ans;
    ListNode *head = ans.mergeKLists(lists);

    ListNode *p = head;
    while(p){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;

    return 0;
}
