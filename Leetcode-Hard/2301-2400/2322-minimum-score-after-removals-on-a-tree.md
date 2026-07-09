# 2322. Minimum Score After Removals on a Tree

## Cpp

```cpp
class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> tin(n), tout(n), subXor(n);
        int timer = 0;
        function<void(int,int)> dfs = [&](int u, int p){
            tin[u] = timer++;
            subXor[u] = nums[u];
            for (int v : adj[u]) {
                if (v == p) continue;
                dfs(v, u);
                subXor[u] ^= subXor[v];
            }
            tout[u] = timer;
        };
        dfs(0, -1);
        int total = subXor[0];
        auto isAnc = [&](int a, int b)->bool{
            return tin[a] <= tin[b] && tout[b] <= tout[a];
        };
        int ans = INT_MAX;
        for (int u = 1; u < n; ++u) {
            for (int v = u + 1; v < n; ++v) {
                if (v == 0) continue;
                int part1, part2, part3;
                if (isAnc(u, v)) {
                    part1 = total ^ subXor[u];
                    part2 = subXor[u] ^ subXor[v];
                    part3 = subXor[v];
                } else if (isAnc(v, u)) {
                    part1 = total ^ subXor[v];
                    part2 = subXor[v] ^ subXor[u];
                    part3 = subXor[u];
                } else {
                    part1 = total ^ subXor[u] ^ subXor[v];
                    part2 = subXor[u];
                    part3 = subXor[v];
                }
                int mx = max({part1, part2, part3});
                int mn = min({part1, part2, part3});
                ans = min(ans, mx - mn);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int timer;
    private int[] in;
    private int[] out;
    private int[] subXor;
    private int[] parent;

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            adj[a].add(b);
            adj[b].add(a);
        }
        in = new int[n];
        out = new int[n];
        subXor = new int[n];
        parent = new int[n];
        timer = 0;
        dfs(0, -1, nums, adj);
        int totalXor = subXor[0];
        int answer = Integer.MAX_VALUE;

        for (int u = 1; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int part1, part2, part3;
                if (isAncestor(u, v)) { // u ancestor of v
                    part1 = totalXor ^ subXor[u];
                    part2 = subXor[u] ^ subXor[v];
                    part3 = subXor[v];
                } else if (isAncestor(v, u)) { // v ancestor of u
                    part1 = totalXor ^ subXor[v];
                    part2 = subXor[v] ^ subXor[u];
                    part3 = subXor[u];
                } else {
                    part1 = totalXor ^ subXor[u] ^ subXor[v];
                    part2 = subXor[u];
                    part3 = subXor[v];
                }
                int max = Math.max(part1, Math.max(part2, part3));
                int min = Math.min(part1, Math.min(part2, part3));
                answer = Math.min(answer, max - min);
            }
        }
        return answer;
    }

    private void dfs(int node, int par, int[] nums, List<Integer>[] adj) {
        parent[node] = par;
        in[node] = timer++;
        int curXor = nums[node];
        for (int nb : adj[node]) {
            if (nb == par) continue;
            dfs(nb, node, nums, adj);
            curXor ^= subXor[nb];
        }
        subXor[node] = curXor;
        out[node] = timer;
    }

    private boolean isAncestor(int anc, int desc) {
        return in[anc] <= in[desc] && out[desc] <= out[anc];
    }
}
```

## Python

```python
class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10000)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        subxor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p):
            nonlocal timer
            parent[u] = p
            tin[u] = timer
            timer += 1
            cur = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                cur ^= dfs(v, u)
            subxor[u] = cur
            tout[u] = timer
            return cur

        total = dfs(0, -1)

        ans = float('inf')
        for u in range(1, n):
            for v in range(u + 1, n):
                # determine relationship
                if tin[u] <= tin[v] and tout[v] <= tout[u]:
                    # u ancestor of v
                    a = total ^ subxor[u]
                    b = subxor[u] ^ subxor[v]
                    c = subxor[v]
                elif tin[v] <= tin[u] and tout[u] <= tout[v]:
                    # v ancestor of u
                    a = total ^ subxor[v]
                    b = subxor[v] ^ subxor[u]
                    c = subxor[u]
                else:
                    # independent
                    a = total ^ subxor[u] ^ subxor[v]
                    b = subxor[u]
                    c = subxor[v]
                cur_score = max(a, b, c) - min(a, b, c)
                if cur_score < ans:
                    ans = cur_score
        return ans
```

## Python3

