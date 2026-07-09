# 2924. Find Champion II

## Cpp

```cpp
class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> indeg(n, 0);
        for (const auto& e : edges) {
            // edge from u to v means u stronger than v
            indeg[e[1]]++;
        }
        int champ = -1;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (indeg[i] == 0) {
                ++cnt;
                champ = i;
                if (cnt > 1) return -1; // early exit if more than one
            }
        }
        return cnt == 1 ? champ : -1;
    }
};
```

## Java

```java
class Solution {
    public int findChampion(int n, int[][] edges) {
        int[] indegree = new int[n];
        for (int[] edge : edges) {
            indegree[edge[1]]++;
        }
        int champion = -1;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                champion = i;
                count++;
                if (count > 1) {
                    return -1;
                }
            }
        }
        return count == 1 ? champion : -1;
    }
}
```

## Python

```python
class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        champ = -1
        count = 0
        for i in range(n):
            if indegree[i] == 0:
                champ = i
                count += 1
                if count > 1:
                    return -1
        return champ if count == 1 else -1
```

## Python3

```python
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        champion = -1
        count = 0
        for i in range(n):
            if indegree[i] == 0:
                count += 1
                champion = i
                if count > 1:
                    return -1
        return champion if count == 1 else -1
```

## C

```c
int findChampion(int n, int** edges, int edgesSize, int* edgesColSize) {
    int indegree[101] = {0};
    for (int i = 0; i < edgesSize; ++i) {
        int v = edges[i][1];
        indegree[v]++;
    }
    int champ = -1;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (indegree[i] == 0) {
            champ = i;
            cnt++;
        }
    }
    return cnt == 1 ? champ : -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindChampion(int n, int[][] edges)
    {
        int[] indegree = new int[n];
        if (edges != null)
        {
            foreach (var edge in edges)
            {
                // edge[0] is stronger than edge[1]
                indegree[edge[1]]++;
            }
        }

        int champion = -1;
        int countZero = 0;
        for (int i = 0; i < n; i++)
        {
            if (indegree[i] == 0)
            {
                champion = i;
                countZero++;
            }
        }

        return countZero == 1 ? champion : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function(n, edges) {
    const indegree = new Array(n).fill(0);
    for (const [u, v] of edges) {
        indegree[v]++;
    }
    let champion = -1;
    let countZero = 0;
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            countZero++;
            champion = i;
            if (countZero > 1) return -1; // early exit if more than one
        }
    }
    return countZero === 1 ? champion : -1;
};
```

## Typescript

```typescript
function findChampion(n: number, edges: number[][]): number {
    const indegree = new Array(n).fill(0);
    for (const [_, v] of edges) {
        indegree[v]++;
    }
    let champion = -1;
    let zeroCount = 0;
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            champion = i;
            zeroCount++;
            if (zeroCount > 1) return -1;
        }
    }
    return zeroCount === 1 ? champion : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function findChampion($n, $edges) {
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $v = $e[1];
            $indeg[$v]++;
        }
        $champ = -1;
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] === 0) {
                $cnt++;
                $champ = $i;
            }
        }
        return $cnt === 1 ? $champ : -1;
    }
}
```

## Swift

```swift
class Solution {
    func findChampion(_ n: Int, _ edges: [[Int]]) -> Int {
        var indegree = Array(repeating: 0, count: n)
        for edge in edges {
            let v = edge[1]
            indegree[v] += 1
        }
        var champion = -1
        var zeroCount = 0
        for i in 0..<n {
            if indegree[i] == 0 {
                champion = i
                zeroCount += 1
            }
        }
        return zeroCount == 1 ? champion : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findChampion(n: Int, edges: Array<IntArray>): Int {
        val indegree = IntArray(n)
        for (e in edges) {
            // e[0] -> stronger than e[1]
            indegree[e[1]]++
        }
        var champion = -1
        var countZero = 0
        for (i in 0 until n) {
            if (indegree[i] == 0) {
                champion = i
                countZero++
                if (countZero > 1) return -1
            }
        }
        return if (countZero == 1) champion else -1
    }
}
```

## Dart

