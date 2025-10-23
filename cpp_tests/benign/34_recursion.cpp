#include<iostream>
#include<vector>
using namespace std;
int GCD(int n1,int n2){
	//base case
	if(n2==0){
		return n1;
	}
	int c = n1%n2;
	return(GCD(n2,c));
}
int sum(int n){
	if (n==1) return 1;
	return(n+sum(n-1));
}
void print(vector<int> &v,int index){
	int n = v.size();//5
    //base case
	if (index==n) return;
	print(v,index+1);
    v[index]++;
	cout<<v[index]<<endl;
}
int smol(vector<int> v,int index){
    int n = v.size();
    //base condition
    if (index==n) return INT_MAX;
    return (min(v[index],smol(v,index+1)));
}
int main(){
	vector<int> arr = {3,4,1,2,8};
	print(arr,0);
    // cout<<arr.size();
    cout<<endl<<smol(arr,0);
}