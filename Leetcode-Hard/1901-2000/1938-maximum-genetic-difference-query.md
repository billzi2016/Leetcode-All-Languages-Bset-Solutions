# 1938. Maximum Genetic Difference Query

## Cpp

```cpp
class Solution {
public:
    struct TrieNode {
        int nxt[2];
        int cnt;
        TrieNode() { nxt[0] = nxt[1] = -1; cnt = 0; }
    };
    
    const int MAXBIT = 20; // enough for values up to >2*10^5
    
    vector<TrieNode> trie;
    vector<vector<int>> tree;
    vector<vector<pair<int,int>>> qlist;
    vector<int> ans;
    
    void add(int x, int delta) {
        int node = 0;
        trie[node].cnt += delta;
        for (int b = MAXBIT; b >= 0; --b) {
            int bit = (x >> b) & 1;
            if (trie[node].nxt[bit] == -1) {
                trie[node].nxt[bit] = (int)trie.size();
                trie.emplace_back();
            }
            node = trie[node].nxt[bit];
            trie[node].cnt += delta;
        }
    }
    
    int queryMaxXor(int x) {
        int node = 0;
        int res = 0;
        for (int b = MAXBIT; b >= 0; --b) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            if (trie[node].nxt[want] != -1 && trie[trie[node].nxt[want]].cnt > 0) {
                res |= (1 << b);
                node = trie[node].nxt[want];
            } else {
                node = trie[node].nxt[bit];
            }
        }
        return res;
    }
    
    void dfs(int u) {
        add(u, +1);
        for (auto &pr : qlist[u]) {
            int val = pr.first;
            int idx = pr.second;
            ans[idx] = queryMaxXor(val);
        }
        for (int v : tree[u]) dfs(v);
        add(u, -1);
    }
    
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        int n = parents.size();
        tree.assign(n, {});
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (parents[i] == -1) root = i;
            else tree[parents[i]].push_back(i);
        }
        
        qlist.assign(n, {});
        int m = queries.size();
        ans.resize(m);
        for (int i = 0; i < m; ++i) {
            int node = queries[i][0];
            int val = queries[i][1];
            qlist[node].push_back({val, i});
        }
        
        trie.clear();
        trie.emplace_back(); // root of trie
        
        dfs(root);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Query {
        int idx;
        int val;
        Query(int i, int v) { idx = i; val = v; }
    }

    private static class Trie {
        int[][] next;
        int[] cnt;
        int nodes;
        final int BIT;

        Trie(int maxNodes, int bit) {
            this.BIT = bit;
            next = new int[maxNodes][2];
            cnt = new int[maxNodes];
            nodes = 1; // root is 0
        }

        void insert(int num) {
            int cur = 0;
            for (int b = BIT - 1; b >= 0; --b) {
                int bit = (num >> b) & 1;
                if (next[cur][bit] == 0) {
                    next[cur][bit] = nodes++;
                }
                cur = next[cur][bit];
                cnt[cur]++;
            }
        }

        void delete(int num) {
            int cur = 0;
            for (int b = BIT - 1; b >= 0; --b) {
                int bit = (num >> b) & 1;
                cur = next[cur][bit];
                cnt[cur]--;
            }
        }

        int maxXor(int num) {
            int cur = 0;
            int res = 0;
            for (int b = BIT - 1; b >= 0; --b) {
                int bit = (num >> b) & 1;
                int want = bit ^ 1;
                if (next[cur][want] != 0 && cnt[next[cur][want]] > 0) {
                    res |= (1 << b);
                    cur = next[cur][want];
                } else {
                    cur = next[cur][bit];
                }
            }
            return res;
        }
    }

    public int[] maxGeneticDifference(int[] parents, int[][] queries) {
        int n = parents.length;
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; ++i) children[i] = new ArrayList<>();
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (parents[i] == -1) {
                root = i;
            } else {
                children[parents[i]].add(i);
            }
        }

        // group queries by node
        @SuppressWarnings("unchecked")
        List<Query>[] qlist = new ArrayList[n];
        int maxQueryVal = 0;
        for (int i = 0; i < queries.length; ++i) {
            int node = queries[i][0];
            int val = queries[i][1];
            if (qlist[node] == null) qlist[node] = new ArrayList<>();
            qlist[node].add(new Query(i, val));
            if (val > maxQueryVal) maxQueryVal = val;
        }

        int maxNodeVal = n - 1;
        int maxVal = Math.max(maxNodeVal, maxQueryVal);
        int BIT = 0;
        while ((1 << BIT) <= maxVal) BIT++;
        // allocate enough trie nodes
        int maxTrieNodes = (n + 5) * (BIT + 1);
        Trie trie = new Trie(maxTrieNodes, BIT);

        int[] ans = new int[queries.length];

        // iterative DFS with explicit stack
        int[] nodeStack = new int[n];
        int[] idxStack = new int[n];
        int sp = 0;
        nodeStack[sp] = root;
        idxStack[sp] = 0;

        trie.insert(root); // insert root value

        while (sp >= 0) {
            int u = nodeStack[sp];
            int childIdx = idxStack[sp];

            if (childIdx == 0) { // first time at this node
                List<Query> qs = qlist[u];
                if (qs != null) {
                    for (Query q : qs) {
                        ans[q.idx] = trie.maxXor(q.val);
                    }
                }
            }

            if (childIdx < children[u].size()) {
                int v = children[u].get(childIdx);
                idxStack[sp]++; // move to next child for current node
                sp++;
                nodeStack[sp] = v;
                idxStack[sp] = 0;
                trie.insert(v);
            } else {
                // all children processed, backtrack
                trie.delete(u);
                sp--;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(300000)

        n = len(parents)
        adj = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                adj[p].append(i)

        q_by_node = {}
        for idx, (node, val) in enumerate(queries):
            q_by_node.setdefault(node, []).append((val, idx))

        ans = [0] * len(queries)

        # Trie implementation with counts for removal
        MAX_BIT = 20  # enough for values up to ~2*10^5

        class TrieNode:
            __slots__ = ('child', 'cnt')
            def __init__(self):
                self.child = [None, None]
                self.cnt = 0

        root_trie = TrieNode()

        def insert(num, delta):
            node = root_trie
            for b in range(MAX_BIT - 1, -1, -1):
                bit = (num >> b) & 1
                if not node.child[bit]:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
                node.cnt += delta

        def max_xor(val):
            node = root_trie
            res = 0
            for b in range(MAX_BIT - 1, -1, -1):
                bit = (val >> b) & 1
                toggled = bit ^ 1
                if node.child[toggled] and node.child[toggled].cnt > 0:
                    res |= (1 << b)
                    node = node.child[toggled]
                else:
                    node = node.child[bit]
            return res

        def dfs(u):
            insert(u, 1)
            for val, idx in q_by_node.get(u, []):
                ans[idx] = max_xor(val)
            for v in adj[u]:
                dfs(v)
            insert(u, -1)

        dfs(root)
        return ans
```

