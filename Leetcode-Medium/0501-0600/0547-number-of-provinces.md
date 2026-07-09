# 0547. Number of Provinces

## Cpp

```cpp
class Solution {
public:
    void dfs(int node, const vector<vector<int>>& isConnected, vector<bool>& visited) {
        visited[node] = true;
        int n = isConnected.size();
        for (int j = 0; j < n; ++j) {
            if (isConnected[node][j] && !visited[j]) {
                dfs(j, isConnected, visited);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int provinces = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++provinces;
                dfs(i, isConnected, visited);
            }
        }
        return provinces;
    }
};
```

## Java

```java
class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinces = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, isConnected, visited);
                provinces++;
            }
        }
        return provinces;
    }

    private void dfs(int city, int[][] isConnected, boolean[] visited) {
        visited[city] = true;
        for (int neighbor = 0; neighbor < isConnected.length; neighbor++) {
            if (isConnected[city][neighbor] == 1 && !visited[neighbor]) {
                dfs(neighbor, isConnected, visited);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1
        return provinces
```

## Python3

```python
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei, conn in enumerate(isConnected[node]):
                if conn and not visited[nei]:
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void dfs(int node, int **matrix, int n, char *visited) {
    visited[node] = 1;
    for (int j = 0; j < n; ++j) {
        if (matrix[node][j] == 1 && !visited[j]) {
            dfs(j, matrix, n, visited);
        }
    }
}

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    int n = isConnectedSize;
    char *visited = (char *)calloc(n, sizeof(char));
    if (!visited) return 0; // allocation failure fallback

    int provinces = 0;
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            ++provinces;
            dfs(i, isConnected, n, visited);
        }
    }

    free(visited);
    return provinces;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindCircleNum(int[][] isConnected)
    {
        int n = isConnected.Length;
        bool[] visited = new bool[n];
        int provinces = 0;

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                provinces++;
                Dfs(i, isConnected, visited);
            }
        }

        return provinces;
    }

    private void Dfs(int node, int[][] graph, bool[] visited)
    {
        visited[node] = true;
        for (int j = 0; j < graph.Length; j++)
        {
            if (graph[node][j] == 1 && !visited[j])
            {
                Dfs(j, graph, visited);
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    const n = isConnected.length;
    const visited = new Array(n).fill(false);
    
    const dfs = (node) => {
        visited[node] = true;
        for (let nei = 0; nei < n; nei++) {
            if (isConnected[node][nei] === 1 && !visited[nei]) {
                dfs(nei);
            }
        }
    };
    
    let provinces = 0;
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            provinces++;
            dfs(i);
        }
    }
    return provinces;
};
```

## Typescript

```typescript
function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const visited = new Array<boolean>(n).fill(false);
    
    const dfs = (city: number) => {
        visited[city] = true;
        for (let neighbor = 0; neighbor < n; neighbor++) {
            if (isConnected[city][neighbor] === 1 && !visited[neighbor]) {
                dfs(neighbor);
            }
        }
    };
    
    let provinces = 0;
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            provinces++;
            dfs(i);
        }
    }
    return provinces;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $isConnected
     * @return Integer
     */
    function findCircleNum($isConnected) {
        $n = count($isConnected);
        $visited = array_fill(0, $n, false);
        $provinces = 0;

        for ($i = 0; $i < $n; $i++) {
            if (!$visited[$i]) {
                $provinces++;
                $stack = [$i];
                while (!empty($stack)) {
                    $node = array_pop($stack);
                    if ($visited[$node]) {
                        continue;
                    }
                    $visited[$node] = true;
                    for ($j = 0; $j < $n; $j++) {
                        if ($isConnected[$node][$j] == 1 && !$visited[$j]) {
                            $stack[] = $j;
                        }
                    }
                }
            }
        }

        return $provinces;
    }
}
```

## Swift

```swift
class Solution {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        let n = isConnected.count
        var visited = [Bool](repeating: false, count: n)
        var provinces = 0

        func dfs(_ node: Int) {
            visited[node] = true
            for neighbor in 0..<n {
                if isConnected[node][neighbor] == 1 && !visited[neighbor] {
                    dfs(neighbor)
                }
            }
        }

        for i in 0..<n {
            if !visited[i] {
                provinces += 1
                dfs(i)
            }
        }
        return provinces
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCircleNum(isConnected: Array<IntArray>): Int {
        val n = isConnected.size
        val visited = BooleanArray(n)
        var provinces = 0

        fun dfs(node: Int) {
            visited[node] = true
            for (neighbor in 0 until n) {
                if (isConnected[node][neighbor] == 1 && !visited[neighbor]) {
                    dfs(neighbor)
                }
            }
        }

        for (i in 0 until n) {
            if (!visited[i]) {
                provinces++
                dfs(i)
            }
        }
        return provinces
    }
}
```

## Dart

