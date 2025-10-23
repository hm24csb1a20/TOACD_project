#include<iostream>
using namespace std;



int main(){
    int arr[]= {2,1,4,23,999,632}; //1 2 4 23 632 999
    int n = 6;
    bool cond = 0;
    int st = 0;
    int en = n-1;
    int search = 2;

    //for the bubble sort algorithm
    for (int i = n-1;i>=0;i--){
    bool b =0;
    for (int j =1;j<=i;j++){
        if (arr[j-1]>arr[j]){
            swap(arr[j-1],arr[j]);
            b =1;
            }
        }
    if (b ==0){ break;}
    }
    //for display algorithm
    for (int j =0; j<n;j++){cout<<arr[j]<<" ";}
    cout<<endl;

    //FOR THE BINARY SEARCH
    while (cond !=1){
        int mid  = (st+en)/2;
        cout<<"start: "<<st<<"  "<<"end: "<<en<<endl;
        cout<<"mid: "<<mid<<" "<<"mid term: "<<arr[mid]<<endl;
        cout<<endl;
        if (arr[mid] == search){
            cout<<"the term is found";
            cond =1;
            
        }
        else if (search < arr[mid]){
            en= mid -1;
        }
        else if(search> arr[mid]){
            st = mid +1;
        }
    }


}