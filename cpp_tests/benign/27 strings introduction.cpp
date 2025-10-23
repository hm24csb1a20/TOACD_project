#include <iostream>
#include <vector>
using namespace std;
int main(){
    string s ="the quick brown fox jumps over the lazy dog";
    int arr[26]={0};
    for (int i = 0;i<s.size();i++){
        arr[s[i]-97]++;
    }
    for (int i =0;i<26;i++){
        cout<<arr[i]<<" ";
    }

}