# 2049. Count Nodes With the Highest Score

## Cpp

```cpp
class Solution {
public:
    int countHighestScoreNodes(vector<int>& parents) {
        int n = parents.size();
        vector<vector<int>> child(n);
        for (int i = 1; i < n; ++i) {
            child[parents[i]].push_back(i);
        }
        
        // Get a traversal order (preorder) then process in reverse for post-order sizes
        vector<int> order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : child[u]) st.push(v);
        }
        
        vector<long long> sz(n, 1); // subtree sizes
        long long maxScore = 0;
        int cnt = 0;
        
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            long long total = 1; // size of subtree rooted at u
            for (int v : child[u]) total += sz[v];
            sz[u] = total;
            
            long long prod = 1;
            for (int v : child[u]) prod *= sz[v];
            long long rest = n - total;
            if (rest > 0) prod *= rest;
            
            if (prod > maxScore) {
                maxScore = prod;
                cnt = 1;
            } else if (prod == maxScore) {
                ++cnt;
            }
        }
        
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countHighestScoreNodes(int[] parents) {
        int n = parents.length;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] children = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            children[i] = new java.util.ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            int p = parents[i];
            children[p].add(i);
        }

        // iterative DFS to get order
        int[] order = new int[n];
        int idx = 0;
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order[idx++] = node;
            for (int child : children[node]) {
                stack.push(child);
            }
        }

        int[] size = new int[n];
        long maxScore = 0L;
        int count = 0;

        for (int i = n - 1; i >= 0; --i) {
            int node = order[i];
            long prod = 1L;
            int sumChildSize = 0;
            for (int child : children[node]) {
                prod *= size[child];
                sumChildSize += size[child];
            }
            int rest = n - (sumChildSize + 1);
            if (rest > 0) {
                prod *= rest;
            }
            size[node] = sumChildSize + 1;

            if (prod > maxScore) {
                maxScore = prod;
                count = 1;
            } else if (prod == maxScore) {
                count++;
            }
        }

        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(300000)

        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            children[p].append(i)

        max_score = 0
        count = 0

        def dfs(u):
            nonlocal max_score, count
            total = 1          # size of subtree rooted at u
            prod = 1           # product of child subtree sizes
            for v in children[u]:
                sz = dfs(v)
                total += sz
                prod *= sz
            rest = n - total
            if rest > 0:
                prod *= rest

            if prod > max_score:
                max_score = prod
                count = 1
            elif prod == max_score:
                count += 1
            return total

        dfs(0)
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            children[p].append(i)

        import sys
        sys.setrecursionlimit(2000000)
        subtree = [0] * n

        def dfs(u: int) -> int:
            sz = 1
            for v in children[u]:
                sz += dfs(v)
            subtree[u] = sz
            return sz

        dfs(0)

        max_score = 0
        cnt = 0
        total = n
        for i in range(n):
            prod = 1
            rest = total - subtree[i]
            if rest > 0:
                prod *= rest
            for v in children[i]:
                prod *= subtree[v]
            if prod > max_score:
                max_score = prod
                cnt = 1
            elif prod == max_score:
                cnt += 1
        return cnt
```

## C

