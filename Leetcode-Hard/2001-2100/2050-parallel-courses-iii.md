# 2050. Parallel Courses III

## Cpp

```cpp
class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> graph(n);
        vector<int> indeg(n, 0);
        for (auto& rel : relations) {
            int u = rel[0] - 1;
            int v = rel[1] - 1;
            graph[u].push_back(v);
            ++indeg[v];
        }
        queue<int> q;
        vector<long long> dp(n, 0);
        for (int i = 0; i < n; ++i) {
            if (indeg[i] == 0) {
                q.push(i);
                dp[i] = time[i];
            }
        }
        long long ans = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            ans = max(ans, dp[u]);
            for (int v : graph[u]) {
                if (dp[v] < dp[u] + time[v])
                    dp[v] = dp[u] + time[v];
                if (--indeg[v] == 0)
                    q.push(v);
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        // Build graph and indegree array
        @SuppressWarnings("unchecked")
        java.util.List<Integer>[] graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new java.util.ArrayList<>();
        }
        int[] indeg = new int[n];
        for (int[] rel : relations) {
            int u = rel[0] - 1;
            int v = rel[1] - 1;
            graph[u].add(v);
            indeg[v]++;
        }

        // Queue for Kahn's algorithm
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        int[] maxTime = new int[n];
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                queue.add(i);
                maxTime[i] = time[i];
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.poll();
            int curTime = maxTime[node];
            for (int nb : graph[node]) {
                // Update the maximum time to reach neighbor
                if (curTime + time[nb] > maxTime[nb]) {
                    maxTime[nb] = curTime + time[nb];
                }
                indeg[nb]--;
                if (indeg[nb] == 0) {
                    queue.add(nb);
                }
            }
        }

        int answer = 0;
        for (int t : maxTime) {
            if (t > answer) answer = t;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        from collections import deque

        # Build graph and indegree array
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            indeg[v] += 1

        # maxTime[i]: earliest completion time of course i
        maxTime = [0] * n
        q = deque()

        for i in range(n):
            if indeg[i] == 0:
                maxTime[i] = time[i]
                q.append(i)

        while q:
            node = q.popleft()
            cur_time = maxTime[node]
            for nb in graph[node]:
                # Update earliest completion for neighbor
                if maxTime[nb] < cur_time + time[nb]:
                    maxTime[nb] = cur_time + time[nb]
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        return max(maxTime)
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            indeg[v] += 1

        max_time = [0] * n
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                max_time[i] = time[i]
                q.append(i)

        while q:
            u = q.popleft()
            cur = max_time[u]
            for v in graph[u]:
                # update the earliest finish time for v
                if max_time[v] < cur + time[v]:
                    max_time[v] = cur + time[v]
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return max(max_time)
```

## C

