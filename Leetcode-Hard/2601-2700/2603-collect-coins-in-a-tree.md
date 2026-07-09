# 2603. Collect Coins in a Tree

## Cpp

```cpp
class Solution {
public:
    int collectTheCoins(vector<int>& coins, vector<vector<int>>& edges) {
        int n = coins.size();
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // First pruning: remove leaves without coins
        vector<int> deg(n);
        for (int i = 0; i < n; ++i) deg[i] = adj[i].size();
        queue<int> q;
        vector<char> removed(n, false);
        int removedCnt = 0;
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 1 && coins[i] == 0) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (removed[u]) continue;
            removed[u] = true;
            ++removedCnt;
            for (int v : adj[u]) {
                if (removed[v]) continue;
                --deg[v];
                if (deg[v] == 1 && coins[v] == 0) q.push(v);
            }
        }
        // Second pruning: remove one layer of leaves from the remaining tree
        vector<int> deg2(n, 0);
        for (int i = 0; i < n; ++i) {
            if (removed[i]) continue;
            for (int v : adj[i]) {
                if (!removed[v]) ++deg2[i];
            }
        }
        queue<int> q2;
        vector<char> removed2 = removed;
        int secondRemoved = 0;
        for (int i = 0; i < n; ++i) {
            if (!removed2[i] && deg2[i] == 1) q2.push(i);
        }
        while (!q2.empty()) {
            int u = q2.front(); q2.pop();
            if (removed2[u]) continue;
            removed2[u] = true;
            ++secondRemoved;
            for (int v : adj[u]) {
                if (removed2[v]) continue;
                --deg2[v];
            }
        }
        int coreNodes = n - removedCnt - secondRemoved;
        if (coreNodes <= 1) return 0;
        return (coreNodes - 1) * 2;
    }
};
```

## Java

```java
class Solution {
    public int collectTheCoins(int[] coins, int[][] edges) {
        int n = coins.length;
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            adj[a].add(b);
            adj[b].add(a);
        }
        int[] degree = new int[n];
        for (int i = 0; i < n; ++i) degree[i] = adj[i].size();
        boolean[] removed = new boolean[n];

        // First pruning: remove leaves without coins
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1 && coins[i] == 0) {
                q.add(i);
            }
        }
        while (!q.isEmpty()) {
            int v = q.poll();
            removed[v] = true;
            for (int nb : adj[v]) {
                if (removed[nb]) continue;
                degree[nb]--;
                if (degree[nb] == 1 && coins[nb] == 0) {
                    q.add(nb);
                }
            }
        }

        // Second pruning: remove two outer layers regardless of coin presence
        for (int iter = 0; iter < 2; ++iter) {
            ArrayDeque<Integer> leaves = new ArrayDeque<>();
            for (int i = 0; i < n; ++i) {
                if (!removed[i] && degree[i] == 1) {
                    leaves.add(i);
                }
            }
            while (!leaves.isEmpty()) {
                int v = leaves.poll();
                removed[v] = true;
                for (int nb : adj[v]) {
                    if (removed[nb]) continue;
                    degree[nb]--;
                }
            }
        }

        int remaining = 0;
        for (boolean r : removed) if (!r) remaining++;
        return Math.max(0, (remaining - 1) * 2);
    }
}
```

## Python