```dart
class Solution {
  int findCircleNum(List<List<int>> isConnected) {
    final n = isConnected.length;
    final visited = List<bool>.filled(n, false);

    void dfs(int i) {
      for (int j = 0; j < n; j++) {
        if (isConnected[i][j] == 1 && !visited[j]) {
          visited[j] = true;
          dfs(j);
        }
      }
    }

    int provinces = 0;
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        provinces++;
        visited[i] = true;
        dfs(i);
      }
    }
    return provinces;
  }
}
```

## Golang

```go
func findCircleNum(isConnected [][]int) int {
    n := len(isConnected)
    visited := make([]bool, n)

    var dfs func(int)
    dfs = func(i int) {
        visited[i] = true
        for j := 0; j < n; j++ {
            if isConnected[i][j] == 1 && !visited[j] {
                dfs(j)
            }
        }
    }

    provinces := 0
    for i := 0; i < n; i++ {
        if !visited[i] {
            provinces++
            dfs(i)
        }
    }
    return provinces
}
```

## Ruby

```ruby
def find_circle_num(is_connected)
  n = is_connected.size
  visited = Array.new(n, false)
  provinces = 0

  dfs = lambda do |city|
    visited[city] = true
    (0...n).each do |neighbor|
      if is_connected[city][neighbor] == 1 && !visited[neighbor]
        dfs.call(neighbor)
      end
    end
  end

  (0...n).each do |i|
    unless visited[i]
      provinces += 1
      dfs.call(i)
    end
  end

  provinces
end
```

## Scala

```scala
object Solution {
  def findCircleNum(isConnected: Array[Array[Int]]): Int = {
    val n = isConnected.length
    val visited = new Array[Boolean](n)

    def dfs(i: Int): Unit = {
      visited(i) = true
      var j = 0
      while (j < n) {
        if (isConnected(i)(j) == 1 && !visited(j)) {
          dfs(j)
        }
        j += 1
      }
    }

    var provinces = 0
    var i = 0
    while (i < n) {
      if (!visited(i)) {
        provinces += 1
        dfs(i)
      }
      i += 1
    }
    provinces
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut visited = vec![false; n];
        let mut provinces = 0;

        for i in 0..n {
            if !visited[i] {
                provinces += 1;
                let mut stack = Vec::new();
                stack.push(i);
                while let Some(node) = stack.pop() {
                    if visited[node] {
                        continue;
                    }
                    visited[node] = true;
                    for j in 0..n {
                        if is_connected[node][j] == 1 && !visited[j] {
                            stack.push(j);
                        }
                    }
                }
            }
        }

        provinces as i32
    }
}
```

## Racket

```racket
(define/contract (find-circle-num isConnected)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length isConnected))
         (visited (make-vector n #f)))
    (letrec ((dfs
              (lambda (i)
                (vector-set! visited i #t)
                (for ([j (in-range n)])
                  (when (and (= (list-ref (list-ref isConnected i) j) 1)
                             (not (vector-ref visited j)))
                    (dfs j))))))
      (let loop ((idx 0) (count 0))
        (if (>= idx n)
            count
            (if (vector-ref visited idx)
                (loop (+ idx 1) count)
                (begin
                  (dfs idx)
                  (loop (+ idx 1) (+ count 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_circle_num/1]).

find_circle_num(IsConnected) ->
    N = length(IsConnected),
    {Count, _} = lists:foldl(
        fun(Node, {Cnt, Vis}) ->
            case maps:is_key(Node, Vis) of
                true -> {Cnt, Vis};
                false ->
                    NewVis = dfs(Node, IsConnected, Vis),
                    {Cnt + 1, NewVis}
            end
        end,
        {0, #{}},
        lists:seq(0, N - 1)
    ),
    Count.

dfs(Node, IsConnected, Visited) ->
    case maps:is_key(Node, Visited) of
        true -> Visited;
        false ->
            Vis1 = maps:put(Node, true, Visited),
            Row = lists:nth(Node + 1, IsConnected),
            NeighborIndices = [
                Idx ||
                {Val, Idx} <- lists:zip(Row, lists:seq(0, length(Row) - 1)),
                Val =:= 1
            ],
            lists:foldl(
                fun(Nbr, AccVis) -> dfs(Nbr, IsConnected, AccVis) end,
                Vis1,
                NeighborIndices
            )
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_circle_num(is_connected :: [[integer]]) :: integer
  def find_circle_num(is_connected) do
    n = length(is_connected)

    {count, _visited} =
      Enum.reduce(0..(n - 1), {0, MapSet.new()}, fn i, {cnt, visited} ->
        if MapSet.member?(visited, i) do
          {cnt, visited}
        else
          visited = dfs(i, is_connected, visited)
          {cnt + 1, visited}
        end
      end)

    count
  end

  defp dfs(i, is_connected, visited) do
    if MapSet.member?(visited, i) do
      visited
    else
      visited = MapSet.put(visited, i)
      row = Enum.at(is_connected, i)

      Enum.reduce(0..(length(row) - 1), visited, fn j, acc ->
        if Enum.at(row, j) == 1 do
          dfs(j, is_connected, acc)
        else
          acc
        end
      end)
    end
  end
end
```
