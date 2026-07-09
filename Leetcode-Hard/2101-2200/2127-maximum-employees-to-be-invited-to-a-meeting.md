# 2127. Maximum Employees to Be Invited to a Meeting

## Cpp

```cpp
class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        int n = favorite.size();
        vector<int> indeg(n, 0);
        for (int i = 0; i < n; ++i) indeg[favorite[i]]++;
        
        queue<int> q;
        vector<int> depth(n, 1); // longest chain length ending at node (including itself)
        for (int i = 0; i < n; ++i) {
            if (indeg[i] == 0) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            int v = favorite[u];
            depth[v] = max(depth[v], depth[u] + 1);
            if (--indeg[v] == 0) q.push(v);
        }
        
        int maxCycle = 0;
        int twoCycleSum = 0;
        for (int i = 0; i < n; ++i) {
            if (indeg[i] > 0) { // part of a cycle
                int cur = i;
                int len = 0;
                while (indeg[cur] > 0) {
                    indeg[cur] = 0; // mark visited
                    cur = favorite[cur];
                    ++len;
                }
                if (len == 2) {
                    int a = i;
                    int b = favorite[i];
                    twoCycleSum += depth[a] + depth[b];
                } else {
                    maxCycle = max(maxCycle, len);
                }
            }
        }
        return max(maxCycle, twoCycleSum);
    }
};
```

## Java

```java
class Solution {
    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;
        int[] indegree = new int[n];
        for (int i = 0; i < n; i++) {
            indegree[favorite[i]]++;
        }

        int[] depth = new int[n];
        java.util.Arrays.fill(depth, 1);
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int u = queue.poll();
            int v = favorite[u];
            if (depth[v] < depth[u] + 1) {
                depth[v] = depth[u] + 1;
            }
            indegree[v]--;
            if (indegree[v] == 0) {
                queue.add(v);
            }
        }

        boolean[] visited = new boolean[n];
        int maxCycle = 0;
        int sumTwoCycles = 0;

        for (int i = 0; i < n; i++) {
            if (indegree[i] > 0 && !visited[i]) {
                java.util.ArrayList<Integer> cycle = new java.util.ArrayList<>();
                int cur = i;
                while (!visited[cur]) {
                    visited[cur] = true;
                    cycle.add(cur);
                    cur = favorite[cur];
                }
                int sz = cycle.size();
                if (sz == 2) {
                    int a = cycle.get(0), b = cycle.get(1);
                    sumTwoCycles += depth[a] + depth[b];
                } else {
                    maxCycle = Math.max(maxCycle, sz);
                }
            }
        }

        return Math.max(maxCycle, sumTwoCycles);
    }
}
```

## Python

```python
import collections

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1

        depth = [0] * n
        q = collections.deque([i for i in range(n) if indeg[i] == 0])

        while q:
            u = q.popleft()
            v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        visited = [False] * n
        max_cycle = 0
        pair_sum = 0

        for i in range(n):
            if indeg[i] > 0 and not visited[i]:
                cur = i
                cycle_nodes = []
                while not visited[cur]:
                    visited[cur] = True
                    cycle_nodes.append(cur)
                    cur = favorite[cur]
                cyc_len = len(cycle_nodes)
                if cyc_len == 2:
                    a, b = cycle_nodes[0], cycle_nodes[1]
                    pair_sum += 2 + depth[a] + depth[b]
                else:
                    max_cycle = max(max_cycle, cyc_len)

        return max(max_cycle, pair_sum)
```

## Python3