```c
#include <stdlib.h>

int minimumTime(int n, int** relations, int relationsSize, int* relationsColSize,
                int* time, int timeSize) {
    (void)relationsColSize; // unused
    int *indeg = (int *)calloc(n, sizeof(int));
    int *outCnt = (int *)calloc(n, sizeof(int));

    for (int i = 0; i < relationsSize; ++i) {
        int u = relations[i][0] - 1;
        int v = relations[i][1] - 1;
        indeg[v]++;
        outCnt[u]++;
    }

    int **adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        if (outCnt[i] > 0)
            adj[i] = (int *)malloc(outCnt[i] * sizeof(int));
        else
            adj[i] = NULL;
    }

    int *pos = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < relationsSize; ++i) {
        int u = relations[i][0] - 1;
        int v = relations[i][1] - 1;
        adj[u][pos[u]++] = v;
    }

    int *queue = (int *)malloc(n * sizeof(int));
    int front = 0, back = 0;

    int *maxTime = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (indeg[i] == 0) {
            queue[back++] = i;
            maxTime[i] = time[i];
        }
    }

    while (front < back) {
        int u = queue[front++];
        for (int k = 0; k < outCnt[u]; ++k) {
            int v = adj[u][k];
            if (maxTime[u] + time[v] > maxTime[v])
                maxTime[v] = maxTime[u] + time[v];
            indeg[v]--;
            if (indeg[v] == 0)
                queue[back++] = v;
        }
    }

    int answer = 0;
    for (int i = 0; i < n; ++i) {
        if (maxTime[i] > answer)
            answer = maxTime[i];
    }

    // free allocated memory
    for (int i = 0; i < n; ++i) {
        if (adj[i]) free(adj[i]);
    }
    free(adj);
    free(indeg);
    free(outCnt);
    free(pos);
    free(queue);
    free(maxTime);

    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumTime(int n, int[][] relations, int[] time)
    {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        var indegree = new int[n];

        foreach (var rel in relations)
        {
            int u = rel[0] - 1;
            int v = rel[1] - 1;
            graph[u].Add(v);
            indegree[v]++;
        }

        var dp = new int[n];
        var queue = new Queue<int>();

        for (int i = 0; i < n; i++)
        {
            dp[i] = time[i];
            if (indegree[i] == 0)
                queue.Enqueue(i);
        }

        while (queue.Count > 0)
        {
            int u = queue.Dequeue();
            foreach (int v in graph[u])
            {
                if (dp[v] < dp[u] + time[v])
                    dp[v] = dp[u] + time[v];
                indegree[v]--;
                if (indegree[v] == 0)
                    queue.Enqueue(v);
            }
        }

        int answer = 0;
        foreach (int val in dp)
            if (val > answer) answer = val;
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number[]} time
 * @return {number}
 */
var minimumTime = function(n, relations, time) {
    const graph = Array.from({ length: n }, () => []);
    const indegree = new Int32Array(n);
    
    for (const [u, v] of relations) {
        const a = u - 1;
        const b = v - 1;
        graph[a].push(b);
        indegree[b]++;
    }
    
    const maxTime = new Int32Array(n);
    const queue = [];
    let head = 0;
    
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
            maxTime[i] = time[i];
        }
    }
    
    while (head < queue.length) {
        const node = queue[head++];
        const cur = maxTime[node];
        for (const nb of graph[node]) {
            // update the longest path ending at neighbor
            const candidate = cur + time[nb];
            if (candidate > maxTime[nb]) {
                maxTime[nb] = candidate;
            }
            indegree[nb]--;
            if (indegree[nb] === 0) {
                queue.push(nb);
            }
        }
    }
    
    let answer = 0;
    for (let i = 0; i < n; i++) {
        if (maxTime[i] > answer) answer = maxTime[i];
    }
    return answer;
};
```

## Typescript

