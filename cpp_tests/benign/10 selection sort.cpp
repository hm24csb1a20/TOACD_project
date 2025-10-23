#include<iostream>
using namespace std;
int main(){
    int arr[]= {10,8,2,3,1,4};
    int index=0;
    for (index;index<=4;index++){
        for (int i = index+1;i<=5;i++){
            if (arr[i]>arr[index]){
                swap(arr[index],arr[i]);
            }
        }
    }
    for (int j =0;j<=5;j++){
        cout<<arr[j]<<endl;
    }
}