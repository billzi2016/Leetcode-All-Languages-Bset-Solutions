# 1557. Minimum Number of Vertices to Reach All Nodes

## Cpp

```cpp
class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> indeg(n, 0);
        for (const auto& e : edges) {
            ++indeg[e[1]];
        }
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (indeg[i] == 0) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        int[] indegree = new int[n];
        for (List<Integer> edge : edges) {
            int to = edge.get(1);
            indegree[to]++;
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        return [i for i in range(n) if indegree[i] == 0]
```

## Python3

```python
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0] * n
        for _, to in edges:
            indeg[to] += 1
        return [i for i in range(n) if indeg[i] == 0]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSmallestSetOfVertices(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize; // unused
    int *indeg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int to = edges[i][1];
        indeg[to]++;
    }
    
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (indeg[i] == 0) cnt++;
    }
    
    int *res = (int *)malloc(cnt * sizeof(int));
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        if (indeg[i] == 0) {
            res[idx++] = i;
        }
    }
    
    free(indeg);
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindSmallestSetOfVertices(int n, IList<IList<int>> edges) {
        int[] indegree = new int[n];
        foreach (var edge in edges) {
            // edge[0] -> edge[1]
            indegree[edge[1]]++;
        }
        List<int> result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                result.Add(i);
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
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function(n, edges) {
    const indegree = new Array(n).fill(0);
    for (const [from, to] of edges) {
        indegree[to]++;
    }
    const result = [];
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) result.push(i);
    }
    return result;
};
```

## Typescript

```typescript
function findSmallestSetOfVertices(n: number, edges: number[][]): number[] {
    const indegree = new Array(n).fill(0);
    for (const [, to] of edges) {
        indegree[to]++;
    }
    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            result.push(i);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findSmallestSetOfVertices($n, $edges) {
        $hasIncoming = array_fill(0, $n, false);
        foreach ($edges as $edge) {
            $to = $edge[1];
            $hasIncoming[$to] = true;
        }
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if (!$hasIncoming[$i]) {
                $result[] = $i;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findSmallestSetOfVertices(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var indegree = Array(repeating: 0, count: n)
        for edge in edges {
            let to = edge[1]
            indegree[to] += 1
        }
        var result: [Int] = []
        for i in 0..<n {
            if indegree[i] == 0 {
                result.append(i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSmallestSetOfVertices(n: Int, edges: List<List<Int>>): List<Int> {
        val indegree = IntArray(n)
        for (edge in edges) {
            indegree[edge[1]]++
        }
        val result = ArrayList<Int>()
        for (i in 0 until n) {
            if (indegree[i] == 0) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findSmallestSetOfVertices(int n, List<List<int>> edges) {
    List<int> indegree = List.filled(n, 0);
    for (var edge in edges) {
      int to = edge[1];
      indegree[to]++;
    }
    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        result.add(i);
      }
    }
    return result;
  }
}
```

## Golang

```go
func findSmallestSetOfVertices(n int, edges [][]int) []int {
    hasIncoming := make([]bool, n)
    for _, e := range edges {
        if len(e) == 2 {
            hasIncoming[e[1]] = true
        }
    }
    res := make([]int, 0)
    for i := 0; i < n; i++ {
        if !hasIncoming[i] {
            res = append(res, i)
        }
    }
    return res
}
```

## Ruby

```ruby
def find_smallest_set_of_vertices(n, edges)
  indegree = Array.new(n, 0)
  edges.each do |from, to|
    indegree[to] += 1
  end
  result = []
  indegree.each_with_index { |deg, idx| result << idx if deg.zero? }
  result
end
```

## Scala

```scala
object Solution {
    def findSmallestSetOfVertices(n: Int, edges: List[List[Int]]): List[Int] = {
        val indegree = Array.fill[Int](n)(0)
        for (edge <- edges) {
            indegree(edge(1)) += 1
        }
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until n) {
            if (indegree(i) == 0) result += i
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut indeg = vec![0i32; n_usize];
        for e in edges.iter() {
            let to = e[1] as usize;
            indeg[to] += 1;
        }
        let mut res = Vec::new();
        for i in 0..n_usize {
            if indeg[i] == 0 {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-smallest-set-of-vertices n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let ([indeg (make-vector n 0)])
    (for-each
     (lambda (e)
       (define to (cadr e))
       (vector-set! indeg to (+ 1 (vector-ref indeg to))))
     edges)
    (for/list ([i (in-range n)] #:when (= (vector-ref indeg i) 0)) i)))
```

## Erlang

```erlang
-module(solution).
-export([find_smallest_set_of_vertices/2]).

-spec find_smallest_set_of_vertices(N :: integer(), Edges :: [[integer()]]) -> [integer()].
find_smallest_set_of_vertices(N, Edges) ->
    Indegrees = build_indegrees(Edges, #{}),
    [Node || Node <- lists:seq(0, N-1), not maps:is_key(Node, Indegrees)].

build_indegrees([], Acc) -> Acc;
build_indegrees([[_, To]|Rest], Acc) ->
    NewAcc = maps:update_with(To, fun(C) -> C + 1 end, 1, Acc),
    build_indegrees(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_smallest_set_of_vertices(n :: integer, edges :: [[integer]]) :: [integer]
  def find_smallest_set_of_vertices(n, edges) do
    indegree =
      Enum.reduce(edges, %{}, fn [_from, to], acc ->
        Map.update(acc, to, 1, &(&1 + 1))
      end)

    0..(n - 1)
    |> Enum.filter(fn v -> not Map.has_key?(indegree, v) end)
  end
end
```
