#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;
int main(){
    vector<int>v= {1,3,5,4,8,50,20,80};
    int st = 0;
    int end = 1;
    int target= 30;
    vector<int>ans;
    
    sort(v.begin(),v.end());
    // for (int i =0;i<v.size();i++){
    //     cout<<v[i]<<endl;
    // }
    while (st<=end){
        if ((v[end]-v[st])==target){
            int j;
            cout<<v[st]<<" "<<v[end]<<endl;
            break;
        }
        else if ((v[end]-v[st])>target){
            st++;
        }else{
            end++;
        }
        // cout << v[st] << " " << v[end] << endl;
    }
    for (int i =0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
}