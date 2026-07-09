# 2242. Maximum Score of a Node Sequence

## Cpp

```cpp
class Solution {
public:
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        int n = scores.size();
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        const int K = 3;
        vector<vector<int>> top(n); // store up to K neighbors with highest scores
        for (int i = 0; i < n; ++i) {
            vector<pair<int,int>> cand;
            cand.reserve(adj[i].size());
            for (int nb : adj[i]) {
                cand.emplace_back(scores[nb], nb);
            }
            sort(cand.begin(), cand.end(),
                 [](const pair<int,int>& a, const pair<int,int>& b){ return a.first > b.first; });
            int limit = min(K, (int)cand.size());
            top[i].reserve(limit);
            for (int j = 0; j < limit; ++j) {
                top[i].push_back(cand[j].second);
            }
        }
        long long bestAns = -1;
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            // consider u as left middle, v as right middle
            for (int a : top[u]) {
                if (a == v) continue;
                for (int d : top[v]) {
                    if (d == u || d == a) continue;
                    long long cur = (long long)scores[a] + scores[u] + scores[v] + scores[d];
                    if (cur > bestAns) bestAns = cur;
                }
            }
        }
        return (int)bestAns;
    }
};
```

## Java

```java
class Solution {
    public int maximumScore(int[] scores, int[][] edges) {
        int n = scores.length;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        int[][] top = new int[n][3];
        for (int i = 0; i < n; i++) {
            java.util.ArrayList<Integer> list = adj[i];
            list.sort((a, b) -> Integer.compare(scores[b], scores[a])); // descending by score
            for (int j = 0; j < 3; j++) {
                top[i][j] = (j < list.size()) ? list.get(j) : -1;
            }
        }

        int ans = -1;
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            // pick a from neighbors of u, d from neighbors of v
            for (int i = 0; i < 3; i++) {
                int a = top[u][i];
                if (a == -1 || a == v) continue;
                for (int j = 0; j < 3; j++) {
                    int d = top[v][j];
                    if (d == -1 || d == u || d == a) continue;
                    int sum = scores[a] + scores[u] + scores[v] + scores[d];
                    if (sum > ans) ans = sum;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # keep up to 3 best neighbors (by score) for each node
        top = [None] * n
        for i in range(n):
            if not adj[i]:
                top[i] = []
                continue
            adj[i].sort(key=lambda x: scores[x], reverse=True)
            top[i] = adj[i][:3]

        ans = -1
        for u, v in edges:
            # try all combinations of best neighbors from u and v
            for a in top[u]:
                if a == v:
                    continue
                for b in top[v]:
                    if b == u or b == a:
                        continue
                    total = scores[a] + scores[u] + scores[v] + scores[b]
                    if total > ans:
                        ans = total
        return ans
```

## Python3

```python
class Solution:
    def maximumScore(self, scores, edges):
        from collections import defaultdict
        n = len(scores)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # store up to 3 best neighbors (by score) for each node
        best = [[] for _ in range(n)]
        for i in range(n):
            if not adj[i]:
                continue
            # sort neighbors by their scores descending, keep top 3
            neigh = sorted(adj[i], key=lambda x: scores[x], reverse=True)
            best[i] = neigh[:3]

        ans = -1
        for u, v in edges:
            # try u as left middle, v as right middle
            for a in best[u]:
                if a == v:
                    continue
                for b in best[v]:
                    if b == u or b == a:
                        continue
                    total = scores[a] + scores[u] + scores[v] + scores[b]
                    if total > ans:
                        ans = total
        return ans
```

## C

