# 1857. Largest Color Value in a Directed Graph

## Cpp

```cpp
class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        vector<vector<int>> adj(n);
        vector<int> indeg(n, 0);
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            adj[a].push_back(b);
            ++indeg[b];
        }
        queue<int> q;
        for (int i = 0; i < n; ++i) if (indeg[i] == 0) q.push(i);
        
        vector<array<int,26>> dp(n);
        for (int i = 0; i < n; ++i) {
            dp[i].fill(0);
            dp[i][colors[i] - 'a'] = 1;
        }
        
        int visited = 0;
        int ans = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            ++visited;
            for (int c = 0; c < 26; ++c) {
                if (dp[u][c] > ans) ans = dp[u][c];
            }
            for (int v : adj[u]) {
                for (int c = 0; c < 26; ++c) {
                    int cand = dp[u][c] + (colors[v] - 'a' == c);
                    if (cand > dp[v][c]) dp[v][c] = cand;
                }
                if (--indeg[v] == 0) q.push(v);
            }
        }
        return visited == n ? ans : -1;
    }
};
```

## Java

```java
class Solution {
    public int largestPathValue(String colors, int[][] edges) {
        int n = colors.length();
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        int[] indeg = new int[n];
        for (int[] e : edges) {
            int from = e[0], to = e[1];
            graph[from].add(to);
            indeg[to]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) queue.add(i);
        }
        int[][] dp = new int[n][26];
        int processed = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            processed++;
            int colIdx = colors.charAt(u) - 'a';
            dp[u][colIdx]++; // include current node's color
            for (int v : graph[u]) {
                // propagate counts from u to v
                for (int c = 0; c < 26; c++) {
                    if (dp[u][c] > dp[v][c]) dp[v][c] = dp[u][c];
                }
                indeg[v]--;
                if (indeg[v] == 0) queue.add(v);
            }
        }
        if (processed != n) return -1; // cycle detected
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int c = 0; c < 26; c++) {
                if (dp[i][c] > ans) ans = dp[i][c];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(colors)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for a, b in edges:
            adj[a].append(b)
            indeg[b] += 1

        dp = [[0] * 26 for _ in range(n)]
        q = deque([i for i in range(n) if indeg[i] == 0])
        visited = 0
        ans = 0
        while q:
            u = q.popleft()
            visited += 1
            col_idx = ord(colors[u]) - 97
            dp[u][col_idx] += 1
            if dp[u][col_idx] > ans:
                ans = dp[u][col_idx]
            for v in adj[u]:
                # propagate counts
                du = dp[u]
                dv = dp[v]
                for c in range(26):
                    if du[c] > dv[c]:
                        dv[c] = du[c]
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return -1 if visited != n else ans
```

## Python3

