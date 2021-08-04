/* Pick a node which is unvisited and has shortest distance
   and check distances of adjoining vertices if shorter distances 
   are available . pre[] is used to store predecessor nodes which 
   can be used for shortest path*/
/*Above process is repeated for n times(outer loop)*/



void dijiktra(int s,int d)
{
    vector<int> dis,pre;
    dis.assign(n,INT_MAX);
    pre.assign(n,0);
    dis[s]=0;pre[s]=-1;
    int i,j,v;
    for(i=0;i<n;i++)
    {
        v=-1;
        for(j=0;j<n;j++)
        {
            if(!vis[j] && (v==-1||dis[j]<dis[v]))
                v=j;

            if(dis[v]==INT_MAX)
                break;
            
            for(auto edge:adj[v])
            {
                to=adj[v].F;
                len=adj[v].S;
                if(dis[v]+len<dis[to])
                {
                    dis[to]=dis[v]+len;
                    pre[to]=v;
                }
            }
        }
    }
    
    /* SHORTEST PATH*/

    vector<int> path;
    for(i=d;i!=-1;i=pre[i])
        path.pb(i);
    reverse(path);
    for(auto u:path)
        cout<<u<<" ";
}


/* Using set 
   Time complexity O(mlogn)*/

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    set<pair<int, int>> q;
    q.insert({0, s});
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;

            if (d[v] + len < d[to]) {
                q.erase({d[to], to});
                d[to] = d[v] + len;
                p[to] = v;
                q.insert({d[to], to});
            }
        }
    }
}


/* Using priority queue 
 faster than sets*/

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    using pii = pair<int, int>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v != d[v])
            continue;

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push({d[to], to});
            }
        }
    }
}