
/*Traverse from root to leaf node along depth of tree*/ 

void dfs(int n)
{
    vis[n]=true;
    cout<<n<<" ";
    for(int i=0;i<adj[n].size();i++)
    {
        if(!vis[adj[n][i]])
            dfs(adj[n][i]);
    }
}

/*Traverses level by level
    Queue helps to store nodes of a particular level
     in linear order*/

void bfs(int n)
{
    list<int> q;
    int i;
    q.pb(n);vis[n]=true;
    while(!q.empty())
    {
        n=q.front();q.pop_front();
        cout<<n<<" ";
        for(i=0;i<adj[n].size();i++)
        {
            if(!vis[adj[n][i]])
                {
                    q.push_back(adj[n][i]);vis[adj[n][i]]=true;
                }
        }
    }
}