```python
class Solution(object):
    def collectTheCoins(self, coins, edges):
        """
        :type coins: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(coins)
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        removed = [False] * n
        q = deque()

        # First pruning: remove leaves without coins
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            if removed[u]:
                continue
            removed[u] = True
            for v in adj[u]:
                if not removed[v]:
                    degree[v] -= 1
                    if degree[v] == 1 and coins[v] == 0:
                        q.append(v)

        # Second pruning: remove leaves (any) up to two rounds
        for _ in range(2):
            leaves = [i for i in range(n) if not removed[i] and degree[i] == 1]
            if not leaves:
                break
            for u in leaves:
                removed[u] = True
                for v in adj[u]:
                    if not removed[v]:
                        degree[v] -= 1

        remaining = sum(1 for i in range(n) if not removed[i])
        return max(0, (remaining - 1) * 2)
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1

        removed = [False] * n

        # First pruning: remove leaves without coins
        q = deque([i for i in range(n) if degree[i] == 1 and coins[i] == 0])
        while q:
            u = q.popleft()
            removed[u] = True
            for v in adj[u]:
                if not removed[v]:
                    degree[v] -= 1
                    if degree[v] == 1 and coins[v] == 0:
                        q.append(v)

        # Second pruning: remove leaves (now all have coins) and their parents
        q = deque()
        for i in range(n):
            if not removed[i] and degree[i] == 1:
                q.append((i, 0))
        while q:
            u, d = q.popleft()
            if d == 2:
                continue
            removed[u] = True
            for v in adj[u]:
                if not removed[v]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        q.append((v, d + 1))

        remaining = sum(1 for i in range(n) if not removed[i])
        return max(0, (remaining - 1) * 2)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int collectTheCoins(int* coins, int coinsSize, int** edges, int edgesSize, int* edgesColSize) {
    int n = coinsSize;
    if (n == 0) return 0;

    int *degOrig = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        degOrig[u]++; degOrig[v]++;
    }

    int **adj = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = malloc(degOrig[i] * sizeof(int));
    }
    int *idx = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][idx[u]++] = v;
        adj[v][idx[v]++] = u;
    }
    free(idx);

    /* First pruning: remove leaves without coins */
    int *deg = malloc(n * sizeof(int));
    memcpy(deg, degOrig, n * sizeof(int));
    bool *removed = calloc(n, sizeof(bool));

    int *queue = malloc(n * sizeof(int));
    int front = 0, back = 0;
    for (int i = 0; i < n; ++i) {
        if (deg[i] == 1 && coins[i] == 0) {
            queue[back++] = i;
        }
    }

    while (front < back) {
        int u = queue[front++];
        if (removed[u]) continue;
        removed[u] = true;
        for (int j = 0; j < degOrig[u]; ++j) {
            int v = adj[u][j];
            if (!removed[v]) {
                deg[v]--;
                if (deg[v] == 1 && coins[v] == 0) {
                    queue[back++] = v;
                }
            }
        }
    }

    /* Second pruning: remove leaves and their parents (two layers) */
    int *deg2 = malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (removed[i]) {
            deg2[i] = 0;
        } else {
            int cnt = 0;
            for (int j = 0; j < degOrig[i]; ++j) {
                int v = adj[i][j];
                if (!removed[v]) cnt++;
            }
            deg2[i] = cnt;
        }
    }

    front = back = 0;
    for (int i = 0; i < n; ++i) {
        if (!removed[i] && deg2[i] == 1) {
            queue[back++] = i;
        }
    }

    int steps = 0;
    while (front < back && steps < 2) {
        int layerSize = back - front;
        for (int k = 0; k < layerSize; ++k) {
            int u = queue[front++];
            if (removed[u]) continue;
            removed[u] = true;
            for (int j = 0; j < degOrig[u]; ++j) {
                int v = adj[u][j];
                if (!removed[v]) {
                    deg2[v]--;
                    if (deg2[v] == 1) {
                        queue[back++] = v;
                    }
                }
            }
        }
        steps++;
    }

    int remain = 0;
    for (int i = 0; i < n; ++i) {
        if (!removed[i]) remain++;
    }

    int ans = 0;
    if (remain > 0) ans = (remain - 1) * 2;

    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(degOrig);
    free(deg);
    free(deg2);
    free(removed);
    free(queue);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CollectTheCoins(int[] coins, int[][] edges) {
        int n = coins.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        int[] degree = new int[n];
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
            degree[u]++;
            degree[v]++;
        }

        bool[] removed = new bool[n];
        var q = new Queue<int>();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1 && coins[i] == 0) q.Enqueue(i);
        }

        while (q.Count > 0) {
            int leaf = q.Dequeue();
            if (removed[leaf]) continue;
            removed[leaf] = true;
            foreach (int nb in graph[leaf]) {
                if (removed[nb]) continue;
                degree[nb]--;
                if (degree[nb] == 1 && coins[nb] == 0) {
                    q.Enqueue(nb);
                }
            }
        }

        var leaves = new List<int>();
        for (int i = 0; i < n; i++) {
            if (!removed[i] && degree[i] == 1) leaves.Add(i);
        }

        foreach (int leaf in leaves) {
            removed[leaf] = true;
            foreach (int nb in graph[leaf]) {
                if (removed[nb]) continue;
                degree[nb]--;
            }
        }

        int remaining = 0;
        for (int i = 0; i < n; i++) {
            if (!removed[i]) remaining++;
        }

        return Math.Max(0, (remaining - 1) * 2);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} coins
 * @param {number[][]} edges
 * @return {number}
 */
var collectTheCoins = function(coins, edges) {
    const n = coins.length;
    const adj = Array.from({length: n}, () => []);
    const degree = new Array(n).fill(0);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
        degree[u]++;
        degree[v]++;
    }

    // First pruning: remove leaves without coins
    const removed = new Array(n).fill(false);
    const queue = [];
    for (let i = 0; i < n; i++) {
        if (degree[i] === 1 && coins[i] === 0) {
            queue.push(i);
        }
    }

    while (queue.length) {
        const u = queue.shift();
        removed[u] = true;
        for (const v of adj[u]) {
            if (removed[v]) continue;
            degree[v]--;
            if (degree[v] === 1 && coins[v] === 0) {
                queue.push(v);
            }
        }
    }

    // Count remaining nodes after first pruning
    let remaining = 0;
    const deg2 = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        if (!removed[i]) {
            remaining++;
            for (const v of adj[i]) {
                if (!removed[v]) deg2[i]++;
            }
        }
    }

    if (remaining <= 1) return 0;

    // Second pruning: remove leaves and their parents
    const toRemove = new Set();
    for (let i = 0; i < n; i++) {
        if (!removed[i] && deg2[i] <= 1) { // leaf in the remaining tree
            toRemove.add(i);
            for (const v of adj[i]) {
                if (!removed[v]) {
                    toRemove.add(v);
                    break;
                }
            }
        }
    }

    const coreSize = remaining - toRemove.size;
    return coreSize <= 0 ? 0 : (coreSize - 1) * 2;
};
```