```c
static int *gScores;

static int cmp_desc(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    if (gScores[ia] < gScores[ib]) return 1;
    if (gScores[ia] > gScores[ib]) return -1;
    return 0;
}

int maximumScore(int* scores, int scoresSize, int** edges, int edgesSize, int* edgesColSize) {
    int n = scoresSize;
    const int K = 3;                     // keep top 3 neighbors per node
    int *deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }

    int **adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *pos = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][pos[u]++] = v;
        adj[v][pos[v]++] = u;
    }
    free(pos);

    /* best[i][j] stores the j‑th highest‑scoring neighbor of i (or -1) */
    int **best = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        best[i] = (int *)malloc(K * sizeof(int));
        for (int j = 0; j < K; ++j) best[i][j] = -1;
    }

    gScores = scores;
    for (int i = 0; i < n; ++i) {
        if (deg[i] == 0) continue;
        qsort(adj[i], deg[i], sizeof(int), cmp_desc);
        int limit = deg[i] < K ? deg[i] : K;
        for (int j = 0; j < limit; ++j) best[i][j] = adj[i][j];
    }

    long long ans = -1;
    for (int e = 0; e < edgesSize; ++e) {
        int u = edges[e][0];
        int v = edges[e][1];
        for (int i = 0; i < K; ++i) {
            int a = best[u][i];
            if (a == -1 || a == v) continue;
            for (int j = 0; j < K; ++j) {
                int d = best[v][j];
                if (d == -1 || d == u || d == a) continue;
                long long cur = (long long)scores[a] + scores[u] + scores[v] + scores[d];
                if (cur > ans) ans = cur;
            }
        }
    }

    /* free allocated memory */
    for (int i = 0; i < n; ++i) {
        free(adj[i]);
        free(best[i]);
    }
    free(adj);
    free(best);
    free(deg);

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumScore(int[] scores, int[][] edges) {
        int n = scores.Length;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        // top up to 3 neighbors with highest scores for each node
        var best = new int[n][];
        for (int i = 0; i < n; i++) {
            var list = adj[i];
            list.Sort((a, b) => scores[b].CompareTo(scores[a])); // descending by score
            int cnt = Math.Min(3, list.Count);
            best[i] = new int[cnt];
            for (int k = 0; k < cnt; k++) best[i][k] = list[k];
        }

        int ans = -1;
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            var bu = best[u];
            var bv = best[v];
            if (bu.Length == 0 || bv.Length == 0) continue;

            foreach (int a in bu) {
                if (a == v) continue; // cannot reuse middle node
                foreach (int d in bv) {
                    if (d == u || d == a) continue;
                    int sum = scores[a] + scores[u] + scores[v] + scores[d];
                    if (sum > ans) ans = sum;
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
 * @param {number[]} scores
 * @param {number[][]} edges
 * @return {number}
 */
var maximumScore = function(scores, edges) {
    const n = scores.length;
    const top = Array.from({ length: n }, () => []);
    
    const insert = (node, neigh) => {
        const arr = top[node];
        arr.push(neigh);
        arr.sort((a, b) => scores[b] - scores[a]);
        if (arr.length > 3) arr.pop();
    };
    
    for (const [u, v] of edges) {
        insert(u, v);
        insert(v, u);
    }
    
    let ans = -1;
    for (const [u, v] of edges) {
        const listU = top[u];
        const listV = top[v];
        for (let i = 0; i < listU.length; ++i) {
            const a = listU[i];
            if (a === v) continue;
            for (let j = 0; j < listV.length; ++j) {
                const d = listV[j];
                if (d === u || d === a) continue;
                const sum = scores[a] + scores[u] + scores[v] + scores[d];
                if (sum > ans) ans = sum;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function maximumScore(scores: number[], edges: number[][]): number {
    const n = scores.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    // For each node keep up to 3 neighbors with highest scores
    const top: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; ++i) {
        const neigh = adj[i];
        neigh.sort((x, y) => scores[y] - scores[x]); // descending by score
        top[i] = neigh.slice(0, 3);
    }

    let best = -1;
    for (const [u, v] of edges) {
        const listU = top[u];
        const listV = top[v];
        for (const a of listU) {
            if (a === v) continue; // cannot reuse middle node
            for (const b of listV) {
                if (b === u || b === a) continue; // distinct nodes
                const cur = scores[a] + scores[u] + scores[v] + scores[b];
                if (cur > best) best = cur;
            }
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @param Integer[][] $edges
     * @return Integer
     */
    function maximumScore($scores, $edges) {
        $n = count($scores);
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // for each node keep up to 3 neighbors with highest scores
        $top = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $list = [];
            foreach ($adj[$i] as $nbr) {
                $inserted = false;
                $cnt = count($list);
                for ($k = 0; $k < $cnt; $k++) {
                    if ($scores[$nbr] > $scores[$list[$k]]) {
                        array_splice($list, $k, 0, [$nbr]);
                        $inserted = true;
                        break;
                    }
                }
                if (!$inserted) {
                    $list[] = $nbr;
                }
                if (count($list) > 3) {
                    array_pop($list);
                }
            }
            $top[$i] = $list; // already in descending order
        }

        $maxScore = -1;

        foreach ($edges as $e) {
            [$u, $v] = $e;
            foreach ($top[$u] as $a) {
                if ($a == $v) continue;
                foreach ($top[$v] as $d) {
                    if ($d == $u || $d == $a) continue;
                    $sum = $scores[$a] + $scores[$u] + $scores[$v] + $scores[$d];
                    if ($sum > $maxScore) {
                        $maxScore = $sum;
                    }
                }
            }
        }

        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func maximumScore(_ scores: [Int], _ edges: [[Int]]) -> Int {
        let n = scores.count
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0]
            let v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        // For each node keep up to 3 neighbors with highest scores
        var best = Array(repeating: [(Int, Int)](), count: n)
        for i in 0..<n {
            if adj[i].isEmpty { continue }
            let sortedNeighbors = adj[i].sorted { scores[$0] > scores[$1] }
            let top = sortedNeighbors.prefix(3)
            best[i] = top.map { (scores[$0], $0) }
        }
        
        var answer = -1
        for e in edges {
            let u = e[0]
            let v = e[1]
            let listU = best[u]
            let listV = best[v]
            if listU.isEmpty || listV.isEmpty { continue }
            for aTuple in listU {
                let a = aTuple.1
                if a == v { continue } // must be distinct from middle nodes
                for bTuple in listV {
                    let b = bTuple.1
                    if b == u || b == a { continue } // distinctness checks
                    let total = scores[a] + scores[u] + scores[v] + scores[b]
                    if total > answer {
                        answer = total
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
    fun maximumScore(scores: IntArray, edges: Array<IntArray>): Int {
        val n = scores.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(Pair(scores[b], b))
            adj[b].add(Pair(scores[a], a))
        }

        // store up to 3 best neighbors for each node
        val top = Array(n) { IntArray(3) { -1 } }
        for (i in 0 until n) {
            val list = adj[i]
            list.sortByDescending { it.first }
            val limit = kotlin.math.min(3, list.size)
            for (k in 0 until limit) {
                top[i][k] = list[k].second
            }
        }

        var best = -1L
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            for (i in 0 until 3) {
                val a = top[u][i]
                if (a == -1 || a == v) continue
                for (j in 0 until 3) {
                    val b = top[v][j]
                    if (b == -1 || b == u || b == a) continue
                    val sum = scores[u].toLong() + scores[v] + scores[a] + scores[b]
                    if (sum > best) best = sum
                }
            }
        }

        return if (best < 0) -1 else best.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumScore(List<int> scores, List<List<int>> edges) {
    int n = scores.length;
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // For each node keep up to 3 neighbors with highest scores
    List<List<int>> top = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      List<int> neigh = adj[i];
      neigh.sort((a, b) => scores[b].compareTo(scores[a])); // descending by score
      int limit = neigh.length < 3 ? neigh.length : 3;
      top[i] = neigh.sublist(0, limit);
    }

    int ans = -1;

    for (var e in edges) {
      int u = e[0];
      int v = e[1];

      // orientation: u as middle left, v as middle right
      for (int a in top[u]) {
        if (a == v) continue;
        for (int d in top[v]) {
          if (d == u || d == a) continue;
          int sum = scores[a] + scores[u] + scores[v] + scores[d];
          if (sum > ans) ans = sum;
        }
      }

      // orientation: v as middle left, u as middle right
      for (int a in top[v]) {
        if (a == u) continue;
        for (int d in top[u]) {
          if (d == v || d == a) continue;
          int sum = scores[a] + scores[v] + scores[u] + scores[d];
          if (sum > ans) ans = sum;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maximumScore(scores []int, edges [][]int) int {
    n := len(scores)
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    top := make([][]int, n)
    for u := 0; u < n; u++ {
        best := make([]int, 0, 3)
        for _, v := range adj[u] {
            best = append(best, v)
            i := len(best) - 1
            for i > 0 && scores[best[i]] > scores[best[i-1]] {
                best[i], best[i-1] = best[i-1], best[i]
                i--
            }
            if len(best) > 3 {
                best = best[:3]
            }
        }
        top[u] = best
    }

    maxScore := -1
    for _, e := range edges {
        u, v := e[0], e[1]

        // orientation u -> v
        for _, a := range top[u] {
            if a == v {
                continue
            }
            for _, d := range top[v] {
                if d == u || d == a {
                    continue
                }
                sum := scores[a] + scores[u] + scores[v] + scores[d]
                if sum > maxScore {
                    maxScore = sum
                }
            }
        }

        // orientation v -> u
        for _, a := range top[v] {
            if a == u {
                continue
            }
            for _, d := range top[u] {
                if d == v || d == a {
                    continue
                }
                sum := scores[a] + scores[v] + scores[u] + scores[d]
                if sum > maxScore {
                    maxScore = sum
                }
            }
        }
    }

    return maxScore
}
```

