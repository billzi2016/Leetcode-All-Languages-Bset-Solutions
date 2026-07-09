# 0447. Number of Boomerangs

## Cpp

```cpp
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int n = points.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            unordered_map<int, int> cnt;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int d2 = dx * dx + dy * dy;
                ++cnt[d2];
            }
            for (auto& p : cnt) {
                int c = p.second;
                ans += 1LL * c * (c - 1);
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int n = points.length;
        int total = 0;
        for (int i = 0; i < n; i++) {
            java.util.HashMap<Integer, Integer> distCount = new java.util.HashMap<>();
            int xi = points[i][0];
            int yi = points[i][1];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int dx = xi - points[j][0];
                int dy = yi - points[j][1];
                int d2 = dx * dx + dy * dy;
                distCount.put(d2, distCount.getOrDefault(d2, 0) + 1);
            }
            for (int cnt : distCount.values()) {
                total += cnt * (cnt - 1);
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            cnt = {}
            xi, yi = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                dx = xi - points[j][0]
                dy = yi - points[j][1]
                d2 = dx * dx + dy * dy
                cnt[d2] = cnt.get(d2, 0) + 1
            for c in cnt.values():
                res += c * (c - 1)
        return res
```

## Python3

```python
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        total = 0
        for i in range(n):
            dist_count = {}
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                dx = xi - points[j][0]
                dy = yi - points[j][1]
                d = dx * dx + dy * dy
                cnt = dist_count.get(d, 0) + 1
                total += (cnt - 1) * 2  # each new point forms ordered pairs with previous ones
                dist_count[d] = cnt
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int numberOfBoomerangs(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize < 2) return 0;
    long total = 0;
    int *dists = (int *)malloc(sizeof(int) * (pointsSize - 1));
    for (int i = 0; i < pointsSize; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];
        int cnt = 0;
        for (int j = 0; j < pointsSize; ++j) {
            if (i == j) continue;
            int dx = xi - points[j][0];
            int dy = yi - points[j][1];
            dists[cnt++] = dx * dx + dy * dy;
        }
        qsort(dists, cnt, sizeof(int), cmp_int);
        for (int k = 0; k < cnt;) {
            int same = 1;
            while (k + same < cnt && dists[k + same] == dists[k]) ++same;
            total += (long)same * (same - 1);
            k += same;
        }
    }
    free(dists);
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfBoomerangs(int[][] points) {
        int n = points.Length;
        int total = 0;
        for (int i = 0; i < n; i++) {
            var distanceCount = new Dictionary<int, int>();
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int d2 = dx * dx + dy * dy;
                if (!distanceCount.TryGetValue(d2, out int cnt)) {
                    distanceCount[d2] = 1;
                } else {
                    distanceCount[d2] = cnt + 1;
                }
            }
            foreach (int cnt in distanceCount.Values) {
                total += cnt * (cnt - 1);
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfBoomerangs = function(points) {
    const n = points.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const distCount = new Map();
        const [xi, yi] = points[i];
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const dx = xi - points[j][0];
            const dy = yi - points[j][1];
            const d = dx * dx + dy * dy;
            distCount.set(d, (distCount.get(d) || 0) + 1);
        }
        for (const cnt of distCount.values()) {
            total += cnt * (cnt - 1);
        }
    }
    return total;
};
```

## Typescript

```typescript
function numberOfBoomerangs(points: number[][]): number {
    const n = points.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        const distCount = new Map<number, number>();
        const [xi, yi] = points[i];
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const dx = xi - points[j][0];
            const dy = yi - points[j][1];
            const d = dx * dx + dy * dy;
            distCount.set(d, (distCount.get(d) ?? 0) + 1);
        }
        for (const cnt of distCount.values()) {
            if (cnt > 1) total += cnt * (cnt - 1);
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfBoomerangs($points) {
        $n = count($points);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $distCount = [];
            $xi = $points[$i][0];
            $yi = $points[$i][1];
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $dx = $xi - $points[$j][0];
                $dy = $yi - $points[$j][1];
                $d2 = $dx * $dx + $dy * $dy;
                if (!isset($distCount[$d2])) {
                    $distCount[$d2] = 0;
                }
                $distCount[$d2]++;
            }
            foreach ($distCount as $cnt) {
                if ($cnt > 1) {
                    $ans += $cnt * ($cnt - 1);
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfBoomerangs(_ points: [[Int]]) -> Int {
        let n = points.count
        var result = 0
        for i in 0..<n {
            var distanceCount = [Int:Int]()
            let xi = points[i][0]
            let yi = points[i][1]
            for j in 0..<n where j != i {
                let dx = xi - points[j][0]
                let dy = yi - points[j][1]
                let d = dx * dx + dy * dy
                distanceCount[d, default: 0] += 1
            }
            for count in distanceCount.values {
                if count > 1 {
                    result += count * (count - 1)
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
    fun numberOfBoomerangs(points: Array<IntArray>): Int {
        var result = 0
        for (i in points.indices) {
            val countMap = HashMap<Int, Int>()
            val xi = points[i][0]
            val yi = points[i][1]
            for (j in points.indices) {
                if (i == j) continue
                val dx = xi - points[j][0]
                val dy = yi - points[j][1]
                val dist = dx * dx + dy * dy
                countMap[dist] = (countMap[dist] ?: 0) + 1
            }
            for (cnt in countMap.values) {
                if (cnt > 1) result += cnt * (cnt - 1)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int numberOfBoomerangs(List<List<int>> points) {
    int n = points.length;
    int result = 0;
    for (int i = 0; i < n; i++) {
      final Map<int, int> count = {};
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        int dx = points[i][0] - points[j][0];
        int dy = points[i][1] - points[j][1];
        int d = dx * dx + dy * dy;
        count[d] = (count[d] ?? 0) + 1;
      }
      count.forEach((_, v) {
        result += v * (v - 1);
      });
    }
    return result;
  }
}
```

