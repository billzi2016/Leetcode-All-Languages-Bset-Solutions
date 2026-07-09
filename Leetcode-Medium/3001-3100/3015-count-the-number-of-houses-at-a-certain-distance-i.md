# 3015. Count the Number of Houses at a Certain Distance I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countOfPairs(int n, int x, int y) {
        vector<vector<int>> adj(n + 1);
        for (int i = 1; i < n; ++i) {
            adj[i].push_back(i + 1);
            adj[i + 1].push_back(i);
        }
        if (x != y) {
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        vector<int> ans(n + 1, 0); // ans[d] = number of ordered pairs with distance d

        for (int s = 1; s <= n; ++s) {
            vector<int> dist(n + 1, -1);
            queue<int> q;
            dist[s] = 0;
            q.push(s);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            for (int t = 1; t <= n; ++t) {
                if (t == s) continue;
                int d = dist[t];
                ans[d]++;
            }
        }

        vector<int> res(n, 0);
        for (int k = 1; k <= n; ++k) res[k - 1] = ans[k];
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] countOfPairs(int n, int x, int y) {
        List<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            adj[i].add(i + 1);
            adj[i + 1].add(i);
        }
        if (x != y) {
            adj[x].add(y);
            adj[y].add(x);
        }

        int[] ans = new int[n]; // ans[k-1] stores count for distance k

        for (int start = 1; start <= n; start++) {
            int[] dist = new int[n + 1];
            Arrays.fill(dist, -1);
            Queue<Integer> q = new ArrayDeque<>();
            dist[start] = 0;
            q.add(start);

            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.add(v);
                    }
                }
            }

            for (int end = 1; end <= n; end++) {
                if (end == start) continue;
                int d = dist[end];
                ans[d - 1]++; // distance is at least 1
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        from collections import deque

        # build adjacency list (1-indexed)
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n):
            adj[i].append(i + 1)
            adj[i + 1].append(i)
        if x != y:
            adj[x].append(y)
            adj[y].append(x)

        ans = [0] * n  # ans[k-1] stores count for distance k

        for start in range(1, n + 1):
            dist = [-1] * (n + 1)
            dq = deque()
            dq.append(start)
            dist[start] = 0
            while dq:
                u = dq.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        dq.append(v)

            for target in range(1, n + 1):
                if target != start:
                    d = dist[target]
                    ans[d - 1] += 1

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                d = abs(i - j)
                via_xy = abs(i - x) + 1 + abs(y - j)
                via_yx = abs(i - y) + 1 + abs(x - j)
                d = min(d, via_xy, via_yx)
                ans[d - 1] += 1
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countOfPairs(int n, int x, int y, int* returnSize) {
    // adjacency list
    int adj[101][3];
    int deg[101] = {0};
    
    // line edges
    for (int i = 1; i < n; ++i) {
        adj[i][deg[i]++] = i + 1;
        adj[i + 1][deg[i + 1]++] = i;
    }
    // extra edge if different houses
    if (x != y) {
        adj[x][deg[x]++] = y;
        adj[y][deg[y]++] = x;
    }
    
    int* ans = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) ans[i] = 0;
    
    int dist[101];
    int q[101];
    
    for (int s = 1; s <= n; ++s) {
        // initialize distances
        for (int i = 1; i <= n; ++i) dist[i] = -1;
        int front = 0, back = 0;
        q[back++] = s;
        dist[s] = 0;
        
        while (front < back) {
            int u = q[front++];
            for (int k = 0; k < deg[u]; ++k) {
                int v = adj[u][k];
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q[back++] = v;
                }
            }
        }
        
        for (int t = 1; t <= n; ++t) {
            if (t == s) continue;
            int d = dist[t];
            // distances are from 1 to n, array is 0-indexed
            ans[d - 1] += 1;
        }
    }
    
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountOfPairs(int n, int x, int y) {
        var adj = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            adj[i].Add(i + 1);
            adj[i + 1].Add(i);
        }
        if (x != y) {
            adj[x].Add(y);
            adj[y].Add(x);
        }

        int[] result = new int[n];
        for (int start = 1; start <= n; start++) {
            int[] dist = new int[n + 1];
            Array.Fill(dist, -1);
            var q = new Queue<int>();
            dist[start] = 0;
            q.Enqueue(start);

            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.Enqueue(v);
                    }
                }
            }

            for (int j = 1; j <= n; j++) {
                if (j == start) continue;
                int d = dist[j];
                // d is guaranteed to be between 1 and n
                result[d - 1]++;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @param {number} y
 * @return {number[]}
 */
var countOfPairs = function(n, x, y) {
    const res = new Array(n).fill(0);
    for (let i = 1; i <= n; ++i) {
        for (let j = 1; j <= n; ++j) {
            if (i === j) continue;
            const direct = Math.abs(i - j);
            const viaXY = Math.abs(i - x) + 1 + Math.abs(y - j);
            const viaYX = Math.abs(i - y) + 1 + Math.abs(x - j);
            const d = Math.min(direct, viaXY, viaYX);
            res[d - 1]++; // distances are 1-indexed
        }
    }
    return res;
};
```

## Typescript

```typescript
function countOfPairs(n: number, x: number, y: number): number[] {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (let i = 1; i < n; i++) {
        adj[i].push(i + 1);
        adj[i + 1].push(i);
    }
    if (x !== y) {
        adj[x].push(y);
        adj[y].push(x);
    }

    const ans: number[] = new Array(n + 1).fill(0);

    for (let start = 1; start <= n; start++) {
        const dist: number[] = new Array(n + 1).fill(-1);
        const queue: number[] = [];
        dist[start] = 0;
        queue.push(start);
        let qIdx = 0;
        while (qIdx < queue.length) {
            const u = queue[qIdx++];
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    queue.push(v);
                }
            }
        }
        for (let j = 1; j <= n; j++) {
            if (j !== start) {
                ans[dist[j]]++;
            }
        }
    }

    return ans.slice(1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $x
     * @param Integer $y
     * @return Integer[]
     */
    function countOfPairs($n, $x, $y) {
        $ans = array_fill(0, $n, 0);
        for ($i = 1; $i <= $n; ++$i) {
            for ($j = 1; $j <= $n; ++$j) {
                if ($i == $j) continue;
                $direct = abs($i - $j);
                $via1   = abs($i - $x) + 1 + abs($y - $j);
                $via2   = abs($i - $y) + 1 + abs($x - $j);
                $d = min($direct, $via1, $via2);
                // distance is at least 1
                $ans[$d - 1]++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countOfPairs(_ n: Int, _ x: Int, _ y: Int) -> [Int] {
        var adj = [[Int]](repeating: [], count: n + 1)
        if n > 1 {
            for i in 1..<n {
                adj[i].append(i + 1)
                adj[i + 1].append(i)
            }
        }
        if x != y {
            adj[x].append(y)
            adj[y].append(x)
        }
        
        var result = [Int](repeating: 0, count: n)
        
        for start in 1...n {
            var dist = [Int](repeating: -1, count: n + 1)
            var queue = [Int]()
            var head = 0
            dist[start] = 0
            queue.append(start)
            
            while head < queue.count {
                let u = queue[head]
                head += 1
                for v in adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1
                        queue.append(v)
                    }
                }
            }
            
            for target in 1...n where target != start {
                let d = dist[target]
                if d > 0 && d <= n {
                    result[d - 1] += 1
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfPairs(n: Int, x: Int, y: Int): IntArray {
        val cnt = IntArray(n + 1)
        for (i in 1..n) {
            for (j in 1..n) {
                if (i == j) continue
                val direct = kotlin.math.abs(i - j)
                val viaXY = kotlin.math.abs(i - x) + 1 + kotlin.math.abs(y - j)
                val viaYX = kotlin.math.abs(i - y) + 1 + kotlin.math.abs(x - j)
                val d = minOf(direct, viaXY, viaYX)
                cnt[d]++
            }
        }
        return cnt.copyOfRange(1, n + 1)
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> countOfPairs(int n, int x, int y) {
    // Build adjacency list for the graph
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    for (int i = 1; i < n; ++i) {
      adj[i].add(i + 1);
      adj[i + 1].add(i);
    }
    if (x != y) {
      adj[x].add(y);
      adj[y].add(x);
    }

    List<int> result = List.filled(n, 0); // result[k-1] stores count for distance k

    // Perform BFS from each node
    for (int start = 1; start <= n; ++start) {
      List<int> dist = List.filled(n + 1, -1);
      Queue<int> q = Queue<int>();
      dist[start] = 0;
      q.add(start);

      while (q.isNotEmpty) {
        int cur = q.removeFirst();
        for (int nb in adj[cur]) {
          if (dist[nb] == -1) {
            dist[nb] = dist[cur] + 1;
            q.add(nb);
          }
        }
      }

      // Accumulate distances to other nodes
      for (int v = 1; v <= n; ++v) {
        if (v == start) continue;
        int d = dist[v];
        result[d - 1] += 1; // ordered pair (start, v)
      }
    }

    return result;
  }
}
```

## Golang

```go
func countOfPairs(n int, x int, y int) []int {
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	ans := make([]int, n)
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if i == j {
				continue
			}
			d := abs(i - j)
			alt1 := abs(i-x) + 1 + abs(y-j)
			if alt1 < d {
				d = alt1
			}
			alt2 := abs(i-y) + 1 + abs(x-j)
			if alt2 < d {
				d = alt2
			}
			ans[d-1]++
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_of_pairs(n, x, y)
  res = Array.new(n + 1, 0)
  (1..n).each do |i|
    (1..n).each do |j|
      next if i == j
      d1 = (i - j).abs
      d2 = (i - x).abs + 1 + (y - j).abs
      d3 = (i - y).abs + 1 + (x - j).abs
      d = [d1, d2, d3].min
      res[d] += 1
    end
  end
  res[1..n]
end
```

## Scala

```scala
object Solution {
  def countOfPairs(n: Int, x: Int, y: Int): Array[Int] = {
    val adj = Array.fill(n + 1)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (i <- 1 until n) {
      adj(i).append(i + 1)
      adj(i + 1).append(i)
    }
    if (x != y) {
      adj(x).append(y)
      adj(y).append(x)
    }

    val ans = Array.fill(n + 1)(0L)
    val dist = new Array[Int](n + 1)

    import scala.collection.mutable.ArrayDeque

    for (s <- 1 to n) {
      java.util.Arrays.fill(dist, -1)
      val q = ArrayDeque[Int]()
      dist(s) = 0
      q.append(s)

      while (q.nonEmpty) {
        val u = q.removeHead()
        val du = dist(u)
        for (v <- adj(u)) {
          if (dist(v) == -1) {
            dist(v) = du + 1
            q.append(v)
          }
        }
      }

      for (t <- 1 to n if t != s) {
        ans(dist(t)) += 1
      }
    }

    val res = new Array[Int](n)
    for (k <- 1 to n) {
      res(k - 1) = ans(k).toInt
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_of_pairs(n: i32, x: i32, y: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize + 1];
        for i in 1..n_usize {
            adj[i].push(i + 1);
            adj[i + 1].push(i);
        }
        if x != y {
            let xi = x as usize;
            let yi = y as usize;
            adj[xi].push(yi);
            adj[yi].push(xi);
        }

        let mut result: Vec<i32> = vec![0; n_usize];
        use std::collections::VecDeque;

        for start in 1..=n_usize {
            let mut dist: Vec<i32> = vec![-1; n_usize + 1];
            let mut q: VecDeque<usize> = VecDeque::new();
            dist[start] = 0;
            q.push_back(start);
            while let Some(u) = q.pop_front() {
                let du = dist[u];
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = du + 1;
                        q.push_back(v);
                    }
                }
            }
            for target in 1..=n_usize {
                if target == start {
                    continue;
                }
                let d = dist[target] as usize; // distance is at least 1
                result[d - 1] += 1;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (count-of-pairs n x y)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let* ((ans (make-vector (+ n 1) 0))) ; ans[d] stores count for distance d
    (for ([i (in-range 1 (add1 n))])
      (for ([j (in-range 1 (add1 n))])
        (when (not (= i j))
          (define d   (abs (- i j)))
          (define alt1 (+ (abs (- i x)) 1 (abs (- y j))))
          (define alt2 (+ (abs (- i y)) 1 (abs (- x j))))
          (define dist (min d alt1 alt2))
          (vector-set! ans dist (add1 (vector-ref ans dist))))))
    ; build result list for distances 1..n
    (let loop ((k 1) (acc '()))
      (if (> k n)
          (reverse acc)
          (loop (+ k 1) (cons (vector-ref ans k) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([count_of_pairs/3]).

-spec count_of_pairs(N :: integer(), X :: integer(), Y :: integer()) -> [integer()].
count_of_pairs(N, X, Y) ->
    Counts0 = erlang:make_tuple(N, 0),
    Counts1 = loop_i(1, N, X, Y, Counts0),
    tuple_to_list(Counts1).

loop_i(I, N, _X, _Y, Counts) when I > N -> Counts;
loop_i(I, N, X, Y, Counts) ->
    NewCounts = loop_j(I, 1, N, X, Y, Counts),
    loop_i(I + 1, N, X, Y, NewCounts).

loop_j(_I, J, N, _X, _Y, Counts) when J > N -> Counts;
loop_j(I, J, N, X, Y, Counts) ->
    case I == J of
        true ->
            loop_j(I, J + 1, N, X, Y, Counts);
        false ->
            Direct = abs(I - J),
            ViaXY = abs(I - X) + 1 + abs(Y - J),
            ViaYX = abs(I - Y) + 1 + abs(X - J),
            D = erlang:min(Direct, erlang:min(ViaXY, ViaYX)),
            Cur = element(D, Counts),
            Updated = setelement(D, Counts, Cur + 1),
            loop_j(I, J + 1, N, X, Y, Updated)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_of_pairs(n :: integer, x :: integer, y :: integer) :: [integer]
  def count_of_pairs(n, x, y) do
    ans0 = List.duplicate(0, n)

    for i <- 1..n, reduce: ans0 do
      acc_i ->
        for j <- 1..n, reduce: acc_i do
          acc_j ->
            if i == j do
              acc_j
            else
              d = abs(i - j)
              via1 = abs(i - x) + 1 + abs(y - j)
              via2 = abs(i - y) + 1 + abs(x - j)
              dist = Enum.min([d, via1, via2])
              idx = dist - 1
              old = Enum.at(acc_j, idx)
              List.replace_at(acc_j, idx, old + 1)
            end
        end
    end
  end
end
```
