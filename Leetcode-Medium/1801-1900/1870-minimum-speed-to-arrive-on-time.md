# 1870. Minimum Speed to Arrive on Time

## Cpp

```cpp
class Solution {
public:
    bool canReach(const vector<int>& dist, double hour, int speed) {
        double time = 0.0;
        int n = dist.size();
        for (int i = 0; i < n - 1; ++i) {
            time += ceil((double)dist[i] / speed);
        }
        time += (double)dist.back() / speed;
        return time <= hour + 1e-9;
    }

    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = dist.size();
        if (hour < n - 1.0) return -1; // impossible even with infinite speed

        const int MAX_SPEED = 10000000;
        int left = 1, right = MAX_SPEED + 1; // [left, right)
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canReach(dist, hour, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return (left == MAX_SPEED + 1) ? -1 : left;
    }
};
```

## Java

```java
class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        int n = dist.length;
        if (hour <= n - 1) return -1;
        int left = 1;
        int right = 10_000_001; // exclusive upper bound
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canReach(dist, hour, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left == 10_000_001 ? -1 : left;
    }

    private boolean canReach(int[] dist, double hour, int speed) {
        double time = 0.0;
        int n = dist.length;
        for (int i = 0; i < n - 1; ++i) {
            time += Math.ceil(dist[i] / (double) speed);
            if (time > hour) return false;
        }
        time += (double) dist[n - 1] / speed;
        return time <= hour + 1e-9;
    }
}
```

## Python

```python
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)
        # Minimum possible time is (n-1) because each of the first n-1 trips needs at least 1 hour.
        if hour <= n - 1:
            return -1

        def can(speed):
            total = 0
            # first n-1 trips: need to wait until next integer hour
            for d in dist[:-1]:
                total += (d + speed - 1) // speed  # ceil division, integer hours
            # last trip: exact time
            total += dist[-1] / speed
            return total <= hour

        left, right = 1, 10**7  # answer guaranteed not to exceed 10^7
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        # Minimum possible time is (n-1) because each of the first n-1 trips
        # takes at least one whole hour after rounding up.
        if hour <= n - 1:
            return -1

        def can(speed: int) -> bool:
            total = 0.0
            for d in dist[:-1]:
                total += (d + speed - 1) // speed  # ceil division, integer part
            total += dist[-1] / speed
            return total <= hour

        lo, hi = 1, 10 ** 7 + 1  # hi is exclusive
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo if lo != 10 ** 7 + 1 and can(lo) else -1
```

## C

```c
#include <stddef.h>

int minSpeedOnTime(int* dist, int distSize, double hour) {
    if (hour <= (double)(distSize - 1))
        return -1;
    
    int left = 1, right = 10000000; // answer guaranteed ≤ 10^7
    while (left < right) {
        int mid = left + (right - left) / 2;
        double total = 0.0;
        for (int i = 0; i < distSize - 1; ++i) {
            total += ((long long)dist[i] + mid - 1) / mid; // ceil division
        }
        total += (double)dist[distSize - 1] / mid;
        if (total <= hour)
            right = mid;
        else
            left = mid + 1;
    }
    
    double total = 0.0;
    for (int i = 0; i < distSize - 1; ++i) {
        total += ((long long)dist[i] + left - 1) / left;
    }
    total += (double)dist[distSize - 1] / left;
    
    return (total <= hour) ? left : -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSpeedOnTime(int[] dist, double hour)
    {
        int n = dist.Length;
        // Minimum possible time is (n-1) + epsilon; if hour <= n-1 it's impossible.
        if (hour <= n - 1) return -1;

        int left = 1, right = 10_000_000;
        int answer = -1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (CanArrive(dist, hour, mid))
            {
                answer = mid;
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return answer;
    }

    private bool CanArrive(int[] dist, double hour, int speed)
    {
        double totalTime = 0.0;
        int n = dist.Length;

        for (int i = 0; i < n - 1; ++i)
        {
            totalTime += Math.Ceiling((double)dist[i] / speed);
        }

        totalTime += (double)dist[n - 1] / speed;

        // small epsilon to counter floating point inaccuracies
        return totalTime <= hour + 1e-9;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} dist
 * @param {number} hour
 * @return {number}
 */
var minSpeedOnTime = function(dist, hour) {
    const n = dist.length;
    // Minimum possible time is (n-1) hours + a positive fraction for the last segment.
    if (hour <= n - 1) return -1;

    const can = (speed) => {
        let time = 0;
        for (let i = 0; i < n - 1; ++i) {
            time += Math.ceil(dist[i] / speed);
            if (time > hour) return false; // early exit
        }
        time += dist[n - 1] / speed;
        return time <= hour + 1e-9; // tolerance for floating point errors
    };

    let left = 1, right = 10000000, ans = -1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minSpeedOnTime(dist: number[], hour: number): number {
    const n = dist.length;
    // Minimum possible time is (n-1) because each of the first n-1 trips needs at least 1 whole hour.
    if (hour <= n - 1) return -1;

    const can = (speed: number): boolean => {
        let total = 0;
        for (let i = 0; i < n - 1; ++i) {
            total += Math.ceil(dist[i] / speed);
        }
        total += dist[n - 1] / speed;
        // small epsilon to counter floating point inaccuracies
        return total <= hour + 1e-9;
    };

    let left = 1, right = 10_000_000;
    let answer = -1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $dist
     * @param Float $hour
     * @return Integer
     */
    public function minSpeedOnTime($dist, $hour) {
        $n = count($dist);
        // Minimum possible time is (n-1) because each of the first n-1 trips needs at least 1 hour.
        if ($hour <= $n - 1) {
            return -1;
        }

        $left = 1;
        $right = 10000000; // given constraint
        $answer = -1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->canReach($dist, $hour, $mid)) {
                $answer = $mid;
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }

        return $answer;
    }

    /**
     * @param Integer[] $dist
     * @param Float $hour
     * @param Integer $speed
     * @return bool
     */
    private function canReach($dist, $hour, $speed) {
        $time = 0.0;
        $n = count($dist);
        for ($i = 0; $i < $n - 1; $i++) {
            // ceil(dist[i] / speed)
            $time += intdiv($dist[$i] + $speed - 1, $speed);
        }
        // last segment exact time
        $time += $dist[$n - 1] / $speed;
        // small epsilon to counter floating point errors
        return $time <= $hour + 1e-9;
    }
}
```

