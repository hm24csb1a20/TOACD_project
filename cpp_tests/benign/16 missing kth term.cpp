#include <iostream>
using namespace std;
int main(){
    int arr[]={2,3,4,7,11,12};
    int n = 6;
    int start = 0;
    int end= n-1;
    int mid;
    int ans=n;
    int k=5;
    while(start<=end){
        mid = start +(end-start)/2;
        if ((arr[mid]-(mid+1))>=k){
            ans= mid;
            end = mid-1;
        }
        else {
            start= mid+1;
        }
    }
    cout<<ans+k;
}