```typescript
function minimumTime(n: number, relations: number[][], time: number[]): number {
    const graph: number[][] = Array.from({ length: n }, () => []);
    const indeg = new Uint32Array(n);
    for (const [u, v] of relations) {
        const a = u - 1;
        const b = v - 1;
        graph[a].push(b);
        indeg[b]++;
    }
    const maxTime = new Float64Array(n);
    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) {
            maxTime[i] = time[i];
            queue[tail++] = i;
        }
    }
    while (head < tail) {
        const node = queue[head++];
        const cur = maxTime[node];
        for (const nb of graph[node]) {
            const cand = cur + time[nb];
            if (cand > maxTime[nb]) {
                maxTime[nb] = cand;
            }
            indeg[nb]--;
            if (indeg[nb] === 0) {
                queue[tail++] = nb;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (maxTime[i] > ans) ans = maxTime[i];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @param Integer[] $time
     * @return Integer
     */
    function minimumTime($n, $relations, $time) {
        // Build graph and indegree array
        $graph = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);
        foreach ($relations as $rel) {
            $u = $rel[0] - 1; // zero‑based index
            $v = $rel[1] - 1;
            $graph[$u][] = $v;
            $indeg[$v]++;
        }

        // Queue for Kahn's algorithm
        $queue = new SplQueue();
        $maxTime = array_fill(0, $n, 0);

        // Initialize queue with nodes having indegree 0
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] === 0) {
                $queue->enqueue($i);
                $maxTime[$i] = $time[$i];
            }
        }

        // Process nodes in topological order
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            foreach ($graph[$u] as $v) {
                $candidate = $maxTime[$u] + $time[$v];
                if ($candidate > $maxTime[$v]) {
                    $maxTime[$v] = $candidate;
                }
                $indeg[$v]--;
                if ($indeg[$v] === 0) {
                    $queue->enqueue($v);
                }
            }
        }

        // The answer is the maximum accumulated time
        return max($maxTime);
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ n: Int, _ relations: [[Int]], _ time: [Int]) -> Int {
        var graph = Array(repeating: [Int](), count: n)
        var indegree = Array(repeating: 0, count: n)
        
        for rel in relations {
            let u = rel[0] - 1
            let v = rel[1] - 1
            graph[u].append(v)
            indegree[v] += 1
        }
        
        var maxTime = Array(repeating: 0, count: n)
        var queue = [Int]()
        queue.reserveCapacity(n)
        
        for i in 0..<n {
            if indegree[i] == 0 {
                queue.append(i)
                maxTime[i] = time[i]
            }
        }
        
        var idx = 0
        while idx < queue.count {
            let node = queue[idx]
            idx += 1
            let cur = maxTime[node]
            for neighbor in graph[node] {
                let cand = cur + time[neighbor]
                if cand > maxTime[neighbor] {
                    maxTime[neighbor] = cand
                }
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 {
                    queue.append(neighbor)
                }
            }
        }
        
        return maxTime.max() ?? 0
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minimumTime(n: Int, relations: Array<IntArray>, time: IntArray): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        val indegree = IntArray(n)
        for (rel in relations) {
            val u = rel[0] - 1
            val v = rel[1] - 1
            graph[u].add(v)
            indegree[v]++
        }

        val maxTime = IntArray(n)
        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (indegree[i] == 0) {
                maxTime[i] = time[i]
                queue.addLast(i)
            }
        }

        while (!queue.isEmpty()) {
            val u = queue.removeFirst()
            for (v in graph[u]) {
                val candidate = maxTime[u] + time[v]
                if (candidate > maxTime[v]) {
                    maxTime[v] = candidate
                }
                indegree[v]--
                if (indegree[v] == 0) {
                    queue.addLast(v)
                }
            }
        }

        var answer = 0
        for (t in maxTime) {
            if (t > answer) answer = t
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumTime(int n, List<List<int>> relations, List<int> time) {
    // Build graph and indegree array
    List<List<int>> graph = List.generate(n, (_) => []);
    List<int> indeg = List.filled(n, 0);
    for (var rel in relations) {
      int u = rel[0] - 1;
      int v = rel[1] - 1;
      graph[u].add(v);
      indeg[v]++;
    }

    // maxTime[i]: earliest completion time of course i
    List<int> maxTime = List.filled(n, 0);
    List<int> queue = [];

    for (int i = 0; i < n; ++i) {
      if (indeg[i] == 0) {
        maxTime[i] = time[i];
        queue.add(i);
      }
    }

    int qIdx = 0;
    while (qIdx < queue.length) {
      int node = queue[qIdx++];
      for (int nb in graph[node]) {
        int candidate = maxTime[node] + time[nb];
        if (candidate > maxTime[nb]) {
          maxTime[nb] = candidate;
        }
        indeg[nb]--;
        if (indeg[nb] == 0) {
          queue.add(nb);
        }
      }
    }

    int ans = 0;
    for (int v in maxTime) {
      if (v > ans) ans = v;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumTime(n int, relations [][]int, time []int) int {
    graph := make([][]int, n)
    indegree := make([]int, n)

    for _, rel := range relations {
        u := rel[0] - 1
        v := rel[1] - 1
        graph[u] = append(graph[u], v)
        indegree[v]++
    }

    maxTime := make([]int, n)
    queue := make([]int, 0, n)

    for i := 0; i < n; i++ {
        if indegree[i] == 0 {
            queue = append(queue, i)
            maxTime[i] = time[i]
        }
    }

    for front := 0; front < len(queue); front++ {
        node := queue[front]
        cur := maxTime[node]
        for _, nb := range graph[node] {
            if cur+time[nb] > maxTime[nb] {
                maxTime[nb] = cur + time[nb]
            }
            indegree[nb]--
            if indegree[nb] == 0 {
                queue = append(queue, nb)
            }
        }
    }

    ans := 0
    for _, v := range maxTime {
        if v > ans {
            ans = v
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_time(n, relations, time)
  graph = Array.new(n) { [] }
  indegree = Array.new(n, 0)

  relations.each do |prev_course, next_course|
    u = prev_course - 1
    v = next_course - 1
    graph[u] << v
    indegree[v] += 1
  end

  max_time = Array.new(n, 0)
  queue = []
  n.times do |i|
    if indegree[i] == 0
      max_time[i] = time[i]
      queue << i
    end
  end

  idx = 0
  while idx < queue.length
    node = queue[idx]
    idx += 1
    cur_time = max_time[node]

    graph[node].each do |nbr|
      # Update the longest path ending at neighbor
      possible = cur_time + time[nbr]
      max_time[nbr] = possible if possible > max_time[nbr]

      indegree[nbr] -= 1
      queue << nbr if indegree[nbr] == 0
    end
  end

  max_time.max
end
```

