#include <iostream>
using namespace std;
int main(){
    int arr[]= {4,5,6,7,0,1,2};
    int n = 7;
    int start = 0;
    int end = n-1;
    int mid;
    int target = 0;
    int ans =-1;

    while (start<=end){
        mid = end +(start-end)/2;
        cout<<"start is "<<start<<endl;
        cout<<"end is "<<end<<endl;
        cout<<"mid is "<<mid<<endl;
        if (arr[mid]==target){
            cout<< mid;
        }
        //left sorted
        if (arr[mid]>arr[0]){
            if (target>=arr[0]&&target<=arr[mid]){
                end = mid-1;
            }
            else{start = mid+1;}
        }
        //right sorted
        else {
            if (target >=arr[mid]&& target <=arr[n-1]){
                start = mid+1;
            }else{ end = mid-1;}
        }
    }
}