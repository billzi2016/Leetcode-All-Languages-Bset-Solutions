# 1326. Minimum Number of Taps to Open to Water a Garden

## Cpp

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> maxReach(n + 1, 0);
        for (int i = 0; i <= n; ++i) {
            int l = max(0, i - ranges[i]);
            int r = min(n, i + ranges[i]);
            maxReach[l] = max(maxReach[l], r);
        }
        int taps = 0;
        int curEnd = 0, nextEnd = 0;
        for (int i = 0; i < n; ++i) {
            nextEnd = max(nextEnd, maxReach[i]);
            if (i == curEnd) {
                ++taps;
                curEnd = nextEnd;
                if (curEnd >= n) break;
                if (curEnd == i) return -1; // cannot move forward
            }
        }
        return curEnd >= n ? taps : -1;
    }
};
```

## Java

```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        // maxReach[l] = farthest right endpoint of any tap whose interval starts at or before l
        int[] maxReach = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]);
            int right = Math.min(n, i + ranges[i]);
            if (maxReach[left] < right) {
                maxReach[left] = right;
            }
        }

        int taps = 0;
        int curEnd = 0;      // end of current coverage
        int farthest = 0;    // farthest reachable within the current segment

        for (int i = 0; i < n; i++) {
            farthest = Math.max(farthest, maxReach[i]);
            if (i == curEnd) {               // need to open a new tap
                taps++;
                curEnd = farthest;
                if (curEnd <= i) {           // cannot extend coverage
                    return -1;
                }
            }
        }

        return curEnd >= n ? taps : -1;
    }
}
```

## Python

```python
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        if n == 0:
            return 0

        # maxReach[i] = farthest right endpoint of any interval that starts at or before i
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            if maxReach[left] < right:
                maxReach[left] = right

        taps = 0
        cur_end = 0
        furthest = 0

        for i in range(n):
            furthest = max(furthest, maxReach[i])
            if i == cur_end:
                taps += 1
                cur_end = furthest
                if cur_end <= i:  # cannot extend further
                    return -1
        return taps
```

## Python3

```python
from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n == 0:
            return 0
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            if maxReach[left] < right:
                maxReach[left] = right

        taps = 0
        curr_end = 0
        furthest = 0

        for i in range(n + 1):
            if i > furthest:  # cannot reach this point
                return -1
            furthest = max(furthest, maxReach[i])
            if i == curr_end:
                taps += 1
                curr_end = furthest
                if curr_end >= n:
                    break

        return taps if curr_end >= n else -1
```

## C

```c
#include <stdlib.h>

