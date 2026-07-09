# 0757. Set Intersection Size At Least Two

## Cpp

```cpp
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [](const vector<int>& a, const vector<int>& b) {
                if (a[1] == b[1]) return a[0] > b[0];
                return a[1] < b[1];
            });
        int ans = 0;
        int p1 = -1, p2 = -1; // two largest selected numbers
        for (const auto& iv : intervals) {
            int l = iv[0], r = iv[1];
            if (l > p2) {
                // need two new points
                p1 = r - 1;
                p2 = r;
                ans += 2;
            } else if (l > p1) {
                // need one new point
                int newPoint = (r == p2) ? r - 1 : r;
                p1 = p2;
                p2 = newPoint;
                ++ans;
            }
            // else both points already inside the interval
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        java.util.Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(b[0], a[0]); // start descending when ends equal
        });
        int ans = 0;
        int x = -1; // smaller of the two largest selected numbers
        int y = -1; // larger of the two largest selected numbers
        for (int[] inter : intervals) {
            int l = inter[0];
            int r = inter[1];
            if (l > y) {                 // neither x nor y is inside the interval
                ans += 2;
                x = r - 1;
                y = r;
            } else if (l > x) {          // only y is inside the interval
                ans += 1;
                if (r != y) {
                    x = y;
                    y = r;
                } else {
                    // need a distinct number, pick r-1
                    x = y - 1;
                    // y remains unchanged
                }
            }
            // else both x and y are already inside; nothing to do
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by end ascending, start descending for tie-breaking
        intervals.sort(key=lambda x: (x[1], -x[0]))
        selected = []
        for l, r in intervals:
            cnt = 0
            if len(selected) > 0 and selected[-1] >= l:
                cnt += 1
            if len(selected) > 1 and selected[-2] >= l:
                cnt += 1

            if cnt == 2:
                continue
            elif cnt == 1:
                # Need one more point, choose the farthest possible (r)
                new_point = r
                if new_point == selected[-1]:
                    new_point = r - 1
                selected.append(new_point)
            else:  # cnt == 0
                # Need two points, pick r-1 and r
                selected.append(r - 1)
                selected.append(r)

        return len(selected)
```

## Python3

```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending; if tie, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = 0
        # a and b are the two largest selected numbers so far
        a, b = -1, -1
        for l, r in intervals:
            if a >= l:
                # both a and b lie inside current interval
                continue
            if b >= l:
                # only b lies inside; need one more number
                ans += 1
                a = b
                b = r
            else:
                # none lie inside; need two numbers
                ans += 2
                a = r - 1
                b = r
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *i = (const Interval *)a;
    const Interval *j = (const Interval *)b;
    if (i->end != j->end)
        return i->end - j->end;          // ascending end
    return j->start - i->start;          // descending start when ends equal
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    if (intervalsSize == 0) return 0;
    
    Interval *arr = (Interval *)malloc(sizeof(Interval) * intervalsSize);
    for (int i = 0; i < intervalsSize; ++i) {
        arr[i].start = intervals[i][0];
        arr[i].end   = intervals[i][1];
    }
    
    qsort(arr, intervalsSize, sizeof(Interval), cmpInterval);
    
    int ans = 0;
    int a = -1000000000; // smallest of the last two selected numbers
    int b = -1000000000; // largest of the last two selected numbers
    
    for (int i = 0; i < intervalsSize; ++i) {
        int l = arr[i].start;
        int r = arr[i].end;
        
        if (l > b) {                     // need two new points
            ans += 2;
            b = r;
            a = r - 1;
        } else if (l > a) {              // need one new point
            ans += 1;
            int newPoint = (r == b) ? r - 1 : r;
            a = b;
            b = newPoint;
        }
        // else: interval already contains both a and b, nothing to do
    }
    
    free(arr);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        System.Array.Sort(intervals, (x, y) => {
            if (x[1] != y[1]) return x[1].CompareTo(y[1]);
            // for same end, larger start first
            return y[0].CompareTo(x[0]);
        });

        int ans = 0;
        int a = -1; // second largest selected number
        int b = -1; // largest selected number

        foreach (var inter in intervals) {
            int l = inter[0];
            int r = inter[1];

            if (l > b) {
                // need two new points
                ans += 2;
                a = r - 1;
                b = r;
            } else if (l > a) {
                // need one new point
                ans += 1;
                int newPoint = (r == b) ? r - 1 : r;
                a = b;
                b = newPoint;
            }
            // else both a and b already lie in the interval
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return b[0] - a[0];
    });
    let first = -1; // second last selected point
    let second = -1; // last selected point
    let ans = 0;
    for (const [l, r] of intervals) {
        if (l > second) {                 // no points inside interval
            first = r - 1;
            second = r;
            ans += 2;
        } else if (l > first) {           // exactly one point inside interval
            if (r === second) {
                // need a different point, pick r-1
                first = r - 1;
            } else {
                // add the farthest possible point r
                first = second;
                second = r;
            }
            ans += 1;
        }
        // else: both points already inside interval, nothing to do
    }
    return ans;
};
```