## Typescript

```typescript
function collectTheCoins(coins: number[], edges: number[][]): number {
    const n = coins.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const degree = new Int32Array(n);
    for (let i = 0; i < n; i++) degree[i] = adj[i].length;

    const removed = new Uint8Array(n); // 1 if node removed in first pruning

    // First pruning: delete leaves without coins
    const queue: number[] = [];
    for (let i = 0; i < n; i++) {
        if (degree[i] === 1 && coins[i] === 0) queue.push(i);
    }
    let qIdx = 0;
    while (qIdx < queue.length) {
        const v = queue[qIdx++];
        if (removed[v]) continue;
        removed[v] = 1;
        for (const nb of adj[v]) {
            if (!removed[nb]) {
                degree[nb]--;
                if (degree[nb] === 1 && coins[nb] === 0) queue.push(nb);
            }
        }
    }

    // Compute degrees after first pruning
    const deg2 = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        if (removed[i]) continue;
        let cnt = 0;
        for (const nb of adj[i]) if (!removed[nb]) cnt++;
        deg2[i] = cnt;
    }

    // Second phase: collect leaves and their parents to delete
    const leaves: number[] = [];
    for (let i = 0; i < n; i++) {
        if (!removed[i] && deg2[i] <= 1) leaves.push(i);
    }

    const toDelete = new Uint8Array(n); // nodes removed in second phase
    let lIdx = 0;
    while (lIdx < leaves.length) {
        const leaf = leaves[lIdx++];
        if (toDelete[leaf]) continue;
        toDelete[leaf] = 1;
        for (const nb of adj[leaf]) {
            if (!removed[nb] && !toDelete[nb]) {
                toDelete[nb] = 1; // delete its parent
            }
        }
    }

    let remaining = 0;
    for (let i = 0; i < n; i++) {
        if (!removed[i] && !toDelete[i]) remaining++;
    }

    const ans = Math.max(0, (remaining - 1) * 2);
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer[][] $edges
     * @return Integer
     */
    function collectTheCoins($coins, $edges) {
        $n = count($coins);
        if ($n <= 1) return 0;

        // build adjacency list and degree array
        $adj = array_fill(0, $n, []);
        $degree = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            [$u, $v] = $e;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
            $degree[$u]++;
            $degree[$v]++;
        }

        // Phase 1: remove leaves without coins
        $removed = array_fill(0, $n, false);
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($degree[$i] == 1 && $coins[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            if ($removed[$node]) continue;
            $removed[$node] = true;
            foreach ($adj[$node] as $nbr) {
                if ($removed[$nbr]) continue;
                $degree[$nbr]--;
                if ($degree[$nbr] == 1 && $coins[$nbr] == 0) {
                    $queue->enqueue($nbr);
                }
            }
        }

        // Phase 2: remove leaves and their parents (two layers)
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if (!$removed[$i] && $degree[$i] == 1) {
                $queue->enqueue($i);
            }
        }

        for ($step = 0; $step < 2; $step++) {
            $size = $queue->count();
            for ($k = 0; $k < $size; $k++) {
                $node = $queue->dequeue();
                if ($removed[$node]) continue;
                $removed[$node] = true;
                foreach ($adj[$node] as $nbr) {
                    if ($removed[$nbr]) continue;
                    $degree[$nbr]--;
                    if ($degree[$nbr] == 1) {
                        $queue->enqueue($nbr);
                    }
                }
            }
        }

        // count remaining nodes
        $remaining = 0;
        for ($i = 0; $i < $n; $i++) {
            if (!$removed[$i]) $remaining++;
        }

        $ans = max(0, ($remaining - 1) * 2);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func collectTheCoins(_ coins: [Int], _ edges: [[Int]]) -> Int {
        let n = coins.count
        if n == 0 { return 0 }
        var adj = [[Int]](repeating: [], count: n)
        var degree = [Int](repeating: 0, count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        }
        var removed = [Bool](repeating: false, count: n)
        var queue = [Int]()
        var head = 0
        for i in 0..<n {
            if degree[i] == 1 && coins[i] == 0 {
                queue.append(i)
                removed[i] = true
            }
        }
        while head < queue.count {
            let node = queue[head]
            head += 1
            for nb in adj[node] where !removed[nb] {
                degree[nb] -= 1
                if degree[nb] == 1 && coins[nb] == 0 {
                    queue.append(nb)
                    removed[nb] = true
                }
            }
        }
        var leaves = [Int]()
        for i in 0..<n where !removed[i] && degree[i] == 1 {
            leaves.append(i)
        }
        var deg = degree
        for _ in 0..<2 {
            var newLeaves = [Int]()
            for leaf in leaves {
                removed[leaf] = true
            }
            for leaf in leaves {
                for nb in adj[leaf] where !removed[nb] {
                    deg[nb] -= 1
                    if deg[nb] == 1 {
                        newLeaves.append(nb)
                    }
                }
            }
            leaves = newLeaves
        }
        var remaining = 0
        for i in 0..<n {
            if !removed[i] { remaining += 1 }
        }
        if remaining == 0 { return 0 }
        return (remaining - 1) * 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun collectTheCoins(coins: IntArray, edges: Array<IntArray>): Int {
        val n = coins.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }
        val degree = IntArray(n) { adj[it].size }

        // First pruning: remove leaves without coins
        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (degree[i] == 1 && coins[i] == 0) {
                queue.add(i)
            }
        }
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            degree[node] = 0
            for (nbr in adj[node]) {
                if (degree[nbr] > 0) {
                    degree[nbr]--
                    if (degree[nbr] == 1 && coins[nbr] == 0) {
                        queue.add(nbr)
                    }
                }
            }
        }

        // Second pruning: remove leaves and their parents
        val q2: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        for (i in 0 until n) {
            if (degree[i] == 1) {
                q2.add(Pair(i, 0))
            }
        }
        while (q2.isNotEmpty()) {
            val (node, dist) = q2.removeFirst()
            if (dist == 2) continue
            degree[node] = 0
            for (nbr in adj[node]) {
                if (degree[nbr] > 0) {
                    degree[nbr]--
                    if (degree[nbr] == 1) {
                        q2.add(Pair(nbr, dist + 1))
                    }
                }
            }
        }

        var remain = 0
        for (d in degree) if (d > 0) remain++
        return if (remain <= 1) 0 else (remain - 1) * 2
    }
}
```