int minTaps(int n, int* ranges, int rangesSize) {
    if (n == 0) return 0;
    
    int *maxReach = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; ++i) {
        int r = ranges[i];
        int left = i - r;
        if (left < 0) left = 0;
        int right = i + r;
        if (right > n) right = n;
        if (maxReach[left] < right) maxReach[left] = right;
    }
    
    int taps = 0, curEnd = 0, farthest = 0;
    for (int i = 0; i < n; ++i) {
        if (i > farthest) {
            free(maxReach);
            return -1;
        }
        if (maxReach[i] > farthest) farthest = maxReach[i];
        if (i == curEnd) {
            ++taps;
            curEnd = farthest;
        }
    }
    
    free(maxReach);
    return curEnd >= n ? taps : -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinTaps(int n, int[] ranges) {
        if (n == 0) return 0;
        int[] maxReach = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.Max(0, i - ranges[i]);
            int right = Math.Min(n, i + ranges[i]);
            if (maxReach[left] < right) {
                maxReach[left] = right;
            }
        }

        int taps = 0;
        int curEnd = 0;
        int furthest = 0;

        for (int i = 0; i < n; i++) {
            furthest = Math.Max(furthest, maxReach[i]);
            if (i == curEnd) {
                taps++;
                curEnd = furthest;
                if (curEnd <= i) return -1;
            }
        }

        return curEnd >= n ? taps : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function(n, ranges) {
    if (n === 0) return 0;
    const maxReach = new Array(n + 1).fill(0);
    for (let i = 0; i <= n; ++i) {
        const r = ranges[i];
        const left = Math.max(0, i - r);
        const right = Math.min(n, i + r);
        if (maxReach[left] < right) maxReach[left] = right;
    }
    let taps = 0;
    let currentEnd = 0;
    let furthest = 0;
    for (let i = 0; i < n; ++i) {
        furthest = Math.max(furthest, maxReach[i]);
        if (i === currentEnd) {
            taps++;
            currentEnd = furthest;
            if (currentEnd <= i) return -1; // cannot progress
        }
    }
    return currentEnd >= n ? taps : -1;
};
```

## Typescript

```typescript
function minTaps(n: number, ranges: number[]): number {
    const maxRight = new Array(n + 1).fill(0);
    for (let i = 0; i <= n; ++i) {
        const r = ranges[i];
        let left = i - r;
        if (left < 0) left = 0;
        let right = i + r;
        if (right > n) right = n;
        if (maxRight[left] < right) maxRight[left] = right;
    }

    let taps = 0;
    let curEnd = 0;
    let nextEnd = 0;

    for (let i = 0; i <= n; ++i) {
        if (i > nextEnd) return -1;
        if (i > curEnd) {
            taps++;
            curEnd = nextEnd;
        }
        if (maxRight[i] > nextEnd) nextEnd = maxRight[i];
    }

    return taps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $ranges
     * @return Integer
     */
    function minTaps($n, $ranges) {
        // Edge case: no length to cover
        if ($n == 0) return 0;

        // maxReach[left] = farthest right endpoint of any tap covering 'left'
        $maxReach = array_fill(0, $n + 1, 0);
        $len = count($ranges);
        for ($i = 0; $i < $len; $i++) {
            $r = $ranges[$i];
            if ($r == 0) continue;
            $left = max(0, $i - $r);
            $right = min($n, $i + $r);
            if ($maxReach[$left] < $right) {
                $maxReach[$left] = $right;
            }
        }

        $steps = 0;
        $currentEnd = 0;
        $furthest = 0;

        for ($i = 0; $i <= $n; $i++) {
            // Update the furthest reachable point within current window
            if ($maxReach[$i] > $furthest) {
                $furthest = $maxReach[$i];
            }

            // When we reach the end of the current coverage interval,
            // we need to open a new tap (increase steps)
            if ($i == $currentEnd) {
                // If we cannot extend further, watering is impossible
                if ($furthest <= $i && $i < $n) {
                    return -1;
                }
                $steps++;
                $currentEnd = $furthest;
                // Early exit if we've already covered the garden
                if ($currentEnd >= $n) {
                    break;
                }
            }
        }

        return $currentEnd >= $n ? $steps : -1;
    }
}
```

## Swift

```swift
class Solution {
    func minTaps(_ n: Int, _ ranges: [Int]) -> Int {
        if n == 0 { return 0 }
        var maxReach = Array(repeating: 0, count: n + 1)
        for i in 0...n {
            let r = ranges[i]
            let left = max(0, i - r)
            let right = min(n, i + r)
            if maxReach[left] < right {
                maxReach[left] = right
            }
        }
        var taps = 0
        var currentEnd = 0
        var furthest = 0
        for i in 0..<n {
            furthest = max(furthest, maxReach[i])
            if i == currentEnd {
                taps += 1
                currentEnd = furthest
                if currentEnd <= i { return -1 }
            }
        }
        return taps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTaps(n: Int, ranges: IntArray): Int {
        if (n == 0) return 0
        val maxReach = IntArray(n + 1)
        for (i in 0..n) {
            val r = ranges[i]
            if (r == 0) continue
            val left = kotlin.math.max(0, i - r)
            val right = kotlin.math.min(n, i + r)
            if (maxReach[left] < right) maxReach[left] = right
        }
        var taps = 0
        var curEnd = 0
        var nextEnd = 0
        var i = 0
        while (i <= n) {
            if (i <= n && maxReach[i] > nextEnd) {
                nextEnd = maxReach[i]
            }
            if (i == curEnd) {
                taps++
                curEnd = nextEnd
                if (curEnd >= n) return taps
            }
            i++
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minTaps(int n, List<int> ranges) {
    List<int> maxReach = List.filled(n + 1, 0);
    for (int i = 0; i <= n; ++i) {
      int r = ranges[i];
      int left = i - r;
      if (left < 0) left = 0;
      int right = i + r;
      if (right > n) right = n;
      if (maxReach[left] < right) maxReach[left] = right;
    }
    int steps = 0;
    int currentEnd = 0;
    int furthest = 0;
    for (int i = 0; i < n; ++i) {
      furthest = furthest > maxReach[i] ? furthest : maxReach[i];
      if (i == currentEnd) {
        steps++;
        currentEnd = furthest;
        if (currentEnd <= i) return -1;
      }
    }
    return steps;
  }
}
```

## Golang

```go
func minTaps(n int, ranges []int) int {
	if n == 0 {
		return 0
	}
	maxReach := make([]int, n+1)
	for i := 0; i <= n; i++ {
		r := ranges[i]
		left := i - r
		if left < 0 {
			left = 0
		}
		right := i + r
		if right > n {
			right = n
		}
		if maxReach[left] < right {
			maxReach[left] = right
		}
	}

	steps, currentEnd, furthest := 0, 0, 0
	for i := 0; i < n; i++ {
		if maxReach[i] > furthest {
			furthest = maxReach[i]
		}
		if i == currentEnd {
			steps++
			currentEnd = furthest
			if currentEnd <= i {
				return -1
			}
		}
	}
	if currentEnd < n {
		return -1
	}
	return steps
}
```

## Ruby

```ruby
def min_taps(n, ranges)
  max_reach = Array.new(n + 1, 0)

  (0..n).each do |i|
    r = ranges[i]
    left = i - r
    left = 0 if left < 0
    right = i + r
    right = n if right > n
    max_reach[left] = [max_reach[left], right].max
  end

  taps = 0
  cur_end = 0
  next_end = 0

  (0...n).each do |i|
    next_end = [next_end, max_reach[i]].max
    if i == cur_end
      taps += 1
      cur_end = next_end
      return -1 if cur_end <= i
    end
    break if cur_end >= n
  end

  cur_end >= n ? taps : -1
end
```

## Scala

```scala
object Solution {
    def minTaps(n: Int, ranges: Array[Int]): Int = {
        if (n == 0) return 0
        val maxReach = Array.fill(n + 1)(0)
        for (i <- 0 to n) {
            val r = ranges(i)
            val left = math.max(0, i - r)
            val right = math.min(n, i + r)
            if (maxReach(left) < right) maxReach(left) = right
        }
        var taps = 0
        var curEnd = 0
        var furthest = 0
        for (i <- 0 until n) {
            furthest = math.max(furthest, maxReach(i))
            if (i == curEnd) {
                taps += 1
                curEnd = furthest
                if (curEnd <= i) return -1
            }
        }
        if (curEnd >= n) taps else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
        let n_usize = n as usize;
        let mut max_reach = vec![0usize; n_usize + 1];
        for (i, &r) in ranges.iter().enumerate() {
            if r == 0 {
                continue;
            }
            let left = if i >= r as usize { i - r as usize } else { 0 };
            let right = std::cmp::min(n_usize, i + r as usize);
            if max_reach[left] < right {
                max_reach[left] = right;
            }
        }

        let mut taps = 0usize;
        let mut cur_end = 0usize;
        let mut next_end = 0usize;

        for i in 0..=n_usize {
            if i > next_end {
                return -1;
            }
            if i > cur_end {
                taps += 1;
                cur_end = next_end;
            }
            if max_reach[i] > next_end {
                next_end = max_reach[i];
            }
        }

        taps as i32
    }
}
```

## Racket

```racket
(define/contract (min-taps n ranges)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ([size (+ n 1)]
         [max-reach (make-vector size 0)])
    ;; Build the farthest right endpoint reachable from each left point
    (for ([i (in-range size)])
      (let* ([r (list-ref ranges i)]
             [left (max 0 (- i r))]
             [right (min n (+ i r))])
        (vector-set! max-reach left
                     (max (vector-ref max-reach left) right))))
    ;; Greedy interval covering
    (let loop ([i 0] [current-end 0] [taps 0])
      (if (>= current-end n)
          taps
          (let-values ([(next-i furthest)]
                       (let inner-loop ([j i] [best current-end])
                         (if (> j current-end)
                             (values j best)
                             (inner-loop (+ j 1) (max best (vector-ref max-reach j))))))
            (if (= furthest current-end)
                -1
                (loop next-i furthest (+ taps 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_taps/2]).

-spec min_taps(N :: integer(), Ranges :: [integer()]) -> integer().
min_taps(N, Ranges) ->
    case N of
        0 -> 0;
        _ ->
            MaxArr = build_max_reach(0, N, Ranges, array:new(N+1, {default,0})),
            BestArr = compute_best(N, MaxArr),
            greedy(N, BestArr)
    end.

build_max_reach(_Idx, _N, [], Arr) -> Arr;
build_max_reach(Idx, N, [R|Rest], Arr) ->
    Left  = max(0, Idx - R),
    Right = min(N, Idx + R),
    Existing = array:get(Left, Arr),
    NewArr = if Right > Existing -> array:set(Left, Right, Arr); true -> Arr end,
    build_max_reach(Idx+1, N, Rest, NewArr).

compute_best(N, MaxArr) ->
    compute_best(0, N, MaxArr, array:new(N+1, {default,0}), 0).

compute_best(I, N, _MaxArr, BestArr, CurMax) when I > N -> BestArr;
compute_best(I, N, MaxArr, BestArr, CurMax) ->
    Reach = array:get(I, MaxArr),
    NewMax = if Reach > CurMax -> Reach; true -> CurMax end,
    UpdatedBestArr = array:set(I, NewMax, BestArr),
    compute_best(I+1, N, MaxArr, UpdatedBestArr, NewMax).

greedy(N, BestArr) ->
    greedy(0, N, BestArr, 0).

greedy(CurEnd, N, _BestArr, Taps) when CurEnd >= N -> Taps;
greedy(CurEnd, N, BestArr, Taps) ->
    Next = array:get(CurEnd, BestArr),
    if
        Next == CurEnd -> -1;
        true -> greedy(Next, N, BestArr, Taps+1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_taps(n :: integer, ranges :: [integer]) :: integer
  def min_taps(n, ranges) do
    # Build an array where max_reach[l] = farthest right endpoint of any tap whose interval starts at l
    max_reach =
      :array.new(n + 1, default: 0)
      |> Enum.reduce(Enum.with_index(ranges), fn {r, i}, arr ->
        left = max(i - r, 0)
        right = min(i + r, n)

        current = :array.get(left, arr)

        if right > current do
          :array.set(left, right, arr)
        else
          arr
        end
      end)

    # Greedy sweep to cover [0, n]
    {result, _} =
      Enum.reduce_while(0..(n - 1), {0, {0, 0}}, fn i, {steps, {cur_end, furthest}} ->
        furthest = max(furthest, :array.get(i, max_reach))

        if i == cur_end do
          # Need to open a new tap
          if furthest <= i do
            {:halt, {-1, nil}}
          else
            {:cont, {steps + 1, {furthest, furthest}}}
          end
        else
          {:cont, {steps, {cur_end, furthest}}}
        end
      end)

    case result do
      -1 -> -1
      steps -> steps
    end
  end
end
```
