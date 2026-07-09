# 2973. Find Number of Coins to Place in Tree Nodes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Info {
        vector<int> large; // up to 3 largest (desc)
        vector<int> small; // up to 3 smallest (asc)
    };
    
    vector<long long> placedCoins(vector<vector<int>>& edges, vector<int>& cost) {
        int n = cost.size();
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<long long> ans(n, 0);
        
        function<Info(int,int)> dfs = [&](int u, int p) -> Info {
            vector<int> vals;
            vals.push_back(cost[u]);
            for (int v : adj[u]) if (v != p) {
                Info child = dfs(v, u);
                vals.insert(vals.end(), child.large.begin(), child.large.end());
                vals.insert(vals.end(), child.small.begin(), child.small.end());
            }
            int sz = vals.size();
            
            // largest three
            vector<int> desc = vals;
            sort(desc.begin(), desc.end(), greater<int>());
            Info res;
            for (int i = 0; i < min(3, (int)desc.size()); ++i)
                res.large.push_back(desc[i]);
            
            // smallest three
            sort(vals.begin(), vals.end());
            for (int i = 0; i < min(3, (int)vals.size()); ++i)
                res.small.push_back(vals[i]);
            
            long long coin;
            if (sz < 3) {
                coin = 1;
            } else {
                long long a = 1LL * res.large[0] * res.large[1] * res.large[2];
                long long b = 1LL * res.small[0] * res.small[1] * res.large[0];
                long long best = max(a, b);
                coin = (best < 0) ? 0 : best;
            }
            ans[u] = coin;
            return res;
        };
        
        dfs(0, -1);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private List<Integer>[] graph;
    private int[] cost;
    private long[] answer;

    public long[] placedCoins(int[][] edges, int[] cost) {
        int n = cost.length;
        this.cost = cost;
        answer = new long[n];
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        dfs(0, -1);
        return answer;
    }

    private List<Long> dfs(int node, int parent) {
        List<Long> vals = new ArrayList<>();
        vals.add((long) cost[node]);

        for (int nb : graph[node]) {
            if (nb == parent) continue;
            List<Long> childVals = dfs(nb, node);
            vals.addAll(childVals);
        }

        Collections.sort(vals);
        int m = vals.size();

        long coin;
        if (m < 3) {
            coin = 1L;
        } else {
            long smallest1 = vals.get(0);
            long smallest2 = vals.get(1);
            long largest1 = vals.get(m - 1);
            long prodNeg = smallest1 * smallest2 * largest1;

            long largest2 = vals.get(m - 2);
            long largest3 = vals.get(m - 3);
            long prodPos = largest1 * largest2 * largest3;

            coin = Math.max(prodNeg, prodPos);
            if (coin < 0) coin = 0;
        }
        answer[node] = coin;

        List<Long> ret = new ArrayList<>();
        for (int i = 0; i < Math.min(3, m); i++) ret.add(vals.get(i));
        for (int i = Math.max(m - 3, 0); i < m; i++) ret.add(vals.get(i));
        return ret;
    }
}
```

## Python

```python
import sys

class Solution(object):
    def placedCoins(self, edges, cost):
        """
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: List[int]
        """
        sys.setrecursionlimit(1000000)
        n = len(cost)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        coin = [0] * n

        def merge(ext1, ext2):
            combined = ext1 + ext2
            combined.sort()
            # keep up to three smallest and three largest
            return combined[:3] + combined[-3:]

        def dfs(u, parent):
            # extremes list for this subtree
            ext = [cost[u]]
            size = 1
            for v in adj[u]:
                if v == parent:
                    continue
                child_ext, child_sz = dfs(v, u)
                size += child_sz
                ext = merge(ext, child_ext)

            if size < 3:
                coin[u] = 1
            else:
                s = sorted(ext)  # at most 6 elements
                a, b, c = s[-1], s[-2], s[-3]
                prod1 = a * b * c
                d, e = s[0], s[1]
                prod2 = d * e * a
                best = max(prod1, prod2)
                coin[u] = best if best > 0 else 0
            return ext, size

        dfs(0, -1)
        return coin
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(1 << 25)

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        ans = [0] * n

        def dfs(u: int, p: int):
            # candidates to determine top3 and bot3
            cand = [cost[u]]
            for v in adj[u]:
                if v == p:
                    continue
                top_child, bot_child = dfs(v, u)
                cand.extend(top_child)
                cand.extend(bot_child)

            sz = len(cand)
            if sz < 3:
                ans[u] = 1
                # return all values (up to 3) for parent merging
                cand.sort()
                top3 = cand[-sz:]  # whole list
                bot3 = cand[:sz]
                return top3, bot3

            cand.sort()
            # three largest product
            prod1 = cand[-1] * cand[-2] * cand[-3]
            # two smallest (most negative) times largest
            prod2 = cand[0] * cand[1] * cand[-1]
            best = max(prod1, prod2)
            ans[u] = best if best > 0 else 0

            top3 = cand[-3:]
            bot3 = cand[:3]
            return top3, bot3

        dfs(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long top[3];   // largest values
    long long bot[3];   // smallest values
    int cnt;            // number of elements in subtree
} NodeInfo;

