# 3281. Maximize Score of Numbers in Ranges

## Cpp

```cpp
class Solution {
public:
    int maxPossibleScore(std::vector<int>& start, int d) {
        std::sort(start.begin(), start.end());
        long long minStart = *std::min_element(start.begin(), start.end());
        long long maxStart = *std::max_element(start.begin(), start.end());
        long long lo = 0;
        long long hi = (maxStart + d) - minStart; // maximum possible distance
        
        auto feasible = [&](long long x) -> bool {
            long long last = start[0]; // choose the leftmost point in first interval
            if (last > (long long)start[0] + d) return false;
            for (size_t i = 1; i < start.size(); ++i) {
                long long need = last + x;
                long long cur = std::max<long long>(need, start[i]);
                if (cur > (long long)start[i] + d) return false;
                last = cur;
            }
            return true;
        };
        
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (feasible(mid))
                lo = mid;
            else
                hi = mid - 1;
        }
        return static_cast<int>(lo);
    }
};
```

## Java

```java
class Solution {
    public int maxPossibleScore(int[] start, int d) {
        Arrays.sort(start);
        int n = start.length;
        long minStart = start[0];
        long maxStart = start[n - 1];
        long lo = 0;
        long hi = (maxStart + d) - minStart; // maximum possible distance

        while (lo < hi) {
            long mid = (lo + hi + 1) >>> 1;
            if (canPlace(start, d, mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return (int) lo;
    }

    private boolean canPlace(int[] start, int d, long minDist) {
        long last = -(1L << 60); // sufficiently small sentinel
        for (int s : start) {
            long candidate = Math.max((long) s, last + minDist);
            if (candidate > (long) s + d) {
                return false;
            }
            last = candidate;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def maxPossibleScore(self, start, d):
        """
        :type start: List[int]
        :type d: int
        :rtype: int
        """
        start.sort()
        n = len(start)

        def feasible(x):
            cur = start[0]  # choose the leftmost point in first interval
            for i in range(1, n):
                l = start[i]
                r = l + d
                need = cur + x
                if need > r:
                    return False
                cur = max(l, need)
            return True

        low, high = 0, (start[-1] + d) - start[0]
        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        starts = sorted(start)
        n = len(starts)

        def feasible(x: int) -> bool:
            cur = -10**20  # sufficiently small
            for s in starts:
                low = max(s, cur + x)
                if low > s + d:
                    return False
                cur = low
            return True

        lo = 0
        hi = max(starts) + d - min(starts)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static bool feasible(int *arr, int n, int d, long long x) {
    long long prev = -(1LL << 60);
    for (int i = 0; i < n; ++i) {
        long long low = arr[i];
        long long high = (long long)arr[i] + d;
        long long cand = low > prev + x ? low : prev + x;
        if (cand > high) return false;
        prev = cand;
    }
    return true;
}

int maxPossibleScore(int* start, int startSize, int d) {
    qsort(start, startSize, sizeof(int), cmp_int);
    long long lo = 0;
    long long hi = ((long long)start[startSize - 1] + d) - (long long)start[0];
    while (lo < hi) {
        long long mid = lo + (hi - lo + 1) / 2;
        if (feasible(start, startSize, d, mid))
            lo = mid;
        else
            hi = mid - 1;
    }
    return (int)lo;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxPossibleScore(int[] start, int d)
    {
        Array.Sort(start);
        int n = start.Length;
        long minStart = start[0];
        long maxEnd = (long)start[n - 1] + d;
        long lo = 0, hi = maxEnd - minStart;

        while (lo < hi)
        {
            long mid = lo + (hi - lo + 1) / 2;
            if (CanAchieve(mid, start, d))
                lo = mid;
            else
                hi = mid - 1;
        }
        return (int)lo;
    }

    private bool CanAchieve(long gap, int[] start, int d)
    {
        long last = long.MinValue / 4; // sufficiently small sentinel
        foreach (int s in start)
        {
            long left = s;
            long right = (long)s + d;
            long need = Math.Max(left, last + gap);
            if (need > right) return false;
            last = need;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} start
 * @param {number} d
 * @return {number}
 */
var maxPossibleScore = function(start, d) {
    const n = start.length;
    const arr = start.slice().sort((a, b) => a - b);
    const minStart = arr[0];
    const maxStart = arr[n - 1];
    let low = 0;
    let high = (maxStart + d) - minStart; // maximum possible distance

    const can = (dist) => {
        let cur = -Infinity;
        for (let i = 0; i < n; i++) {
            const l = arr[i];
            const r = l + d;
            const val = Math.max(l, cur + dist);
            if (val > r) return false;
            cur = val;
        }
        return true;
    };

    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maxPossibleScore(start: number[], d: number): number {
    const n = start.length;
    start.sort((a, b) => a - b);
    const minStart = start[0];
    const maxStart = start[n - 1];
    let lo = 0;
    let hi = (maxStart + d) - minStart;

    const can = (dist: number): boolean => {
        let last = Number.NEGATIVE_INFINITY;
        for (let i = 0; i < n; i++) {
            const low = start[i];
            const high = start[i] + d;
            const need = Math.max(low, last + dist);
            if (need > high) return false;
            last = need;
        }
        return true;
    };

    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $start
     * @param Integer $d
     * @return Integer
     */
    function maxPossibleScore($start, $d) {
        sort($start);
        $n = count($start);
        $low = 0;
        // maximum possible value is up to max(start)+d (<=2e9), so distance can't exceed that.
        $high = 2000000000 + $d; 

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canPlace($start, $d, $mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canPlace($arr, $d, $dist) {
        $prev = $arr[0]; // choose the smallest possible for first interval
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $need = $prev + $dist;
            $cur = max($arr[$i], $need);
            if ($cur > $arr[$i] + $d) {
                return false;
            }
            $prev = $cur;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func maxPossibleScore(_ start: [Int], _ d: Int) -> Int {
        var starts = start.map { Int64($0) }
        starts.sort()
        let D = Int64(d)
        var low: Int64 = 0
        let minStart = starts.first!
        let maxStart = starts.last!
        var high: Int64 = (maxStart + D) - minStart
        while low < high {
            let mid = (low + high + 1) >> 1
            if can(mid, starts, D) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return Int(low)
    }

    private func can(_ dist: Int64, _ starts: [Int64], _ d: Int64) -> Bool {
        var last: Int64 = Int64.min / 4
        for s in starts {
            let candidate = max(s, last + dist)
            if candidate > s + d {
                return false
            }
            last = candidate
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPossibleScore(start: IntArray, d: Int): Int {
        val n = start.size
        val intervals = LongArray(n) { start[it].toLong() }
        java.util.Arrays.sort(intervals)
        val D = d.toLong()
        var low = 0L
        var high = (intervals[n - 1] + D) - intervals[0]
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (canPlace(mid, intervals, D)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low.toInt()
    }

    private fun canPlace(dist: Long, intervals: LongArray, d: Long): Boolean {
        var prev = intervals[0] // choose the smallest possible in first interval
        for (i in 1 until intervals.size) {
            val needed = prev + dist
            val cur = if (needed > intervals[i]) needed else intervals[i]
            if (cur > intervals[i] + d) return false
            prev = cur
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int maxPossibleScore(List<int> start, int d) {
    List<int> s = List.from(start);
    s.sort();
    int n = s.length;
    int low = 0;
    int high = (s.last + d) - s.first;

    bool can(int x) {
      int last = -(1 << 60);
      for (int i = 0; i < n; ++i) {
        int left = s[i];
        int right = left + d;
        int need = left > last + x ? left : last + x;
        if (need > right) return false;
        last = need;
      }
      return true;
    }

    while (low < high) {
      int mid = low + ((high - low) >> 1) + 1; // upper middle
      if (can(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
import "sort"

func maxPossibleScore(start []int, d int) int {
	n := len(start)
	sort.Ints(start)

	minStart := start[0]
	maxStart := start[n-1]

	hi := (maxStart + d) - minStart
	low := 0

	for low < hi {
		mid := (low + hi + 1) / 2
		if feasible(start, d, mid) {
			low = mid
		} else {
			hi = mid - 1
		}
	}
	return low
}

func feasible(arr []int, d int, x int) bool {
	var last int64 = -(1 << 60)
	dd := int64(d)
	xx := int64(x)

	for _, s := range arr {
		minVal := int64(s)
		if last+xx > minVal {
			minVal = last + xx
		}
		if minVal > int64(s)+dd {
			return false
		}
		last = minVal
	}
	return true
}
```