```python
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import deque

        n = len(colors)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])
        color_idx = [ord(c) - 97 for c in colors]
        dp = [[0] * 26 for _ in range(n)]

        ans = 0
        visited = 0

        while q:
            u = q.popleft()
            visited += 1
            cu = color_idx[u]
            if dp[u][cu] == 0:
                dp[u][cu] = 1
            if dp[u][cu] > ans:
                ans = dp[u][cu]

            du = dp[u]
            for v in graph[u]:
                cv = color_idx[v]
                dv = dp[v]
                # propagate counts
                for c in range(26):
                    val = du[c] + (1 if c == cv else 0)
                    if val > dv[c]:
                        dv[c] = val
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return -1 if visited != n else ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int largestPathValue(char * colors, int** edges, int edgesSize, int* edgesColSize){
    int n = strlen(colors);
    int *indeg = calloc(n, sizeof(int));
    int *outCnt = calloc(n, sizeof(int));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        outCnt[u]++;
        indeg[v]++;
    }

    int *offset = malloc((n + 1) * sizeof(int));
    offset[0] = 0;
    for (int i = 0; i < n; ++i)
        offset[i + 1] = offset[i] + outCnt[i];

    int *nbr = malloc(edgesSize * sizeof(int));
    int *cur = malloc(n * sizeof(int));
    memcpy(cur, offset, n * sizeof(int));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        nbr[cur[u]++] = v;
    }

    int *dp = calloc(n * 26, sizeof(int));
    int *queue = malloc(n * sizeof(int));
    int qh = 0, qt = 0;

    for (int i = 0; i < n; ++i)
        if (indeg[i] == 0) queue[qt++] = i;

    int processed = 0;
    int answer = 0;

    while (qh < qt) {
        int u = queue[qh++];
        processed++;

        int colIdx = colors[u] - 'a';
        dp[u * 26 + colIdx]++;  // include current node

        for (int c = 0; c < 26; ++c)
            if (dp[u * 26 + c] > answer) answer = dp[u * 26 + c];

        for (int idx = offset[u]; idx < offset[u + 1]; ++idx) {
            int v = nbr[idx];
            for (int c = 0; c < 26; ++c) {
                int val = dp[u * 26 + c];
                if (val > dp[v * 26 + c]) dp[v * 26 + c] = val;
            }
            if (--indeg[v] == 0) queue[qt++] = v;
        }
    }

    free(indeg);
    free(outCnt);
    free(offset);
    free(nbr);
    free(cur);
    free(dp);
    free(queue);

    return processed == n ? answer : -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LargestPathValue(string colors, int[][] edges) {
        int n = colors.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        int[] indeg = new int[n];
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            indeg[b]++;
        }

        int[,] dp = new int[n, 26];
        for (int i = 0; i < n; i++) {
            dp[i, colors[i] - 'a'] = 1;
        }

        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);

        int processed = 0;
        int answer = 0;

        while (q.Count > 0) {
            int u = q.Dequeue();
            processed++;

            // update global answer with current node's dp values
            for (int c = 0; c < 26; c++) {
                if (dp[u, c] > answer) answer = dp[u, c];
            }

            foreach (int v in graph[u]) {
                for (int c = 0; c < 26; c++) {
                    int cand = dp[u, c] + ((colors[v] - 'a') == c ? 1 : 0);
                    if (cand > dp[v, c]) dp[v, c] = cand;
                }
                indeg[v]--;
                if (indeg[v] == 0) q.Enqueue(v);
            }
        }

        return processed == n ? answer : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function(colors, edges) {
    const n = colors.length;
    const indeg = new Int32Array(n);
    const adj = Array.from({length: n}, () => []);
    
    for (const [a, b] of edges) {
        adj[a].push(b);
        indeg[b]++;
    }
    
    // color index per node
    const colIdx = new Uint8Array(n);
    for (let i = 0; i < n; ++i) colIdx[i] = colors.charCodeAt(i) - 97;
    
    // dp[node][c] = max count of color c on any path ending at node
    const dp = Array.from({length: n}, () => new Int32Array(26));
    for (let i = 0; i < n; ++i) {
        dp[i][colIdx[i]] = 1;
    }
    
    // Kahn's algorithm
    const queue = [];
    for (let i = 0; i < n; ++i) if (indeg[i] === 0) queue.push(i);
    let qh = 0, visited = 0;
    let answer = 0;
    
    while (qh < queue.length) {
        const u = queue[qh++];
        visited++;
        // update global max
        for (let c = 0; c < 26; ++c) {
            if (dp[u][c] > answer) answer = dp[u][c];
        }
        for (const v of adj[u]) {
            const dv = dp[v];
            const du = dp[u];
            const add = colIdx[v];
            for (let c = 0; c < 26; ++c) {
                const cand = du[c] + (c === add ? 1 : 0);
                if (cand > dv[c]) dv[c] = cand;
            }
            indeg[v]--;
            if (indeg[v] === 0) queue.push(v);
        }
    }
    
    return visited === n ? answer : -1;
};
```

## Typescript