```c
#include <stdlib.h>

int countHighestScoreNodes(int* parents, int parentsSize) {
    int n = parentsSize;
    int *left = (int*)malloc(n * sizeof(int));
    int *right = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        left[i] = -1;
        right[i] = -1;
    }
    for (int i = 1; i < n; ++i) {
        int p = parents[i];
        if (left[p] == -1)
            left[p] = i;
        else
            right[p] = i;
    }

    int *subSize = (int*)malloc(n * sizeof(int));
    int *stack = (int*)malloc(n * sizeof(int));
    int *order = (int*)malloc(n * sizeof(int));
    int top = 0, idx = 0;

    stack[top++] = 0;
    while (top) {
        int node = stack[--top];
        order[idx++] = node;
        if (left[node] != -1) stack[top++] = left[node];
        if (right[node] != -1) stack[top++] = right[node];
    }

    for (int i = n - 1; i >= 0; --i) {
        int node = order[i];
        int sz = 1;
        if (left[node] != -1) sz += subSize[left[node]];
        if (right[node] != -1) sz += subSize[right[node]];
        subSize[node] = sz;
    }

    unsigned long long maxScore = 0;
    int count = 0;

    for (int node = 0; node < n; ++node) {
        unsigned long long score = 1ULL;
        if (left[node] != -1)
            score *= (unsigned long long)subSize[left[node]];
        if (right[node] != -1)
            score *= (unsigned long long)subSize[right[node]];
        unsigned long long rest = (unsigned long long)(n - subSize[node]);
        if (rest > 0)
            score *= rest;

        if (score > maxScore) {
            maxScore = score;
            count = 1;
        } else if (score == maxScore) {
            ++count;
        }
    }

    free(left);
    free(right);
    free(subSize);
    free(stack);
    free(order);

    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountHighestScoreNodes(int[] parents) {
        int n = parents.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            int p = parents[i];
            children[p].Add(i);
        }

        int[] subtreeSize = new int[n];
        long maxScore = -1;
        int count = 0;

        var stack = new Stack<(int node, bool visited)>();
        stack.Push((0, false));

        while (stack.Count > 0) {
            var (node, visited) = stack.Pop();
            if (!visited) {
                stack.Push((node, true));
                foreach (var child in children[node]) {
                    stack.Push((child, false));
                }
            } else {
                int size = 1;
                long score = 1;
                foreach (var child in children[node]) {
                    size += subtreeSize[child];
                    score *= subtreeSize[child];
                }

                int rest = n - size;
                if (rest > 0) score *= rest;

                subtreeSize[node] = size;

                if (score > maxScore) {
                    maxScore = score;
                    count = 1;
                } else if (score == maxScore) {
                    count++;
                }
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parents
 * @return {number}
 */
var countHighestScoreNodes = function(parents) {
    const n = parents.length;
    const children = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        const p = parents[i];
        children[p].push(i);
    }

    // Compute subtree sizes using iterative post-order traversal
    const size = new Array(n).fill(0);
    const stack = [0];
    const order = [];
    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const child of children[node]) {
            stack.push(child);
        }
    }
    for (let i = order.length - 1; i >= 0; i--) {
        const node = order[i];
        let sz = 1;
        for (const child of children[node]) {
            sz += size[child];
        }
        size[node] = sz;
    }

    let maxScore = 0;
    let count = 0;

    for (let i = 0; i < n; i++) {
        let prod = 1;
        const rest = n - size[i];
        if (rest > 0) prod *= rest;
        for (const child of children[i]) {
            const sz = size[child];
            if (sz > 0) prod *= sz;
        }

        if (prod > maxScore) {
            maxScore = prod;
            count = 1;
        } else if (prod === maxScore) {
            count++;
        }
    }

    return count;
};
```

## Typescript

