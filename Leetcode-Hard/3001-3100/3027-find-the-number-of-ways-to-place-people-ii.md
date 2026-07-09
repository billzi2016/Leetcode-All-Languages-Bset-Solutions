# 3027. Find the Number of Ways to Place People II

## Cpp

```cpp
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();
        vector<pair<long long,long long>> pts;
        pts.reserve(n);
        for (auto &p : points) pts.emplace_back(p[0], p[1]);
        sort(pts.begin(), pts.end(), [](const auto& a, const auto& b){
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second; // y descending for equal x
        });
        long long ans = 0;
        const long long NEG_INF = LLONG_MIN / 4;
        for (int i = 0; i < n; ++i) {
            multiset<long long> ms;
            long long yi = pts[i].second;
            for (int j = i + 1; j < n; ++j) {
                long long yj = pts[j].second;
                if (yi >= yj) {
                    // find maximum y in ms that is <= yi
                    auto it = ms.upper_bound(yi);
                    long long maxY = NEG_INF;
                    if (it != ms.begin()) {
                        --it;
                        maxY = *it;
                    }
                    if (maxY < yj) ++ans;
                }
                ms.insert(yj);
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfPairs(int[][] points) {
        // Sort by x ascending, then y descending
        java.util.Arrays.sort(points, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]); // descending y
        });
        int n = points.length;
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) {
            ys[i] = points[i][1];
        }
        long ans = 0;
        for (int i = 0; i < n - 1; i++) {
            int curMax = Integer.MIN_VALUE;
            for (int j = i + 1; j < n; j++) {
                if (ys[i] >= ys[j] && curMax < ys[j]) {
                    ans++;
                }
                if (ys[j] > curMax) curMax = ys[j];
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort by x asc, then y desc
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0
        import bisect
        for i in range(n):
            yi = points[i][1]
            interior_ys = []  # sorted list of y's between i and current j
            for j in range(i + 1, n):
                yj = points[j][1]
                if yi >= yj:
                    # check if any y in interior_ys lies within [yj, yi]
                    idx = bisect.bisect_left(interior_ys, yj)
                    if idx == len(interior_ys) or interior_ys[idx] > yi:
                        ans += 1
                # add current j's y to interior for future larger j
                bisect.insort(interior_ys, yj)
        return ans
```

## Python3

