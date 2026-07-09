# 0939. Minimum Area Rectangle

## Cpp

```cpp
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        unordered_set<long long> pointSet;
        const long long SHIFT = (1LL << 32);
        for (const auto& p : points) {
            long long key = ((long long)p[0] << 32) | (unsigned int)p[1];
            pointSet.insert(key);
        }
        int minArea = INT_MAX;
        int n = points.size();
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue; // not diagonal
                long long key1 = ((long long)x1 << 32) | (unsigned int)y2;
                long long key2 = ((long long)x2 << 32) | (unsigned int)y1;
                if (pointSet.count(key1) && pointSet.count(key2)) {
                    int area = abs(x1 - x2) * abs(y1 - y2);
                    minArea = min(minArea, area);
                }
            }
        }
        return minArea == INT_MAX ? 0 : minArea;
    }
};
```

## Java

```java
class Solution {
    public int minAreaRect(int[][] points) {
        Set<Long> pointSet = new HashSet<>();
        for (int[] p : points) {
            long key = ((long) p[0] << 32) | (p[1] & 0xffffffffL);
            pointSet.add(key);
        }
        int minArea = Integer.MAX_VALUE;
        int n = points.length;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                long keyA = ((long) x1 << 32) | (y2 & 0xffffffffL);
                long keyB = ((long) x2 << 32) | (y1 & 0xffffffffL);
                if (pointSet.contains(keyA) && pointSet.contains(keyB)) {
                    int area = Math.abs(x1 - x2) * Math.abs(y1 - y2);
                    if (area < minArea) minArea = area;
                }
            }
        }
        return minArea == Integer.MAX_VALUE ? 0 : minArea;
    }
}
```

## Python

```python
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        point_set = set(map(tuple, points))
        n = len(points)
        min_area = float('inf')
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        if area < min_area:
                            min_area = area
        return 0 if min_area == float('inf') else int(min_area)
```

## Python3

```python
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = { (x, y) for x, y in points }
        n = len(points)
        min_area = float('inf')
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        if area < min_area:
                            min_area = area
        return 0 if min_area == float('inf') else min_area
```

## C

```c
#include <stdlib.h>
#include <limits.h>

#define HASH_SIZE 200003

typedef struct Node {
    long long key;
    struct Node* next;
} Node;

static unsigned int hash_func(long long key) {
    return (unsigned int)((key ^ (key >> 32)) % HASH_SIZE);
}

static void insert(Node** table, long long key) {
    unsigned int idx = hash_func(key);
    Node* n = (Node*)malloc(sizeof(Node));
    n->key = key;
    n->next = table[idx];
    table[idx] = n;
}

static int exists(Node** table, long long key) {
    unsigned int idx = hash_func(key);
    for (Node* cur = table[idx]; cur; cur = cur->next) {
        if (cur->key == key) return 1;
    }
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int minAreaRect(int** points, int pointsSize, int* pointsColSize){
    Node* table[HASH_SIZE] = {0};
    for (int i = 0; i < pointsSize; ++i) {
        long long key = ((long long)points[i][0] << 32) | (unsigned int)points[i][1];
        insert(table, key);
    }

    int minArea = INT_MAX;
    for (int i = 0; i < pointsSize; ++i) {
        int x1 = points[i][0], y1 = points[i][1];
        for (int j = i + 1; j < pointsSize; ++j) {
            int x2 = points[j][0], y2 = points[j][1];
            if (x1 == x2 || y1 == y2) continue; // not diagonal
            long long keyA = ((long long)x1 << 32) | (unsigned int)y2;
            long long keyB = ((long long)x2 << 32) | (unsigned int)y1;
            if (exists(table, keyA) && exists(table, keyB)) {
                int area = abs(x1 - x2) * abs(y1 - y2);
                if (area < minArea) minArea = area;
            }
        }
    }

    // free hash table
    for (int i = 0; i < HASH_SIZE; ++i) {
        Node* cur = table[i];
        while (cur) {
            Node* nxt = cur->next;
            free(cur);
            cur = nxt;
        }
    }

    return (minArea == INT_MAX) ? 0 : minArea;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinAreaRect(int[][] points)
    {
        var pointSet = new HashSet<(int, int)>();
        foreach (var p in points)
            pointSet.Add((p[0], p[1]));

        int minArea = int.MaxValue;
        int n = points.Length;

        for (int i = 0; i < n; i++)
        {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++)
            {
                int x2 = points[j][0];
                int y2 = points[j][1];

                if (x1 == x2 || y1 == y2) continue;

                if (pointSet.Contains((x1, y2)) && pointSet.Contains((x2, y1)))
                {
                    int area = Math.Abs(x1 - x2) * Math.Abs(y1 - y2);
                    if (area < minArea) minArea = area;
                }
            }
        }

        return minArea == int.MaxValue ? 0 : minArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaRect = function(points) {
    const colMap = new Map(); // x -> array of y's
    for (const [x, y] of points) {
        if (!colMap.has(x)) colMap.set(x, []);
        colMap.get(x).push(y);
    }
    const xs = Array.from(colMap.keys()).sort((a, b) => a - b);
    // sort each column's y list
    for (const x of xs) {
        colMap.get(x).sort((a, b) => a - b);
    }

    const pairLastX = new Map(); // "y1,y2" -> last x where this pair appeared
    let minArea = Infinity;

    for (const x of xs) {
        const ys = colMap.get(x);
        const n = ys.length;
        for (let i = 0; i < n; ++i) {
            for (let j = i + 1; j < n; ++j) {
                const y1 = ys[i];
                const y2 = ys[j];
                const key = `${y1},${y2}`;
                if (pairLastX.has(key)) {
                    const prevX = pairLastX.get(key);
                    const area = (x - prevX) * (y2 - y1);
                    if (area < minArea) minArea = area;
                }
                // update to current x for future rectangles
                pairLastX.set(key, x);
            }
        }
    }

    return minArea === Infinity ? 0 : minArea;
};
```