## Dart

```dart
class Solution {
  int collectTheCoins(List<int> coins, List<List<int>> edges) {
    int n = coins.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0], b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }
    List<int> degree = List.filled(n, 0);
    for (int i = 0; i < n; ++i) degree[i] = adj[i].length;

    // First pruning: remove leaves without coins
    List<int> q = [];
    int head = 0;
    for (int i = 0; i < n; ++i) {
      if (degree[i] == 1 && coins[i] == 0) q.add(i);
    }
    while (head < q.length) {
      int leaf = q[head++];
      if (degree[leaf] == 0) continue;
      degree[leaf] = 0;
      for (int nb in adj[leaf]) {
        if (degree[nb] > 0) {
          degree[nb]--;
          if (degree[nb] == 1 && coins[nb] == 0) q.add(nb);
        }
      }
    }

    // Second pruning: remove each leaf and its parent
    List<int> leaves = [];
    for (int i = 0; i < n; ++i) {
      if (degree[i] == 1) leaves.add(i);
    }
    for (int leaf in leaves) {
      if (degree[leaf] == 0) continue;
      int parent = -1;
      for (int nb in adj[leaf]) {
        if (degree[nb] > 0) {
          parent = nb;
          break;
        }
      }
      degree[leaf] = 0;
      if (parent != -1 && degree[parent] > 0) {
        for (int nb2 in adj[parent]) {
          if (degree[nb2] > 0) degree[nb2]--;
        }
        degree[parent] = 0;
      }
    }

    int sumDeg = 0;
    for (int d in degree) sumDeg += d;
    int remainingEdges = sumDeg ~/ 2;
    return remainingEdges * 2;
  }
}
```