static void addValue(NodeInfo *info, long long val) {
    info->cnt++;

    // update top three largest
    if (val > info->top[0]) {
        info->top[2] = info->top[1];
        info->top[1] = info->top[0];
        info->top[0] = val;
    } else if (val > info->top[1]) {
        info->top[2] = info->top[1];
        info->top[1] = val;
    } else if (val > info->top[2]) {
        info->top[2] = val;
    }

    // update bottom three smallest
    if (val < info->bot[0]) {
        info->bot[2] = info->bot[1];
        info->bot[1] = info->bot[0];
        info->bot[0] = val;
    } else if (val < info->bot[1]) {
        info->bot[2] = info->bot[1];
        info->bot[1] = val;
    } else if (val < info->bot[2]) {
        info->bot[2] = val;
    }
}

static void dfs(int u, int parent,
                int **adj, int *deg,
                int *cost,
                NodeInfo *infos,
                long long *ans) {
    NodeInfo cur;
    cur.cnt = 0;
    cur.top[0] = cur.top[1] = cur.top[2] = LLONG_MIN;
    cur.bot[0] = cur.bot[1] = cur.bot[2] = LLONG_MAX;

    addValue(&cur, (long long)cost[u]);

    for (int i = 0; i < deg[u]; ++i) {
        int v = adj[u][i];
        if (v == parent) continue;
        dfs(v, u, adj, deg, cost, infos, ans);
        NodeInfo *ch = &infos[v];
        for (int k = 0; k < 3; ++k) {
            if (ch->top[k] != LLONG_MIN)
                addValue(&cur, ch->top[k]);
        }
        for (int k = 0; k < 3; ++k) {
            if (ch->bot[k] != LLONG_MAX)
                addValue(&cur, ch->bot[k]);
        }
    }

    infos[u] = cur;

    long long res;
    if (cur.cnt < 3) {
        res = 1LL;
    } else {
        long long prod1 = cur.bot[0] * cur.bot[1] * cur.top[0];
        long long prod2 = cur.top[0] * cur.top[1] * cur.top[2];
        long long best = (prod1 > prod2) ? prod1 : prod2;
        res = (best < 0) ? 0LL : best;
    }
    ans[u] = res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* placedCoins(int** edges, int edgesSize, int* edgesColSize,
                       int* cost, int costSize, int* returnSize) {
    int n = costSize;
    *returnSize = n;

    /* compute degrees */
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        deg[a]++; deg[b]++;
    }

    /* allocate adjacency lists */
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    int *idx = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][idx[a]++] = b;
        adj[b][idx[b]++] = a;
    }
    free(idx);

    NodeInfo *infos = (NodeInfo*)malloc(n * sizeof(NodeInfo));
    long long *ans = (long long*)malloc(n * sizeof(long long));

    dfs(0, -1, adj, deg, cost, infos, ans);

    /* clean up */
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(infos);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private List<int>[] graph;
    private int[] costs;
    private long[] answer;

    public long[] PlacedCoins(int[][] edges, int[] cost) {
        int n = cost.Length;
        graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }
        costs = cost;
        answer = new long[n];
        Dfs(0, -1);
        return answer;
    }

    private NodeInfo Dfs(int node, int parent) {
        List<long> candidates = new List<long>();
        candidates.Add(costs[node]);

        foreach (int nb in graph[node]) {
            if (nb == parent) continue;
            NodeInfo child = Dfs(nb, node);
            candidates.AddRange(child.MaxVals);
            candidates.AddRange(child.MinVals);
        }

        candidates.Sort();
        int m = candidates.Count;

        List<long> maxVals = new List<long>();
        List<long> minVals = new List<long>();

        for (int i = 0; i < Math.Min(3, m); i++) minVals.Add(candidates[i]);
        for (int i = m - 1; i >= Math.Max(m - 3, 0); i--) maxVals.Add(candidates[i]);

        long coin;
        if (m < 3) {
            coin = 1;
        } else {
            long a = candidates[0] * candidates[1] * candidates[m - 1];
            long b = candidates[m - 1] * candidates[m - 2] * candidates[m - 3];
            long best = Math.Max(a, b);
            coin = best < 0 ? 0 : best;
        }
        answer[node] = coin;

        return new NodeInfo { MaxVals = maxVals, MinVals = minVals };
    }

    private class NodeInfo {
        public List<long> MaxVals;
        public List<long> MinVals;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} cost
 * @return {number[]}
 */