```dart
class Solution {
  int findChampion(int n, List<List<int>> edges) {
    List<int> indegree = List.filled(n, 0);
    for (var edge in edges) {
      int v = edge[1];
      indegree[v]++;
    }
    int champ = -1;
    int count = 0;
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        champ = i;
        count++;
        if (count > 1) return -1;
      }
    }
    return count == 1 ? champ : -1;
  }
}
```

## Golang

```go
func findChampion(n int, edges [][]int) int {
	indeg := make([]int, n)
	for _, e := range edges {
		if len(e) == 2 {
			v := e[1]
			indeg[v]++
		}
	}
	champ := -1
	count := 0
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			champ = i
			count++
			if count > 1 {
				return -1
			}
		}
	}
	if count == 1 {
		return champ
	}
	return -1
}
```

## Ruby

```ruby
def find_champion(n, edges)
  indegree = Array.new(n, 0)
  edges.each do |u, v|
    indegree[v] += 1
  end

  champion = -1
  count = 0
  n.times do |i|
    if indegree[i].zero?
      champion = i
      count += 1
    end
  end

  count == 1 ? champion : -1
end
```

## Scala

```scala
object Solution {
    def findChampion(n: Int, edges: Array[Array[Int]]): Int = {
        val indegree = new Array[Int](n)
        var i = 0
        while (i < edges.length) {
            val v = edges(i)(1)
            indegree(v) += 1
            i += 1
        }
        var champ = -1
        var count = 0
        var j = 0
        while (j < n) {
            if (indegree(j) == 0) {
                champ = j
                count += 1
                if (count > 1) return -1
            }
            j += 1
        }
        if (count == 1) champ else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_champion(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut indegree = vec![0i32; n_usize];
        for e in edges.iter() {
            // each edge is [u, v] meaning u stronger than v
            if e.len() >= 2 {
                let v = e[1] as usize;
                indegree[v] += 1;
            }
        }
        let mut champion = -1;
        let mut cnt = 0;
        for i in 0..n_usize {
            if indegree[i] == 0 {
                champion = i as i32;
                cnt += 1;
            }
        }
        if cnt == 1 { champion } else { -1 }
    }
}
```

## Racket

```racket
(define/contract (find-champion n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((indeg (make-vector n 0))
         (process-edge
          (lambda (e)
            (let ((v (list-ref e 1)))
              (vector-set! indeg v (+ (vector-ref indeg v) 1))))))
    (for-each process-edge edges)
    (let loop ((i 0) (champ -1) (cnt 0))
      (if (= i n)
          (if (= cnt 1) champ -1)
          (let ((deg (vector-ref indeg i)))
            (if (= deg 0)
                (loop (+ i 1) i (+ cnt 1))
                (loop (+ i 1) champ cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_champion/2]).

-spec find_champion(N :: integer(), Edges :: [[integer()]]) -> integer().
find_champion(N, Edges) ->
    IndegMap = build_indegree_map(Edges, #{}),
    find_unique_zero(0, N, IndegMap, -1, 0).

build_indegree_map([], Map) ->
    Map;
build_indegree_map([[_, V] | Rest], Map) ->
    Count = maps:get(V, Map, 0) + 1,
    build_indegree_map(Rest, Map#{V => Count}).

find_unique_zero(Index, N, _Map, Champ, Count) when Index == N ->
    case Count of
        1 -> Champ;
        _ -> -1
    end;
find_unique_zero(Index, N, Map, Champ, Count) ->
    Indeg = maps:get(Index, Map, 0),
    if Indeg == 0 ->
            find_unique_zero(Index + 1, N, Map, Index, Count + 1);
       true ->
            find_unique_zero(Index + 1, N, Map, Champ, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_champion(n :: integer, edges :: [[integer]]) :: integer
  def find_champion(n, edges) do
    indegrees = List.duplicate(0, n)

    indegrees =
      Enum.reduce(edges, indegrees, fn [_u, v], acc ->
        List.update_at(acc, v, &(&1 + 1))
      end)

    {champ, cnt} =
      Enum.with_index(indegrees)
      |> Enum.reduce({-1, 0}, fn
        {0, idx}, {_c, c} -> {idx, c + 1}
        {_deg, _idx}, acc -> acc
      end)

    if cnt == 1, do: champ, else: -1
  end
end
```
