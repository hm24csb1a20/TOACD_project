#include<iostream>
#include <vector>
#include<string>
#include <algorithm>

using namespace std;
int main(){
    vector<char> roman ={
        'I','V','X','L','C','D','M'
    };
    vector<int> value ={ 1,5,10,50,100,500,1000};
    string s = "IV";
    signed int sum;
    for (int i =0;i<s.size();i++){
        for (int j=0;j<roman.size();j++){
            if (s[i]==roman[j]){
                cout<<"yes";
                if (s[i+1]==roman[j+1]){
                    sum+=(value[j]*-1);
                }else{
                    cout<<"no";
                    sum+= value[j];
                }
            }
        }

    }cout<<sum;
}