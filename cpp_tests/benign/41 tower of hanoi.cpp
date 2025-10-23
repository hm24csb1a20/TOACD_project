#include <iostream>
using namespace std;


void toh(int n , int src, int help,int dest){

    //base condition
    if(n==1){
        cout<<"move disk "<<n<<" from "<<src<<" to "<<dest;
        return;
    }

    //takes n-1 to help 
    toh(n-1,src,dest,help);
    //move last to destination
    cout<<"move disk "<<n<<"from "<<src<<" to "<<dest;
    //takes the n-1 in help to destination
    toh(n-1,help,src,dest);

}