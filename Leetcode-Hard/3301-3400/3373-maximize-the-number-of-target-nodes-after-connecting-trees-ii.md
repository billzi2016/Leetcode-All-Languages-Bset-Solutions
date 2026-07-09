# 3373. Maximize the Number of Target Nodes After Connecting Trees II

## Cpp

```cpp
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;
        vector<vector<int>> g1(n), g2(m);
        for (auto &e : edges1) {
            g1[e[0]].push_back(e[1]);
            g1[e[1]].push_back(e[0]);
        }
        for (auto &e : edges2) {
            g2[e[0]].push_back(e[1]);
            g2[e[1]].push_back(e[0]);
        }
        vector<int> col1(n, -1), col2(m, -1);
        long long white1 = 0, black1 = 0, white2 = 0, black2 = 0;
        // BFS for tree1
        queue<int> q;
        q.push(0);
        col1[0] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (col1[u]==0) ++white1; else ++black1;
            for (int v: g1[u]) if (col1[v]==-1) {
                col1[v]=col1[u]^1;
                q.push(v);
            }
        }
        // BFS for tree2
        q.push(0);
        col2[0] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (col2[u]==0) ++white2; else ++black2;
            for (int v: g2[u]) if (col2[v]==-1) {
                col2[v]=col2[u]^1;
                q.push(v);
            }
        }
        long long bestSecond = max(white2, black2);
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            long long sameColorCount = (col1[i]==0 ? white1 : black1);
            ans[i] = static_cast<int>(sameColorCount + bestSecond);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;

        // Build adjacency lists
        @SuppressWarnings("unchecked")
        List<Integer>[] adj1 = new ArrayList[n];
        for (int i = 0; i < n; i++) adj1[i] = new ArrayList<>();
        for (int[] e : edges1) {
            int u = e[0], v = e[1];
            adj1[u].add(v);
            adj1[v].add(u);
        }

        @SuppressWarnings("unchecked")
        List<Integer>[] adj2 = new ArrayList[m];
        for (int i = 0; i < m; i++) adj2[i] = new ArrayList<>();
        for (int[] e : edges2) {
            int u = e[0], v = e[1];
            adj2[u].add(v);
            adj2[v].add(u);
        }

        // Compute colors and counts for first tree
        boolean[] color1 = new boolean[n]; // false = white (even depth), true = black (odd depth)
        int white1 = 0, black1 = 0;
        {
            boolean[] visited = new boolean[n];
            ArrayDeque<Integer> dq = new ArrayDeque<>();
            dq.add(0);
            visited[0] = true;
            while (!dq.isEmpty()) {
                int u = dq.poll();
                if (color1[u]) black1++; else white1++;
                for (int v : adj1[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        color1[v] = !color1[u];
                        dq.add(v);
                    }
                }
            }
        }

        // Compute colors and counts for second tree
        boolean[] color2 = new boolean[m];
        int white2 = 0, black2 = 0;
        {
            boolean[] visited = new boolean[m];
            ArrayDeque<Integer> dq = new ArrayDeque<>();
            dq.add(0);
            visited[0] = true;
            while (!dq.isEmpty()) {
                int u = dq.poll();
                if (color2[u]) black2++; else white2++;
                for (int v : adj2[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        color2[v] = !color2[u];
                        dq.add(v);
                    }
                }
            }
        }

        int maxSecond = Math.max(white2, black2);
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int evenInFirst = color1[i] ? black1 : white1;
            answer[i] = evenInFirst + maxSecond;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges1) + 1
        m = len(edges2) + 1

        # build adjacency lists
        adj1 = [[] for _ in range(n)]
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # BFS to color nodes (0/1) and count colors
        from collections import deque

        def bfs_color(adj):
            size = len(adj)
            color = [-1] * size
            cnt0 = cnt1 = 0
            dq = deque([0])
            color[0] = 0
            cnt0 += 1
            while dq:
                node = dq.popleft()
                curc = color[node]
                for nb in adj[node]:
                    if color[nb] == -1:
                        nc = curc ^ 1
                        color[nb] = nc
                        if nc == 0:
                            cnt0 += 1
                        else:
                            cnt1 += 1
                        dq.append(nb)
            return color, cnt0, cnt1

        color1, white1, black1 = bfs_color(adj1)
        _, white2, black2 = bfs_color(adj2)

        best_second = max(white2, black2)

        ans = [0] * n
        for i in range(n):
            same = white1 if color1[i] == 0 else black1
            ans[i] = same + best_second

        return ans
```

