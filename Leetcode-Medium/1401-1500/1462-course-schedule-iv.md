# 1462. Course Schedule IV

## Cpp

```cpp
class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        const int MAXN = 100;
        vector<bitset<MAXN>> reach(numCourses);
        for (const auto& p : prerequisites) {
            reach[p[0]].set(p[1]);
        }
        for (int k = 0; k < numCourses; ++k) {
            for (int i = 0; i < numCourses; ++i) {
                if (reach[i][k]) {
                    reach[i] |= reach[k];
                }
            }
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            ans.push_back(reach[q[0]][q[1]]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] reach = new boolean[numCourses][numCourses];
        for (int[] pre : prerequisites) {
            reach[pre[0]][pre[1]] = true;
        }
        for (int k = 0; k < numCourses; ++k) {
            for (int i = 0; i < numCourses; ++i) {
                if (reach[i][k]) {
                    for (int j = 0; j < numCourses; ++j) {
                        if (reach[k][j]) {
                            reach[i][j] = true;
                        }
                    }
                }
            }
        }
        List<Boolean> ans = new ArrayList<>(queries.length);
        for (int[] q : queries) {
            ans.add(reach[q[0]][q[1]]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Initialize reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True

        # Floyd-Warshall to compute transitive closure
        for k in range(numCourses):
            rk = reachable[k]
            for i in range(numCourses):
                if reachable[i][k]:
                    ri = reachable[i]
                    # combine paths i->k and k->*
                    for j in range(numCourses):
                        if rk[j]:
                            ri[j] = True

        return [reachable[u][v] for u, v in queries]
```

## Python3

```python
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reach[a][b] = True

        for k in range(numCourses):
            rk = reach[k]
            for i in range(numCourses):
                if reach[i][k]:
                    ri = reach[i]
                    for j in range(numCourses):
                        if rk[j]:
                            ri[j] = True

        return [reach[u][v] for u, v in queries]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* checkIfPrerequisite(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize,
                          int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // Allocate reachability matrix
    bool *reach = (bool *)calloc(numCourses * numCourses, sizeof(bool));
    
    // Direct edges
    for (int i = 0; i < prerequisitesSize; ++i) {
        int a = prerequisites[i][0];
        int b = prerequisites[i][1];
        reach[a * numCourses + b] = true;
    }
    
    // Floyd-Warshall transitive closure
    for (int k = 0; k < numCourses; ++k) {
        for (int i = 0; i < numCourses; ++i) {
            if (!reach[i * numCourses + k]) continue;
            for (int j = 0; j < numCourses; ++j) {
                if (reach[k * numCourses + j])
                    reach[i * numCourses + j] = true;
            }
        }
    }
    
    // Answer queries
    bool *answer = (bool *)malloc(sizeof(bool) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int v = queries[i][1];
        answer[i] = reach[u * numCourses + v];
    }
    
    free(reach);
    *returnSize = queriesSize;
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<bool> CheckIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries)
    {
        bool[,] reach = new bool[numCourses, numCourses];

        foreach (var pre in prerequisites)
        {
            int a = pre[0];
            int b = pre[1];
            reach[a, b] = true;
        }

        for (int k = 0; k < numCourses; k++)
        {
            for (int i = 0; i < numCourses; i++)
            {
                if (!reach[i, k]) continue;
                for (int j = 0; j < numCourses; j++)
                {
                    if (reach[k, j])
                        reach[i, j] = true;
                }
            }
        }

        List<bool> answer = new List<bool>(queries.Length);
        foreach (var q in queries)
        {
            answer.Add(reach[q[0], q[1]]);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var checkIfPrerequisite = function(numCourses, prerequisites, queries) {
    const reach = Array.from({ length: numCourses }, () => Array(numCourses).fill(false));
    
    for (const [u, v] of prerequisites) {
        reach[u][v] = true;
    }
    
    for (let k = 0; k < numCourses; k++) {
        for (let i = 0; i < numCourses; i++) {
            if (reach[i][k]) {
                for (let j = 0; j < numCourses; j++) {
                    if (reach[k][j]) {
                        reach[i][j] = true;
                    }
                }
            }
        }
    }
    
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [u, v] = queries[i];
        ans[i] = reach[u][v];
    }
    return ans;
};
```

## Typescript