## Python3

```python
class Solution:
    def maxGeneticDifference(self, parents, queries):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(300000)

        n = len(parents)
        # build tree
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # group queries by node
        q_by_node = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            q_by_node[node].append((idx, val))

        ans = [0] * len(queries)

        MAX_BIT = 20  # enough for values up to ~2*10^5

        # trie node: [child0, child1, count]
        trie = [[-1, -1, 0]]

        def insert(num):
            node = 0
            trie[node][2] += 1
            for i in range(MAX_BIT, -1, -1):
                b = (num >> i) & 1
                if trie[node][b] == -1:
                    trie.append([-1, -1, 0])
                    trie[node][b] = len(trie) - 1
                node = trie[node][b]
                trie[node][2] += 1

        def delete(num):
            node = 0
            trie[node][2] -= 1
            for i in range(MAX_BIT, -1, -1):
                b = (num >> i) & 1
                nxt = trie[node][b]
                node = nxt
                trie[node][2] -= 1

        def max_xor(val):
            node = 0
            res = 0
            for i in range(MAX_BIT, -1, -1):
                b = (val >> i) & 1
                want = 1 - b
                if trie[node][want] != -1 and trie[trie[node][want]][2] > 0:
                    res |= (1 << i)
                    node = trie[node][want]
                else:
                    node = trie[node][b]
            return res

        def dfs(u):
            insert(u)
            for idx, v in q_by_node.get(u, []):
                ans[idx] = max_xor(v)
            for v in children[u]:
                dfs(v)
            delete(u)

        dfs(root)
        return ans
```

## C

