#include <iostream>
#include <vector>
using namespace std;
void printp(int n,int countl,int countr, string temp, vector<string>&ans){
    //base 
    if (countl +countr == 2*n){
        ans.push_back(temp);
        return;
    }
    
    //left
    if(countl<n){
        temp += '(';
        printp(n,countl+1,countr,temp,ans);
    }
    //right

    if (countr<countl){
        temp += ')';
        printp(n,countl,countr+1,temp,ans);
    }
}
int main(){
    int n =2;
    vector <string> ans;
    string temp="";
    char c;
    printp(n,0,0,temp,ans);
    for (int i =0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
}