## Typescript

```typescript
function minAreaRect(points: number[][]): number {
    const pointSet = new Set<string>();
    for (const [x, y] of points) {
        pointSet.add(`${x},${y}`);
    }
    let minArea = Infinity;
    const n = points.length;
    for (let i = 0; i < n; ++i) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n; ++j) {
            const [x2, y2] = points[j];
            if (x1 === x2 || y1 === y2) continue;
            if (pointSet.has(`${x1},${y2}`) && pointSet.has(`${x2},${y1}`)) {
                const area = Math.abs(x1 - x2) * Math.abs(y1 - y2);
                if (area < minArea) minArea = area;
            }
        }
    }
    return minArea === Infinity ? 0 : minArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minAreaRect($points) {
        usort($points, function ($a, $b) {
            if ($a[1] == $b[1]) {
                return $a[0] <=> $b[0];
            }
            return $a[1] <=> $b[1];
        });

        $map = []; // key "x1:x2" => previous y
        $minArea = PHP_INT_MAX;
        $n = count($points);
        $i = 0;

        while ($i < $n) {
            $y = $points[$i][1];
            $xs = [];

            while ($i < $n && $points[$i][1] == $y) {
                $xs[] = $points[$i][0];
                $i++;
            }

            sort($xs);
            $len = count($xs);

            for ($a = 0; $a < $len - 1; $a++) {
                for ($b = $a + 1; $b < $len; $b++) {
                    $key = $xs[$a] . ':' . $xs[$b];
                    if (isset($map[$key])) {
                        $area = ($xs[$b] - $xs[$a]) * ($y - $map[$key]);
                        if ($area < $minArea) {
                            $minArea = $area;
                        }
                    }
                    // store current y for this x-pair
                    $map[$key] = $y;
                }
            }
        }

        return $minArea === PHP_INT_MAX ? 0 : $minArea;
    }
}
```

## Swift