```python
class Solution:
    def minimumScore(self, nums, edges):
        from collections import defaultdict
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        subxor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p):
            nonlocal timer
            parent[u] = p
            tin[u] = timer
            timer += 1
            cur = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                cur ^= dfs(v, u)
            subxor[u] = cur
            tout[u] = timer
            return cur

        total_xor = dfs(0, -1)

        def is_ancestor(a, b):
            # a ancestor of b (including self)
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        ans = float('inf')
        # consider all pairs of non-root nodes
        for u in range(1, n):
            for v in range(u + 1, n):
                if is_ancestor(u, v):
                    part1 = total_xor ^ subxor[u]
                    part2 = subxor[u] ^ subxor[v]
                    part3 = subxor[v]
                elif is_ancestor(v, u):
                    part1 = total_xor ^ subxor[v]
                    part2 = subxor[v] ^ subxor[u]
                    part3 = subxor[u]
                else:
                    part1 = total_xor ^ subxor[u] ^ subxor[v]
                    part2 = subxor[u]
                    part3 = subxor[v]

                cur_score = max(part1, part2, part3) - min(part1, part2, part3)
                if cur_score < ans:
                    ans = cur_score
        return ans
```

## C

```c
#include <limits.h>
#include <stdlib.h>

struct Edge {
    int to;
    int next;
};

static int n;
static int *numsArr;
static int *head;
static struct Edge *edgesList;
static int edgeCnt;

static int *parentArr;
static int *tinArr;
static int *toutArr;
static int *subxorArr;
static int timerVal;

static void addEdge(int u, int v) {
    edgesList[edgeCnt].to = v;
    edgesList[edgeCnt].next = head[u];
    head[u] = edgeCnt++;
}

static void dfs(int u, int p) {
    parentArr[u] = p;
    tinArr[u] = timerVal++;
    subxorArr[u] = numsArr[u];
    for (int i = head[u]; i != -1; i = edgesList[i].next) {
        int v = edgesList[i].to;
        if (v == p) continue;
        dfs(v, u);
        subxorArr[u] ^= subxorArr[v];
    }
    toutArr[u] = timerVal;
}

static inline int isAncestor(int a, int b) {
    return tinArr[a] <= tinArr[b] && toutArr[b] <= toutArr[a];
}

int minimumScore(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize){
    n = numsSize;
    numsArr = nums;

    head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    edgesList = (struct Edge*)malloc(2 * edgesSize * sizeof(struct Edge));
    edgeCnt = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        addEdge(u, v);
        addEdge(v, u);
    }

    parentArr = (int*)malloc(n * sizeof(int));
    tinArr = (int*)malloc(n * sizeof(int));
    toutArr = (int*)malloc(n * sizeof(int));
    subxorArr = (int*)malloc(n * sizeof(int));
    timerVal = 0;

    dfs(0, -1);
    int totalXor = subxorArr[0];
    int answer = INT_MAX;

    for (int u = 1; u < n; ++u) {
        for (int v = u + 1; v < n; ++v) {
            int part1, part2, part3;
            if (isAncestor(u, v)) {
                part1 = totalXor ^ subxorArr[u];
                part2 = subxorArr[u] ^ subxorArr[v];
                part3 = subxorArr[v];
            } else if (isAncestor(v, u)) {
                part1 = totalXor ^ subxorArr[v];
                part2 = subxorArr[v] ^ subxorArr[u];
                part3 = subxorArr[u];
            } else {
                part1 = totalXor ^ subxorArr[u] ^ subxorArr[v];
                part2 = subxorArr[u];
                part3 = subxorArr[v];
            }
            int mx = part1, mn = part1;
            if (part2 > mx) mx = part2;
            if (part3 > mx) mx = part3;
            if (part2 < mn) mn = part2;
            if (part3 < mn) mn = part3;
            int diff = mx - mn;
            if (diff < answer) answer = diff;
        }
    }

    free(head);
    free(edgesList);
    free(parentArr);
    free(tinArr);
    free(toutArr);
    free(subxorArr);

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumScore(int[] nums, int[][] edges) {
        int n = nums.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        int[] tin = new int[n];
        int[] tout = new int[n];
        int[] subXor = new int[n];
        int timer = 0;

        void Dfs(int u, int parent) {
            tin[u] = ++timer;
            int cur = nums[u];
            foreach (int v in graph[u]) {
                if (v == parent) continue;
                Dfs(v, u);
                cur ^= subXor[v];
            }
            subXor[u] = cur;
            tout[u] = timer;
        }

        Dfs(0, -1);
        int totalXor = subXor[0];
        int answer = int.MaxValue;

        for (int u = 1; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int partA, partB, partC;
                bool uAncV = tin[u] < tin[v] && tout[v] <= tout[u];
                bool vAncU = tin[v] < tin[u] && tout[u] <= tout[v];

                if (uAncV) {
                    partA = totalXor ^ subXor[u];
                    partB = subXor[u] ^ subXor[v];
                    partC = subXor[v];
                } else if (vAncU) {
                    partA = totalXor ^ subXor[v];
                    partB = subXor[v] ^ subXor[u];
                    partC = subXor[u];
                } else {
                    partA = totalXor ^ subXor[u] ^ subXor[v];
                    partB = subXor[u];
                    partC = subXor[v];
                }

                int maxVal = Math.Max(partA, Math.Max(partB, partC));
                int minVal = Math.Min(partA, Math.Min(partB, partC));
                answer = Math.Min(answer, maxVal - minVal);
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
var minimumScore = function(nums, edges) {
    const n = nums.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const parent = new Array(n).fill(-1);
    const inTime = new Array(n);
    const outTime = new Array(n);
    const subXor = new Array(n);
    let timer = 0;
    function dfs(u, p) {
        parent[u] = p;
        inTime[u] = timer++;
        let cur = nums[u];
        for (const v of adj[u]) {
            if (v === p) continue;
            dfs(v, u);
            cur ^= subXor[v];
        }
        subXor[u] = cur;
        outTime[u] = timer;
    }
    dfs(0, -1);
    const total = subXor[0];
    let ans = Infinity;
    function isAncestor(a, b) {
        return inTime[a] < inTime[b] && outTime[b] <= outTime[a];
    }
    for (let i = 1; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let a, b, c;
            if (isAncestor(i, j)) {
                a = total ^ subXor[i];
                b = subXor[i] ^ subXor[j];
                c = subXor[j];
            } else if (isAncestor(j, i)) {
                a = total ^ subXor[j];
                b = subXor[j] ^ subXor[i];
                c = subXor[i];
            } else {
                a = total ^ subXor[i] ^ subXor[j];
                b = subXor[i];
                c = subXor[j];
            }
            const mx = Math.max(a, b, c);
            const mn = Math.min(a, b, c);
            ans = Math.min(ans, mx - mn);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumScore(nums: number[], edges: number[][]): number {
    const n = nums.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Int32Array(n);
    const inTime = new Int32Array(n);
    const outTime = new Int32Array(n);
    const subXor = new Array<number>(n);
    let timer = 0;

    function dfs(u: number, p: number): void {
        parent[u] = p;
        inTime[u] = timer++;
        let xorVal = nums[u];
        for (const v of adj[u]) {
            if (v === p) continue;
            dfs(v, u);
            xorVal ^= subXor[v];
        }
        subXor[u] = xorVal;
        outTime[u] = timer;
    }

    dfs(0, -1);
    const total = subXor[0];
    let answer = Number.MAX_SAFE_INTEGER;

    function isAncestor(a: number, b: number): boolean {
        return inTime[a] <= inTime[b] && outTime[b] <= outTime[a];
    }

    for (let i = 1; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            let part1: number, part2: number, part3: number;
            if (isAncestor(i, j)) {
                // i is ancestor of j
                part1 = total ^ subXor[i];
                part2 = subXor[i] ^ subXor[j];
                part3 = subXor[j];
            } else if (isAncestor(j, i)) {
                // j is ancestor of i
                part1 = total ^ subXor[j];
                part2 = subXor[j] ^ subXor[i];
                part3 = subXor[i];
            } else {
                // independent subtrees
                part1 = total ^ subXor[i] ^ subXor[j];
                part2 = subXor[i];
                part3 = subXor[j];
            }
            const maxVal = Math.max(part1, part2, part3);
            const minVal = Math.min(part1, part2, part3);
            const score = maxVal - minVal;
            if (score < answer) answer = score;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    private array $adj = [];
    private array $nums = [];
    private array $xor = [];
    private array $tin = [];
    private array $tout = [];
    private int $timer = 0;
    private array $parent = [];

    /**
     * @param Integer[] $nums
     * @param Integer[][] $edges
     * @return Integer
     */
    function minimumScore($nums, $edges) {
        $n = count($nums);
        $this->nums = $nums;
        $this->adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $this->adj[$a][] = $b;
            $this->adj[$b][] = $a;
        }
        $this->xor = array_fill(0, $n, 0);
        $this->tin = array_fill(0, $n, 0);
        $this->tout = array_fill(0, $n, 0);
        $this->parent = array_fill(0, $n, -1);
        $this->timer = 0;
        $this->dfs(0, -1);

        $totalXor = $this->xor[0];
        $ans = PHP_INT_MAX;

        for ($i = 1; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                if ($this->isAncestor($i, $j)) {
                    $a = $totalXor ^ $this->xor[$i];
                    $b = $this->xor[$i] ^ $this->xor[$j];
                    $c = $this->xor[$j];
                } elseif ($this->isAncestor($j, $i)) {
                    $a = $totalXor ^ $this->xor[$j];
                    $b = $this->xor[$j] ^ $this->xor[$i];
                    $c = $this->xor[$i];
                } else {
                    $a = $totalXor ^ $this->xor[$i] ^ $this->xor[$j];
                    $b = $this->xor[$i];
                    $c = $this->xor[$j];
                }
                $mx = max($a, $b, $c);
                $mn = min($a, $b, $c);
                $score = $mx - $mn;
                if ($score < $ans) {
                    $ans = $score;
                }
            }
        }

        return $ans;
    }

    private function dfs(int $u, int $p): void {
        $this->parent[$u] = $p;
        $this->tin[$u] = ++$this->timer;
        $cur = $this->nums[$u];
        foreach ($this->adj[$u] as $v) {
            if ($v === $p) continue;
            $this->dfs($v, $u);
            $cur ^= $this->xor[$v];
        }
        $this->xor[$u] = $cur;
        $this->tout[$u] = ++$this->timer;
    }

    private function isAncestor(int $a, int $b): bool {
        return $this->tin[$a] <= $this->tin[$b] && $this->tout[$b] <= $this->tout[$a];
    }
}
```

