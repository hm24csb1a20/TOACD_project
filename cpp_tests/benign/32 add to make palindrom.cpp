#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    string s = "aaaotcaakr";
    int start=0;
    int end = s.size()-1;
    int start1;
    int end1;
    int count=0;
    while (start<end){
        //if from start to end index it makes a palindrome;
        start1=start;
        end1=end;
        while(start1<end1){
            if (s[start1]!=s[end1]){
                break;
            }
            start1++;end1--;
        }
        if (start1>=end1){
            start++;
            end--;
        }else if(start1<end1){
            count++;
            end--;
        }
    }cout<<count;
}