## Ruby

```ruby
def maximum_score(scores, edges)
  n = scores.length
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  top = Array.new(n) { [] }
  (0...n).each do |u|
    neigh = adj[u].sort_by { |v| -scores[v] }
    top[u] = neigh[0, 3]
  end

  max_sum = -1
  edges.each do |b, c|
    cand_a = top[b].reject { |a| a == c }
    cand_d = top[c].reject { |d| d == b }
    next if cand_a.empty? || cand_d.empty?

    cand_a.each do |a|
      cand_d.each do |d|
        next if a == d || a == b || a == c || d == b || d == c
        sum = scores[a] + scores[b] + scores[c] + scores[d]
        max_sum = sum if sum > max_sum
      end
    end
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maximumScore(scores: Array[Int], edges: Array[Array[Int]]): Int = {
        val n = scores.length
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        // top 3 neighbors with highest scores for each node
        val top = Array.ofDim[Array[(Int, Int)]](n)
        for (i <- 0 until n) {
            val arr = adj(i)
                .map(j => (scores(j), j))
                .sortBy(-_._1)
                .take(3)
                .toArray
            top(i) = arr
        }

        var best: Long = -1L

        for (e <- edges) {
            val u = e(0)
            val v = e(1)

            for ((scoreA, a) <- top(u)) {
                if (a == v) {} else {
                    for ((scoreB, b) <- top(v)) {
                        if (b == u || b == a) {}
                        else {
                            val total = scores(u).toLong + scores(v) + scores(a) + scores(b)
                            if (total > best) best = total
                        }
                    }
                }
            }
        }

        if (best < 0) -1 else best.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score(scores: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = scores.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in &edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // For each node keep up to 3 neighbors with highest scores
        let mut top: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 0..n {
            let mut neigh: Vec<(i32, usize)> = adj[i]
                .iter()
                .map(|&j| (scores[j], j))
                .collect();
            neigh.sort_by(|a, b| b.0.cmp(&a.0)); // descending by score
            let limit = if neigh.len() > 3 { 3 } else { neigh.len() };
            top[i] = neigh.iter().take(limit).map(|&(_, idx)| idx).collect();
        }

        let mut ans: i64 = -1;
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            for &a in &top[u] {
                if a == v { continue; }
                for &b in &top[v] {
                    if b == u || b == a { continue; }
                    let sum = scores[u] as i64 + scores[v] as i64
                        + scores[a] as i64 + scores[b] as i64;
                    if sum > ans { ans = sum; }
                }
            }
        }

        if ans < 0 { -1 } else { ans as i32 }
    }
}
```