## Ruby

```ruby
def max_possible_score(start, d)
  starts = start.sort
  n = starts.length
  lo = 0
  hi = (starts[-1] + d) - starts[0]

  feasible = lambda do |dist|
    cur = starts[0]
    i = 1
    while i < n
      s = starts[i]
      need = cur + dist
      val = need > s ? need : s
      return false if val > s + d
      cur = val
      i += 1
    end
    true
  end

  while lo < hi
    mid = (lo + hi + 1) / 2
    if feasible.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
```

## Scala

```scala
object Solution {
  def maxPossibleScore(start: Array[Int], d: Int): Int = {
    val arr = start.sorted.map(_.toLong)
    val dd = d.toLong
    var lo = 0L
    var hi = (arr.max + dd) - arr.min // maximum possible distance

    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (feasible(mid, arr, dd)) lo = mid else hi = mid - 1
    }
    lo.toInt
  }

  private def feasible(x: Long, arr: Array[Long], d: Long): Boolean = {
    var last = Long.MinValue / 4 // sufficiently small sentinel
    for (s <- arr) {
      val need = math.max(s, if (last == Long.MinValue / 4) s else last + x)
      if (need > s + d) return false
      last = need
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_possible_score(start: Vec<i32>, d: i32) -> i32 {
        let mut starts: Vec<i64> = start.iter().map(|&x| x as i64).collect();
        starts.sort_unstable();
        let d_i = d as i64;
        let min_start = *starts.first().unwrap();
        let max_start = *starts.last().unwrap();
        // exclusive upper bound for binary search
        let mut lo: i64 = 0;
        let mut hi: i64 = (max_start + d_i) - min_start + 1;

        while lo < hi {
            let mid = (lo + hi) / 2;
            if Self::feasible(mid, &starts, d_i) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        (lo - 1) as i32
    }

    fn feasible(x: i64, starts: &[i64], d: i64) -> bool {
        let mut last: i64 = i64::MIN / 4; // sufficiently small sentinel
        for &l in starts.iter() {
            let r = l + d;
            let v = std::cmp::max(l, last + x);
            if v > r {
                return false;
            }
            last = v;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (max-possible-score start d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort start <))
         (vec (list->vector sorted))
         (n (vector-length vec))
         (min-start (vector-ref vec 0))
         (max-end (+ (apply max start) d))
         (high (- max-end min-start))) ; inclusive upper bound
    (define (feasible? x)
      (let loop ((i 0) (prev #f))
        (if (= i n)
            #t
            (let* ((s (vector-ref vec i))
                   (val (if prev (+ prev x) s)))
              (if (> val (+ s d))
                  #f
                  (loop (+ i 1) val))))))
    (let loop ((lo 0) (hi high))
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi 1) 2))) ; upper mid to avoid infinite loop
            (if (feasible? mid)
                (loop mid hi)
                (loop lo (- mid 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_possible_score/2]).

-spec max_possible_score(Start :: [integer()], D :: integer()) -> integer().
max_possible_score(Start, D) ->
    Sorted = lists:sort(Start),
    MinStart = lists:min(Sorted),
    MaxStart = lists:max(Sorted),
    High = (MaxStart + D) - MinStart,
    binary_search(0, High, Sorted, D).

binary_search(Low, High, _Sorted, _D) when Low >= High ->
    Low;
binary_search(Low, High, Sorted, D) ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, Sorted, D) of
        true -> binary_search(Mid, High, Sorted, D);
        false -> binary_search(Low, Mid - 1, Sorted, D)
    end.

-spec feasible(integer(), [integer()], integer()) -> boolean().
feasible(_X, [], _D) ->
    true;
feasible(X, [First|Rest], D) ->
    feasible_loop(Rest, X, D, First).

-spec feasible_loop([integer()], integer(), integer(), integer()) -> boolean().
feasible_loop([], _X, _D, _Cur) ->
    true;
feasible_loop([S|Rest], X, D, Cur) ->
    MinVal = erlang:max(S, Cur + X),
    if
        MinVal =< S + D ->
            feasible_loop(Rest, X, D, MinVal);
        true ->
            false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_possible_score(start :: [integer], d :: integer) :: integer
  def max_possible_score(start, d) do
    sorted = Enum.sort(start)
    min_s = hd(sorted)
    max_s = List.last(sorted)

    lo = 0
    hi = (max_s + d) - min_s

    binary_search(lo, hi, sorted, d)
  end

  defp binary_search(lo, hi, sorted, d) when lo < hi do
    mid = div(lo + hi + 1, 2)

    if feasible?(sorted, d, mid) do
      binary_search(mid, hi, sorted, d)
    else
      binary_search(lo, mid - 1, sorted, d)
    end
  end

  defp binary_search(lo, _hi, _sorted, _d), do: lo

  defp feasible?(sorted, d, x) do
    result =
      Enum.reduce_while(sorted, nil, fn s, prev ->
        left = s
        right = s + d

        if prev == nil do
          {:cont, left}
        else
          need = prev + x

          if need > right do
            {:halt, false}
          else
            new_val = max(need, left)
            {:cont, new_val}
          end
        end
      end)

    result != false
  end
end
```