```python
import collections
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for i, f in enumerate(favorite):
            indeg[f] += 1

        depth = [0] * n
        q = collections.deque([i for i in range(n) if indeg[i] == 0])
        while q:
            u = q.popleft()
            v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        max_cycle = 0
        two_cycle_sum = 0
        for i in range(n):
            if indeg[i] > 0:  # part of a cycle
                cnt = 0
                cur = i
                while indeg[cur] > 0:
                    indeg[cur] = 0
                    cnt += 1
                    cur = favorite[cur]
                if cnt == 2:
                    a = i
                    b = favorite[i]
                    two_cycle_sum += depth[a] + depth[b] + 2
                else:
                    max_cycle = max(max_cycle, cnt)

        return max(max_cycle, two_cycle_sum)
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maximumInvitations(int* favorite, int favoriteSize) {
    int n = favoriteSize;
    int *indeg = (int *)calloc(n, sizeof(int));
    int *depth = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) depth[i] = 1;

    for (int i = 0; i < n; ++i) {
        indeg[favorite[i]]++;
    }

    int *queue = (int *)malloc(n * sizeof(int));
    int head = 0, tail = 0;
    for (int i = 0; i < n; ++i) {
        if (indeg[i] == 0) queue[tail++] = i;
    }

    while (head < tail) {
        int u = queue[head++];
        int v = favorite[u];
        if (depth[v] < depth[u] + 1) depth[v] = depth[u] + 1;
        indeg[v]--;
        if (indeg[v] == 0) queue[tail++] = v;
    }

    int maxCycle = 0;
    int sumTwoCycles = 0;

    for (int i = 0; i < n; ++i) {
        if (indeg[i] > 0) {
            int cur = i, len = 0;
            while (indeg[cur] > 0) {
                indeg[cur] = 0;          // mark visited
                len++;
                cur = favorite[cur];
            }
            if (len == 2) {
                int a = i;
                int b = favorite[i];
                sumTwoCycles += depth[a] + depth[b];
            } else {
                if (len > maxCycle) maxCycle = len;
            }
        }
    }

    free(indeg);
    free(depth);
    free(queue);

    return maxCycle > sumTwoCycles ? maxCycle : sumTwoCycles;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumInvitations(int[] favorite) {
        int n = favorite.Length;
        int[] indeg = new int[n];
        for (int i = 0; i < n; i++) {
            indeg[favorite[i]]++;
        }

        int[] depth = new int[n];
        Queue<int> q = new Queue<int>();
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) q.Enqueue(i);
        }

        while (q.Count > 0) {
            int u = q.Dequeue();
            int v = favorite[u];
            depth[v] = Math.Max(depth[v], depth[u] + 1);
            indeg[v]--;
            if (indeg[v] == 0) q.Enqueue(v);
        }

        bool[] visited = new bool[n];
        int maxCycle = 0;
        int pairSum = 0;

        for (int i = 0; i < n; i++) {
            if (indeg[i] > 0 && !visited[i]) {
                List<int> cycleNodes = new List<int>();
                int cur = i;
                while (!visited[cur]) {
                    visited[cur] = true;
                    cycleNodes.Add(cur);
                    cur = favorite[cur];
                }

                int len = cycleNodes.Count;
                if (len == 2) {
                    int a = cycleNodes[0];
                    int b = cycleNodes[1];
                    pairSum += 2 + depth[a] + depth[b];
                } else {
                    maxCycle = Math.Max(maxCycle, len);
                }
            }
        }

        return Math.Max(maxCycle, pairSum);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} favorite
 * @return {number}
 */
var maximumInvitations = function(favorite) {
    const n = favorite.length;
    const indeg = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        indeg[favorite[i]]++;
    }
    
    const depth = new Array(n).fill(1); // longest chain ending at node, including the node itself
    const queue = [];
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) queue.push(i);
    }
    
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const v = favorite[u];
        depth[v] = Math.max(depth[v], depth[u] + 1);
        indeg[v]--;
        if (indeg[v] === 0) queue.push(v);
    }
    
    let maxCycle = 0;
    let pairSum = 0;
    
    for (let i = 0; i < n; i++) {
        if (indeg[i] > 0) { // part of a cycle
            const nodes = [];
            let cur = i;
            while (indeg[cur] > 0) {
                indeg[cur] = 0; // mark visited
                nodes.push(cur);
                cur = favorite[cur];
            }
            if (nodes.length === 2) {
                const a = nodes[0], b = nodes[1];
                pairSum += depth[a] + depth[b]; // includes the two nodes themselves
            } else {
                maxCycle = Math.max(maxCycle, nodes.length);
            }
        }
    }
    
    return Math.max(maxCycle, pairSum);
};
```