```swift
class Solution {
    func minAreaRect(_ points: [[Int]]) -> Int {
        let factor = 40001
        var pointSet = Set<Int>()
        for p in points {
            pointSet.insert(p[0] * factor + p[1])
        }
        let n = points.count
        var minArea = Int.max
        for i in 0..<n {
            let x1 = points[i][0]
            let y1 = points[i][1]
            for j in (i + 1)..<n {
                let x2 = points[j][0]
                let y2 = points[j][1]
                if x1 == x2 || y1 == y2 { continue }
                if pointSet.contains(x1 * factor + y2) && pointSet.contains(x2 * factor + y1) {
                    let area = abs(x1 - x2) * abs(y1 - y2)
                    if area < minArea {
                        minArea = area
                    }
                }
            }
        }
        return minArea == Int.max ? 0 : minArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAreaRect(points: Array<IntArray>): Int {
        val pointSet = HashSet<Long>()
        for (p in points) {
            val key = (p[0].toLong() shl 32) or (p[1].toLong() and 0xffffffffL)
            pointSet.add(key)
        }
        var minArea = Int.MAX_VALUE
        val n = points.size
        for (i in 0 until n) {
            val x1 = points[i][0]
            val y1 = points[i][1]
            for (j in i + 1 until n) {
                val x2 = points[j][0]
                val y2 = points[j][1]
                if (x1 == x2 || y1 == y2) continue
                val key3 = (x1.toLong() shl 32) or (y2.toLong() and 0xffffffffL)
                val key4 = (x2.toLong() shl 32) or (y1.toLong() and 0xffffffffL)
                if (pointSet.contains(key3) && pointSet.contains(key4)) {
                    val area = kotlin.math.abs(x1 - x2) * kotlin.math.abs(y1 - y2)
                    if (area < minArea) minArea = area
                }
            }
        }
        return if (minArea == Int.MAX_VALUE) 0 else minArea
    }
}
```

## Dart

```dart
class Solution {
  int minAreaRect(List<List<int>> points) {
    final Set<String> pointSet = {};
    for (var p in points) {
      pointSet.add('${p[0]}#${p[1]}');
    }
    int minArea = 0x7fffffff;
    int n = points.length;
    for (int i = 0; i < n; ++i) {
      int x1 = points[i][0];
      int y1 = points[i][1];
      for (int j = i + 1; j < n; ++j) {
        int x2 = points[j][0];
        int y2 = points[j][1];
        if (x1 == x2 || y1 == y2) continue;
        if (pointSet.contains('$x1#${y2}') && pointSet.contains('$x2#${y1}')) {
          int area = (x1 - x2).abs() * (y1 - y2).abs();
          if (area < minArea) minArea = area;
        }
      }
    }
    return minArea == 0x7fffffff ? 0 : minArea;
  }
}
```

## Golang

```go
func minAreaRect(points [][]int) int {
	type void struct{}
	const maxCoord = 40001
	pointSet := make(map[int]void, len(points))
	for _, p := range points {
		key := p[0]*maxCoord + p[1]
		pointSet[key] = void{}
	}
	minArea := int(^uint(0) >> 1) // MaxInt
	n := len(points)
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	for i := 0; i < n; i++ {
		x1, y1 := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]
			if x1 == x2 || y1 == y2 {
				continue
			}
			if _, ok1 := pointSet[x1*maxCoord+y2]; !ok1 {
				continue
			}
			if _, ok2 := pointSet[x2*maxCoord+y1]; !ok2 {
				continue
			}
			area := abs(x1-x2) * abs(y1-y2)
			if area < minArea {
				minArea = area
			}
		}
	}
	if minArea == int(^uint(0)>>1) {
		return 0
	}
	return minArea
}
```

## Ruby

```ruby
def min_area_rect(points)
  point_set = {}
  points.each { |x, y| point_set[[x, y]] = true }

  min_area = Float::INFINITY
  n = points.length

  (0...n).each do |i|
    x1, y1 = points[i]
    ((i + 1)...n).each do |j|
      x2, y2 = points[j]
      next if x1 == x2 || y1 == y2
      if point_set[[x1, y2]] && point_set[[x2, y1]]
        area = (x1 - x2).abs * (y1 - y2).abs
        min_area = area if area < min_area
      end
    end
  end

  min_area == Float::INFINITY ? 0 : min_area.to_i
end
```

## Scala

```scala
object Solution {
    def minAreaRect(points: Array[Array[Int]]): Int = {
        val pointSet = points.map(p => (p(0), p(1))).toSet
        var minArea = Int.MaxValue
        val n = points.length
        for (i <- 0 until n) {
            val x1 = points(i)(0)
            val y1 = points(i)(1)
            for (j <- i + 1 until n) {
                val x2 = points(j)(0)
                val y2 = points(j)(1)
                if (x1 != x2 && y1 != y2) {
                    if (pointSet.contains((x1, y2)) && pointSet.contains((x2, y1))) {
                        val area = math.abs(x1 - x2) * math.abs(y1 - y2)
                        if (area < minArea) minArea = area
                    }
                }
            }
        }
        if (minArea == Int.MaxValue) 0 else minArea
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_area_rect(points: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashSet;
        let mut point_set = HashSet::new();
        for p in &points {
            point_set.insert((p[0], p[1]));
        }
        let n = points.len();
        let mut min_area = i32::MAX;
        for i in 0..n {
            let (x1, y1) = (points[i][0], points[i][1]);
            for j in (i + 1)..n {
                let (x2, y2) = (points[j][0], points[j][1]);
                if x1 != x2 && y1 != y2 {
                    if point_set.contains(&(x1, y2)) && point_set.contains(&(x2, y1)) {
                        let area = (x1 - x2).abs() * (y1 - y2).abs();
                        if area < min_area {
                            min_area = area;
                        }
                    }
                }
            }
        }
        if min_area == i32::MAX { 0 } else { min_area }
    }
}
```