```typescript
function checkIfPrerequisite(numCourses: number, prerequisites: number[][], queries: number[][]): boolean[] {
    const reach: boolean[][] = Array.from({ length: numCourses }, () => Array(numCourses).fill(false));
    
    for (const [u, v] of prerequisites) {
        reach[u][v] = true;
    }
    
    for (let k = 0; k < numCourses; k++) {
        for (let i = 0; i < numCourses; i++) {
            if (reach[i][k]) {
                for (let j = 0; j < numCourses; j++) {
                    if (reach[k][j]) {
                        reach[i][j] = true;
                    }
                }
            }
        }
    }
    
    const answer: boolean[] = [];
    for (const [u, v] of queries) {
        answer.push(reach[u][v]);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numCourses
     * @param Integer[][] $prerequisites
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function checkIfPrerequisite($numCourses, $prerequisites, $queries) {
        // Initialize reachability matrix
        $reach = array_fill(0, $numCourses, array_fill(0, $numCourses, false));
        foreach ($prerequisites as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $reach[$a][$b] = true;
        }

        // Floyd-Warshall to compute transitive closure
        for ($k = 0; $k < $numCourses; $k++) {
            for ($i = 0; $i < $numCourses; $i++) {
                if ($reach[$i][$k]) { // only proceed if i can reach k
                    for ($j = 0; $j < $numCourses; $j++) {
                        if ($reach[$k][$j]) {
                            $reach[$i][$j] = true;
                        }
                    }
                }
            }
        }

        // Answer queries
        $answer = [];
        foreach ($queries as $q) {
            $answer[] = $reach[$q[0]][$q[1]];
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func checkIfPrerequisite(_ numCourses: Int, _ prerequisites: [[Int]], _ queries: [[Int]]) -> [Bool] {
        var reach = Array(repeating: Array(repeating: false, count: numCourses), count: numCourses)
        for p in prerequisites {
            let a = p[0]
            let b = p[1]
            reach[a][b] = true
        }
        for k in 0..<numCourses {
            for i in 0..<numCourses where reach[i][k] {
                for j in 0..<numCourses where reach[k][j] {
                    if !reach[i][j] {
                        reach[i][j] = true
                    }
                }
            }
        }
        var result = [Bool]()
        result.reserveCapacity(queries.count)
        for q in queries {
            result.append(reach[q[0]][q[1]])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkIfPrerequisite(numCourses: Int, prerequisites: Array<IntArray>, queries: Array<IntArray>): List<Boolean> {
        val reach = Array(numCourses) { BooleanArray(numCourses) }
        for (p in prerequisites) {
            reach[p[0]][p[1]] = true
        }
        for (k in 0 until numCourses) {
            for (i in 0 until numCourses) {
                if (reach[i][k]) {
                    for (j in 0 until numCourses) {
                        if (reach[k][j]) {
                            reach[i][j] = true
                        }
                    }
                }
            }
        }
        val result = ArrayList<Boolean>(queries.size)
        for (q in queries) {
            result.add(reach[q[0]][q[1]])
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> checkIfPrerequisite(int numCourses, List<List<int>> prerequisites, List<List<int>> queries) {
    // Initialize reachability matrix
    List<List<bool>> reach = List.generate(numCourses, (_) => List.filled(numCourses, false));
    
    // Direct prerequisites
    for (var pre in prerequisites) {
      int a = pre[0];
      int b = pre[1];
      reach[a][b] = true;
    }
    
    // Floyd-Warshall to compute transitive closure
    for (int k = 0; k < numCourses; ++k) {
      for (int i = 0; i < numCourses; ++i) {
        if (reach[i][k]) {
          for (int j = 0; j < numCourses; ++j) {
            if (reach[k][j]) {
              reach[i][j] = true;
            }
          }
        }
      }
    }
    
    // Answer queries
    List<bool> answer = [];
    for (var q in queries) {
      answer.add(reach[q[0]][q[1]]);
    }
    return answer;
  }
}
```

## Golang

```go
func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {
    reachable := make([][]bool, numCourses)
    for i := 0; i < numCourses; i++ {
        reachable[i] = make([]bool, numCourses)
    }
    for _, p := range prerequisites {
        a, b := p[0], p[1]
        reachable[a][b] = true
    }

    for k := 0; k < numCourses; k++ {
        for i := 0; i < numCourses; i++ {
            if reachable[i][k] {
                for j := 0; j < numCourses; j++ {
                    if reachable[k][j] && !reachable[i][j] {
                        reachable[i][j] = true
                    }
                }
            }
        }
    }

    ans := make([]bool, len(queries))
    for idx, q := range queries {
        u, v := q[0], q[1]
        ans[idx] = reachable[u][v]
    }
    return ans
}
```

## Ruby

```ruby
def check_if_prerequisite(num_courses, prerequisites, queries)
  reach = Array.new(num_courses) { Array.new(num_courses, false) }
  prerequisites.each do |a, b|
    reach[a][b] = true
  end

  (0...num_courses).each do |k|
    (0...num_courses).each do |i|
      next unless reach[i][k]
      (0...num_courses).each do |j|
        reach[i][j] ||= reach[k][j]
      end
    end
  end

  queries.map { |u, v| reach[u][v] }
end
```

## Scala

