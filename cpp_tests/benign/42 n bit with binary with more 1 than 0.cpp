#include <iostream>
#include <vector>
using namespace std;

void nbit(string temp, int n, int c1,int c0, vector <string> & ans){
    //base condition 
    if(c0+c1==n){
        if (c1>=c0){
            ans.push_back(temp);
            
        }
        return;

    }

    //add 1
    nbit(temp+"1",n,c1+1,c0,ans);
    //add 0
    nbit(temp+"0",n,c1,c0+1,ans);

}

int main(){
    string temp="";
    int n =4;
    int c1=0,c0=0;
    vector <string> ans;
    nbit(temp,n,c1,c0,ans);
    for(int i =0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
}