```typescript
function largestPathValue(colors: string, edges: number[][]): number {
    const n = colors.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    for (const [a, b] of edges) {
        adj[a].push(b);
        indeg[b]++;
    }

    const dp: Uint32Array[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const arr = new Uint32Array(26);
        arr[colors.charCodeAt(i) - 97] = 1;
        dp[i] = arr;
    }

    const queue: number[] = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let qh = 0, processed = 0, answer = 0;

    while (qh < queue.length) {
        const u = queue[qh++];
        processed++;
        const du = dp[u];
        for (let c = 0; c < 26; c++) if (du[c] > answer) answer = du[c];

        for (const v of adj[u]) {
            const dv = dp[v];
            const colV = colors.charCodeAt(v) - 97;
            for (let c = 0; c < 26; c++) {
                const cand = du[c] + (c === colV ? 1 : 0);
                if (cand > dv[c]) dv[c] = cand;
            }
            indeg[v]--;
            if (indeg[v] === 0) queue.push(v);
        }
    }

    return processed === n ? answer : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $colors
     * @param Integer[][] $edges
     * @return Integer
     */
    function largestPathValue($colors, $edges) {
        $n = strlen($colors);
        $adj = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);

        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $indeg[$b]++;
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        // map each node to its color index (0-25)
        $colorIdx = [];
        for ($i = 0; $i < $n; $i++) {
            $colorIdx[$i] = ord($colors[$i]) - 97;
        }

        // dp[node][c] = max count of color c on any path ending at node
        $dp = array_fill(0, $n, array_fill(0, 26, 0));
        for ($i = 0; $i < $n; $i++) {
            $c = $colorIdx[$i];
            $dp[$i][$c] = 1;
        }

        $processed = 0;
        $ans = 0;

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $processed++;

            // update global answer
            $maxU = max($dp[$u]);
            if ($maxU > $ans) {
                $ans = $maxU;
            }

            foreach ($adj[$u] as $v) {
                for ($c = 0; $c < 26; $c++) {
                    $cand = $dp[$u][$c];
                    if ($colorIdx[$v] == $c) {
                        $cand++;
                    }
                    if ($cand > $dp[$v][$c]) {
                        $dp[$v][$c] = $cand;
                    }
                }

                $indeg[$v]--;
                if ($indeg[$v] == 0) {
                    $queue->enqueue($v);
                }
            }
        }

        if ($processed != $n) {
            return -1; // cycle detected
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func largestPathValue(_ colors: String, _ edges: [[Int]]) -> Int {
        let n = colors.count
        var colorIdx = [Int]()
        let base = Character("a").unicodeScalars.first!.value
        for scalar in colors.unicodeScalars {
            colorIdx.append(Int(scalar.value - base))
        }
        
        var graph = [[Int]](repeating: [], count: n)
        var indegree = [Int](repeating: 0, count: n)
        for edge in edges {
            let a = edge[0]
            let b = edge[1]
            graph[a].append(b)
            indegree[b] += 1
        }
        
        var queue = [Int]()
        for i in 0..<n where indegree[i] == 0 {
            queue.append(i)
        }
        
        var dp = [[Int]](repeating: Array(repeating: 0, count: 26), count: n)
        var visited = 0
        var maxVal = 0
        var head = 0
        
        while head < queue.count {
            let u = queue[head]
            head += 1
            visited += 1
            
            let cu = colorIdx[u]
            if dp[u][cu] == 0 { dp[u][cu] = 1 }
            
            for col in 0..<26 {
                if dp[u][col] > maxVal {
                    maxVal = dp[u][col]
                }
            }
            
            for v in graph[u] {
                for col in 0..<26 {
                    var val = dp[u][col]
                    if colorIdx[v] == col { val += 1 }
                    if val > dp[v][col] {
                        dp[v][col] = val
                    }
                }
                indegree[v] -= 1
                if indegree[v] == 0 {
                    queue.append(v)
                }
            }
        }
        
        return visited == n ? maxVal : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPathValue(colors: String, edges: Array<IntArray>): Int {
        val n = colors.length
        val adj = Array(n) { mutableListOf<Int>() }
        val indeg = IntArray(n)
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            indeg[b]++
        }

        val colorIdx = IntArray(n) { colors[it] - 'a' }
        val dp = Array(n) { IntArray(26) }
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        for (i in 0 until n) {
            if (indeg[i] == 0) {
                queue.add(i)
                dp[i][colorIdx[i]] = 1
            }
        }

        var processed = 0
        var answer = 0

        while (!queue.isEmpty()) {
            val u = queue.poll()
            processed++
            // update global answer with current node's dp values
            for (c in 0 until 26) {
                if (dp[u][c] > answer) answer = dp[u][c]
            }
            for (v in adj[u]) {
                for (c in 0 until 26) {
                    var cand = dp[u][c]
                    if (c == colorIdx[v]) cand += 1
                    if (cand > dp[v][c]) dp[v][c] = cand
                }
                indeg[v]--
                if (indeg[v] == 0) {
                    // ensure at least the node itself contributes its own color
                    if (dp[v][colorIdx[v]] == 0) dp[v][colorIdx[v]] = 1
                    queue.add(v)
                }
            }
        }

        return if (processed < n) -1 else answer
    }
}
```

