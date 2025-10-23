#include<iostream>
#include <vector>
using namespace std;
int main(){
    vector<int>v ={4,2,0,5,2,6,2,3};
    int start = 1;
    int n = v.size();
    int water=0;
    int end= n-1;
    int previous=v[0];
    int left[n] ;
    left[0]=0;
    int right [n];
    right [n-1]=0;

    for (int i =1;i<n;i++){
        
        left[i] = max(left[i-1],v[i-1]);
    }
    for (int i =n-2;i>=0;i--){
        right[i] = max(right[i+1],v[i+1]);
    }
    for (int i=0;i<n;i++){
        int min_h = min(left[i],right[i]);
        if ((min_h-v[i])>0){
            water += min_h-v[i]; 
        }
    }
    cout<<water;

}