# 3296. Minimum Number of Seconds to Make Mountain Height Zero

## Cpp

```cpp
class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        int n = workerTimes.size();
        long long H = mountainHeight;
        // upper bound: worst single worker does all work
        long long maxT = 0;
        for (int t : workerTimes) {
            __int128 val = (__int128)t * H * (H + 1) / 2;
            if (val > maxT) maxT = (long long)val;
        }
        long long lo = 0, hi = maxT;
        auto can = [&](long long seconds)->bool{
            __int128 total = 0;
            for (int t : workerTimes) {
                // find max x such that t*x*(x+1)/2 <= seconds
                if ((long long)t > seconds) continue;
                long double limit = (long double)seconds / t;
                long double disc = sqrtl(1.0L + 8.0L * limit);
                long long x = (long long)((-1.0L + disc) / 2.0L);
                // adjust for possible precision errors
                while ((__int128)t * x * (x + 1) / 2 > seconds) --x;
                while ((__int128)t * (x + 1) * (x + 2) / 2 <= seconds) ++x;
                total += x;
                if (total >= H) return true;
            }
            return total >= H;
        };
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long target = mountainHeight;
        long maxW = 0;
        for (int w : workerTimes) {
            if (w > maxW) maxW = w;
        }
        long low = 0;
        long high = maxW * target * (target + 1) / 2; // upper bound
        while (low < high) {
            long mid = (low + high) >>> 1;
            if (canFinish(mid, workerTimes, target)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canFinish(long time, int[] workerTimes, long need) {
        long total = 0;
        for (int w : workerTimes) {
            // Solve w * x * (x + 1) / 2 <= time
            long D = 1 + (8L * time) / w;               // discriminant part
            double sqrtD = Math.sqrt(D);
            long x = (long) ((sqrtD - 1) / 2);          // initial estimate

            // Adjust in case of rounding errors
            while (w * x * (x + 1) / 2 > time) {
                x--;
            }
            while (w * (x + 1) * (x + 2) / 2 <= time) {
                x++;
            }

            total += x;
            if (total >= need) return true;
        }
        return total >= need;
    }
}
```

## Python