## Golang

```go
func largestPathValue(colors string, edges [][]int) int {
	n := len(colors)
	indeg := make([]int, n)
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		indeg[v]++
	}
	dp := make([][26]int, n)
	for i := 0; i < n; i++ {
		idx := colors[i] - 'a'
		dp[i][idx] = 1
	}
	queue := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	processed := 0
	ans := 0
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		processed++
		for c := 0; c < 26; c++ {
			if dp[u][c] > ans {
				ans = dp[u][c]
			}
		}
		for _, v := range graph[u] {
			for c := 0; c < 26; c++ {
				val := dp[u][c]
				if int(colors[v]-'a') == c {
					val++
				}
				if val > dp[v][c] {
					dp[v][c] = val
				}
			}
			indeg[v]--
			if indeg[v] == 0 {
				queue = append(queue, v)
			}
		}
	}
	if processed != n {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def largest_path_value(colors, edges)
  n = colors.length
  adj = Array.new(n) { [] }
  indegree = Array.new(n, 0)

  edges.each do |a, b|
    adj[a] << b
    indegree[b] += 1
  end

  color_idx = colors.bytes.map { |b| b - 97 }

  dp = Array.new(n) { Array.new(26, 0) }
  n.times { |i| dp[i][color_idx[i]] = 1 }

  queue = []
  indegree.each_with_index { |deg, i| queue << i if deg.zero? }
  front = 0
  processed = 0
  max_val = 0

  while front < queue.length
    u = queue[front]
    front += 1
    processed += 1
    cur_max = dp[u].max
    max_val = cur_max if cur_max > max_val

    adj[u].each do |v|
      26.times do |c|
        cand = dp[u][c] + (c == color_idx[v] ? 1 : 0)
        dp[v][c] = cand if cand > dp[v][c]
      end
      indegree[v] -= 1
      queue << v if indegree[v].zero?
    end
  end

  return -1 if processed != n
  max_val
end
```

## Scala

