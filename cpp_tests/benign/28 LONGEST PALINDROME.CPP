#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector <int> lower(26);
    vector<int> upper(26);
    string s = "aaabbceedd";
    int count;
    int odd;//tracks if there was an odd no
    for (int i = 0;i<s.size();i++){
        if (s[i]>'a'){
            lower[s[i]-'a']++;
        }
        else{
            upper[s[i]-'A']++;
        }
    }
    for (int i=0;i<26;i++){
        if (lower[i] %2==0){
            count += lower[i];
        }
        else{
            count += lower[i]-1;
            odd=1;
        }
        
        if(upper[i]%2==0){
            count += upper[i];
        }
        else{
            count +=upper[i]-1;
            odd=1;
        }
    }count += odd;
    cout<<count;
}