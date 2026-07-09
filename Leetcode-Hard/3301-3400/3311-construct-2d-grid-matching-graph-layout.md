# 3311. Construct 2D Grid Matching Graph Layout

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> constructGridLayout(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        vector<int> deg(n,0);
        for (auto &e: edges){
            int u=e[0], v=e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            ++deg[u]; ++deg[v];
        }

        // count degree frequencies
        int cnt1=0,cnt2=0,cnt3=0,cnt4=0;
        for(int d:deg){
            if(d==1)cnt1++;
            else if(d==2)cnt2++;
            else if(d==3)cnt3++;
            else if(d==4)cnt4++;
        }

        // helper to attempt construction with given rows and cols
        auto tryBuild = [&](int R,int C)->vector<vector<int>>{
            vector<vector<int>> grid(R, vector<int>(C,-1));
            // line cases
            if (R==1){
                // single row
                int start=-1;
                for(int i=0;i<n;++i) if(deg[i]<=1){start=i;break;}
                if(start==-1) return {};
                vector<int> order;
                order.reserve(n);
                unordered_set<int> vis;
                int cur=start, prev=-1;
                while(true){
                    order.push_back(cur);
                    vis.insert(cur);
                    int nxt=-1;
                    for(int nb:adj[cur]){
                        if(nb!=prev){
                            nxt=nb; break;
                        }
                    }
                    if(nxt==-1) break;
                    prev=cur; cur=nxt;
                }
                if((int)order.size()!=n) return {};
                for(int j=0;j<C;++j) grid[0][j]=order[j];
                return grid;
            }
            if (C==1){
                // single column
                int start=-1;
                for(int i=0;i<n;++i) if(deg[i]<=1){start=i;break;}
                if(start==-1) return {};
                vector<int> order;
                order.reserve(n);
                unordered_set<int> vis;
                int cur=start, prev=-1;
                while(true){
                    order.push_back(cur);
                    vis.insert(cur);
                    int nxt=-1;
                    for(int nb:adj[cur]){
                        if(nb!=prev){
                            nxt=nb; break;
                        }
                    }
                    if(nxt==-1) break;
                    prev=cur; cur=nxt;
                }
                if((int)order.size()!=n) return {};
                for(int i=0;i<R;++i) grid[i][0]=order[i];
                return grid;
            }

            // general rectangle
            vector<int> corners;
            for(int i=0;i<n;++i){
                if(deg[i]==2) corners.push_back(i);
            }
            if(corners.size()!=4) return {};

            int start = corners[0];

            auto bfsDist = [&](int src)->vector<int>{
                vector<int> d(n,-1);
                queue<int> q;
                d[src]=0; q.push(src);
                while(!q.empty()){
                    int u=q.front(); q.pop();
                    for(int v:adj[u]){
                        if(d[v]==-1){
                            d[v]=d[u]+1;
                            q.push(v);
                        }
                    }
                }
                return d;
            };

            vector<int> dA = bfsDist(start);

            int tr=-1, bl=-1;
            for(int cnode: corners){
                if(dA[cnode]==C-1) tr=cnode;          // same row, far column
                else if(dA[cnode]==R-1) bl=cnode;    // same column, far row
            }
            if(tr==-1 || bl==-1) return {};

            vector<int> dTR = bfsDist(tr);

            vector<vector<bool>> used(R, vector<bool>(C,false));
            for(int v=0; v<n; ++v){
                int i = (dA[v] + dTR[v] - (C-1)) / 2;
                int j = (dA[v] - dTR[v] + (C-1)) / 2;
                if(i<0||i>=R||j<0||j>=C) return {};
                if(used[i][j]) return {};
                used[i][j]=true;
                grid[i][j]=v;
            }
            // verify all filled
            for(int i=0;i<R;++i)
                for(int j=0;j<C;++j)
                    if(grid[i][j]==-1) return {};

            return grid;
        };

        // enumerate possible dimensions
        vector<pair<int,int>> candidates;
        for(int r=1; (long long)r*r<=n; ++r){
            if(n%r==0){
                int c=n/r;
                candidates.emplace_back(r,c);
                if(r!=c) candidates.emplace_back(c,r);
            }
        }

        // sort to try more square-like first (optional)
        sort(candidates.begin(), candidates.end(),
             [&](const pair<int,int>&a,const pair<int,int>&b){
                 return abs(a.first-a.second)<abs(b.first-b.second);
             });

        for(auto [R,C]:candidates){
            // check degree pattern matches
            if(R==1 && C==1) continue;
            int exp1=0,exp2=0,exp3=0,exp4=0;
            if(R==1 || C==1){
                exp1=2;
                exp2=n-2;
            }else{
                exp2=4; // corners degree 2
                exp3=2*(R-2)+2*(C-2);
                exp4=(R-2)*(C-2);
            }
            if(cnt1!=exp1 || cnt2!=exp2 || cnt3!=exp3 || cnt4!=exp4) continue;
            auto res = tryBuild(R,C);
            if(!res.empty()) return res;
        }
        // Should never reach here as per problem guarantee
        return {};
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[][] constructGridLayout(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }
        int m = edges.length;

        // find possible dimensions
        List<int[]> dims = new ArrayList<>();
        for (int r = 1; r * (long) r <= n; ++r) {
            if (n % r == 0) {
                int c = n / r;
                long expected = (long) r * (c - 1) + (long) (r - 1) * c;
                if (expected == m) dims.add(new int[]{r, c});
                if (r != c && ((long) c * (r - 1) + (long) (c - 1) * r) == m)
                    dims.add(new int[]{c, r}); // swapped already covered but keep safety
            }
        }

        // degree array
        int[] deg = new int[n];
        for (int i = 0; i < n; ++i) deg[i] = adj[i].size();

        // handle path case (one dimension ==1)
        for (int[] rc : dims) {
            int rows = rc[0], cols = rc[1];
            if (rows == 1 || cols == 1) {
                int start = -1;
                for (int i = 0; i < n; ++i) {
                    if (deg[i] <= 1) { start = i; break; }
                }
                int[] dist = bfs(start, adj);
                int[][] res = rows == 1 ? new int[1][n] : new int[n][1];
                for (int v = 0; v < n; ++v) {
                    int d = dist[v];
                    if (rows == 1) res[0][d] = v;
                    else res[d][0] = v;
                }
                return res;
            }
        }

        // general case
        for (int[] rc : dims) {
            int rows = rc[0], cols = rc[1];
            int[][] ans = tryBuild(rows, cols, adj, deg);
            if (ans != null) return ans;
            // try swapped orientation
            ans = tryBuild(cols, rows, adj, deg);
            if (ans != null) return ans;
        }
        return new int[0][0]; // should never reach here
    }

    private int[][] tryBuild(int rows, int cols, List<Integer>[] adj, int[] deg) {
        List<Integer> corners = new ArrayList<>();
        for (int i = 0; i < deg.length; ++i) if (deg[i] == 2) corners.add(i);
        if (corners.size() != 4) return null;

        int A = corners.get(0);
        int[] distA = bfs(A, adj);

        int oppositeDist = rows + cols - 2;
        Integer D = null;
        for (int v : corners) {
            if (v != A && distA[v] == oppositeDist) { D = v; break; }
        }
        if (D == null) return null;

        Integer C = null, B = null;
        int rowDist = rows - 1;
        int colDist = cols - 1;
        for (int v : corners) {
            if (v == A || v == D) continue;
            if (distA[v] == rowDist && C == null) C = v;
            else if (distA[v] == colDist && B == null) B = v;
        }
        // when rows==cols both distances equal, assign arbitrarily
        if (C == null || B == null) {
            for (int v : corners) {
                if (v == A || v == D) continue;
                if (C == null) C = v;
                else B = v;
            }
        }

        int[] distC = bfs(C, adj);
        int[][] grid = new int[rows][cols];
        boolean[][] filled = new boolean[rows][cols];

        for (int v = 0; v < deg.length; ++v) {
            int r = (distA[v] - distC[v] + rows - 1) / 2;
            int c = distA[v] - r;
            if (r < 0 || r >= rows || c < 0 || c >= cols) return null;
            if (filled[r][c]) return null;
            grid[r][c] = v;
            filled[r][c] = true;
        }
        // verify all cells filled
        for (int i = 0; i < rows; ++i)
            for (int j = 0; j < cols; ++j)
                if (!filled[i][j]) return null;

        return grid;
    }

    private int[] bfs(int src, List<Integer>[] adj) {
        int n = adj.length;
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        ArrayDeque<Integer> q = new ArrayDeque<>();
        dist[src] = 0;
        q.add(src);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return dist;
    }
}
```

## Python

```python
class Solution(object):
    def constructGridLayout(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque, defaultdict

        adj = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # Helper BFS returning distance array
        def bfs(start):
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            while q:
                u = q.popleft()
                du = dist[u] + 1
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = du
                        q.append(v)
            return dist

        # If there is a node with degree 1, the graph is a simple path (1 x n grid)
        endpoint = None
        for i, d in enumerate(deg):
            if d == 1:
                endpoint = i
                break
        if endpoint is not None:
            # Build linear order starting from one endpoint
            order = []
            visited = [False] * n
            cur = endpoint
            prev = -1
            while True:
                order.append(cur)
                visited[cur] = True
                nxt = None
                for nb in adj[cur]:
                    if nb != prev:
                        nxt = nb
                        break
                if nxt is None or visited[nxt]:
                    break
                prev, cur = cur, nxt
            return [order]

        # Otherwise it's a proper rectangle grid
        corners = [i for i, d in enumerate(deg) if d == 2]
        # there should be exactly four corners
        c0 = corners[0]
        dist0 = bfs(c0)

        # opposite corner (diagonal)
        opp = max(corners, key=lambda x: dist0[x])
        D = dist0[opp]

        remaining = [c for c in corners if c != c0 and c != opp]
        tr_corner, bl_corner = remaining[0], remaining[1]  # arbitrary assignment

        L1 = dist0[tr_corner]          # columns - 1
        L2 = D - L1                     # rows - 1

        distA = dist0                   # from top-left corner (c0)
        distB = bfs(tr_corner)         # from top-right corner

        rows, cols = L2 + 1, L1 + 1
        grid = [[0] * cols for _ in range(rows)]

        for v in range(n):
            j = (distA[v] - distB[v] + L1) // 2
            i = distA[v] - j
            grid[i][j] = v

        return grid
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        deg = [0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=1
            deg[v]+=1

        cnt_deg = {}
        for d in deg:
            cnt_deg[d]=cnt_deg.get(d,0)+1

        # helper to find dimensions from degree counts
        def find_dims():
            # line case
            if cnt_deg.get(1,0)==2 and cnt_deg.get(2,0)==n-2:
                return (1,n)  # treat as 1 row
            # rectangle case
            for r in range(2,int(n**0.5)+1):
                if n%r: continue
                c = n//r
                if r==1 or c==1: continue
                corners = 4
                edges_cnt = 2*(r-2)+2*(c-2)
                interior = (r-2)*(c-2)
                if cnt_deg.get(2,0)==corners and cnt_deg.get(3,0)==edges_cnt and cnt_deg.get(4,0)==interior:
                    return (r,c)
            # fallback line other orientation
            return (n,1)

        rows, cols = find_dims()
        # collect corner nodes
        if rows==1 or cols==1:
            # line layout
            endpoints = [i for i,d in enumerate(deg) if d==1]
            start = endpoints[0]
            dist = [-1]*n
            q=deque([start])
            dist[start]=0
            order=[None]*n
            while q:
                u=q.popleft()
                order[dist[u]]=u
                for v in adj[u]:
                    if dist[v]==-1:
                        dist[v]=dist[u]+1
                        q.append(v)
            if rows==1:
                return [order]
            else:
                # column layout
                return [[x] for x in order]

        # rectangle case
        corners = [i for i,d in enumerate(deg) if d==2]
        # try each corner as top-left
        for tl in corners:
            # bfs from tl
            dist_tl=[-1]*n
            q=deque([tl])
            dist_tl[tl]=0
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if dist_tl[v]==-1:
                        dist_tl[v]=dist_tl[u]+1
                        q.append(v)
            # find top-right and bottom-left based on expected distances
            tr = bl = None
            for c in corners:
                if c==tl: continue
                d=dist_tl[c]
                if d==cols-1:
                    tr=c
                elif d==rows-1:
                    bl=c
            if tr is None or bl is None:
                continue
            # bfs from top-right
            dist_tr=[-1]*n
            q=deque([tr])
            dist_tr[tr]=0
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if dist_tr[v]==-1:
                        dist_tr[v]=dist_tr[u]+1
                        q.append(v)
            # compute coordinates
            pos=[[None]*cols for _ in range(rows)]
            ok=True
            used=set()
            for node in range(n):
                dtl=dist_tl[node]
                dtr=dist_tr[node]
                i = (dtl + dtr - (cols-1))//2
                j = dtl - i
                if not (0<=i<rows and 0<=j<cols):
                    ok=False
                    break
                if pos[i][j] is not None:
                    ok=False
                    break
                pos[i][j]=node
                used.add(node)
            if ok and len(used)==n:
                return pos
        # fallback (should not happen)
        return []
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** constructGridLayout(int n, int** edges, int edgesSize, int* edgesColSize,
                          int* returnSize, int*** returnColumnSizes) {
    // Compute degrees
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }

    // Allocate adjacency lists
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    // Fill adjacency
    int *cur = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][cur[u]++] = v;
        adj[v][cur[v]++] = u;
    }
    free(cur);

    // Find corner nodes (degree == 2)
    int corners[4];
    int ccnt = 0;
    for (int i = 0; i < n; ++i) {
        if (deg[i] == 2) {
            corners[ccnt++] = i;
        }
    }

    // Choose a corner as origin
    int c0 = corners[0];

    // BFS from c0
    int *dist0 = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) dist0[i] = -1;
    int *queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;
    dist0[c0] = 0;
    queue[rear++] = c0;
    while (front < rear) {
        int u = queue[front++];
        for (int k = 0; k < deg[u]; ++k) {
            int v = adj[u][k];
            if (dist0[v] == -1) {
                dist0[v] = dist0[u] + 1;
                queue[rear++] = v;
            }
        }
    }

    // Identify opposite corner (max distance)
    int opp = -1, maxd = -1;
    for (int i = 1; i < ccnt; ++i) {
        int node = corners[i];
        if (dist0[node] > maxd) {
            maxd = dist0[node];
            opp = node;
        }
    }

    // Remaining two corners
    int cr = -1, cc = -1;
    for (int i = 1; i < ccnt; ++i) {
        int node = corners[i];
        if (node == opp) continue;
        if (cr == -1) cr = node;
        else cc = node;
    }

    // Ensure dr + dc == maxd, swap if needed
    int dr = dist0[cr];
    int dc = dist0[cc];
    if (dr + dc != maxd) {
        int tmp = cr; cr = cc; cc = tmp;
        dr = dist0[cr];
        dc = dist0[cc];
    }

    int rows = dr + 1;
    int cols = dc + 1;

    // BFS from cr to get distances for column calculation
    int *distR = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) distR[i] = -1;
    front = rear = 0;
    distR[cr] = 0;
    queue[rear++] = cr;
    while (front < rear) {
        int u = queue[front++];
        for (int k = 0; k < deg[u]; ++k) {
            int v = adj[u][k];
            if (distR[v] == -1) {
                distR[v] = distR[u] + 1;
                queue[rear++] = v;
            }
        }
    }

    // Allocate result grid
    int **grid = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; ++i) {
        grid[i] = (int*)malloc(cols * sizeof(int));
    }
    int *colSizes = (int*)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) colSizes[i] = cols;

    // Place nodes
    for (int v = 0; v < n; ++v) {
        int d0 = dist0[v];
        int drv = distR[v];
        int j = (d0 + drv - dr) / 2;
        int i = d0 - j;
        grid[i][j] = v;
    }

    // Clean up
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(dist0);
    free(distR);
    free(queue);

    *returnSize = rows;
    *returnColumnSizes = &colSizes;
    return grid;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] ConstructGridLayout(int n, int[][] edges) {
        // Build adjacency list
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        // Degree counts
        int[] degCount = new int[5];
        int[] degree = new int[n];
        for (int i = 0; i < n; i++) {
            int d = adj[i].Count;
            degree[i] = d;
            if (d <= 4) degCount[d]++;
        }

        // Find dimensions
        int rows = -1, cols = -1;
        for (int r = 1; r * r <= n; ++r) {
            if (n % r != 0) continue;
            int c = n / r;
            if (CheckDimensions(r, c)) { rows = r; cols = c; break; }
            // the loop will also consider swapped pair when r iterates further
        }

        bool CheckDimensions(int r, int c) {
            if (r == 1 || c == 1) {
                // line
                return degCount[1] == 2 && degCount[2] == n - 2 && degCount[3] == 0 && degCount[4] == 0;
            } else {
                long expDeg2 = 4;
                long expDeg3 = 2L * (r + c) - 8;
                long expDeg4 = (long)(r - 2) * (c - 2);
                return degCount[2] == expDeg2 && degCount[3] == expDeg3 && degCount[4] == expDeg4;
            }
        }

        // Handle line case
        if (rows == 1 || cols == 1) {
            int start = -1;
            for (int i = 0; i < n; i++) if (adj[i].Count == 1) { start = i; break; }
            List<int> order = new List<int>();
            bool[] visited = new bool[n];
            int cur = start, prev = -1;
            while (true) {
                order.Add(cur);
                visited[cur] = true;
                int next = -1;
                foreach (int nb in adj[cur]) if (nb != prev) { next = nb; break; }
                if (next == -1) break;
                prev = cur;
                cur = next;
            }

            if (rows == 1) {
                int[][] ans = new int[1][];
                ans[0] = order.ToArray();
                return ans;
            } else { // cols == 1
                int[][] ans = new int[rows][];
                for (int i = 0; i < rows; i++) {
                    ans[i] = new int[1];
                    ans[i][0] = order[i];
                }
                return ans;
            }
        }

        // Rectangle case
        // Find corner nodes (degree == 2)
        List<int> corners = new List<int>();
        for (int i = 0; i < n; i++) if (adj[i].Count == 2) corners.Add(i);
        int origin = corners[0];

        int[] distO = BFS(origin, adj);
        // Identify opposite corner (max distance)
        int opp = -1;
        foreach (int cNode in corners) {
            if (cNode != origin && distO[cNode] > distO[opp == -1 ? origin : opp]) opp = cNode;
        }
        int maxDist = rows - 1 + cols - 1; // should equal distO[opp]

        // Find a corner that is not opposite and not origin
        int cornerH = -1;
        foreach (int cNode in corners) {
            if (cNode != origin && cNode != opp) { cornerH = cNode; break; }
        }

        // Determine which side corresponds to columns using distance from origin
        int colMinus1 = distO[cornerH];
        // If colMinus1 does not match cols-1, swap rows and cols (grid transposition)
        if (colMinus1 != cols - 1) {
            // swap interpretation: treat cornerH as vertical side
            colMinus1 = rows - 1;
            int temp = rows; rows = cols; cols = temp;
        }

        int[] distH = BFS(cornerH, adj);

        int[][] result = new int[rows][];
        for (int i = 0; i < rows; i++) result[i] = new int[cols];

        for (int node = 0; node < n; node++) {
            int x = (distO[node] + distH[node] - colMinus1) / 2;
            int y = distO[node] - x;
            result[x][y] = node;
        }

        return result;

        // Local BFS function
        int[] BFS(int start, List<int>[] graph) {
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = -1;
            Queue<int> q = new Queue<int>();
            dist[start] = 0;
            q.Enqueue(start);
            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in graph[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.Enqueue(v);
                    }
                }
            }
            return dist;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var constructGridLayout = function(n, edges) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const degree = new Int32Array(n);
    for (let i = 0; i < n; ++i) degree[i] = adj[i].length;

    // ----- line case -----
    const ends = [];
    for (let i = 0; i < n; ++i) {
        if (degree[i] === 1) ends.push(i);
    }
    if (ends.length === 2) { // a single row/column
        const order = [];
        let prev = -1;
        let cur = ends[0];
        while (true) {
            order.push(cur);
            let nxt = -1;
            for (const nb of adj[cur]) {
                if (nb !== prev) {
                    nxt = nb;
                    break;
                }
            }
            if (nxt === -1) break;
            prev = cur;
            cur = nxt;
        }
        return [order];
    }

    // ----- rectangle case -----
    const corners = [];
    for (let i = 0; i < n; ++i) {
        if (degree[i] === 2) corners.push(i);
    }
    // BFS utility
    const bfs = (src) => {
        const dist = new Int32Array(n).fill(-1);
        const q = new Array(n);
        let head = 0, tail = 0;
        dist[src] = 0;
        q[tail++] = src;
        while (head < tail) {
            const u = q[head++];
            const du = dist[u] + 1;
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = du;
                    q[tail++] = v;
                }
            }
        }
        return dist;
    };

    const start = corners[0];
    const distS = bfs(start);

    // find opposite corner (max distance)
    let opp = -1, maxd = -1;
    for (let i = 1; i < corners.length; ++i) {
        const d = distS[corners[i]];
        if (d > maxd) {
            maxd = d;
            opp = corners[i];
        }
    }

    // remaining two are side corners
    const side = [];
    for (const c of corners) {
        if (c !== start && c !== opp) side.push(c);
    }
    const sideA = side[0], sideB = side[1];
    const a = distS[sideA];
    const b = distS[sideB]; // note a + b == maxd

    const distA = bfs(sideA);
    const distB = bfs(sideB);

    const tryBuild = (R, C, distV, distH) => {
        const grid = Array.from({length: R}, () => new Array(C));
        for (let node = 0; node < n; ++node) {
            const dS = distS[node];
            const dV = distV[node];
            const dH = distH[node];
            const xNum = dS + dH - (C - 1);
            const yNum = dS + dV - (R - 1);
            if ((xNum & 1) || (yNum & 1)) return null;
            const x = xNum >> 1;
            const y = yNum >> 1;
            if (x < 0 || x >= R || y < 0 || y >= C) return null;
            grid[x][y] = node;
        }
        // verify all cells filled
        for (let i = 0; i < R; ++i) {
            for (let j = 0; j < C; ++j) {
                if (grid[i][j] === undefined) return null;
            }
        }
        return grid;
    };

    // first orientation: sideA as vertical side
    let R = a + 1, C = b + 1;
    let result = tryBuild(R, C, distA, distB);
    if (result !== null) return result;

    // swapped orientation
    R = b + 1; C = a + 1;
    result = tryBuild(R, C, distB, distA);
    return result;
};
```

## Typescript

```typescript
function constructGridLayout(n: number, edges: number[][]): number[][] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const degree = adj.map(a => a.length);

    // find a corner with minimal degree
    let start = 0;
    for (let i = 1; i < n; i++) {
        if (degree[i] < degree[start]) start = i;
    }

    const bfs = (src: number): number[] => {
        const dist = new Array(n).fill(-1);
        const q: number[] = [];
        dist[src] = 0;
        q.push(src);
        let head = 0;
        while (head < q.length) {
            const u = q[head++];
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return dist;
    };

    const distStart = bfs(start);

    // corners are nodes with degree <= 2
    const corners: number[] = [];
    for (let i = 0; i < n; i++) {
        if (degree[i] <= 2) corners.push(i);
    }

    // line case (only two corners)
    if (corners.length === 2) {
        const order = Array.from({ length: n }, (_, i) => i).sort((a, b) => distStart[a] - distStart[b]);
        return [order];
    }

    // general rectangle
    let opposite = start;
    for (const c of corners) {
        if (distStart[c] > distStart[opposite]) opposite = c;
    }
    const others = corners.filter(c => c !== start && c !== opposite);
    const c1 = others[0];
    const c2 = others[1];
    let rows = distStart[c1] + 1;
    let cols = distStart[c2] + 1;
    if (rows * cols !== n) {
        rows = distStart[c2] + 1;
        cols = distStart[c1] + 1;
    }

    // decide which remaining corner is vertical
    let cornerRow: number, cornerCol: number;
    if (distStart[c1] === rows - 1 && distStart[c2] === cols - 1) {
        cornerRow = c1; cornerCol = c2;
    } else if (distStart[c2] === rows - 1 && distStart[c1] === cols - 1) {
        cornerRow = c2; cornerCol = c1;
    } else {
        // square case, arbitrary choice
        cornerRow = c1; cornerCol = c2;
    }

    const distCornerRow = bfs(cornerRow);

    const grid: number[][] = Array.from({ length: rows }, () => Array(cols).fill(-1));

    for (let v = 0; v < n; v++) {
        const dA = distStart[v];
        const dB = distCornerRow[v];
        const y = (dA + dB - (rows - 1)) / 2;
        const x = dA - y;
        grid[x][y] = v;
    }

    return grid;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[][]
     */
    function constructGridLayout($n, $edges) {
        // build adjacency list and degree count
        $adj = array_fill(0, $n, []);
        $deg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            [$u, $v] = $e;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
            $deg[$u]++;
            $deg[$v]++;
        }

        // count degree-1 nodes (line case)
        $ends = [];
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] == 1) $ends[] = $i;
        }
        if (count($ends) == 2) { // line
            $order = [];
            $prev = -1;
            $cur = $ends[0];
            while (true) {
                $order[] = $cur;
                $next = null;
                foreach ($adj[$cur] as $nei) {
                    if ($nei !== $prev) {
                        $next = $nei;
                        break;
                    }
                }
                if ($next === null) break;
                $prev = $cur;
                $cur = $next;
            }
            return [$order];
        }

        // rectangle case: find corner nodes (degree == 2)
        $corners = [];
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] == 2) $corners[] = $i;
        }
        // BFS function
        $bfs = function($src) use (&$adj, $n) {
            $dist = array_fill(0, $n, -1);
            $q = new SplQueue();
            $dist[$src] = 0;
            $q->enqueue($src);
            while (!$q->isEmpty()) {
                $u = $q->dequeue();
                foreach ($adj[$u] as $v) {
                    if ($dist[$v] == -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q->enqueue($v);
                    }
                }
            }
            return $dist;
        };

        // choose TL arbitrarily
        $tl = $corners[0];
        $distTL = $bfs($tl);

        // find opposite corner (BR) with max distance among corners
        $br = $tl;
        $maxDist = -1;
        foreach ($corners as $c) {
            if ($distTL[$c] > $maxDist) {
                $maxDist = $distTL[$c];
                $br = $c;
            }
        }

        // remaining two corners
        $remaining = [];
        foreach ($corners as $c) {
            if ($c !== $tl && $c !== $br) $remaining[] = $c;
        }

        // try both assignments for TR and BL
        foreach ([$remaining, array_reverse($remaining)] as $perm) {
            [$tr, $bl] = $perm;

            $colLen = $distTL[$tr] + 1;               // distance TL->TR is columns-1
            $rowLen = $maxDist - ($colLen - 1) + 1;   // rows = (totalDist - (cols-1)) +1

            if ($rowLen <= 0 || $colLen <= 0) continue;

            $distTR = $bfs($tr);

            $grid = array_fill(0, $rowLen, array_fill(0, $colLen, -1));
            $used = [];

            $valid = true;
            for ($v = 0; $v < $n; $v++) {
                $dL = $distTL[$v];
                $dR = $distTR[$v];
                $temp = $dL - $dR + ($colLen - 1);
                if (($temp & 1) != 0) { $valid = false; break; }
                $j = intdiv($temp, 2);
                $i = $dL - $j;
                if ($i < 0 || $i >= $rowLen || $j < 0 || $j >= $colLen) {
                    $valid = false; break;
                }
                if (isset($used[$i . ',' . $j])) { $valid = false; break; }
                $grid[$i][$j] = $v;
                $used[$i . ',' . $j] = true;
            }

            if ($valid) return $grid;
        }

        // Fallback (should not happen with valid input)
        return [];
    }
}
```

## Swift

```swift
class Solution {
    func constructGridLayout(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        var deg = [Int](repeating: 0, count: n)
        for i in 0..<n { deg[i] = adj[i].count }

        // Check if the graph is a simple path (single row or column)
        let cornerDeg2Count = deg.filter { $0 == 2 }.count
        let hasDegreeOne = deg.contains(1)

        if !hasDegreeOne && cornerDeg2Count == 0 {
            // fallback, treat as path anyway
        }

        if hasDegreeOne {
            // Build a line layout (single row)
            var start = -1
            for i in 0..<n where deg[i] == 1 { start = i; break }
            if start == -1 { start = 0 } // safety
            var order = [Int]()
            var prev = -1
            var cur = start
            while true {
                order.append(cur)
                var nxt: Int? = nil
                for nb in adj[cur] where nb != prev {
                    nxt = nb
                    break
                }
                if nxt == nil { break }
                prev = cur
                cur = nxt!
            }
            return [order]
        }

        // Rectangle case (including 2x2)
        var startCorner = -1
        for i in 0..<n where deg[i] == 2 {
            startCorner = i
            break
        }
        if startCorner == -1 { startCorner = 0 } // safety

        let neighbors = adj[startCorner]
        guard neighbors.count >= 2 else { return [] }
        let rightNeighbor = neighbors[0]

        // Build the top row
        var topRow = [Int]()
        var topSet = Set<Int>()
        topRow.append(startCorner)
        topSet.insert(startCorner)

        var prevNode = startCorner
        var curNode = rightNeighbor

        while true {
            topRow.append(curNode)
            topSet.insert(curNode)
            if deg[curNode] == 2 { break } // reached opposite corner of the top edge
            var nextNode: Int? = nil
            for nb in adj[curNode] {
                if nb == prevNode { continue }
                if topSet.contains(nb) { continue }
                if deg[nb] <= 3 {   // still on the border
                    nextNode = nb
                    break
                }
            }
            guard let nxt = nextNode else { return [] }
            prevNode = curNode
            curNode = nxt
        }

        let colCount = topRow.count

        // Build columns using unvisited neighbors
        var placed = [Bool](repeating: false, count: n)
        for v in topRow { placed[v] = true }

        var cols = [[Int]]()
        for j in 0..<colCount {
            var column = [Int]()
            var cur = topRow[j]
            var prev = -1
            while true {
                column.append(cur)
                if deg[cur] == 2 && !(j == 0 && cur == startCorner) { // bottom corner reached
                    break
                }
                var next: Int? = nil
                for nb in adj[cur] {
                    if nb == prev { continue }
                    if placed[nb] { continue }
                    next = nb
                    break
                }
                guard let nxt = next else { return [] }
                prev = cur
                cur = nxt
                placed[cur] = true
            }
            cols.append(column)
        }

        // All columns should have the same length
        let rowCount = cols[0].count
        for col in cols where col.count != rowCount {
            return []
        }

        // Assemble final grid
        var result = [[Int]]()
        for i in 0..<rowCount {
            var rowVals = [Int]()
            for j in 0..<colCount {
                rowVals.append(cols[j][i])
            }
            result.append(rowVals)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructGridLayout(n: Int, edges: Array<IntArray>): Array<IntArray> {
        // build adjacency list
        val temp = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            temp[u].add(v)
            temp[v].add(u)
        }
        val adj = Array(n) { i -> IntArray(temp[i].size) { idx -> temp[i][idx] } }

        // find dimensions using divisor method
        var R = 0
        var C = 0
        val m = edges.size
        val sqrtN = kotlin.math.sqrt(n.toDouble()).toInt()
        loop@ for (d in 1..sqrtN) {
            if (n % d == 0) {
                val r = d
                val c = n / d
                if (2 * n - r - c == m) {
                    R = r
                    C = c
                    break@loop
                }
                // also check swapped, but condition symmetric
            }
        }

        // line case
        if (R == 1 || C == 1) {
            val isRow = R == 1
            var start = -1
            for (i in 0 until n) {
                if (adj[i].size == 1) { // endpoint
                    start = i
                    break
                }
            }
            if (start == -1) start = 0
            val order = IntArray(n)
            var idx = 0
            var prev = -1
            var cur = start
            while (cur != -1) {
                order[idx++] = cur
                var nxt = -1
                for (v in adj[cur]) {
                    if (v != prev) {
                        nxt = v
                        break
                    }
                }
                prev = cur
                cur = nxt
            }
            return if (isRow) {
                arrayOf(order)
            } else {
                Array(n) { i -> intArrayOf(order[i]) }
            }
        }

        // rectangle case
        // find a corner node (degree == 2)
        var startCorner = -1
        for (i in 0 until n) if (adj[i].size == 2) { startCorner = i; break }
        // BFS from startCorner
        fun bfs(s: Int): IntArray {
            val dist = IntArray(n) { -1 }
            val q = IntArray(n)
            var head = 0
            var tail = 0
            dist[s] = 0
            q[tail++] = s
            while (head < tail) {
                val u = q[head++]
                for (v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1
                        q[tail++] = v
                    }
                }
            }
            return dist
        }

        val distS = bfs(startCorner)

        // locate opposite corner that defines horizontal length C-1
        var tr = -1
        for (i in 0 until n) {
            if (adj[i].size == 2 && distS[i] == C - 1) {
                tr = i
                break
            }
        }
        // if not found, maybe dimensions swapped; try using R-1 and swap later
        var swapped = false
        if (tr == -1) {
            for (i in 0 until n) {
                if (adj[i].size == 2 && distS[i] == R - 1) {
                    tr = i
                    break
                }
            }
            // swap rows and columns
            val tmp = R
            R = C
            C = tmp
            swapped = true
        }

        val distT = bfs(tr)

        // build grid using formula:
        // i = (ds + dt - (C-1)) / 2
        // j = ds - i
        val grid = Array(R) { IntArray(C) }
        for (v in 0 until n) {
            val ds = distS[v]
            val dt = distT[v]
            val iCoord = (ds + dt - (C - 1)) / 2
            val jCoord = ds - iCoord
            grid[iCoord][jCoord] = v
        }
        return grid
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> constructGridLayout(int n, List<List<int>> edges) {
    // Build adjacency list
    final adj = List.generate(n, (_) => <int>[]);
    for (var e in edges) {
      int u = e[0], v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // Find corner nodes (degree == 2)
    List<int> corners = [];
    for (int i = 0; i < n; ++i) {
      if (adj[i].length == 2) corners.add(i);
    }
    // Choose one corner as origin
    int s = corners[0];
    // Its two neighbors will be orthogonal directions
    int a = adj[s][0];
    int b = adj[s][1];

    // BFS to compute distances from three sources
    List<int> bfs(int src) {
      final dist = List.filled(n, -1);
      final q = List<int>.filled(n, 0);
      int head = 0, tail = 0;
      dist[src] = 0;
      q[tail++] = src;
      while (head < tail) {
        int cur = q[head++];
        for (int nb in adj[cur]) {
          if (dist[nb] == -1) {
            dist[nb] = dist[cur] + 1;
            q[tail++] = nb;
          }
        }
      }
      return dist;
    }

    final distS = bfs(s);
    final distA = bfs(a);
    final distB = bfs(b);

    // Compute coordinates
    List<int> xs = List.filled(n, 0);
    List<int> ys = List.filled(n, 0);
    int maxX = 0, maxY = 0;
    for (int v = 0; v < n; ++v) {
      int x = ((distS[v] + distA[v] - 1) ~/ 2);
      int y = distS[v] - x;
      xs[v] = x;
      ys[v] = y;
      if (x > maxX) maxX = x;
      if (y > maxY) maxY = y;
    }

    // Build grid
    List<List<int>> grid = List.generate(maxX + 1, (_) => List.filled(maxY + 1, -1));
    for (int v = 0; v < n; ++v) {
      grid[xs[v]][ys[v]] = v;
    }
    return grid;
  }
}
```

## Golang

```go
func constructGridLayout(n int, edges [][]int) [][]int {
    adj := make([][]int, n)
    deg := make([]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
        deg[u]++
        deg[v]++
    }

    // find a corner (degree <= 2)
    startA := -1
    for i := 0; i < n; i++ {
        if deg[i] <= 2 {
            startA = i
            break
        }
    }
    if startA == -1 {
        startA = 0
    }

    bfs := func(src int) []int {
        dist := make([]int, n)
        for i := range dist {
            dist[i] = -1
        }
        q := make([]int, 0, n)
        dist[src] = 0
        q = append(q, src)
        for head := 0; head < len(q); head++ {
            v := q[head]
            for _, nb := range adj[v] {
                if dist[nb] == -1 {
                    dist[nb] = dist[v] + 1
                    q = append(q, nb)
                }
            }
        }
        return dist
    }

    distA := bfs(startA)

    // farthest node from startA -> opposite corner B
    farB, maxd := startA, -1
    for i, d := range distA {
        if d > maxd {
            maxd = d
            farB = i
        }
    }

    distB := bfs(farB)
    D := maxd // diameter

    // collect nodes with degree <= 2 (potential corners)
    corners := []int{}
    for i := 0; i < n; i++ {
        if deg[i] <= 2 {
            corners = append(corners, i)
        }
    }

    // find a third corner C different from A and B
    C := -1
    minPosDist := n + 1
    for _, v := range corners {
        if v == startA || v == farB {
            continue
        }
        d := distA[v]
        if d > 0 && d < D && d < minPosDist {
            minPosDist = d
            C = v
        }
    }

    // line case (no third corner)
    if C == -1 {
        order := make([]int, 0, n)
        visited := make([]bool, n)
        cur, prev := startA, -1
        for {
            order = append(order, cur)
            visited[cur] = true
            nxt := -1
            for _, nb := range adj[cur] {
                if nb != prev {
                    nxt = nb
                    break
                }
            }
            if nxt == -1 || visited[nxt] {
                break
            }
            prev, cur = cur, nxt
        }
        res := make([][]int, 1)
        res[0] = make([]int, n)
        for i, v := range order {
            res[0][i] = v
        }
        return res
    }

    // dimensions using corner C
    d1 := distA[C]
    cols := d1 + 1
    rows := D - d1 + 1

    distC := bfs(C)

    res := make([][]int, rows)
    for i := 0; i < rows; i++ {
        res[i] = make([]int, cols)
    }

    for v := 0; v < n; v++ {
        s := distA[v]
        t := distC[v]
        j := (s - t + cols - 1) / 2
        i := s - j
        res[i][j] = v
    }
    return res
}
```

## Ruby

```ruby
def construct_grid_layout(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  degree = adj.map(&:size)

  # Line case: exactly two nodes with degree 1 (endpoints)
  if degree.count(1) == 2 && degree.count(2) == 0
    start = degree.index(1)
    order = []
    prev = -1
    cur = start
    loop do
      order << cur
      nxts = adj[cur].reject { |x| x == prev }
      break if nxts.empty?
      prev = cur
      cur = nxts[0]
    end
    return [order]
  end

  # General rectangular grid case
  corners = []
  degree.each_with_index do |deg, idx|
    corners << idx if deg == 2
  end

  # BFS helper
  bfs = lambda do |src|
    dist = Array.new(n, -1)
    q = [src]
    dist[src] = 0
    head = 0
    while head < q.length
      u = q[head]
      head += 1
      adj[u].each do |v|
        if dist[v] == -1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    dist
  end

  a = corners[0]
  dist_a = bfs.call(a)

  # opposite corner (farthest from a)
  b = corners.max_by { |c| dist_a[c] }

  remaining = corners - [a, b]
  c1, c2 = remaining

  try_build = lambda do |dist_top_left, dist_other_corner, rows, cols|
    grid = Array.new(rows) { Array.new(cols) }
    (0...n).each do |v|
      sum = dist_top_left[v] + dist_other_corner[v] - (rows - 1)
      return nil if sum.odd?
      j = sum / 2
      i = dist_top_left[v] - j
      return nil if i < 0 || i >= rows || j < 0 || j >= cols
      return nil if grid[i][j]
      grid[i][j] = v
    end
    grid
  end

  # First attempt: assume c1 is the bottom‑left corner (same column as a)
  rows1 = dist_a[c1] + 1
  cols1 = dist_a[c2] + 1
  dist_c1 = bfs.call(c1)
  result = try_build.call(dist_a, dist_c1, rows1, cols1)

  # If failed, swap c1 and c2
  if result.nil?
    rows2 = dist_a[c2] + 1
    cols2 = dist_a[c1] + 1
    dist_c2 = bfs.call(c2)
    result = try_build.call(dist_a, dist_c2, rows2, cols2)
  end

  result
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, Queue}

object Solution {
  def constructGridLayout(n: Int, edges: Array[Array[Int]]): Array[Array[Int]] = {
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    val deg = new Array[Int](n)
    for (e <- edges) {
      val u = e(0); val v = e(1)
      adj(u).append(v)
      adj(v).append(u)
      deg(u) += 1
      deg(v) += 1
    }

    // Detect line case (two nodes with degree 1)
    val ends = (0 until n).filter(deg(_) == 1).toArray
    if (ends.length == 2) {
      val order = new Array[Int](n)
      var cur = ends(0)
      var prev = -1
      var idx = 0
      while (cur != -1) {
        order(idx) = cur
        idx += 1
        val nextOpt = adj(cur).find(_ != prev)
        prev = cur
        cur = nextOpt.getOrElse(-1)
      }
      Array(order)
    } else {
      // Rectangle case: four corners with degree 2
      val corners = (0 until n).filter(deg(_) == 2).toArray
      val start = corners(0)

      def bfs(s: Int): Array[Int] = {
        val dist = Array.fill(n)(-1)
        val q = new java.util.ArrayDeque[Int]()
        dist(s) = 0
        q.add(s)
        while (!q.isEmpty) {
          val u = q.poll()
          val nd = dist(u) + 1
          var i = 0
          while (i < adj(u).size) {
            val v = adj(u)(i)
            if (dist(v) == -1) {
              dist(v) = nd
              q.add(v)
            }
            i += 1
          }
        }
        dist
      }

      val distA = bfs(start)

      var minDist = Int.MaxValue
      var cornerB = -1
      for (c <- corners if c != start) {
        val d = distA(c)
        if (d > 0 && d < minDist) {
          minDist = d
          cornerB = c
        }
      }

      val rows = minDist + 1
      val cols = n / rows

      val distB = bfs(cornerB)

      val res = Array.ofDim[Int](rows, cols)
      var v = 0
      while (v < n) {
        val da = distA(v)
        val db = distB(v)
        val row = (da - db + (rows - 1)) / 2
        val col = da - row
        res(row)(col) = v
        v += 1
      }
      res
    }
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn construct_grid_layout(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // find corner nodes (degree <= 2)
        let mut corners: Vec<usize> = Vec::new();
        for i in 0..n_usize {
            if adj[i].len() <= 2 {
                corners.push(i);
            }
        }

        // line case (only two corners)
        if corners.len() == 2 {
            let start = corners[0];
            let mut order: Vec<i32> = Vec::with_capacity(n_usize);
            order.push(start as i32);
            let mut prev = start;
            let mut cur_opt = adj[start].get(0).cloned();
            while let Some(cur) = cur_opt {
                order.push(cur as i32);
                if adj[cur].len() == 1 {
                    break;
                }
                // next neighbor not equal to prev
                let nxt = *adj[cur].iter().find(|&&x| x != prev).unwrap();
                prev = cur;
                cur_opt = Some(nxt);
            }
            return vec![order];
        }

        // helper BFS
        fn bfs(start: usize, adj: &Vec<Vec<usize>>, n: usize) -> Vec<i32> {
            let mut dist = vec![-1i32; n];
            let mut q = VecDeque::new();
            dist[start] = 0;
            q.push_back(start);
            while let Some(u) = q.pop_front() {
                let du = dist[u];
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = du + 1;
                        q.push_back(v);
                    }
                }
            }
            dist
        }

        // line length along edge starting from corner s through neighbor nxt
        fn line_len(s: usize, nxt: usize, adj: &Vec<Vec<usize>>) -> usize {
            let mut len = 1; // includes nxt
            let mut prev = s;
            let mut cur = nxt;
            loop {
                let deg = adj[cur].len();
                if deg != 3 {
                    break;
                }
                let next_node = *adj[cur].iter().find(|&&x| x != prev).unwrap();
                prev = cur;
                cur = next_node;
                len += 1;
            }
            len
        }

        // choose an arbitrary corner as start
        let s = corners[0];
        let neighs = adj[s].clone(); // size == 2
        let len0 = line_len(s, neighs[0], &adj);
        let len1 = line_len(s, neighs[1], &adj);

        // possible dimensions
        let mut rows = len0 + 1;
        let mut cols = len1 + 1;
        let mut right_dir = neighs[0];
        let mut down_dir = neighs[1];
        if rows * cols != n_usize {
            rows = len1 + 1;
            cols = len0 + 1;
            right_dir = neighs[1];
            down_dir = neighs[0];
        }

        // distances from start corner
        let dist_s = bfs(s, &adj, n_usize);

        // find opposite corner (farthest)
        let mut opp = s;
        let mut maxd = -1i32;
        for &c in corners.iter() {
            if dist_s[c] > maxd {
                maxd = dist_s[c];
                opp = c;
            }
        }

        // identify top-right and bottom-left corners
        let mut tr_opt: Option<usize> = None;
        let mut bl_opt: Option<usize> = None;
        for &c in corners.iter() {
            if c == s || c == opp { continue; }
            let d = dist_s[c] as usize;
            if d == cols - 1 && tr_opt.is_none() {
                tr_opt = Some(c);
            } else if d == rows - 1 && bl_opt.is_none() {
                bl_opt = Some(c);
            }
        }
        let tr = tr_opt.unwrap();

        // distances from top-right corner
        let dist_tr = bfs(tr, &adj, n_usize);

        // build grid
        let mut grid: Vec<Vec<i32>> = vec![vec![-1; cols]; rows];
        for i in 0..n_usize {
            let d1 = dist_s[i] as i32;
            let d2 = dist_tr[i] as i32;
            let y = (d1 - d2 + (cols as i32 - 1)) / 2;
            let x = d1 - y;
            grid[x as usize][y as usize] = i as i32;
        }
        grid
    }
}
```

## Racket

```racket
(define/contract (construct-grid-layout n edges)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ([adj (make-vector n '())]
         [add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v))))]
         [_ (for-each (lambda (e) (add-edge (list-ref e 0) (list-ref e 1))) edges)]
         [deg (make-vector n 0)]
         [_ (for ([i (in-range n)])
              (vector-set! deg i (length (vector-ref adj i))))]
         ; count degree frequencies
         [cnt2 (let loop ([i 0] [c 0])
                 (if (= i n) c
                     (loop (+ i 1)
                           (if (= (vector-ref deg i) 2) (+ c 1) c))))]
         [cnt3 (let loop ([i 0] [c 0])
                 (if (= i n) c
                     (loop (+ i 1)
                           (if (= (vector-ref deg i) 3) (+ c 1) c))))]
         [cnt4 (let loop ([i 0] [c 0])
                 (if (= i n) c
                     (loop (+ i 1)
                           (if (= (vector-ref deg i) 4) (+ c 1) c))))]
         ; find dimensions r,c
         [dims
          (let find-dims ()
            (cond
              [(and (= cnt2 2) (= cnt3 (- n 2))) ; path case
               (values 1 n)]
              [(= cnt2 4)
               (let loop ((d 1))
                 (if (> (* d d) n)
                     (error "invalid grid")
                     (if (zero? (remainder n d))
                         (let* ([r d] [c (/ n d)])
                           (if (and (= (+ (* (- r 2) 2) (* (- c 2) 2)) cnt3)
                                    (= (* (- r 2) (- c 2)) cnt4))
                               (values r c)
                               (loop (+ d 1))))
                         (loop (+ d 1)))))]
              [else (error "unsupported degree pattern")]))]
         [r (car dims)] [c (cdr dims)]
         ; locate a corner node
         [corner (let find-corner ()
                   (let loop ((i 0))
                     (if (= i n) (error "no corner")
                         (if (= (vector-ref deg i) 2) i (loop (+ i 1))))))]
         ; its two neighbors
         [nbrs (vector-ref adj corner)]
         [right-nbr (car nbrs)]
         [down-nbr (cadr nbrs)]
         ; coordinate maps
         [coord (make-vector n #f)]
         [_ (vector-set! coord corner (cons 0 0))
            (vector-set! coord right-nbr (cons 0 1))
            (vector-set! coord down-nbr (cons 1 0))]
         ; BFS to assign coordinates
         [queue (list corner right-nbr down-nbr)]
         [_ (let bfs ((q queue) (visited (make-hash)))
               (when (not (null? q))
                 (define u (car q))
                 (hash-set! visited u #t)
                 (for ([v (in-list (vector-ref adj u))])
                   (unless (hash-has-key? visited v)
                     (if (not (vector-ref coord v))
                         (let* ([pu (vector-ref coord u)]
                                [neighbors (filter (lambda (x) (vector-ref coord x)) (vector-ref adj u))]
                                [used-dirs
                                 (map (lambda (w)
                                        (let* ([pw (vector-ref coord w)]
                                               [dx (- (car pw) (car pu))]
                                               [dy (- (cdr pw) (cdr pu))])
                                          (cons dx dy)))
                                      neighbors)])
                           ; pick a direction not used yet (horizontal or vertical)
                           (cond
                             [(and (not (member '(1 . 0) used-dirs))
                                   (not (member '(-1 . 0) used-dirs)))
                              (vector-set! coord v (cons (+ (car pu) 1) (cdr pu)))]
                             [(and (not (member '(0 . 1) used-dirs))
                                   (not (member '(0 . -1) used-dirs)))
                              (vector-set! coord v (cons (car pu) (+ (cdr pu) 1)))]
                             [else
                              ; fallback: try any unit direction
                              (let ([dx (if (= (car pu) 0) 1 0)]
                                    [dy (if (= (cdr pu) 0) 1 0)])
                                (vector-set! coord v (cons (+ (car pu) dx) (+ (cdr pu) dy))))])))
                     (set! q (append q (list v))))))
                 (bfs (cdr q) visited)))])
         ; collect nodes by coordinates
         [grid (make-vector r (lambda () (make-vector c -1)))]
         [_ (for ([i (in-range n)])
              (let* ([p (vector-ref coord i)]
                     [row (car p)] [col (cdr p)])
                (vector-set! (vector-ref grid row) col i)))]
         ; convert to list of lists
         [result (let build ()
                   (map (lambda (rowvec)
                          (let loop ((j 0) (acc '()))
                            (if (= j c) (reverse acc)
                                (loop (+ j 1) (cons (vector-ref rowvec j) acc)))))
                        (vector->list grid)))])
    result))
```

## Erlang

```erlang
-spec construct_grid_layout(N :: integer(), Edges :: [[integer()]]) -> [[integer()]].
construct_grid_layout(_N, Edges) ->
    Adj = build_adj(Edges, #{}),
    % Find nodes by degree
    Deg1 = [V || {V,Ns} <- maps:to_list(Adj), length(Ns) == 1],
    case Deg1 of
        [_Start,_End] ->                     % line case
            Start = hd(Deg1),
            Order = traverse_line(Start, Adj, [] , undefined),
            [Order];
        _ ->
            Corners = [V || {V,Ns} <- maps:to_list(Adj), length(Ns) == 2],
            [C0|Rest] = Corners,
            Dist0 = bfs(C0, Adj),
            % sort remaining corners by distance from C0
            Sorted = lists:keysort(2, [{C, maps:get(C, Dist0)} || C <- Rest]),
            [{C1,D1},{C2,D2},{Opp,_}] = Sorted,
            Rlen = D1 + 1,
            Clen = D2 + 1,
            Dist1 = bfs(C1, Adj),
            Dist2 = bfs(C2, Adj),
            CoordMap = fill_coords(N, Dist0, Dist1, Dist2, Rlen, Clen, #{}),
            build_grid(Rlen, Clen, CoordMap)
    end.

build_adj([], Acc) -> Acc;
build_adj([[U,V]|Rest], Acc) ->
    Acc1 = maps:update_with(U,
                fun(L) -> [V|L] end,
                [V],
                Acc),
    Acc2 = maps:update_with(V,
                fun(L) -> [U|L] end,
                [U],
                Acc1),
    build_adj(Rest, Acc2).

traverse_line(Node, Adj, Acc, Prev) ->
    NewAcc = [Node|Acc],
    Neighs = maps:get(Node, Adj, []),
    Next = case lists:filter(fun(N) -> N =/= Prev end, Neighs) of
               [] -> undefined;
               [N] -> N
           end,
    case Next of
        undefined -> lists:reverse(NewAcc);
        _ -> traverse_line(Next, Adj, NewAcc, Node)
    end.

bfs(Start, Adj) ->
    Q0 = queue:in(Start, queue:new()),
    Dist0 = maps:put(Start, 0, #{}),
    bfs_loop(Q0, Dist0, Adj).

bfs_loop(Q, Dist, Adj) ->
    case queue:out(Q) of
        {empty, _} -> Dist;
        {{value, Node}, Q1} ->
            D = maps:get(Node, Dist),
            Neighs = maps:get(Node, Adj, []),
            {Dist2, Q2} = lists:foldl(fun(Nbr,{AccDist,AccQ}) ->
                case maps:is_key(Nbr, AccDist) of
                    true -> {AccDist, AccQ};
                    false ->
                        {maps:put(Nbr, D+1, AccDist), queue:in(Nbr, AccQ)}
                end
            end, {Dist, Q1}, Neighs),
            bfs_loop(Q2, Dist2, Adj)
    end.

fill_coords(0, _, _, _, _, _, Acc) -> Acc;
fill_coords(N, D0, D1, D2, Rlen, Clen, Acc) ->
    Node = N-1,
    X = (maps:get(Node, D0) - maps:get(Node, D1) + (Rlen-1)) div 2,
    Y = (maps:get(Node, D0) - maps:get(Node, D2) + (Clen-1)) div 2,
    NewAcc = maps:put({X,Y}, Node, Acc),
    fill_coords(Node, D0, D1, D2, Rlen, Clen, NewAcc).

build_grid(R, C, CoordMap) ->
    [ [ maps:get({Row,Col}, CoordMap) || Col <- lists:seq(0, C-1) ]
      || Row <- lists:seq(0, R-1) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_grid_layout(integer, [[integer]]) :: [[integer]]
  def construct_grid_layout(n, edges) do
    # Build adjacency list using :array for fast indexed access
    adj = build_adj(n, edges)

    degrees =
      Enum.map(0..n - 1, fn i ->
        length(:array.get(i, adj))
      end)

    min_deg = Enum.min(degrees)
    corners = for i <- 0..n - 1, deg = Enum.at(degrees, i), deg == min_deg, do: i

    # Choose a corner as origin
    c0 = hd(corners)
    dist0 = bfs(c0, adj, n)

    if length(corners) == 2 and min_deg == 1 do
      # The graph is a simple path (1 x n grid)
      nodes_by_dist =
        Enum.map(0..n - 1, fn i ->
          {i, :array.get(i, dist0)}
        end)
        |> Enum.sort_by(fn {_id, d} -> d end)

      row = Enum.map(nodes_by_dist, fn {id, _d} -> id end)
      [row]
    else
      # Grid with at least 2 rows and 2 columns
      corner_infos =
        for c <- corners do
          {c, :array.get(c, dist0)}
        end

      # Sort corners (excluding the origin) by distance from origin
      sorted_corners =
        corner_infos
        |> Enum.filter(fn {_c, d} -> d != 0 end)
        |> Enum.sort_by(fn {_c, d} -> d end)

      [{corner_down, d_row}, {corner_right, d_col}] = sorted_corners

      rows = d_row + 1
      cols = d_col + 1

      dist_down = bfs(corner_down, adj, n)

      positions =
        Enum.reduce(0..n - 1, %{}, fn i, acc ->
          d0 = :array.get(i, dist0)
          dd = :array.get(i, dist_down)
          x = div(d0 - dd + rows - 1, 2)
          y = d0 - x
          Map.put(acc, {x, y}, i)
        end)

      for r <- 0..rows - 1 do
        for c <- 0..cols - 1 do
          Map.get(positions, {r, c})
        end
      end
    end
  end

  defp build_adj(n, edges) do
    init = :array.new(n, default: [])
    Enum.reduce(edges, init, fn [u, v], acc ->
      list_u = :array.get(u, acc)
      list_v = :array.get(v, acc)
      acc
      |> :array.set(u, [v | list_u])
      |> :array.set(v, [u | list_v])
    end)
  end

  defp bfs(start, adj, n) do
    dist = :array.new(n, default: -1)
    q0 = :queue.from_list([start])
    dist = :array.set(start, 0, dist)
    bfs_loop(q0, adj, dist)
  end

  defp bfs_loop(queue, adj, dist) do
    case :queue.out(queue) do
      {:empty, _} ->
        dist

      {{:value, node}, q2} ->
        d = :array.get(node, dist)

        neighbors = :array.get(node, adj)

        {dist2, q3} =
          Enum.reduce(neighbors, {dist, q2}, fn nb, {dacc, qacc} ->
            if :array.get(nb, dacc) == -1 do
              dnew = :array.set(nb, d + 1, dacc)
              {dnew, :queue.in(nb, qacc)}
            else
              {dacc, qacc}
            end
          end)

        bfs_loop(q3, adj, dist2)
    end
  end
end
```
