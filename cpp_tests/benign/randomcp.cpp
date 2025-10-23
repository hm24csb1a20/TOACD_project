#include<bits/stdc++.h>
using namespace std;

int main(){
    int t ;
    cin>>t;
    while(t--){
        int ele;
        cin>>ele;
        if(ele<5){
            cout<<"-1"<<endl;
            continue;
        }

        for(int i =2;i<=ele;i+=2){
            if(i!=4)cout<<i<<" ";
        }
        cout<<"4 5 ";
        for(int i =1;i<=ele;i+=2){
            if(i!=5)cout<<i<<" ";
        }
        cout<<endl;

    }
}