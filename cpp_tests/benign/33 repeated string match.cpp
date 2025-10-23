#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    string s1= "abcd";
    string s2="cdabcdab";
    s1=s1*(s2.size()/s1.size());
}