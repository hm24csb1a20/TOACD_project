#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector <int> arr ={4,3,2,1,2,7,6};
    int N = 7;
    int n = arr.size();
    for (int i = 0;i<n;i++){
        arr[i]--;
    }
    for (int i =0;i<n;i++){
        int element = arr[i]%N;
        arr[element]+= N;
    }
    //missing
    for (int i =0;i<n;i++){
        if(arr[i]/N==0){
            cout<<i+1<<endl;
        }
    }
    //repeating
    for (int i=0;i<n;i++){
        if (arr[i]/N==2){
            cout<<i+1<<endl;
        }
    }cout<<"mad"<<endl;
    for (int i = 0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}