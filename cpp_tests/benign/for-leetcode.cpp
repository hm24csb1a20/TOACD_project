#include<bits/stdc++.h>
using namespace std;

vector<int> bfs(int v, vector<int>adj[]){
    queue<int>q;
    vector<bool>visited(v,0);
    vector<int>ans;
    q.push(0);
    visited[0]=1;
    while(!q.empty()){
        int node= q.front();
        q.pop();
        ans.push_back(node);
        for (int i =0;i<adj[node].size();i++){
            if(!visited[adj[node][i]]){
                visited[adj[node][i]]=1;
                q.push(adj[node][i]);
            }
        }

    }
}

void dfs ( int node, vector<int>adj[],vector<bool>&visited,vector<int>&ans){
    visited[node]=1;
    ans.push_back(node);
    for (int i =0;i<adj[node].size();i++){
        if(!visited[adj[node][i]]){
            dfs(adj[node][i],adj,visited,ans);
        }
    }
}

void dfsloop(int node, vector<int>adj[],vector<bool>&visited){
    vector<int> ans;
    stack<int> s;
    s.push(node);
    visited[node]=1;
    while(!s.empty()){
        node = s.top();
        s.pop();

        
        ans.push_back(node);
        for (int i = adj[node].size() - 1; i >= 0; i--) {
            if(!visited[adj[node][i]]){
                s.push(adj[node][i]);
                visited[adj[node][i]]=1;
            }
        }
    }
}

bool checkdfs( int node,int parent, vector<int>adj[],vector<bool>&visited){
    // zero node has -1 parent
    visited[node]=1;

    for (int i =0;i<adj[node].size();i++){
        if(visited[adj[node][i]] && adj[node][i]!= parent){
            return 1;
        }
        else if (!visited[adj[node][i]]){

            if(checkdfs(adj[node][i],node,adj,visited)){
                return true;
            };
        }
    }
    return 0;
}


bool checkbfs( vector<int>adj[],vector<bool>&visited){
    visited[0]= 1;
    queue<pair<int,int> > q;
    q.push(make_pair(0,-1));

    while(!q.empty()){
        int node = q.front().first;
        int parent = q.front().second;

        for ( int j = 0 ; j<adj[node].size();j++){
            int neigh = adj[node][j];
            if(parent == neigh){
                continue;
            }
            if(visited[neigh]){
                return 1;
            }
            visited[neigh]=1;
            q.push(make_pair(neigh,node));
        }
    }
    return 0;
}



void toposortdfs(int node, vector<int>adj[],vector<bool>&visited,
stack<int> &s){
    visited[node] =1;
    // look at neighbour one by one 
    for (int j = 0 ;j<adj[node].size();j++)   {
        int nei= adj[node][j];
        if (!visited[nei]){
            toposortdfs(nei,adj,visited,s);
        }
    }
    s.push(node);
}

vector<int> runner(int v , vector<int> adj[]){
    vector<bool>visited(v,0);
    stack<int>s;
    for(int i =0;i<v;i++){
        if(!visited[i]){
            toposortdfs(i,adj,visited,s);
        }
    }

    vector<int>ans;
    while(!s.empty()){
        ans.push_back(s.top());
        s.pop();
    }
    return ans;
}

vector<int>toposort(int v , vector<int>adj[]){
    vector<int>ans;
    vector<int> indeg(v,0);

    for (int i =0;i<v;i++){
        for (int j = 0;j<adj[i].size();j++){
            indeg[adj[i][j]]++;
        }
    }
    //push all 0 to the queue
    queue<int>q;
    for(int i=0;i<v;i++){
        if(!indeg[i]){
            q.push(i);
        }
    }

    while(!q.empty()){
        int node = q.front();
        q.pop();
        ans.push_back(node);
        // the elements going from node decreaing 
        for (int j =0;j<adj[node].size();j++){
            indeg[adj[node][j]]--;
            if(indeg[adj[node][j]]==0){
                q.push(adj[node][j]);
            }
        }
    }

    return ans;

}

bool detectcylce(int node, vector<int>adj[],vector<int>&path){
    path[node]=1;
    for (int j =0;j<adj[node].size();j++){
        int neig= adj[node][j];
        if(path[neig]){
            return 1;
        }   
        if(detectcylce(neig,adj,path)){
            return 1;
        }

    }
    path[node]=0;
}

bool iscyclic(int v , vector<int> adj[]){
    vector <int > indeg(v,0);
    int ct=0;
    for (int i =0;i<v;i++){
        for(int j = 0;j<adj[i].size();j++){
            indeg[adj[i][j]]++;
        }
    }

    queue<int>q;
    for (int i=0;i<v;i++){
        if(indeg[i]==0){
            q.push(i);
        }
    }

    while(!q.empty()){
        int node = q.front();
        q.pop();
        ct++;
        for (size_t i = 0; i < adj[node].size(); i++)
        {
            indeg[adj[node][i]]--;
            if (indeg[adj][node][i]==0){
                q.push(adj[node][i]);
            }
        }
    }
    
    return ct!=v;
}


    bool isbip( int node , vector<int>adj[], vector<int>&color){
        
        for (size_t j = 0; j < adj[node].size(); j++)
        {
            int neigh = adj[node][j];
            if(color[neigh]==-1){
                color[neigh]= (color[node]+1)%2;
                if(!isbip(neigh,adj,color)){
                    return 0;
                }
            }
            else{
                if(color[node]==color[neigh]){
                    return 0;
                }
            }
        }
        return 1;
        
    }
    bool runn(int v , vector<int> adj[]){
        vector<int> color(v,-1);
        for (size_t i = 0; i < v; i++)
        {
            if (color[i]==-1){
                color[i]=0;
                if(!isbip(i,adj,color)){
                    return 0;
                }
            }
        }
        return 1;
    }