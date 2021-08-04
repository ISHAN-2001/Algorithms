/* Detect cycle
   Dont include 2nd parameter in directed graph*/

int colour[7]={0};
bool dfs(int a,int p=-1)
{
    colour[a]=1;
    for(auto u:adj[a])
    {
        if(u==p)
            continue;
        else if(colour[u]==0)
            return dfs(u,a);
        else if(colour[u]==1)
            return true;
    }
    colour[a]=2;
    return false;
}
void cycle()
{
    bool res;
    for(i=1;i<n;i++)
    {
        if(colour[a]==0)
            res=dfs(a);
        if(res==true)
            break;
    }
    cout<<res;
}