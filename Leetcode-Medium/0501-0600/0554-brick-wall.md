# 0554. Brick Wall

## Cpp

```cpp
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> edgeCount;
        int rows = wall.size();
        for (const auto& row : wall) {
            int sum = 0;
            // exclude the last brick to avoid the rightmost edge
            for (size_t i = 0; i + 1 < row.size(); ++i) {
                sum += row[i];
                ++edgeCount[sum];
            }
        }
        int maxEdges = 0;
        for (const auto& p : edgeCount) {
            if (p.second > maxEdges) maxEdges = p.second;
        }
        return rows - maxEdges;
    }
};
```

## Java

```java
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        if (wall == null || wall.isEmpty()) return 0;
        Map<Integer, Integer> edgeCount = new HashMap<>();
        for (List<Integer> row : wall) {
            int sum = 0;
            // exclude the last brick to avoid counting the rightmost edge
            for (int i = 0; i < row.size() - 1; i++) {
                sum += row.get(i);
                edgeCount.put(sum, edgeCount.getOrDefault(sum, 0) + 1);
            }
        }
        int maxEdges = 0;
        for (int cnt : edgeCount.values()) {
            if (cnt > maxEdges) maxEdges = cnt;
        }
        return wall.size() - maxEdges;
    }
}
```

## Python

```python
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        edge_counts = defaultdict(int)
        for row in wall:
            cum = 0
            # exclude the last brick to avoid counting the right edge of the wall
            for w in row[:-1]:
                cum += w
                edge_counts[cum] += 1
        if not edge_counts:
            return len(wall)
        max_edges = max(edge_counts.values())
        return len(wall) - max_edges
```

## Python3

```python
class Solution:
    def leastBricks(self, wall):
        edge_counts = {}
        for row in wall:
            cum = 0
            # exclude the last brick to avoid counting the rightmost edge
            for w in row[:-1]:
                cum += w
                edge_counts[cum] = edge_counts.get(cum, 0) + 1
        if not edge_counts:
            return len(wall)
        max_edges = max(edge_counts.values())
        return len(wall) - max_edges
```

## C

```c
int cmp_ll(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int leastBricks(int** wall, int wallSize, int* wallColSize) {
    if (wallSize == 0) return 0;

    // Count total number of edge positions (excluding the rightmost edge)
    int totalEdges = 0;
    for (int i = 0; i < wallSize; ++i) {
        totalEdges += wallColSize[i] - 1;
    }

    if (totalEdges == 0) {
        // Every row consists of a single brick
        return wallSize;
    }

    long long *edges = (long long *)malloc(sizeof(long long) * totalEdges);
    int idx = 0;

    for (int i = 0; i < wallSize; ++i) {
        long long cum = 0;
        for (int j = 0; j < wallColSize[i] - 1; ++j) {
            cum += (long long)wall[i][j];
            edges[idx++] = cum;
        }
    }

    qsort(edges, totalEdges, sizeof(long long), cmp_ll);

    int maxCount = 0;
    int i = 0;
    while (i < totalEdges) {
        int j = i + 1;
        while (j < totalEdges && edges[j] == edges[i]) {
            ++j;
        }
        int cnt = j - i;
        if (cnt > maxCount) maxCount = cnt;
        i = j;
    }

    free(edges);
    return wallSize - maxCount;
}
```

## Csharp