```python
class Solution:
    def numberOfPairs(self, points):
        # Sort by x ascending, tie by y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0
        INF = 10**18
        for i in range(n):
            yi = points[i][1]
            max_int = -INF
            min_int = INF
            for j in range(i + 1, n):
                # add the point just before j to interior stats if it is not i
                if j - 1 >= i + 1:
                    yprev = points[j - 1][1]
                    if yprev > max_int:
                        max_int = yprev
                    if yprev < min_int:
                        min_int = yprev
                xj, yj = points[j]
                if yi < yj:   # not a valid upper‑left / lower‑right orientation
                    continue
                # rectangle is empty iff interior points are all above or all below it
                if max_int < yj or min_int > yi:
                    ans += 1
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long x;
    long long y;
} Pt;

static int cmpPt(const void *a, const void *b) {
    const Pt *pa = (const Pt *)a;
    const Pt *pb = (const Pt *)b;
    if (pa->x < pb->x) return -1;
    if (pa->x > pb->x) return 1;
    // x equal, sort y descending
    if (pa->y > pb->y) return -1;
    if (pa->y < pb->y) return 1;
    return 0;
}

int numberOfPairs(int** points, int pointsSize, int* pointsColSize){
    int n = pointsSize;
    Pt *arr = (Pt *)malloc(sizeof(Pt) * n);
    for (int i = 0; i < n; ++i) {
        arr[i].x = points[i][0];
        arr[i].y = points[i][1];
    }
    qsort(arr, n, sizeof(Pt), cmpPt);

    int ans = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long curMax = LLONG_MIN;
        for (int j = i + 1; j < n; ++j) {
            if (arr[i].y >= arr[j].y && curMax < arr[j].y) {
                ans++;
            }
            if (arr[j].y > curMax) curMax = arr[j].y;
        }
    }

    free(arr);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfPairs(int[][] points) {
        int n = points.Length;
        System.Array.Sort(points, (a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            // y descending for equal x
            return b[1].CompareTo(a[1]);
        });
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) ys[i] = points[i][1];

        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            int curMax = int.MinValue;
            for (int j = i + 1; j < n; j++) {
                if (ys[i] >= ys[j] && curMax < ys[j]) ans++;
                if (ys[j] > curMax) curMax = ys[j];
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfPairs = function(points) {
    // sort by x asc, then y desc for tie
    points.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    const n = points.length;
    const ys = points.map(p => p[1]);

    // build logs
    const log = new Array(n + 1).fill(0);
    for (let i = 2; i <= n; i++) {
        log[i] = log[Math.floor(i / 2)] + 1;
    }
    const K = log[n] + 1;

    // Sparse tables for max and min
    const stMax = Array.from({ length: K }, () => new Array(n));
    const stMin = Array.from({ length: K }, () => new Array(n));

    for (let i = 0; i < n; i++) {
        stMax[0][i] = ys[i];
        stMin[0][i] = ys[i];
    }
    for (let k = 1; k < K; k++) {
        const len = 1 << k;
        const half = len >> 1;
        for (let i = 0; i + len <= n; i++) {
            stMax[k][i] = Math.max(stMax[k - 1][i], stMax[k - 1][i + half]);
            stMin[k][i] = Math.min(stMin[k - 1][i], stMin[k - 1][i + half]);
        }
    }

    const queryMax = (l, r) => {
        const len = r - l + 1;
        const k = log[len];
        return Math.max(stMax[k][l], stMax[k][r - (1 << k) + 1]);
    };
    const queryMin = (l, r) => {
        const len = r - l + 1;
        const k = log[len];
        return Math.min(stMin[k][l], stMin[k][r - (1 << k) + 1]);
    };

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (ys[i] < ys[j]) continue; // not upper-left / lower-right
            if (i + 1 > j - 1) {
                ans++; // no interior points
            } else {
                const maxMid = queryMax(i + 1, j - 1);
                const minMid = queryMin(i + 1, j - 1);
                if (maxMid < ys[j] || minMid > ys[i]) {
                    ans++;
                }
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfPairs(points: number[][]): number {
    // Sort by x ascending, tie by y descending
    points.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    const n = points.length;
    const ys: number[] = new Array(n);
    for (let i = 0; i < n; ++i) ys[i] = points[i][1];

    // Coordinate compression of y values
    const uniqY = Array.from(new Set(ys)).sort((a, b) => a - b);
    const yToIdx = new Map<number, number>();
    for (let i = 0; i < uniqY.length; ++i) {
        yToIdx.set(uniqY[i], i + 1); // 1‑based index for Fenwick
    }
    const m = uniqY.length;

    class Fenwick {
        n: number;
        bit: number[];
        constructor(n: number) {
            this.n = n;
            this.bit = new Array(n + 2).fill(0);
        }
        add(i: number, delta: number): void {
            for (; i <= this.n; i += i & -i) this.bit[i] += delta;
        }
        sum(i: number): number {
            let s = 0;
            for (; i > 0; i -= i & -i) s += this.bit[i];
            return s;
        }
        rangeSum(l: number, r: number): number {
            if (l > r) return 0;
            return this.sum(r) - this.sum(l - 1);
        }
    }

    let ans = 0;
    for (let i = 0; i < n - 1; ++i) {
        const fenwick = new Fenwick(m);
        const yiIdx = yToIdx.get(ys[i])!;
        for (let j = i + 1; j < n; ++j) {
            // Check if point i can be upper‑left of point j
            if (ys[i] >= ys[j]) {
                const yjIdx = yToIdx.get(ys[j])!;
                const low = Math.min(yjIdx, yiIdx);
                const high = Math.max(yjIdx, yiIdx);
                // interior points are those already added to fenwick
                if (fenwick.rangeSum(low, high) === 0) {
                    ++ans;
                }
            }
            // Add point j's y for future intervals
            fenwick.add(yToIdx.get(ys[j])!, 1);
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfPairs($points) {
        $n = count($points);
        usort($points, function($a, $b) {
            if ($a[0] == $b[0]) {
                // y descending when x equal
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });

        $count = 0;
        for ($i = 0; $i < $n; ++$i) {
            $yi = $points[$i][1];
            $maxY = PHP_INT_MIN; // maximum y among intermediate points that are <= yi
            for ($j = $i + 1; $j < $n; ++$j) {
                $yj = $points[$j][1];
                if ($yj <= $yi) {               // candidate lower‑right corner
                    if ($maxY < $yj) {
                        ++$count;               // no intermediate point inside/on the fence
                    }
                    if ($yj > $maxY) {
                        $maxY = $yj;            // become part of intermediate set for later j
                    }
                }
                // if $yj > $yi, it cannot be Bob and also does not affect $maxY
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ points: [[Int]]) -> Int {
        let sorted = points.sorted { (a, b) -> Bool in
            if a[0] != b[0] {
                return a[0] < b[0]
            } else {
                return a[1] > b[1]
            }
        }
        let n = sorted.count
        var ys = [Int]()
        ys.reserveCapacity(n)
        for p in sorted {
            ys.append(p[1])
        }
        var ans = 0
        for i in 0..<(n - 1) {
            var maxInterior = Int.min
            var minInterior = Int.max
            for j in (i + 1)..<n {
                // check upper-left / lower-right condition (x is already non‑decreasing)
                if ys[i] >= ys[j] {
                    let valid: Bool
                    if i + 1 == j { // no interior points
                        valid = true
                    } else {
                        if maxInterior < ys[j] || minInterior > ys[i] {
                            valid = true
                        } else {
                            valid = false
                        }
                    }
                    if valid {
                        ans += 1
                    }
                }
                // add current j as interior for next iteration
                let y = ys[j]
                if y > maxInterior { maxInterior = y }
                if y < minInterior { minInterior = y }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(points: Array<IntArray>): Int {
        val sorted = points.map { it[0] to it[1] }
            .sortedWith(compareBy<Pair<Int, Int>>({ it.first }).thenByDescending { it.second })
        val n = sorted.size
        val y = IntArray(n) { sorted[it].second }

        var ans = 0L
        for (i in 0 until n - 1) {
            var curMax = Int.MIN_VALUE
            for (j in i + 1 until n) {
                if (y[i] >= y[j] && curMax < y[j]) {
                    ans++
                }
                if (y[j] > curMax) curMax = y[j]
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPairs(List<List<int>> points) {
    // Sort by x ascending, then y descending
    points.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return b[1] - a[1];
    });

    int n = points.length;
    const int INF = 1 << 60; // sufficiently large
    int ans = 0;

    for (int i = 0; i < n - 1; ++i) {
      int yi = points[i][1];
      int curMax = -INF;
      int curMin = INF;
      for (int j = i + 1; j < n; ++j) {
        if (j > i + 1) {
          int yInterior = points[j - 1][1];
          if (yInterior > curMax) curMax = yInterior;
          if (yInterior < curMin) curMin = yInterior;
        }
        int yj = points[j][1];
        if (yi >= yj) {
          // rectangle is valid if no interior point lies within [yj, yi]
          if (curMax < yj || curMin > yi) {
            ans++;
          }
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func numberOfPairs(points [][]int) int {
	n := len(points)
	sort.Slice(points, func(i, j int) bool {
		if points[i][0] == points[j][0] {
			return points[i][1] > points[j][1]
		}
		return points[i][0] < points[j][0]
	})

	ans := 0
	for i := 0; i < n; i++ {
		yi := points[i][1]
		m := -1 << 60 // largest y <= yi seen between i and current j (exclusive)
		for j := i + 1; j < n; j++ {
			xj, yj := points[j][0], points[j][1]

			if points[i][0] <= xj && yi >= yj {
				if m < yj {
					ans++
				}
			}

			if yj <= yi && yj > m {
				m = yj
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def number_of_pairs(points)
  n = points.size
  # compress y-coordinates
  ys = points.map { |p| p[1] }.uniq.sort
  y_to_rank = {}
  ys.each_with_index { |y, i| y_to_rank[y] = i }

  # sort by x asc, then y desc
  sorted = points.sort_by { |x, y| [x, -y] }
  yrank = sorted.map { |_, y| y_to_rank[y] }

  ans = 0
  n.times do |i|
    interior = 0
    yi = yrank[i]
    (i + 1...n).each do |j|
      yj = yrank[j]
      if yi >= yj
        len = yi - yj + 1
        mask = ((1 << len) - 1) << yj
        ans += 1 if (interior & mask).zero?
      end
      interior |= (1 << yj)
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfPairs(points: Array[Array[Int]]): Int = {
        val pts = points.sortWith { (a, b) =>
            if (a(0) != b(0)) a(0) < b(0)
            else a(1) > b(1)
        }
        val n = pts.length
        var ans: Long = 0L
        for (i <- 0 until n) {
            var curMax = Int.MinValue
            val yi = pts(i)(1)
            var j = i + 1
            while (j < n) {
                val yj = pts(j)(1)
                if (yi >= yj && curMax < yj) ans += 1
                if (yj > curMax) curMax = yj
                j += 1
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_pairs(points: Vec<Vec<i32>>) -> i32 {
        let mut pts: Vec<(i32, i32)> = points.into_iter().map(|v| (v[0], v[1])).collect();
        // sort by x ascending, then y descending
        pts.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                b.1.cmp(&a.1)
            }
        });
        let n = pts.len();
        let mut ans: i64 = 0;
        for i in 0..n {
            let yi = pts[i].1;
            let mut max_y = std::i32::MIN; // maximum y among interior points that are <= yi
            for j in (i + 1)..n {
                let yj = pts[j].1;
                if yi >= yj && max_y < yj {
                    ans += 1;
                }
                if yj <= yi && yj > max_y {
                    max_y = yj;
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket
(provide number-of-pairs)

(define/contract (number-of-pairs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
          (sort points
                (lambda (p1 p2)
                  (let ([x1 (first p1)] [y1 (second p1)]
                        [x2 (first p2)] [y2 (second p2)])
                    (cond [(< x1 x2) #t]
                          [(> x1 x2) #f]
                          [else (> y1 y2)])))))
         (ys (map second sorted)))
    (let loop ((rest ys) (stack '()) (ans 0))
      (if (null? rest)
          ans
          (let* ((cur (car rest))
                 ;; pop while top < cur
                 (new-stack
                  (let rec ((stk stack))
                    (cond [(null? stk) '()]
                          [(< (car stk) cur) (rec (cdr stk))]
                          [else stk])))
                 (ans2 (if (null? new-stack) ans (+ ans 1)))
                 (stack2 (cons cur new-stack)))
            (loop (cdr rest) stack2 ans2))))))
```

