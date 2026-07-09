# 2250. Count Number of Rectangles Containing Each Point

## Cpp

```cpp
class Solution {
public:
    vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
        const int MAX_H = 100;
        vector<vector<int>> byHeight(MAX_H + 1);
        for (const auto& rec : rectangles) {
            int l = rec[0], h = rec[1];
            byHeight[h].push_back(l);
        }
        for (int h = 1; h <= MAX_H; ++h) {
            sort(byHeight[h].begin(), byHeight[h].end());
        }
        vector<int> result;
        result.reserve(points.size());
        for (const auto& pt : points) {
            int x = pt[0], y = pt[1];
            long long cnt = 0;
            for (int h = y; h <= MAX_H; ++h) {
                const auto& vec = byHeight[h];
                if (!vec.empty()) {
                    auto it = lower_bound(vec.begin(), vec.end(), x);
                    cnt += vec.size() - (it - vec.begin());
                }
            }
            result.push_back((int)cnt);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] countRectangles(int[][] rectangles, int[][] points) {
        List<Integer>[] temp = new ArrayList[101];
        for (int[] rec : rectangles) {
            int l = rec[0];
            int h = rec[1];
            if (temp[h] == null) temp[h] = new ArrayList<>();
            temp[h].add(l);
        }

        int[][] lens = new int[101][];
        for (int h = 1; h <= 100; ++h) {
            if (temp[h] != null) {
                Collections.sort(temp[h]);
                int sz = temp[h].size();
                lens[h] = new int[sz];
                for (int i = 0; i < sz; ++i) {
                    lens[h][i] = temp[h].get(i);
                }
            } else {
                lens[h] = new int[0];
            }
        }

        int m = points.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; ++i) {
            int x = points[i][0];
            int y = points[i][1];
            int cnt = 0;
            for (int h = y; h <= 100; ++h) {
                int[] arr = lens[h];
                if (arr.length == 0) continue;
                int idx = lowerBound(arr, x);
                cnt += arr.length - idx;
            }
            ans[i] = cnt;
        }
        return ans;
    }

    private int lowerBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        # bucket lengths by height (heights are at most 100)
        buckets = [[] for _ in range(101)]  # index 0 unused
        for l, h in rectangles:
            buckets[h].append(l)

        # sort each bucket to enable binary search
        for lst in buckets:
            lst.sort()

        res = []
        for x, y in points:
            cnt = 0
            # consider all heights >= y
            for h in range(y, 101):
                arr = buckets[h]
                if not arr:
                    continue
                idx = bisect.bisect_left(arr, x)
                cnt += len(arr) - idx
            res.append(cnt)

        return res
```

## Python3

