#include <iostream>
using namespace std;

int subsum(int arr[], int index, int n, int sum){
    if (index==n||sum<0){
        return 0;
    }
    if (sum==0){
        return 1;
    }

    return subsum(arr,index+1,n,sum)+subsum(arr,index,n,sum-arr[index]);
}

int main(){
    int arr[]={2,3,4};
    int sum = 6;
    cout<<subsum (arr, 0,3,sum);
}