## Erlang

```erlang
number_of_pairs(Points) ->
    Sorted = lists:sort(
        fun({X1,Y1},{X2,Y2}) ->
            case X1 < X2 of
                true -> true;
                false when X1 > X2 -> false;
                false -> Y1 > Y2
            end
        end,
        [{X,Y} || [X,Y] <- Points]),
    Ys = [Y || {_X,Y} <- Sorted],
    UniqueYs = lists:usort(Ys),
    CompMap = maps:from_list(lists:zip(UniqueYs, lists:seq(1, length(UniqueYs)))),
    M = length(UniqueYs),
    YArr = array:from_list(Ys),
    N = length(Ys),
    count_i(1, N, YArr, CompMap, M, 0).

count_i(I, N, _YArr, _CompMap, _M, Acc) when I > N-1 -> Acc;
count_i(I, N, YArr, CompMap, M, Acc) ->
    Yi = array:get(I, YArr),
    YiIdx = maps:get(Yi, CompMap),
    Bit0 = array:new(M + 2, {default, 0}),
    CountI = count_j(I + 1, N, YArr, CompMap, Yi, YiIdx, Bit0, M, 0),
    NewAcc = Acc + CountI,
    count_i(I + 1, N, YArr, CompMap, M, NewAcc).

count_j(J, N, _YArr, _CompMap, _Yi, _YiIdx, _Bit, _M, CountJ) when J > N -> CountJ;
count_j(J, N, YArr, CompMap, Yi, YiIdx, Bit, M, CountJ) ->
    Yj = array:get(J, YArr),
    YjIdx = maps:get(Yj, CompMap),
    NewCount =
        if Yi >= Yj ->
                Sum = range_query(YjIdx, YiIdx, Bit),
                if Sum == 0 -> CountJ + 1; true -> CountJ end;
           true -> CountJ
        end,
    Bit2 = bit_update(YjIdx, 1, M, Bit),
    count_j(J + 1, N, YArr, CompMap, Yi, YiIdx, Bit2, M, NewCount).

range_query(L, R, _Bit) when L > R -> 0;
range_query(L, R, Bit) ->
    query(R, Bit) - query(L - 1, Bit).

query(0, _Bit) -> 0;
query(Index, Bit) ->
    Val = array:get(Index, Bit),
    Index2 = Index - (Index band -Index),
    Val + query(Index2, Bit).

bit_update(Index, _Delta, Size, Bit) when Index > Size -> Bit;
bit_update(Index, Delta, Size, Bit) ->
    Old = array:get(Index, Bit),
    NewBit = array:set(Index, Old + Delta, Bit),
    Next = Index + (Index band -Index),
    bit_update(Next, Delta, Size, NewBit).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(points :: [[integer]]) :: integer
  def number_of_pairs(points) do
    # Sort by x ascending, and for equal x by y descending
    sorted =
      Enum.sort_by(points, fn [x, y] -> {x, -y} end)

    ys = sorted |> Enum.map(fn [_x, y] -> y end) |> List.to_tuple()
    n = tuple_size(ys)
    min_inf = -1_000_000_001

    0..(n - 2)
    |> Enum.reduce(0, fn i, acc ->
      yi = elem(ys, i)

      {cnt, _} =
        ((i + 1)..(n - 1))
        |> Enum.reduce({acc, min_inf}, fn j, {c, max_y} ->
          yj = elem(ys, j)

          c2 =
            if yj <= yi and max_y < yj do
              c + 1
            else
              c
            end

          max_y2 =
            if yj <= yi and yj > max_y do
              yj
            else
              max_y
            end

          {c2, max_y2}
        end)

      cnt
    end)
  end
end
```