```python
class Solution:
    def countRectangles(self, rectangles, points):
        from bisect import bisect_left
        # bucket lengths by height (1..100)
        buckets = [[] for _ in range(101)]
        for l, h in rectangles:
            buckets[h].append(l)
        for h in range(101):
            if buckets[h]:
                buckets[h].sort()
        res = []
        for x, y in points:
            cnt = 0
            for h in range(y, 101):
                arr = buckets[h]
                if not arr:
                    continue
                idx = bisect_left(arr, x)
                cnt += len(arr) - idx
            res.append(cnt)
        return res
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize,
                     int** points, int pointsSize, int* pointsColSize, int* returnSize) {
    // heights are in range [1,100]
    const int MAX_H = 100;
    int cntHeight[MAX_H + 1] = {0};

    // First pass: count rectangles per height
    for (int i = 0; i < rectanglesSize; ++i) {
        int h = rectangles[i][1];
        cntHeight[h]++;
    }

    // Allocate arrays for each height
    int *lenArr[MAX_H + 1] = {NULL};
    for (int h = 1; h <= MAX_H; ++h) {
        if (cntHeight[h] > 0) {
            lenArr[h] = (int *)malloc(cntHeight[h] * sizeof(int));
        }
    }

    // Second pass: fill lengths
    int idx[MAX_H + 1] = {0};
    for (int i = 0; i < rectanglesSize; ++i) {
        int l = rectangles[i][0];
        int h = rectangles[i][1];
        lenArr[h][idx[h]++] = l;
    }

    // Sort each height's length array
    for (int h = 1; h <= MAX_H; ++h) {
        if (cntHeight[h] > 0) {
            qsort(lenArr[h], cntHeight[h], sizeof(int), cmp_int);
        }
    }

    // Prepare result array
    int *result = (int *)malloc(pointsSize * sizeof(int));
    *returnSize = pointsSize;

    // Process each point
    for (int i = 0; i < pointsSize; ++i) {
        int x = points[i][0];
        int y = points[i][1];
        int total = 0;
        for (int h = y; h <= MAX_H; ++h) {
            int n = cntHeight[h];
            if (n == 0) continue;
            int *arr = lenArr[h];
            // lower_bound for x
            int l = 0, r = n;
            while (l < r) {
                int m = (l + r) >> 1;
                if (arr[m] < x)
                    l = m + 1;
                else
                    r = m;
            }
            total += n - l;
        }
        result[i] = total;
    }

    // Free allocated length arrays
    for (int h = 1; h <= MAX_H; ++h) {
        if (lenArr[h]) free(lenArr[h]);
    }

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] CountRectangles(int[][] rectangles, int[][] points)
    {
        const int MAX_H = 100;
        var buckets = new List<int>[MAX_H + 1];
        for (int i = 0; i <= MAX_H; i++) buckets[i] = new List<int>();

        foreach (var rect in rectangles)
        {
            int l = rect[0];
            int h = rect[1];
            buckets[h].Add(l);
        }

        var sortedLengths = new int[MAX_H + 1][];
        for (int h = 0; h <= MAX_H; h++)
        {
            var list = buckets[h];
            if (list.Count > 0)
            {
                list.Sort();
                sortedLengths[h] = list.ToArray();
            }
            else
            {
                sortedLengths[h] = new int[0];
            }
        }

        int m = points.Length;
        var ans = new int[m];

        for (int i = 0; i < m; i++)
        {
            int x = points[i][0];
            int y = points[i][1];
            int cnt = 0;

            for (int h = y; h <= MAX_H; h++)
            {
                var arr = sortedLengths[h];
                if (arr.Length == 0) continue;

                int idx = System.Array.BinarySearch(arr, x);
                if (idx < 0)
                {
                    idx = ~idx;
                }
                else
                {
                    while (idx > 0 && arr[idx - 1] == x) idx--;
                }

                cnt += arr.Length - idx;
            }

            ans[i] = cnt;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangles
 * @param {number[][]} points
 * @return {number[]}
 */
var countRectangles = function(rectangles, points) {
    const MAX_H = 100;
    // bucket lengths by height
    const buckets = Array.from({length: MAX_H + 1}, () => []);
    for (const [len, h] of rectangles) {
        buckets[h].push(len);
    }
    // sort each bucket
    for (let h = 1; h <= MAX_H; ++h) {
        if (buckets[h].length > 0) {
            buckets[h].sort((a, b) => a - b);
        }
    }

    const lowerBound = (arr, target) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    };

    const ans = new Array(points.length);
    for (let i = 0; i < points.length; ++i) {
        const [x, y] = points[i];
        let cnt = 0;
        for (let h = y; h <= MAX_H; ++h) {
            const arr = buckets[h];
            if (arr.length === 0) continue;
            const idx = lowerBound(arr, x);
            cnt += arr.length - idx;
        }
        ans[i] = cnt;
    }
    return ans;
};
```

## Typescript