## Racket

```racket
(define (take lst k)
  (if (or (= k 0) (null? lst))
      '()
      (cons (car lst) (take (cdr lst) (- k 1)))))

(define/contract (maximum-score scores edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length scores))
         (score-vec (list->vector scores))
         (adj (make-vector n '()))
         ;; build adjacency lists
         (add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v)))))
         )
    (for-each (lambda (e)
                (let ((u (first e))
                      (v (second e)))
                  (add-edge u v)))
              edges)

    ;; compute top 3 neighbors by score for each node
    (define top-neigh (make-vector n '()))
    (do ((i 0 (+ i 1))) ((= i n))
      (let* ((nbrs (vector-ref adj i))
             (pairs (map (lambda (nb) (cons (vector-ref score-vec nb) nb)) nbrs))
             (sorted (sort pairs (lambda (a b) (> (car a) (car b)))))
             (top (take sorted 3))
             (neighbors (map cdr top)))
        (vector-set! top-neigh i neighbors)))

    ;; evaluate each edge as middle pair
    (define best -1)
    (for-each (lambda (e)
                (let ((b (first e))
                      (c (second e)))
                  (for ([a (vector-ref top-neigh b)])
                    (when (not (= a c))
                      (for ([d (vector-ref top-neigh c)])
                        (when (and (not (= d b)) (not (= a d)))
                          (let ((sum (+ (vector-ref score-vec a)
                                        (vector-ref score-vec b)
                                        (vector-ref score-vec c)
                                        (vector-ref score-vec d))))
                            (when (> sum best) (set! best sum)))))))))
              edges)
    best))
```