## Typescript

```typescript
function maximumInvitations(favorite: number[]): number {
    const n = favorite.length;
    const indeg = new Array<number>(n).fill(0);
    for (let i = 0; i < n; i++) {
        indeg[favorite[i]]++;
    }

    const depth = new Array<number>(n).fill(0);
    const queue: number[] = [];
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) queue.push(i);
    }

    let qIdx = 0;
    while (qIdx < queue.length) {
        const u = queue[qIdx++];
        const v = favorite[u];
        if (depth[u] + 1 > depth[v]) depth[v] = depth[u] + 1;
        indeg[v]--;
        if (indeg[v] === 0) queue.push(v);
    }

    let maxCycle = 0;
    let pairSum = 0;

    for (let i = 0; i < n; i++) {
        if (indeg[i] > 0) {
            // traverse this cycle
            let cur = i;
            let len = 0;
            while (indeg[cur] > 0) {
                indeg[cur] = 0; // mark visited
                cur = favorite[cur];
                len++;
            }
            if (len === 2) {
                const a = i;
                const b = favorite[a];
                pairSum += 2 + depth[a] + depth[b];
            } else {
                maxCycle = Math.max(maxCycle, len);
            }
        }
    }

    return Math.max(maxCycle, pairSum);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $favorite
     * @return Integer
     */
    function maximumInvitations($favorite) {
        $n = count($favorite);
        $indeg = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $indeg[$favorite[$i]]++;
        }

        $depth = array_fill(0, $n, 0);
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $v = $favorite[$u];
            $newDepth = $depth[$u] + 1;
            if ($newDepth > $depth[$v]) {
                $depth[$v] = $newDepth;
            }
            $indeg[$v]--;
            if ($indeg[$v] == 0) {
                $queue->enqueue($v);
            }
        }

        $maxCycle = 0;
        $pairSum = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] > 0) {
                $len = 0;
                $cur = $i;
                while ($indeg[$cur] > 0) {
                    $indeg[$cur] = 0;
                    $cur = $favorite[$cur];
                    $len++;
                }
                if ($len == 2) {
                    $a = $i;
                    $b = $favorite[$i];
                    $pairSum += 2 + $depth[$a] + $depth[$b];
                } else {
                    if ($len > $maxCycle) {
                        $maxCycle = $len;
                    }
                }
            }
        }

        return max($maxCycle, $pairSum);
    }
}
```

## Swift

```swift
class Solution {
    func maximumInvitations(_ favorite: [Int]) -> Int {
        let n = favorite.count
        var indeg = Array(repeating: 0, count: n)
        for v in favorite {
            indeg[v] += 1
        }
        var depth = Array(repeating: 1, count: n) // longest chain ending at node (including itself)
        var queue = [Int]()
        var head = 0
        for i in 0..<n where indeg[i] == 0 {
            queue.append(i)
        }
        while head < queue.count {
            let u = queue[head]
            head += 1
            let v = favorite[u]
            if depth[u] + 1 > depth[v] {
                depth[v] = depth[u] + 1
            }
            indeg[v] -= 1
            if indeg[v] == 0 {
                queue.append(v)
            }
        }
        var visited = Array(repeating: false, count: n)
        var maxCycle = 0
        var twoSum = 0
        for i in 0..<n {
            if indeg[i] > 0 && !visited[i] {
                var cur = i
                var len = 0
                while !visited[cur] {
                    visited[cur] = true
                    len += 1
                    cur = favorite[cur]
                }
                if len == 2 {
                    let a = i
                    let b = favorite[i]
                    twoSum += depth[a] + depth[b]
                } else {
                    if len > maxCycle { maxCycle = len }
                }
            }
        }
        return max(maxCycle, twoSum)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun maximumInvitations(favorite: IntArray): Int {
        val n = favorite.size
        val indeg = IntArray(n)
        for (i in 0 until n) {
            indeg[favorite[i]]++
        }
        val dp = IntArray(n) // longest chain length ending at node, excluding the node itself
        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (indeg[i] == 0) queue.add(i)
        }
        while (!queue.isEmpty()) {
            val u = queue.removeFirst()
            val v = favorite[u]
            dp[v] = maxOf(dp[v], dp[u] + 1)
            indeg[v]--
            if (indeg[v] == 0) queue.add(v)
        }

        var maxCycle = 0
        var sumTwoCycles = 0
        val visited = BooleanArray(n)

        for (i in 0 until n) {
            if (indeg[i] > 0 && !visited[i]) {
                var cur = i
                val cycleNodes = mutableListOf<Int>()
                while (!visited[cur]) {
                    visited[cur] = true
                    cycleNodes.add(cur)
                    cur = favorite[cur]
                }
                val len = cycleNodes.size
                if (len == 2) {
                    val a = cycleNodes[0]
                    val b = cycleNodes[1]
                    sumTwoCycles += dp[a] + dp[b] + 2
                } else {
                    maxCycle = maxOf(maxCycle, len)
                }
            }
        }

        return maxOf(maxCycle, sumTwoCycles)
    }
}
```