## Typescript

```typescript
function intersectionSizeTwo(intervals: number[][]): number {
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return b[0] - a[0];
    });
    let ans = 0;
    let first = -Infinity; // second largest selected number
    let second = -Infinity; // largest selected number
    for (const [l, r] of intervals) {
        let cnt = 0;
        if (first >= l) cnt++;
        if (second >= l) cnt++;
        if (cnt === 2) continue;
        if (cnt === 1) {
            ans += 1;
            // add the largest possible number not already selected
            if (second === r) {
                first = second - 1;
                second = r;
            } else {
                first = second;
                second = r;
            }
        } else { // cnt === 0
            ans += 2;
            first = r - 1;
            second = r;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function intersectionSizeTwo($intervals) {
        usort($intervals, function($a, $b) {
            if ($a[1] == $b[1]) {
                return $b[0] <=> $a[0];
            }
            return $a[1] <=> $b[1];
        });

        $ans = 0;
        $p1 = -1; // second largest selected number
        $p2 = -1; // largest selected number

        foreach ($intervals as $int) {
            $l = $int[0];
            $r = $int[1];

            if ($l > $p2) {                 // need two new points
                $ans += 2;
                $p1 = $r - 1;
                $p2 = $r;
            } elseif ($l > $p1) {           // need one new point
                $ans += 1;
                $p1 = $p2;
                if ($r == $p2) {
                    $p2 = $r - 1;          // avoid duplicate
                } else {
                    $p2 = $r;
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
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted { (i1, i2) -> Bool in
            if i1[1] == i2[1] {
                return i1[0] > i2[0]
            }
            return i1[1] < i2[1]
        }
        
        var a = -1   // second last selected number
        var b = -1   // last selected number, a < b
        var ans = 0
        
        for interval in sorted {
            let l = interval[0]
            let r = interval[1]
            
            if l > b {
                // No numbers from current set are inside the interval
                a = r - 1
                b = r
                ans += 2
            } else if l > a {
                // Exactly one number (b) is inside the interval
                a = b
                b = r
                ans += 1
            }
            // else: both a and b are already inside, nothing to add
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        val sorted = intervals.sortedWith { a, b ->
            if (a[1] != b[1]) a[1] - b[1] else b[0] - a[0]
        }
        var ans = 0
        var first = -1
        var second = -1
        for (intv in sorted) {
            val l = intv[0]
            val r = intv[1]
            if (l > second) {
                // need two new points
                first = r - 1
                second = r
                ans += 2
            } else if (l > first) {
                // need one more point
                val newPoint = if (second == r) r - 1 else r
                first = second
                second = newPoint
                ans += 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int intersectionSizeTwo(List<List<int>> intervals) {
    intervals.sort((a, b) {
      if (a[1] != b[1]) return a[1] - b[1];
      return b[0] - a[0];
    });
    int ans = 0;
    int first = -1, second = -1;
    for (var inter in intervals) {
      int l = inter[0];
      int r = inter[1];
      if (l > second) {
        ans += 2;
        first = r - 1;
        second = r;
      } else if (l > first) {
        ans += 1;
        int newPoint = (second == r) ? r - 1 : r;
        first = second;
        second = newPoint;
      }
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func intersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] > intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})
	a := intervals[0][1] - 1
	b := intervals[0][1]
	ans := 2
	for i := 1; i < len(intervals); i++ {
		l, r := intervals[i][0], intervals[i][1]
		if l <= a {
			continue
		} else if l <= b {
			ans++
			a = b
			b = r
		} else {
			ans += 2
			a = r - 1
			b = r
		}
	}
	return ans
}
```

## Ruby

```ruby
def intersection_size_two(intervals)
  intervals.sort_by! { |a| [a[1], -a[0]] }
  p1 = -Float::INFINITY
  p2 = -Float::INFINITY
  ans = 0

  intervals.each do |l, r|
    if l > p2
      # need two new points
      p1 = r - 1
      p2 = r
      ans += 2
    elsif l > p1
      # need one new point
      new_point = (r == p2) ? r - 1 : r
      p1 = p2
      p2 = new_point
      ans += 1
    end
    # else: already have at least two points in the interval
  end

  ans
end
```

