#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <cmath>
#include <string>
using namespace std;

vector<int> o;
vector<vector<int> > adj;
int ff(int n, vector <int> visited){
    int sum = o[n];
    visited[n] = 1;
    for(int i = 0; i<adj[n].size(); i++){
        if(visited[adj[n][i]] == 0){
            sum = sum + ff(adj[n][i], visited);
        }
    }
    return sum;
}
int main(){
    int n, m;
    cin >> n >> m;
    for(int i = 0; i<n; i++){
        int x;
        cin >> x;
        o.push_back(x);
        vector<int> blank;
        blank.push_back(i);
        adj.push_back(blank);
    }
    for(int i = 0; i<m; i++){
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    bool flag = false;
    for(int i = 0; i<n; i++){
        vector<int> v;
        for(int j = 0; j<n; j++){
            v.push_back(0);
        }
        int sum = ff(i, v);
        if(sum != 0){
            flag = true;
            break;
        }
        
    }
    
    if(flag == true)
        cout << "IMPOSSIBLE";
    else
        cout << "POSSIBLE";

    return 0;
}