## Dart

```dart
import 'dart:collection';
import 'dart:math';

class Solution {
  int maximumInvitations(List<int> favorite) {
    int n = favorite.length;
    List<int> indegree = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      indegree[favorite[i]]++;
    }

    // depth[i] = longest chain length ending at i (including i)
    List<int> depth = List.filled(n, 1);
    Queue<int> q = ListQueue<int>();
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) q.add(i);
    }

    while (q.isNotEmpty) {
      int u = q.removeFirst();
      int v = favorite[u];
      if (depth[v] < depth[u] + 1) {
        depth[v] = depth[u] + 1;
      }
      indegree[v]--;
      if (indegree[v] == 0) q.add(v);
    }

    int maxCycle = 0;
    int sumTwoCycles = 0;
    List<bool> visited = List.filled(n, false);

    for (int i = 0; i < n; i++) {
      if (indegree[i] > 0 && !visited[i]) {
        // traverse the cycle starting at i
        int cur = i;
        int len = 0;
        do {
          visited[cur] = true;
          cur = favorite[cur];
          len++;
        } while (cur != i);

        if (len == 2) {
          int a = i;
          int b = favorite[i];
          sumTwoCycles += depth[a] + depth[b];
        } else {
          maxCycle = max(maxCycle, len);
        }
      }
    }

    return max(maxCycle, sumTwoCycles);
  }
}
```

## Golang

```go
func maximumInvitations(favorite []int) int {
    n := len(favorite)
    indeg := make([]int, n)
    for _, v := range favorite {
        indeg[v]++
    }

    dp := make([]int, n)
    for i := 0; i < n; i++ {
        dp[i] = 1
    }

    queue := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if indeg[i] == 0 {
            queue = append(queue, i)
        }
    }

    head := 0
    for head < len(queue) {
        v := queue[head]
        head++
        nxt := favorite[v]
        if dp[v]+1 > dp[nxt] {
            dp[nxt] = dp[v] + 1
        }
        indeg[nxt]--
        if indeg[nxt] == 0 {
            queue = append(queue, nxt)
        }
    }

    visited := make([]bool, n)
    maxCycle := 0
    pairSum := 0

    for i := 0; i < n; i++ {
        if indeg[i] > 0 && !visited[i] {
            cnt := 0
            cur := i
            for {
                visited[cur] = true
                cnt++
                cur = favorite[cur]
                if cur == i {
                    break
                }
            }
            if cnt == 2 {
                a := i
                b := favorite[i]
                pairSum += (dp[a]-1) + (dp[b]-1) + 2
            } else {
                if cnt > maxCycle {
                    maxCycle = cnt
                }
            }
        }
    }

    if pairSum > maxCycle {
        return pairSum
    }
    return maxCycle
}
```

## Ruby

