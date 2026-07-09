# 3439. Reschedule Meetings for Maximum Free Time I

## Cpp

```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + (long long)(endTime[i] - startTime[i]);
        }
        long long ans = 0;
        for (int i = k - 1; i < n; ++i) {
            long long left = (i - k >= 0) ? endTime[i - k] : 0LL;
            long long right = (i == n - 1) ? eventTime : startTime[i + 1];
            long long totalDur = pref[i + 1] - pref[i - k + 1];
            long long freeLen = right - left - totalDur;
            if (freeLen > ans) ans = freeLen;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length;
        long windowSum = 0; // sum of durations in current window
        int maxFree = 0;

        for (int i = 0; i < n; i++) {
            windowSum += (long) endTime[i] - startTime[i];

            if (i >= k - 1) {
                long left = (i <= k - 1) ? 0L : endTime[i - k];
                long right = (i == n - 1) ? eventTime : startTime[i + 1];
                long free = right - left - windowSum;
                if (free > maxFree) {
                    maxFree = (int) free;
                }
                // slide the window: remove the earliest meeting in the window
                int outIdx = i - k + 1;
                windowSum -= (long) endTime[outIdx] - startTime[outIdx];
            }
        }

        return maxFree;
    }
}
```

## Python

```python
class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        total_window = 0
        best = 0
        for i in range(n):
            total_window += endTime[i] - startTime[i]
            if i >= k - 1:
                # left boundary of merged free interval
                if i == k - 1:
                    left = 0
                else:
                    left = endTime[i - k]
                # right boundary
                right = eventTime if i == n - 1 else startTime[i + 1]
                best = max(best, right - left - total_window)
                # slide window: remove the earliest meeting in current window
                total_window -= endTime[i - k + 1] - startTime[i - k + 1]
        return max(best, 0)
```

## Python3

```python
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        total_meeting_time = 0
        best = 0
        for i in range(n):
            total_meeting_time += endTime[i] - startTime[i]
            if i >= k - 1:
                # left boundary of merged free interval
                if i <= k - 1:
                    left = 0
                else:
                    left = endTime[i - k]
                # right boundary of merged free interval
                if i == n - 1:
                    right = eventTime
                else:
                    right = startTime[i + 1]
                free = right - left - total_meeting_time
                if free > best:
                    best = free
                # slide window: remove the earliest meeting in current window
                total_meeting_time -= endTime[i - k + 1] - startTime[i - k + 1]
        return best
```

## C

