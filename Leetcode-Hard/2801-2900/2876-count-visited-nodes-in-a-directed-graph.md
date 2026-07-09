# 2876. Count Visited Nodes in a Directed Graph

## Cpp

```cpp
class Solution {
public:
    vector<int> countVisitedNodes(vector<int>& edges) {
        int n = edges.size();
        vector<int> indeg(n, 0);
        for (int v : edges) indeg[v]++;

        queue<int> q;
        vector<int> order;
        vector<char> removed(n, false);
        for (int i = 0; i < n; ++i)
            if (indeg[i] == 0) q.push(i);

        while (!q.empty()) {
            int u = q.front(); q.pop();
            removed[u] = true;
            order.push_back(u);
            int v = edges[u];
            if (--indeg[v] == 0) q.push(v);
        }

        vector<int> ans(n, 0);
        vector<char> visited(n, false); // for cycle nodes

        for (int i = 0; i < n; ++i) {
            if (!removed[i] && !visited[i]) { // node in a cycle
                int cur = i;
                int cnt = 0;
                do {
                    ++cnt;
                    cur = edges[cur];
                } while (cur != i);
                cur = i;
                do {
                    ans[cur] = cnt;
                    visited[cur] = true;
                    cur = edges[cur];
                } while (cur != i);
            }
        }

        for (int idx = (int)order.size() - 1; idx >= 0; --idx) {
            int u = order[idx];
            ans[u] = ans[edges[u]] + 1;
        }

        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countVisitedNodes(java.util.List<Integer> edges) {
        int n = edges.size();
        int[] to = new int[n];
        for (int i = 0; i < n; i++) {
            to[i] = edges.get(i);
        }

        int[] indeg = new int[n];
        for (int v : to) {
            indeg[v]++;
        }

        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int v = queue.poll();
            int u = to[v];
            indeg[u]--;
            if (indeg[u] == 0) {
                queue.add(u);
            }
        }

        boolean[] visitedCycle = new boolean[n];
        int[] ans = new int[n];

        // Process cycles
        for (int i = 0; i < n; i++) {
            if (indeg[i] > 0 && !visitedCycle[i]) {
                int cur = i;
                int cnt = 0;
                do {
                    visitedCycle[cur] = true;
                    cnt++;
                    cur = to[cur];
                } while (cur != i);
                cur = i;
                do {
                    ans[cur] = cnt;
                    cur = to[cur];
                } while (cur != i);
            }
        }

        // Process tree nodes leading into cycles
        for (int i = 0; i < n; i++) {
            if (ans[i] == 0) {
                int cur = i;
                java.util.ArrayList<Integer> path = new java.util.ArrayList<>();
                while (ans[cur] == 0) {
                    path.add(cur);
                    cur = to[cur];
                }
                int val = ans[cur];
                for (int idx = path.size() - 1; idx >= 0; --idx) {
                    val += 1;
                    ans[path.get(idx)] = val;
                }
            }
        }

        return ans;
    }
}
```

## Python