```ruby
def maximum_invitations(favorite)
  n = favorite.length
  indeg = Array.new(n, 0)
  favorite.each { |f| indeg[f] += 1 }

  depth = Array.new(n, 0)
  queue = []
  head = 0

  (0...n).each { |i| queue << i if indeg[i] == 0 }

  while head < queue.length
    u = queue[head]
    head += 1
    v = favorite[u]
    depth[v] = depth[u] + 1 if depth[u] + 1 > depth[v]
    indeg[v] -= 1
    queue << v if indeg[v] == 0
  end

  visited = Array.new(n, false)
  max_cycle = 0
  pair_sum = 0

  (0...n).each do |i|
    next if indeg[i] == 0 || visited[i]

    cur = i
    cnt = 0
    while !visited[cur]
      visited[cur] = true
      cnt += 1
      cur = favorite[cur]
    end

    if cnt == 2
      a = i
      b = favorite[i]
      pair_sum += depth[a] + depth[b] + 2
    else
      max_cycle = cnt if cnt > max_cycle
    end
  end

  [max_cycle, pair_sum].max
end
```

## Scala

```scala
object Solution {
    def maximumInvitations(favorite: Array[Int]): Int = {
        val n = favorite.length
        val indeg = new Array[Int](n)
        for (i <- 0 until n) indeg(favorite(i)) += 1

        val depth = Array.fill(n)(1)
        val q = scala.collection.mutable.Queue[Int]()
        for (i <- 0 until n) if (indeg(i) == 0) q.enqueue(i)

        while (q.nonEmpty) {
            val v = q.dequeue()
            val u = favorite(v)
            if (depth(u) < depth(v) + 1) depth(u) = depth(v) + 1
            indeg(u) -= 1
            if (indeg(u) == 0) q.enqueue(u)
        }

        val visited = new Array[Boolean](n)
        var maxCycle = 0
        var twoSum = 0

        for (i <- 0 until n) {
            if (indeg(i) > 0 && !visited(i)) {
                var cur = i
                var len = 0
                while (!visited(cur)) {
                    visited(cur) = true
                    len += 1
                    cur = favorite(cur)
                }
                if (len == 2) {
                    val a = i
                    val b = favorite(i)
                    twoSum += depth(a) + depth(b)
                } else {
                    maxCycle = math.max(maxCycle, len)
                }
            }
        }

        math.max(maxCycle, twoSum)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        let n = favorite.len();
        let mut indeg = vec![0usize; n];
        for &f in &favorite {
            indeg[f as usize] += 1;
        }

        let mut depth = vec![0i32; n];
        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }

        while let Some(u) = q.pop_front() {
            let v = favorite[u] as usize;
            if depth[u] + 1 > depth[v] {
                depth[v] = depth[u] + 1;
            }
            indeg[v] -= 1;
            if indeg[v] == 0 {
                q.push_back(v);
            }
        }

        let mut max_cycle = 0usize;
        let mut sum_two = 0i32;

        for i in 0..n {
            if indeg[i] > 0 {
                // traverse the cycle starting from i
                let mut cnt = 0usize;
                let mut cur = i;
                while indeg[cur] > 0 {
                    indeg[cur] = 0; // mark visited
                    cnt += 1;
                    cur = favorite[cur] as usize;
                }
                if cnt == 2 {
                    let a = i;
                    let b = favorite[i] as usize;
                    sum_two += depth[a] + depth[b] + 2;
                } else {
                    if cnt > max_cycle {
                        max_cycle = cnt;
                    }
                }
            }
        }

        std::cmp::max(max_cycle as i32, sum_two)
    }
}
```

## Racket