## Scala

```scala
object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        if (intervals.isEmpty) return 0
        val sorted = intervals.sortWith { (a, b) =>
            if (a(1) != b(1)) a(1) < b(1)
            else a(0) > b(0)
        }
        var ans = 2
        var x = sorted(0)(1) - 1
        var y = sorted(0)(1)

        for (i <- 1 until sorted.length) {
            val l = sorted(i)(0)
            val r = sorted(i)(1)
            if (l <= x) {
                // already have two points in this interval
            } else if (l > y) {
                ans += 2
                x = r - 1
                y = r
            } else { // l > x && l <= y
                ans += 1
                x = y
                if (r == y) y = r - 1 else y = r
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        // Sort by end ascending, and for equal ends sort start descending
        intervals.sort_by(|a, b| {
            if a[1] != b[1] {
                a[1].cmp(&b[1])
            } else {
                b[0].cmp(&a[0])
            }
        });

        let mut res = 0;
        // Initialize with values smaller than any possible start (starts are >= 0)
        let mut p1: i32 = -1_000_000_001;
        let mut p2: i32 = -1_000_000_001;

        for intv in intervals.iter() {
            let l = intv[0];
            let r = intv[1];

            if l > p1 {
                // Need two new points
                p1 = r - 1;
                p2 = r;
                res += 2;
            } else if l > p2 {
                // Need one new point
                p1 = p2;
                p2 = r;
                res += 1;
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (intersection-size-two intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
          (sort intervals
                (lambda (a b)
                  (let ((end-a (cadr a))
                        (end-b (cadr b)))
                    (if (< end-a end-b)
                        #t
                        (if (> end-a end-b)
                            #f
                            (> (car a) (car b))))))))
         (process
          (letrec ((proc (lambda (lst s1 s2 ans)
                           (if (null? lst)
                               ans
                               (let* ((l (car (car lst)))
                                      (r (cadr (car lst)))
                                      (cnt (+ (if (>= s1 l) 1 0)
                                              (if (>= s2 l) 1 0))))
                                 (cond
                                   [(= cnt 2) (proc (cdr lst) s1 s2 ans)]
                                   [(= cnt 1)
                                    (let ((new (if (= r s2) (- r 1) r)))
                                      (proc (cdr lst) s2 new (+ ans 1)))]
                                   [else
                                    (let ((new1 (- r 1))
                                          (new2 r))
                                      (proc (cdr lst) new1 new2 (+ ans 2)))])))))
            proc))
         )
    (process sorted -inf.0 -inf.0 0)))
```

## Erlang

```erlang
-module(solution).
-export([intersection_size_two/1]).

-spec intersection_size_two(Intervals :: [[integer()]]) -> integer().
intersection_size_two(Intervals) ->
    Sorted = lists:sort(fun compare/2, Intervals),
    {Count,_P1,_P2} = lists:foldl(fun process_interval/2, {0, -1, -1}, Sorted),
    Count.

compare([L1,R1], [L2,R2]) ->
    if
        R1 < R2 -> true;
        R1 > R2 -> false;
        true    -> L1 > L2
    end.

process_interval([L,R], {Count, P1, P2}) ->
    case L > P2 of
        true ->
            NewP1 = R - 1,
            NewP2 = R,
            {Count + 2, NewP1, NewP2};
        false ->
            case L > P1 of
                true ->
                    NewPoint = if R == P2 -> R - 1; true -> R end,
                    {Count + 1, P2, NewPoint};
                false ->
                    {Count, P1, P2}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec intersection_size_two(intervals :: [[integer]]) :: integer
  def intersection_size_two(intervals) do
    sorted =
      intervals
      |> Enum.map(fn [l, r] -> {l, r} end)
      |> Enum.sort(fn {l1, r1}, {l2, r2} ->
        if r1 != r2 do
          r1 < r2
        else
          l1 > l2
        end
      end)

    {_a, _b, ans} =
      Enum.reduce(sorted, {-1_000_000_000, -1_000_000_000, 0}, fn {l, r},
                                                               {a, b, cnt} ->
        cond do
          l <= a and a <= r and l <= b and b <= r ->
            {a, b, cnt}

          l <= b and b <= r ->
            {b, r, cnt + 1}

          true ->
            {r - 1, r, cnt + 2}
        end
      end)

    ans
  end
end
```
