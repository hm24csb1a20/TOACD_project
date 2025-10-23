#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

void perm(vector <int> arr,vector <vector <int> > &ans,vector <int> temp,vector<int> visited){
    //base condition
    if (visited.size()==temp.size()){
        ans.push_back(temp);
        return;
    }
    for (int i=0;i<visited.size(),i++){
        if (visited[i]==0){
            visited[i]=1;
            temp.push_back(arr[i]);
            perm(arr,ans,temp,visited);
        }
    }
}

int main(){
    vector <int> arr={1,2,3};
    vector<vector <int> > ans;
    vector <int> temp;
    vector<bool> visited (3,0);
    int n =3;
    perm(arr,ans,temp,visited);
}