## Swift

```swift
class Solution {
    func minimumScore(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var parent = [Int](repeating: -1, count: n)
        var inTime = [Int](repeating: 0, count: n)
        var outTime = [Int](repeating: 0, count: n)
        var subXor = [Int](repeating: 0, count: n)
        var timer = 0
        
        func dfs(_ node: Int, _ par: Int) {
            parent[node] = par
            inTime[node] = timer
            timer += 1
            var cur = nums[node]
            for nb in adj[node] where nb != par {
                dfs(nb, node)
                cur ^= subXor[nb]
            }
            subXor[node] = cur
            outTime[node] = timer
        }
        
        dfs(0, -1)
        let total = subXor[0]
        var answer = Int.max
        
        func isAncestor(_ anc: Int, _ desc: Int) -> Bool {
            return inTime[anc] <= inTime[desc] && outTime[desc] <= outTime[anc]
        }
        
        for u in 1..<n {
            for v in (u + 1)..<n {
                var a = 0, b = 0, c = 0
                if isAncestor(u, v) {
                    a = total ^ subXor[u]
                    b = subXor[u] ^ subXor[v]
                    c = subXor[v]
                } else if isAncestor(v, u) {
                    a = total ^ subXor[v]
                    b = subXor[v] ^ subXor[u]
                    c = subXor[u]
                } else {
                    a = total ^ subXor[u] ^ subXor[v]
                    b = subXor[u]
                    c = subXor[v]
                }
                let maxVal = max(a, max(b, c))
                let minVal = min(a, min(b, c))
                let score = maxVal - minVal
                if score < answer {
                    answer = score
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
    fun minimumScore(nums: IntArray, edges: Array<IntArray>): Int {
        val n = nums.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val parent = IntArray(n) { -1 }
        val inTime = IntArray(n)
        val outTime = IntArray(n)
        val subXor = IntArray(n)

        var timer = 0
        fun dfs(u: Int, p: Int) {
            parent[u] = p
            inTime[u] = timer++
            var cur = nums[u]
            for (v in adj[u]) {
                if (v == p) continue
                dfs(v, u)
                cur = cur xor subXor[v]
            }
            subXor[u] = cur
            outTime[u] = timer - 1
        }

        dfs(0, -1)

        fun isAncestor(a: Int, b: Int): Boolean {
            return inTime[a] <= inTime[b] && outTime[b] <= outTime[a]
        }

        val totalXor = subXor[0]
        var answer = Int.MAX_VALUE

        for (i in 1 until n) {
            for (j in i + 1 until n) {
                val part1: Int
                val part2: Int
                val part3: Int
                if (isAncestor(i, j)) {
                    // i is ancestor of j
                    part1 = totalXor xor subXor[i]
                    part2 = subXor[i] xor subXor[j]
                    part3 = subXor[j]
                } else if (isAncestor(j, i)) {
                    // j is ancestor of i
                    part1 = totalXor xor subXor[j]
                    part2 = subXor[j] xor subXor[i]
                    part3 = subXor[i]
                } else {
                    // independent subtrees
                    part1 = totalXor xor subXor[i] xor subXor[j]
                    part2 = subXor[i]
                    part3 = subXor[j]
                }
                val maxVal = maxOf(part1, part2, part3)
                val minVal = minOf(part1, part2, part3)
                answer = kotlin.math.min(answer, maxVal - minVal)
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumScore(List<int> nums, List<List<int>> edges) {
    int n = nums.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    List<int> parent = List.filled(n, -1);
    List<int> inTime = List.filled(n, 0);
    List<int> outTime = List.filled(n, 0);
    List<int> subXor = List.filled(n, 0);
    int timer = 0;

    void dfs(int u, int p) {
      parent[u] = p;
      inTime[u] = timer++;
      int cur = nums[u];
      for (int v in adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        cur ^= subXor[v];
      }
      subXor[u] = cur;
      outTime[u] = timer;
    }

    dfs(0, -1);
    int totalXor = subXor[0];
    int ans = 1 << 60;

    bool isAncestor(int a, int b) {
      return inTime[a] < inTime[b] && outTime[b] <= outTime[a];
    }

    for (int u = 1; u < n; ++u) {
      for (int v = u + 1; v < n; ++v) {
        int part1, part2, part3;
        if (isAncestor(u, v)) {
          part1 = totalXor ^ subXor[u];
          part2 = subXor[u] ^ subXor[v];
          part3 = subXor[v];
        } else if (isAncestor(v, u)) {
          part1 = totalXor ^ subXor[v];
          part2 = subXor[v] ^ subXor[u];
          part3 = subXor[u];
        } else {
          part1 = totalXor ^ subXor[u] ^ subXor[v];
          part2 = subXor[u];
          part3 = subXor[v];
        }
        int mx = part1;
        if (part2 > mx) mx = part2;
        if (part3 > mx) mx = part3;
        int mn = part1;
        if (part2 < mn) mn = part2;
        if (part3 < mn) mn = part3;
        int score = mx - mn;
        if (score < ans) ans = score;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minimumScore(nums []int, edges [][]int) int {
    n := len(nums)
    adj := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    in := make([]int, n)
    out := make([]int, n)
    subXor := make([]int, n)
    parent := make([]int, n)

    timer := 0
    var dfs func(int, int)
    dfs = func(u, p int) {
        parent[u] = p
        in[u] = timer
        timer++
        xorVal := nums[u]
        for _, v := range adj[u] {
            if v == p {
                continue
            }
            dfs(v, u)
            xorVal ^= subXor[v]
        }
        subXor[u] = xorVal
        out[u] = timer
    }
    dfs(0, -1)

    totalXor := subXor[0]

    isAncestor := func(a, b int) bool {
        // a ancestor of b (including self)
        return in[a] <= in[b] && out[b] <= out[a]
    }

    ans := 1 << 60
    for u := 1; u < n; u++ {
        for v := u + 1; v < n; v++ {
            var part1, part2, part3 int
            if isAncestor(u, v) {
                // u ancestor of v
                part1 = totalXor ^ subXor[u]
                part2 = subXor[u] ^ subXor[v]
                part3 = subXor[v]
            } else if isAncestor(v, u) {
                // v ancestor of u
                part1 = totalXor ^ subXor[v]
                part2 = subXor[v] ^ subXor[u]
                part3 = subXor[u]
            } else {
                // independent subtrees
                part1 = totalXor ^ subXor[u] ^ subXor[v]
                part2 = subXor[u]
                part3 = subXor[v]
            }
            mx := part1
            if part2 > mx {
                mx = part2
            }
            if part3 > mx {
                mx = part3
            }
            mn := part1
            if part2 < mn {
                mn = part2
            }
            if part3 < mn {
                mn = part3
            }
            score := mx - mn
            if score < ans {
                ans = score
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_score(nums, edges)
  n = nums.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  parent = Array.new(n, -1)
  intime = Array.new(n, 0)
  outtime = Array.new(n, 0)
  subxor = Array.new(n, 0)

  time = 0
  dfs = nil
  dfs = lambda do |u, p|
    parent[u] = p
    time += 1
    intime[u] = time
    cur = nums[u]
    adj[u].each do |v|
      next if v == p
      dfs.call(v, u)
      cur ^= subxor[v]
    end
    subxor[u] = cur
    outtime[u] = time
  end

  dfs.call(0, -1)

  total = subxor[0]
  ans = Float::INFINITY

  is_ancestor = lambda do |a, b|
    intime[a] < intime[b] && outtime[b] <= outtime[a]
  end

  (1...n).each do |u|
    ((u + 1)...n).each do |v|
      if is_ancestor.call(u, v)
        part3 = subxor[v]
        part2 = subxor[u] ^ subxor[v]
        part1 = total ^ subxor[u]
      elsif is_ancestor.call(v, u)
        part3 = subxor[u]
        part2 = subxor[v] ^ subxor[u]
        part1 = total ^ subxor[v]
      else
        part1 = total ^ subxor[u] ^ subxor[v]
        part2 = subxor[u]
        part3 = subxor[v]
      end
      maxv = [part1, part2, part3].max
      minv = [part1, part2, part3].min
      score = maxv - minv
      ans = score if score < ans
    end
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
  def minimumScore(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a) += b
      adj(b) += a
    }

    val parent = new Array[Int](n)
    java.util.Arrays.fill(parent, -1)
    val in = new Array[Int](n)
    val out = new Array[Int](n)
    val subXor = new Array[Int](n)

    var timer = 0

    def dfs(u: Int): Unit = {
      timer += 1
      in(u) = timer
      var cur = nums(u)
      for (v <- adj(u)) {
        if (v != parent(u)) {
          parent(v) = u
          dfs(v)
          cur ^= subXor(v)
        }
      }
      subXor(u) = cur
      out(u) = timer
    }

    dfs(0)

    val total = subXor(0)

    def isAncestor(a: Int, b: Int): Boolean =
      in(a) <= in(b) && out(b) <= out(a)

    var answer = Int.MaxValue

    for (u <- 1 until n) {
      for (v <- u + 1 until n) {
        val (x, y, z) =
          if (isAncestor(u, v)) {
            (total ^ subXor(u), subXor(u) ^ subXor(v), subXor(v))
          } else if (isAncestor(v, u)) {
            (total ^ subXor(v), subXor(v) ^ subXor(u), subXor(u))
          } else {
            (total ^ subXor(u) ^ subXor(v), subXor(u), subXor(v))
          }
        val maxVal = math.max(x, math.max(y, z))
        val minVal = math.min(x, math.min(y, z))
        answer = math.min(answer, maxVal - minVal)
      }
    }

    answer
  }
}
```

