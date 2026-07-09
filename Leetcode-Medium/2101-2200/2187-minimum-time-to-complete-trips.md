# 2187. Minimum Time to Complete Trips

## Cpp

```cpp
class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        long long min_t = *min_element(time.begin(), time.end());
        long long left = 1;
        long long right = min_t * (long long)totalTrips; // upper bound
        
        while (left < right) {
            long long mid = left + (right - left) / 2;
            long long trips = 0;
            for (int t : time) {
                trips += mid / t;
                if (trips >= totalTrips) break; // avoid unnecessary work/overflow
            }
            if (trips >= totalTrips) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long minTime = Long.MAX_VALUE;
        for (int t : time) {
            if (t < minTime) minTime = t;
        }
        long low = 1L;
        long high = minTime * (long) totalTrips; // upper bound
        
        while (low < high) {
            long mid = low + (high - low) / 2;
            long trips = 0;
            for (int t : time) {
                trips += mid / t;
                if (trips >= totalTrips) break; // avoid unnecessary work
            }
            if (trips >= totalTrips) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        lo = 1
        hi = min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    break
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo = 1
        hi = min(time) * totalTrips  # upper bound
        
        while lo < hi:
            mid = (lo + hi) // 2
            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:  # early stop to avoid unnecessary work
                    break
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
long long minimumTime(int* time, int timeSize, int totalTrips) {
    long long min_t = LLONG_MAX;
    for (int i = 0; i < timeSize; ++i) {
        if ((long long)time[i] < min_t) min_t = time[i];
    }
    long long left = 1;
    long long right = min_t * (long long)totalTrips;
    while (left < right) {
        long long mid = left + (right - left) / 2;
        long long trips = 0;
        for (int i = 0; i < timeSize; ++i) {
            trips += mid / time[i];
            if (trips >= totalTrips) break;
        }
        if (trips >= totalTrips) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinimumTime(int[] time, int totalTrips)
    {
        long minTime = time[0];
        foreach (int t in time)
        {
            if (t < minTime) minTime = t;
        }

        long left = 1;
        long right = minTime * (long)totalTrips; // upper bound

        while (left < right)
        {
            long mid = left + (right - left) / 2;
            long trips = 0;
            foreach (int t in time)
            {
                trips += mid / t;
                if (trips >= totalTrips) break; // early stop to avoid overflow
            }

            if (trips >= totalTrips)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function(time, totalTrips) {
    let minT = Number.MAX_SAFE_INTEGER;
    for (let t of time) {
        if (t < minT) minT = t;
    }
    let left = 1;
    let right = minT * totalTrips; // upper bound
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let trips = 0;
        for (let t of time) {
            trips += Math.floor(mid / t);
            if (trips >= totalTrips) break; // early stop
        }
        if (trips >= totalTrips) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function minimumTime(time: number[], totalTrips: number): number {
    const minTime = Math.min(...time);
    let left = 1;
    let right = minTime * totalTrips; // upper bound

    const canComplete = (t: number): boolean => {
        let trips = 0;
        for (const ti of time) {
            trips += Math.floor(t / ti);
            if (trips >= totalTrips) return true;
        }
        return false;
    };

    while (left < right) {
        const mid = Math.floor((left + right) >> 1);
        if (canComplete(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer $totalTrips
     * @return Integer
     */
    function minimumTime($time, $totalTrips) {
        $minTime = min($time);
        $left = 1;
        $right = $minTime * $totalTrips; // upper bound

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            $trips = 0;
            foreach ($time as $t) {
                $trips += intdiv($mid, $t);
                if ($trips >= $totalTrips) {
                    break;
                }
            }

            if ($trips >= $totalTrips) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }

        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ time: [Int], _ totalTrips: Int) -> Int {
        guard let minTime = time.min() else { return 0 }
        var low: Int64 = 1
        var high: Int64 = Int64(minTime) * Int64(totalTrips)
        let target = Int64(totalTrips)
        
        while low < high {
            let mid = (low + high) / 2
            var trips: Int64 = 0
            for t in time {
                trips += mid / Int64(t)
                if trips >= target { break }
            }
            if trips >= target {
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
    fun minimumTime(time: IntArray, totalTrips: Int): Long {
        var minTime = time[0].toLong()
        for (t in time) {
            if (t.toLong() < minTime) minTime = t.toLong()
        }
        var left = 1L
        var right = minTime * totalTrips.toLong()
        while (left < right) {
            val mid = left + (right - left) / 2
            var trips = 0L
            for (t in time) {
                trips += mid / t
                if (trips >= totalTrips) break
            }
            if (trips >= totalTrips) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int minimumTime(List<int> time, int totalTrips) {
    int minTime = time.reduce((a, b) => a < b ? a : b);
    int left = 0;
    int right = minTime * totalTrips;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      int trips = 0;
      for (int t in time) {
        trips += mid ~/ t;
        if (trips >= totalTrips) break;
      }
      if (trips >= totalTrips) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func minimumTime(time []int, totalTrips int) int64 {
    minT := time[0]
    for _, t := range time {
        if t < minT {
            minT = t
        }
    }
    low, high := int64(1), int64(minT)*int64(totalTrips)
    target := int64(totalTrips)

    for low < high {
        mid := (low + high) / 2
        var trips int64
        for _, t := range time {
            trips += mid / int64(t)
            if trips >= target {
                break
            }
        }
        if trips >= target {
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
def minimum_time(time, total_trips)
  min_t = time.min
  left = 1
  right = min_t * total_trips
  while left < right
    mid = (left + right) / 2
    trips = 0
    time.each do |t|
      trips += mid / t
      break if trips >= total_trips
    end
    if trips >= total_trips
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
    def minimumTime(time: Array[Int], totalTrips: Int): Long = {
        val minT = time.min.toLong
        var left: Long = 0L
        var right: Long = minT * totalTrips
        while (left < right) {
            val mid = left + (right - left) / 2
            var trips: Long = 0L
            var i = 0
            while (i < time.length && trips < totalTrips) {
                trips += mid / time(i)
                i += 1
            }
            if (trips >= totalTrips) right = mid else left = mid + 1
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let min_time = *time.iter().min().unwrap() as i64;
        let target = total_trips as i64;
        let mut left: i64 = 0;
        let mut right: i64 = min_time * target; // maximum possible time

        while left < right {
            let mid = left + (right - left) / 2;
            let mut trips: i64 = 0;
            for &t in &time {
                trips += mid / t as i64;
                if trips >= target {
                    break;
                }
            }
            if trips >= target {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left
    }
}
```

