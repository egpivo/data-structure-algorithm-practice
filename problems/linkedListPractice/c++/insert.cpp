#include<iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int x): data(x), next(nullptr) {}
};

Node* Insert(Node* head, int x) {
    Node* temp = new Node(x);
    if(head != nullptr)
        temp->next = head;
    head = temp;
    return head;
}

void Print(Node* head) {
    Node *temp = head;
    cout << "List is: " << endl;
    while(temp != nullptr) {
        cout << temp->data << endl;
        temp = temp->next;
    }
}

int main(){
    // we need to initiate the head
    Node *head = nullptr;
    int n, input;
    cout << "How many numbers \n" << endl;

    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        cout << "Enter the  number \n" << endl;
        scanf("%d", &input);
        head = Insert(head, input);
        Print(head);
    }
}