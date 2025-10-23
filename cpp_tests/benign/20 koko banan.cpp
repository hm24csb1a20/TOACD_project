#include <iostream>
using namespace std;
int main(){
    int arr[]= {3,6,11,7};
    int n = 4;
    int start = 3;
    int end= 27;
    int mid;
    int k=8;
    int ans;
    
    while (start<=end){
        mid = start +(end-start)/2;
        int ct= 0;
        for (int i =0;i<n;i++){
            if (arr[i]%mid==0){
                ct+= arr[i]/mid;
            }else{
                ct+= arr[i]/mid+1;
            }
        }
        if (ct<=k){
            ans = mid;
            end = mid-1;
        }else{
            start=mid+1;
        }
        cout<<ans<<endl;
    }
    cout<<ans;
}