## Python3

```python
class Solution:
    def maxTargetNodes(self, edges1, edges2):
        from collections import deque
        n = len(edges1) + 1
        m = len(edges2) + 1

        # build adjacency lists
        g1 = [[] for _ in range(n)]
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        g2 = [[] for _ in range(m)]
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a]

        # compute parity colors for tree 1
        color1 = [0] * n
        seen = [False] * n
        dq = deque([0])
        seen[0] = True
        while dq:
            u = dq.popleft()
            for v in g1[u]:
                if not seen[v]:
                    seen[v] = True
                    color1[v] = color1[u] ^ 1
                    dq.append(v)
        white1 = sum(1 for c in color1 if c == 0)
        black1 = n - white1

        # compute parity colors for tree 2
        color2 = [0] * m
        seen = [False] * m
        dq = deque([0])
        seen[0] = True
        while dq:
            u = dq.popleft()
            for v in g2[u]:
                if not seen[v]:
                    seen[v] = True
                    color2[v] = color2[u] ^ 1
                    dq.append(v)
        white2 = sum(1 for c in color2 if c == 0)
        black2 = m - white2

        max_odd_second = max(white2, black2)

        ans = [0] * n
        for i in range(n):
            same_parity_cnt = white1 if color1[i] == 0 else black1
            ans[i] = same_parity_cnt + max_odd_second

        return ans
```

## C