```csharp
public class Solution
{
    public int LeastBricks(IList<IList<int>> wall)
    {
        var edgeCount = new Dictionary<long, int>();
        foreach (var row in wall)
        {
            long sum = 0;
            // exclude the last brick to avoid counting the rightmost edge
            for (int i = 0; i < row.Count - 1; i++)
            {
                sum += row[i];
                if (edgeCount.ContainsKey(sum))
                    edgeCount[sum]++;
                else
                    edgeCount[sum] = 1;
            }
        }

        int maxEdges = 0;
        foreach (var cnt in edgeCount.Values)
        {
            if (cnt > maxEdges) maxEdges = cnt;
        }

        return wall.Count - maxEdges;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    const edgeCount = new Map();
    for (const row of wall) {
        let sum = 0;
        // exclude the last brick to avoid counting the right edge of the wall
        for (let i = 0; i < row.length - 1; ++i) {
            sum += row[i];
            edgeCount.set(sum, (edgeCount.get(sum) || 0) + 1);
        }
    }
    let maxEdges = 0;
    for (const cnt of edgeCount.values()) {
        if (cnt > maxEdges) maxEdges = cnt;
    }
    return wall.length - maxEdges;
};
```

## Typescript

```typescript
function leastBricks(wall: number[][]): number {
    const edgeCount = new Map<number, number>();
    for (const row of wall) {
        let sum = 0;
        // exclude the last brick to avoid counting the rightmost edge
        for (let i = 0; i < row.length - 1; ++i) {
            sum += row[i];
            edgeCount.set(sum, (edgeCount.get(sum) ?? 0) + 1);
        }
    }
    let maxEdges = 0;
    for (const cnt of edgeCount.values()) {
        if (cnt > maxEdges) maxEdges = cnt;
    }
    return wall.length - maxEdges;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $wall
     * @return Integer
     */
    function leastBricks($wall) {
        $edgeCount = [];
        foreach ($wall as $row) {
            $sum = 0;
            $len = count($row);
            // exclude the last brick to avoid counting the right edge of the wall
            for ($i = 0; $i < $len - 1; $i++) {
                $sum += $row[$i];
                if (isset($edgeCount[$sum])) {
                    $edgeCount[$sum]++;
                } else {
                    $edgeCount[$sum] = 1;
                }
            }
        }

        $maxEdges = 0;
        foreach ($edgeCount as $cnt) {
            if ($cnt > $maxEdges) {
                $maxEdges = $cnt;
            }
        }

        return count($wall) - $maxEdges;
    }
}
```

## Swift

```swift
class Solution {
    func leastBricks(_ wall: [[Int]]) -> Int {
        var edgeCounts = [Int:Int]()
        for row in wall {
            var position = 0
            if row.count > 1 {
                for i in 0..<(row.count - 1) {
                    position += row[i]
                    edgeCounts[position, default: 0] += 1
                }
            }
        }
        let maxEdges = edgeCounts.values.max() ?? 0
        return wall.count - maxEdges
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun leastBricks(wall: List<List<Int>>): Int {
        val edgeCounts = HashMap<Int, Int>()
        for (row in wall) {
            var sum = 0
            // Exclude the last brick to avoid counting the right edge of the wall
            for (i in 0 until row.size - 1) {
                sum += row[i]
                edgeCounts[sum] = edgeCounts.getOrDefault(sum, 0) + 1
            }
        }
        var maxEdges = 0
        for (cnt in edgeCounts.values) {
            if (cnt > maxEdges) maxEdges = cnt
        }
        return wall.size - maxEdges
    }
}
```

## Dart

```dart
class Solution {
  int leastBricks(List<List<int>> wall) {
    final Map<int, int> edgeCounts = {};
    for (final row in wall) {
      int sum = 0;
      for (int i = 0; i < row.length - 1; ++i) {
        sum += row[i];
        edgeCounts[sum] = (edgeCounts[sum] ?? 0) + 1;
      }
    }
    int maxEdges = 0;
    edgeCounts.forEach((_, count) {
      if (count > maxEdges) maxEdges = count;
    });
    return wall.length - maxEdges;
  }
}
```

## Golang

```go
func leastBricks(wall [][]int) int {
    edgeCount := make(map[int]int)
    for _, row := range wall {
        sum := 0
        // exclude the last brick to avoid counting the rightmost edge
        for i := 0; i < len(row)-1; i++ {
            sum += row[i]
            edgeCount[sum]++
        }
    }
    maxFreq := 0
    for _, cnt := range edgeCount {
        if cnt > maxFreq {
            maxFreq = cnt
        }
    }
    return len(wall) - maxFreq
}
```