## Racket

```racket
(define/contract (minimum-time time totalTrips)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((min-t (apply min time))
         (low 0)
         (high (* min-t totalTrips)))
    (let loop ((l low) (h high))
      (if (= l h)
          l
          (let* ((mid (quotient (+ l h) 2))
                 (trips (for/sum ([t time]) (quotient mid t))))
            (if (>= trips totalTrips)
                (loop l mid)
                (loop (+ mid 1) h)))))))
```

## Erlang

```erlang
-spec minimum_time(Time :: [integer()], TotalTrips :: integer()) -> integer().
minimum_time(Time, TotalTrips) ->
    Min = lists:min(Time),
    Upper = Min * TotalTrips,
    binary_search(Time, TotalTrips, 1, Upper).

binary_search(_Time, _TotalTrips, Low, High) when Low >= High ->
    Low;
binary_search(Time, TotalTrips, Low, High) ->
    Mid = (Low + High) div 2,
    Trips = total_trips(Time, Mid),
    if
        Trips >= TotalTrips -> binary_search(Time, TotalTrips, Low, Mid);
        true -> binary_search(Time, TotalTrips, Mid + 1, High)
    end.

total_trips(TimeList, T) ->
    total_trips(TimeList, T, 0).

total_trips([], _T, Acc) -> Acc;
total_trips([H|Rest], T, Acc) ->
    total_trips(Rest, T, Acc + (T div H)).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(time :: [integer], total_trips :: integer) :: integer
  def minimum_time(time, total_trips) do
    min_time = Enum.min(time)
    lo = 1
    hi = min_time * total_trips

    binary_search(lo, hi, time, total_trips)
  end

  defp binary_search(lo, hi, time, total_trips) when lo < hi do
    mid = div(lo + hi, 2)

    trips =
      Enum.reduce(time, 0, fn t, acc ->
        acc + div(mid, t)
      end)

    if trips >= total_trips do
      binary_search(lo, mid, time, total_trips)
    else
      binary_search(mid + 1, hi, time, total_trips)
    end
  end

  defp binary_search(lo, _hi, _time, _total_trips), do: lo
end
```