```typescript
function countHighestScoreNodes(parents: number[]): number {
    const n = parents.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        const p = parents[i];
        children[p].push(i);
    }

    // Get nodes in preorder then process in reverse to compute subtree sizes
    const order: number[] = [];
    const stack: number[] = [0];
    while (stack.length) {
        const node = stack.pop()!;
        order.push(node);
        for (const child of children[node]) {
            stack.push(child);
        }
    }

    const size = new Array<number>(n).fill(1);
    for (let i = order.length - 1; i >= 0; i--) {
        const node = order[i];
        let total = 1;
        for (const child of children[node]) {
            total += size[child];
        }
        size[node] = total;
    }

    let maxScore = -1;
    let count = 0;

    for (let i = 0; i < n; i++) {
        let prod = 1;
        for (const child of children[i]) {
            prod *= size[child];
        }
        const rest = n - size[i];
        if (rest > 0) prod *= rest;

        if (prod > maxScore) {
            maxScore = prod;
            count = 1;
        } else if (prod === maxScore) {
            count++;
        }
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @return Integer
     */
    function countHighestScoreNodes($parents) {
        $n = count($parents);
        // Build children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; ++$i) {
            $p = $parents[$i];
            $children[$p][] = $i;
        }

        // Compute subtree sizes using iterative post-order DFS
        $subSize = array_fill(0, $n, 0);
        $stack = [[0, false]]; // [node, visitedFlag]
        while (!empty($stack)) {
            [$node, $visited] = array_pop($stack);
            if (!$visited) {
                $stack[] = [$node, true];
                foreach ($children[$node] as $ch) {
                    $stack[] = [$ch, false];
                }
            } else {
                $size = 1;
                foreach ($children[$node] as $ch) {
                    $size += $subSize[$ch];
                }
                $subSize[$node] = $size;
            }
        }

        $maxScore = -1;
        $count = 0;

        for ($i = 0; $i < $n; ++$i) {
            $score = 1;
            foreach ($children[$i] as $ch) {
                $score *= $subSize[$ch];
            }
            $rest = $n - $subSize[$i];
            if ($rest > 0) {
                $score *= $rest;
            }

            if ($score > $maxScore) {
                $maxScore = $score;
                $count = 1;
            } elseif ($score == $maxScore) {
                ++$count;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countHighestScoreNodes(_ parents: [Int]) -> Int {
        let n = parents.count
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = parents[i]
                children[p].append(i)
            }
        }
        
        // Compute subtree sizes using iterative post-order DFS
        var size = [Int](repeating: 0, count: n)
        var stack: [(node: Int, visited: Bool)] = [(0, false)]
        while let last = stack.popLast() {
            if last.visited {
                var sz = 1
                for c in children[last.node] {
                    sz += size[c]
                }
                size[last.node] = sz
            } else {
                stack.append((last.node, true))
                for c in children[last.node] {
                    stack.append((c, false))
                }
            }
        }
        
        var maxScore: UInt64 = 0
        var count = 0
        
        for i in 0..<n {
            var score: UInt64 = 1
            for c in children[i] {
                score *= UInt64(size[c])
            }
            let rest = n - size[i]
            if rest > 0 {
                score *= UInt64(rest)
            }
            if score > maxScore {
                maxScore = score
                count = 1
            } else if score == maxScore {
                count += 1
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countHighestScoreNodes(parents: IntArray): Int {
        val n = parents.size
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = parents[i]
            children[p].add(i)
        }

        val size = IntArray(n)
        val order = IntArray(n)
        var idx = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.push(0)
        while (stack.isNotEmpty()) {
            val node = stack.pop()
            order[idx++] = node
            for (c in children[node]) {
                stack.push(c)
            }
        }

        for (i in n - 1 downTo 0) {
            val node = order[i]
            var sz = 1
            for (c in children[node]) {
                sz += size[c]
            }
            size[node] = sz
        }

        var maxScore = 0L
        var count = 0
        for (node in 0 until n) {
            var score = 1L
            for (c in children[node]) {
                score *= size[c].toLong()
            }
            val rest = n - size[node]
            if (rest > 0) {
                score *= rest.toLong()
            }
            when {
                score > maxScore -> {
                    maxScore = score
                    count = 1
                }
                score == maxScore -> count++
            }
        }

        return count
    }
}
```

## Dart

```dart
class Solution {
  int countHighestScoreNodes(List<int> parents) {
    int n = parents.length;
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      int p = parents[i];
      children[p].add(i);
    }

    // Get nodes in a order suitable for post‑order processing
    List<int> order = [];
    List<int> stack = [0];
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int child in children[node]) {
        stack.add(child);
      }
    }

    // Compute subtree sizes
    List<int> size = List.filled(n, 1);
    for (int i = order.length - 1; i >= 0; i--) {
      int node = order[i];
      for (int child in children[node]) {
        size[node] += size[child];
      }
    }

    BigInt maxScore = BigInt.zero;
    int count = 0;

    // Evaluate scores
    for (int node = 0; node < n; node++) {
      BigInt score = BigInt.one;
      for (int child in children[node]) {
        score *= BigInt.from(size[child]);
      }
      int rest = n - size[node];
      if (rest > 0) {
        score *= BigInt.from(rest);
      }

      if (score > maxScore) {
        maxScore = score;
        count = 1;
      } else if (score == maxScore) {
        count++;
      }
    }

    return count;
  }
}
```

## Golang

```go
func countHighestScoreNodes(parents []int) int {
    n := len(parents)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parents[i]
        children[p] = append(children[p], i)
    }

    var maxScore int64
    count := 0

    var dfs func(int) int
    dfs = func(node int) int {
        sz := 1
        var prod int64 = 1
        for _, ch := range children[node] {
            childSize := dfs(ch)
            sz += childSize
            prod *= int64(childSize)
        }
        rest := n - sz
        if rest > 0 {
            prod *= int64(rest)
        }
        if prod > maxScore {
            maxScore = prod
            count = 1
        } else if prod == maxScore {
            count++
        }
        return sz
    }

    dfs(0)
    return count
}
```

## Ruby