## Swift

```swift
class Solution {
    func minSpeedOnTime(_ dist: [Int], _ hour: Double) -> Int {
        let n = dist.count
        if hour <= Double(n - 1) { return -1 }
        var lo = 1
        var hi = 10_000_001 // exclusive upper bound
        
        func can(_ speed: Int) -> Bool {
            var total: Double = 0.0
            for i in 0..<(n - 1) {
                let d = dist[i]
                let tInt = (d + speed - 1) / speed   // ceil division
                total += Double(tInt)
                if total > hour { return false }
            }
            total += Double(dist[n - 1]) / Double(speed)
            return total <= hour + 1e-9
        }
        
        while lo < hi {
            let mid = (lo + hi) / 2
            if can(mid) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo == 10_000_001 ? -1 : lo
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSpeedOnTime(dist: IntArray, hour: Double): Int {
        val n = dist.size
        if (hour <= n - 1) return -1
        var left = 1
        var right = 10_000_000
        while (left < right) {
            val mid = left + (right - left) / 2
            if (canReach(dist, hour, mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return if (canReach(dist, hour, left)) left else -1
    }

    private fun canReach(dist: IntArray, hour: Double, speed: Int): Boolean {
        var totalHours = 0L
        val n = dist.size
        for (i in 0 until n - 1) {
            totalHours += ((dist[i] + speed - 1) / speed).toLong()
            if (totalHours > hour) return false
        }
        val lastTime = dist[n - 1].toDouble() / speed
        val totalTime = totalHours.toDouble() + lastTime
        return totalTime <= hour
    }
}
```

## Dart

```dart
class Solution {
  int minSpeedOnTime(List<int> dist, double hour) {
    int n = dist.length;
    if (hour <= n - 1) return -1;

    bool can(int speed) {
      int totalInt = 0;
      for (int i = 0; i < n - 1; ++i) {
        totalInt += ((dist[i] + speed - 1) ~/ speed);
        if (totalInt > hour) return false;
      }
      double total = totalInt + dist[n - 1] / speed;
      return total <= hour + 1e-9;
    }

    int left = 1, right = 10000000, ans = -1;
    while (left <= right) {
      int mid = (left + right) >> 1;
      if (can(mid)) {
        ans = mid;
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
import "math"

func minSpeedOnTime(dist []int, hour float64) int {
    n := len(dist)
    if hour <= float64(n-1) {
        return -1
    }

    can := func(speed int) bool {
        v := float64(speed)
        total := 0.0
        for i := 0; i < n-1; i++ {
            total += math.Ceil(float64(dist[i]) / v)
            if total > hour { // early exit
                return false
            }
        }
        total += float64(dist[n-1]) / v
        return total <= hour
    }

    low, high := 1, 10000000
    for low < high {
        mid := (low + high) / 2
        if can(mid) {
            high = mid
        } else {
            low = mid + 1
        }
    }
    if can(low) {
        return low
    }
    return -1
}
```

## Ruby

```ruby
def min_speed_on_time(dist, hour)
  n = dist.length
  return -1 if hour <= n - 1

  max_speed = 10_000_000
  low = 1
  high = max_speed + 1

  feasible = lambda do |v|
    time_int = 0
    (0...n-1).each do |i|
      time_int += (dist[i] + v - 1) / v
    end
    total = time_int + dist[-1].to_f / v
    total <= hour
  end

  while low < high
    mid = (low + high) / 2
    if feasible.call(mid)
      high = mid
    else
      low = mid + 1
    end
  end

  feasible.call(low) ? low : -1
end
```

## Scala

