#include <iostream>
using namespace std;
int main(){
    int arr[]= {2,4,3,3,3,4,5,6};
    int n = 8;
    int target =3;
    int start =0;
    int end= n-1;
    int last =-1;
    int first =-1;
    int mid;
    while(start<=end){
        mid = start + (end-start)/2;
        cout<<"start is "<<start<<endl;
        cout<<"end is "<<end<<endl;
        cout<<"mid is "<<mid<<endl;
        if (arr[mid]==target){
            first= mid;
            end= mid;
        }
        else if (arr[mid]<target){
            start = mid+1;
        }else if (arr[mid]>target){
            end= mid-1;
        }
        
    }
    cout<<"the first term is at "<<first<<" index"<<endl;
}