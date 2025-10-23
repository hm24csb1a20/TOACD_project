#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <limits>

using namespace std;
vector<string> split(string s) {
    string outer = "";
    vector<string> ans;

    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            string temp = "";
            temp += s[i];

            i++; 
            while (i < s.size() && isdigit(s[i])) {
                temp += s[i];
                i++;
            }
            if (i < s.size() && s[i] == '[') {
                temp += s[i];
                i++;
            }

            int co = 1, cc = 0;
            while (i < s.size() && co != cc) {
                temp += s[i];
                if (s[i] == '[') co++;
                else if (s[i] == ']') cc++;
                i++;
            }
            ans.push_back(temp);
            i--;
        }
        else {
            outer = "";
            while (i < s.size() && !isdigit(s[i])) {
                outer += s[i];
                i++;
            }
            ans.push_back(outer);
            i--;
        }
    }
    return ans;
}
void make(string s,stack<int>& st1,stack<char> &st2,int &size, vector<string>&words ){
    for(char c:s){
        if(c=='['||c==']'){
            st2.push(c);
        }
        else if (isdigit(c)){
            st1.push(c-'0');
        }
        else{
            size++;
            string f(1, c);
            words.push_back(f);
        }
    }
}
string compute(stack<int> st1,stack<char>st2,int size,vector<string> words){
    if(!st2.empty()){
        while(st2.top()==']' && size>=0){
                string h= words[size];
                if(!st1.empty()){
                    for(int i=0;i<st1.top()-1;i++){
                        words[size]+=h;
                    }
                }
                
                st1.pop();
                st2.pop();
                size--;
                if(size>=0)words[size]+=words[size+1];
        }
    }

    return words[0];
}
int main() {
    int x;
    cin >> x;
    
    while (x--) {
        cin.ignore();
        string s;
        getline(cin, s);

        vector<string>spl = split(s);

        for(int i =0;i<spl.size();i++){
            stack<int>st1;
            stack<char>st2;
            int size=-1;
            vector<string> words;
            make(spl[i],st1,st2,size,words);
            // cout<<st1.top();
            if(st2.size()==0){cout<<spl[i];continue;}
            string sk = compute(st1,st2,size,words);
            spl[i]=sk;
            cout<<spl[i];
        }
        
        // make(s,st1,st2,size,words);
        cout <<endl;
    }
}