```ruby
def count_highest_score_nodes(parents)
  n = parents.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parents[i]
    children[p] << i
  end

  size = Array.new(n, 0)
  stack = [[0, false]]
  while !stack.empty?
    node, visited = stack.pop
    if visited
      sz = 1
      children[node].each { |c| sz += size[c] }
      size[node] = sz
    else
      stack << [node, true]
      children[node].reverse_each { |c| stack << [c, false] }
    end
  end

  max_score = -1
  count = 0
  total = n
  (0...n).each do |i|
    prod = 1
    children[i].each { |c| prod *= size[c] }
    rest = total - size[i]
    prod *= rest if rest > 0
    if prod > max_score
      max_score = prod
      count = 1
    elsif prod == max_score
      count += 1
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def countHighestScoreNodes(parents: Array[Int]): Int = {
        val n = parents.length
        val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        var i = 1
        while (i < n) {
            val p = parents(i)
            children(p).append(i)
            i += 1
        }

        val sz = new Array[Long](n)
        var maxScore: Long = -1L
        var count = 0

        val stack = new java.util.ArrayDeque[(Int, Boolean)]()
        stack.push((0, false))

        while (!stack.isEmpty) {
            val (node, visited) = stack.pop()
            if (!visited) {
                stack.push((node, true))
                val chIter = children(node).iterator
                while (chIter.hasNext) {
                    stack.push((chIter.next(), false))
                }
            } else {
                var size: Long = 1L
                var score: Long = 1L
                val chIter = children(node).iterator
                while (chIter.hasNext) {
                    val c = chIter.next()
                    val cs = sz(c)
                    size += cs
                    score *= cs
                }
                val rest = n - size
                if (rest > 0) score *= rest
                sz(node) = size

                if (score > maxScore) {
                    maxScore = score
                    count = 1
                } else if (score == maxScore) {
                    count += 1
                }
            }
        }

        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_highest_score_nodes(parents: Vec<i32>) -> i32 {
        let n = parents.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parents[i] as usize;
            children[p].push(i);
        }

        // Get nodes in DFS order
        let mut stack = Vec::with_capacity(n);
        stack.push(0usize);
        let mut order = Vec::with_capacity(n);
        while let Some(node) = stack.pop() {
            order.push(node);
            for &c in &children[node] {
                stack.push(c);
            }
        }

        // Compute subtree sizes
        let mut size = vec![0usize; n];
        for &node in order.iter().rev() {
            let mut s = 1usize;
            for &c in &children[node] {
                s += size[c];
            }
            size[node] = s;
        }

        // Evaluate scores
        let mut max_score: i64 = 0;
        let mut count: i32 = 0;
        for i in 0..n {
            let mut score: i64 = 1;
            for &c in &children[i] {
                score *= size[c] as i64;
            }
            let rest = n - size[i];
            if rest > 0 {
                score *= rest as i64;
            }

            if score > max_score {
                max_score = score;
                count = 1;
            } else if score == max_score {
                count += 1;
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (count-highest-score-nodes parents)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length parents)]
         [children (make-vector n '())])
    ;; build children adjacency
    (for ([i (in-range n)])
      (let ([p (list-ref parents i)])
        (when (>= p 0)
          (vector-set! children p (cons i (vector-ref children p))))))
    ;; compute subtree sizes using iterative post‑order DFS
    (define sizes (make-vector n 0))
    (define stack (list (cons 0 #f))) ; (node . visited?)
    (let loop ()
      (unless (null? stack)
        (define pair (car stack))
        (set! stack (cdr stack))
        (define node (car pair))
        (define visited (cdr pair))
        (if visited
            (let ([total 1])
              (for ([c (in-list (vector-ref children node))])
                (set! total (+ total (vector-ref sizes c))))
              (vector-set! sizes node total))
            (begin
              (set! stack (cons (cons node #t) stack))
              (for ([c (in-list (vector-ref children node))])
                (set! stack (cons (cons c #f) stack)))))
        (loop)))
    ;; evaluate scores and find maximum count
    (let loop2 ([i 0] [max-score 0] [cnt 0])
      (if (= i n)
          cnt
          (let* ([child-list (vector-ref children i)]
                 [prod (let loop3 ([lst child-list] [acc 1])
                         (if (null? lst)
                             acc
                             (loop3 (cdr lst) (* acc (vector-ref sizes (car lst))))))]
                 [rest (- n (vector-ref sizes i))]
                 [score (if (> rest 0) (* prod rest) prod)])
            (cond [(> score max-score) (loop2 (add1 i) score 1)]
                  [(= score max-score) (loop2 (add1 i) max-score (add1 cnt))]
                  [else (loop2 (add1 i) max-score cnt)]))))))
```

## Erlang

