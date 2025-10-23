#include <iostream>
#include <vector>
using namespace std;

void subs(string st,int index, string temp, vector<string>&ans,int n){
    if(index==n){
        ans.push_back(temp);
        return;
    }
    //not included 
    subs(st,index+1,temp,ans,n);
    //included
    temp.push_back(st[index]);
    subs(st,index+1,temp,ans,n);
}

int main(){
    string st= "hello";
    vector <string> ans;
    string temp;
    int n =5;
    subs(st,0,temp,ans,n);
    for (int i =0;i<32;i++){
        cout<<ans[i]<<" "<<i+1<<endl;
    }
}