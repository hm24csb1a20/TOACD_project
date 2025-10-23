#include<iostream>
#include <vector>
#include<string>
#include <algorithm>

using namespace std;
int main(){
    string s1 = "42345";
    string s2="9987";
    string ans;
    int carry;
    int sum;
    //assuming num1 > num2
    int index1 = s1.size()-1;
    int index2= s2.size()-1;
    while(index2 >=0){
        int a = s1[index1]-'0';
        int b = s2[index2]-'0';
        sum = a+b+carry;
        cout<<a<<" " <<b<<" "<<carry<<" "<<sum<<endl;
        carry = sum/10;
        char put = '0' +sum%10;
        ans+= put;
        index2--;
        index1--;
    }

    //here index1 still remains;
    while (index1>=0){
        int a = s1[index1]-'0';
        sum=a +carry;
        carry = sum/10;
        char c = '0'+sum%10;
        ans+=c;
        index1--;
    }
    reverse(ans.begin(),ans.end());


    
    cout<<ans;
}