```python
import sys

class Solution(object):
    def countVisitedNodes(self, edges):
        """
        :type edges: List[int]
        :rtype: List[int]
        """
        sys.setrecursionlimit(1 << 25)
        n = len(edges)
        ans = [0] * n
        state = [0] * n  # 0=unvisited,1=visiting,2=processed

        def dfs(u):
            if state[u] == 2:
                return ans[u]
            if state[u] == 1:
                # found a cycle starting at u
                cnt = 1
                v = edges[u]
                while v != u:
                    cnt += 1
                    v = edges[v]
                # assign size to all nodes in the cycle
                v = u
                while True:
                    ans[v] = cnt
                    state[v] = 2
                    v = edges[v]
                    if v == u:
                        break
                return ans[u]

            state[u] = 1
            nxt = edges[u]
            dfs(nxt)
            if state[u] != 2:  # not part of a cycle
                ans[u] = 1 + ans[nxt]
                state[u] = 2
            return ans[u]

        for i in range(n):
            if state[i] == 0:
                dfs(i)

        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        state = [0] * n          # 0 = unvisited, 1 = visiting, 2 = processed
        ans = [0] * n
        sys.setrecursionlimit(3000000)

        def dfs(u: int) -> int:
            if state[u] == 2:
                return ans[u]
            if state[u] == 1:
                # found a cycle starting at u
                cnt = 0
                cur = u
                while True:
                    cnt += 1
                    cur = edges[cur]
                    if cur == u:
                        break
                cur = u
                while True:
                    ans[cur] = cnt
                    state[cur] = 2
                    cur = edges[cur]
                    if cur == u:
                        break
                return ans[u]

            state[u] = 1
            v = edges[u]
            dfs(v)
            if state[u] != 2:          # not part of a cycle
                ans[u] = ans[v] + 1
                state[u] = 2
            return ans[u]

        for i in range(n):
            if state[i] == 0:
                dfs(i)

        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countVisitedNodes(int* edges, int edgesSize, int* returnSize) {
    int n = edgesSize;
    int *ans = (int*)malloc(n * sizeof(int));
    char *state = (char*)calloc(n, sizeof(char)); // 0=unvisited,1=visiting,2=done
    int *stack = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        if (state[i] != 0) continue;

        int top = 0;
        int cur = i;
        while (state[cur] == 0) {
            state[cur] = 1;
            stack[top++] = cur;
            cur = edges[cur];
        }

        if (state[cur] == 1) { // found a cycle
            int pos = -1;
            for (int k = 0; k < top; ++k) {
                if (stack[k] == cur) {
                    pos = k;
                    break;
                }
            }
            int cycleLen = top - pos;

            // nodes in the cycle
            for (int k = pos; k < top; ++k) {
                int node = stack[k];
                ans[node] = cycleLen;
                state[node] = 2;
            }

            // nodes leading to the cycle
            for (int k = pos - 1; k >= 0; --k) {
                int node = stack[k];
                int nxt = edges[node];
                ans[node] = ans[nxt] + 1;
                state[node] = 2;
            }
        } else { // reached an already processed node
            for (int k = top - 1; k >= 0; --k) {
                int node = stack[k];
                int nxt = edges[node];
                ans[node] = ans[nxt] + 1;
                state[node] = 2;
            }
        }
    }

    free(stack);
    free(state);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] CountVisitedNodes(IList<int> edges) {
        int n = edges.Count;
        int[] indeg = new int[n];
        for (int i = 0; i < n; i++) {
            indeg[edges[i]]++;
        }

        var queue = new Queue<int>();
        var removedOrder = new List<int>();

        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) queue.Enqueue(i);
        }

        while (queue.Count > 0) {
            int u = queue.Dequeue();
            removedOrder.Add(u);
            int v = edges[u];
            indeg[v]--;
            if (indeg[v] == 0) queue.Enqueue(v);
        }

        int[] answer = new int[n];
        bool[] visitedCycle = new bool[n];

        for (int i = 0; i < n; i++) {
            if (indeg[i] > 0 && !visitedCycle[i]) {
                // find cycle size
                int cur = i;
                int cnt = 0;
                do {
                    visitedCycle[cur] = true;
                    cnt++;
                    cur = edges[cur];
                } while (cur != i);

                // assign answer for all nodes in this cycle
                cur = i;
                do {
                    answer[cur] = cnt;
                    cur = edges[cur];
                } while (cur != i);
            }
        }

        // process non-cycle nodes in reverse removal order
        for (int idx = removedOrder.Count - 1; idx >= 0; idx--) {
            int u = removedOrder[idx];
            answer[u] = answer[edges[u]] + 1;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} edges
 * @return {number[]}
 */
var countVisitedNodes = function(edges) {
    const n = edges.length;
    const ans = new Array(n);
    const state = new Uint8Array(n); // 0=unvisited,1=visiting,2=done
    const pos = new Int32Array(n);
    pos.fill(-1);
    
    for (let i = 0; i < n; ++i) {
        if (state[i] !== 0) continue;
        let cur = i;
        const path = [];
        while (state[cur] === 0) {
            state[cur] = 1;
            pos[cur] = path.length;
            path.push(cur);
            cur = edges[cur];
        }
        if (state[cur] === 1) { // found a cycle
            const idx = pos[cur];               // start index of the cycle in path
            const cycleSize = path.length - idx; // length of the cycle
            for (let j = idx; j < path.length; ++j) {
                const node = path[j];
                ans[node] = cycleSize;
                state[node] = 2;
            }
            for (let j = idx - 1; j >= 0; --j) {
                const node = path[j];
                const nxt = edges[node];
                ans[node] = ans[nxt] + 1;
                state[node] = 2;
            }
        } else { // reached an already processed node
            for (let j = path.length - 1; j >= 0; --j) {
                const node = path[j];
                const nxt = edges[node];
                ans[node] = ans[nxt] + 1;
                state[node] = 2;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countVisitedNodes(edges: number[]): number[] {
    const n = edges.length;
    const ans = new Array<number>(n);
    const state = new Uint8Array(n); // 0 = unvisited, 1 = visiting, 2 = processed
    const pos = new Int32Array(n);
    for (let i = 0; i < n; i++) pos[i] = -1;

    for (let i = 0; i < n; i++) {
        if (state[i] !== 0) continue;
        let cur = i;
        const path: number[] = [];

        while (state[cur] === 0) {
            state[cur] = 1;
            pos[cur] = path.length;
            path.push(cur);
            cur = edges[cur];
        }

        if (state[cur] === 1) { // found a new cycle
            const startIdx = pos[cur];
            const cycleSize = path.length - startIdx;
            for (let j = startIdx; j < path.length; ++j) {
                const node = path[j];
                ans[node] = cycleSize;
                state[node] = 2;
            }
        }

        // compute answers for nodes leading to the cycle
        for (let k = path.length - 1; k >= 0; --k) {
            const node = path[k];
            if (state[node] === 2) continue; // already set (cycle node)
            const nxt = edges[node];
            ans[node] = ans[nxt] + 1;
            state[node] = 2;
        }

        // reset positions for reuse
        for (const node of path) {
            pos[node] = -1;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer[]
     */
    function countVisitedNodes($edges) {
        $n = count($edges);
        $state = array_fill(0, $n, 0); // 0=unvisited,1=visiting,2=done
        $ans   = array_fill(0, $n, 0);

        $dfs = function ($u) use (&$edges, &$state, &$ans, &$dfs) {
            if ($state[$u] === 2) {
                return $ans[$u];
            }
            if ($state[$u] === 1) { // found a cycle
                $cycleSize = 0;
                $v = $u;
                do {
                    $cycleSize++;
                    $v = $edges[$v];
                } while ($v !== $u);
                $v = $u;
                do {
                    $ans[$v]   = $cycleSize;
                    $state[$v] = 2;
                    $v = $edges[$v];
                } while ($v !== $u);
                return $ans[$u];
            }
            // state == 0
            $state[$u] = 1;
            $next = $edges[$u];
            $res = $dfs($next);
            if ($state[$u] === 2) { // became part of a cycle during recursion
                return $ans[$u];
            }
            $ans[$u]   = $res + 1; // distance to cycle + cycle size
            $state[$u] = 2;
            return $ans[$u];
        };

        for ($i = 0; $i < $n; $i++) {
            if ($state[$i] === 0) {
                $dfs($i);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countVisitedNodes(_ edges: [Int]) -> [Int] {
        let n = edges.count
        var state = Array(repeating: 0, count: n) // 0: unvisited, 1: visiting, 2: processed
        var answer = Array(repeating: 0, count: n)
        var indexInStack = Array(repeating: -1, count: n)

        for i in 0..<n {
            if state[i] != 0 { continue }
            var cur = i
            var stack = [Int]()
            while true {
                if state[cur] == 0 {
                    state[cur] = 1
                    indexInStack[cur] = stack.count
                    stack.append(cur)
                    cur = edges[cur]
                } else if state[cur] == 1 {
                    // Cycle detected
                    let startIdx = indexInStack[cur]
                    let cycleLen = stack.count - startIdx
                    // Nodes in the cycle
                    for j in startIdx..<stack.count {
                        let node = stack[j]
                        answer[node] = cycleLen
                        state[node] = 2
                        indexInStack[node] = -1
                    }
                    // Nodes leading to the cycle
                    if startIdx > 0 {
                        for j in stride(from: startIdx - 1, through: 0, by: -1) {
                            let node = stack[j]
                            let next = edges[node]
                            answer[node] = answer[next] + 1
                            state[node] = 2
                            indexInStack[node] = -1
                        }
                    }
                    break
                } else { // state[cur] == 2, already computed
                    for node in stack.reversed() {
                        let next = edges[node]
                        answer[node] = answer[next] + 1
                        state[node] = 2
                        indexInStack[node] = -1
                    }
                    break
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
    fun countVisitedNodes(edges: List<Int>): IntArray {
        val n = edges.size
        val state = IntArray(n) // 0 = unvisited, 1 = visiting, 2 = processed
        val ans = IntArray(n)
        for (i in 0 until n) {
            if (state[i] != 0) continue
            var cur = i
            val stack = mutableListOf<Int>()
            while (state[cur] == 0) {
                state[cur] = 1
                stack.add(cur)
                cur = edges[cur]
            }
            if (state[cur] == 1) {
                // found a cycle starting at cur
                var len = 1
                var node = edges[cur]
                while (node != cur) {
                    len++
                    node = edges[node]
                }
                var v = cur
                do {
                    ans[v] = len
                    state[v] = 2
                    v = edges[v]
                } while (v != cur)
            }
            // backtrack for nodes leading to already known results
            for (idx in stack.size - 1 downTo 0) {
                val v = stack[idx]
                if (state[v] == 2) continue
                val nxt = edges[v]
                ans[v] = ans[nxt] + 1
                state[v] = 2
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countVisitedNodes(List<int> edges) {
    int n = edges.length;
    List<int> ans = List.filled(n, 0);
    List<int> state = List.filled(n, 0); // 0: unvisited, 1: visiting, 2: done
    List<int> pos = List.filled(n, -1);

    for (int i = 0; i < n; ++i) {
      if (state[i] != 0) continue;

      List<int> path = [];
      int cur = i;
      while (state[cur] == 0) {
        state[cur] = 1;
        pos[cur] = path.length;
        path.add(cur);
        cur = edges[cur];
      }

      if (state[cur] == 1) {
        // Found a cycle
        int cycleStart = pos[cur];
        int cycleLen = path.length - cycleStart;

        for (int j = cycleStart; j < path.length; ++j) {
          int node = path[j];
          ans[node] = cycleLen;
          state[node] = 2;
        }
        for (int j = cycleStart - 1; j >= 0; --j) {
          int node = path[j];
          int nxt = edges[node];
          ans[node] = 1 + ans[nxt];
          state[node] = 2;
        }
      } else {
        // Reached an already processed node
        for (int j = path.length - 1; j >= 0; --j) {
          int node = path[j];
          int nxt = edges[node];
          ans[node] = 1 + ans[nxt];
          state[node] = 2;
        }
      }

      // Reset positions for this traversal
      for (int node in path) {
        pos[node] = -1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countVisitedNodes(edges []int) []int {
    n := len(edges)
    ans := make([]int, n)
    state := make([]int, n) // 0 = unvisited, 1 = visiting, 2 = done

    var dfs func(int) int
    dfs = func(u int) int {
        if state[u] == 2 {
            return ans[u]
        }
        if state[u] == 1 {
            // found a cycle starting at u
            cnt := 1
            v := edges[u]
            for v != u {
                cnt++
                v = edges[v]
            }
            // assign answer to all nodes in the cycle
            v = u
            for {
                ans[v] = cnt
                state[v] = 2
                v = edges[v]
                if v == u {
                    break
                }
            }
            return ans[u]
        }
        state[u] = 1
        next := edges[u]
        res := dfs(next)
        if state[u] != 2 { // not part of a cycle already processed
            ans[u] = res + 1
            state[u] = 2
        }
        return ans[u]
    }

    for i := 0; i < n; i++ {
        if state[i] == 0 {
            dfs(i)
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_visited_nodes(edges)
  n = edges.length
  ans = Array.new(n)
  state = Array.new(n, 0) # 0: unvisited, 1: visiting, 2: visited

  (0...n).each do |i|
    next if state[i] != 0

    cur = i
    stack = []
    while state[cur] == 0
      stack << cur
      state[cur] = 1
      cur = edges[cur]
    end

    if state[cur] == 1
      # found a cycle starting at cur
      cnt = 1
      node = edges[cur]
      while node != cur
        cnt += 1
        node = edges[node]
      end
      node = cur
      loop do
        ans[node] = cnt
        state[node] = 2
        node = edges[node]
        break if node == cur
      end
    end

    until stack.empty?
      node = stack.pop
      next if state[node] == 2
      ans[node] = ans[edges[node]] + 1
      state[node] = 2
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countVisitedNodes(edges: List[Int]): Array[Int] = {
    val n = edges.length
    val edgeArr = edges.toArray
    val state = new Array[Byte](n) // 0 = unvisited, 1 = visiting, 2 = processed
    val ans = new Array[Int](n)

    for (i <- 0 until n) {
      if (state(i) == 0) {
        var cur = i
        val path = scala.collection.mutable.ArrayBuffer.empty[Int]
        while (state(cur) == 0) {
          state(cur) = 1
          path += cur
          cur = edgeArr(cur)
        }

        if (state(cur) == 1) { // found a new cycle
          var idx = path.length - 1
          while (path(idx) != cur) idx -= 1
          val cycleStart = idx
          val cycleLen = path.length - cycleStart

          // assign answers for nodes in the cycle
          for (k <- cycleStart until path.length) {
            val node = path(k)
            ans(node) = cycleLen
            state(node) = 2
          }

          // process nodes leading to the cycle
          var k = cycleStart - 1
          while (k >= 0) {
            val node = path(k)
            val nxt = edgeArr(node)
            ans(node) = ans(nxt) + 1
            state(node) = 2
            k -= 1
          }
        } else { // cur already processed
          var k = path.length - 1
          while (k >= 0) {
            val node = path(k)
            val nxt = edgeArr(node)
            ans(node) = ans(nxt) + 1
            state(node) = 2
            k -= 1
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
    pub fn count_visited_nodes(edges: Vec<i32>) -> Vec<i32> {
        let n = edges.len();
        let mut state = vec![0u8; n]; // 0=unvisited,1=visiting,2=done
        let mut ans = vec![0i32; n];
        for i in 0..n {
            if state[i] != 0 {
                continue;
            }
            let mut cur = i;
            let mut stack: Vec<usize> = Vec::new();
            while state[cur] == 0 {
                state[cur] = 1;
                stack.push(cur);
                cur = edges[cur] as usize;
            }
            if state[cur] == 1 {
                // found a cycle
                let mut cycle_len = 0usize;
                for &node in stack.iter().rev() {
                    cycle_len += 1;
                    if node == cur {
                        break;
                    }
                }
                // assign answer for nodes inside the cycle
                let mut in_cycle = false;
                for &node in &stack {
                    if node == cur {
                        in_cycle = true;
                    }
                    if in_cycle {
                        ans[node] = cycle_len as i32;
                        state[node] = 2;
                    }
                }
                // process nodes leading to the cycle
                while let Some(node) = stack.pop() {
                    if state[node] == 2 {
                        continue;
                    }
                    let next = edges[node] as usize;
                    ans[node] = ans[next] + 1;
                    state[node] = 2;
                }
            } else {
                // cur already processed
                while let Some(node) = stack.pop() {
                    let next = edges[node] as usize;
                    ans[node] = ans[next] + 1;
                    state[node] = 2;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-visited-nodes edges)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length edges))
         (edgesV (list->vector edges))
         (state (make-vector n 0))   ; 0 = unvisited, 1 = visiting, 2 = done
         (ans (make-vector n -1)))
    (define (dfs u)
      (cond
        [(= (vector-ref state u) 2)
         (vector-ref ans u)]
        [(= (vector-ref state u) 1)
         ;; cycle detected starting at u
         (let ((len
                (let loop ((cur u) (cnt 0))
                  (if (= cnt 0)
                      (loop (vector-ref edgesV cur) (+ cnt 1))
                      (if (= cur u) cnt
                          (loop (vector-ref edgesV cur) (+ cnt 1)))))))
           ;; assign length to all nodes in the cycle
           (let assign ((cur u))
             (vector-set! ans cur len)
             (vector-set! state cur 2)
             (define nxt (vector-ref edgesV cur))
             (when (not (= nxt u))
               (assign nxt)))
           len)]
        [else
         (vector-set! state u 1)
         (define v (vector-ref edgesV u))
         (dfs v)
         (when (= (vector-ref state u) 1)
           (vector-set! ans u (+ (vector-ref ans v) 1))
           (vector-set! state u 2))
         (vector-ref ans u)]))
    ;; compute answer for every node
    (for ([i (in-range n)])
      (when (= (vector-ref state i) 0)
        (dfs i)))
    ;; convert vector of answers to list
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (+ i 1) (cons (vector-ref ans i) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([count_visited_nodes/1]).

-spec count_visited_nodes(Edges :: [integer()]) -> [integer()].
count_visited_nodes(Edges) ->
    N = length(Edges),
    EdgesArr = array:from_list(Edges),
    State0 = array:new(N, {default, 0}),
    Ans0   = array:new(N, {default, 0}),
    {_StateFinal, AnsFinal} = process_nodes(0, N - 1, EdgesArr, State0, Ans0),
    [array:get(I, AnsFinal) || I <- lists:seq(0, N - 1)].

process_nodes(Cur, Max, _Edges, State, Ans) when Cur > Max ->
    {State, Ans};
process_nodes(Cur, Max, Edges, State, Ans) ->
    case array:get(Cur, State) of
        2 -> process_nodes(Cur + 1, Max, Edges, State, Ans);
        _ ->
            {NewState, NewAns} = dfs(Cur, Edges, State, Ans),
            process_nodes(Cur + 1, Max, Edges, NewState, NewAns)
    end.

dfs(V, Edges, State, Ans) ->
    case array:get(V, State) of
        2 -> {State, Ans};
        _ ->
            State1 = array:set(V, 1, State),
            Next = array:get(V, Edges),
            case array:get(Next, State1) of
                0 ->
                    {State2, Ans2} = dfs(Next, Edges, State1, Ans),
                    finalize(V, Next, State2, Ans2);
                1 ->
                    CycleSize = compute_cycle_size(Next, Edges),
                    {StateCyc, AnsCyc} = set_cycle_nodes(Next, Edges, CycleSize, State1, Ans),
                    finalize(V, Next, StateCyc, AnsCyc);
                2 ->
                    finalize(V, Next, State1, Ans)
            end
    end.

finalize(V, Next, State, Ans) ->
    case array:get(V, Ans) of
        0 ->
            ChildAns = array:get(Next, Ans),
            NewAns = ChildAns + 1,
            State2 = array:set(V, 2, State),
            Ans2   = array:set(V, NewAns, Ans),
            {State2, Ans2};
        _ -> % already set (cycle node)
            {State, Ans}
    end.

compute_cycle_size(Start, Edges) ->
    Next = array:get(Start, Edges),
    compute_cycle_size_loop(Next, Start, Edges, 1).

compute_cycle_size_loop(Cur, Start, Edges, Count) when Cur == Start ->
    Count;
compute_cycle_size_loop(Cur, Start, Edges, Count) ->
    Next = array:get(Cur, Edges),
    compute_cycle_size_loop(Next, Start, Edges, Count + 1).

set_cycle_nodes(Start, Edges, Size, State, Ans) ->
    set_cycle_nodes_loop(Start, Edges, Size, State, Ans).

set_cycle_nodes_loop(Node, Edges, Size, StateAcc, AnsAcc) ->
    Ans1   = array:set(Node, Size, AnsAcc),
    State1 = array:set(Node, 2, StateAcc),
    Next = array:get(Node, Edges),
    if
        Next == Node -> % impossible per constraints
            {State1, Ans1};
        Next == Start ->
            {State1, Ans1};
        true ->
            set_cycle_nodes_loop(Next, Edges, Size, State1, Ans1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_visited_nodes(edges :: [integer]) :: [integer]
  def count_visited_nodes(edges) do
    n = length(edges)
    edges_arr = :array.from_list(edges)

    # indegree array
    indeg_arr =
      Enum.reduce(0..(n - 1), :array.new(n, default: 0), fn i, arr ->
        to = :array.get(i, edges_arr)
        cnt = :array.get(to, arr) + 1
        :array.set(to, cnt, arr)
      end)

    # initial stack of nodes with indegree 0
    init_stack =
      Enum.reduce(0..(n - 1), [], fn i, acc ->
        if :array.get(i, indeg_arr) == 0, do: [i | acc], else: acc
      end)

    {indeg_arr, removed} = remove_nodes(init_stack, indeg_arr, edges_arr, [])

    # answer array
    ans_arr = :array.new(n, default: 0)
    visited_cycle = :array.new(n, default: false)

    # process cycles
    {ans_arr, _visited_cycle} =
      Enum.reduce(0..(n - 1), {ans_arr, visited_cycle}, fn i, {a_arr, v_arr} ->
        if :array.get(i, indeg_arr) > 0 and not :array.get(i, v_arr) do
          {len, nodes} = traverse_cycle(i, edges_arr)
          a_arr2 =
            Enum.reduce(nodes, a_arr, fn node, acc -> :array.set(node, len, acc) end)

          v_arr2 =
            Enum.reduce(nodes, v_arr, fn node, acc -> :array.set(node, true, acc) end)

          {a_arr2, v_arr2}
        else
          {a_arr, v_arr}
        end
      end)

    # process removed nodes (already in reverse topological order)
    ans_arr =
      Enum.reduce(removed, ans_arr, fn u, a_arr ->
        v = :array.get(u, edges_arr)
        val = :array.get(v, a_arr) + 1
        :array.set(u, val, a_arr)
      end)

    # build result list
    Enum.map(0..(n - 1), fn i -> :array.get(i, ans_arr) end)
  end

  defp remove_nodes([], indeg_arr, _edges_arr, removed_acc), do: {indeg_arr, removed_acc}

  defp remove_nodes([u | rest], indeg_arr, edges_arr, removed_acc) do
    v = :array.get(u, edges_arr)
    indeg_v = :array.get(v, indeg_arr) - 1
    indeg_arr2 = :array.set(v, indeg_v, indeg_arr)

    new_stack =
      if indeg_v == 0 do
        [v | rest]
      else
        rest
      end

    remove_nodes(new_stack, indeg_arr2, edges_arr, [u | removed_acc])
  end

  # returns {cycle_length, list_of_nodes_in_cycle}
  defp traverse_cycle(start, edges_arr) do
    do_traverse_cycle(start, start, edges_arr, 0, [])
  end

  defp do_traverse_cycle(current, start, edges_arr, len, nodes) do
    nodes = [current | nodes]
    len = len + 1
    nxt = :array.get(current, edges_arr)

    if nxt == start do
      {len, nodes}
    else
      do_traverse_cycle(nxt, start, edges_arr, len, nodes)
    end
  end
end
```
