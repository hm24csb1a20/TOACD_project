#include<bits/stdc++.h>
using namespace std;

class MaxHeap{

    int*arr;//array to stroe the elements;
    int size;
    int total_size;
    public:
    MaxHeap(int n ){
        arr= new int[n];
        size= 0;
        total_size=n;
    }
    void heapify(int index){
        int largest = index;
        int left = 2*index +1;
        int right = 2* index +2;
        //largest wiil stroe the index of the leement which is
        //greatest
        if(left<size&& arr[left]>arr[largest]){
            largest = left;
        }
        if(right<size&&arr[right]>arr[largest]){
            largest = right;
        }
        if(largest!= index){
            swap(arr[index],arr[largest]);
            heapify(largest);
        }
    }
    void insert(int value){
        //if heap size is aavailabel
        if(size ==total_size){
            cout<<"overflow";
            return;
        }
        arr[size]=value;
        int index = size;
        size++;
        
        //compare with parent
        while(index>0&& arr[(index-1)/2]<arr[index]){
            swap(arr[index],arr[(index-1)/2]);
            index = (index-1)/2;

        }
        cout<<arr[index]<<" has been inserted \n";
    }
    void print(){
        for (int i =0;i<size;i++){
            cout<<arr[i]<<" ";

        }
        cout<<endl;
    }
    void delete_top() {
        if (size==0){
            cout<<"underflow";
        }
        cout<<arr[0]<<" is deleted from the heap";
        arr[0]=arr[size-1];
        size--;
        if(size==0)return;
        heapify(0);
    }
};
void heapify(int arr[],int index, int n){
    int largest = index;
    int right = index *2+2;
    int left = index*2+1;
    
    if(left<n&&arr[left]>arr[largest]){
        largest = left;
    }
    if (right<n&&arr[right]>arr[largest]) largest = right;
    if(largest!= index){
        swap(arr[index],arr[largest]);
        heapify(arr,largest,n);
    }
}
void BuildMaxHeap( int arr[],int n ){
    //step down
    for (int i =n/2;i>=0;i--){
        heapify(arr,i,n);
    }
}

void sortArray(int arr[],int n ){
    for(int i =n-1;i>=0;i--){
        swap(arr[i],arr[0]);
        heapify(arr,0,i);
    }
}
int nchoc(int a, vector<int> &arr){
    priority_queue<int> p;
    for(int i =0;i<arr.size();i++)p.push(arr[i]);
    long long maxChoc=0;
    while(a&&(!p.empty())){
        maxChoc+=p.top();
        if(p.top()/2) p.push(p.top()/2);
        p.pop();
        a--;
    }
    return maxChoc;
}
int main(){
    
    priority_queue<int> p;//maxheap
    p.push(10);
    p.push(20);
    p.push(11);
    p.push(18);
    cout<<p.top();

    //minheap
    priority_queue<int, vector<int>,greater<int> >p;
}