```c
#include <stdlib.h>

struct Edge {
    int to;
    int next;
};

static void addEdge(int *head, struct Edge *e, int *cnt, int u, int v) {
    e[*cnt].to = v;
    e[*cnt].next = head[u];
    head[u] = (*cnt)++;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxTargetNodes(int** edges1, int edges1Size, int* edges1ColSize,
                    int** edges2, int edges2Size, int* edges2ColSize,
                    int* returnSize) {
    int n = edges1Size + 1;
    int m = edges2Size + 1;

    /* Build adjacency for first tree */
    int *head1 = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head1[i] = -1;
    struct Edge *e1 = (struct Edge*)malloc(2 * edges1Size * sizeof(struct Edge));
    int ecnt1 = 0;
    for (int i = 0; i < edges1Size; ++i) {
        int a = edges1[i][0];
        int b = edges1[i][1];
        addEdge(head1, e1, &ecnt1, a, b);
        addEdge(head1, e1, &ecnt1, b, a);
    }

    /* Build adjacency for second tree */
    int *head2 = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) head2[i] = -1;
    struct Edge *e2 = (struct Edge*)malloc(2 * edges2Size * sizeof(struct Edge));
    int ecnt2 = 0;
    for (int i = 0; i < edges2Size; ++i) {
        int a = edges2[i][0];
        int b = edges2[i][1];
        addEdge(head2, e2, &ecnt2, a, b);
        addEdge(head2, e2, &ecnt2, b, a);
    }

    /* Color first tree and count colors */
    char *color1 = (char*)malloc(n * sizeof(char));
    for (int i = 0; i < n; ++i) color1[i] = -1;
    int white1 = 0, black1 = 0;
    int *stack = (int*)malloc(n * sizeof(int));
    int top = 0;
    stack[top++] = 0;
    color1[0] = 0;
    while (top) {
        int u = stack[--top];
        if (color1[u] == 0) ++white1; else ++black1;
        for (int ei = head1[u]; ei != -1; ei = e1[ei].next) {
            int v = e1[ei].to;
            if (color1[v] == (char)-1) {
                color1[v] = color1[u] ^ 1;
                stack[top++] = v;
            }
        }
    }

    /* Color second tree and count colors */
    char *color2 = (char*)malloc(m * sizeof(char));
    for (int i = 0; i < m; ++i) color2[i] = -1;
    int white2 = 0, black2 = 0;
    top = 0;
    stack[top++] = 0;
    color2[0] = 0;
    while (top) {
        int u = stack[--top];
        if (color2[u] == 0) ++white2; else ++black2;
        for (int ei = head2[u]; ei != -1; ei = e2[ei].next) {
            int v = e2[ei].to;
            if (color2[v] == (char)-1) {
                color2[v] = color2[u] ^ 1;
                stack[top++] = v;
            }
        }
    }

    int maxSecond = white2 > black2 ? white2 : black2;

    int *ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        ans[i] = (color1[i] == 0 ? white1 : black1) + maxSecond;
    }

    *returnSize = n;

    /* Free temporary allocations */
    free(head1); free(e1);
    free(head2); free(e2);
    free(color1); free(color2);
    free(stack);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaxTargetNodes(int[][] edges1, int[][] edges2) {
        int n = edges1.Length + 1;
        int m = edges2.Length + 1;

        // Build adjacency lists
        List<int>[] g1 = new List<int>[n];
        for (int i = 0; i < n; i++) g1[i] = new List<int>();
        foreach (var e in edges1) {
            int a = e[0], b = e[1];
            g1[a].Add(b);
            g1[b].Add(a);
        }

        List<int>[] g2 = new List<int>[m];
        for (int i = 0; i < m; i++) g2[i] = new List<int>();
        foreach (var e in edges2) {
            int a = e[0], b = e[1];
            g2[a].Add(b);
            g2[b].Add(a);
        }

        // BFS to color tree 1
        int[] color1 = new int[n];
        Array.Fill(color1, -1);
        int cnt0_1 = 0, cnt1_1 = 0;
        Queue<int> q = new Queue<int>();
        q.Enqueue(0);
        color1[0] = 0;
        cnt0_1++;
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g1[u]) {
                if (color1[v] == -1) {
                    color1[v] = color1[u] ^ 1;
                    if (color1[v] == 0) cnt0_1++; else cnt1_1++;
                    q.Enqueue(v);
                }
            }
        }

        // BFS to color tree 2
        int[] color2 = new int[m];
        Array.Fill(color2, -1);
        int cnt0_2 = 0, cnt1_2 = 0;
        q.Clear();
        q.Enqueue(0);
        color2[0] = 0;
        cnt0_2++;
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g2[u]) {
                if (color2[v] == -1) {
                    color2[v] = color2[u] ^ 1;
                    if (color2[v] == 0) cnt0_2++; else cnt1_2++;
                    q.Enqueue(v);
                }
            }
        }

        int maxSecond = Math.Max(cnt0_2, cnt1_2);
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int sameColorCount = color1[i] == 0 ? cnt0_1 : cnt1_1;
            answer[i] = sameColorCount + maxSecond;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @return {number[]}
 */
var maxTargetNodes = function(edges1, edges2) {
    const n = edges1.length + 1;
    const m = edges2.length + 1;

    // Build adjacency for first tree
    const adj1 = Array.from({length: n}, () => []);
    for (const [a, b] of edges1) {
        adj1[a].push(b);
        adj1[b].push(a);
    }

    // Color first tree and count colors
    const color1 = new Int8Array(n);
    let white1 = 0, black1 = 0;
    const stack1 = [0];
    const visited1 = new Uint8Array(n);
    visited1[0] = 1;
    while (stack1.length) {
        const u = stack1.pop();
        const c = color1[u];
        if (c === 0) white1++; else black1++;
        for (const v of adj1[u]) {
            if (!visited1[v]) {
                visited1[v] = 1;
                color1[v] = c ^ 1;
                stack1.push(v);
            }
        }
    }

    // Build adjacency for second tree
    const adj2 = Array.from({length: m}, () => []);
    for (const [a, b] of edges2) {
        adj2[a].push(b);
        adj2[b].push(a);
    }

    // Color second tree and count colors
    const color2 = new Int8Array(m);
    let white2 = 0, black2 = 0;
    const stack2 = [0];
    const visited2 = new Uint8Array(m);
    visited2[0] = 1;
    while (stack2.length) {
        const u = stack2.pop();
        const c = color2[u];
        if (c === 0) white2++; else black2++;
        for (const v of adj2[u]) {
            if (!visited2[v]) {
                visited2[v] = 1;
                color2[v] = c ^ 1;
                stack2.push(v);
            }
        }
    }

    const maxSecond = Math.max(white2, black2);
    const ans = new Array(n);
    for (let i = 0; i < n; ++i) {
        const evenFirst = color1[i] === 0 ? white1 : black1;
        ans[i] = evenFirst + maxSecond;
    }
    return ans;
};
```

## Typescript