## Ruby

```ruby
def least_bricks(wall)
  edge_counts = Hash.new(0)

  wall.each do |row|
    sum = 0
    (0...row.length - 1).each do |i|
      sum += row[i]
      edge_counts[sum] += 1
    end
  end

  max_edges = edge_counts.values.max || 0
  wall.size - max_edges
end
```

## Scala

```scala
object Solution {
    def leastBricks(wall: List[List[Int]]): Int = {
        import scala.collection.mutable

        val edgeCount = mutable.Map[Int, Int]()
        for (row <- wall) {
            var sum = 0
            // exclude the last brick to avoid the rightmost edge
            for (i <- 0 until row.length - 1) {
                sum += row(i)
                edgeCount.update(sum, edgeCount.getOrElse(sum, 0) + 1)
            }
        }

        if (edgeCount.isEmpty) wall.length
        else wall.length - edgeCount.values.max
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        let mut edge_counts: HashMap<i32, i32> = HashMap::new();
        for row in wall.iter() {
            let mut sum = 0;
            // exclude the last brick to avoid counting the rightmost edge
            for (i, &brick) in row.iter().enumerate() {
                sum += brick;
                if i + 1 < row.len() {
                    *edge_counts.entry(sum).or_insert(0) += 1;
                }
            }
        }
        let max_edges = edge_counts.values().max().cloned().unwrap_or(0);
        (wall.len() as i32) - max_edges
    }
}
```

## Racket

```racket
#lang racket

(define/contract (least-bricks wall)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length wall))
         (counts (make-hash)))
    (for-each
     (lambda (row)
       (let loop ((sum 0) (lst row))
         (cond
           [(null? lst) (void)]
           [else
            (define w (car lst))
            (set! sum (+ sum w))
            (when (pair? (cdr lst)) ; not the last brick in this row
              (hash-update! counts sum (lambda (old) (+ old 1)) 1))
            (loop sum (cdr lst))])))
     wall)
    (define max-freq
      (let ((max 0))
        (hash-for-each counts (lambda (_ v) (when (> v max) (set! max v))))
        max))
    (- n max-freq)))
```

## Erlang

```erlang
-module(solution).
-export([least_bricks/1]).

-spec least_bricks(Wall :: [[integer()]]) -> integer().
least_bricks(Wall) ->
    Map = lists:foldl(fun(Row, AccMap) ->
        PosList = positions(Row),
        update_map(PosList, AccMap)
    end, #{}, Wall),
    MaxFreq = maps:fold(fun(_Key, Val, Max) ->
        if Val > Max -> Val; true -> Max end
    end, 0, Map),
    N = length(Wall),
    N - MaxFreq.

positions(Row) ->
    positions(Row, 0, []).

positions([_Last], _Sum, Acc) ->
    lists:reverse(Acc);
positions([H|T], Sum, Acc) ->
    NewSum = Sum + H,
    positions(T, NewSum, [NewSum | Acc]).

update_map([], Map) -> Map;
update_map([Pos|Rest], Map) ->
    Count = maps:get(Pos, Map, 0),
    NewMap = maps:put(Pos, Count + 1, Map),
    update_map(Rest, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec least_bricks(wall :: [[integer]]) :: integer
  def least_bricks(wall) do
    n = length(wall)

    counts =
      Enum.reduce(wall, %{}, fn row, acc ->
        positions = Enum.scan(row, 0, fn brick, sum -> sum + brick end)
        internal = Enum.slice(positions, 1, length(row) - 1)

        Enum.reduce(internal, acc, fn pos, map ->
          Map.update(map, pos, 1, &(&1 + 1))
        end)
      end)

    max_edges =
      case Map.values(counts) do
        [] -> 0
        vals -> Enum.max(vals)
      end

    n - max_edges
  end
end
```