```c
#include <stdlib.h>

#define MAX_BIT 20   // enough for values up to ~2*10^5

typedef struct {
    int child[2];
    int cnt;
} TrieNode;

static TrieNode *trie;
static int trieSize;
static int nodeCount;

/* create a new trie node */
static int newNode() {
    int id = nodeCount++;
    trie[id].child[0] = trie[id].child[1] = -1;
    trie[id].cnt = 0;
    return id;
}

/* insert or remove value x (delta = +1 for insert, -1 for delete) */
static void updateTrie(int x, int delta) {
    int cur = 0;
    trie[cur].cnt += delta;
    for (int b = MAX_BIT - 1; b >= 0; --b) {
        int bit = (x >> b) & 1;
        if (trie[cur].child[bit] == -1) {
            trie[cur].child[bit] = newNode();
        }
        cur = trie[cur].child[bit];
        trie[cur].cnt += delta;
    }
}

/* query maximum xor with val among numbers present in the trie */
static int queryMaxXor(int val) {
    int cur = 0;
    int ans = 0;
    for (int b = MAX_BIT - 1; b >= 0; --b) {
        int bit = (val >> b) & 1;
        int want = bit ^ 1;
        if (trie[cur].child[want] != -1 && trie[trie[cur].child[want]].cnt > 0) {
            ans |= (1 << b);
            cur = trie[cur].child[want];
        } else {
            cur = trie[cur].child[bit];
        }
    }
    return ans;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxGeneticDifference(int* parents, int parentsSize, int** queries, int queriesSize,
                          int* queriesColSize, int* returnSize) {
    int n = parentsSize;

    /* build children adjacency list */
    int *firstChild = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) firstChild[i] = -1;
    int edgeCnt = n - 1;
    int *to = (int *)malloc(edgeCnt * sizeof(int));
    int *nextEdge = (int *)malloc(edgeCnt * sizeof(int));
    int e = 0;
    int root = -1;
    for (int i = 0; i < n; ++i) {
        if (parents[i] == -1) {
            root = i;
        } else {
            int p = parents[i];
            to[e] = i;
            nextEdge[e] = firstChild[p];
            firstChild[p] = e;
            ++e;
        }
    }

    /* store queries per node */
    int *headQ = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) headQ[i] = -1;
    int *nextQ = (int *)malloc(queriesSize * sizeof(int));
    int *qVal = (int *)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int node = queries[i][0];
        int val  = queries[i][1];
        qVal[i] = val;
        nextQ[i] = headQ[node];
        headQ[node] = i;
    }

    /* allocate answer array */
    int *ans = (int *)malloc(queriesSize * sizeof(int));

    /* initialise trie */
    int maxNodes = (n + queriesSize + 5) * MAX_BIT;
    trie = (TrieNode *)malloc(maxNodes * sizeof(TrieNode));
    nodeCount = 0;
    newNode();               // root of trie at index 0
    trie[0].cnt = 0;

    /* iterative DFS with explicit stack */
    int stackCap = 2 * n + 5;
    int *stackNode = (int *)malloc(stackCap * sizeof(int));
    char *stackState = (char *)malloc(stackCap * sizeof(char)); // 0 = enter, 1 = exit
    int top = 0;

    stackNode[top] = root;
    stackState[top] = 0;
    ++top;

    while (top) {
        --top;
        int u = stackNode[top];
        char state = stackState[top];

        if (state == 0) {               // entering node
            updateTrie(u, +1);

            for (int qi = headQ[u]; qi != -1; qi = nextQ[qi]) {
                ans[qi] = queryMaxXor(qVal[qi]);
            }

            /* push exit marker */
            stackNode[top] = u;
            stackState[top] = 1;
            ++top;

            /* push children */
            for (int ed = firstChild[u]; ed != -1; ed = nextEdge[ed]) {
                int v = to[ed];
                stackNode[top] = v;
                stackState[top] = 0;
                ++top;
            }
        } else {                         // exiting node
            updateTrie(u, -1);
        }
    }

    /* clean up */
    free(firstChild);
    free(to);
    free(nextEdge);
    free(headQ);
    free(nextQ);
    free(qVal);
    free(stackNode);
    free(stackState);
    free(trie);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MAX_BIT = 20; // enough for values up to ~2*10^5
    
    private class TrieNode {
        public int[] child = new int[2] { -1, -1 };
        public int cnt = 0;
    }
    
    private List<TrieNode> trie = new List<TrieNode>();
    
    private void Update(int num, int delta) {
        int node = 0;
        trie[node].cnt += delta;
        for (int b = MAX_BIT - 1; b >= 0; --b) {
            int bit = (num >> b) & 1;
            if (trie[node].child[bit] == -1) {
                trie[node].child[bit] = trie.Count;
                trie.Add(new TrieNode());
            }
            node = trie[node].child[bit];
            trie[node].cnt += delta;
        }
    }
    
    private int GetMaxXor(int val) {
        int node = 0;
        int ans = 0;
        for (int b = MAX_BIT - 1; b >= 0; --b) {
            int bit = (val >> b) & 1;
            int desired = 1 - bit;
            int next = trie[node].child[desired];
            if (next != -1 && trie[next].cnt > 0) {
                ans |= (1 << b);
                node = next;
            } else {
                int other = trie[node].child[bit];
                // other must exist because at least one number is in the trie
                node = other;
            }
        }
        return ans;
    }
    
    private class QueryInfo {
        public int val;
        public int idx;
        public QueryInfo(int v, int i) { val = v; idx = i; }
    }
    
    public int[] MaxGeneticDifference(int[] parents, int[][] queries) {
        int n = parents.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; ++i) children[i] = new List<int>();
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (parents[i] == -1) {
                root = i;
            } else {
                children[parents[i]].Add(i);
            }
        }
        
        var qlist = new List<QueryInfo>[n];
        for (int i = 0; i < n; ++i) qlist[i] = new List<QueryInfo>();
        int m = queries.Length;
        for (int i = 0; i < m; ++i) {
            int node = queries[i][0];
            int val = queries[i][1];
            qlist[node].Add(new QueryInfo(val, i));
        }
        
        int[] ans = new int[m];
        trie.Add(new TrieNode()); // root of trie
        
        var stack = new Stack<(int node, int state)>();
        stack.Push((root, 0)); // 0 = enter, 1 = exit
        
        while (stack.Count > 0) {
            var cur = stack.Pop();
            int u = cur.node;
            if (cur.state == 0) {
                // entering
                Update(u, +1);
                
                foreach (var q in qlist[u]) {
                    ans[q.idx] = GetMaxXor(q.val);
                }
                
                stack.Push((u, 1)); // schedule exit
                
                // push children for DFS
                var childs = children[u];
                for (int i = childs.Count - 1; i >= 0; --i) {
                    stack.Push((childs[i], 0));
                }
            } else {
                // exiting
                Update(u, -1);
            }
        }
        
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parents
 * @param {number[][]} queries
 * @return {number[]}
 */
var maxGeneticDifference = function(parents, queries) {
    const n = parents.length;
    const children = Array.from({length: n}, () => []);
    let root = -1;
    for (let i = 0; i < n; ++i) {
        const p = parents[i];
        if (p === -1) {
            root = i;
        } else {
            children[p].push(i);
        }
    }

    // group queries by node
    const qByNode = Array.from({length: n}, () => []);
    for (let i = 0; i < queries.length; ++i) {
        const [node, val] = queries[i];
        qByNode[node].push([val, i]);
    }
    const ans = new Array(queries.length);

    // binary trie
    const MAX_BIT = 20; // enough for values up to >2e5
    const trie = [{next: [-1, -1], cnt: 0}]; // root at index 0

    function insert(num) {
        let node = 0;
        for (let b = MAX_BIT; b >= 0; --b) {
            const bit = (num >> b) & 1;
            if (trie[node].next[bit] === -1) {
                trie[node].next[bit] = trie.length;
                trie.push({next: [-1, -1], cnt: 0});
            }
            node = trie[node].next[bit];
            trie[node].cnt++;
        }
    }

    function remove(num) {
        let node = 0;
        for (let b = MAX_BIT; b >= 0; --b) {
            const bit = (num >> b) & 1;
            node = trie[node].next[bit];
            trie[node].cnt--;
        }
    }

    function query(num) {
        let node = 0;
        let res = 0;
        for (let b = MAX_BIT; b >= 0; --b) {
            const bit = (num >> b) & 1;
            const prefer = bit ^ 1;
            const prefNode = trie[node].next[prefer];
            if (prefNode !== -1 && trie[prefNode].cnt > 0) {
                res |= (1 << b);
                node = prefNode;
            } else {
                node = trie[node].next[bit];
            }
        }
        return res;
    }

    // iterative DFS with explicit stack
    const stack = [];
    stack.push([root, false]); // [node, visitedFlag]

    while (stack.length) {
        const [u, exited] = stack.pop();
        if (!exited) {
            insert(u);
            // answer queries at u
            for (const [val, idx] of qByNode[u]) {
                ans[idx] = query(val);
            }
            // push exit marker
            stack.push([u, true]);
            // push children
            const childs = children[u];
            for (let i = childs.length - 1; i >= 0; --i) {
                stack.push([childs[i], false]);
            }
        } else {
            remove(u);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxGeneticDifference(parents: number[], queries: number[][]): number[] {
    const n = parents.length;
    const tree: number[][] = Array.from({ length: n }, () => []);
    let root = -1;
    for (let i = 0; i < n; i++) {
        const p = parents[i];
        if (p === -1) {
            root = i;
        } else {
            tree[p].push(i);
        }
    }

    const qByNode: number[][][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < queries.length; i++) {
        const [node, val] = queries[i];
        qByNode[node].push([val, i]);
    }

    const ans = new Array(queries.length).fill(0);
    const MAX_BIT = 20;

    class TrieNode {
        child: (TrieNode | null)[];
        cnt: number;
        constructor() {
            this.child = [null, null];
            this.cnt = 0;
        }
    }

    const trieRoot = new TrieNode();

    function insert(x: number): void {
        let node = trieRoot;
        for (let i = MAX_BIT; i >= 0; i--) {
            const b = (x >> i) & 1;
            if (!node.child[b]) node.child[b] = new TrieNode();
            node = node.child[b]!;
            node.cnt++;
        }
    }

    function remove(x: number): void {
        let node = trieRoot;
        for (let i = MAX_BIT; i >= 0; i--) {
            const b = (x >> i) & 1;
            const nxt = node.child[b];
            if (!nxt) return;
            node = nxt;
            node.cnt--;
        }
    }

    function query(val: number): number {
        let node = trieRoot;
        let res = 0;
        for (let i = MAX_BIT; i >= 0; i--) {
            const b = (val >> i) & 1;
            const toggled = b ^ 1;
            if (node.child[toggled] && node.child[toggled]!.cnt > 0) {
                res |= (1 << i);
                node = node.child[toggled]!;
            } else {
                node = node.child[b]!;
            }
        }
        return res;
    }

    const stack: [number, number][] = [];
    if (root !== -1) stack.push([root, 0]);

    while (stack.length) {
        const [u, state] = stack.pop()!;
        if (state === 0) {
            insert(u);
            for (const [val, idx] of qByNode[u]) {
                ans[idx] = query(val);
            }
            stack.push([u, 1]);
            const children = tree[u];
            for (let i = children.length - 1; i >= 0; i--) {
                stack.push([children[i], 0]);
            }
        } else {
            remove(u);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maxGeneticDifference($parents, $queries) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        $root = -1;
        for ($i = 0; $i < $n; $i++) {
            $p = $parents[$i];
            if ($p == -1) {
                $root = $i;
            } else {
                $children[$p][] = $i;
            }
        }

        // group queries by node
        $nodeQueries = array_fill(0, $n, []);
        foreach ($queries as $idx => $q) {
            $node = $q[0];
            $val  = $q[1];
            $nodeQueries[$node][] = [$idx, $val];
        }

        $ansCount = count($queries);
        $ans = array_fill(0, $ansCount, 0);

        // binary trie
        $MAX_BIT = 20; // enough for values up to ~2*10^5
        $trie = [[-1, -1]];
        $cnt  = [0];

        $insert = function($num) use (&$trie, &$cnt, $MAX_BIT) {
            $node = 0;
            for ($i = $MAX_BIT; $i >= 0; $i--) {
                $bit = ($num >> $i) & 1;
                if ($trie[$node][$bit] == -1) {
                    $trie[] = [-1, -1];
                    $cnt[] = 0;
                    $newIdx = count($trie) - 1;
                    $trie[$node][$bit] = $newIdx;
                }
                $node = $trie[$node][$bit];
                $cnt[$node]++;
            }
        };

        $remove = function($num) use (&$trie, &$cnt, $MAX_BIT) {
            $node = 0;
            for ($i = $MAX_BIT; $i >= 0; $i--) {
                $bit = ($num >> $i) & 1;
                $node = $trie[$node][$bit];
                $cnt[$node]--;
            }
        };

        $queryTrie = function($num) use (&$trie, &$cnt, $MAX_BIT) {
            $node = 0;
            $res = 0;
            for ($i = $MAX_BIT; $i >= 0; $i--) {
                $bit = ($num >> $i) & 1;
                $desired = 1 - $bit;
                if ($trie[$node][$desired] != -1 && $cnt[$trie[$node][$desired]] > 0) {
                    $res |= (1 << $i);
                    $node = $trie[$node][$desired];
                } else {
                    $node = $trie[$node][$bit];
                }
            }
            return $res;
        };

        // iterative DFS with explicit stack
        $stack = [];
        array_push($stack, [$root, 0]); // state 0 = enter, 1 = exit

        while (!empty($stack)) {
            $item = array_pop($stack);
            $node = $item[0];
            $state = $item[1];

            if ($state === 0) {
                // entering node
                $insert($node);

                foreach ($nodeQueries[$node] as $qinfo) {
                    [$qid, $val] = $qinfo;
                    $ans[$qid] = $queryTrie($val);
                }

                // schedule exit after children
                array_push($stack, [$node, 1]);

                // push children (reverse order not important)
                $childList = $children[$node];
                for ($i = count($childList) - 1; $i >= 0; $i--) {
                    array_push($stack, [$childList[$i], 0]);
                }
            } else {
                // exiting node
                $remove($node);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct TrieNode {
        var child: [Int] = [-1, -1]
        var cnt: Int = 0
    }
    
    func maxGeneticDifference(_ parents: [Int], _ queries: [[Int]]) -> [Int] {
        let n = parents.count
        // Build adjacency list
        var children = [[Int]](repeating: [], count: n)
        var root = 0
        for i in 0..<n {
            let p = parents[i]
            if p == -1 {
                root = i
            } else {
                children[p].append(i)
            }
        }
        
        // Group queries by node
        var nodeQueries = [[(Int, Int)]](repeating: [], count: n)
        for (idx, q) in queries.enumerated() {
            let node = q[0]
            let val = q[1]
            nodeQueries[node].append((val, idx))
        }
        var answers = [Int](repeating: 0, count: queries.count)
        
        // Trie
        var trie = [TrieNode]()
        trie.append(TrieNode()) // root at index 0
        let MAX_BIT = 20   // enough for values up to ~2*10^5
        
        func modify(_ num: Int, _ delta: Int) {
            var nodeIdx = 0
            trie[nodeIdx].cnt += delta
            for i in stride(from: MAX_BIT, through: 0, by: -1) {
                let bit = (num >> i) & 1
                if trie[nodeIdx].child[bit] == -1 {
                    trie.append(TrieNode())
                    trie[nodeIdx].child[bit] = trie.count - 1
                }
                nodeIdx = trie[nodeIdx].child[bit]
                trie[nodeIdx].cnt += delta
            }
        }
        
        func query(_ num: Int) -> Int {
            var nodeIdx = 0
            var res = 0
            for i in stride(from: MAX_BIT, through: 0, by: -1) {
                let bit = (num >> i) & 1
                let desired = bit ^ 1
                if let next = trie[nodeIdx].child[desired], next != -1,
                   trie[next].cnt > 0 {
                    res |= (1 << i)
                    nodeIdx = next
                } else {
                    nodeIdx = trie[nodeIdx].child[bit]
                }
            }
            return res
        }
        
        // Iterative DFS with explicit stack to avoid recursion depth issues
        var stack: [(node: Int, state: Int)] = []   // state 0 = enter, 1 = exit
        stack.append((root, 0))
        while let cur = stack.popLast() {
            let node = cur.node
            if cur.state == 0 {
                // entering node
                modify(node, 1)
                // answer queries for this node
                for (val, idx) in nodeQueries[node] {
                    answers[idx] = query(val)
                }
                // push exit marker
                stack.append((node, 1))
                // push children (enter state)
                let childs = children[node]
                if !childs.isEmpty {
                    for child in childs.reversed() {   // reversed to maintain original order
                        stack.append((child, 0))
                    }
                }
            } else {
                // exiting node
                modify(node, -1)
            }
        }
        
        return answers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxGeneticDifference(parents: IntArray, queries: Array<IntArray>): IntArray {
        val n = parents.size
        // Build tree adjacency list
        val children = Array(n) { mutableListOf<Int>() }
        var root = -1
        for (i in 0 until n) {
            val p = parents[i]
            if (p == -1) {
                root = i
            } else {
                children[p].add(i)
            }
        }

        // Group queries by node
        val qPerNode = Array(n) { mutableListOf<Pair<Int, Int>>() }
        var maxVal = 0
        for (i in queries.indices) {
            val node = queries[i][0]
            val v = queries[i][1]
            qPerNode[node].add(Pair(v, i))
            if (v > maxVal) maxVal = v
        }
        if (n - 1 > maxVal) maxVal = n - 1

        // Determine highest bit needed
        var maxBit = 0
        while ((1 shl maxBit) <= maxVal) {
            maxBit++
        }
        maxBit--
        if (maxBit < 0) maxBit = 0

        // Trie structures with count for deletions
        val nxt0 = mutableListOf<Int>()
        val nxt1 = mutableListOf<Int>()
        val cnt = mutableListOf<Int>()
        fun newNode(): Int {
            nxt0.add(-1)
            nxt1.add(-1)
            cnt.add(0)
            return nxt0.size - 1
        }
        newNode() // root node index 0

        fun insert(x: Int) {
            var node = 0
            cnt[node]++
            for (i in maxBit downTo 0) {
                val b = (x shr i) and 1
                var next = if (b == 0) nxt0[node] else nxt1[node]
                if (next == -1) {
                    next = newNode()
                    if (b == 0) nxt0[node] = next else nxt1[node] = next
                }
                node = next
                cnt[node]++
            }
        }

        fun remove(x: Int) {
            var node = 0
            cnt[node]--
            for (i in maxBit downTo 0) {
                val b = (x shr i) and 1
                val next = if (b == 0) nxt0[node] else nxt1[node]
                node = next
                cnt[node]--
            }
        }

        fun queryMax(x: Int): Int {
            var node = 0
            var ans = 0
            for (i in maxBit downTo 0) {
                val b = (x shr i) and 1
                val pref = if (b == 0) nxt1[node] else nxt0[node]
                if (pref != -1 && cnt[pref] > 0) {
                    ans = ans or (1 shl i)
                    node = pref
                } else {
                    val same = if (b == 0) nxt0[node] else nxt1[node]
                    node = same
                }
            }
            return ans
        }

        val res = IntArray(queries.size)

        // Iterative DFS with explicit stack for backtracking
        data class StackItem(val node: Int, val visited: Boolean)
        val stack = java.util.ArrayDeque<StackItem>()
        stack.push(StackItem(root, false))
        while (stack.isNotEmpty()) {
            val cur = stack.pop()
            if (!cur.visited) {
                // Enter node
                insert(cur.node)
                for ((v, idx) in qPerNode[cur.node]) {
                    res[idx] = queryMax(v)
                }
                // Exit marker
                stack.push(StackItem(cur.node, true))
                // Push children
                val childs = children[cur.node]
                for (i in childs.size - 1 downTo 0) {
                    stack.push(StackItem(childs[i], false))
                }
            } else {
                // Exit node
                remove(cur.node)
            }
        }

        return res
    }
}
```