```typescript
function countRectangles(rectangles: number[][], points: number[][]): number[] {
    const buckets: number[][] = Array.from({ length: 101 }, () => []);
    for (const [len, h] of rectangles) {
        buckets[h].push(len);
    }
    for (let h = 1; h <= 100; h++) {
        if (buckets[h].length) buckets[h].sort((a, b) => a - b);
    }

    const result: number[] = [];
    for (const [x, y] of points) {
        let cnt = 0;
        for (let h = y; h <= 100; h++) {
            const arr = buckets[h];
            if (!arr.length) continue;
            // lower bound for x
            let lo = 0, hi = arr.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (arr[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            cnt += arr.length - lo;
        }
        result.push(cnt);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @param Integer[][] $points
     * @return Integer[]
     */
    function countRectangles($rectangles, $points) {
        // Bucket rectangle lengths by their height (1..100)
        $byHeight = array_fill(0, 101, []);
        foreach ($rectangles as $rec) {
            $l = $rec[0];
            $h = $rec[1];
            $byHeight[$h][] = $l;
        }
        // Sort each bucket for binary search
        for ($i = 1; $i <= 100; $i++) {
            if (!empty($byHeight[$i])) {
                sort($byHeight[$i]);
            }
        }

        $result = [];
        foreach ($points as $pt) {
            $x = $pt[0];
            $y = $pt[1];
            $cnt = 0;
            for ($h = $y; $h <= 100; $h++) {
                if (empty($byHeight[$h])) continue;
                $list = $byHeight[$h];
                $n = count($list);
                // lower bound: first index with value >= x
                $lo = 0;
                $hi = $n;
                while ($lo < $hi) {
                    $mid = intdiv($lo + $hi, 2);
                    if ($list[$mid] < $x) {
                        $lo = $mid + 1;
                    } else {
                        $hi = $mid;
                    }
                }
                $cnt += $n - $lo;
            }
            $result[] = $cnt;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countRectangles(_ rectangles: [[Int]], _ points: [[Int]]) -> [Int] {
        var groups = Array(repeating: [Int](), count: 101)
        for rect in rectangles {
            let l = rect[0]
            let h = rect[1]
            groups[h].append(l)
        }
        for i in 0...100 {
            if !groups[i].isEmpty {
                groups[i].sort()
            }
        }
        var result = [Int]()
        result.reserveCapacity(points.count)
        for pt in points {
            let x = pt[0]
            let y = pt[1]
            var cnt = 0
            if y <= 100 {
                var h = y
                while h <= 100 {
                    let arr = groups[h]
                    if !arr.isEmpty {
                        var lo = 0
                        var hi = arr.count
                        while lo < hi {
                            let mid = (lo + hi) >> 1
                            if arr[mid] < x {
                                lo = mid + 1
                            } else {
                                hi = mid
                            }
                        }
                        cnt += arr.count - lo
                    }
                    h += 1
                }
            }
            result.append(cnt)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countRectangles(rectangles: Array<IntArray>, points: Array<IntArray>): IntArray {
        val byHeight = Array(101) { mutableListOf<Int>() }
        for (rect in rectangles) {
            val l = rect[0]
            val h = rect[1]
            byHeight[h].add(l)
        }
        for (h in 1..100) {
            byHeight[h].sort()
        }

        val result = IntArray(points.size)
        for ((idx, p) in points.withIndex()) {
            val x = p[0]
            val y = p[1]
            var count = 0
            for (h in y..100) {
                val list = byHeight[h]
                if (list.isNotEmpty()) {
                    var lo = 0
                    var hi = list.size
                    while (lo < hi) {
                        val mid = (lo + hi) ushr 1
                        if (list[mid] >= x) {
                            hi = mid
                        } else {
                            lo = mid + 1
                        }
                    }
                    count += list.size - lo
                }
            }
            result[idx] = count
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> countRectangles(List<List<int>> rectangles, List<List<int>> points) {
    const int MAX_H = 100;
    List<List<int>> buckets = List.generate(MAX_H + 1, (_) => []);
    for (var rect in rectangles) {
      int l = rect[0];
      int h = rect[1];
      buckets[h].add(l);
    }
    for (int h = 1; h <= MAX_H; ++h) {
      buckets[h].sort();
    }

    List<int> ans = List.filled(points.length, 0);
    for (int i = 0; i < points.length; ++i) {
      int x = points[i][0];
      int y = points[i][1];
      int cnt = 0;
      for (int h = y; h <= MAX_H; ++h) {
        List<int> arr = buckets[h];
        if (arr.isEmpty) continue;
        int lo = 0, hi = arr.length;
        while (lo < hi) {
          int mid = (lo + hi) >> 1;
          if (arr[mid] < x) {
            lo = mid + 1;
          } else {
            hi = mid;
          }
        }
        cnt += arr.length - lo;
      }
      ans[i] = cnt;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func countRectangles(rectangles [][]int, points [][]int) []int {
	const maxH = 100
	groups := make([][]int, maxH+1)
	for _, rec := range rectangles {
		l, h := rec[0], rec[1]
		groups[h] = append(groups[h], l)
	}
	for i := 1; i <= maxH; i++ {
		sort.Ints(groups[i])
	}
	ans := make([]int, len(points))
	for i, p := range points {
		x, y := p[0], p[1]
		cnt := 0
		for h := y; h <= maxH; h++ {
			arr := groups[h]
			if len(arr) == 0 {
				continue
			}
			idx := sort.Search(len(arr), func(j int) bool { return arr[j] >= x })
			cnt += len(arr) - idx
		}
		ans[i] = cnt
	}
	return ans
}
```