```erlang
-export([count_highest_score_nodes/1]).
-spec count_highest_score_nodes(Parents :: [integer()]) -> integer().
count_highest_score_nodes(Parents) ->
    N = length(Parents),
    Indices = lists:seq(0, N-1),
    Pairs = lists:zip(Indices, Parents),
    Children = build_children(Pairs, #{}),
    Stack0 = [{0,false}],
    loop(Stack0, Children, #{}, 0, 0, N).

build_children([], Acc) -> Acc;
build_children([{Idx,P}|Rest], Acc) ->
    case P of
        -1 -> build_children(Rest, Acc);
        _ ->
            NewAcc = maps:update_with(P,
                fun(L) -> [Idx|L] end,
                [Idx],
                Acc),
            build_children(Rest, NewAcc)
    end.

loop([], _Children, _SizeMap, _MaxScore, Count, _N) ->
    Count;
loop([{Node,false}|RestStack], Children, SizeMap, MaxScore, Count, N) ->
    ChildList = maps:get(Node, Children, []),
    NewStack = [{Node,true}|RestStack],
    StackWithChildren = lists:foldl(fun(C, Acc) -> [{C,false}|Acc] end,
                                    NewStack,
                                    ChildList),
    loop(StackWithChildren, Children, SizeMap, MaxScore, Count, N);
loop([{Node,true}|RestStack], Children, SizeMap, MaxScore, Count, N) ->
    ChildList = maps:get(Node, Children, []),
    {SubSize, Score} = compute_score(ChildList, SizeMap, N),
    NewSizeMap = maps:put(Node, SubSize, SizeMap),
    case Score > MaxScore of
        true -> loop(RestStack, Children, NewSizeMap, Score, 1, N);
        false ->
            case Score == MaxScore of
                true -> loop(RestStack, Children, NewSizeMap, MaxScore, Count+1, N);
                false -> loop(RestStack, Children, NewSizeMap, MaxScore, Count, N)
            end
    end.

compute_score(ChildList, SizeMap, N) ->
    ChildSizes = [maps:get(C, SizeMap) || C <- ChildList],
    SubSize = 1 + lists:sum(ChildSizes),
    Rest = N - SubSize,
    Parts = case Rest > 0 of
                true -> [Rest|ChildSizes];
                false -> ChildSizes
            end,
    Score = lists:foldl(fun(A,B) -> A*B end, 1, Parts),
    {SubSize, Score}.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_highest_score_nodes(parents :: [integer]) :: integer
  def count_highest_score_nodes(parents) do
    n = length(parents)

    # Build children map: parent => list of its children
    children =
      Enum.with_index(parents)
      |> Enum.reduce(%{}, fn {p, i}, acc ->
        if p != -1 do
          Map.update(acc, p, [i], fn lst -> [i | lst] end)
        else
          acc
        end
      end)

    # Compute subtree sizes using iterative post‑order DFS
    subsize = :array.new(n, default: 0)
    stack = [{0, false}]

    subsize =
      while_stack(stack, children, subsize)

    # Evaluate scores and find the maximum count
    {max_score, cnt} =
      Enum.reduce(0..(n - 1), {-1, 0}, fn node, {mx, c} ->
        child_list = Map.get(children, node, [])
        prod_child = Enum.reduce(child_list, 1, fn ch, acc ->
          acc * :array.get(ch, subsize)
        end)

        rest = n - :array.get(node, subsize)
        score =
          if rest > 0 do
            prod_child * rest
          else
            prod_child
          end

        cond do
          score > mx -> {score, 1}
          score == mx -> {mx, c + 1}
          true -> {mx, c}
        end
      end)

    cnt
  end

  # Helper to process the stack iteratively
  defp while_stack([], _children, subsize), do: subsize

  defp while_stack([{node, true} | rest], children, subsize) do
    child_list = Map.get(children, node, [])
    size =
      1 +
        Enum.reduce(child_list, 0, fn ch, acc ->
          acc + :array.get(ch, subsize)
        end)

    new_subsize = :array.set(node, size, subsize)
    while_stack(rest, children, new_subsize)
  end

  defp while_stack([{node, false} | rest], children, subsize) do
    child_list = Map.get(children, node, [])
    # push visited marker then children onto stack
    new_stack =
      [{node, true}]
      |> Enum.concat(Enum.map(child_list, fn ch -> {ch, false} end))
      |> Kernel.++(rest)

    while_stack(new_stack, children, subsize)
  end
end
```