```scala
object Solution {
  def minSpeedOnTime(dist: Array[Int], hour: Double): Int = {
    val n = dist.length
    if (n > 1 && hour <= n - 1) return -1

    var lo = 1
    var hi = 10000000
    var ans = -1

    while (lo <= hi) {
      val mid = lo + (hi - lo) / 2
      if (can(dist, hour, mid)) {
        ans = mid
        hi = mid - 1
      } else {
        lo = mid + 1
      }
    }
    ans
  }

  private def can(dist: Array[Int], hour: Double, speed: Int): Boolean = {
    val n = dist.length
    var time = 0.0
    var i = 0
    while (i < n - 1) {
      time += ((dist(i) + speed - 1) / speed).toDouble // ceil division
      i += 1
    }
    time += dist(n - 1).toDouble / speed
    time <= hour
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let n = dist.len();
        if hour < (n - 1) as f64 {
            return -1;
        }
        let mut left = 1i32;
        let mut right = 10_000_001i32; // exclusive upper bound
        while left < right {
            let mid = left + ((right - left) >> 1);
            if Self::can(&dist, hour, mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        if left == 10_000_001 || !Self::can(&dist, hour, left) {
            -1
        } else {
            left
        }
    }

    fn can(dist: &Vec<i32>, hour: f64, speed: i32) -> bool {
        let n = dist.len();
        let mut total: f64 = 0.0;
        for i in 0..n - 1 {
            let d = dist[i] as i64;
            let s = speed as i64;
            total += ((d + s - 1) / s) as f64; // ceil division
        }
        total += (dist[n - 1] as f64) / (speed as f64);
        total <= hour + 1e-9
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)

;; Helper: determine if a given speed allows arrival within hour
(define (can? speed dist hour)
  (let* ((n (length dist))
         (last-index (- n 1)))
    (let loop ((i 0) (lst dist) (sum 0))
      (cond
        [(= i last-index)
         (<= (+ sum (/ (car lst) speed)) hour)]
        [else
         (define d (car lst))
         (define new-sum (+ sum (ceiling (/ d speed))))
         (if (> new-sum hour)
             #f
             (loop (add1 i) (cdr lst) new-sum))]))))

;; Main function with contract
(define/contract (min-speed-on-time dist hour)
  (-> (listof exact-integer?) flonum? exact-integer?)
  (let ((max-speed 10000000))
    (if (not (can? max-speed dist hour))
        -1
        (let loop ((low 1) (high max-speed) (ans max-speed))
          (if (> low high)
              ans
              (let ((mid (quotient (+ low high) 2)))
                (if (can? mid dist hour)
                    (loop low (sub1 mid) mid)
                    (loop (add1 mid) high ans))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_speed_on_time/2]).

-spec min_speed_on_time(Dist :: [integer()], Hour :: float()) -> integer().
min_speed_on_time(Dist, Hour) ->
    N = length(Dist),
    case Hour =< N - 1 of
        true -> -1;
        false -> binary_search(1, 10000000, Dist, Hour)
    end.

-spec binary_search(integer(), integer(), [integer()], float()) -> integer().
binary_search(Low, High, _Dist, _Hour) when Low > High ->
    -1;
binary_search(Low, High, Dist, Hour) ->
    Mid = (Low + High) div 2,
    case feasible(Mid, Dist, Hour) of
        true ->
            Ans = binary_search(Low, Mid - 1, Dist, Hour),
            case Ans of
                -1 -> Mid;
                _ -> Ans
            end;
        false ->
            binary_search(Mid + 1, High, Dist, Hour)
    end.

-spec feasible(integer(), [integer()], float()) -> boolean().
feasible(V, Dist, Hour) ->
    feasible_acc(V, Dist, 0, Hour).

-spec feasible_acc(integer(), [integer()], integer(), float()) -> boolean().
feasible_acc(_V, [], _Acc, _Hour) ->
    false;
feasible_acc(V, [Last], Acc, Hour) ->
    Total = Acc + Last / V,
    Total =< Hour;
feasible_acc(V, [D|Rest], Acc, Hour) ->
    NewAcc = Acc + ((D + V - 1) div V),
    feasible_acc(V, Rest, NewAcc, Hour).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_speed_on_time(dist :: [integer], hour :: float) :: integer
  def min_speed_on_time(dist, hour) do
    max_v = 10_000_000

    # If even the maximum speed cannot meet the deadline, return -1 early.
    if not feasible?(max_v, dist, hour) do
      -1
    else
      binary_search(1, max_v, dist, hour)
    end
  end

  defp binary_search(l, r, dist, hour) when l < r do
    mid = div(l + r, 2)

    if feasible?(mid, dist, hour) do
      binary_search(l, mid, dist, hour)
    else
      binary_search(mid + 1, r, dist, hour)
    end
  end

  defp binary_search(l, _r, _dist, _hour), do: l

  defp feasible?(v, dist, hour) do
    n = length(dist)

    total_int =
      dist
      |> Enum.take(n - 1)
      |> Enum.reduce(0, fn d, acc -> acc + div(d + v - 1, v) end)

    last = List.last(dist)
    total = total_int + last / v

    total <= hour + 1.0e-9
  end
end
```