## Ruby

```ruby
def count_rectangles(rectangles, points)
  buckets = Array.new(101) { [] }
  rectangles.each do |l, h|
    buckets[h] << l
  end
  (1..100).each { |h| buckets[h].sort! }

  result = []
  points.each do |x, y|
    cnt = 0
    (y..100).each do |h|
      arr = buckets[h]
      next if arr.empty?
      idx = arr.bsearch_index { |v| v >= x }
      cnt += arr.length - idx if idx
    end
    result << cnt
  end
  result
end
```

## Scala

```scala
object Solution {
    def countRectangles(rectangles: Array[Array[Int]], points: Array[Array[Int]]): Array[Int] = {
        val maxH = 100
        val tempLists = Array.fill(maxH + 1)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (rect <- rectangles) {
            val l = rect(0)
            val h = rect(1)
            tempLists(h).append(l)
        }
        val buckets = new Array[Array[Int]](maxH + 1)
        for (h <- 0 to maxH) {
            if (tempLists(h).nonEmpty) {
                buckets(h) = tempLists(h).sorted.toArray
            } else {
                buckets(h) = Array.empty[Int]
            }
        }

        def lowerBound(arr: Array[Int], target: Int): Int = {
            var l = 0
            var r = arr.length
            while (l < r) {
                val m = (l + r) >>> 1
                if (arr(m) >= target) r = m else l = m + 1
            }
            l
        }

        val res = new Array[Int](points.length)
        var i = 0
        while (i < points.length) {
            val x = points(i)(0)
            val y = points(i)(1)
            var cnt = 0
            var h = y
            while (h <= maxH) {
                val arr = buckets(h)
                if (arr.nonEmpty) {
                    val pos = lowerBound(arr, x)
                    cnt += arr.length - pos
                }
                h += 1
            }
            res(i) = cnt
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_rectangles(rectangles: Vec<Vec<i32>>, points: Vec<Vec<i32>>) -> Vec<i32> {
        // rectangles grouped by height (1..=100)
        let mut by_h: Vec<Vec<i32>> = vec![Vec::new(); 101];
        for rect in rectangles.iter() {
            let l = rect[0];
            let h = rect[1] as usize;
            by_h[h].push(l);
        }
        // sort lengths for each height to enable binary search
        for v in by_h.iter_mut() {
            v.sort_unstable();
        }

        let mut ans: Vec<i32> = Vec::with_capacity(points.len());
        for pt in points.iter() {
            let x = pt[0];
            let y = pt[1] as usize;
            let mut cnt = 0i32;
            // any rectangle with height >= y can contain the point
            for h in y..=100 {
                let arr = &by_h[h];
                if !arr.is_empty() {
                    // lower bound: first index where length >= x
                    let pos = arr.partition_point(|&v| v < x);
                    cnt += (arr.len() - pos) as i32;
                }
            }
            ans.push(cnt);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-rectangles rectangles points)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((max-h 100)
         (height-lists (make-vector (+ max-h 1) '())))

    ;; collect lengths per height
    (for-each (lambda (rc)
                (let ((l (first rc))
                      (h (second rc)))
                  (vector-set! height-lists h
                               (cons l (vector-ref height-lists h)))))
              rectangles)

    ;; sort each list and turn into vectors for binary search
    (define height-vecs
      (for/vector ([h (in-range 0 (+ max-h 1))])
        (let ((lst (vector-ref height-lists h)))
          (if (null? lst)
              #()
              (list->vector (sort lst <))))))

    ;; lower‑bound binary search: first index with value >= target
    (define (lower-bound vec target)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (< (vector-ref vec mid) target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))

    ;; count rectangles containing a single point
    (define (count-for-point pt)
      (let* ((x (first pt))
             (y (second pt)))
        (let loop ((h y) (acc 0))
          (if (> h max-h)
              acc
              (let ((vec (vector-ref height-vecs h)))
                (if (= (vector-length vec) 0)
                    (loop (+ h 1) acc)
                    (let ((idx (lower-bound vec x)))
                      (loop (+ h 1)
                            (+ acc (- (vector-length vec) idx))))))))))

    ;; produce result list in the order of points
    (for/list ([pt points]) (count-for-point pt))))
```