```typescript
function maxTargetNodes(edges1: number[][], edges2: number[][]): number[] {
    const n = edges1.length + 1;
    const m = edges2.length + 1;

    // build adjacency lists
    const adj1: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges1) {
        adj1[a].push(b);
        adj1[b].push(a);
    }
    const adj2: number[][] = Array.from({ length: m }, () => []);
    for (const [u, v] of edges2) {
        adj2[u].push(v);
        adj2[v].push(u);
    }

    // color first tree
    const color1: number[] = new Array(n).fill(-1);
    const queue1: number[] = [0];
    color1[0] = 0;
    let idx = 0;
    while (idx < queue1.length) {
        const node = queue1[idx++];
        for (const nb of adj1[node]) {
            if (color1[nb] === -1) {
                color1[nb] = color1[node] ^ 1;
                queue1.push(nb);
            }
        }
    }
    let white1 = 0;
    for (let i = 0; i < n; ++i) if (color1[i] === 0) ++white1;
    const black1 = n - white1;

    // color second tree
    const color2: number[] = new Array(m).fill(-1);
    const queue2: number[] = [0];
    color2[0] = 0;
    idx = 0;
    while (idx < queue2.length) {
        const node = queue2[idx++];
        for (const nb of adj2[node]) {
            if (color2[nb] === -1) {
                color2[nb] = color2[node] ^ 1;
                queue2.push(nb);
            }
        }
    }
    let white2 = 0;
    for (let i = 0; i < m; ++i) if (color2[i] === 0) ++white2;
    const black2 = m - white2;

    const maxSecond = Math.max(white2, black2);

    const ans: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        const evenCount = color1[i] === 0 ? white1 : black1;
        ans[i] = evenCount + maxSecond;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges1
     * @param Integer[][] $edges2
     * @return Integer[]
     */
    function maxTargetNodes($edges1, $edges2) {
        // Number of nodes in each tree
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;

        // Build adjacency lists
        $adj1 = array_fill(0, $n, []);
        foreach ($edges1 as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj1[$a][] = $b;
            $adj1[$b][] = $a;
        }

        $adj2 = array_fill(0, $m, []);
        foreach ($edges2 as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj2[$u][] = $v;
            $adj2[$v][] = $u;
        }

        // Color arrays: 0 or 1, -1 unvisited
        $color1 = array_fill(0, $n, -1);
        $color2 = array_fill(0, $m, -1);

        // Count of nodes per color in each tree
        $cntFirst = [0, 0];
        $cntSecond = [0, 0];

        // DFS for first tree
        $stack = [0];
        $color1[0] = 0;
        $cntFirst[0] = 1;
        while (!empty($stack)) {
            $u = array_pop($stack);
            foreach ($adj1[$u] as $v) {
                if ($color1[$v] === -1) {
                    $color1[$v] = 1 - $color1[$u];
                    $cntFirst[$color1[$v]]++;
                    $stack[] = $v;
                }
            }
        }

        // DFS for second tree
        $stack = [0];
        $color2[0] = 0;
        $cntSecond[0] = 1;
        while (!empty($stack)) {
            $u = array_pop($stack);
            foreach ($adj2[$u] as $v) {
                if ($color2[$v] === -1) {
                    $color2[$v] = 1 - $color2[$u];
                    $cntSecond[$color2[$v]]++;
                    $stack[] = $v;
                }
            }
        }

        // Maximum possible target nodes contributed by second tree
        $maxSecond = max($cntSecond[0], $cntSecond[1]);

        // Build answer for each node in first tree
        $answer = [];
        for ($i = 0; $i < $n; ++$i) {
            $sameColorCount = $cntFirst[$color1[$i]];
            $answer[] = $sameColorCount + $maxSecond;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]]) -> [Int] {
        // First tree
        let n = edges1.count + 1
        var adj1 = Array(repeating: [Int](), count: n)
        for e in edges1 {
            let a = e[0], b = e[1]
            adj1[a].append(b)
            adj1[b].append(a)
        }
        var color1 = Array(repeating: 0, count: n) // 0 = white, 1 = black
        var white1 = 0, black1 = 0
        var stack = [Int]()
        var visited = Array(repeating: false, count: n)
        stack.append(0)
        visited[0] = true
        while let u = stack.popLast() {
            let c = color1[u]
            if c == 0 { white1 += 1 } else { black1 += 1 }
            for v in adj1[u] where !visited[v] {
                visited[v] = true
                color1[v] = c ^ 1
                stack.append(v)
            }
        }
        
        // Second tree
        let m = edges2.count + 1
        var adj2 = Array(repeating: [Int](), count: m)
        for e in edges2 {
            let a = e[0], b = e[1]
            adj2[a].append(b)
            adj2[b].append(a)
        }
        var color2 = Array(repeating: 0, count: m)
        var white2 = 0, black2 = 0
        stack.removeAll()
        visited = Array(repeating: false, count: m)
        stack.append(0)
        visited[0] = true
        while let u = stack.popLast() {
            let c = color2[u]
            if c == 0 { white2 += 1 } else { black2 += 1 }
            for v in adj2[u] where !visited[v] {
                visited[v] = true
                color2[v] = c ^ 1
                stack.append(v)
            }
        }
        
        let maxSecond = max(white2, black2)
        var answer = [Int]()
        answer.reserveCapacity(n)
        for i in 0..<n {
            let evenCount = (color1[i] == 0) ? white1 : black1
            answer.append(evenCount + maxSecond)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTargetNodes(edges1: Array<IntArray>, edges2: Array<IntArray>): IntArray {
        val n = edges1.size + 1
        val m = edges2.size + 1

        fun bfsColors(edges: Array<IntArray>, size: Int): Pair<IntArray, LongArray> {
            val adj = Array(size) { mutableListOf<Int>() }
            for (e in edges) {
                val u = e[0]
                val v = e[1]
                adj[u].add(v)
                adj[v].add(u)
            }
            val color = IntArray(size) { -1 }
            val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
            color[0] = 0
            deque.add(0)
            var white = 0L
            var black = 0L
            while (!deque.isEmpty()) {
                val u = deque.removeFirst()
                if (color[u] == 0) white++ else black++
                for (v in adj[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] xor 1
                        deque.add(v)
                    }
                }
            }
            return Pair(color, longArrayOf(white, black))
        }

        val (color1, cnt1) = bfsColors(edges1, n)
        val (_, cnt2) = bfsColors(edges2, m)

        val maxSecond = kotlin.math.max(cnt2[0], cnt2[1]).toInt()
        val ans = IntArray(n)
        for (i in 0 until n) {
            val evenFirst = if (color1[i] == 0) cnt1[0] else cnt1[1]
            ans[i] = (evenFirst + maxSecond).toInt()
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxTargetNodes(List<List<int>> edges1, List<List<int>> edges2) {
    // Helper to build adjacency list
    List<List<int>> buildAdj(int n, List<List<int>> edges) {
      var adj = List.generate(n, (_) => <int>[]);
      for (var e in edges) {
        int u = e[0], v = e[1];
        adj[u].add(v);
        adj[v].add(u);
      }
      return adj;
    }

    // Helper to compute colors and counts
    List<int> bfsColors(List<List<int>> adj) {
      int n = adj.length;
      var color = List.filled(n, -1);
      var queue = <int>[];
      color[0] = 0;
      queue.add(0);
      int head = 0;
      while (head < queue.length) {
        int u = queue[head++];
        for (int v in adj[u]) {
          if (color[v] == -1) {
            color[v] = 1 - color[u];
            queue.add(v);
          }
        }
      }
      return color;
    }

    // First tree
    int n = edges1.isEmpty ? 0 : edges1.map((e) => e[0]).fold(0, (a, b) => a > b ? a : b) + 1;
    // Actually n can be derived from max node index in edges1 plus 1.
    // Safer: compute using length of colors after building adjacency.
    var adj1 = buildAdj(n, edges1);
    var color1 = bfsColors(adj1);
    int white1 = 0, black1 = 0;
    for (int c in color1) {
      if (c == 0) white1++; else black1++;
    }

    // Second tree
    int m = edges2.isEmpty ? 0 : edges2.map((e) => e[0]).fold(0, (a, b) => a > b ? a : b) + 1;
    var adj2 = buildAdj(m, edges2);
    var color2 = bfsColors(adj2);
    int white2 = 0, black2 = 0;
    for (int c in color2) {
      if (c == 0) white2++; else black2++;
    }
    int maxSecond = white2 > black2 ? white2 : black2;

    // Build answer
    var ans = List<int>.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int sameColorCount = color1[i] == 0 ? white1 : black1;
      ans[i] = sameColorCount + maxSecond;
    }
    return ans;
  }
}
```