## Scala

```scala
object Solution {
  def minimumTime(n: Int, relations: Array[Array[Int]], time: Array[Int]): Int = {
    val graph = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    val indeg = new Array[Int](n)
    for (rel <- relations) {
      val u = rel(0) - 1
      val v = rel(1) - 1
      graph(u).append(v)
      indeg(v) += 1
    }

    val dp = new Array[Long](n)
    val queue = new java.util.ArrayDeque[Int]()

    for (i <- 0 until n) {
      if (indeg(i) == 0) {
        dp(i) = time(i).toLong
        queue.add(i)
      }
    }

    while (!queue.isEmpty) {
      val u = queue.poll()
      val cur = dp(u)
      for (v <- graph(u)) {
        val cand = cur + time(v).toLong
        if (cand > dp(v)) dp(v) = cand
        indeg(v) -= 1
        if (indeg(v) == 0) queue.add(v)
      }
    }

    var ans: Long = 0L
    for (i <- 0 until n) {
      if (dp(i) > ans) ans = dp(i)
    }
    ans.toInt
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indegree: Vec<usize> = vec![0; n];

        for rel in relations.iter() {
            let u = (rel[0] - 1) as usize;
            let v = (rel[1] - 1) as usize;
            graph[u].push(v);
            indegree[v] += 1;
        }

        let mut max_time: Vec<i32> = vec![0; n];
        let mut queue: VecDeque<usize> = VecDeque::new();

        for i in 0..n {
            if indegree[i] == 0 {
                max_time[i] = time[i];
                queue.push_back(i);
            }
        }

        while let Some(u) = queue.pop_front() {
            for &v in graph[u].iter() {
                let candidate = max_time[u] + time[v];
                if candidate > max_time[v] {
                    max_time[v] = candidate;
                }
                indegree[v] -= 1;
                if indegree[v] == 0 {
                    // If the node had no incoming edges (should not happen here), ensure its own time is considered.
                    if max_time[v] == 0 {
                        max_time[v] = time[v];
                    }
                    queue.push_back(v);
                }
            }
        }

        *max_time.iter().max().unwrap()
    }
}
```

## Racket