## Dart

```dart
class Query {
  int val;
  int idx;
  Query(this.val, this.idx);
}

class TrieNode {
  List<TrieNode?> child = [null, null];
  int cnt = 0;
}

class Solution {
  static const int _MAX_BIT = 20; // enough for values up to ~1e6

  void _insert(TrieNode root, int num) {
    TrieNode node = root;
    for (int i = _MAX_BIT; i >= 0; --i) {
      int b = (num >> i) & 1;
      if (node.child[b] == null) node.child[b] = TrieNode();
      node = node.child[b]!;
      node.cnt++;
    }
  }

  void _remove(TrieNode root, int num) {
    TrieNode node = root;
    for (int i = _MAX_BIT; i >= 0; --i) {
      int b = (num >> i) & 1;
      TrieNode? nxt = node.child[b];
      if (nxt == null) return;
      nxt.cnt--;
      node = nxt;
    }
  }

  int _maxXor(TrieNode root, int num) {
    TrieNode node = root;
    int ans = 0;
    for (int i = _MAX_BIT; i >= 0; --i) {
      int b = (num >> i) & 1;
      int want = 1 - b;
      if (node.child[want] != null && node.child[want]!.cnt > 0) {
        ans |= (1 << i);
        node = node.child[want]!;
      } else {
        node = node.child[b]!;
      }
    }
    return ans;
  }

  List<int> maxGeneticDifference(List<int> parents, List<List<int>> queries) {
    int n = parents.length;
    List<List<int>> tree = List.generate(n, (_) => []);
    int root = -1;
    for (int i = 0; i < n; ++i) {
      if (parents[i] == -1) {
        root = i;
      } else {
        tree[parents[i]].add(i);
      }
    }

    List<List<Query>> qAtNode = List.generate(n, (_) => []);
    for (int i = 0; i < queries.length; ++i) {
      int node = queries[i][0];
      int val = queries[i][1];
      qAtNode[node].add(Query(val, i));
    }

    List<int> ans = List.filled(queries.length, 0);
    TrieNode trieRoot = TrieNode();

    // iterative DFS with explicit stack
    List<List<dynamic>> stack = [];
    stack.add([root, false]); // [node, exitingFlag]

    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int node = cur[0] as int;
      bool exiting = cur[1] as bool;

      if (exiting) {
        _remove(trieRoot, node);
      } else {
        _insert(trieRoot, node);
        for (var q in qAtNode[node]) {
          ans[q.idx] = _maxXor(trieRoot, q.val);
        }
        stack.add([node, true]); // add exit marker
        var children = tree[node];
        for (int i = children.length - 1; i >= 0; --i) {
          stack.add([children[i], false]);
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxGeneticDifference(parents []int, queries [][]int) []int {
	const MAXBIT = 20

	type TrieNode struct {
		child [2]*TrieNode
		cnt   int
	}
	insert := func(root *TrieNode, num int) {
		node := root
		for i := MAXBIT - 1; i >= 0; i-- {
			b := (num >> i) & 1
			if node.child[b] == nil {
				node.child[b] = &TrieNode{}
			}
			node = node.child[b]
			node.cnt++
		}
	}
	remove := func(root *TrieNode, num int) {
		node := root
		for i := MAXBIT - 1; i >= 0; i-- {
			b := (num >> i) & 1
			child := node.child[b]
			if child == nil {
				return
			}
			child.cnt--
			if child.cnt == 0 {
				node.child[b] = nil
				return
			}
			node = child
		}
	}
	maxXor := func(root *TrieNode, num int) int {
		node := root
		ans := 0
		for i := MAXBIT - 1; i >= 0; i-- {
			b := (num >> i) & 1
			want := 1 - b
			if node.child[want] != nil && node.child[want].cnt > 0 {
				ans |= 1 << i
				node = node.child[want]
			} else {
				node = node.child[b]
			}
		}
		return ans
	}

	n := len(parents)
	adj := make([][]int, n)
	rootIdx := -1
	for i, p := range parents {
		if p == -1 {
			rootIdx = i
		} else {
			adj[p] = append(adj[p], i)
		}
	}

	type pair struct{ val, idx int }
	qlist := make([][]pair, n)
	for i, q := range queries {
		node, val := q[0], q[1]
		qlist[node] = append(qlist[node], pair{val, i})
	}

	ans := make([]int, len(queries))
	trie := &TrieNode{}

	var dfs func(int)
	dfs = func(u int) {
		insert(trie, u)
		for _, p := range qlist[u] {
			ans[p.idx] = maxXor(trie, p.val)
		}
		for _, v := range adj[u] {
			dfs(v)
		}
		remove(trie, u)
	}

	dfs(rootIdx)
	return ans
}
```