## Golang

```go
func numberOfBoomerangs(points [][]int) int {
	n := len(points)
	total := 0
	for i := 0; i < n; i++ {
		distCount := make(map[int]int)
		xi, yi := points[i][0], points[i][1]
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			dx := xi - points[j][0]
			dy := yi - points[j][1]
			d2 := dx*dx + dy*dy
			distCount[d2]++
		}
		for _, c := range distCount {
			total += c * (c - 1)
		}
	}
	return total
}
```

## Ruby

```ruby
def number_of_boomerangs(points)
  n = points.length
  total = 0
  n.times do |i|
    counts = Hash.new(0)
    xi, yi = points[i]
    (0...n).each do |j|
      next if i == j
      xj, yj = points[j]
      d = (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj)
      counts[d] += 1
    end
    counts.each_value { |c| total += c * (c - 1) }
  end
  total
end
```

## Scala

```scala
object Solution {
    def numberOfBoomerangs(points: Array[Array[Int]]): Int = {
        var total = 0
        val n = points.length
        for (i <- 0 until n) {
            val freq = scala.collection.mutable.Map[Int, Int]()
            val xi = points(i)(0)
            val yi = points(i)(1)
            for (j <- 0 until n if j != i) {
                val dx = xi - points(j)(0)
                val dy = yi - points(j)(1)
                val d2 = dx * dx + dy * dy
                freq(d2) = freq.getOrElse(d2, 0) + 1
            }
            for ((_, cnt) <- freq) {
                total += cnt * (cnt - 1)
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_boomerangs(points: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashMap;
        let n = points.len();
        let mut result: i32 = 0;
        for i in 0..n {
            let (xi, yi) = (points[i][0] as i64, points[i][1] as i64);
            let mut cnt_map: HashMap<i64, i32> = HashMap::new();
            for j in 0..n {
                if i == j { continue; }
                let dx = xi - points[j][0] as i64;
                let dy = yi - points[j][1] as i64;
                let d = dx * dx + dy * dy;
                *cnt_map.entry(d).or_insert(0) += 1;
            }
            for &c in cnt_map.values() {
                if c > 1 {
                    result += c * (c - 1);
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (number-of-boomerangs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((total 0))
    (for ([i points])
      (define dist-count (make-hash))
      (for ([j points])
        (unless (equal? i j)
          (let* ((dx (- (first j) (first i)))
                 (dy (- (second j) (second i)))
                 (d (+ (* dx dx) (* dy dy))))
            (hash-update! dist-count d add1 0))))
      (for ([cnt (in-hash-values dist-count)])
        (set! total (+ total (* cnt (- cnt 1))))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([number_of_boomerangs/1]).

-spec number_of_boomerangs(Points :: [[integer()]]) -> integer().
number_of_boomerangs(Points) ->
    lists:foldl(fun(Pi, Acc) ->
        DistMap = build_dist_map(Pi, Points),
        Count = maps:fold(fun(_Dist, Cnt, Sum) -> Sum + Cnt * (Cnt - 1) end,
                          0, DistMap),
        Acc + Count
    end, 0, Points).

build_dist_map(PointI, Points) ->
    lists:foldl(fun(Pj, Map) ->
        if Pj =:= PointI ->
                Map;
           true ->
                D = dist_sq(PointI, Pj),
                maps:update_with(D,
                                 fun(Old) -> Old + 1 end,
                                 1,
                                 Map)
        end
    end, #{}, Points).

dist_sq([X1,Y1], [X2,Y2]) ->
    Dx = X1 - X2,
    Dy = Y1 - Y2,
    Dx*Dx + Dy*Dy.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_boomerangs(points :: [[integer]]) :: integer
  def number_of_boomerangs(points) do
    Enum.reduce(points, 0, fn i, acc ->
      freq =
        points
        |> Enum.filter(&(&1 != i))
        |> Enum.map(fn j -> dist2(i, j) end)
        |> Enum.reduce(%{}, fn d, m -> Map.update(m, d, 1, &(&1 + 1)) end)

      acc + Enum.reduce(freq, 0, fn {_d, c}, a -> a + c * (c - 1) end)
    end)
  end

  defp dist2([x1, y1], [x2, y2]) do
    dx = x1 - x2
    dy = y1 - y2
    dx * dx + dy * dy
  end
end
```