## Golang

```go
func collectTheCoins(coins []int, edges [][]int) int {
	n := len(coins)
	if n == 0 {
		return 0
	}
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	deg := make([]int, n)
	for i := 0; i < n; i++ {
		deg[i] = len(adj[i])
	}
	removed := make([]bool, n)

	// First pruning: remove leaves without coins
	queue := make([]int, 0)
	head := 0
	for i := 0; i < n; i++ {
		if deg[i] == 1 && coins[i] == 0 {
			queue = append(queue, i)
		}
	}
	for head < len(queue) {
		v := queue[head]
		head++
		if removed[v] {
			continue
		}
		removed[v] = true
		for _, nb := range adj[v] {
			if removed[nb] {
				continue
			}
			deg[nb]--
			if deg[nb] == 1 && coins[nb] == 0 {
				queue = append(queue, nb)
			}
		}
	}

	// Second pruning: remove leaves and their parents
	type nodeDepth struct {
		v int
		d int
	}
	q2 := make([]nodeDepth, 0)
	head = 0
	for i := 0; i < n; i++ {
		if !removed[i] && deg[i] == 1 {
			q2 = append(q2, nodeDepth{i, 0})
		}
	}
	for head < len(q2) {
		cur := q2[head]
		head++
		v, d := cur.v, cur.d
		if removed[v] {
			continue
		}
		removed[v] = true
		for _, nb := range adj[v] {
			if removed[nb] {
				continue
			}
			deg[nb]--
			if d == 0 && deg[nb] == 1 {
				q2 = append(q2, nodeDepth{nb, d + 1})
			}
		}
	}

	remaining := 0
	for i := 0; i < n; i++ {
		if !removed[i] {
			remaining++
		}
	}
	if remaining <= 1 {
		return 0
	}
	return (remaining - 1) * 2
}
```

## Ruby

```ruby
def collect_the_coins(coins, edges)
  n = coins.length
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  degree = Array.new(n) { |i| adj[i].size }
  removed = Array.new(n, false)

  # First pruning: delete leaf nodes without coins
  queue = []
  head = 0
  (0...n).each do |i|
    queue << i if degree[i] == 1 && coins[i] == 0
  end

  while head < queue.size
    leaf = queue[head]
    head += 1
    next if removed[leaf]

    removed[leaf] = true
    neighbor = nil
    adj[leaf].each do |v|
      unless removed[v]
        neighbor = v
        break
      end
    end

    if neighbor
      degree[neighbor] -= 1
      queue << neighbor if degree[neighbor] == 1 && coins[neighbor] == 0
    end
  end

  # Second pruning: remove up to two layers of leaves
  queue = []
  head = 0
  (0...n).each do |i|
    queue << [i, 0] if !removed[i] && degree[i] == 1
  end

  while head < queue.size
    node, d = queue[head]
    head += 1
    next if removed[node] || d >= 2

    removed[node] = true
    neighbor = nil
    adj[node].each do |v|
      unless removed[v]
        neighbor = v
        break
      end
    end

    if neighbor
      degree[neighbor] -= 1
      queue << [neighbor, d + 1] if degree[neighbor] == 1
    end
  end

  remaining = 0
  (0...n).each { |i| remaining += 1 unless removed[i] }

  remaining <= 1 ? 0 : (remaining - 1) * 2
end
```

## Scala