```racket
(define/contract (maximum-invitations favorite)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((fav (list->vector favorite))
         (n (vector-length fav))
         (indeg (make-vector n 0))
         (depth (make-vector n 0)))
    ;; compute indegrees
    (for ([i (in-range n)])
      (let ([v (vector-ref fav i)])
        (vector-set! indeg v (+ (vector-ref indeg v) 1))))
    ;; topological order to compute longest chain lengths
    (define queue (make-vector n))
    (define head 0)
    (define tail 0)
    (for ([i (in-range n)])
      (when (= (vector-ref indeg i) 0)
        (vector-set! queue tail i)
        (set! tail (+ tail 1))))
    (let loop ()
      (when (< head tail)
        (let* ((u (vector-ref queue head))
               (v (vector-ref fav u)))
          (set! head (+ head 1))
          ;; update depth of v
          (let ([newd (+ (vector-ref depth u) 1)])
            (when (> newd (vector-ref depth v))
              (vector-set! depth v newd)))
          ;; remove edge u->v
          (vector-set! indeg v (- (vector-ref indeg v) 1))
          (when (= (vector-ref indeg v) 0)
            (vector-set! queue tail v)
            (set! tail (+ tail 1))))
        (loop)))
    ;; process remaining cycles
    (define maxCycle 0)
    (define pairSum 0)
    (for ([i (in-range n)])
      (when (> (vector-ref indeg i) 0)
        (let loop ((cur i) (len 0) (nodes '()))
          (if (= (vector-ref indeg cur) 0)
              (begin
                (if (= len 2)
                    (let* ([a (car nodes)]
                           [b (cadr nodes)])
                      (set! pairSum (+ pairSum (+ 2 (vector-ref depth a) (vector-ref depth b)))))
                    (when (> len maxCycle) (set! maxCycle len))))
              (begin
                (vector-set! indeg cur 0)
                (loop (vector-ref fav cur) (+ len 1) (cons cur nodes)))))))
    (max maxCycle pairSum)))
```

## Erlang

