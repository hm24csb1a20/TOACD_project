#include<iostream>
#include <vector>
#include<algorithm>
using namespace std;
class Node {
public:
	int data;
    Node* next;
	Node(int d,Node* n) {
		data=d;
		next =n;
	}
	Node(int d) {
		data= d;
		next = NULL;
	}
};

void insert(int i,Node*&head){
    Node *temp = new Node(i);
    if(head==NULL){
        head= temp;
    }
    else{
        temp->next = head;
        head = temp;
    }
}
vector<Node*> previous(Node *head){
    Node *temp=head;
    Node*pre= NULL;
    vector<Node*>ans;
    while(temp){
        ans.push_back(pre);
        pre= temp;
        temp=temp->next;
    }
    return ans;
}
int size(Node*head){
    int n=0;
    Node *temp = head;
    while(temp){
        n++;
        temp=temp->next;
    }
    return n;
}
Node* getadd(int index,Node*head){
    Node*temp = head;
    while(index--){
        temp= temp->next;
    }
    return temp;
}
void swap(Node*&head, vector<Node*>pre,int pos1, int pos2,int n){
    Node* pre1 = getadd(pos1-1,head);
    Node* node1= getadd(pos1,head);
    Node* pre2 = getadd(pos2-1,head);
    Node*node2= getadd(pos2,head);
    if(pre1)pre1->next = node2;
    else head = node2;
    if(pre2)pre2->next = node1;
    
    Node*temp = node1->next;
    node1->next = node2->next;
    node2->next = temp;
}
int main(){
    int x;
    cin>>x;
    while(x--){
        Node *head = NULL;
        int i=1;
        
        while(true){
            cin>>i;
            if(i==-1)break;
            insert(i,head);
            
        }
        //take the 2 positions;
        int pos1,pos2;
        int n = size(head);
        cin>>pos1>>pos2;
        //convert to 0base
        pos1--;pos2--;
        #include<iostream>
#include <vector>
#include<algorithm>
using namespace std;
class Node {
public:
	int data;
    Node* next;
	Node(int d,Node* n) {
		data=d;
		next =n;
	}
	Node(int d) {
		data= d;
		next = NULL;
	}
};

void insert(int i,Node*&head){
    Node *temp = new Node(i);
    if(head==NULL){
        head= temp;
    }
    else{
        temp->next = head;
        head = temp;
    }
}
vector<Node*> previous(Node *head){
    Node *temp=head;
    Node*pre= NULL;
    vector<Node*>ans;
    while(temp){
        ans.push_back(pre);
        pre= temp;
        temp=temp->next;
    }
    return ans;
}
int size(Node*head){
    int n=0;
    Node *temp = head;
    while(temp){
        n++;
        temp=temp->next;
    }
    return n;
}
Node* getadd(int index,Node*head){
    Node*temp = head;
    while(index--){
        temp= temp->next;
    }
    return temp;
}
void swap(Node*&head, vector<Node*>pre,int pos1, int pos2,int n){
    Node* pre1,post1;
    //1st is at the start
    if(pre[pos1-1]) pre1= pre[pos1-1];
    else pre1= pre[pos1];
    //1st at the end
    if(getadd(pos1,head)->next) post1= getadd(pos1,head)->next;
    else post1=NULL;
    
    //for the second variable
    Node* pre2,post2;
    //1st is at the start
    if(pre[pos2-1]) pre2= pre[pos2-1];
    else pre2= pre[pos2];
    //1st at the end
    if(getadd(pos2,head)->next) post1= getadd(pos2,head)->next;
    else post2=NULL;
    //making the swap
    pre1->next = getadd(pos2, head);
    getadd(pos2,head)->next = post1;
    pre2->next = getadd(pos1,head);
    getadd(pos1,head)->next = post2;
}
int main(){
    int x;
    cin>>x;
    while(x--){
        Node *head = NULL;
        int i=1;
        vector<int>nodes;
        while(true){
            cin>>i;
            if(i==-1)break;
            insert(i,head);
            
        }
        //take the 2 positions;
        int pos1,pos2;
        int n = size(head);
        cin>>pos1>>pos2;
        //convert to 0base
        pos1--;pos2--;
        vector<Node*>pre= previous(head)
        swap(head,pre,pos1,pos2,n);
        Node*temp=NULL;
        while(temp){
            cout<<temp->data<<" ";
            temp=temp->next;
            
        }
        cout<<endl;
    }
}