```scala
object Solution {
    def collectTheCoins(coins: Array[Int], edges: Array[Array[Int]]): Int = {
        val n = coins.length
        if (n <= 1) return 0

        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }

        val degree = Array.ofDim[Int](n)
        var i = 0
        while (i < n) {
            degree(i) = adj(i).size
            i += 1
        }

        // First pruning: remove leaves without coins
        val q = new scala.collection.mutable.Queue[Int]()
        i = 0
        while (i < n) {
            if (degree(i) == 1 && coins(i) == 0) q.enqueue(i)
            i += 1
        }

        while (q.nonEmpty) {
            val leaf = q.dequeue()
            degree(leaf) = 0 // removed
            for (nb <- adj(leaf)) {
                if (degree(nb) > 0) {
                    degree(nb) -= 1
                    if (degree(nb) == 1 && coins(nb) == 0) {
                        q.enqueue(nb)
                    }
                }
            }
        }

        // Second pruning: remove leaves and their parents (up to depth 2)
        val q2 = new scala.collection.mutable.Queue[(Int, Int)]()
        i = 0
        while (i < n) {
            if (degree(i) == 1) q2.enqueue((i, 0))
            i += 1
        }

        while (q2.nonEmpty) {
            val (node, d) = q2.dequeue()
            if (d >= 2) {
                // do nothing
            } else {
                degree(node) = 0 // remove this node
                for (nb <- adj(node)) {
                    if (degree(nb) > 0) {
                        degree(nb) -= 1
                        if (degree(nb) == 1 && d + 1 < 2) {
                            q2.enqueue((nb, d + 1))
                        }
                    }
                }
            }
        }

        // Count remaining nodes
        var remain = 0
        i = 0
        while (i < n) {
            if (degree(i) > 0) remain += 1
            i += 1
        }

        if (remain <= 1) 0 else (remain - 1) * 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn collect_the_coins(coins: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        use std::collections::VecDeque;
        let n = coins.len();
        if n == 0 {
            return 0;
        }
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut deg = vec![0usize; n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
            deg[a] += 1;
            deg[b] += 1;
        }

        // First pruning: remove leaves without coins
        let mut removed = vec![false; n];
        let mut q = VecDeque::new();
        for i in 0..n {
            if deg[i] == 1 && coins[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            if removed[u] {
                continue;
            }
            removed[u] = true;
            for &v in adj[u].iter() {
                if !removed[v] {
                    deg[v] -= 1;
                    if deg[v] == 1 && coins[v] == 0 {
                        q.push_back(v);
                    }
                }
            }
        }

        // Second pruning: remove up to two layers of leaves
        let mut q2 = VecDeque::new();
        for i in 0..n {
            if !removed[i] && deg[i] == 1 {
                q2.push_back((i, 0));
            }
        }
        while let Some((u, d)) = q2.pop_front() {
            if d == 2 {
                continue;
            }
            removed[u] = true;
            for &v in adj[u].iter() {
                if !removed[v] {
                    deg[v] -= 1;
                    if deg[v] == 1 {
                        q2.push_back((v, d + 1));
                    }
                }
            }
        }

        let remaining = removed.iter().filter(|&&r| !r).count();
        if remaining == 0 {
            0
        } else {
            ((remaining as i32) - 1) * 2
        }
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (collect-the-coins coins edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length coins))
         (adj (make-vector n '()))
         (degree (make-vector n 0))
         (removed (make-vector n #f)))
    ;; build adjacency list
    (for ([e edges])
      (define a (first e))
      (define b (second e))
      (vector-set! adj a (cons b (vector-ref adj a)))
      (vector-set! adj b (cons a (vector-ref adj b))))
    ;; compute degrees
    (for ([i (in-range n)])
      (vector-set! degree i (length (vector-ref adj i))))
    ;; first pruning: remove leaves without coins
    (define q (make-queue))
    (for ([i (in-range n)])
      (when (and (= (vector-ref degree i) 1)
                 (= (list-ref coins i) 0))
        (enqueue! q i)))
    (let loop ()
      (unless (queue-empty? q)
        (define u (dequeue! q))
        (when (not (vector-ref removed u))
          (vector-set! removed u #t)
          (for ([v (in-list (vector-ref adj u))])
            (when (not (vector-ref removed v))
              (vector-set! degree v (- (vector-ref degree v) 1))
              (when (and (= (vector-ref degree v) 1)
                         (= (list-ref coins v) 0))
                (enqueue! q v)))))
        (loop)))
    ;; second pruning: remove up to two layers of leaves
    (define leaf-q (make-queue))
    (for ([i (in-range n)])
      (when (and (not (vector-ref removed i))
                 (= (vector-ref degree i) 1))
        (enqueue! leaf-q i)))
    (let loop2 ((layer 0))
      (when (< layer 2)
        (define sz (queue-count leaf-q))
        (for ([k (in-range sz)])
          (define u (dequeue! leaf-q))
          (when (not (vector-ref removed u))
            (vector-set! removed u #t)
            (for ([v (in-list (vector-ref adj u))])
              (when (not (vector-ref removed v))
                (vector-set! degree v (- (vector-ref degree v) 1))
                (when (= (vector-ref degree v) 1)
                  (enqueue! leaf-q v))))))
        (loop2 (+ layer 1))))
    ;; count remaining nodes
    (define remaining
      (for/sum ([i (in-range n)])
        (if (vector-ref removed i) 0 1)))
    (if (<= remaining 0)
        0
        (* 2 (- remaining 1)))))
```

