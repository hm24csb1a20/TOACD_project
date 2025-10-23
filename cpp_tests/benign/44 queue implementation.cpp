#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node(int value){
        data = value;
        next= NULL;
    }
};
class Queue{
    Node * front;
    Node * rear;
    public:
    Queue(){
        front= rear = NULL;
    }
    bool IsEmtpy(){
        return front==NULL;
    }
    void push(int x){
        if(IsEmtpy()){
            Node *temp = new Node(x);
            front = temp;
            rear = front;
        }
        else{
            rear->next = new Node(x);
            rear= rear->next;
        }
    }
    void pop(){
        if(IsEmtpy()){
            cout<<"queue underflwo";
        }
        else{
            Node * temp= front;
            front = front->next;
            delete temp;
        }
    }
    int start(){
        if(IsEmtpy()){
            cout<<"emtpy";
            return -1;
        }else{
            return front->data;
        }
    }
};

while(!q.empty()){
    cout<<q.front();
    q.pop();
}