## Golang

```go
package main

func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
	n := len(edges1) + 1
	m := len(edges2) + 1

	// Build adjacency for first tree
	adj1 := make([][]int, n)
	for _, e := range edges1 {
		u, v := e[0], e[1]
		adj1[u] = append(adj1[u], v)
		adj1[v] = append(adj1[v], u)
	}
	color1 := make([]int8, n) // 0 or 1
	visited1 := make([]bool, n)
	var white1, black1 int
	queue := []int{0}
	visited1[0] = true
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		if color1[u] == 0 {
			white1++
		} else {
			black1++
		}
		for _, v := range adj1[u] {
			if !visited1[v] {
				visited1[v] = true
				color1[v] = color1[u] ^ 1
				queue = append(queue, v)
			}
		}
	}

	// Build adjacency for second tree
	adj2 := make([][]int, m)
	for _, e := range edges2 {
		u, v := e[0], e[1]
		adj2[u] = append(adj2[u], v)
		adj2[v] = append(adj2[v], u)
	}
	color2 := make([]int8, m)
	visited2 := make([]bool, m)
	var white2, black2 int
	queue = []int{0}
	visited2[0] = true
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		if color2[u] == 0 {
			white2++
		} else {
			black2++
		}
		for _, v := range adj2[u] {
			if !visited2[v] {
				visited2[v] = true
				color2[v] = color2[u] ^ 1
				queue = append(queue, v)
			}
		}
	}

	maxSecond := white2
	if black2 > maxSecond {
		maxSecond = black2
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		var evenCount int
		if color1[i] == 0 {
			evenCount = white1
		} else {
			evenCount = black1
		}
		ans[i] = evenCount + maxSecond
	}
	return ans
}
```

