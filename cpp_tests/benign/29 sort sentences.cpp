//sort the sentence
#include <iostream>
#include <vector>
using namespace std;
int main(){
    string s = "is2 my3 This1 sentence4";
    vector <string> ans (10);
    string temp;
    int count;
    for (int i =0;i<s.size();i++){
        if (s[i]==' '){
            
            int pos =temp[temp.size()-1]-'0';

            temp.pop_back();
            ans[pos]=temp;
            temp.clear();
            count++;
        }else{
            temp += s[i];
        }
    }
    // now even now the last word is left in temp
    int pos =temp[temp.size()-1]-'0';

    temp.pop_back();
    ans[pos]=temp;
    temp.clear();
    count++;
    for (int i =1;i<10;i++){
        temp += ans[i];
        temp+=' ';
    }
    //now in the last iteration of loop and extra ' '
    //remains so therefore
    temp.pop_back();
    cout<<temp;
}