## Ruby

```ruby
class TrieNode
  attr_accessor :child, :cnt
  def initialize
    @child = [nil, nil]
    @cnt = 0
  end
end

class Trie
  def initialize(max_bit)
    @max_bit = max_bit
    @root = TrieNode.new
  end

  def insert(num)
    node = @root
    @max_bit.downto(0) do |i|
      bit = (num >> i) & 1
      child = node.child[bit]
      unless child
        child = TrieNode.new
        node.child[bit] = child
      end
      child.cnt += 1
      node = child
    end
  end

  def remove(num)
    node = @root
    @max_bit.downto(0) do |i|
      bit = (num >> i) & 1
      child = node.child[bit]
      next unless child
      child.cnt -= 1
      node = child
    end
  end

  def max_xor(num)
    node = @root
    xor = 0
    @max_bit.downto(0) do |i|
      bit = (num >> i) & 1
      toggled = bit ^ 1
      if node.child[toggled] && node.child[toggled].cnt > 0
        xor |= (1 << i)
        node = node.child[toggled]
      else
        node = node.child[bit]
      end
    end
    xor
  end
end

# @param {Integer[]} parents
# @param {Integer[][]} queries
# @return {Integer[]}
def max_genetic_difference(parents, queries)
  n = parents.size
  children = Array.new(n) { [] }
  root = nil
  parents.each_with_index do |p, i|
    if p == -1
      root = i
    else
      children[p] << i
    end
  end

  q_by_node = Array.new(n) { [] }
  queries.each_with_index do |(node, _val), idx|
    q_by_node[node] << idx
  end

  # Use enough bits to cover possible values (up to ~2*10^5)
  max_bit = 20
  trie = Trie.new(max_bit)

  ans = Array.new(queries.size)

  stack = [[root, 0]]
  while !stack.empty?
    node, state = stack.pop
    if state == 0
      trie.insert(node)
      q_by_node[node].each do |idx|
        val = queries[idx][1]
        ans[idx] = trie.max_xor(val)
      end
      stack << [node, 1]
      children[node].reverse_each { |ch| stack << [ch, 0] }
    else
      trie.remove(node)
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def maxGeneticDifference(parents: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = parents.length
    val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    var root = -1
    for (i <- 0 until n) {
      val p = parents(i)
      if (p == -1) root = i else children(p).append(i)
    }

    val qByNode = Array.fill(n)(new scala.collection.mutable.ListBuffer[(Int, Int)]())
    for (i <- queries.indices) {
      val node = queries(i)(0)
      val value = queries(i)(1)
      qByNode(node).append((value, i))
    }
    val ans = new Array[Int](queries.length)

    // Trie parameters
    val MAX_BIT = 20 // enough for values up to ~2*10^5 and node indices
    val maxNodes = (n + queries.length + 5) * MAX_BIT
    val child = Array.ofDim[Int](maxNodes, 2)
    val cnt = new Array[Int](maxNodes)
    var nodeCnt = 1 // root of trie is index 0

    def modify(x: Int, delta: Int): Unit = {
      var cur = 0
      for (b <- (MAX_BIT - 1) to 0 by -1) {
        val bit = (x >> b) & 1
        if (child(cur)(bit) == 0) {
          child(cur)(bit) = nodeCnt
          nodeCnt += 1
        }
        cur = child(cur)(bit)
        cnt(cur) += delta
      }
    }

    def queryMaxXor(x: Int): Int = {
      var cur = 0
      var res = 0
      for (b <- (MAX_BIT - 1) to 0 by -1) {
        val bit = (x >> b) & 1
        val pref = bit ^ 1
        if (child(cur)(pref) != 0 && cnt(child(cur)(pref)) > 0) {
          res |= (1 << b)
          cur = child(cur)(pref)
        } else {
          cur = child(cur)(bit)
        }
      }
      res
    }

    // iterative DFS using stack (node, state) where state 0=enter, 1=exit
    val stack = new java.util.ArrayDeque[(Int, Int)]()
    stack.addLast((root, 0))
    while (!stack.isEmpty) {
      val (u, state) = stack.removeLast()
      if (state == 0) {
        modify(u, +1)
        // answer queries at this node
        for ((value, idx) <- qByNode(u)) {
          ans(idx) = queryMaxXor(value)
        }
        // push exit marker then children
        stack.addLast((u, 1))
        val ch = children(u)
        var i = ch.length - 1
        while (i >= 0) {
          stack.addLast((ch(i), 0))
          i -= 1
        }
      } else {
        modify(u, -1)
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::vec::Vec;

struct TrieNode {
    child: [i32; 2],
    cnt: i32,
}

struct Trie {
    nodes: Vec<TrieNode>,
}

impl Trie {
    const MAX_BIT: i32 = 20;
    fn new() -> Self {
        let root = TrieNode { child: [-1, -1], cnt: 0 };
        Self { nodes: vec![root] }
    }

    fn insert(&mut self, num: i32) {
        let mut node = 0usize;
        let x = num as u32;
        for k in (0..=Self::MAX_BIT).rev() {
            let bit = ((x >> k) & 1) as usize;
            if self.nodes[node].child[bit] == -1 {
                self.nodes.push(TrieNode { child: [-1, -1], cnt: 0 });
                let new_idx = (self.nodes.len() - 1) as i32;
                self.nodes[node].child[bit] = new_idx;
            }
            node = self.nodes[node].child[bit] as usize;
            self.nodes[node].cnt += 1;
        }
    }

    fn remove(&mut self, num: i32) {
        let mut node = 0usize;
        let x = num as u32;
        for k in (0..=Self::MAX_BIT).rev() {
            let bit = ((x >> k) & 1) as usize;
            node = self.nodes[node].child[bit] as usize;
            self.nodes[node].cnt -= 1;
        }
    }

    fn max_xor(&self, num: i32) -> i32 {
        let mut node = 0usize;
        let x = num as u32;
        let mut ans = 0i32;
        for k in (0..=Self::MAX_BIT).rev() {
            let bit = ((x >> k) & 1) as usize;
            let desired = 1 - bit;
            let next_bit = if self.nodes[node].child[desired] != -1
                && self.nodes[self.nodes[node].child[desired] as usize].cnt > 0
            {
                desired
            } else {
                bit
            };
            let xor_bit = (next_bit ^ bit) as i32;
            ans |= xor_bit << (k as u32);
            node = self.nodes[node].child[next_bit] as usize;
        }
        ans
    }
}

impl Solution {
    pub fn max_genetic_difference(parents: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = parents.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut root = 0usize;
        for i in 0..n {
            let p = parents[i];
            if p == -1 {
                root = i;
            } else {
                children[p as usize].push(i);
            }
        }

        let qlen = queries.len();
        let mut query_map: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
        for (i, q) in queries.iter().enumerate() {
            let node = q[0] as usize;
            let val = q[1];
            query_map[node].push((i, val));
        }

        let mut ans: Vec<i32> = vec![0; qlen];
        let mut trie = Trie::new();

        // iterative DFS with entry/exit markers
        let mut stack: Vec<(usize, bool)> = Vec::new();
        stack.push((root, false));

        while let Some((u, visited)) = stack.pop() {
            if !visited {
                // entering node
                trie.insert(u as i32);
                for &(idx, val) in &query_map[u] {
                    ans[idx] = trie.max_xor(val);
                }
                stack.push((u, true)); // exit marker
                for &v in children[u].iter().rev() {
                    stack.push((v, false));
                }
            } else {
                // exiting node
                trie.remove(u as i32);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-genetic-difference parents queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length parents))
         ;; adjacency list
         (children (make-vector n '()))
         (root -1))
    (for ([i (in-range n)])
      (define p (list-ref parents i))
      (if (= p -1)
          (set! root i)
          (vector-set! children p (cons i (vector-ref children p)))))
    ;; queries grouped by node
    (define m (length queries))
    (define qby (make-vector n '()))
    (for ([idx (in-range m)])
      (define pair (list-ref queries idx))
      (define node (first pair))
      (define val  (second pair))
      (vector-set! qby node (cons (list idx val) (vector-ref qby node))))
    ;; max bit needed
    (define max-val
      (max (sub1 n)
           (if (null? queries) 0 (apply max (map second queries)))))
    (define max-bit (integer-length max-val))
    ;; trie node definition
    (struct tnode ([child #:mutable] [cnt #:mutable]))
    (define (make-node)
      (tnode (vector #f #f) 0))
    (define trie-root (make-node))
    ;; trie operations
    (define (trie-insert root val)
      (let loop ((node root) (bit (- max-bit 1)))
        (set-tnode-cnt! node (+ (tnode-cnt node) 1))
        (when (>= bit 0)
          (define b (if (zero? (bitwise-and (arithmetic-shift val (- bit)) 1)) 0 1))
          (define child (vector-ref (tnode-child node) b))
          (if child
              (loop child bit-1)
              (let ((new (make-node)))
                (vector-set! (tnode-child node) b new)
                (loop new bit-1))))))
    (define (trie-remove root val)
      (let loop ((node root) (bit (- max-bit 1)))
        (set-tnode-cnt! node (- (tnode-cnt node) 1))
        (when (>= bit 0)
          (define b (if (zero? (bitwise-and (arithmetic-shift val (- bit)) 1)) 0 1))
          (let ((child (vector-ref (tnode-child node) b)))
            (loop child bit-1)))))
    (define (trie-max-xor root val)
      (let loop ((node root) (bit (- max-bit 1)) (acc 0))
        (if (< bit 0)
            acc
            (let* ((b (if (zero? (bitwise-and (arithmetic-shift val (- bit)) 1)) 0 1))
                   (desired (if (= b 0) 1 0))
                   (next (vector-ref (tnode-child node) desired)))
              (if (and next (> (tnode-cnt next) 0))
                  (loop next (- bit 1) (bitwise-ior acc (arithmetic-shift 1 bit)))
                  (let ((alt (vector-ref (tnode-child node) b)))
                    (if alt
                        (loop alt (- bit 1) acc)
                        acc)))))))
    ;; answer container
    (define ans (make-vector m 0))
    ;; iterative DFS stack: list of (node exiting?)
    (define stack (list (list root #f)))
    (let recur ()
      (when (not (null? stack))
        (define cur (car stack))
        (set! stack (cdr stack))
        (define node (first cur))
        (define exiting? (second cur))
        (if exiting?
            (trie-remove trie-root node)
            (begin
              (trie-insert trie-root node)
              ;; answer queries at this node
              (for ([q (in-list (vector-ref qby node))])
                (define idx (first q))
                (define val (second q))
                (vector-set! ans idx (trie-max-xor trie-root val)))
              ;; push exit marker then children
              (set! stack (cons (list node #t) stack))
              (for ([child (in-list (vector-ref children node))])
                (set! stack (cons (list child #f) stack)))))
        (recur))))
    ;; collect results
    (let ((res '()))
      (for ([i (in-range m)])
        (set! res (cons (vector-ref ans i) res)))
      (reverse res))))
```