```scala
object Solution {
    def largestPathValue(colors: String, edges: Array[Array[Int]]): Int = {
        val n = colors.length
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        val indeg = new Array[Int](n)
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            indeg(v) += 1
        }
        val dp = Array.ofDim[Int](n, 26)
        val queue = new java.util.ArrayDeque[Int]()
        for (i <- 0 until n) {
            if (indeg(i) == 0) queue.add(i)
        }
        var processed = 0
        var answer = 0
        while (!queue.isEmpty) {
            val u = queue.poll()
            processed += 1
            val colIdx = colors.charAt(u) - 'a'
            dp(u)(colIdx) += 1
            if (dp(u)(colIdx) > answer) answer = dp(u)(colIdx)
            for (v <- adj(u)) {
                var c = 0
                while (c < 26) {
                    val cur = dp(u)(c)
                    if (cur > dp(v)(c)) dp(v)(c) = cur
                    c += 1
                }
                indeg(v) -= 1
                if (indeg(v) == 0) queue.add(v)
            }
        }
        if (processed != n) -1 else answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            indeg[v] += 1;
        }

        let mut dp: Vec<[i32; 26]> = vec![[0; 26]; n];
        let colors_bytes = colors.as_bytes();
        for i in 0..n {
            let idx = (colors_bytes[i] - b'a') as usize;
            dp[i][idx] = 1;
        }

        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }

        let mut visited = 0usize;
        let mut ans = 0i32;
        // initial answer from single nodes
        for i in 0..n {
            for c in 0..26 {
                if dp[i][c] > ans {
                    ans = dp[i][c];
                }
            }
        }

        while let Some(u) = q.pop_front() {
            visited += 1;
            for &v in adj[u].iter() {
                for c in 0..26 {
                    let mut val = dp[u][c];
                    if c == ((colors_bytes[v] - b'a') as usize) {
                        val += 1;
                    }
                    if val > dp[v][c] {
                        dp[v][c] = val;
                        if val > ans {
                            ans = val;
                        }
                    }
                }
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }

        if visited != n {
            -1
        } else {
            ans
        }
    }
}
```

## Racket

```racket
(define/contract (largest-path-value colors edges)
  (-> string? (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (string-length colors)]
         [color-idx (make-vector n 0)])
    ;; map each node to its color index 0..25
    (for ([i (in-range n)])
      (vector-set! color-idx i
                   (- (char->integer (string-ref colors i))
                      (char->integer #\a))))
    (define indegree (make-vector n 0))
    (define adj (make-vector n '()))
    ;; build graph and indegrees
    (for ([e edges])
      (let ([a (first e)]
            [b (second e)])
        (vector-set! indegree b (+ (vector-ref indegree b) 1))
        (vector-set! adj a (cons b (vector-ref adj a)))))
    ;; dp[node][color] = max count of that color on any path ending at node
    (define dp (make-vector n #f))
    (for ([i (in-range n)])
      (let ([arr (make-vector 26 0)])
        (vector-set! arr (vector-ref color-idx i) 1)
        (vector-set! dp i arr)))
    ;; queue for Kahn's algorithm
    (define q (make-vector n 0))
    (define front 0)
    (define back 0)
    (for ([i (in-range n)])
      (when (= (vector-ref indegree i) 0)
        (vector-set! q back i)
        (set! back (+ back 1))))
    (define processed 0)
    (define answer 0)
    ;; process nodes in topological order
    (let loop ()
      (when (< front back)
        (let* ([u (vector-ref q front)]
               [_ (set! front (+ front 1))]
               [arrU (vector-ref dp u)])
          (set! processed (+ processed 1))
          ;; update global answer with counts at u
          (for ([c (in-range 26)])
            (let ([val (vector-ref arrU c)])
              (when (> val answer) (set! answer val))))
          ;; relax edges u -> v
          (for ([v (in-list (vector-ref adj u))])
            (let* ([arrV (vector-ref dp v)]
                   [colV (vector-ref color-idx v)])
              (for ([c (in-range 26)])
                (define cand (+ (vector-ref arrU c)
                                (if (= c colV) 1 0)))
                (when (> cand (vector-ref arrV c))
                  (vector-set! arrV c cand)))
              ;; update indegree and possibly enqueue
              (vector-set! indegree v (- (vector-ref indegree v) 1))
              (when (= (vector-ref indegree v) 0)
                (vector-set! q back v)
                (set! back (+ back 1))))))
        (loop)))
    (if (< processed n) -1 answer)))
```
