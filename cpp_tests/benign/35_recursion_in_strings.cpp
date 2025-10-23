#include<iostream>
using namespace std;

int counts(string s,int end=8){
    //base condition 
    if (end==-1) return 0;
    //check for vowel
    if( s[end]=='a'||s[end]=='e'||s[end]=='i'||s[end]=='o'||s[end]=='u')
    return 1+counts(s,end-1);
    else
    return counts(s,end-1);
}
string reverse(string s, int end){
    //base condiition
    if (end ==-1)
    return;
    //reversing 
    swap(s[end],s[8-end]);
    return reverse(s,end-1);
}
int main(){
    string s = "abacadaba";
    cout<<counts(s,8);

}