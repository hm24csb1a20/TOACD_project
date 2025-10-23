#include<iostream>
using namespace std;
int main(){
    int arr[]={7,4,8,5,3};
    int n=5;
    for(int j =n-2;j>=0;j--){
        for (int i=0;i<=j;i++){
        if (arr[i+1]<arr[i]){
            swap(arr[i+1],arr[i]);
        }}}
    for (int i =0;i<=4;i++){
        cout<<arr[i]<<endl;
    }
}