## Erlang

```erlang
-spec max_genetic_difference(Parents :: [integer()], Queries :: [[integer()]]) -> [integer()].
max_genetic_difference(Parents, Queries) ->
    {Adj, Root} = build_adj(Parents, 0, #{}, undefined),
    QMap = build_qmap(Queries, 0, #{}),
    EmptyTrie = {nil, nil},
    AnswersMap = process_stack([{Root, EmptyTrie}], Adj, QMap, #{}),
    QLen = length(Queries),
    [maps:get(I, AnswersMap) || I <- lists:seq(0, QLen - 1)].

%% Build adjacency list and find root
build_adj([], _Idx, Adj, Root) -> {Adj, Root};
build_adj([P|Rest], Idx, Adj, Root) ->
    case P of
        -1 ->
            build_adj(Rest, Idx + 1, Adj, Idx);
        Parent ->
            NewAdj = maps:update_with(Parent,
                fun(L) -> [Idx | L] end,
                [Idx],
                Adj),
            build_adj(Rest, Idx + 1, NewAdj, Root)
    end.

%% Group queries by node
build_qmap([], _Idx, QMap) -> QMap;
build_qmap([[Node, Val]|Rest], Idx, QMap) ->
    NewQMap = maps:update_with(Node,
        fun(L) -> [{Val, Idx} | L] end,
        [{Val, Idx}],
        QMap),
    build_qmap(Rest, Idx + 1, NewQMap).

-define(MAX_BIT, 19).

%% Insert a number into the binary trie
insert(Node, Num) -> insert(Node, Num, ?MAX_BIT).
insert({C0, C1} = _Node, _Num, Bit) when Bit < 0 -> {C0, C1};
insert({C0, C1}, Num, Bit) ->
    BitVal = (Num bsr Bit) band 1,
    if BitVal == 0 ->
            NewC0 = insert(if C0 == nil -> {nil, nil}; true -> C0 end, Num, Bit - 1),
            {NewC0, C1};
       true ->
            NewC1 = insert(if C1 == nil -> {nil, nil}; true -> C1 end, Num, Bit - 1),
            {C0, NewC1}
    end.

%% Query maximum xor with Val in the trie
max_xor(Node, Val) -> max_xor(Node, Val, ?MAX_BIT).
max_xor(nil, _Val, _Bit) -> 0;
max_xor({C0, C1}, _Val, Bit) when Bit < 0 -> 0;
max_xor({C0, C1} = _Node, Val, Bit) ->
    Desired = 1 - ((Val bsr Bit) band 1),
    case Desired of
        0 ->
            case C0 of
                nil ->
                    case C1 of
                        nil -> 0;
                        _   -> (1 bsl Bit) bor max_xor(C1, Val, Bit - 1)
                    end;
                _ ->
                    (1 bsl Bit) bor max_xor(C0, Val, Bit - 1)
            end;
        1 ->
            case C1 of
                nil ->
                    case C0 of
                        nil -> 0;
                        _   -> max_xor(C0, Val, Bit - 1)
                    end;
                _ ->
                    (1 bsl Bit) bor max_xor(C1, Val, Bit - 1)
            end
    end.

%% Iterative DFS using explicit stack
process_stack([], _Adj, _QMap, Answers) -> Answers;
process_stack([{Node, Trie0} | Rest], Adj, QMap, Answers) ->
    Trie = insert(Trie0, Node),
    Qs = maps:get(Node, QMap, []),
    NewAnswers = lists:foldl(fun({Val, Idx}, Acc) ->
        Answer = max_xor(Trie, Val),
        maps:put(Idx, Answer, Acc)
    end, Answers, Qs),
    Children = maps:get(Node, Adj, []),
    NewStack = [{Child, Trie} || Child <- Children] ++ Rest,
    process_stack(NewStack, Adj, QMap, NewAnswers).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @max_bit 19

  @spec max_genetic_difference(parents :: [integer], queries :: [[integer]]) :: [integer]
  def max_genetic_difference(parents, queries) do
    n = length(parents)

    # Build children adjacency map
    children =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        p = Enum.at(parents, i)
        if p != -1 do
          Map.update(acc, p, [i], &[i | &1])
        else
          acc
        end
      end)

    # Group queries by node with their original index
    query_map =
      Enum.with_index(queries)
      |> Enum.reduce(%{}, fn {{node, val}, idx}, acc ->
        Map.update(acc, node, [{idx, val}], &[{idx, val} | &1])
      end)

    # Find root
    root = Enum.find_index(parents, fn p -> p == -1 end)

    # Initialize mutable trie using ETS
    tid = :ets.new(:trie, [:set, :private])
    :ets.insert(tid, {0, nil, nil, 0})
    :erlang.put(:next_idx, 1)

    ans_map = dfs(root, children, query_map, tid, %{})
    # Build answer list in order
    Enum.map(0..(length(queries) - 1), fn i -> Map.fetch!(ans_map, i) end)
  end

  defp dfs(node, children, qmap, tid, ans) do
    trie_insert(tid, node)

    ans =
      case Map.get(qmap, node) do
        nil ->
          ans

        list ->
          Enum.reduce(list, ans, fn {idx, val}, a ->
            maxxor = trie_max_xor(tid, val)
            Map.put(a, idx, maxxor)
          end)
      end

    ans =
      Enum.reduce(Map.get(children, node, []), ans, fn child, a ->
        dfs(child, children, qmap, tid, a)
      end)

    trie_delete(tid, node)
    ans
  end

  # Trie operations ---------------------------------------------------------

  defp update_cnt(tid, idx, delta) do
    [{^idx, c0, c1, cnt}] = :ets.lookup(tid, idx)
    :ets.update_element(tid, idx, {4, cnt + delta})
  end

  defp trie_insert(tid, val) do
    insert_path(tid, val, 0, @max_bit, true)
  end

  defp trie_delete(tid, val) do
    insert_path(tid, val, 0, @max_bit, false)
  end

  # shared logic for insert (+1) and delete (-1)
  defp insert_path(_tid, _val, _idx, -1, _inc), do: :ok

  defp insert_path(tid, val, idx, bit, inc) do
    delta = if inc, do: 1, else: -1
    update_cnt(tid, idx, delta)

    if bit < 0 do
      :ok
    else
      cur_bit = (val >>> bit) &&& 1

      [{^idx, c0, c1, _cnt}] = :ets.lookup(tid, idx)
      child =
        case cur_bit do
          0 -> c0
          1 -> c1
        end

      child_idx =
        if child == nil do
          new_idx = :erlang.get(:next_idx)
          :erlang.put(:next_idx, new_idx + 1)
          :ets.insert(tid, {new_idx, nil, nil, 0})

          case cur_bit do
            0 -> :ets.update_element(tid, idx, {2, new_idx})
            1 -> :ets.update_element(tid, idx, {3, new_idx})
          end

          new_idx
        else
          child
        end

      insert_path(tid, val, child_idx, bit - 1, inc)
    end
  end

  defp trie_max_xor(tid, val) do
    do_max_xor(tid, val, @max_bit, 0, 0)
  end

  defp do_max_xor(_tid, _val, -1, _idx, acc), do: acc

  defp do_max_xor(tid, val, bit, idx, acc) do
    cur_bit = (val >>> bit) &&& 1
    desired = 1 - cur_bit

    [{^idx, c0, c1, _cnt}] = :ets.lookup(tid, idx)

    {desired_child, other_child} =
      if desired == 0 do
        {c0, c1}
      else
        {c1, c0}
      end

    {next_idx, new_acc} =
      case desired_child do
        nil ->
          {other_child, acc}

        child_idx ->
          [{^child_idx, _c0, _c1, cnt}] = :ets.lookup(tid, child_idx)

          if cnt > 0 do
            {child_idx, acc ||| (1 <<< bit)}
          else
            {other_child, acc}
          end
      end

    do_max_xor(tid, val, bit - 1, next_idx, new_acc)
  end
end
```