```c
int maxFreeTime(int eventTime, int k, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    int n = startTimeSize;
    long long windowSum = 0; // total duration of meetings in current window
    long long best = 0;
    for (int i = 0; i < n; ++i) {
        windowSum += (long long)endTime[i] - startTime[i];
        if (i >= k - 1) {
            int left = (i >= k) ? endTime[i - k] : 0;
            int right = (i == n - 1) ? eventTime : startTime[i + 1];
            long long freeLen = (long long)right - left - windowSum;
            if (freeLen > best) best = freeLen;
            // slide the window forward
            windowSum -= (long long)endTime[i - k + 1] - startTime[i - k + 1];
        }
    }
    return (int)best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.Length;
        long windowSum = 0; // total duration of meetings in current window
        int maxFree = 0;

        for (int i = 0; i < n; i++) {
            windowSum += (long)endTime[i] - startTime[i];

            if (i >= k - 1) {
                long left = (i <= k - 1) ? 0L : endTime[i - k];
                long right = (i == n - 1) ? eventTime : startTime[i + 1];
                long free = right - left - windowSum;
                if (free > maxFree) {
                    maxFree = (int)free;
                }
                // slide the window: remove the earliest meeting
                int outIdx = i - k + 1;
                windowSum -= (long)endTime[outIdx] - startTime[outIdx];
            }
        }

        return maxFree;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} eventTime
 * @param {number} k
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function(eventTime, k, startTime, endTime) {
    const n = startTime.length;
    let windowSum = 0; // total duration of current window
    let ans = 0;

    for (let i = 0; i < n; ++i) {
        // add current meeting duration
        windowSum += endTime[i] - startTime[i];

        // keep window size at most k
        if (i >= k) {
            windowSum -= endTime[i - k] - startTime[i - k];
        }

        // when we have exactly k meetings in the window
        if (i >= k - 1) {
            const left = (i <= k - 1) ? 0 : endTime[i - k];
            const right = (i === n - 1) ? eventTime : startTime[i + 1];
            const free = right - left - windowSum;
            if (free > ans) ans = free;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxFreeTime(eventTime: number, k: number, startTime: number[], endTime: number[]): number {
    const n = startTime.length;
    let windowSum = 0; // total duration of meetings in current window
    let best = 0;

    for (let i = 0; i < n; ++i) {
        windowSum += endTime[i] - startTime[i];

        if (i >= k - 1) {
            const left = (i <= k - 1) ? 0 : endTime[i - k];
            const right = (i === n - 1) ? eventTime : startTime[i + 1];
            const free = right - left - windowSum;
            if (free > best) best = free;

            // slide the window: remove the earliest meeting in it
            windowSum -= endTime[i - k + 1] - startTime[i - k + 1];
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $eventTime
     * @param Integer $k
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @return Integer
     */
    function maxFreeTime($eventTime, $k, $startTime, $endTime) {
        $n = count($startTime);
        $t = 0; // total duration of meetings in current window
        $max = 0;
        for ($i = 0; $i < $n; ++$i) {
            $t += $endTime[$i] - $startTime[$i];
            if ($i >= $k - 1) {
                // left boundary of merged free interval
                if ($i <= $k - 1) {
                    $left = 0;
                } else {
                    $left = $endTime[$i - $k];
                }
                // right boundary of merged free interval
                if ($i == $n - 1) {
                    $right = $eventTime;
                } else {
                    $right = $startTime[$i + 1];
                }
                $free = $right - $left - $t;
                if ($free > $max) {
                    $max = $free;
                }
                // slide window: remove earliest meeting in the window
                $removeIdx = $i - $k + 1;
                $t -= $endTime[$removeIdx] - $startTime[$removeIdx];
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxFreeTime(_ eventTime: Int, _ k: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        var windowSum = 0
        var answer = 0
        for i in 0..<n {
            windowSum += endTime[i] - startTime[i]
            if i >= k - 1 {
                let left: Int
                if i <= k - 1 {
                    left = 0
                } else {
                    left = endTime[i - k]
                }
                let right: Int
                if i == n - 1 {
                    right = eventTime
                } else {
                    right = startTime[i + 1]
                }
                let free = right - left - windowSum
                if free > answer { answer = free }
                // slide the window
                windowSum -= endTime[i - k + 1] - startTime[i - k + 1]
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFreeTime(eventTime: Int, k: Int, startTime: IntArray, endTime: IntArray): Int {
        val n = startTime.size
        var windowSum = 0L
        var best = 0L
        for (i in 0 until n) {
            windowSum += (endTime[i] - startTime[i]).toLong()
            if (i >= k - 1) {
                val left = if (i <= k - 1) 0 else endTime[i - k]
                val right = if (i == n - 1) eventTime else startTime[i + 1]
                val free = (right - left).toLong() - windowSum
                if (free > best) best = free
                // slide the window
                windowSum -= (endTime[i - k + 1] - startTime[i - k + 1]).toLong()
            }
        }
        return best.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxFreeTime(int eventTime, int k, List<int> startTime, List<int> endTime) {
    int n = startTime.length;
    int totalDuration = 0;
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      totalDuration += endTime[i] - startTime[i];

      if (i >= k) {
        totalDuration -= endTime[i - k] - startTime[i - k];
      }

      if (i >= k - 1) {
        int left = (i <= k - 1) ? 0 : endTime[i - k];
        int right = (i == n - 1) ? eventTime : startTime[i + 1];
        int free = right - left - totalDuration;
        if (free > ans) ans = free;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
    n := len(startTime)
    totalDur := 0
    maxFree := 0

    for i := 0; i < n; i++ {
        dur := endTime[i] - startTime[i]
        totalDur += dur

        if i >= k-1 {
            // left boundary of merged free interval
            var left int
            if i <= k-1 { // i == k-1
                left = 0
            } else {
                left = endTime[i-k]
            }

            // right boundary of merged free interval
            var right int
            if i == n-1 {
                right = eventTime
            } else {
                right = startTime[i+1]
            }

            free := right - left - totalDur
            if free > maxFree {
                maxFree = free
            }

            // slide window: remove earliest meeting in current window
            earlyIdx := i - k + 1
            totalDur -= endTime[earlyIdx] - startTime[earlyIdx]
        }
    }

    return maxFree
}
```

## Ruby

```ruby
def max_free_time(event_time, k, start_time, end_time)
  n = start_time.length
  total_duration = 0
  max_free = 0

  (0...n).each do |i|
    total_duration += end_time[i] - start_time[i]

    if i >= k - 1
      left_boundary = (i <= k - 1) ? 0 : end_time[i - k]
      right_boundary = (i == n - 1) ? event_time : start_time[i + 1]

      free_interval = right_boundary - left_boundary - total_duration
      max_free = free_interval if free_interval > max_free

      # slide window: remove the earliest meeting in current window
      total_duration -= end_time[i - k + 1] - start_time[i - k + 1]
    end
  end

  max_free
end
```

## Scala

