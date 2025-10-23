#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    vector<int> v = {1,3,4,8,2,78};
    sort(v.begin(),v.end());
    int n = v.size();
    int end= n-1;
    int start = 0;
    int t = 13;
    int i =1;
    int b =-1;
    int c=1;
    while (start<=end){
        int ans = t- v[start]-v[end];
        b = binary_search(v.begin(),v.end(),ans);
        if (b==1){
            cout<<v[start]<<" "<<v[end]<<" "<<ans;
            break;
        }
        if (c%2==0){
            start ++;
        }else{
            end--;
        }
    }
}