```python
import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        H = mountainHeight
        # Upper bound: worst case single fastest worker does all work
        min_t = min(workerTimes)
        high = min_t * H * (H + 1) // 2
        low = 0

        def feasible(T):
            total = 0
            for ti in workerTimes:
                # solve ti * x*(x+1)/2 <= T
                if ti > T:
                    continue
                disc = 1.0 + 8.0 * T / ti
                x = int((math.sqrt(disc) - 1) // 2)
                # adjust for possible floating error
                while ti * x * (x + 1) // 2 > T:
                    x -= 1
                while ti * (x + 1) * (x + 2) // 2 <= T:
                    x += 1
                total += x
                if total >= H:
                    return True
            return total >= H

        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## Python3

```python
import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Helper to compute total units reduced within given time t
        def total_units(t: int) -> int:
            total = 0
            for w in workerTimes:
                limit = (2 * t) // w
                if limit == 0:
                    continue
                # solve k(k+1) <= limit
                d = 1 + 4 * limit
                k = (math.isqrt(d) - 1) // 2
                total += k
                if total >= mountainHeight:  # early stop
                    break
            return total

        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2  # worst case all work by fastest worker
        low = 0
        while low < high:
            mid = (low + high) // 2
            if total_units(mid) >= mountainHeight:
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
long long minNumberOfSeconds(int mountainHeight, int* workerTimes, int workerTimesSize) {
    // Find minimum possible time using binary search.
    long long low = 0;
    // Upper bound: fastest worker does all work alone.
    int minTime = workerTimes[0];
    for (int i = 1; i < workerTimesSize; ++i)
        if (workerTimes[i] < minTime) minTime = workerTimes[i];
    long long high = (long long)minTime * mountainHeight * (mountainHeight + 1LL) / 2;
    
    while (low < high) {
        long long mid = low + (high - low) / 2;
        long long totalUnits = 0;
        for (int i = 0; i < workerTimesSize; ++i) {
            int t = workerTimes[i];
            // Solve t * x*(x+1)/2 <= mid
            double disc = 1.0 + 8.0 * (double)mid / t;
            long long x = (long long)((sqrt(disc) - 1.0) / 2.0);
            // Adjust for possible floating error
            while (x > 0 && (long long)t * x * (x + 1LL) / 2 > mid) --x;
            while ((long long)t * (x + 1LL) * (x + 2LL) / 2 <= mid) ++x;
            totalUnits += x;
            if (totalUnits >= mountainHeight) break; // early exit
        }
        if (totalUnits >= mountainHeight)
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinNumberOfSeconds(int mountainHeight, int[] workerTimes)
    {
        long H = mountainHeight;
        long maxT = 0;
        foreach (int t in workerTimes)
            if (t > maxT) maxT = t;

        long low = 0;
        long high = maxT * H * (H + 1) / 2; // upper bound

        while (low < high)
        {
            long mid = low + (high - low) / 2;
            if (CanFinish(mid, H, workerTimes))
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }

    private bool CanFinish(long timeLimit, long needed, int[] times)
    {
        long total = 0;
        foreach (int ti in times)
        {
            if (timeLimit < ti) continue; // cannot finish even one unit
            double val = (double)(2.0 * timeLimit) / ti;
            double discriminant = 1.0 + 4.0 * val;
            double sqrtD = Math.Sqrt(discriminant);
            long x = (long)Math.Floor((-1.0 + sqrtD) / 2.0);
            total += x;
            if (total >= needed) return true;
        }
        return total >= needed;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} mountainHeight
 * @param {number[]} workerTimes
 * @return {number}
 */
var minNumberOfSeconds = function(mountainHeight, workerTimes) {
    const H = mountainHeight;
    // Upper bound: slowest worker does all work alone
    let maxT = 0;
    for (const t of workerTimes) if (t > maxT) maxT = t;
    let low = 0;
    let high = Math.floor(maxT * H * (H + 1) / 2); // safe within Number range

    const canFinish = (time) => {
        let total = 0;
        for (const t of workerTimes) {
            // solve t * x*(x+1)/2 <= time
            // quadratic: x^2 + x - (2*time)/t <= 0
            const disc = 1 + (8 * time) / t; // may be large, use double
            let x = Math.floor((Math.sqrt(disc) - 1) / 2);
            if (x < 0) x = 0;
            // adjust for possible floating errors
            while (t * x * (x + 1) / 2 > time) x--;
            while (t * (x + 1) * (x + 2) / 2 <= time) x++;
            total += x;
            if (total >= H) return true; // early exit
        }
        return total >= H;
    };

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (canFinish(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function minNumberOfSeconds(mountainHeight: number, workerTimes: number[]): number {
    const can = (time: number): boolean => {
        let total = 0;
        for (const t of workerTimes) {
            // Solve t * x * (x + 1) / 2 <= time
            // x^2 + x - (2*time)/t <= 0
            const disc = 1 + (8 * time) / t;
            const x = Math.floor((-1 + Math.sqrt(disc)) / 2);
            total += x;
            if (total >= mountainHeight) return true;
        }
        return false;
    };

    let low = 0;
    // Upper bound: slowest worker does all work alone
    const maxT = Math.max(...workerTimes);
    let high = Math.floor(maxT * mountainHeight * (mountainHeight + 1) / 2);

    while (low < high) {
        const mid = Math.floor((low + high) >> 1);
        if (can(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $mountainHeight
     * @param Integer[] $workerTimes
     * @return Integer
     */
    function minNumberOfSeconds($mountainHeight, $workerTimes) {
        $m = $mountainHeight;
        // Upper bound: slowest worker does all work
        $maxA = max($workerTimes);
        $high = (int)($maxA * $m * ($m + 1) / 2);
        $low = 0;

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $total = 0;
            foreach ($workerTimes as $a) {
                if ($mid < $a) continue; // cannot even do one unit
                // solve a * x*(x+1)/2 <= mid
                // x^2 + x - (2*mid)/a <= 0
                $val = (int)(8.0 * $mid / $a); // use float for division then cast
                $disc = 1 + $val;
                $sqrtDisc = sqrt($disc);
                $x = (int)floor((-1 + $sqrtDisc) / 2);
                $total += $x;
                if ($total >= $m) break; // early stop
            }
            if ($total >= $m) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minNumberOfSeconds(_ mountainHeight: Int, _ workerTimes: [Int]) -> Int {
        let H = Int64(mountainHeight)
        var minTime = Int64.max
        for t in workerTimes {
            let ti = Int64(t)
            if ti < minTime { minTime = ti }
        }
        var low: Int64 = 0
        var high: Int64 = minTime * H * (H + 1) / 2
        
        while low < high {
            let mid = (low + high) / 2
            var total: Int64 = 0
            for tInt in workerTimes {
                let t = Int64(tInt)
                if mid >= t {
                    let val = (2 * mid) / t   // maximum k(k+1)
                    var k = Int64((sqrt(Double(1 + 4 * Double(val))) - 1) / 2)
                    while k * (k + 1) > val { k -= 1 }
                    while (k + 1) * (k + 2) <= val { k += 1 }
                    total += k
                    if total >= H { break }
                }
            }
            if total >= H {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumberOfSeconds(mountainHeight: Int, workerTimes: IntArray): Long {
        val h = mountainHeight.toLong()
        var maxT = 0L
        for (t in workerTimes) if (t > maxT) maxT = t.toLong()
        var low = 0L
        var high = maxT * h * (h + 1) / 2
        while (low < high) {
            val mid = (low + high) ushr 1
            if (canFinish(mid, workerTimes, mountainHeight)) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun canFinish(time: Long, workerTimes: IntArray, need: Int): Boolean {
        var total = 0L
        for (tInt in workerTimes) {
            val t = tInt.toLong()
            val discriminant = 1.0 + 8.0 * time / t
            val k = ((Math.sqrt(discriminant) - 1.0) / 2.0).toLong()
            total += k
            if (total >= need) return true
        }
        return false
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int minNumberOfSeconds(int mountainHeight, List<int> workerTimes) {
    int maxWorker = workerTimes.reduce((a, b) => a > b ? a : b);
    int low = 0;
    int high = (maxWorker *
            mountainHeight *
            (mountainHeight + 1)) ~/
        2;

    bool can(int time) {
      int total = 0;
      for (int w in workerTimes) {
        // maximum k such that w * k * (k + 1) / 2 <= time
        int val = (2 * time) ~/ w; // k*(k+1) <= val
        double d = math.sqrt(1.0 + 4.0 * val);
        int k = ((-1.0 + d) / 2.0).floor();
        // adjust for possible floating errors
        while ((k + 1) * (k + 2) <= val) k++;
        while (k * (k + 1) > val) k--;
        total += k;
        if (total >= mountainHeight) return true;
      }
      return false;
    }

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (can(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
import "math"

func minNumberOfSeconds(mountainHeight int, workerTimes []int) int64 {
	type int64 = int64
	H := int64(mountainHeight)

	// find the maximum worker time to set an upper bound
	var maxT int64
	for _, v := range workerTimes {
		if t := int64(v); t > maxT {
			maxT = t
		}
	}

	high := maxT * H * (H + 1) / 2 // definitely enough time
	low := int64(0)

	capacity := func(t, limit int64) int64 {
		if t == 0 || limit < t {
			return 0
		}
		K := (2 * limit) / t // x*(x+1) <= K
		D := float64(1 + 4*K)
		sqrtD := math.Sqrt(D)
		x := int64((sqrtD - 1) / 2)

		// adjust for possible floating‑point error
		for (t*x*(x+1))/2 > limit {
			x--
		}
		for ((t * (x + 1) * (x + 2)) / 2) <= limit {
			x++
		}
		return x
	}

	for low < high {
		mid := (low + high) / 2
		var total int64
		for _, v := range workerTimes {
			total += capacity(int64(v), mid)
			if total >= H {
				break
			}
		}
		if total >= H {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
def min_number_of_seconds(mountain_height, worker_times)
  # Upper bound: fastest worker alone does all work
  t_min = worker_times.min
  high = t_min * mountain_height * (mountain_height + 1) / 2
  low = 0

  while low < high
    mid = (low + high) / 2
    total = 0

    worker_times.each do |ti|
      # solve ti * k * (k + 1) / 2 <= mid
      disc = 1.0 + (8.0 * mid) / ti
      k = ((Math.sqrt(disc) - 1) / 2).floor
      total += k
      break if total >= mountain_height
    end

    if total >= mountain_height
      high = mid
    else
      low = mid + 1
    end
  end

  low
end
```

## Scala

```scala
object Solution {
    def minNumberOfSeconds(mountainHeight: Int, workerTimes: Array[Int]): Long = {
        var low: Long = 0L
        val maxT = workerTimes.max
        var high: Long = maxT.toLong * mountainHeight.toLong * (mountainHeight + 1).toLong / 2

        while (low < high) {
            val mid = low + (high - low) / 2
            var total: Long = 0L
            var i = 0
            while (i < workerTimes.length && total < mountainHeight) {
                val t = workerTimes(i).toLong
                // solve x*(x+1) <= 2*mid / t
                val v = 2.0 * mid / t
                val x = ((Math.sqrt(1.0 + 4.0 * v) - 1.0) / 2.0).toLong
                total += x
                i += 1
            }
            if (total >= mountainHeight) high = mid else low = mid + 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        let h = mountain_height as i64;
        // Upper bound using the slowest (largest time) worker doing all work alone
        let max_t = *worker_times.iter().max().unwrap() as i64;
        let mut low: i64 = 0;
        let mut high: i64 = ((max_t as i128) * (h as i128) * ((h + 1) as i128) / 2) as i64;

        // Helper to compute max units a worker can finish within given time
        fn max_units(t: i64, time: i64) -> i64 {
            if t == 0 { return 0; }
            let limit = (2 * time) / t; // k*(k+1) <= limit
            // initial approximation using floating point sqrt
            let mut k = ((limit as f64).sqrt()) as i64;
            // adjust to correct integer value
            while (k + 1) * (k + 2) <= limit {
                k += 1;
            }
            while k * (k + 1) > limit {
                k -= 1;
            }
            k
        }

        // Feasibility check for a given total time
        let feasible = |time: i64| -> bool {
            let mut sum: i64 = 0;
            for &wt in worker_times.iter() {
                sum += max_units(wt as i64, time);
                if sum >= h {
                    return true;
                }
            }
            false
        };

        while low < high {
            let mid = low + (high - low) / 2;
            if feasible(mid) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low
    }
}
```

## Racket

```racket
(define/contract (min-number-of-seconds mountainHeight workerTimes)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (define (max-units t T)
    (let* ((hi (add1 (floor (sqrt (/ (* 2 T) t))))))
      (let loop ((lo 0) (hi hi))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (time (* t (quotient (* mid (add1 mid)) 2))))
              (if (<= time T)
                  (loop (add1 mid) hi)
                  (loop lo mid)))))))
  (let* ((h mountainHeight)
         (min-t (apply min workerTimes))
         (high (* min-t (/ (* h (+ h 1)) 2)))
         (low 0))
    (let loop ((lo low) (hi high))
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi) 2))
                 (total (let sum-loop ((lst workerTimes) (acc 0))
                          (if (null? lst)
                              acc
                              (sum-loop (cdr lst) (+ acc (max-units (car lst) mid)))))))
            (if (>= total h)
                (loop lo mid)
                (loop (add1 mid) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_number_of_seconds/2]).

-spec min_number_of_seconds(MountainHeight :: integer(), WorkerTimes :: [integer()]) -> integer().
min_number_of_seconds(MountainHeight, WorkerTimes) ->
    MaxTime = lists:max(WorkerTimes),
    High0 = MaxTime * MountainHeight * (MountainHeight + 1) div 2,
    binary_search(0, High0, MountainHeight, WorkerTimes).

binary_search(Low, High, MountainHeight, WorkerTimes) when Low < High ->
    Mid = (Low + High) div 2,
    Total = total_ops(Mid, WorkerTimes),
    if
        Total >= MountainHeight ->
            binary_search(Low, Mid, MountainHeight, WorkerTimes);
        true ->
            binary_search(Mid + 1, High, MountainHeight, WorkerTimes)
    end;
binary_search(Low, _High, _MountainHeight, _WorkerTimes) ->
    Low.

total_ops(_T, []) -> 0;
total_ops(T, [W|Ws]) ->
    Ops = calc_ops(T, W),
    Ops + total_ops(T, Ws).

calc_ops(0, _W) -> 0;
calc_ops(T, W) ->
    X = (math:sqrt(1.0 + 8.0 * T / W) - 1.0) / 2.0,
    trunc(X).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number_of_seconds(mountain_height :: integer, worker_times :: [integer]) :: integer
  def min_number_of_seconds(mountain_height, worker_times) do
    t_min = Enum.min(worker_times)
    high = div(t_min * mountain_height * (mountain_height + 1), 2)
    binary_search(0, high, mountain_height, worker_times)
  end

  defp binary_search(low, high, h, worker_times) when low < high do
    mid = div(low + high, 2)

    if feasible?(mid, h, worker_times) do
      binary_search(low, mid, h, worker_times)
    else
      binary_search(mid + 1, high, h, worker_times)
    end
  end

  defp binary_search(low, _high, _h, _worker_times), do: low

  defp feasible?(time_limit, needed_height, worker_times) do
    total =
      Enum.reduce(worker_times, 0, fn ti, acc ->
        max_units = max_units_for(ti, time_limit)
        acc + max_units
      end)

    total >= needed_height
  end

  defp max_units_for(_ti, time_limit) when time_limit <= 0, do: 0

  defp max_units_for(ti, time_limit) do
    # Solve ti * x * (x + 1) / 2 <= time_limit for maximal integer x
    disc = 1.0 + 8.0 * time_limit / ti
    x = (:math.sqrt(disc) - 1.0) / 2.0
    trunc(Float.floor(x))
  end
end
```