```scala
object Solution {
    def checkIfPrerequisite(numCourses: Int, prerequisites: Array[Array[Int]], queries: Array[Array[Int]]): List[Boolean] = {
        val n = numCourses
        val reach = Array.ofDim[Boolean](n, n)
        for (p <- prerequisites) {
            reach(p(0))(p(1)) = true
        }
        for (k <- 0 until n) {
            for (i <- 0 until n) {
                if (reach(i)(k)) {
                    for (j <- 0 until n) {
                        if (reach(k)(j)) {
                            reach(i)(j) = true
                        }
                    }
                }
            }
        }
        queries.map(q => reach(q(0))(q(1))).toList
    }
}
```

## Rust

```rust
struct Solution;

impl Solution {
    pub fn check_if_prerequisite(
        num_courses: i32,
        prerequisites: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n = num_courses as usize;
        let mut reach = vec![vec![false; n]; n];

        for p in &prerequisites {
            let a = p[0] as usize;
            let b = p[1] as usize;
            reach[a][b] = true;
        }

        for k in 0..n {
            for i in 0..n {
                if reach[i][k] {
                    for j in 0..n {
                        if reach[k][j] {
                            reach[i][j] = true;
                        }
                    }
                }
            }
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in &queries {
            let u = q[0] as usize;
            let v = q[1] as usize;
            ans.push(reach[u][v]);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (check-if-prerequisite numCourses prerequisites queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof boolean?))
  (let* ([n numCourses]
         [reach (make-vector n)])
    ;; initialize matrix
    (for ([i (in-range n)])
      (vector-set! reach i (make-vector n #f)))
    ;; direct edges
    (for ([pair prerequisites])
      (let* ([a (first pair)]
             [b (second pair)]
             [row (vector-ref reach a)])
        (vector-set! row b #t)))
    ;; Floyd‑Warshall transitive closure
    (for ([k (in-range n)])
      (for ([i (in-range n)])
        (when (vector-ref (vector-ref reach i) k)
          (let* ([row-i (vector-ref reach i)]
                 [row-k (vector-ref reach k)])
            (for ([j (in-range n)])
              (when (vector-ref row-k j)
                (vector-set! row-i j #t)))))))
    ;; answer queries
    (map (lambda (q)
           (let* ([u (first q)]
                  [v (second q)])
             (vector-ref (vector-ref reach u) v)))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([check_if_prerequisite/3]).

-spec check_if_prerequisite(integer(), [[integer()]], [[integer()]]) -> [boolean()].
check_if_prerequisite(NumCourses, Prerequisites, Queries) ->
    Rows0 = init_rows(NumCourses),
    Rows1 = add_prereqs(Rows0, Prerequisites),
    Closure = floyd(Rows1, NumCourses),
    [maps:is_key(V, maps:get(U, Closure)) || [U, V] <- Queries].

init_rows(N) ->
    lists:foldl(fun(I, Acc) -> maps:put(I, #{}, Acc) end,
                #{},
                lists:seq(0, N - 1)).

add_prereqs(Rows, PrList) ->
    lists:foldl(fun([A, B], AccRows) ->
        RowA = maps:get(A, AccRows),
        NewRowA = maps:put(B, true, RowA),
        maps:put(A, NewRowA, AccRows)
    end, Rows, PrList).

floyd(Rows, N) ->
    lists:foldl(fun(K, RowsK) ->
        RowK = maps:get(K, RowsK),
        lists:foldl(fun(I, RowsI) ->
            RowI = maps:get(I, RowsI),
            case maps:is_key(K, RowI) of
                true ->
                    NewRowI = maps:merge(RowI, RowK),
                    maps:put(I, NewRowI, RowsI);
                false -> RowsI
            end
        end, RowsK, lists:seq(0, N - 1))
    end, Rows, lists:seq(0, N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_if_prerequisite(num_courses :: integer, prerequisites :: [[integer]], queries :: [[integer]]) :: [boolean]
  def check_if_prerequisite(num_courses, prerequisites, queries) do
    init_row = List.duplicate(false, num_courses)
    matrix0 = for _ <- 0..num_courses - 1, do: init_row

    matrix1 =
      Enum.reduce(prerequisites, matrix0, fn [a, b], acc ->
        List.update_at(acc, a, fn row -> List.replace_at(row, b, true) end)
      end)

    matrix2 =
      Enum.reduce(0..num_courses - 1, matrix1, fn k, mat_k ->
        Enum.reduce(0..num_courses - 1, mat_k, fn i, mat_i ->
          if Enum.at(Enum.at(mat_i, i), k) do
            row_i = Enum.at(mat_i, i)
            row_k = Enum.at(mat_i, k)

            new_row =
              Enum.zip(row_i, row_k)
              |> Enum.map(fn {x, y} -> x or y end)

            List.update_at(mat_i, i, fn _ -> new_row end)
          else
            mat_i
          end
        end)
      end)

    Enum.map(queries, fn [u, v] ->
      Enum.at(Enum.at(matrix2, u), v)
    end)
  end
end
```
