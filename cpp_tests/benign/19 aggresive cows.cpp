#include <iostream>
#include<algorithm>
using namespace std;
int main(){
    int arr[]={1,2,4,8,9};
    int n = 5;
    int start;
    int end;
    int k = 3;


    //linear method
    
    //binary
    int start=1,end,mid,ans;
    //sort them in increasing
    sort(stalls.begin(),stalls.end());
    end = stalls[n-1]-stalls[0];
    
    while (start<=end){
        mid = start+(end-start)/2;
        int count=1,position= stalls[0];
        for (int i =1;i<n;i++){
            if ((position +mid)<=stalls[i]){
                count++;
                position=stalls[i];
            }
        }
        
        if (count<k){
            end=mid-1;
        }
        else{
            ans=mid;
            start= mid+1;
            
        }
    }
}