var placedCoins = function(edges, cost) {
    const n = cost.length;
    const graph = Array.from({length: n}, () => []);
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const result = new Array(n).fill(0);

    function dfs(u, parent) {
        let size = 1;
        // collect candidates: own cost + extremes from children
        const vals = [cost[u]];
        for (const v of graph[u]) {
            if (v === parent) continue;
            const childInfo = dfs(v, u);
            size += childInfo.size;
            // merge child's extreme values
            vals.push(...childInfo.small);
            vals.push(...childInfo.large);
        }
        // sort to obtain new extremes
        vals.sort((a, b) => a - b);
        const m = vals.length;
        const small = vals.slice(0, Math.min(3, m));               // up to 3 smallest
        const large = vals.slice(Math.max(0, m - 3));              // up to 3 largest

        let coin;
        if (size < 3) {
            coin = 1;
        } else {
            // product of two smallest and the largest
            const prodA = small[0] * small[1] * large[large.length - 1];
            // product of three largest
            const prodB = large[0] * large[1] * large[2];
            const best = Math.max(prodA, prodB);
            coin = best > 0 ? best : 0;
        }
        result[u] = coin;
        return {size, small, large};
    }

    dfs(0, -1);
    return result;
};
```

## Typescript

```typescript
function placedCoins(edges: number[][], cost: number[]): number[] {
    const n = cost.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = 0;
    while (stack.length) {
        const node = stack.pop()!;
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }

    const tops: number[][] = Array.from({ length: n }, () => []);
    const bots: number[][] = Array.from({ length: n }, () => []);
    const ans = new Array<number>(n).fill(0);

    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        const candidates: number[] = [cost[node]];
        for (const nb of adj[node]) {
            if (parent[nb] === node) { // child
                candidates.push(...tops[nb]);
                candidates.push(...bots[nb]);
            }
        }

        const len = candidates.length;
        if (len < 3) {
            ans[node] = 1;
        } else {
            const desc = [...candidates].sort((a, b) => b - a);
            const asc = [...candidates].sort((a, b) => a - b);
            let maxProd = desc[0] * desc[1] * desc[2];
            const prod2 = asc[0] * asc[1] * desc[0];
            if (prod2 > maxProd) maxProd = prod2;
            ans[node] = maxProd < 0 ? 0 : maxProd;
        }

        // store up to three largest and three smallest for parent merges
        const sortedDesc = [...candidates].sort((a, b) => b - a);
        tops[node] = sortedDesc.slice(0, 3);
        const sortedAsc = [...candidates].sort((a, b) => a - b);
        bots[node] = sortedAsc.slice(0, 3);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[] $cost
     * @return Integer[]
     */
    function placedCoins($edges, $cost) {
        $n = count($cost);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$a, $b] = $e;
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        $result = array_fill(0, $n, 1);

        // helper to keep top 3 largest (desc) or bottom 3 smallest (asc)
        $addVal = function(&$arr, $val, $desc) {
            $arr[] = $val;
            if ($desc) {
                rsort($arr);
            } else {
                sort($arr);
            }
            if (count($arr) > 3) {
                array_pop($arr); // remove extra element
            }
        };

        $dfs = function($u, $parent) use (&$dfs, &$adj, &$cost, &$result, &$addVal) {
            $maxVals = []; // top 3 largest
            $minVals = []; // bottom 3 smallest
            $size = 1;

            // add own cost
            $addVal($maxVals, $cost[$u], true);
            $addVal($minVals, $cost[$u], false);

            foreach ($adj[$u] as $v) {
                if ($v === $parent) continue;
                $childInfo = $dfs($v, $u);
                $size += $childInfo['size'];
                foreach ($childInfo['max'] as $val) {
                    $addVal($maxVals, $val, true);
                }
                foreach ($childInfo['min'] as $val) {
                    $addVal($minVals, $val, false);
                }
            }

            if ($size < 3) {
                $coin = 1;
            } else {
                // ensure we have at least three values in maxVals
                // candidate using three largest
                $cand1 = $maxVals[0] * $maxVals[1] * $maxVals[2];
                // candidate using two smallest and the largest
                $cand2 = $minVals[0] * $minVals[1] * $maxVals[0];
                $best = max($cand1, $cand2);
                $coin = ($best < 0) ? 0 : $best;
            }

            $result[$u] = $coin;

            return ['size' => $size, 'max' => $maxVals, 'min' => $minVals];
        };

        $dfs(0, -1);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func placedCoins(_ edges: [[Int]], _ cost: [Int]) -> [Int] {
        let n = cost.count
        var graph = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        var answer = [Int](repeating: 1, count: n)

        func dfs(_ node: Int, _ parent: Int) -> ([Int], [Int], Int) {
            var large = [cost[node]]
            var small = [cost[node]]
            var size = 1

            for nb in graph[node] where nb != parent {
                let (childLarge, childSmall, childSize) = dfs(nb, node)
                size += childSize

                // merge largest three
                var tempLarge = large + childLarge
                tempLarge.sort(by: >)
                if tempLarge.count > 3 { tempLarge.removeSubrange(3..) }
                large = tempLarge

                // merge smallest three
                var tempSmall = small + childSmall
                tempSmall.sort()
                if tempSmall.count > 3 { tempSmall.removeSubrange(3..) }
                small = tempSmall
            }

            if size < 3 {
                answer[node] = 1
            } else {
                var best = Int.min

                if large.count >= 3 {
                    let val = large[0] * large[1] * large[2]
                    best = max(best, val)
                }
                if small.count >= 2 && large.count >= 1 {
                    let val = small[0] * small[1] * large[0]
                    best = max(best, val)
                }

                answer[node] = best < 0 ? 0 : best
            }

            return (large, small, size)
        }

        _ = dfs(0, -1)
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.*
 
class Solution {
    private lateinit var cost: IntArray
    private lateinit var adj: Array<MutableList<Int>>
    private lateinit var ans: LongArray
 
    private data class NodeInfo(
        val cnt: Int,
        val maxVals: IntArray, // up to 3 largest values (ascending)
        val minVals: IntArray  // up to 3 smallest values (ascending)
    )
 
    fun placedCoins(edges: Array<IntArray>, cost: IntArray): LongArray {
        val n = cost.size
        this.cost = cost
        adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }
        ans = LongArray(n)
        dfs(0, -1)
        return ans
    }
 
    private fun dfs(u: Int, parent: Int): NodeInfo {
        var cnt = 1
        val maxList = mutableListOf<Int>()
        val minList = mutableListOf<Int>()
 
        fun addValue(v: Int) {
            // maintain top three largest in ascending order
            if (maxList.size < 3) {
                maxList.add(v)
                maxList.sort()
            } else if (v > maxList[0]) {
                maxList[0] = v
                maxList.sort()
            }
            // maintain bottom three smallest in ascending order
            if (minList.size < 3) {
                minList.add(v)
                minList.sort()
            } else if (v < minList[minList.size - 1]) {
                minList[minList.size - 1] = v
                minList.sort()
            }
        }
 
        addValue(cost[u])
 
        for (v in adj[u]) {
            if (v == parent) continue
            val childInfo = dfs(v, u)
            cnt += childInfo.cnt
            for (x in childInfo.maxVals) addValue(x)
            for (x in childInfo.minVals) addValue(x)
        }
 
        // compute answer for node u
        if (cnt < 3) {
            ans[u] = 1L
        } else {
            val extreme = mutableListOf<Int>()
            extreme.addAll(maxList)
            extreme.addAll(minList)
            extreme.sort()
            val nE = extreme.size
            var best = Long.MIN_VALUE
            // three largest
            if (nE >= 3) {
                val p1 = extreme[nE - 1].toLong() * extreme[nE - 2] * extreme[nE - 3]
                best = maxOf(best, p1)
            }
            // two smallest and the largest
            if (nE >= 3) {
                val p2 = extreme[0].toLong() * extreme[1] * extreme[nE - 1]
                best = maxOf(best, p2)
            }
            ans[u] = if (best < 0) 0L else best
        }
 
        return NodeInfo(cnt, maxList.toIntArray(), minList.toIntArray())
    }
}
```

## Dart

```dart
class Solution {
  List<int> placedCoins(List<List<int>> edges, List<int> cost) {
    int n = cost.length;
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    List<int> answer = List.filled(n, 0);

    NodeInfo dfs(int u, int parent) {
      int cnt = 1;
      List<int> maxVals = [cost[u]];
      List<int> minVals = [cost[u]];

      for (int v in graph[u]) {
        if (v == parent) continue;
        NodeInfo child = dfs(v, u);
        cnt += child.cnt;

        // merge max values
        List<int> tmpMax = []..addAll(maxVals)..addAll(child.maxVals);
        tmpMax.sort((a, b) => b.compareTo(a)); // descending
        if (tmpMax.length > 3) tmpMax = tmpMax.sublist(0, 3);
        maxVals = tmpMax;

        // merge min values
        List<int> tmpMin = []..addAll(minVals)..addAll(child.minVals);
        tmpMin.sort(); // ascending
        if (tmpMin.length > 3) tmpMin = tmpMin.sublist(0, 3);
        minVals = tmpMin;
      }

      int coin;
      if (cnt < 3) {
        coin = 1;
      } else {
        int best = -9223372036854775808; // very small number
        if (maxVals.length >= 3) {
          int prod = maxVals[0] * maxVals[1] * maxVals[2];
          if (prod > best) best = prod;
        }
        if (maxVals.isNotEmpty && minVals.length >= 2) {
          int prod = maxVals[0] * minVals[0] * minVals[1];
          if (prod > best) best = prod;
        }
        if (minVals.length >= 3) {
          int prod = minVals[0] * minVals[1] * minVals[2];
          if (prod > best) best = prod;
        }
        coin = best < 0 ? 0 : best;
      }

      answer[u] = coin;
      return NodeInfo(cnt, maxVals, minVals);
    }

    dfs(0, -1);
    return answer;
  }
}

class NodeInfo {
  int cnt;
  List<int> maxVals;
  List<int> minVals;
  NodeInfo(this.cnt, this.maxVals, this.minVals);
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

type info struct {
	maxVals []int // descending, up to 3 largest values
	minVals []int // ascending, up to 3 smallest values (most negative)
	size    int
}

func insertMax(vals []int, x int) []int {
	vals = append(vals, x)
	sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
	if len(vals) > 3 {
		vals = vals[:3]
	}
	return vals
}

func insertMin(vals []int, x int) []int {
	vals = append(vals, x)
	sort.Slice(vals, func(i, j int) bool { return vals[i] < vals[j] })
	if len(vals) > 3 {
		vals = vals[:3]
	}
	return vals
}

func dfs(u, parent int, g [][]int, cost []int, ans []int64) info {
	cur := info{
		maxVals: make([]int, 0, 3),
		minVals: make([]int, 0, 3),
		size:    1,
	}
	cur.maxVals = insertMax(cur.maxVals, cost[u])
	cur.minVals = insertMin(cur.minVals, cost[u])

	for _, v := range g[u] {
		if v == parent {
			continue
		}
		child := dfs(v, u, g, cost, ans)
		for _, val := range child.maxVals {
			cur.maxVals = insertMax(cur.maxVals, val)
		}
		for _, val := range child.minVals {
			cur.minVals = insertMin(cur.minVals, val)
		}
		cur.size += child.size
	}

	var coin int64
	if cur.size < 3 {
		coin = 1
	} else {
		best := int64(math.MinInt64)
		if len(cur.maxVals) >= 3 {
			prod := int64(cur.maxVals[0]) * int64(cur.maxVals[1]) * int64(cur.maxVals[2])
			if prod > best {
				best = prod
			}
		}
		if len(cur.maxVals) >= 1 && len(cur.minVals) >= 2 {
			prod := int64(cur.maxVals[0]) * int64(cur.minVals[0]) * int64(cur.minVals[1])
			if prod > best {
				best = prod
			}
		}
		if best < 0 {
			coin = 0
		} else {
			coin = best
		}
	}
	ans[u] = coin
	return cur
}

func placedCoins(edges [][]int, cost []int) []int64 {
	n := len(cost)
	graph := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	ans := make([]int64, n)
	dfs(0, -1, graph, cost, ans)
	return ans
}
```

## Ruby

```ruby
def placed_coins(edges, cost)
  n = cost.size
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  while (u = stack.pop)
    order << u
    adj[u].each do |v|
      next if v == parent[u]
      parent[v] = u
      stack << v
    end
  end

  max_vals = Array.new(n) { [] }
  min_vals = Array.new(n) { [] }
  coin = Array.new(n, 0)

  order.reverse_each do |u|
    vals = [cost[u]]
    adj[u].each do |v|
      next unless parent[v] == u
      vals.concat(max_vals[v])
      vals.concat(min_vals[v])
    end

    if vals.size < 3
      coin[u] = 1
    else
      desc = vals.sort.reverse
      asc = vals.sort
      max3 = desc[0, 3]
      min3 = asc[0, 3]

      candidates = []
      candidates << max3[0] * max3[1] * max3[2] if max3.size == 3
      candidates << max3[0] * min3[0] * min3[1] if max3.size >= 1 && min3.size >= 2

      best = candidates.max
      coin[u] = best > 0 ? best : 0
    end

    desc = vals.sort.reverse
    asc = vals.sort
    max_vals[u] = desc[0, 3]
    min_vals[u] = asc[0, 3]
  end

  coin
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.ArrayBuffer

    def placedCoins(edges: Array[Array[Int]], cost: Array[Int]): Array[Long] = {
        val n = cost.length
        val adj = Array.fill(n)(new ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }
        val ans = new Array[Long](n)

        def dfs(u: Int, parent: Int): ArrayBuffer[Int] = {
            // collect values from this node and its children (up to 6 per child)
            val vals = new ArrayBuffer[Int]()
            vals.append(cost(u))
            for (v <- adj(u) if v != parent) {
                val childVals = dfs(v, u)
                vals ++= childVals
            }
            // sort ascending
            val sorted = vals.sorted

            // compute answer for node u
            if (sorted.length < 3) {
                ans(u) = 1L
            } else {
                val a0 = sorted(0).toLong
                val a1 = sorted(1).toLong
                val an1 = sorted(sorted.length - 1).toLong
                val an2 = sorted(sorted.length - 2).toLong
                val an3 = sorted(sorted.length - 3).toLong

                val cand1 = a0 * a1 * an1          // two smallest * largest
                val cand2 = an1 * an2 * an3        // three largest
                var best = math.max(cand1, cand2)
                if (best < 0) best = 0
                ans(u) = best
            }

            // keep only up to three smallest and three largest for parent propagation
            val kept = new ArrayBuffer[Int]()
            val takeSmall = math.min(3, sorted.length)
            for (i <- 0 until takeSmall) kept.append(sorted(i))
            val startLarge = math.max(0, sorted.length - 3)
            for (i <- startLarge until sorted.length) kept.append(sorted(i))
            kept.sorted
        }

        dfs(0, -1)
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn placed_coins(edges: Vec<Vec<i32>>, cost: Vec<i32>) -> Vec<i64> {
        let n = cost.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut ans = vec![0i64; n];

        fn dfs(
            u: usize,
            parent: usize,
            adj: &Vec<Vec<usize>>,
            cost: &Vec<i32>,
            ans: &mut Vec<i64>,
        ) -> (Vec<i32>, Vec<i32>, usize) {
            // start with the node's own value
            let mut largest = vec![cost[u]];
            let mut smallest = vec![cost[u]];
            let mut size = 1usize;

            for &v in &adj[u] {
                if v == parent {
                    continue;
                }
                let (child_largest, child_smallest, child_size) = dfs(v, u, adj, cost, ans);
                size += child_size;

                // merge largest values
                for &val in &child_largest {
                    largest.push(val);
                }
                largest.sort_by(|a, b| b.cmp(a)); // descending
                if largest.len() > 3 {
                    largest.truncate(3);
                }

                // merge smallest values (keep two smallest)
                for &val in &child_smallest {
                    smallest.push(val);
                }
                smallest.sort(); // ascending
                if smallest.len() > 2 {
                    smallest.truncate(2);
                }
            }

            let res = if size < 3 {
                1i64
            } else {
                let mut best = i64::MIN;
                if largest.len() >= 3 {
                    let p = largest[0] as i64 * largest[1] as i64 * largest[2] as i64;
                    if p > best {
                        best = p;
                    }
                }
                if smallest.len() >= 2 && !largest.is_empty() {
                    let p = smallest[0] as i64 * smallest[1] as i64 * largest[0] as i64;
                    if p > best {
                        best = p;
                    }
                }
                if best < 0 { 0 } else { best }
            };
            ans[u] = res;
            (largest, smallest, size)
        }

        dfs(0, n, &adj, &cost, &mut ans);
        ans
    }
}
```

## Racket

```racket
(define/contract (placed-coins edges cost)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (vector-length (list->vector cost)))
         (cost-vec (list->vector cost))
         (adj (make-vector n '()))
         (_ (for-each
              (lambda (e)
                (match e
                  [(list a b)
                   (vector-set! adj a (cons b (vector-ref adj a)))
                   (vector-set! adj b (cons a (vector-ref adj b)))]))
              edges))
         (result (make-vector n 0)))

    (define (take lst k)
      (if (or (zero? k) (null? lst))
          '()
          (cons (car lst) (take (cdr lst) (- k 1)))))

    (struct subtree (size top bot))

    (define (dfs node parent)
      (let* ((vals (list (vector-ref cost-vec node)))
             (size 1))
        (for-each
         (lambda (nbr)
           (when (not (= nbr parent))
             (let ([child (dfs nbr node)])
               (set! size (+ size (subtree-size child)))
               (set! vals (append vals (subtree-top child) (subtree-bot child))))))
         (vector-ref adj node))
        (define sorted-desc (sort vals >))
        (define top3 (take sorted-desc 3))
        (define sorted-asc (sort vals <))
        (define bot3 (take sorted-asc 3))

        (if (< size 3)
            (vector-set! result node 1)
            (let* ((candidates (append top3 bot3))
                   (len (length candidates))
                   (max-prod #f))
              (for ([i (in-range len)])
                (for ([j (in-range (+ i 1) len)])
                  (for ([k (in-range (+ j 1) len)])
                    (let* ((a (list-ref candidates i))
                           (b (list-ref candidates j))
                           (c (list-ref candidates k))
                           (prod (* a b c)))
                      (when (or (not max-prod) (> prod max-prod))
                        (set! max-prod prod))))))
              (vector-set! result node
                (if (and max-prod (>= max-prod 0)) max-prod 0)))))
        (make-subtree size top3 bot3)))

    (dfs 0 -1)
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (+ i 1) (cons (vector-ref result i) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([placed_coins/2]).

-spec placed_coins(Edges :: [[integer()]], Cost :: [integer()]) -> [integer()].
placed_coins(Edges, Cost) ->
    Adj = build_adj(Edges, #{}),
    {_, _, _, Map} = dfs(0, -1, Adj, Cost),
    N = length(Cost),
    [maps:get(I, Map) || I <- lists:seq(0, N-1)].

build_adj([], M) -> M;
build_adj([[A,B]|T], M) ->
    M1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            M),
    M2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            M1),
    build_adj(T, M2).

dfs(Node, Parent, Adj, Cost) ->
    Children = [C || C <- maps:get(Node, Adj, []), C =/= Parent],
    {Top0, Bot0, Size0, Map0} =
        lists:foldl(fun(Child, {T,B,S,M}) ->
            {CTop, CBot, CSize, CMap} = dfs(Child, Node, Adj, Cost),
            NewTop = top3(T ++ CTop),
            NewBot = bot3(B ++ CBot),
            {NewTop, NewBot, S + CSize, maps:merge(M, CMap)}
        end, {[], [], 0, #{}}, Children),

    Val = lists:nth(Node+1, Cost),
    Top1 = top3([Val|Top0]),
    Bot1 = bot3([Val|Bot0]),
    Size1 = Size0 + 1,
    Coin = compute_coin(Top1, Bot1, Size1),
    Map1 = maps:put(Node, Coin, Map0),
    {Top1, Bot1, Size1, Map1}.

top3(List) ->
    lists:sublist(lists:sort(fun(A,B) -> A > B end, List), 3).

bot3(List) ->
    lists:sublist(lists:sort(List), 3).

compute_coin(Top, Bot, Size) ->
    case Size < 3 of
        true -> 1;
        false ->
            Cand = Top ++ Bot,
            MaxProd = max_product(Cand),
            if MaxProd < 0 -> 0; true -> MaxProd end
    end.

max_product(Cands) ->
    max_product(Cands, -1000000000000).

max_product([], Max) -> Max;
max_product([H|T], Max) ->
    Max1 = max_product_pair(H, T, Max),
    max_product(T, Max1).

max_product_pair(_, [], Max) -> Max;
max_product_pair(X, [Y|Ys], Max) ->
    Max2 = max_product_triplet(X, Y, Ys, Max),
    max_product_pair(X, Ys, Max2).

max_product_triplet(_, _, [], Max) -> Max;
max_product_triplet(X, Y, [Z|Zs], Max) ->
    Prod = X * Y * Z,
    NewMax = if Prod > Max -> Prod; true -> Max end,
    max_product_triplet(X, Y, Zs, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec placed_coins(edges :: [[integer]], cost :: [integer]) :: [integer]
  def placed_coins(edges, cost) do
    n = length(cost)
    adj = build_adj(edges, %{})
    {_cand, _size, res_map} = dfs(0, -1, adj, cost)

    Enum.map(0..n - 1, fn i -> Map.get(res_map, i) end)
  end

  defp build_adj([], acc), do: acc

  defp build_adj([[a, b] | rest], acc) do
    acc = Map.update(acc, a, [b], &[b | &1])
    acc = Map.update(acc, b, [a], &[a | &1])
    build_adj(rest, acc)
  end

  # Returns {candidate values (up to 6), subtree size, result map}
  defp dfs(u, parent, adj, cost) do
    init = {[Enum.at(cost, u)], 1, %{}}

    {vals, sz, res_map} =
      Enum.reduce(Map.get(adj, u, []), init, fn v,
                                                {vals_acc, sz_acc, map_acc} ->
        if v == parent do
          {vals_acc, sz_acc, map_acc}
        else
          {child_vals, child_sz, child_map} = dfs(v, u, adj, cost)

          {
            vals_acc ++ child_vals,
            sz_acc + child_sz,
            Map.merge(map_acc, child_map)
          }
        end
      end)

    # extremes
    sorted_desc = Enum.sort(vals, &>=/2)
    largest_three = Enum.take(sorted_desc, min(3, length(sorted_desc)))

    sorted_asc = Enum.sort(vals)
    smallest_three = Enum.take(sorted_asc, min(3, length(sorted_asc)))

    result =
      if sz < 3 do
        1
      else
        prod1 =
          if length(largest_three) == 3,
            do:
              Enum.at(largest_three, 0) *
                Enum.at(largest_three, 1) *
                Enum.at(largest_three, 2),
            else: -1_000_000_000_000

        prod2 =
          if length(smallest_three) >= 2 and length(largest_three) >= 1,
            do:
              Enum.at(smallest_three, 0) *
                Enum.at(smallest_three, 1) *
                Enum.at(largest_three, 0),
            else: -1_000_000_000_000

        max_prod = max(prod1, prod2)

        if max_prod < 0, do: 0, else: max_prod
      end

    res_map = Map.put(res_map, u, result)
    {largest_three ++ smallest_three, sz, res_map}
  end
end
```