## Erlang

```erlang
-spec collect_the_coins(Coins :: [integer()], Edges :: [[integer()]]) -> integer().
collect_the_coins(Coins, Edges) ->
    N = length(Coins),
    %% Build adjacency list as array of lists
    Adj0 = array:new(N, {default, []}),
    Adj = build_adj(Edges, Adj0),
    %% Convert Coins to array for O(1) access
    CoinsArr = array:from_list(Coins),
    %% Initial degrees
    DegList = [length(array:get(Adj, I)) || I <- lists:seq(0, N - 1)],
    Deg0 = array:from_list(DegList),
    Removed0 = array:new(N, {default, false}),
    %% First pruning: remove leaves without coins
    InitLeaves = [I || I <- lists:seq(0, N - 1),
                       array:get(Deg0, I) == 1,
                       array:get(CoinsArr, I) == 0],
    {Deg1, Removed1} = prune_no_coin_leaves(InitLeaves, Deg0, Removed0, Adj, CoinsArr),
    %% Second pruning: remove leaves and their parents (up to distance 1)
    RemainingSeq = lists:seq(0, N - 1),
    Leaves2 = [I || I <- RemainingSeq,
                    not array:get(Removed1, I),
                    array:get(Deg1, I) == 1],
    {Deg2, Removed2, Parents} = prune_layer(Leaves2, Deg1, Removed1, Adj),
    {_DegFinal, _RemovedFinal, _} = prune_layer(Parents, Deg2, Removed2, Adj),
    %% Count remaining nodes
    Remaining = [I || I <- RemainingSeq, not array:get(_RemovedFinal, I)],
    RemCnt = length(Remaining),
    case RemCnt of
        0 -> 0;
        _ -> max(0, (RemCnt - 1) * 2)
    end.

%% Build adjacency array from edge list
build_adj([], Adj) -> Adj;
build_adj([[A,B]|Rest], Adj) ->
    L1 = [B | array:get(Adj, A)],
    Adj1 = array:set(Adj, A, L1),
    L2 = [A | array:get(Adj1, B)],
    Adj2 = array:set(Adj1, B, L2),
    build_adj(Rest, Adj2).

%% Prune leaves that have no coin (first phase)
prune_no_coin_leaves([], Deg, Removed, _Adj, _Coins) ->
    {Deg, Removed};
prune_no_coin_leaves([U|Q], Deg, Removed, Adj, Coins) ->
    case array:get(Removed, U) of
        true -> prune_no_coin_leaves(Q, Deg, Removed, Adj, Coins);
        false ->
            Removed1 = array:set(Removed, U, true),
            Neighs = array:get(Adj, U),
            {Deg2, NewLeaves} = lists:foldl(
                fun(V, {DAcc, LAcc}) ->
                    case array:get(Removed1, V) of
                        true -> {DAcc, LAcc};
                        false ->
                            Dv = array:get(DAcc, V) - 1,
                            DAcc1 = array:set(DAcc, V, Dv),
                            case {Dv, array:get(Coins, V)} of
                                {1,0} -> {DAcc1, [V|LAcc]};
                                _     -> {DAcc1, LAcc}
                            end
                    end
                end,
                {Deg, []},
                Neighs),
            prune_no_coin_leaves(NewLeaves ++ Q, Deg2, Removed1, Adj, Coins)
    end.

%% Prune a layer of leaves (used for second phase). Returns new degrees, removed array and list of newly created leaves.
prune_layer([], Deg, Removed, _Adj) ->
    {Deg, Removed, []};
prune_layer([U|Q], Deg, Removed, Adj) ->
    case array:get(Removed, U) of
        true -> prune_layer(Q, Deg, Removed, Adj);
        false ->
            Removed1 = array:set(Removed, U, true),
            Neighs = array:get(Adj, U),
            {Deg2, NewLeaves} = lists:foldl(
                fun(V, {DAcc, LAcc}) ->
                    case array:get(Removed1, V) of
                        true -> {DAcc, LAcc};
                        false ->
                            Dv = array:get(DAcc, V) - 1,
                            DAcc1 = array:set(DAcc, V, Dv),
                            if Dv == 1 -> {DAcc1, [V|LAcc]};
                               true   -> {DAcc1, LAcc}
                            end
                    end
                end,
                {Deg, []},
                Neighs),
            {DegFinal, RemovedFinal, Parents} = prune_layer(Q ++ NewLeaves, Deg2, Removed1, Adj),
            {DegFinal, RemovedFinal, NewLeaves ++ Parents}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec collect_the_coins(coins :: [integer], edges :: [[integer]]) :: integer
  def collect_the_coins(coins, edges) do
    n = length(coins)

    # adjacency list as a map: node => [neighbors]
    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], fn lst -> [b | lst] end)
        |> Map.update(b, [a], fn lst -> [a | lst] end)
      end)

    # convert coins to an array for O(1) access
    coin_arr = :array.from_list(coins)

    # initial degrees
    init_deg =
      Enum.map(0..(n - 1), fn i ->
        (Map.get(adj, i, []) |> length())
      end)

    deg_arr = :array.from_list(init_deg)
    removed = MapSet.new()

    # queue of leaves without a coin
    initial_leaves =
      Enum.filter(0..(n - 1), fn i ->
        :array.get(i, deg_arr) == 1 and :array.get(i, coin_arr) == 0
      end)

    q = :queue.from_list(initial_leaves)
    {removed, deg_arr} = prune(q, removed, deg_arr, adj, coin_arr)

    total_remain = n - MapSet.size(removed)

    if total_remain <= 0 do
      0
    else
      # degrees inside the remaining subgraph
      sub_deg_arr =
        :array.from_list(
          Enum.map(0..(n - 1), fn i ->
            if MapSet.member?(removed, i) do
              0
            else
              Enum.count(Map.get(adj, i, []), fn nb -> not MapSet.member?(removed, nb) end)
            end
          end)
        )

      # mark leaves and their neighbors for second removal
      to_remove =
        Enum.reduce(0..(n - 1), MapSet.new(), fn i, acc ->
          if not MapSet.member?(removed, i) do
            deg = :array.get(i, sub_deg_arr)

            if deg == 1 do
              nb = Enum.find(Map.get(adj, i, []), fn v -> not MapSet.member?(removed, v) end)
              acc
              |> MapSet.put(i)
              |> (fn set ->
                    if nb != nil, do: MapSet.put(set, nb), else: set
                  end).()
            else
              acc
            end
          else
            acc
          end
        end)

      core = total_remain - MapSet.size(to_remove)

      if core <= 0, do: 0, else: (core - 1) * 2
    end
  end

  defp prune(q, removed, deg_arr, adj, coin_arr) do
    case :queue.out(q) do
      {:empty, _} ->
        {removed, deg_arr}

      {{:value, leaf}, q_rest} ->
        if MapSet.member?(removed, leaf) do
          prune(q_rest, removed, deg_arr, adj, coin_arr)
        else
          removed = MapSet.put(removed, leaf)

          {deg_arr, q_new} =
            Enum.reduce(Map.get(adj, leaf, []), {deg_arr, q_rest}, fn nb,
                                                                    {darr, qq} ->
              if not MapSet.member?(removed, nb) do
                cur = :array.get(nb, darr)
                new = cur - 1
                darr = :array.set(nb, new, darr)

                if new == 1 and :array.get(nb, coin_arr) == 0 do
                  {darr, :queue.in(nb, qq)}
                else
                  {darr, qq}
                end
              else
                {darr, qq}
              end
            end)

          prune(q_new, removed, deg_arr, adj, coin_arr)
        end
    end
  end
end
```