## Ruby

```ruby
def max_target_nodes(edges1, edges2)
  n = edges1.length + 1
  m = edges2.length + 1

  adj1 = Array.new(n) { [] }
  edges1.each do |a, b|
    adj1[a] << b
    adj1[b] << a
  end

  color1 = Array.new(n, -1)
  cnt1 = [0, 0]
  stack = [[0, 0]]
  until stack.empty?
    node, col = stack.pop
    next if color1[node] != -1
    color1[node] = col
    cnt1[col] += 1
    adj1[node].each { |nb| stack << [nb, col ^ 1] unless color1[nb] != -1 }
  end

  adj2 = Array.new(m) { [] }
  edges2.each do |a, b|
    adj2[a] << b
    adj2[b] << a
  end

  color2 = Array.new(m, -1)
  cnt2 = [0, 0]
  stack = [[0, 0]]
  until stack.empty?
    node, col = stack.pop
    next if color2[node] != -1
    color2[node] = col
    cnt2[col] += 1
    adj2[node].each { |nb| stack << [nb, col ^ 1] unless color2[nb] != -1 }
  end

  max_second = cnt2.max
  ans = Array.new(n)
  n.times do |i|
    ans[i] = cnt1[color1[i]] + max_second
  end
  ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, Stack}
  
  def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Array[Int] = {
    val n = edges1.length + 1
    val m = edges2.length + 1

    // Build adjacency lists
    val adj1 = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges1) {
      val a = e(0)
      val b = e(1)
      adj1(a).append(b)
      adj1(b).append(a)
    }

    val adj2 = Array.fill(m)(new ArrayBuffer[Int]())
    for (e <- edges2) {
      val a = e(0)
      val b = e(1)
      adj2(a).append(b)
      adj2(b).append(a)
    }

    // Compute colors and counts for first tree
    val color1 = Array.fill(n)(-1)
    var white1 = 0
    var black1 = 0
    val stack1 = new Stack[Int]()
    color1(0) = 0
    stack1.push(0)
    while (stack1.nonEmpty) {
      val u = stack1.pop()
      if (color1(u) == 0) white1 += 1 else black1 += 1
      for (v <- adj1(u)) {
        if (color1(v) == -1) {
          color1(v) = 1 - color1(u)
          stack1.push(v)
        }
      }
    }

    // Compute colors and counts for second tree
    val color2 = Array.fill(m)(-1)
    var white2 = 0
    var black2 = 0
    val stack2 = new Stack[Int]()
    color2(0) = 0
    stack2.push(0)
    while (stack2.nonEmpty) {
      val u = stack2.pop()
      if (color2(u) == 0) white2 += 1 else black2 += 1
      for (v <- adj2(u)) {
        if (color2(v) == -1) {
          color2(v) = 1 - color2(u)
          stack2.push(v)
        }
      }
    }

    val maxSecond = math.max(white2, black2)

    // Build answer
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val sameColorCount = if (color1(i) == 0) white1 else black1
      ans(i) = sameColorCount + maxSecond
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> Vec<i32> {
        // Build adjacency lists
        let n = edges1.len() + 1;
        let m = edges2.len() + 1;
        let mut adj1: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges1.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj1[a].push(b);
            adj1[b].push(a);
        }
        let mut adj2: Vec<Vec<usize>> = vec![Vec::new(); m];
        for e in edges2.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj2[a].push(b);
            adj2[b].push(a);
        }

        // BFS to color nodes and count colors
        fn bfs(adj: &Vec<Vec<usize>>) -> (Vec<u8>, usize, usize) {
            let n = adj.len();
            let mut color = vec![2u8; n]; // 0 or 1, 2 = unvisited
            let mut q = VecDeque::new();
            color[0] = 0;
            q.push_back(0usize);
            let mut cnt0 = 1usize;
            let mut cnt1 = 0usize;
            while let Some(u) = q.pop_front() {
                for &v in &adj[u] {
                    if color[v] == 2 {
                        color[v] = 1 - color[u];
                        if color[v] == 0 { cnt0 += 1; } else { cnt1 += 1; }
                        q.push_back(v);
                    }
                }
            }
            (color, cnt0, cnt1)
        }

        let (col1, white1, black1) = bfs(&adj1);
        let (_col2, white2, black2) = bfs(&adj2);
        let best_second = if white2 > black2 { white2 } else { black2 };

        // Build answer
        let mut ans: Vec<i32> = Vec::with_capacity(n);
        for i in 0..n {
            let same_color_cnt = if col1[i] == 0 { white1 } else { black1 };
            ans.push((same_color_cnt + best_second) as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define (build-adj n edges)
  (let ([adj (make-vector n '())])
    (for ([e edges])
      (let* ([a (list-ref e 0)]
             [b (list-ref e 1)])
        (vector-set! adj a (cons b (vector-ref adj a)))
        (vector-set! adj b (cons a (vector-ref adj b)))))
    adj))

(define (color-tree n adj)
  (let ([color (make-vector n -1)]
        [cnt0 0]
        [cnt1 0])
    (let loop ((stack (list (cons 0 0))))
      (when (not (null? stack))
        (let* ([pair (car stack)]
               [node (car pair)]
               [par (cdr pair)]
               [rest (cdr stack)])
          (if (= (vector-ref color node) -1)
              (begin
                (vector-set! color node par)
                (if (= par 0) (set! cnt0 (+ cnt0 1)) (set! cnt1 (+ cnt1 1)))
                (for ([nb (vector-ref adj node)])
                  (when (= (vector-ref color nb) -1)
                    (set! rest (cons (cons nb (if (= par 0) 1 0)) rest))))
                (loop rest))
              (loop rest)))))
    (values color cnt0 cnt1)))

(define/contract (max-target-nodes edges1 edges2)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ([n (+ 1 (length edges1))]
         [m (+ 1 (length edges2))]
         [adj1 (build-adj n edges1)]
         [adj2 (build-adj m edges2)]
         [values1 (color-tree n adj1)]
         [color1 (car values1)]
         [_cnt0_1 (cadr values1)]
         [_cnt1_1 (caddr values1)]
         [values2 (color-tree m adj2)]
         [_cnt0_2 (cadr values2)]
         [_cnt1_2 (caddr values2)]
         [max-odd-second (if (> _cnt0_2 _cnt1_2) _cnt0_2 _cnt1_2)])
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (let* ([par (vector-ref color1 i)]
                 [even-count (if (= par 0) _cnt0_1 _cnt1_1)])
            (loop (+ i 1) (cons (+ even-count max-odd-second) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_target_nodes/2]).

-spec max_target_nodes(Edges1 :: [[integer()]], Edges2 :: [[integer()]]) -> [integer()].
max_target_nodes(Edges1, Edges2) ->
    Adj1 = build_adj(Edges1),
    Adj2 = build_adj(Edges2),

    Colors1 = bfs(:queue.in(0, :queue.new()), #{0 => 0}, Adj1),
    {White1, Black1} = count_colors(Colors1),

    Colors2 = bfs(:queue.in(0, :queue.new()), #{0 => 0}, Adj2),
    {White2, Black2} = count_colors(Colors2),

    MaxSecond = erlang:max(White2, Black2),
    N = maps:size(Colors1),

    lists:map(fun(I) ->
        Color = maps:get(I, Colors1),
        Same = if Color == 0 -> White1; true -> Black1 end,
        Same + MaxSecond
    end, lists:seq(0, N - 1)).

build_adj(Edges) ->
    lists:foldl(fun([A, B], Acc) ->
        Acc1 = maps:update_with(A,
                fun(L) -> [B | L] end,
                [B],
                Acc),
        maps:update_with(B,
                fun(L) -> [A | L] end,
                [A],
                Acc1)
    end, #{}, Edges).

bfs(Queue, Colors, Adj) ->
    case :queue.out(Queue) of
        {empty, _} ->
            Colors;
        {{value, Node}, Q2} ->
            Color = maps:get(Node, Colors),
            Neighs = maps:get(Node, Adj, []),
            {NewQ, NewColors} = add_neighbors(Neighs, Q2, Colors, Color),
            bfs(NewQ, NewColors, Adj)
    end.

add_neighbors([], Queue, Colors, _CurColor) ->
    {Queue, Colors};
add_neighbors([Nb | Rest], Queue, Colors, CurColor) ->
    case maps:is_key(Nb, Colors) of
        true ->
            add_neighbors(Rest, Queue, Colors, CurColor);
        false ->
            UpdatedColors = maps:put(Nb, 1 - CurColor, Colors),
            UpdatedQueue = :queue.in(Nb, Queue),
            add_neighbors(Rest, UpdatedQueue, UpdatedColors, CurColor)
    end.

count_colors(ColorsMap) ->
    maps:fold(fun(_Node, Col, {W, B}) ->
        if
            Col == 0 -> {W + 1, B};
            true -> {W, B + 1}
        end
    end, {0, 0}, ColorsMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_target_nodes(edges1 :: [[integer]], edges2 :: [[integer]]) :: [integer]
  def max_target_nodes(edges1, edges2) do
    n = length(edges1) + 1
    m = length(edges2) + 1

    adj1 = build_adj(n, edges1)
    {color1, w1, b1} = bfs_color(adj1)

    adj2 = build_adj(m, edges2)
    {_color2, w2, b2} = bfs_color(adj2)

    max_second = if w2 > b2, do: w2, else: b2

    Enum.map(0..n - 1, fn i ->
      even_cnt = if Enum.at(color1, i) == 0, do: w1, else: b1
      even_cnt + max_second
    end)
  end

  defp build_adj(size, edges) do
    base = for i <- 0..size - 1, into: %{}, do: {i, []}
    Enum.reduce(edges, base, fn [u, v], acc ->
      acc
      |> Map.update!(u, &[v | &1])
      |> Map.update!(v, &[u | &1])
    end)
  end

  defp bfs_color(adj) do
    n = map_size(adj)
    colors = :array.new(n, default: -1)

    {colors, w, b} =
      Enum.reduce(0..n - 1, {colors, 0, 0}, fn start, {col_arr, wc, bc} ->
        if :array.get(start, col_arr) == -1 do
          dfs_component(start, adj, col_arr, wc, bc)
        else
          {col_arr, wc, bc}
        end
      end)

    color_list = Enum.map(0..n - 1, fn i -> :array.get(i, colors) end)
    {color_list, w, b}
  end

  defp dfs_component(start, adj, colors, wc, bc) do
    stack = [{start, 0}]
    colors = :array.set(start, 0, colors)
    dfs_stack(stack, adj, colors, wc + 1, bc)
  end

  defp dfs_stack([], _adj, colors, wc, bc), do: {colors, wc, bc}

  defp dfs_stack([{node, col} | rest], adj, colors, wc, bc) do
    neighbors = Map.get(adj, node, [])

    {colors2, wc2, bc2, new_stack} =
      Enum.reduce(neighbors, {colors, wc, bc, []}, fn nb,
                                                    {c_arr, wcnt, bcnt, acc} ->
        if :array.get(nb, c_arr) == -1 do
          ncol = 1 - col
          c_arr = :array.set(nb, ncol, c_arr)

          {wcnt, bcnt} =
            if ncol == 0, do: {wcnt + 1, bcnt}, else: {wcnt, bcnt + 1}

          {c_arr, wcnt, bcnt, [{nb, ncol} | acc]}
        else
          {c_arr, wcnt, bcnt, acc}
        end
      end)

    dfs_stack(rest ++ new_stack, adj, colors2, wc2, bc2)
  end
end
```
