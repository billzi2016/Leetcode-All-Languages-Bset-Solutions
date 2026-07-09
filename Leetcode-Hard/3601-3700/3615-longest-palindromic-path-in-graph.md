# 3615. Longest Palindromic Path in Graph

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int Nmask = 1 << n;
        int NN = n * n;
        vector<vector<char>> dp(Nmask, vector<char>(NN, 0));
        auto idx = [&](int l, int r) { return l * n + r; };
        int ans = 1; // at least one node

        // single node start
        for (int i = 0; i < n; ++i) {
            dp[1 << i][idx(i, i)] = 1;
        }

        // pair start with matching labels and an edge between them
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            if (label[u] == label[v]) {
                int m = (1 << u) | (1 << v);
                dp[m][idx(u, v)] = 1;
                ans = max(ans, 2);
            }
        }

        for (int mask = 0; mask < Nmask; ++mask) {
            int curSize = __builtin_popcount(mask);
            if (curSize <= ans) { // still need to explore for larger sizes
                // continue anyway because future expansions may increase size
            }
            for (int l = 0; l < n; ++l) {
                for (int r = 0; r < n; ++r) {
                    if (!dp[mask][idx(l, r)]) continue;
                    ans = max(ans, curSize);
                    // try to add a pair of nodes
                    for (int u : adj[l]) {
                        if (mask & (1 << u)) continue;
                        for (int v : adj[r]) {
                            if (mask & (1 << v)) continue;
                            if (label[u] != label[v]) continue;
                            int nmask = mask | (1 << u) | (1 << v);
                            dp[nmask][idx(u, v)] = 1;
                        }
                    }
                }
            }
        }

        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxLen(int n, int[][] edges, String label) {
        // Build adjacency list
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            graph[u].add(v);
            graph[v].add(u);
        }

        int fullMask = (1 << n) - 1;
        boolean[][][] dp = new boolean[1 << n][n][n];
        int maxLen = 0;

        // Initialize single node palindromes
        for (int i = 0; i < n; ++i) {
            int mask = 1 << i;
            dp[mask][i][i] = true;
            maxLen = Math.max(maxLen, 1);
        }

        // Initialize two-node palindromes where labels match and edge exists
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            if (label.charAt(u) == label.charAt(v)) {
                int mask = (1 << u) | (1 << v);
                dp[mask][u][v] = true;
                dp[mask][v][u] = true;
                maxLen = Math.max(maxLen, 2);
            }
        }

        // DP over masks
        for (int mask = 0; mask <= fullMask; ++mask) {
            for (int l = 0; l < n; ++l) {
                if ((mask & (1 << l)) == 0) continue;
                for (int r = 0; r < n; ++r) {
                    if (!dp[mask][l][r]) continue;

                    int curLen = Integer.bitCount(mask);
                    if (curLen > maxLen) maxLen = curLen;

                    if (l == r) { // center node
                        for (int x : graph[l]) {
                            if ((mask & (1 << x)) != 0) continue;
                            for (int y : graph[l]) {
                                if (y == x) continue;
                                if ((mask & (1 << y)) != 0) continue;
                                if (label.charAt(x) != label.charAt(y)) continue;
                                int newMask = mask | (1 << x) | (1 << y);
                                dp[newMask][x][y] = true;
                            }
                        }
                    } else { // distinct endpoints
                        for (int x : graph[l]) {
                            if ((mask & (1 << x)) != 0) continue;
                            for (int y : graph[r]) {
                                if ((mask & (1 << y)) != 0) continue;
                                if (label.charAt(x) != label.charAt(y)) continue;
                                int newMask = mask | (1 << x) | (1 << y);
                                dp[newMask][x][y] = true;
                            }
                        }
                    }
                }
            }
        }

        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def maxLen(self, n, edges, label):
        """
        :type n: int
        :type edges: List[List[int]]
        :type label: str
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        size = 1 << n
        dp = [[[-1] * n for _ in range(n)] for __ in range(size)]

        # base: single node as center of palindrome
        for i in range(n):
            mask = 1 << i
            dp[mask][i][i] = 1

        # base: two-node path with matching labels
        for u, v in edges:
            if label[u] == label[v]:
                m = (1 << u) | (1 << v)
                dp[m][u][v] = dp[m][v][u] = 2

        ans = 1  # at least one node exists
        for mask in range(size):
            # quick skip if mask has no bits set
            if mask == 0:
                continue
            for l in range(n):
                if not (mask >> l) & 1:
                    continue
                row = dp[mask][l]
                for r in range(n):
                    cur = row[r]
                    if cur < 0:
                        continue
                    # update answer
                    if cur > ans:
                        ans = cur
                    # try to expand with a matching pair (nl, nr)
                    for nl in adj[l]:
                        if (mask >> nl) & 1:
                            continue
                        for nr in adj[r]:
                            if (mask >> nr) & 1 or nl == nr:
                                continue
                            if label[nl] != label[nr]:
                                continue
                            new_mask = mask | (1 << nl) | (1 << nr)
                            if dp[new_mask][nl][nr] < cur + 2:
                                dp[new_mask][nl][nr] = cur + 2

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        size = 1 << n
        dp = [[[-1] * n for _ in range(n)] for __ in range(size)]
        ans = 0

        # single node palindromes
        for i in range(n):
            m = 1 << i
            dp[m][i][i] = 1
            ans = max(ans, 1)

        # two-node palindromes (edges with same label)
        for u, v in edges:
            if label[u] == label[v]:
                m = (1 << u) | (1 << v)
                dp[m][u][v] = dp[m][v][u] = 2
                ans = max(ans, 2)

        # DP over subsets
        for mask in range(size):
            for l in range(n):
                if not (mask >> l) & 1:
                    continue
                row = dp[mask][l]
                for r in range(n):
                    cur = row[r]
                    if cur < 0:
                        continue
                    # expand outward with matching pair
                    for nl in adj[l]:
                        if (mask >> nl) & 1:
                            continue
                        for nr in adj[r]:
                            if (mask >> nr) & 1 or nl == nr:
                                continue
                            if label[nl] != label[nr]:
                                continue
                            new_mask = mask | (1 << nl) | (1 << nr)
                            if dp[new_mask][nl][nr] < cur + 2:
                                dp[new_mask][nl][nr] = cur + 2
                                ans = max(ans, cur + 2)

        return ans
```

## C

```c
#include <stddef.h>
#include <string.h>

static int dp[1 << 14][14][14];
static int adj[14][14];
static int deg[14];

int maxLen(int n, int** edges, int edgesSize, int* edgesColSize, char* label) {
    // Build adjacency list
    for (int i = 0; i < n; ++i) deg[i] = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][deg[u]++] = v;
        adj[v][deg[v]++] = u;
    }

    // Initialize DP
    memset(dp, -1, sizeof(dp));
    int maxAns = 0;

    for (int i = 0; i < n; ++i) {
        int mask = 1 << i;
        dp[mask][i][i] = 1;
        if (maxAns < 1) maxAns = 1;
    }

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        if (label[u] == label[v]) {
            int mask = (1 << u) | (1 << v);
            dp[mask][u][v] = 2;
            dp[mask][v][u] = 2;
            if (maxAns < 2) maxAns = 2;
        }
    }

    int fullMask = 1 << n;
    for (int mask = 0; mask < fullMask; ++mask) {
        for (int l = 0; l < n; ++l) {
            if (!(mask & (1 << l))) continue;
            for (int r = 0; r < n; ++r) {
                if (!(mask & (1 << r))) continue;
                int cur = dp[mask][l][r];
                if (cur == -1) continue;

                // Expand outward
                for (int i = 0; i < deg[l]; ++i) {
                    int nl = adj[l][i];
                    if (mask & (1 << nl)) continue;
                    for (int j = 0; j < deg[r]; ++j) {
                        int nr = adj[r][j];
                        if (mask & (1 << nr)) continue;
                        if (label[nl] != label[nr]) continue;

                        int newMask = mask | (1 << nl) | (1 << nr);
                        if (dp[newMask][nl][nr] < cur + 2) {
                            dp[newMask][nl][nr] = cur + 2;
                            if (maxAns < cur + 2) maxAns = cur + 2;
                        }
                    }
                }
            }
        }
    }

    return maxAns;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxLen(int n, int[][] edges, string label) {
        // Build adjacency list
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int maxMask = 1 << n;
        // dp[mask, l, r] = maximum palindrome length for visited set mask with endpoints l and r
        int[,,] dp = new int[maxMask, n, n];
        int ans = 0;

        // Initialize single node paths
        for (int i = 0; i < n; i++) {
            int m = 1 << i;
            dp[m, i, i] = 1;
            ans = Math.Max(ans, 1);
        }

        // Initialize two-node palindrome paths (edges with matching labels)
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            if (label[u] == label[v]) {
                int m = (1 << u) | (1 << v);
                dp[m, u, v] = Math.Max(dp[m, u, v], 2);
                dp[m, v, u] = Math.Max(dp[m, v, u], 2);
                ans = Math.Max(ans, 2);
            }
        }

        // DP over masks
        for (int mask = 0; mask < maxMask; mask++) {
            for (int l = 0; l < n; l++) {
                for (int r = 0; r < n; r++) {
                    int curLen = dp[mask, l, r];
                    if (curLen == 0) continue;

                    foreach (int nl in adj[l]) {
                        if ((mask & (1 << nl)) != 0) continue;
                        foreach (int nr in adj[r]) {
                            if ((mask & (1 << nr)) != 0) continue;
                            if (nl == nr) continue; // cannot reuse same node
                            if (label[nl] != label[nr]) continue;

                            int newMask = mask | (1 << nl) | (1 << nr);
                            int newLen = curLen + 2;
                            if (dp[newMask, nl, nr] < newLen) {
                                dp[newMask, nl, nr] = newLen;
                                ans = Math.Max(ans, newLen);
                            }
                        }
                    }
                }
            }
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
 * @param {string} label
 * @return {number}
 */
var maxLen = function(n, edges, label) {
    const N = n;
    const adj = Array.from({length: N}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const totalMask = 1 << N;
    const dp = new Array(totalMask);
    const idx = (l, r) => l * N + r;

    // initialize dp arrays
    for (let mask = 0; mask < totalMask; ++mask) {
        dp[mask] = new Int16Array(N * N);
        dp[mask].fill(-1);
    }

    // single node centers
    for (let i = 0; i < N; ++i) {
        const m = 1 << i;
        dp[m][idx(i, i)] = 1;
    }
    // pair starts where labels match and edge exists
    for (const [u, v] of edges) {
        if (label.charCodeAt(u) === label.charCodeAt(v)) {
            const m = (1 << u) | (1 << v);
            dp[m][idx(u, v)] = 2;
            dp[m][idx(v, u)] = 2;
        }
    }

    // DP over masks
    for (let mask = 0; mask < totalMask; ++mask) {
        const curArr = dp[mask];
        for (let l = 0; l < N; ++l) {
            for (let r = 0; r < N; ++r) {
                const curVal = curArr[idx(l, r)];
                if (curVal < 0) continue;
                // try to expand outward with a matching pair
                for (const nl of adj[l]) {
                    if (mask & (1 << nl)) continue;
                    for (const nr of adj[r]) {
                        if (mask & (1 << nr)) continue;
                        if (label.charCodeAt(nl) !== label.charCodeAt(nr)) continue;
                        const newMask = mask | (1 << nl) | (1 << nr);
                        const nxtArr = dp[newMask];
                        const pos = idx(nl, nr);
                        const cand = curVal + 2;
                        if (nxtArr[pos] < cand) {
                            nxtArr[pos] = cand;
                        }
                    }
                }
            }
        }
    }

    // find maximum length
    let ans = 0;
    for (let mask = 0; mask < totalMask; ++mask) {
        const arr = dp[mask];
        for (let i = 0; i < N * N; ++i) {
            if (arr[i] > ans) ans = arr[i];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxLen(n: number, edges: number[][], label: string): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const fullMask = 1 << n;
    // dp[mask][l][r] = max palindrome length using nodes in mask with endpoints l and r
    const dp: Uint8Array[][][] = new Array(fullMask);
    for (let mask = 0; mask < fullMask; ++mask) {
        const mat: Uint8Array[][] = new Array(n);
        for (let i = 0; i < n; ++i) {
            mat[i] = new Uint8Array(n); // initialized to 0 (unreachable)
        }
        dp[mask] = mat;
    }

    let ans = 1;

    // single node palindromes
    for (let i = 0; i < n; ++i) {
        const m = 1 << i;
        dp[m][i][i] = Uint8Array.from([1]);
        ans = Math.max(ans, 1);
    }

    // two-node palindromes (edges with same label)
    for (const [u, v] of edges) {
        if (label.charCodeAt(u) === label.charCodeAt(v)) {
            const m = (1 << u) | (1 << v);
            dp[m][u][v][0] = 2;
            dp[m][v][u][0] = 2;
            ans = Math.max(ans, 2);
        }
    }

    for (let mask = 0; mask < fullMask; ++mask) {
        const mat = dp[mask];
        for (let l = 0; l < n; ++l) {
            const row = mat[l];
            for (let r = 0; r < n; ++r) {
                const cur = row[r];
                if (cur === 0) continue;
                // try to extend on both sides
                for (const nl of adj[l]) {
                    if (mask & (1 << nl)) continue;
                    for (const nr of adj[r]) {
                        if (mask & (1 << nr)) continue;
                        if (nl === nr) continue; // cannot reuse same node
                        if (label.charCodeAt(nl) !== label.charCodeAt(nr)) continue;
                        const newMask = mask | (1 << nl) | (1 << nr);
                        const targetRow = dp[newMask][nl];
                        if (targetRow[nr] < cur + 2) {
                            targetRow[nr] = cur + 2;
                            if (cur + 2 > ans) ans = cur + 2;
                        }
                    }
                }
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $label
     * @return Integer
     */
    function maxLen($n, $edges, $label) {
        // adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $maxMask = 1 << $n;
        $dp = array_fill(0, $maxMask, null);
        $ans = 0;

        // base: single node
        for ($i = 0; $i < $n; $i++) {
            $mask = 1 << $i;
            if (!isset($dp[$mask])) $dp[$mask] = [];
            $dp[$mask][$i][$i] = 1;
            $ans = max($ans, 1);
        }

        // base: edge with same label
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            if ($label[$u] === $label[$v]) {
                $mask = (1 << $u) | (1 << $v);
                if (!isset($dp[$mask])) $dp[$mask] = [];
                // u -> v
                if (!isset($dp[$mask][$u][$v]) || $dp[$mask][$u][$v] < 2) {
                    $dp[$mask][$u][$v] = 2;
                }
                // v -> u
                if (!isset($dp[$mask][$v][$u]) || $dp[$mask][$v][$u] < 2) {
                    $dp[$mask][$v][$u] = 2;
                }
                $ans = max($ans, 2);
            }
        }

        // DP over masks
        for ($mask = 0; $mask < $maxMask; $mask++) {
            if (!isset($dp[$mask])) continue;
            foreach ($dp[$mask] as $l => $arrR) {
                foreach ($arrR as $r => $len) {
                    // expand from both ends
                    foreach ($adj[$l] as $nl) {
                        if ($mask & (1 << $nl)) continue; // already used
                        foreach ($adj[$r] as $nr) {
                            if ($mask & (1 << $nr)) continue;
                            if ($label[$nl] !== $label[$nr]) continue;
                            $newMask = $mask | (1 << $nl) | (1 << $nr);
                            $newLen = $len + 2;
                            if (!isset($dp[$newMask])) $dp[$newMask] = [];
                            if (!isset($dp[$newMask][$nl][$nr]) || $dp[$newMask][$nl][$nr] < $newLen) {
                                $dp[$newMask][$nl][$nr] = $newLen;
                                if ($newLen > $ans) $ans = $newLen;
                            }
                        }
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxLen(_ n: Int, _ edges: [[Int]], _ label: String) -> Int {
        let labels = Array(label.utf8)
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        let maxMask = 1 << n
        let totalSize = maxMask * n * n
        var dp = [UInt8](repeating: 0, count: totalSize)
        @inline(__always) func idx(_ mask: Int, _ u: Int, _ v: Int) -> Int {
            return (mask * n + u) * n + v
        }
        var answer = 1
        // single node paths
        for i in 0..<n {
            let m = 1 << i
            dp[idx(m, i, i)] = 1
        }
        // two-node palindrome paths
        for e in edges {
            let u = e[0], v = e[1]
            if labels[u] == labels[v] {
                let m = (1 << u) | (1 << v)
                dp[idx(m, u, v)] = 1
                dp[idx(m, v, u)] = 1
                answer = max(answer, 2)
            }
        }
        // DP over masks
        for mask in 0..<maxMask {
            for u in 0..<n {
                let baseU = (mask * n + u) * n
                for v in 0..<n {
                    if dp[baseU + v] == 0 { continue }
                    // expand by adding a pair (a,b)
                    for a in adj[u] where ((mask >> a) & 1) == 0 {
                        for b in adj[v] where ((mask >> b) & 1) == 0 {
                            if labels[a] != labels[b] { continue }
                            let newMask = mask | (1 << a) | (1 << b)
                            let newIdx = idx(newMask, a, b)
                            if dp[newIdx] == 0 {
                                dp[newIdx] = 1
                                let len = newMask.nonzeroBitCount
                                if len > answer { answer = len }
                            }
                        }
                    }
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxLen(n: Int, edges: Array<IntArray>, label: String): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }
        val size = 1 shl n
        val dp = Array(size) { Array(n) { IntArray(n) { -1 } } }
        var ans = 0

        // single node paths
        for (i in 0 until n) {
            val mask = 1 shl i
            dp[mask][i][i] = 1
            if (ans < 1) ans = 1
        }

        // two-node palindrome paths (edges with matching labels)
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            if (label[u] == label[v]) {
                val mask = (1 shl u) or (1 shl v)
                dp[mask][u][v] = maxOf(dp[mask][u][v], 2)
                dp[mask][v][u] = maxOf(dp[mask][v][u], 2)
                if (ans < 2) ans = 2
            }
        }

        // DP over subsets
        for (mask in 0 until size) {
            for (l in 0 until n) {
                for (r in 0 until n) {
                    val cur = dp[mask][l][r]
                    if (cur < 0) continue
                    for (nl in adj[l]) {
                        if ((mask and (1 shl nl)) != 0) continue
                        for (nr in adj[r]) {
                            if ((mask and (1 shl nr)) != 0) continue
                            if (label[nl] != label[nr]) continue
                            val newMask = mask or (1 shl nl) or (1 shl nr)
                            if (dp[newMask][nl][nr] < cur + 2) {
                                dp[newMask][nl][nr] = cur + 2
                                if (ans < cur + 2) ans = cur + 2
                            }
                        }
                    }
                }
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxLen(int n, List<List<int>> edges, String label) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    int totalMask = 1 << n;
    // dp[mask][l * n + r] = max palindrome length with visited set mask,
    // left endpoint l, right endpoint r.
    List<List<int>> dp = List.generate(totalMask, (_) => List.filled(n * n, 0));

    // Base: single node paths (length 1)
    for (int i = 0; i < n; ++i) {
      int mask = 1 << i;
      dp[mask][i * n + i] = 1;
    }

    // Base: two-node palindrome if labels match and edge exists
    for (var e in edges) {
      int u = e[0], v = e[1];
      if (label.codeUnitAt(u) == label.codeUnitAt(v)) {
        int mask = (1 << u) | (1 << v);
        dp[mask][u * n + v] = 2;
        dp[mask][v * n + u] = 2;
      }
    }

    int answer = 1; // at least one node

    for (int mask = 0; mask < totalMask; ++mask) {
      for (int l = 0; l < n; ++l) {
        if ((mask & (1 << l)) == 0) continue;
        for (int r = 0; r < n; ++r) {
          if ((mask & (1 << r)) == 0) continue;
          int cur = dp[mask][l * n + r];
          if (cur == 0) continue;
          if (cur > answer) answer = cur;

          // Try to extend by adding a matching pair (nl, nr)
          for (int nl in adj[l]) {
            if ((mask & (1 << nl)) != 0) continue; // already visited
            for (int nr in adj[r]) {
              if ((mask & (1 << nr)) != 0) continue;
              if (label.codeUnitAt(nl) != label.codeUnitAt(nr)) continue;

              int newMask = mask | (1 << nl) | (1 << nr);
              int idx = nl * n + nr;
              int cand = cur + 2;
              if (cand > dp[newMask][idx]) {
                dp[newMask][idx] = cand;
              }
            }
          }
        }
      }
    }

    return answer;
  }
}
```

## Golang

```go
import "math/bits"

func maxLen(n int, edges [][]int, label string) int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	maxMask := 1 << n
	dp := make([][][]bool, maxMask)
	for m := 0; m < maxMask; m++ {
		dp[m] = make([][]bool, n)
		for i := 0; i < n; i++ {
			dp[m][i] = make([]bool, n)
		}
	}

	// single node paths
	for i := 0; i < n; i++ {
		mask := 1 << i
		dp[mask][i][i] = true
	}

	// two-node palindrome paths
	for _, e := range edges {
		u, v := e[0], e[1]
		if label[u] == label[v] {
			mask := (1 << u) | (1 << v)
			dp[mask][u][v] = true
			dp[mask][v][u] = true
		}
	}

	// expand palindromes by adding matching pairs on both ends
	for mask := 0; mask < maxMask; mask++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if !dp[mask][i][j] {
					continue
				}
				for _, x := range adj[i] {
					if mask&(1<<x) != 0 {
						continue
					}
					for _, y := range adj[j] {
						if mask&(1<<y) != 0 {
							continue
						}
						if label[x] != label[y] {
							continue
						}
						newMask := mask | (1 << x) | (1 << y)
						dp[newMask][x][y] = true
					}
				}
			}
		}
	}

	ans := 0
	for mask := 0; mask < maxMask; mask++ {
		cnt := bits.OnesCount(uint(mask))
		if cnt <= ans {
			continue
		}
		found := false
		for i := 0; i < n && !found; i++ {
			for j := 0; j < n; j++ {
				if dp[mask][i][j] {
					found = true
					break
				}
			}
		}
		if found {
			ans = cnt
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_len(n, edges, label)
  lbl = label.chars
  neighbors = Array.new(n) { [] }
  edges.each do |u, v|
    neighbors[u] << v
    neighbors[v] << u
  end

  total_masks = 1 << n
  dp = Array.new(total_masks) { Array.new(n) { Array.new(n, -1) } }

  max_len = 0

  # single node paths
  (0...n).each do |i|
    mask = 1 << i
    dp[mask][i][i] = 1
    max_len = 1
  end

  # two-node palindrome paths
  edges.each do |u, v|
    next unless lbl[u] == lbl[v]
    mask = (1 << u) | (1 << v)
    dp[mask][u][v] = 2
    dp[mask][v][u] = 2
    max_len = 2 if max_len < 2
  end

  (0...total_masks).each do |mask|
    (0...n).each do |l|
      (0...n).each do |r|
        cur = dp[mask][l][r]
        next if cur < 0
        neighbors[l].each do |nl|
          next if (mask >> nl) & 1 == 1
          neighbors[r].each do |nr|
            next if (mask >> nr) & 1 == 1
            next unless lbl[nl] == lbl[nr]
            new_mask = mask | (1 << nl) | (1 << nr)
            if dp[new_mask][nl][nr] < cur + 2
              dp[new_mask][nl][nr] = cur + 2
              max_len = cur + 2 if max_len < cur + 2
            end
          end
        end
      end
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def maxLen(n: Int, edges: Array[Array[Int]], label: String): Int = {
        val maxMask = 1 << n
        // dp(mask)(l)(r) = max palindrome length using nodes in mask with endpoints l and r
        val dp = Array.ofDim[Int](maxMask, n, n)
        var ans = 0

        // initialize to -1
        for (mask <- 0 until maxMask; i <- 0 until n; j <- 0 until n) {
            dp(mask)(i)(j) = -1
        }

        // adjacency list
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }
        val adjArr = adj.map(_.toArray)

        // base cases: single node
        for (i <- 0 until n) {
            val m = 1 << i
            dp(m)(i)(i) = 1
            ans = math.max(ans, 1)
        }

        // base cases: edge with matching labels -> length 2
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            if (label.charAt(u) == label.charAt(v)) {
                val m = (1 << u) | (1 << v)
                dp(m)(u)(v) = 2
                dp(m)(v)(u) = 2
                ans = math.max(ans, 2)
            }
        }

        // DP over masks
        for (mask <- 0 until maxMask) {
            for (l <- 0 until n) {
                for (r <- 0 until n) {
                    val cur = dp(mask)(l)(r)
                    if (cur > 0) {
                        // try to extend on both sides
                        for (nl <- adjArr(l)) {
                            if ((mask & (1 << nl)) == 0) {
                                for (nr <- adjArr(r)) {
                                    if ((mask & (1 << nr)) == 0 && label.charAt(nl) == label.charAt(nr)) {
                                        val newMask = mask | (1 << nl) | (1 << nr)
                                        val newLen = cur + 2
                                        if (dp(newMask)(nl)(nr) < newLen) {
                                            dp(newMask)(nl)(nr) = newLen
                                            ans = math.max(ans, newLen)
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_len(n: i32, edges: Vec<Vec<i32>>, label: String) -> i32 {
        let n = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }
        let lbl = label.as_bytes();

        let total_masks = 1usize << n;
        let total_states = total_masks * n * n;
        // dp value: -128 means unreachable, otherwise length (max 14)
        let mut dp: Vec<i8> = vec![-128; total_states];

        // helper to compute index
        let idx = |mask: usize, l: usize, r: usize| -> usize { (mask * n + l) * n + r };

        // initialize single node centers
        for i in 0..n {
            let m = 1usize << i;
            dp[idx(m, i, i)] = 1;
        }
        // initialize two-node palindromes where labels match and edge exists
        for u in 0..n {
            for &v in &adj[u] {
                if lbl[u] == lbl[v] {
                    let m = (1usize << u) | (1usize << v);
                    let i1 = idx(m, u, v);
                    if dp[i1] < 2 { dp[i1] = 2; }
                    let i2 = idx(m, v, u);
                    if dp[i2] < 2 { dp[i2] = 2; }
                }
            }
        }

        // DP over masks
        for mask in 0..total_masks {
            for l in 0..n {
                if (mask >> l) & 1 == 0 { continue; }
                for r in 0..n {
                    if (mask >> r) & 1 == 0 { continue; }
                    let cur_idx = idx(mask, l, r);
                    let cur_val = dp[cur_idx];
                    if cur_val < 0 { continue; }

                    // try to add a matching pair (nl, nr)
                    for &nl in &adj[l] {
                        if (mask >> nl) & 1 == 1 { continue; }
                        for &nr in &adj[r] {
                            if (mask >> nr) & 1 == 1 { continue; }
                            if nl == nr { continue; } // must be distinct nodes
                            if lbl[nl] != lbl[nr] { continue; }
                            let new_mask = mask | (1usize << nl) | (1usize << nr);
                            let new_idx = idx(new_mask, nl, nr);
                            let cand = cur_val + 2;
                            if dp[new_idx] < cand {
                                dp[new_idx] = cand;
                            }
                        }
                    }
                }
            }
        }

        // find maximum length
        let mut ans: i32 = 0;
        for &v in dp.iter() {
            if v > 0 && (v as i32) > ans {
                ans = v as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-len n edges label)
  (-> exact-integer? (listof (listof exact-integer?)) string? exact-integer?)
  (let* ((adj (make-vector n 0))
         (set-edge
          (lambda (u v)
            (vector-set! adj u (bitwise-ior (vector-ref adj u) (arithmetic-shift 1 v)))
            (vector-set! adj v (bitwise-ior (vector-ref adj v) (arithmetic-shift 1 u)))))
         )
    ;; build adjacency bitmasks
    (for-each (lambda (e) (set-edge (first e) (second e))) edges)

    (define total-mask (arithmetic-shift 1 n))

    ;; dp[mask][l][r] = #t if a palindrome path using exactly nodes in mask
    ;; with left endpoint l and right endpoint r exists.
    (define dp (make-vector total-mask))
    (for ([mask (in-range total-mask)])
      (define rows (make-vector n))
      (for ([i n]) (vector-set! rows i (make-vector n #f)))
      (vector-set! dp mask rows))

    (define (set-state mask l r)
      (let ((rows (vector-ref dp mask)))
        (unless (vector-ref (vector-ref rows l) r)
          (vector-set! (vector-ref rows l) r #t))))

    ;; initialize single-node states
    (for ([i n])
      (set-state (arithmetic-shift 1 i) i i))

    ;; initialize two-node palindrome states (edge with equal labels)
    (for ([e edges])
      (let* ((u (first e)) (v (second e)))
        (when (char=? (string-ref label u) (string-ref label v))
          (set-state (bitwise-ior (arithmetic-shift 1 u) (arithmetic-shift 1 v)) u v))))

    ;; DP transitions: add a matching pair on both ends
    (for ([mask (in-range total-mask)])
      (define rows (vector-ref dp mask))
      (for ([l n])
        (define colvec (vector-ref rows l))
        (for ([r n])
          (when (vector-ref colvec r)
            ;; try to extend with nl adjacent to l and nr adjacent to r
            (for ([nl n])
              (let ((bit-nl (arithmetic-shift 1 nl)))
                (when (and (= (bitwise-and bit-nl mask) 0)
                           (> (bitwise-and (vector-ref adj l) bit-nl) 0))
                  (define c (string-ref label nl))
                  (for ([nr n])
                    (let ((bit-nr (arithmetic-shift 1 nr)))
                      (when (and (= (bitwise-and bit-nr mask) 0)
                                 (> (bitwise-and (vector-ref adj r) bit-nr) 0)
                                 (char=? c (string-ref label nr)))
                        (define new-mask (bitwise-ior mask bit-nl bit-nr))
                        (set-state new-mask nl nr))))))))))
    ;; compute answer
    (define ans 0)
    (for ([mask (in-range total-mask)])
      (define rows (vector-ref dp mask))
      (for ([l n])
        (define colvec (vector-ref rows l))
        (for ([r n])
          (when (vector-ref colvec r)
            (set! ans (max ans (bitwise-bit-count mask)))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_len/3]).

max_len(N, Edges, Label) ->
    Adj0 = erlang:list_to_tuple(lists:duplicate(N, [])),
    AdjTuple = lists:foldl(fun([U, V], Acc) ->
        L1 = element(U + 1, Acc),
        Acc1 = setelement(U + 1, Acc, [V | L1]),
        L2 = element(V + 1, Acc1),
        setelement(V + 1, Acc1, [U | L2])
    end, Adj0, Edges),

    LabelTuple = erlang:list_to_tuple(binary_to_list(Label)),

    {SeenInit, QueueInit} = init_states(N, Edges, AdjTuple, LabelTuple),

    loop(QueueInit, SeenInit, 1, AdjTuple, LabelTuple).

init_states(N, Edges, _AdjTuple, LabelTuple) ->
    Seen0 = #{},
    Queue0 = queue:new(),
    {Seen1, Queue1} =
        lists:foldl(fun(I, {S, Q}) ->
            Mask = 1 bsl I,
            State = {Mask, I, I},
            S2 = maps:put(State, true, S),
            Q2 = queue:in(State, Q),
            {S2, Q2}
        end, {Seen0, Queue0}, lists:seq(0, N - 1)),

    {SeenFinal, QueueFinal} =
        lists:foldl(fun([U, V], {S, Q}) ->
            CharU = element(U + 1, LabelTuple),
            CharV = element(V + 1, LabelTuple),
            if
                CharU == CharV ->
                    Mask = (1 bsl U) bor (1 bsl V),
                    StateUV = {Mask, U, V},
                    StateVU = {Mask, V, U},
                    {S2, Q2} = maybe_add(StateUV, S, Q),
                    {S3, Q3} = maybe_add(StateVU, S2, Q2),
                    {S3, Q3};
                true ->
                    {S, Q}
            end
        end, {Seen1, Queue1}, Edges),

    {SeenFinal, QueueFinal}.

maybe_add(State, Seen, Queue) ->
    case maps:is_key(State, Seen) of
        true -> {Seen, Queue};
        false -> {maps:put(State, true, Seen), queue:in(State, Queue)}
    end.

loop(Queue, Seen, Max, AdjTuple, LabelTuple) ->
    case queue:out(Queue) of
        {empty, _} ->
            Max;
        {{value, State = {Mask, L, R}}, Q2} ->
            Len = popcount(Mask),
            Max1 = if Len > Max -> Len; true -> Max end,
            NeighL = element(L + 1, AdjTuple),
            NeighR = element(R + 1, AdjTuple),

            NewStates =
                [ {Mask bor (1 bsl X) bor (1 bsl Y), X, Y}
                  || X <- NeighL,
                     ((Mask band (1 bsl X)) == 0),
                     Y <- NeighR,
                     ((Mask band (1 bsl Y)) == 0),
                     X =/= Y,
                     element(X + 1, LabelTuple) == element(Y + 1, LabelTuple)
                ],

            {Seen2, Q3} =
                lists:foldl(fun(NewState = {NewMask, _, _}, {SAcc, QAcc}) ->
                    case maps:is_key(NewState, SAcc) of
                        true -> {SAcc, QAcc};
                        false ->
                            {maps:put(NewState, true, SAcc), queue:in(NewState, QAcc)}
                    end
                end, {Seen, Q2}, NewStates),

            loop(Q3, Seen2, Max1, AdjTuple, LabelTuple)
    end.

popcount(0) -> 0;
popcount(N) ->
    1 + popcount(N band (N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_len(n :: integer, edges :: [[integer]], label :: String.t) :: integer
  def max_len(n, edges, label) do
    labels = String.to_charlist(label)

    # Build neighbor lists for each node
    neighbor_lists =
      for i <- 0..(n - 1) do
        Enum.reduce(edges, [], fn [u, v], acc ->
          cond do
            u == i -> [v | acc]
            v == i -> [u | acc]
            true -> acc
          end
        end)
      end

    # Initialize DP with single nodes
    dp =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        mask = 1 <<< i
        Map.put(acc, {mask, i, i}, 1)
      end)

    # Add two-node palindromes (edges with same label)
    dp =
      Enum.reduce(edges, dp, fn [u, v], acc ->
        if Enum.at(labels, u) == Enum.at(labels, v) do
          mask = (1 <<< u) ||| (1 <<< v)
          acc
          |> Map.update({mask, u, v}, 2, &max(&1, 2))
          |> Map.update({mask, v, u}, 2, &max(&1, 2))
        else
          acc
        end
      end)

    max_mask = 1 <<< n

    dp =
      Enum.reduce(0..(max_mask - 1), dp, fn mask, cur_dp ->
        # Extract states for current mask
        states =
          for {{m, l, r}, len} <- Map.to_list(cur_dp), m == mask do
            {l, r, len}
          end

        if states == [] do
          cur_dp
        else
          new_entries =
            for {l, r, len} <- states,
                nl <- Enum.at(neighbor_lists, l),
                nr <- Enum.at(neighbor_lists, r) do
              bit_nl = 1 <<< nl
              bit_nr = 1 <<< nr

              cond do
                (mask &&& bit_nl) != 0 -> nil
                (mask &&& bit_nr) != 0 -> nil
                Enum.at(labels, nl) != Enum.at(labels, nr) -> nil
                true ->
                  new_mask = mask ||| bit_nl ||| bit_nr
                  {new_mask, nl, nr, len + 2}
              end
            end
            |> Enum.filter(& &1)

          Enum.reduce(new_entries, cur_dp, fn {nm, l, r, new_len}, acc ->
            key = {nm, l, r}
            old = Map.get(acc, key, 0)
            if new_len > old, do: Map.put(acc, key, new_len), else: acc
          end)
        end
      end)

    dp
    |> Enum.map(fn {_k, v} -> v end)
    |> Enum.max()
  end
end
```
