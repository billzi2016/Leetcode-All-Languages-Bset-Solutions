# 3547. Maximum Sum of Edge Values in a Graph

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxScore(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // Determine if the graph is a path or a cycle
        bool isPath = false;
        int start = 0;
        for (int i = 0; i < n; ++i) {
            if ((int)adj[i].size() == 1) {
                isPath = true;
                start = i;
                break;
            }
        }
        // Build ordering of nodes along the path/cycle
        vector<int> order;
        order.reserve(n);
        int cur = start;
        int prev = -1;
        for (int cnt = 0; cnt < n; ++cnt) {
            order.push_back(cur);
            int nxt = -1;
            for (int nb : adj[cur]) {
                if (nb != prev) {
                    nxt = nb;
                    break;
                }
            }
            prev = cur;
            cur = nxt;
        }

        // Construct optimal permutation of values 1..n
        vector<int> perm(n);
        if (n % 2 == 1) { // odd length
            int mid = n / 2;
            perm[mid] = n;
            int curVal = n - 1;
            int l = mid - 1, r = mid + 1;
            while (l >= 0 || r < n) {
                if (l >= 0) {
                    perm[l] = curVal--;
                    --l;
                }
                if (r < n) {
                    perm[r] = curVal--;
                    ++r;
                }
            }
        } else { // even length
            int midL = n / 2 - 1, midR = n / 2;
            perm[midL] = n;
            perm[midR] = n - 1;
            int curVal = n - 2;
            int l = midL - 1, r = midR + 1;
            while (l >= 0 || r < n) {
                if (l >= 0) {
                    perm[l] = curVal--;
                    --l;
                }
                if (r < n) {
                    perm[r] = curVal--;
                    ++r;
                }
            }
        }

        // Assign values to nodes according to order
        vector<long long> val(n);
        for (int i = 0; i < n; ++i) {
            val[order[i]] = perm[i];
        }

        // Compute total score
        long long ans = 0;
        for (auto &e : edges) {
            ans += val[e[0]] * val[e[1]];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxScore(int n, int[][] edges) {
        // Build adjacency list
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        // Determine if the graph is a path or a cycle
        int endpoint = -1;
        int degreeOneCount = 0;
        for (int i = 0; i < n; i++) {
            if (adj[i].size() == 1) {
                degreeOneCount++;
                endpoint = i;
            }
        }

        java.util.ArrayList<Integer> order = new java.util.ArrayList<>(n);
        if (degreeOneCount == 2) { // path
            int prev = -1, cur = endpoint;
            while (true) {
                order.add(cur);
                int next = -1;
                for (int nb : adj[cur]) {
                    if (nb != prev) {
                        next = nb;
                        break;
                    }
                }
                if (next == -1) break; // reached other end
                prev = cur;
                cur = next;
            }
        } else { // cycle
            int start = 0;
            int prev = -1, cur = start;
            do {
                order.add(cur);
                int next = -1;
                for (int nb : adj[cur]) {
                    if (nb != prev) {
                        next = nb;
                        break;
                    }
                }
                prev = cur;
                cur = next;
            } while (cur != start);
        }

        // Build optimal value sequence using pendulum arrangement
        java.util.Deque<Integer> dq = new java.util.ArrayDeque<>();
        boolean addFront = false; // start by adding to the back
        for (int v = n; v >= 1; v--) {
            if (addFront) {
                dq.addFirst(v);
            } else {
                dq.addLast(v);
            }
            addFront = !addFront;
        }

        int[] seq = new int[n];
        int idx = 0;
        for (int val : dq) {
            seq[idx++] = val;
        }

        // Assign values to nodes according to the order
        int[] nodeVal = new int[n];
        for (int i = 0; i < n; i++) {
            nodeVal[order.get(i)] = seq[i];
        }

        // Compute total score
        long ans = 0L;
        for (int[] e : edges) {
            ans += (long) nodeVal[e[0]] * nodeVal[e[1]];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        deg = [len(x) for x in adj]

        # find traversal order of nodes
        def get_path_order(start):
            order = []
            prev = -1
            cur = start
            while True:
                order.append(cur)
                nxt = None
                for nb in adj[cur]:
                    if nb != prev:
                        nxt = nb
                        break
                if nxt is None:
                    break
                prev, cur = cur, nxt
            return order

        def get_cycle_order(start):
            order = []
            prev = -1
            cur = start
            for _ in range(n):
                order.append(cur)
                nxt = None
                for nb in adj[cur]:
                    if nb != prev:
                        nxt = nb
                        break
                prev, cur = cur, nxt
            return order

        # determine if graph is a cycle or a path
        cnt_deg1 = sum(1 for d in deg if d == 1)
        if cnt_deg1 == 0:   # cycle (n >= 2)
            start_node = 0
            seq_nodes = get_cycle_order(start_node)
        else:               # path
            start_node = deg.index(1)  # one endpoint
            seq_nodes = get_path_order(start_node)

        # generate mountain order of positions
        pos_order = []
        if n % 2 == 1:
            mid = n // 2
            pos_order.append(mid)
            l, r = mid - 1, mid + 1
        else:
            left = n // 2 - 1
            right = left + 1
            pos_order.extend([left, right])
            l, r = left - 1, right + 1

        while len(pos_order) < n:
            if l >= 0:
                pos_order.append(l)
                l -= 1
            if len(pos_order) == n:
                break
            if r < n:
                pos_order.append(r)
                r += 1

        # assign descending values according to mountain positions
        vals = [0] * n
        cur_val = n
        for p in pos_order:
            node = seq_nodes[p]
            vals[node] = cur_val
            cur_val -= 1

        # compute total score
        total = 0
        for u, v in edges:
            total += vals[u] * vals[v]
        return total
```

## Python3

```python
class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # find a degree-1 node to detect a path
        start = -1
        for i in range(n):
            if len(adj[i]) == 1:
                start = i
                break

        order = []
        if start != -1:  # path
            cur, prev = start, -1
            while True:
                order.append(cur)
                nxt = None
                for nb in adj[cur]:
                    if nb != prev:
                        nxt = nb
                        break
                if nxt is None:
                    break
                prev, cur = cur, nxt
        else:  # cycle
            start = 0
            cur, prev = start, -1
            for _ in range(n):
                order.append(cur)
                # each node has degree 2
                nb0, nb1 = adj[cur][0], adj[cur][1]
                nxt = nb0 if nb0 != prev else nb1
                prev, cur = cur, nxt

        # generate value sequence: even indices then odd indices reversed
        vals = list(range(1, n + 1))
        evens = vals[::2]          # positions 0,2,4,...
        odds_rev = vals[1::2][::-1]
        assign_vals = evens + odds_rev

        assigned = [0] * n
        for node, val in zip(order, assign_vals):
            assigned[node] = val

        total = 0
        for u, v in edges:
            total += assigned[u] * assigned[v]
        return total
```

## C

```c
#include <stdlib.h>

long long maxScore(int n, int** edges, int edgesSize, int* edgesColSize) {
    if (n <= 1) return 0LL;

    // adjacency list with at most 2 neighbors per node
    int *deg = (int*)calloc(n, sizeof(int));
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(2 * sizeof(int));
    }
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][deg[a]++] = b;
        adj[b][deg[b]++] = a;
    }

    // find start node: degree 1 if path, otherwise any node (0)
    int start = 0;
    for (int i = 0; i < n; ++i) {
        if (deg[i] == 1) { start = i; break; }
    }

    // order nodes along the unique traversal
    int *order = (int*)malloc(n * sizeof(int));
    int cur = start, prev = -1;
    for (int i = 0; i < n; ++i) {
        order[i] = cur;
        int next = -1;
        for (int k = 0; k < deg[cur]; ++k) {
            if (adj[cur][k] != prev) { next = adj[cur][k]; break; }
        }
        prev = cur;
        cur = next;
    }

    // build optimal value sequence using deque simulation
    int *dequeArr = (int*)malloc(2 * n * sizeof(int));
    int head = n, tail = n - 1; // empty deque
    for (int v = n; v >= 1; --v) {
        if ((n - v) % 2 == 0) {          // push front
            dequeArr[--head] = v;
        } else {                         // push back
            dequeArr[++tail] = v;
        }
    }
    int *seq = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        seq[i] = dequeArr[head + i];
    }

    // assign values to nodes
    int *val = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        val[order[i]] = seq[i];
    }

    // compute total score
    long long ans = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        ans += (long long)val[a] * (long long)val[b];
    }

    // free memory
    free(deg);
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(order);
    free(dequeArr);
    free(seq);
    free(val);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxScore(int n, int[][] edges) {
        // Build adjacency list and degree array
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int[] degree = new int[n];
        for (int i = 0; i < n; i++) degree[i] = adj[i].Count;

        int[] value = new int[n];

        if (edges.Length == n - 1) { // path
            Queue<int> q = new Queue<int>();
            for (int i = 0; i < n; i++) {
                if (degree[i] <= 1) q.Enqueue(i);
            }
            int cur = 1;
            while (q.Count > 0) {
                int node = q.Dequeue();
                value[node] = cur++;
                foreach (int nb in adj[node]) {
                    degree[nb]--;
                    if (degree[nb] == 1) q.Enqueue(nb);
                }
            }
        } else { // cycle
            // Obtain nodes order along the cycle
            int[] order = new int[n];
            bool[] visited = new bool[n];
            int start = 0;
            int prev = -1, curNode = start;
            for (int i = 0; i < n; i++) {
                order[i] = curNode;
                visited[curNode] = true;
                int next = -1;
                foreach (int nb in adj[curNode]) {
                    if (nb != prev) { next = nb; break; }
                }
                prev = curNode;
                curNode = next;
            }

            // Build value sequence: high parity descending, then low parity ascending
            List<int> seq = new List<int>(n);
            if ((n & 1) == 0) {
                for (int v = n; v >= 2; v -= 2) seq.Add(v);      // even descending
                for (int v = 1; v <= n - 1; v += 2) seq.Add(v);   // odd ascending
            } else {
                for (int v = n; v >= 1; v -= 2) seq.Add(v);       // odd descending
                for (int v = 2; v <= n - 1; v += 2) seq.Add(v);   // even ascending
            }

            for (int i = 0; i < n; i++) {
                value[order[i]] = seq[i];
            }
        }

        long ans = 0;
        foreach (var e in edges) {
            ans += (long)value[e[0]] * value[e[1]];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var maxScore = function(n, edges) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Determine if the graph is a cycle (all degrees == 2)
    let isCycle = true;
    for (let i = 0; i < n; i++) {
        if (adj[i].length === 1) { isCycle = false; break; }
    }

    // Get nodes in order along the path or around the cycle
    const order = [];
    if (!isCycle) {
        // Path: start from an endpoint (degree 1)
        let start = 0;
        for (let i = 0; i < n; i++) if (adj[i].length === 1) { start = i; break; }
        let prev = -1, cur = start;
        while (true) {
            order.push(cur);
            const neighbors = adj[cur];
            let next = -1;
            for (const nb of neighbors) {
                if (nb !== prev) { next = nb; break; }
            }
            if (next === -1) break;
            prev = cur;
            cur = next;
        }
    } else {
        // Cycle: start anywhere and walk until we return
        const start = 0;
        let prev = -1, cur = start;
        while (true) {
            order.push(cur);
            const neighbors = adj[cur];
            let next = -1;
            for (const nb of neighbors) {
                if (nb !== prev) { next = nb; break; }
            }
            if (next === start) break; // completed the cycle
            prev = cur;
            cur = next;
        }
    }

    const assign = new Array(n);
    if (!isCycle) {
        // Path assignment: smallest two at ends, rest decreasing
        assign[order[0]] = 1;
        assign[order[n - 1]] = 2;
        let val = n;
        for (let i = 1; i < n - 1; i++) {
            assign[order[i]] = val--;
        }
    } else {
        // Cycle assignment: interleave large and small numbers
        const desc = [];
        for (let v = n; v >= 1; v--) desc.push(v);
        const seq = [];
        for (let i = 0; i < desc.length; i += 2) seq.push(desc[i]);
        const tmp = [];
        for (let i = 1; i < desc.length; i += 2) tmp.push(desc[i]);
        tmp.reverse();
        seq.push(...tmp);
        for (let i = 0; i < n; i++) {
            assign[order[i]] = seq[i];
        }
    }

    let total = 0;
    for (const [u, v] of edges) {
        total += assign[u] * assign[v];
    }
    return total;
};
```

## Typescript

```typescript
function maxScore(n: number, edges: number[][]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Build ordered list of nodes along the path or cycle
    const order: number[] = [];
    if (n === 1) {
        order.push(0);
    } else {
        let start = -1;
        for (let i = 0; i < n; i++) {
            if (adj[i].length === 1) { // endpoint of a path
                start = i;
                break;
            }
        }
        const isCycle = start === -1; // all degrees are 2
        if (!isCycle) {
            // Path traversal
            let prev = -1;
            let cur = start;
            while (true) {
                order.push(cur);
                const nexts = adj[cur];
                let nxt = -1;
                for (const nb of nexts) {
                    if (nb !== prev) {
                        nxt = nb;
                        break;
                    }
                }
                if (nxt === -1) break;
                prev = cur;
                cur = nxt;
            }
        } else {
            // Cycle traversal
            let prev = -1;
            let cur = 0;
            for (let cnt = 0; cnt < n; cnt++) {
                order.push(cur);
                const nexts = adj[cur];
                let nxt = -1;
                for (const nb of nexts) {
                    if (nb !== prev) {
                        nxt = nb;
                        break;
                    }
                }
                prev = cur;
                cur = nxt!;
            }
        }
    }

    // Prepare descending values
    const desc: number[] = [];
    for (let v = n; v >= 1; v--) desc.push(v);

    // Assign values to positions using alternating placement
    const assignedVals: number[] = new Array(n);
    let idx = 0;
    if (n % 2 === 1) {
        const mid = Math.floor(n / 2);
        assignedVals[mid] = desc[idx++];
        let l = mid - 1, r = mid + 1;
        while (idx < n) {
            if (l >= 0) {
                assignedVals[l] = desc[idx++];
                l--;
            }
            if (idx >= n) break;
            if (r < n) {
                assignedVals[r] = desc[idx++];
                r++;
            }
        }
    } else {
        let l = n / 2 - 1, r = n / 2;
        // place first two largest
        assignedVals[l] = desc[idx++];
        assignedVals[r] = desc[idx++];
        l--; r++;
        while (idx < n) {
            if (l >= 0) {
                assignedVals[l] = desc[idx++];
                l--;
            }
            if (idx >= n) break;
            if (r < n) {
                assignedVals[r] = desc[idx++];
                r++;
            }
        }
    }

    // Map values to node ids
    const value: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const node = order[i];
        value[node] = assignedVals[i];
    }

    // Compute total score
    let total = 0;
    for (const [u, v] of edges) {
        total += value[u] * value[v];
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function maxScore($n, $edges) {
        if ($n <= 1) return 0;

        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // find a start node (an endpoint if exists)
        $start = 0;
        for ($i = 0; $i < $n; $i++) {
            if (count($adj[$i]) == 1) {
                $start = $i;
                break;
            }
        }

        // traverse the graph to obtain linear order of nodes
        $order = [];
        $visited = array_fill(0, $n, false);
        $curr = $start;
        $prev = -1;
        while (true) {
            $order[] = $curr;
            $visited[$curr] = true;
            $next = null;
            foreach ($adj[$curr] as $nei) {
                if ($nei != $prev) {
                    $next = $nei;
                    break;
                }
            }
            if ($next === null || $visited[$next]) {
                break;
            }
            $prev = $curr;
            $curr = $next;
        }

        // assign values 1..n to nodes
        $assign = array_fill(0, $n, 0);
        // internal nodes get the largest values in descending order
        $idx = $n - 1; // index of current largest value (value = $idx+1)
        for ($i = 1; $i <= $n - 2; $i++) {
            $node = $order[$i];
            $assign[$node] = $idx + 1;
            $idx--;
        }
        if ($n >= 2) {
            // remaining two smallest values are 1 and 2
            $assign[$order[0]] = 2;          // larger of the two to left end
            $assign[$order[$n - 1]] = 1;     // smaller to right end
        }

        // compute total score
        $sum = 0;
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $sum += $assign[$u] * $assign[$v];
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ n: Int, _ edges: [[Int]]) -> Int {
        if n <= 1 { return 0 }
        var degree = [Int](repeating: 0, count: n)
        for e in edges {
            degree[e[0]] += 1
            degree[e[1]] += 1
        }
        let isCycle = edges.count == n   // all degrees are 2
        
        // generate optimal ordering using deque technique
        var valuesDesc = [Int]()
        valuesDesc.reserveCapacity(n)
        for v in stride(from: n, through: 1, by: -1) {
            valuesDesc.append(v)
        }
        
        var left = [Int]()   // will be reversed later
        var right = [Int]()
        var front = true
        for val in valuesDesc {
            if front {
                left.append(val)
            } else {
                right.append(val)
            }
            front.toggle()
        }
        let order = left.reversed() + right
        
        var total: Int64 = 0
        for i in 0..<(order.count - 1) {
            total += Int64(order[i]) * Int64(order[i + 1])
        }
        if isCycle, let first = order.first, let last = order.last {
            total += Int64(first) * Int64(last)
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(n: Int, edges: Array<IntArray>): Long {
        if (n == 0) return 0L
        // build adjacency list
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        // obtain traversal order of nodes (path or cycle)
        val order = ArrayList<Int>(n)
        if (n == 1) {
            order.add(0)
        } else {
            var start = -1
            for (i in 0 until n) {
                if (adj[i].size == 1) { // endpoint of a path
                    start = i
                    break
                }
            }
            if (start == -1) start = 0 // cycle case

            val visited = BooleanArray(n)
            var cur = start
            var prev = -1
            while (!visited[cur]) {
                order.add(cur)
                visited[cur] = true
                var next = -1
                for (nb in adj[cur]) {
                    if (nb != prev) {
                        next = nb
                        break
                    }
                }
                prev = cur
                if (next == -1) break
                cur = next
            }
        }

        // build value sequence using alternating insertion of descending numbers
        val deque: ArrayDeque<Int> = ArrayDeque()
        var addToBack = true
        for (v in n downTo 1) {
            if (addToBack) {
                deque.addLast(v)
            } else {
                deque.addFirst(v)
            }
            addToBack = !addToBack
        }

        val seq = IntArray(n)
        var idx = 0
        for (value in deque) {
            seq[idx++] = value
        }

        // assign values to nodes according to traversal order
        val assigned = IntArray(n)
        for (i in 0 until n) {
            assigned[order[i]] = seq[i]
        }

        // compute total score
        var total = 0L
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            total += assigned[u].toLong() * assigned[v].toLong()
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(int n, List<List<int>> edges) {
    if (n <= 1) return 0;
    // Build degree array
    List<int> deg = List.filled(n, 0);
    for (var e in edges) {
      deg[e[0]]++;
      deg[e[1]]++;
    }
    bool isCycle = true;
    for (int d in deg) {
      if (d != 2) {
        isCycle = false;
        break;
      }
    }

    // Prepare values arrangement
    List<int> order = List.filled(n, 0);
    int idx = 0;

    if (!isCycle) {
      // Path: place numbers from center outward
      List<int> posOrder = [];
      if (n % 2 == 1) {
        int mid = n >> 1;
        posOrder.add(mid);
        int left = mid - 1, right = mid + 1;
        while (left >= 0 || right < n) {
          if (left >= 0) {
            posOrder.add(left);
            left--;
          }
          if (right < n) {
            posOrder.add(right);
            right++;
          }
        }
      } else {
        int midLeft = n ~/ 2 - 1;
        int midRight = n ~/ 2;
        posOrder.add(midLeft);
        posOrder.add(midRight);
        int left = midLeft - 1, right = midRight + 1;
        while (left >= 0 || right < n) {
          if (left >= 0) {
            posOrder.add(left);
            left--;
          }
          if (right < n) {
            posOrder.add(right);
            right++;
          }
        }
      }
      int val = n;
      for (int p in posOrder) {
        order[p] = val--;
      }

      // Compute sum over edges (path adjacency)
      int ans = 0;
      for (int i = 0; i < n - 1; ++i) {
        ans += order[i] * order[i + 1];
      }
      return ans;
    } else {
      // Cycle: arrange as even-indexed ascending then odd-indexed descending
      List<int> seq = [];
      for (int i = 0; i < n; i += 2) {
        seq.add(i + 1);
      }
      int start = (n % 2 == 0) ? n - 1 : n - 2;
      for (int i = start; i >= 1; i -= 2) {
        seq.add(i + 1);
      }

      // seq now holds the values in order around the cycle
      int ans = 0;
      for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        ans += seq[i] * seq[j];
      }
      return ans;
    }
  }
}
```

## Golang

```go
package main

func maxScore(n int, edges [][]int) int64 {
	adj := make([][]int, n)
	deg := make([]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
		deg[u]++
		deg[v]++
	}

	isCycle := true
	for i := 0; i < n; i++ {
		if deg[i] != 2 {
			isCycle = false
			break
		}
	}

	start := 0
	if !isCycle {
		// find an endpoint (degree 1)
		for i := 0; i < n; i++ {
			if deg[i] == 1 {
				start = i
				break
			}
		}
	}

	// obtain node order along the path or cycle
	order := make([]int, 0, n)
	prev := -1
	cur := start
	for len(order) < n {
		order = append(order, cur)
		next := -1
		for _, nb := range adj[cur] {
			if nb != prev {
				next = nb
				break
			}
		}
		prev, cur = cur, next
	}

	vals := make([]int64, n)

	if isCycle {
		// assign increasing values along the traversal order
		for i, node := range order {
			vals[node] = int64(i + 1)
		}
	} else {
		// path: place smallest numbers at ends, larger towards center
		assign := make([]int, n)
		l, r := 0, n-1
		for i := 1; i <= n; i++ {
			if i%2 == 1 { // odd -> left side
				assign[l] = i
				l++
			} else { // even -> right side
				assign[r] = i
				r--
			}
		}
		for idx, node := range order {
			vals[node] = int64(assign[idx])
		}
	}

	var total int64
	for _, e := range edges {
		u, v := e[0], e[1]
		total += vals[u] * vals[v]
	}
	return total
}
```

## Ruby

```ruby
def max_score(n, edges)
  m = edges.length
  left = []
  right = []
  push_front = true
  n.downto(1) do |v|
    if push_front
      left << v
    else
      right << v
    end
    push_front = !push_front
  end
  order = left.reverse + right

  score = 0
  (order.length - 1).times do |i|
    score += order[i] * order[i + 1]
  end
  if m == n # cycle
    score += order[0] * order[-1]
  end
  score
end
```

## Scala

```scala
object Solution {
    def maxScore(n: Int, edges: Array[Array[Int]]): Long = {
        if (n <= 1) return 0L
        val deg = Array.fill(n)(0)
        var i = 0
        while (i < edges.length) {
            val e = edges(i)
            deg(e(0)) += 1
            deg(e(1)) += 1
            i += 1
        }
        var isCycle = true
        var j = 0
        while (j < n) {
            if (deg(j) != 2) { isCycle = false; j = n } // break early
            j += 1
        }

        import scala.collection.mutable.ArrayDeque
        val dq = new ArrayDeque[Int]()
        var addFront = true
        var v = n
        while (v >= 1) {
            if (addFront) dq.prepend(v) else dq.append(v)
            addFront = !addFront
            v -= 1
        }

        val arr = dq.toArray
        var total: Long = 0L
        var k = 0
        while (k < arr.length - 1) {
            total += arr(k).toLong * arr(k + 1)
            k += 1
        }
        if (isCycle) {
            total += arr(0).toLong * arr(arr.length - 1)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // Determine if the graph is a cycle (all degrees are 2)
        let is_cycle = adj.iter().all(|v| v.len() == 2);

        // Obtain an ordering of nodes along the path or around the cycle
        let mut order: Vec<usize> = Vec::with_capacity(n_usize);
        if n_usize == 1 {
            order.push(0);
        } else if is_cycle {
            // start from node 0 and walk the cycle
            let mut cur = 0usize;
            let mut prev = usize::MAX; // sentinel for "no previous"
            for _ in 0..n_usize {
                order.push(cur);
                // choose neighbor that is not the previous node
                let next = if adj[cur][0] != prev { adj[cur][0] } else { adj[cur][1] };
                prev = cur;
                cur = next;
            }
        } else {
            // path: find an endpoint (degree == 1)
            let mut start = 0usize;
            for i in 0..n_usize {
                if adj[i].len() == 1 {
                    start = i;
                    break;
                }
            }
            let mut cur = start;
            let mut prev = usize::MAX;
            loop {
                order.push(cur);
                // find next neighbor not equal to previous
                let mut found = false;
                for &nb in &adj[cur] {
                    if nb != prev {
                        prev = cur;
                        cur = nb;
                        found = true;
                        break;
                    }
                }
                if !found {
                    break; // reached the other endpoint
                }
            }
        }

        // Assign values 1..=n to nodes to maximize edge sum
        let mut value: Vec<i64> = vec![0; n_usize];
        if is_cycle {
            // Alternate high and low numbers around the cycle
            let mut low = 1i32;
            let mut high = n;
            let mut idx = 0usize;
            while low <= high {
                if low == high {
                    value[order[idx]] = low as i64;
                    break;
                }
                value[order[idx]] = high as i64;
                idx += 1;
                value[order[idx]] = low as i64;
                idx += 1;
                low += 1;
                high -= 1;
            }
        } else {
            // Path: place numbers by alternating front/back in a deque
            use std::collections::VecDeque;
            let mut deq: VecDeque<i64> = VecDeque::new();
            let mut left = true; // true -> push_front, false -> push_back
            for v in (1..=n).rev() {
                if left {
                    deq.push_front(v as i64);
                } else {
                    deq.push_back(v as i64);
                }
                left = !left;
            }
            for (i, &node) in order.iter().enumerate() {
                value[node] = deq[i];
            }
        }

        // Compute total score over all edges
        let mut total: i64 = 0;
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            total += value[a] * value[b];
        }
        total
    }
}
```

## Racket

```racket
(define/contract (max-score n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((adj (make-vector n '()))
         (add-edge
          (lambda (a b)
            (vector-set! adj a (cons b (vector-ref adj a)))
            (vector-set! adj b (cons a (vector-ref adj b))))))
    ;; build adjacency lists
    (for-each (lambda (e)
                (let ((a (first e))
                      (b (second e)))
                  (add-edge a b)))
              edges)
    ;; find a start node: leaf if exists, otherwise 0
    (define start
      (let loop ((i 0))
        (if (< i n)
            (if (= (length (vector-ref adj i)) 1) i (loop (+ i 1)))
            0)))
    ;; traverse the graph to obtain node order
    (define order (make-vector n #f))
    (let loop ((idx 0) (cur start) (prev -1))
      (vector-set! order idx cur)
      (when (< (+ idx 1) n)
        (let* ((nbrs (vector-ref adj cur))
               (next
                (if (= (length nbrs) 1)
                    (car nbrs)
                    (let ((n1 (first nbrs)) (n2 (second nbrs)))
                      (if (= n1 prev) n2 n1)))))
          (loop (+ idx 1) next cur))))
    ;; generate value sequence using deque logic
    (define front '())
    (define back '())
    (let loop ((val n) (toggle #t))
      (when (>= val 1)
        (if toggle
            (set! back (cons val back))
            (set! front (cons val front)))
        (loop (- val 1) (not toggle))))
    (define seq-vec (list->vector (append front (reverse back))))
    ;; assign values to nodes according to order
    (define nodeVals (make-vector n 0))
    (let loop ((i 0))
      (when (< i n)
        (let* ((node (vector-ref order i))
               (value (vector-ref seq-vec i)))
          (vector-set! nodeVals node value))
        (loop (+ i 1))))
    ;; compute total score
    (define total 0)
    (for-each (lambda (e)
                (let* ((a (first e)) (b (second e))
                       (va (vector-ref nodeVals a))
                       (vb (vector-ref nodeVals b)))
                  (set! total (+ total (* va vb)))))
              edges)
    total))
```

## Erlang

```erlang
-spec max_score(N :: integer(), Edges :: [[integer()]]) -> integer().
max_score(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    {Start, _IsCycle} = find_start(Adj),
    Order = traverse_order(N, Start, Adj),
    Seq = gen_seq(N),
    NodeVals = maps:from_list(lists:zip(Order, Seq)),
    lists:foldl(fun([A,B], Acc) ->
        ValA = maps:get(A, NodeVals),
        ValB = maps:get(B, NodeVals),
        Acc + ValA * ValB
    end, 0, Edges).

build_adj([], Adj) -> Adj;
build_adj([[A,B]|Rest], Adj) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            Adj1),
    build_adj(Rest, Adj2).

find_start(Adj) ->
    case [Node || {Node, Neighs} <- maps:to_list(Adj), length(Neighs) =:= 1] of
        [] -> {hd(maps:keys(Adj)), true};
        [Start|_] -> {Start, false}
    end.

traverse_order(N, Start, Adj) ->
    traverse_order(N, Start, -1, Adj, []).

traverse_order(N, Curr, Prev, Adj, Acc) when length(Acc) =:= N ->
    lists:reverse(Acc);
traverse_order(N, Curr, Prev, Adj, Acc) ->
    NewAcc = [Curr|Acc],
    Neighs = maps:get(Curr, Adj),
    Next = case Prev of
        -1 ->
            case Neighs of
                [] -> undefined;
                _ -> hd(Neighs)
            end;
        _ ->
            case lists:filter(fun(Nb) -> Nb =/= Prev end, Neighs) of
                [] -> undefined;
                [Only] -> Only;
                [N1|_] -> N1
            end
    end,
    if Next =:= undefined orelse length(NewAcc) =:= N ->
            lists:reverse(NewAcc);
       true ->
            traverse_order(N, Next, Curr, Adj, NewAcc)
    end.

gen_seq(N) ->
    Odds = lists:seq(1, N, 2),
    StartEven = if N rem 2 =:= 0 -> N; true -> N-1 end,
    EvensDesc = case StartEven >= 2 of
        true -> lists:reverse(lists:seq(2, StartEven, 2));
        false -> []
    end,
    Odds ++ EvensDesc.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(n :: integer, edges :: [[integer]]) :: integer
  def max_score(n, edges) do
    m = length(edges)

    if n <= 1 do
      0
    else
      {total, left_end, right_end} = greedy(n - 1, n, n, 0)

      if m == n do
        total + left_end * right_end
      else
        total
      end
    end
  end

  defp greedy(0, l, r, acc), do: {acc, l, r}

  defp greedy(v, l, r, acc) do
    left_prod = v * l
    right_prod = v * r

    if left_prod >= right_prod do
      greedy(v - 1, v, r, acc + left_prod)
    else
      greedy(v - 1, l, v, acc + right_prod)
    end
  end
end
```
