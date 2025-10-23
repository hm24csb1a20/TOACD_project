#include<iostream>
using namespace std;
void fun(int a[],int n){
    cout<<sizeof(a)<<" is the size of the pointer"<<endl;
    for (int i =0;i<n;i++){
        cout<<a[i]<<"  ";
    }
}
int main(){
    int arr[5]= {3,2,1,6,7};
    cout<<sizeof(arr)<<" is the size of the array"<<endl;
    fun (arr,5);
}
// int main(){
//     int arr[]= {1,2,3,4,5,6};
//     int last = arr[5];
//     for (int i =4;i>=0;i--){
//         arr[i+1]=arr[i];
//     }
//     arr[0]=last;
//     for (int i =0;i<=5;i++){
//         cout<<arr[i]<<endl;
//     }
// }