```scala
object Solution {
    def maxFreeTime(eventTime: Int, k: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
        val n = startTime.length
        var windowSum: Long = 0L
        var best: Long = 0L

        for (i <- 0 until n) {
            windowSum += (endTime(i) - startTime(i)).toLong

            if (i >= k - 1) {
                val left = if (i <= k - 1) 0 else endTime(i - k)
                val right = if (i == n - 1) eventTime else startTime(i + 1)

                val free = right.toLong - left.toLong - windowSum
                if (free > best) best = free

                // slide the window: remove the earliest meeting in current window
                windowSum -= (endTime(i - k + 1) - startTime(i - k + 1)).toLong
            }
        }

        best.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_free_time(event_time: i32, k: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let k_usize = k as usize;
        let mut window_sum: i64 = 0;
        let mut best: i64 = 0;

        for i in 0..n {
            // add current meeting duration
            window_sum += (end_time[i] - start_time[i]) as i64;

            if i + 1 >= k_usize {
                // left boundary of merged free interval
                let left: i64 = if i < k_usize { 0 } else { end_time[i - k_usize] as i64 };
                // right boundary of merged free interval
                let right: i64 = if i == n - 1 {
                    event_time as i64
                } else {
                    start_time[i + 1] as i64
                };

                let free = right - left - window_sum;
                if free > best {
                    best = free;
                }

                // slide the window: remove the earliest meeting in it
                let rem_idx = i + 1 - k_usize;
                window_sum -= (end_time[rem_idx] - start_time[rem_idx]) as i64;
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (max-free-time eventTime k startTime endTime)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length startTime))
         (st (list->vector startTime))
         (et (list->vector endTime)))
    (let loop ((i 0) (t 0) (ans 0))
      (if (= i n)
          ans
          (let* ((duration (- (vector-ref et i) (vector-ref st i)))
                 (t2 (+ t duration)))
            (if (>= i (- k 1))
                (let* ((left (if (< i k) 0 (vector-ref et (- i k))))
                       (right (if (= i (- n 1)) eventTime (vector-ref st (+ i 1))))
                       (cur (- (- right left) t2))
                       (ans2 (max ans cur))
                       (remove-idx (+ (- i k) 1))
                       (rem-dur (- (vector-ref et remove-idx)
                                   (vector-ref st remove-idx)))
                       (t-next (- t2 rem-dur)))
                  (loop (+ i 1) t-next ans2))
                (loop (+ i 1) t2 ans)))))))
```

## Erlang

```erlang
-spec max_free_time(EventTime :: integer(), K :: integer(), StartTime :: [integer()], EndTime :: [integer()]) -> integer().
max_free_time(EventTime, K, StartTime, EndTime) ->
    N = length(StartTime),
    S = list_to_tuple(StartTime),
    E = list_to_tuple(EndTime),
    Pref = build_prefix(N, S, E),
    compute_max(K - 1, N - 1, EventTime, K, S, E, Pref, 0).

%% Build prefix sum tuple: Pref[0]=0, Pref[i+1]=sum of durations of meetings [0..i]
build_prefix(N, S, E) ->
    build_prefix(0, N, S, E, [0]).

build_prefix(I, N, _S, _E, Acc) when I == N ->
    list_to_tuple(lists:reverse(Acc));
build_prefix(I, N, S, E, Acc) ->
    Dur = element(I + 1, E) - element(I + 1, S),
    Prev = hd(Acc),
    NewSum = Prev + Dur,
    build_prefix(I + 1, N, S, E, [NewSum | Acc]).

%% Retrieve prefix sum at index Idx (0‑based)
pref_at(Pref, Idx) ->
    element(Idx + 1, Pref).

compute_max(I, MaxI, _EventTime, _K, _S, _E, _Pref, Max) when I > MaxI ->
    Max;
compute_max(I, MaxI, EventTime, K, S, E, Pref, Max) ->
    Left = if
        I < K -> 0;
        true -> element((I - K) + 1, E)
    end,
    Right = if
        I == MaxI -> EventTime;
        true -> element(I + 2, S)
    end,
    SumDur = pref_at(Pref, I + 1) - pref_at(Pref, I - K + 1),
    Cand = Right - Left - SumDur,
    NewMax = erlang:max(Max, Cand),
    compute_max(I + 1, MaxI, EventTime, K, S, E, Pref, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_free_time(event_time :: integer, k :: integer, start_time :: [integer], end_time :: [integer]) :: integer
  def max_free_time(event_time, k, start_time, end_time) do
    n = length(start_time)
    start_tup = List.to_tuple(start_time)
    end_tup = List.to_tuple(end_time)

    loop(0, n, k, event_time, start_tup, end_tup, 0, 0)
  end

  defp loop(i, n, _k, _event_time, _start_tup, _end_tup, _t, max) when i == n do
    max
  end

  defp loop(i, n, k, event_time, start_tup, end_tup, t, max) do
    dur = elem(end_tup, i) - elem(start_tup, i)
    t2 = t + dur

    {t3, new_max} =
      if i >= k - 1 do
        left = if i < k, do: 0, else: elem(end_tup, i - k)
        right = if i == n - 1, do: event_time, else: elem(start_tup, i + 1)

        cand = right - left - t2
        max_candidate = if cand > max, do: cand, else: max

        early_idx = i - k + 1
        early_dur = elem(end_tup, early_idx) - elem(start_tup, early_idx)
        {t2 - early_dur, max_candidate}
      else
        {t2, max}
      end

    loop(i + 1, n, k, event_time, start_tup, end_tup, t3, new_max)
  end
end
```