```erlang
-spec maximum_invitations([integer()]) -> integer().
maximum_invitations(Favorite) ->
    N = length(Favorite),
    FavTuple = list_to_tuple(Favorite),

    %% indegree array
    Indeg0 = array:new(N, {default, 0}),
    Indeg = build_indeg(0, N - 1, FavTuple, Indeg0),

    Depth0 = array:new(N, {default, 0}),

    Queue0 = init_queue(Indeg, N),
    {Indeg1, Depth1} = process_queue(Queue0, Indeg, Depth0, FavTuple),

    %% process cycles
    {LongestCycle, TwoCycleSum} = process_cycles(0, N - 1, Indeg1, Depth1, FavTuple, 0, 0),

    erlang:max(LongestCycle, TwoCycleSum).

%% Build indegree array
build_indeg(I, Max, FavTuple, Indeg) when I > Max ->
    Indeg;
build_indeg(I, Max, FavTuple, Indeg) ->
    To = element(I + 1, FavTuple),
    Cur = array:get(To, Indeg),
    Indeg2 = array:set(To, Cur + 1, Indeg),
    build_indeg(I + 1, Max, FavTuple, Indeg2).

%% Initialize queue with nodes of indegree 0
init_queue(Indeg, N) ->
    init_queue(0, N - 1, Indeg, queue:new()).

init_queue(I, Max, _Indeg, Q) when I > Max ->
    Q;
init_queue(I, Max, Indeg, Q) ->
    case array:get(I, Indeg) of
        0 -> init_queue(I + 1, Max, Indeg, queue:in(I, Q));
        _ -> init_queue(I + 1, Max, Indeg, Q)
    end.

%% Process topological order, compute depths and reduce indegrees
process_queue(Q, Indeg, Depth, FavTuple) ->
    case queue:out(Q) of
        empty ->
            {Indeg, Depth};
        {value, V, Q2} ->
            F = element(V + 1, FavTuple),

            Dv = array:get(V, Depth),
            Df = array:get(F, Depth),
            NewDf = erlang:max(Df, Dv + 1),
            Depth1 = if NewDf =/= Df -> array:set(F, NewDf, Depth) else Depth end,

            IndegF = array:get(F, Indeg) - 1,
            Indeg1 = array:set(F, IndegF, Indeg),

            Q3 = case IndegF of
                     0 -> queue:in(F, Q2);
                     _ -> Q2
                 end,
            process_queue(Q3, Indeg1, Depth1, FavTuple)
    end.

%% Process remaining cycles
process_cycles(I, Max, Indeg, Depth, FavTuple, Longest, TwoSum) when I > Max ->
    {Longest, TwoSum};
process_cycles(I, Max, Indeg, Depth, FavTuple, Longest, TwoSum) ->
    case array:get(I, Indeg) of
        0 ->
            process_cycles(I + 1, Max, Indeg, Depth, FavTuple, Longest, TwoSum);
        _ ->
            {Len, Indeg2} = traverse_cycle(I, FavTuple, Indeg, 0),
            if Len == 2 ->
                    A = I,
                    B = element(A + 1, FavTuple),
                    Contrib = array:get(A, Depth) + array:get(B, Depth) + 2,
                    process_cycles(I + 1, Max, Indeg2, Depth, FavTuple, Longest, TwoSum + Contrib);
               true ->
                    NewLongest = erlang:max(Longest, Len),
                    process_cycles(I + 1, Max, Indeg2, Depth, FavTuple, NewLongest, TwoSum)
            end
    end.

%% Traverse a cycle, marking visited nodes (indegree set to 0) and counting length
traverse_cycle(Node, FavTuple, Indeg, Acc) ->
    case array:get(Node, Indeg) of
        0 -> {Acc, Indeg};
        _ ->
            Indeg1 = array:set(Node, 0, Indeg),
            Next = element(Node + 1, FavTuple),
            traverse_cycle(Next, FavTuple, Indeg1, Acc + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_invitations(favorite :: [integer]) :: integer
  def maximum_invitations(favorite) do
    n = length(favorite)
    fav_arr = :array.from_list(favorite)

    indeg0 =
      Enum.reduce(0..(n - 1), :array.new(n, default: 0), fn i, acc ->
        v = :array.get(i, fav_arr)
        cur = :array.get(v, acc)
        :array.set(v, cur + 1, acc)
      end)

    q0 =
      Enum.reduce(0..(n - 1), :queue.new(), fn i, q ->
        if :array.get(i, indeg0) == 0 do
          :queue.in(i, q)
        else
          q
        end
      end)

    {indeg1, depth_arr} = bfs(q0, indeg0, :array.new(n, default: 0), fav_arr)

    {_, max_cycle, sum_two} =
      Enum.reduce(0..(n - 1), {indeg1, 0, 0}, fn i, {indeg, mc, st} ->
        if :array.get(i, indeg) > 0 do
          {new_indeg, len, nodes} = traverse_cycle(i, indeg, fav_arr, 0, [])
          if len == 2 do
            [a, b] = nodes
            da = :array.get(a, depth_arr)
            db = :array.get(b, depth_arr)
            {new_indeg, mc, st + 2 + da + db}
          else
            new_mc = if len > mc, do: len, else: mc
            {new_indeg, new_mc, st}
          end
        else
          {indeg, mc, st}
        end
      end)

    max(max_cycle, sum_two)
  end

  defp bfs(queue, indeg, depth, fav_arr) do
    case :queue.out(queue) do
      {:empty, _} ->
        {indeg, depth}

      {{:value, u}, qrest} ->
        v = :array.get(u, fav_arr)

        du = :array.get(u, depth)
        dv = :array.get(v, depth)

        new_depth =
          if du + 1 > dv do
            :array.set(v, du + 1, depth)
          else
            depth
          end

        indeg_val = :array.get(v, indeg) - 1
        new_indeg = :array.set(v, indeg_val, indeg)

        new_queue =
          if indeg_val == 0 do
            :queue.in(v, qrest)
          else
            qrest
          end

        bfs(new_queue, new_indeg, new_depth, fav_arr)
    end
  end

  defp traverse_cycle(cur, indeg, fav_arr, len_acc, nodes_acc) do
    if :array.get(cur, indeg) == 0 do
      {indeg, len_acc, Enum.reverse(nodes_acc)}
    else
      indeg = :array.set(cur, 0, indeg)
      next = :array.get(cur, fav_arr)
      traverse_cycle(next, indeg, fav_arr, len_acc + 1, [cur | nodes_acc])
    end
  end
end
```
