#include <iostream>
using namespace std;
int main(){
    int arr[]= {19,9,30,22,7};
    int n = 5;
    int m=4;
    int start = 30;
    int end = 87;
    int mid;
    
    int ans;
  
    while (start<=end){
        mid = end +(start-end)/2;
        int page=0;
        int count=1;

        for (int i=0;i<n;i++){
            page += arr[i];
            if (page>mid){
                count++;
                page= arr[i];
            }
            
        }
        if (count<=m){
            ans = mid;
            end = mid-1;
        }else{
            start=mid+1;
        }
        cout<<mid<<endl;
    }
    cout<<ans;
}