#include<bits/stdc++.h>
using namespace std;

const int N= 1e4+5;
typedef pair<int,int> p;
typedef long long ll;
typedef pair<ll,p> pllp;
typedef vector<pllp> vpllp;
typedef vector<int> v;

v id;
int nodes, edges;
vpllp graph;

void initialize(){
    for(int i=0;i<N;i++)
        id.push_back(i);
}

int root(int x){
    while(id[x]!=x){
        id[x]=id[id[x]];
        x=id[x];
    }
    return x;
}

void union1(int x,int y){
    int p= root(x);
    int q=root(y);
    id[p]=id[q];
}

ll kruskal(vpllp graph){
    int x,y;
    ll cost, mincost=0;
    for(auto f:graph){
        x=f.second.first;
        y=f.second.second;
        cost=f.first;
        if(root(x)!=root(y)){
            mincost+=cost;
            union1(x,y);
        }
    }
    return mincost;
}


int main(){
    int x,y;
    ll weight, cost, mincost;
    initialize();
    cin>>nodes>>edges;
    for(int i=0;i<edges;i++){
        cin>>x>>y>>weight;
        graph.push_back(pllp(weight,p(x,y)));
    }
    sort(graph.begin(),graph.end());
    mincost=kruskal(graph);
    cout<<mincost<<endl;
    return 0;
}