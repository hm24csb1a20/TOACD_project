#include <iostream>
using namespace std;
int main(){
    int arr[]= {5,10,30,20,15};
    int n = 5;
    int start=0;
    int end;
    int mid;
    int count;
    int ans;
    int painter=3;

    for (int i =0;i<n;i++){
        start = max(start, arr[i]);
        end += arr[i];
    }
    

    while (start<end){
        mid= start +(end -start)/2;
        int length=0, count=1;
        for (int i = 0; i <n;i++){
            length += arr[i];
            if (length>mid){
                count++;
                length= arr[i];
            }
        }
        if (count<= painter){
            ans= mid;
            end= mid-1;
        }else{
            start= mid+1;
        }
    }
    cout<<ans;
}