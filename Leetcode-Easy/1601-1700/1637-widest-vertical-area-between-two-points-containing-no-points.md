# 1637. Widest Vertical Area Between Two Points Containing No Points

## Cpp

```cpp
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0] < b[0]; });
        int ans = 0;
        for (size_t i = 1; i < points.size(); ++i) {
            ans = max(ans, points[i][0] - points[i-1][0]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[0]));
        int ans = 0;
        for (int i = 1; i < points.length; i++) {
            ans = Math.max(ans, points[i][0] - points[i - 1][0]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort points by x-coordinate
        points.sort(key=lambda p: p[0])
        max_width = 0
        prev_x = points[0][0]
        for i in range(1, len(points)):
            cur_x = points[i][0]
            diff = cur_x - prev_x
            if diff > max_width:
                max_width = diff
            prev_x = cur_x
        return max_width
```

## Python3

```python
class Solution:
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda p: p[0])
        ans = 0
        for i in range(1, len(points)):
            ans = max(ans, points[i][0] - points[i-1][0])
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int maxWidthOfVerticalArea(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize < 2) return 0;
    int *xs = (int *)malloc(pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; ++i) {
        xs[i] = points[i][0];
    }
    qsort(xs, pointsSize, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 1; i < pointsSize; ++i) {
        int diff = xs[i] - xs[i - 1];
        if (diff > ans) ans = diff;
    }
    free(xs);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxWidthOfVerticalArea(int[][] points) {
        System.Array.Sort(points, (a, b) => a[0].CompareTo(b[0]));
        int max = 0;
        for (int i = 1; i < points.Length; i++) {
            int diff = points[i][0] - points[i - 1][0];
            if (diff > max) max = diff;
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    points.sort((a, b) => a[0] - b[0]);
    let maxWidth = 0;
    for (let i = 1; i < points.length; i++) {
        const width = points[i][0] - points[i - 1][0];
        if (width > maxWidth) maxWidth = width;
    }
    return maxWidth;
};
```

## Typescript

```typescript
function maxWidthOfVerticalArea(points: number[][]): number {
    points.sort((a, b) => a[0] - b[0]);
    let ans = 0;
    for (let i = 1; i < points.length; i++) {
        const diff = points[i][0] - points[i - 1][0];
        if (diff > ans) ans = diff;
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
    function maxWidthOfVerticalArea($points) {
        $xs = [];
        foreach ($points as $p) {
            $xs[] = $p[0];
        }
        sort($xs, SORT_NUMERIC);
        $ans = 0;
        $n = count($xs);
        for ($i = 1; $i < $n; $i++) {
            $diff = $xs[$i] - $xs[$i - 1];
            if ($diff > $ans) {
                $ans = $diff;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxWidthOfVerticalArea(_ points: [[Int]]) -> Int {
        var xs = [Int]()
        xs.reserveCapacity(points.count)
        for p in points {
            xs.append(p[0])
        }
        xs.sort()
        var ans = 0
        for i in 1..<xs.count {
            let diff = xs[i] - xs[i - 1]
            if diff > ans { ans = diff }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxWidthOfVerticalArea(points: Array<IntArray>): Int {
        val xs = IntArray(points.size)
        for (i in points.indices) {
            xs[i] = points[i][0]
        }
        xs.sort()
        var ans = 0
        for (i in 1 until xs.size) {
            val diff = xs[i] - xs[i - 1]
            if (diff > ans) ans = diff
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxWidthOfVerticalArea(List<List<int>> points) {
    List<int> xs = points.map((p) => p[0]).toList();
    xs.sort();
    int ans = 0;
    for (int i = 1; i < xs.length; ++i) {
      int diff = xs[i] - xs[i - 1];
      if (diff > ans) ans = diff;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxWidthOfVerticalArea(points [][]int) int {
	xs := make([]int, len(points))
	for i, p := range points {
		xs[i] = p[0]
	}
	sort.Ints(xs)
	maxGap := 0
	for i := 1; i < len(xs); i++ {
		if diff := xs[i] - xs[i-1]; diff > maxGap {
			maxGap = diff
		}
	}
	return maxGap
}
```

## Ruby

```ruby
def max_width_of_vertical_area(points)
  points.sort_by! { |p| p[0] }
  max_gap = 0
  (1...points.size).each do |i|
    gap = points[i][0] - points[i - 1][0]
    max_gap = gap if gap > max_gap
  end
  max_gap
end
```

## Scala

```scala
object Solution {
    def maxWidthOfVerticalArea(points: Array[Array[Int]]): Int = {
        val xs = points.map(_(0)).sorted
        var maxDiff = 0
        var i = 1
        while (i < xs.length) {
            val diff = xs(i) - xs(i - 1)
            if (diff > maxDiff) maxDiff = diff
            i += 1
        }
        maxDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut xs: Vec<i32> = points.into_iter().map(|p| p[0]).collect();
        xs.sort_unstable();
        let mut ans = 0;
        for i in 1..xs.len() {
            let diff = xs[i] - xs[i - 1];
            if diff > ans {
                ans = diff;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-width-of-vertical-area points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([xs (map first points)]
         [sorted-xs (sort xs <)])
    (if (< (length sorted-xs) 2)
        0
        (let loop ((prev (first sorted-xs))
                   (rest (rest sorted-xs))
                   (max-diff 0))
          (if (null? rest)
              max-diff
              (let* ([curr (first rest)]
                     [diff (- curr prev)])
                (loop curr (rest rest) (max max-diff diff))))))))
```

## Erlang

```erlang
-spec max_width_of_vertical_area(Points :: [[integer()]]) -> integer().
max_width_of_vertical_area(Points) ->
    Xs = [X || [X,_] <- Points],
    Sorted = lists:sort(Xs),
    max_width(Sorted, 0).

max_width([_], Max) -> Max;
max_width([A,B|Rest], Max) ->
    Diff = B - A,
    NewMax = if Diff > Max -> Diff; true -> Max end,
    max_width([B|Rest], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_width_of_vertical_area(points :: [[integer]]) :: integer
  def max_width_of_vertical_area(points) do
    xs =
      points
      |> Enum.map(fn [x, _y] -> x end)
      |> Enum.sort()

    [first | rest] = xs

    {_last, max_diff} =
      Enum.reduce(rest, {first, 0}, fn x, {prev, current_max} ->
        diff = x - prev
        new_max = if diff > current_max, do: diff, else: current_max
        {x, new_max}
      end)

    max_diff
  end
end
```