```racket
#lang racket
(require racket/queue)

(define/contract (minimum-time n relations time)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ([adj   (make-vector n '())]               ; adjacency list
         [indeg (make-vector n 0)]                ; indegree counts
         [_ (for-each
              (lambda (rel)
                (match rel [(list u v)
                            (define ui (- u 1))
                            (define vi (- v 1))
                            (vector-set! adj ui (cons vi (vector-ref adj ui)))
                            (vector-set! indeg vi (+ 1 (vector-ref indeg vi)))])
                )
              relations)]
         [time-vec (list->vector time)]           ; fast random access
         [max-time (make-vector n 0)]             ; longest path ending at each node
         [q (make-queue)])                        ; processing queue

    ;; Initialize sources (indegree == 0)
    (for ([i (in-range n)])
      (when (= (vector-ref indeg i) 0)
        (vector-set! max-time i (vector-ref time-vec i))
        (enqueue! q i)))

    ;; Kahn's algorithm
    (let loop ()
      (unless (queue-empty? q)
        (define node (dequeue! q))
        (for ([nbr (in-list (vector-ref adj node))])
          (define cand (+ (vector-ref max-time node) (vector-ref time-vec nbr)))
          (when (> cand (vector-ref max-time nbr))
            (vector-set! max-time nbr cand))
          (vector-set! indeg nbr (- (vector-ref indeg nbr) 1))
          (when (= (vector-ref indeg nbr) 0)
            (enqueue! q nbr)))
        (loop)))

    ;; Result is the maximum accumulated time
    (let ([ans 0])
      (for ([i (in-range n)])
        (set! ans (max ans (vector-ref max-time i))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time/3]).

-include_lib("kernel/include/logger.hrl").

-spec minimum_time(N :: integer(), Relations :: [[integer()]], Time :: [integer()]) -> integer().
minimum_time(N, Relations, Time) ->
    Adj0 = array:new(N, [{default, []}]),
    Indeg0 = array:new(N, [{default, 0}]),
    {Adj, Indeg} = build_graph(Relations, Adj0, Indeg0, N),
    TimeArr = array:from_list(Time),
    MaxTime0 = array:new(N, [{default, 0}]),
    Queue0 = queue:new(),
    {MaxTime1, Queue1} = init_queue(0, N, Indeg, TimeArr, MaxTime0, Queue0),
    {FinalMaxTime, _FinalIndeg, _FinalQueue} = bfs(Adj, Indeg, TimeArr, MaxTime1, Queue1),
    lists:max(array:to_list(FinalMaxTime)).

%% Build adjacency list and indegree array
-spec build_graph([[integer()]], array:array(), array:array(), integer()) -> {array:array(), array:array()}.
build_graph([], Adj, Indeg, _N) ->
    {Adj, Indeg};
build_graph([[A,B]|Rest], Adj, Indeg, N) ->
    A0 = A - 1,
    B0 = B - 1,
    OldList = array:get(A0, Adj),
    NewAdj = array:set(A0, [B0|OldList], Adj),
    OldIndeg = array:get(B0, Indeg),
    NewIndeg = array:set(B0, OldIndeg + 1, Indeg),
    build_graph(Rest, NewAdj, NewIndeg, N).

%% Initialize queue with nodes of indegree zero and set their max times
-spec init_queue(integer(), integer(), array:array(), array:array(), array:array(), queue:queue()) ->
      {array:array(), queue:queue()}.
init_queue(I, N, _Indeg, _TimeArr, MaxTime, Queue) when I >= N ->
    {MaxTime, Queue};
init_queue(I, N, Indeg, TimeArr, MaxTime, Queue) ->
    case array:get(I, Indeg) of
        0 ->
            CurTime = array:get(I, TimeArr),
            NewMaxTime = array:set(I, CurTime, MaxTime),
            NewQueue = queue:in(I, Queue),
            init_queue(I + 1, N, Indeg, TimeArr, NewMaxTime, NewQueue);
        _Other ->
            init_queue(I + 1, N, Indeg, TimeArr, MaxTime, Queue)
    end.

%% BFS (Kahn's algorithm) processing
-spec bfs(array:array(), array:array(), array:array(), array:array(), queue:queue()) ->
      {array:array(), array:array(), queue:queue()}.
bfs(Adj, Indeg, TimeArr, MaxTime, Queue) ->
    case queue:out(Queue) of
        {empty, _} ->
            {MaxTime, Indeg, Queue};
        {{value, Node}, RestQueue} ->
            CurMax = array:get(Node, MaxTime),
            NeighList = array:get(Node, Adj),
            {NewMaxTime, NewIndeg, NewQueue} =
                process_neighbors(NeighList, CurMax, TimeArr, MaxTime, Indeg, RestQueue),
            bfs(Adj, NewIndeg, TimeArr, NewMaxTime, NewQueue)
    end.

%% Process all outgoing edges from a node
-spec process_neighbors([integer()], integer(), array:array(),
                        array:array(), array:array(), queue:queue()) ->
      {array:array(), array:array(), queue:queue()}.
process_neighbors([], _CurMax, _TimeArr, MaxTime, Indeg, Queue) ->
    {MaxTime, Indeg, Queue};
process_neighbors([Nb|Rest], CurMax, TimeArr, MaxTime, Indeg, Queue) ->
    NbTime = array:get(Nb, TimeArr),
    Cand = CurMax + NbTime,
    Prev = array:get(Nb, MaxTime),
    UpdatedMaxTime = if Cand > Prev -> array:set(Nb, Cand, MaxTime); true -> MaxTime end,
    OldIndeg = array:get(Nb, Indeg),
    NewIndegVal = OldIndeg - 1,
    UpdatedIndeg = array:set(Nb, NewIndegVal, Indeg),
    UpdatedQueue = case NewIndegVal of
                       0 -> queue:in(Nb, Queue);
                       _ -> Queue
                   end,
    process_neighbors(Rest, CurMax, TimeArr, UpdatedMaxTime, UpdatedIndeg, UpdatedQueue).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(integer, [[integer]], [integer]) :: integer
  def minimum_time(n, relations, time) do
    {adj, indeg} =
      Enum.reduce(relations, {%{}, %{}}, fn [u, v], {a, i} ->
        a2 = Map.update(a, u, [v], &[v | &1])
        i2 = Map.update(i, v, 1, &(&1 + 1))
        {a2, i2}
      end)

    q0 = :queue.new()

    {queue, max_time} =
      Enum.reduce(1..n, {q0, %{}}, fn node, {q_acc, mt_acc} ->
        indeg_val = Map.get(indeg, node, 0)

        if indeg_val == 0 do
          q_new = :queue.in(node, q_acc)
          mt_new = Map.put(mt_acc, node, Enum.at(time, node - 1))
          {q_new, mt_new}
        else
          {q_acc, mt_acc}
        end
      end)

    final_max_time = bfs_process(queue, adj, indeg, time, max_time)
    Enum.max(Map.values(final_max_time))
  end

  defp bfs_process(queue, adj, indeg, time, max_time) do
    case :queue.out(queue) do
      {:empty, _} ->
        max_time

      {{:value, node}, q_rest} ->
        cur_time = Map.get(max_time, node)

        {new_queue, new_indeg, new_max_time} =
          Enum.reduce(Map.get(adj, node, []), {q_rest, indeg, max_time}, fn nb,
                                                                          {q_acc, indeg_acc, mt_acc} ->
            nb_time = cur_time + Enum.at(time, nb - 1)

            mt_updated =
              case Map.get(mt_acc, nb) do
                nil -> Map.put(mt_acc, nb, nb_time)
                existing when nb_time > existing -> Map.put(mt_acc, nb, nb_time)
                _ -> mt_acc
              end

            indeg_val = Map.get(indeg_acc, nb, 0) - 1

            indeg_updated =
              if indeg_val == 0 do
                Map.delete(indeg_acc, nb)
              else
                Map.put(indeg_acc, nb, indeg_val)
              end

            q_updated =
              if indeg_val == 0 do
                :queue.in(nb, q_acc)
              else
                q_acc
              end

            {q_updated, indeg_updated, mt_updated}
          end)

        bfs_process(new_queue, adj, new_indeg, time, new_max_time)
    end
  end
end
```