## Erlang

```erlang
-module(solution).
-export([maximum_score/2]).
-spec maximum_score(Scores :: [integer()], Edges :: [[integer()]]) -> integer().
maximum_score(Scores, Edges) ->
    ScoresTuple = list_to_tuple(Scores),
    AdjMap = build_adj(Edges, #{}),
    TopMap = build_top_map(AdjMap, ScoresTuple),
    compute_max(Edges, ScoresTuple, TopMap, -1).

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

build_top_map(AdjMap, ScoresTuple) ->
    maps:fold(fun(Node, Neighs, Acc) ->
        ScoreNeigh = [{element(N+1, ScoresTuple), N} || N <- Neighs],
        Sorted = lists:sort(fun({S1,_},{S2,_}) -> S1 > S2 end, ScoreNeigh),
        Top3 = [N || {_Score,N} <- lists:sublist(Sorted, 3)],
        maps:put(Node, Top3, Acc)
    end, #{}, AdjMap).

compute_max(Edges, ScoresTuple, TopMap, Init) ->
    lists:foldl(fun([B,C], MaxAcc) ->
        TopB = maps:get(B, TopMap, []),
        TopC = maps:get(C, TopMap, []),
        ScoreB = element(B+1, ScoresTuple),
        ScoreC = element(C+1, ScoresTuple),
        NewMax = lists:foldl(fun(A, CurMax) ->
            if A == C -> CurMax;
               true ->
                ScoreA = element(A+1, ScoresTuple),
                lists:foldl(fun(D, Cur2) ->
                    if D == B orelse D == A -> Cur2;
                       true ->
                        ScoreD = element(D+1, ScoresTuple),
                        Sum = ScoreA + ScoreB + ScoreC + ScoreD,
                        case Sum > Cur2 of
                            true -> Sum;
                            false -> Cur2
                        end
                    end
                , CurMax, TopC)
            end
        end, MaxAcc, TopB),
        NewMax
    end, Init, Edges).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score(scores :: [integer], edges :: [[integer]]) :: integer
  def maximum_score(scores, edges) do
    n = length(scores)
    scores_t = List.to_tuple(scores)

    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [v], &[v | &1])
        |> Map.update(v, [u], &[u | &1])
      end)

    top_lists =
      for i <- 0..(n - 1) do
        neighs = Map.get(adj, i, [])
        sorted = Enum.sort_by(neighs, fn nb -> elem(scores_t, nb) end, &>=/2)
        Enum.take(sorted, 3)
      end

    top_t = List.to_tuple(top_lists)

    Enum.reduce(edges, -1, fn [u, v], acc ->
      best1 = compute_best(u, v, scores_t, top_t)
      best2 = compute_best(v, u, scores_t, top_t)
      max(acc, max(best1, best2))
    end)
  end

  defp compute_best(l, r, scores_t, top_t) do
    left_neis = elem(top_t, l)
    right_neis = elem(top_t, r)

    Enum.reduce(left_neis, -1, fn a, acc_a ->
      if a == r do
        acc_a
      else
        Enum.reduce(right_neis, acc_a, fn d, acc_d ->
          if d == l or d == a do
            acc_d
          else
            sum =
              elem(scores_t, a) + elem(scores_t, l) + elem(scores_t, r) +
                elem(scores_t, d)

            if sum > acc_d, do: sum, else: acc_d
          end
        end)
      end
    end)
  end
end
```