## Erlang

```erlang
-module(solution).
-export([count_rectangles/2]).

-spec count_rectangles(Rectangles :: [[integer()]], Points :: [[integer()]]) -> [integer()].
count_rectangles(Rectangles, Points) ->
    HeightMap0 = build_height_map(Rectangles, #{}),
    HeightMap = maps:fold(
        fun(H, Ls, Acc) ->
            Sorted = lists:sort(Ls),
            Tuple = list_to_tuple(Sorted),
            maps:put(H, Tuple, Acc)
        end,
        #{},
        HeightMap0
    ),
    [process_point(Point, HeightMap) || Point <- Points].

build_height_map([], Map) -> Map;
build_height_map([[L, H] | Rest], Map) ->
    Updated = maps:update_with(
        H,
        fun(Ls) -> [L | Ls] end,
        [L],
        Map
    ),
    build_height_map(Rest, Updated).

process_point([X, Y], HeightMap) ->
    count_for_heights(Y, 100, X, HeightMap, 0).

count_for_heights(Current, Max, _X, _HeightMap, Acc) when Current > Max -> Acc;
count_for_heights(Current, Max, X, HeightMap, Acc) ->
    Tuple = maps:get(Current, HeightMap, {}),
    Count = count_ge(Tuple, X),
    count_for_heights(Current + 1, Max, X, HeightMap, Acc + Count).

count_ge({}, _X) -> 0;
count_ge(Tuple, X) ->
    N = tuple_size(Tuple),
    case N of
        0 -> 0;
        _ ->
            Pos = lower_bound(Tuple, 1, N + 1, X),
            N - Pos + 1
    end.

lower_bound(_Tuple, Low, High, _X) when Low >= High -> Low;
lower_bound(Tuple, Low, High, X) ->
    Mid = (Low + High) div 2,
    Val = element(Tuple, Mid),
    if
        Val >= X -> lower_bound(Tuple, Low, Mid, X);
        true     -> lower_bound(Tuple, Mid + 1, High, X)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_rectangles(rectangles :: [[integer]], points :: [[integer]]) :: [integer]
  def count_rectangles(rectangles, points) do
    # Bucket rectangle lengths by their height
    buckets =
      Enum.reduce(rectangles, %{}, fn [len, h], acc ->
        Map.update(acc, h, [len], &[len | &1])
      end)

    # For each possible height (1..100), create a sorted array of lengths
    height_arrays =
      Enum.reduce(1..100, %{}, fn h, acc ->
        list = Map.get(buckets, h, [])
        if list == [] do
          acc
        else
          arr = :array.from_list(Enum.sort(list))
          Map.put(acc, h, arr)
        end
      end)

    # Process each point
    Enum.map(points, fn [x, y] ->
      y..100
      |> Enum.reduce(0, fn h, sum ->
        case Map.get(height_arrays, h) do
          nil -> sum
          arr ->
            idx = lower_bound(arr, x)
            cnt = :array.size(arr) - idx
            sum + cnt
        end
      end)
    end)
  end

  # Binary search: first index with value >= target
  defp lower_bound(arr, target), do: lower_bound(arr, target, 0, :array.size(arr))

  defp lower_bound(_arr, _target, low, high) when low >= high, do: low

  defp lower_bound(arr, target, low, high) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val < target do
      lower_bound(arr, target, mid + 1, high)
    else
      lower_bound(arr, target, low, mid)
    end
  end
end
```
