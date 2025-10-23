#include <iostream>
using namespace std;
int main(){
    //in this array 8 is not given to find where this would go if it were to be there.
    int arr[]= {2,4,5,78,98,345};
    int target = 8;
    int start = 0;
    int n = 6;
    int end=n-1;
    int index = n;
    int mid;

    while (start<end){
        mid = start+ (end-start)/2;
        cout<<"start is "<<start<<endl;
        cout<<"end is "<<end<<endl;
        cout<<"mid is "<<mid<<endl;
        if (arr[mid]==target){
            index = mid;
            break;
        } 
        else if (arr[mid]>target){
            index= mid;
            end=mid-1;
        }
        else{
            start= mid+1;
        }
    }
    cout<<index;
    

}