## Racket

```racket
(define/contract (min-area-rect points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length points))
         (point-hash (make-hash #:test equal?)))
    (for-each (lambda (pt) (hash-set! point-hash pt #t)) points)
    (let ((min-area #f))
      (for ([i (in-range n)])
        (define p1 (list-ref points i))
        (define x1 (first p1))
        (define y1 (second p1))
        (for ([j (in-range (+ i 1) n)])
          (define p2 (list-ref points j))
          (define x2 (first p2))
          (define y2 (second p2))
          (when (and (not (= x1 x2)) (not (= y1 y2)))
            (define p3 (list x1 y2))
            (define p4 (list x2 y1))
            (when (and (hash-has-key? point-hash p3)
                       (hash-has-key? point-hash p4))
              (define area (* (abs (- x1 x2)) (abs (- y1 y2))))
              (set! min-area (if (or (not min-area) (< area min-area)) area min-area)))))))
      (if min-area min-area 0))))
```

## Erlang

```erlang
-module(solution).
-export([min_area_rect/1]).

-spec min_area_rect(Points :: [[integer()]]) -> integer().
min_area_rect(Points) ->
    Set = maps:from_list([{ {X,Y}, true } || [X,Y] <- Points]),
    Tuples = [{X,Y} || [X,Y] <- Points],
    Min = find_min(Tuples, Set, infinity),
    case Min of
        infinity -> 0;
        _ -> Min
    end.

find_min([], _Set, Min) ->
    Min;
find_min([P|Rest], Set, Min) ->
    NewMin = check_pairs(P, Rest, Set, Min),
    find_min(Rest, Set, NewMin).

check_pairs(_P, [], _Set, Min) -> Min;
check_pairs({X1,Y1}=P1, [P2|Rest], Set, Min) ->
    {X2,Y2} = P2,
    case (X1 =/= X2) andalso (Y1 =/= Y2) of
        true ->
            if X1 < X2, Y1 < Y2 ->
                    case maps:is_key({X1,Y2}, Set) andalso maps:is_key({X2,Y1}, Set) of
                        true ->
                            Area = erlang:abs(X1 - X2) * erlang:abs(Y1 - Y2),
                            UpdatedMin = 
                                case Min of
                                    infinity -> Area;
                                    _ -> erlang:min(Min, Area)
                                end,
                            check_pairs(P1, Rest, Set, UpdatedMin);
                        false ->
                            check_pairs(P1, Rest, Set, Min)
                    end;
               true ->
                    check_pairs(P1, Rest, Set, Min)
            end;
        false ->
            check_pairs(P1, Rest, Set, Min)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_area_rect(points :: [[integer]]) :: integer
  def min_area_rect(points) do
    point_set = MapSet.new(Enum.map(points, fn [x, y] -> {x, y} end))
    pts = Enum.map(points, fn [x, y] -> {x, y} end)
    n = length(pts)

    min_area =
      0..(n - 2)
      |> Enum.reduce(nil, fn i, acc ->
        {xi, yi} = Enum.at(pts, i)

        (i + 1)..(n - 1)
        |> Enum.reduce(acc, fn j, inner_acc ->
          {xj, yj} = Enum.at(pts, j)

          if xi != xj && yi != yj do
            if MapSet.member?(point_set, {xi, yj}) && MapSet.member?(point_set, {xj, yi}) do
              area = abs(xi - xj) * abs(yi - yj)

              cond do
                inner_acc == nil -> area
                area < inner_acc -> area
                true -> inner_acc
              end
            else
              inner_acc
            end
          else
            inner_acc
          end
        end)
      end)

    case min_area do
      nil -> 0
      v -> v
    end
  end
end
```