## Rust

```rust
use std::cmp::{max, min};

impl Solution {
    pub fn minimum_score(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut adj = vec![Vec::<usize>::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        fn dfs(
            u: usize,
            p: usize,
            adj: &Vec<Vec<usize>>,
            timer: &mut i32,
            in_time: &mut Vec<i32>,
            out_time: &mut Vec<i32>,
            sum: &mut Vec<i32>,
            parent: &mut Vec<usize>,
            nums: &Vec<i32>,
        ) {
            parent[u] = p;
            in_time[u] = *timer;
            *timer += 1;
            let mut cur = nums[u];
            for &v in &adj[u] {
                if v == p {
                    continue;
                }
                dfs(v, u, adj, timer, in_time, out_time, sum, parent, nums);
                cur ^= sum[v];
            }
            sum[u] = cur;
            out_time[u] = *timer;
        }

        let mut in_time = vec![0i32; n];
        let mut out_time = vec![0i32; n];
        let mut sum = vec![0i32; n];
        let mut parent = vec![n; n]; // n as sentinel for root's parent
        let mut timer: i32 = 0;
        dfs(
            0,
            n,
            &adj,
            &mut timer,
            &mut in_time,
            &mut out_time,
            &mut sum,
            &mut parent,
            &nums,
        );

        fn is_ancestor(a: usize, b: usize, in_time: &Vec<i32>, out_time: &Vec<i32>) -> bool {
            in_time[a] <= in_time[b] && out_time[b] <= out_time[a]
        }

        let total = sum[0];
        let mut answer = i32::MAX;

        for i in 1..n {
            for j in (i + 1)..n {
                let (p1, p2, p3) = if is_ancestor(i, j, &in_time, &out_time) {
                    (total ^ sum[i], sum[i] ^ sum[j], sum[j])
                } else if is_ancestor(j, i, &in_time, &out_time) {
                    (total ^ sum[j], sum[j] ^ sum[i], sum[i])
                } else {
                    (total ^ sum[i] ^ sum[j], sum[i], sum[j])
                };
                let maxv = max(p1, max(p2, p3));
                let minv = min(p1, min(p2, p3));
                answer = min(answer, maxv - minv);
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (minimum-score nums edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (adj (make-vector n '()))
         ;; build adjacency list
         (add-edge (lambda (a b)
                     (vector-set! adj a (cons b (vector-ref adj a)))
                     (vector-set! adj b (cons a (vector-ref adj b)))))
         (_ (for-each (lambda (e) (add-edge (first e) (second e))) edges))
         (in (make-vector n 0))
         (out (make-vector n 0))
         (sum (make-vector n 0))
         (timer 0)
         
         ;; dfs to compute entry/exit times and subtree xor
         (dfs (letrec ((dfs
                        (lambda (u p)
                          (vector-set! in u timer)
                          (set! timer (+ timer 1))
                          (let ((xor (vector-ref nums-vec u)))
                            (for-each
                             (lambda (v)
                               (when (not (= v p))
                                 (let ((child-xor (dfs v u)))
                                   (set! xor (bitwise-xor xor child-xor)))))
                             (vector-ref adj u))
                            (vector-set! sum u xor)
                            (vector-set! out u timer)
                            (set! timer (+ timer 1))
                            xor))))
                 dfs))
         (_ (dfs 0 -1))
         (totalXor (vector-ref sum 0))
         
         ;; ancestor check using entry/exit times
         (ancestor? (lambda (a b)
                      (and (< (vector-ref in a) (vector-ref in b))
                           (> (vector-ref out a) (vector-ref out b)))))
         
         (ans (expt 2 60))) ; large initial value
    ;; enumerate all unordered pairs of non‑root nodes
    (for ([u (in-range 1 n)])
      (for ([v (in-range (+ u 1) n)])
        (let* ((x (vector-ref sum u))
               (y (vector-ref sum v))
               (parts
                (cond
                  [(ancestor? u v)
                   (list (bitwise-xor totalXor x)
                         (bitwise-xor x y)
                         y)]
                  [(ancestor? v u)
                   (list (bitwise-xor totalXor y)
                         (bitwise-xor y x)
                         x)]
                  [else
                   (list (bitwise-xor totalXor (bitwise-xor x y))
                         x
                         y)]))
               (mx (apply max parts))
               (mn (apply min parts))
               (score (- mx mn)))
          (when (< score ans) (set! ans score)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([minimum_score/2]).

-spec minimum_score(Nums :: [integer()], Edges :: [[integer()]]) -> integer().
minimum_score(Nums, Edges) ->
    N = length(Nums),
    Adj = build_adj(Edges, #{}),

    % Initialize arrays
    Parent0 = lists:duplicate(N, -1),
    Sum0    = lists:duplicate(N, 0),
    In0     = lists:duplicate(N, 0),
    Out0    = lists:duplicate(N, 0),

    % DFS from root (node 0)
    {_, ParentArr, SumArr, InArr, OutArr} =
        dfs(0, -1, Adj, Nums, 0, Parent0, Sum0, In0, Out0),

    TotalXor = get_elem(SumArr, 0),
    Indices = lists:seq(1, N-1),

    % Enumerate all unordered pairs of non‑root nodes
    Pairs = [{U,V} || U <- Indices, V <- Indices, V > U],
    InitialBest = 1 bsl 60,
    Best = lists:foldl(
        fun({U,V}, Acc) ->
            Score = pair_score(U, V, TotalXor, SumArr, InArr, OutArr),
            if Score < Acc -> Score; true -> Acc end
        end,
        InitialBest,
        Pairs),

    Best.

%% Build adjacency map from edge list
build_adj([], Adj) -> Adj;
build_adj([[A,B]|Rest], Adj) ->
    Adj1 = add_neighbor(Adj, A, B),
    Adj2 = add_neighbor(Adj1, B, A),
    build_adj(Rest, Adj2).

add_neighbor(Adj, From, To) ->
    case maps:is_key(From, Adj) of
        true ->
            Old = maps:get(From, Adj),
            maps:put(From, [To|Old], Adj);
        false ->
            maps:put(From, [To], Adj)
    end.

%% Depth‑first search to compute parent, subtree xor, entry/exit times
dfs(Node, ParentNode, Adj, Nums, Time, ParentArr, SumArr, InArr, OutArr) ->
    % set parent
    ParentArr1 = set_elem(ParentArr, Node, ParentNode),
    % entry time
    InArr1 = set_elem(InArr, Node, Time),

    Val = get_elem(Nums, Node),

    Neighbors = maps:get(Node, Adj, []),

    {TimeAfterChildren, ParentAcc, SumAcc, InAcc, OutAcc, SubXor} =
        lists:foldl(
            fun(Nei, {T, PArr, SArr, IArr, OArr, AccXor}) ->
                if Nei =:= ParentNode ->
                        {T, PArr, SArr, IArr, OArr, AccXor};
                   true ->
                        {NewTime, PArr1, SArr1, IArr1, OArr1} =
                            dfs(Nei, Node, Adj, Nums, T+1, PArr, SArr, IArr, OArr),
                        ChildSum = get_elem(SArr1, Nei),
                        {NewTime, PArr1, SArr1, IArr1, OArr1,
                         AccXor bxor ChildSum}
                end
            end,
            {Time, ParentArr1, SumArr, InArr1, OutArr, Val},
            Neighbors),

    % set subtree xor sum for this node
    SumAcc1 = set_elem(SumAcc, Node, SubXor),
    % set exit time
    OutAcc1 = set_elem(OutAcc, Node, TimeAfterChildren),

    {TimeAfterChildren, ParentArr1, SumAcc1, InAcc, OutAcc1}.

%% Compute score for a pair of removed edges (nodes U and V)
pair_score(U, V, TotalXor, SumArr, InArr, OutArr) ->
    SumU = get_elem(SumArr, U),
    SumV = get_elem(SumArr, V),

    case ancestor(U, V, InArr, OutArr) of
        true -> % U is ancestor of V
            Part1 = TotalXor bxor SumU,
            Part2 = SumU bxor SumV,
            Part3 = SumV;
        false ->
            case ancestor(V, U, InArr, OutArr) of
                true -> % V is ancestor of U
                    Part1 = TotalXor bxor SumV,
                    Part2 = SumV bxor SumU,
                    Part3 = SumU;
                false -> % independent subtrees
                    Part1 = TotalXor bxor SumU bxor SumV,
                    Part2 = SumU,
                    Part3 = SumV
            end
    end,

    MaxPart = max(Part1, max(Part2, Part3)),
    MinPart = min(Part1, min(Part2, Part3)),
    MaxPart - MinPart.

%% Ancestor check using entry/exit timestamps
ancestor(A, B, InArr, OutArr) ->
    InA  = get_elem(InArr, A),
    OutA = get_elem(OutArr, A),
    InB  = get_elem(InArr, B),
    OutB = get_elem(OutArr, B),
    (InA < InB) andalso (OutB =< OutA).

%% Helper to get element at index (0‑based)
get_elem(List, Index) ->
    lists:nth(Index + 1, List).

%% Helper to set element at index (0‑based), returns new list
set_elem(List, Index, Value) ->
    lists:setelement(Index + 1, List, Value).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec minimum_score(nums :: [integer], edges :: [[integer]]) :: integer
  def minimum_score(nums, edges) do
    n = length(nums)
    adj = build_adj(n, edges)

    {_, in_map, out_map, xor_map} = dfs(0, -1, 0, nums, adj)
    total = Map.get(xor_map, 0)

    init_min = :math.pow(2, 60) |> trunc()

    Enum.reduce(1..(n - 1), init_min, fn u, acc_u ->
      Enum.reduce((u + 1)..(n - 1), acc_u, fn v, acc_v ->
        in_u = Map.get(in_map, u)
        out_u = Map.get(out_map, u)
        in_v = Map.get(in_map, v)
        out_v = Map.get(out_map, v)

        {part1, part2, part3} =
          cond do
            in_u < in_v and out_v < out_u ->
              {
                Bitwise.bxor(total, Map.get(xor_map, u)),
                Bitwise.bxor(Map.get(xor_map, u), Map.get(xor_map, v)),
                Map.get(xor_map, v)
              }

            in_v < in_u and out_u < out_v ->
              {
                Bitwise.bxor(total, Map.get(xor_map, v)),
                Bitwise.bxor(Map.get(xor_map, v), Map.get(xor_map, u)),
                Map.get(xor_map, u)
              }

            true ->
              {
                Bitwise.bxor(Bitwise.bxor(total, Map.get(xor_map, u)), Map.get(xor_map, v)),
                Map.get(xor_map, u),
                Map.get(xor_map, v)
              }
          end

        max_part = Enum.max([part1, part2, part3])
        min_part = Enum.min([part1, part2, part3])
        score = max_part - min_part
        if score < acc_v, do: score, else: acc_v
      end)
    end)
  end

  defp build_adj(n, edges) do
    adj0 = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)

    Enum.reduce(edges, adj0, fn [a, b], acc ->
      acc
      |> Map.update!(a, fn list -> [b | list] end)
      |> Map.update!(b, fn list -> [a | list] end)
    end)
  end

  defp dfs(node, parent, time, nums, adj) do
    in_map = %{node => time}
    cur_xor = Enum.at(nums, node)

    {t, in_acc, out_acc, xor_acc, cur_xor} =
      Enum.reduce(Map.get(adj, node, []), {time + 1, in_map, %{}, %{}, cur_xor}, fn child,
          {cur_time, imap, omap, xmap, acc_xor} ->
        if child == parent do
          {cur_time, imap, omap, xmap, acc_xor}
        else
          {new_time, im_child, out_child, xor_child} = dfs(child, node, cur_time, nums, adj)
          child_xor = Map.get(xor_child, child)

          {
            new_time,
            Map.merge(imap, im_child),
            Map.merge(omap, out_child),
            Map.merge(xmap, xor_child),
            Bitwise.bxor(acc_xor, child_xor)
          }
        end
      end)

    out_map = Map.put(out_acc, node, t)
    xor_map = Map.put(xor_acc, node, cur_xor)
    {t + 1, in_acc, out_map, xor_map}
  end
end
```
