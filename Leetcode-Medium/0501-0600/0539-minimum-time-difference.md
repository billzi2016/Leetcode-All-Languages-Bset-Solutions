# 0539. Minimum Time Difference

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        const int DAY = 24 * 60;
        vector<bool> seen(DAY, false);
        for (const string& t : timePoints) {
            int h = stoi(t.substr(0, 2));
            int m = stoi(t.substr(3, 2));
            int total = h * 60 + m;
            if (seen[total]) return 0; // duplicate times
            seen[total] = true;
        }
        
        int prev = -1, first = -1, last = -1;
        int ans = INT_MAX;
        for (int i = 0; i < DAY; ++i) {
            if (!seen[i]) continue;
            if (prev != -1) ans = min(ans, i - prev);
            else first = i;
            prev = i;
            last = i;
        }
        // wrap-around difference
        ans = min(ans, DAY - last + first);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findMinDifference(List<String> timePoints) {
        boolean[] seen = new boolean[24 * 60];
        for (String tp : timePoints) {
            int hour = Integer.parseInt(tp.substring(0, 2));
            int minute = Integer.parseInt(tp.substring(3, 5));
            int total = hour * 60 + minute;
            if (seen[total]) {
                return 0; // duplicate time
            }
            seen[total] = true;
        }

        int first = -1, prev = -1, last = -1;
        int minDiff = Integer.MAX_VALUE;

        for (int i = 0; i < seen.length; i++) {
            if (seen[i]) {
                if (first == -1) {
                    first = i;
                }
                if (prev != -1) {
                    minDiff = Math.min(minDiff, i - prev);
                }
                prev = i;
                last = i;
            }
        }

        // circular difference between last and first
        minDiff = Math.min(minDiff, 24 * 60 - last + first);
        return minDiff;
    }
}
```

## Python

```python
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # There are at most 1440 distinct minutes in a day.
        seen = [False] * 1440
        for t in timePoints:
            h = int(t[:2])
            m = int(t[3:])
            total = h * 60 + m
            if seen[total]:
                return 0
            seen[total] = True

        first = -1
        prev = -1
        ans = 1440  # maximum possible difference
        last = -1

        for i in range(1440):
            if seen[i]:
                if first == -1:
                    first = i
                if prev != -1:
                    ans = min(ans, i - prev)
                prev = i
                last = i

        # wrap-around difference between last and first
        ans = min(ans, (first + 1440) - last)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes_present = [False] * 1440
        for tp in timePoints:
            h = int(tp[:2])
            m = int(tp[3:])
            total = h * 60 + m
            if minutes_present[total]:
                return 0
            minutes_present[total] = True

        prev = -1
        first = -1
        last = -1
        ans = 1440  # maximum possible difference is less than 24*60

        for i in range(1440):
            if minutes_present[i]:
                if prev != -1:
                    ans = min(ans, i - prev)
                if first == -1:
                    first = i
                last = i
                prev = i

        # wrap-around difference between the last and first time points
        ans = min(ans, 1440 - last + first)
        return ans
```

## C

```c
#include <limits.h>

int findMinDifference(char** timePoints, int timePointsSize) {
    int seen[1440] = {0};
    for (int i = 0; i < timePointsSize; ++i) {
        char *s = timePoints[i];
        int h = (s[0] - '0') * 10 + (s[1] - '0');
        int m = (s[3] - '0') * 10 + (s[4] - '0');
        int total = h * 60 + m;
        if (seen[total]) return 0;
        seen[total] = 1;
    }
    
    int first = -1, prev = -1, last = -1;
    int ans = INT_MAX;
    for (int i = 0; i < 1440; ++i) {
        if (seen[i]) {
            if (first == -1) first = i;
            if (prev != -1) {
                int diff = i - prev;
                if (diff < ans) ans = diff;
            }
            prev = i;
            last = i;
        }
    }
    
    int wrap = (first + 1440) - last;
    if (wrap < ans) ans = wrap;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMinDifference(IList<string> timePoints) {
        const int DAY = 24 * 60;
        bool[] seen = new bool[DAY];
        foreach (var tp in timePoints) {
            int hour = (tp[0] - '0') * 10 + (tp[1] - '0');
            int minute = (tp[3] - '0') * 10 + (tp[4] - '0');
            int total = hour * 60 + minute;
            if (seen[total]) return 0; // duplicate time
            seen[total] = true;
        }

        int first = -1, prev = -1, last = -1;
        int minDiff = DAY;

        for (int i = 0; i < DAY; i++) {
            if (!seen[i]) continue;
            if (first == -1) first = i;
            if (prev != -1) {
                minDiff = Math.Min(minDiff, i - prev);
            }
            prev = i;
            last = i;
        }

        // wrap‑around difference between the last and first times
        minDiff = Math.Min(minDiff, DAY - last + first);
        return minDiff;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {
    const DAY = 24 * 60;
    const seen = new Array(DAY).fill(false);
    
    for (const tp of timePoints) {
        const h = parseInt(tp.slice(0, 2), 10);
        const m = parseInt(tp.slice(3), 10);
        const mins = h * 60 + m;
        if (seen[mins]) return 0; // duplicate time
        seen[mins] = true;
    }
    
    let prev = -1;
    let first = -1;
    let last = -1;
    let ans = DAY;
    
    for (let i = 0; i < DAY; ++i) {
        if (seen[i]) {
            if (prev !== -1) {
                const diff = i - prev;
                if (diff < ans) ans = diff;
            } else {
                first = i;
            }
            prev = i;
            last = i;
        }
    }
    
    // wrap-around difference between the last and first times
    const wrapDiff = DAY - last + first;
    return Math.min(ans, wrapDiff);
};
```

## Typescript

```typescript
function findMinDifference(timePoints: string[]): number {
    const TOTAL_MINUTES = 24 * 60;
    const seen: boolean[] = new Array(TOTAL_MINUTES).fill(false);
    
    for (const tp of timePoints) {
        const [hStr, mStr] = tp.split(':');
        const mins = parseInt(hStr, 10) * 60 + parseInt(mStr, 10);
        if (seen[mins]) return 0; // duplicate time
        seen[mins] = true;
    }
    
    let first = -1;
    let last = -1;
    let prev = -1;
    let ans = TOTAL_MINUTES; // maximum possible difference
    
    for (let i = 0; i < TOTAL_MINUTES; i++) {
        if (!seen[i]) continue;
        if (first === -1) first = i;
        if (prev !== -1) {
            const diff = i - prev;
            if (diff < ans) ans = diff;
        }
        prev = i;
        last = i;
    }
    
    // circular difference between last and first
    const circularDiff = TOTAL_MINUTES - last + first;
    if (circularDiff < ans) ans = circularDiff;
    
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $timePoints
     * @return Integer
     */
    function findMinDifference($timePoints) {
        $totalMinutes = 24 * 60;
        // Boolean array to mark presence of each minute
        $present = array_fill(0, $totalMinutes, false);
        
        foreach ($timePoints as $tp) {
            [$h, $m] = explode(':', $tp);
            $minutes = intval($h) * 60 + intval($m);
            if ($present[$minutes]) {
                // Duplicate time -> minimum difference is zero
                return 0;
            }
            $present[$minutes] = true;
        }
        
        $prev = -1;
        $first = -1;
        $last = -1;
        $minDiff = PHP_INT_MAX;
        
        for ($i = 0; $i < $totalMinutes; $i++) {
            if ($present[$i]) {
                if ($prev != -1) {
                    $diff = $i - $prev;
                    if ($diff < $minDiff) {
                        $minDiff = $diff;
                    }
                } else {
                    // This is the first time point encountered
                    $first = $i;
                }
                $prev = $i;
                $last = $i;
            }
        }
        
        // Circular difference between last and first times
        $circularDiff = $totalMinutes - $last + $first;
        if ($circularDiff < $minDiff) {
            $minDiff = $circularDiff;
        }
        
        return $minDiff;
    }
}
```

## Swift

```swift
class Solution {
    func findMinDifference(_ timePoints: [String]) -> Int {
        let totalMinutes = 24 * 60
        var seen = [Bool](repeating: false, count: totalMinutes)
        
        for tp in timePoints {
            let parts = tp.split(separator: ":")
            guard parts.count == 2,
                  let hour = Int(parts[0]),
                  let minute = Int(parts[1]) else { continue }
            let minutes = hour * 60 + minute
            if seen[minutes] {
                return 0
            }
            seen[minutes] = true
        }
        
        var first = -1
        var last = -1
        var prev = -1
        var answer = Int.max
        
        for i in 0..<totalMinutes {
            if seen[i] {
                if first == -1 {
                    first = i
                } else {
                    answer = min(answer, i - prev)
                }
                prev = i
                last = i
            }
        }
        
        // wrap around difference between last and first
        let wrapDiff = totalMinutes - last + first
        answer = min(answer, wrapDiff)
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinDifference(timePoints: List<String>): Int {
        val minutesPresent = BooleanArray(24 * 60)
        for (time in timePoints) {
            val mins = ((time[0] - '0') * 10 + (time[1] - '0')) * 60 +
                       ((time[3] - '0') * 10 + (time[4] - '0'))
            if (minutesPresent[mins]) return 0
            minutesPresent[mins] = true
        }

        var first = -1
        var last = -1
        var prev = -1
        var minDiff = Int.MAX_VALUE

        for (i in minutesPresent.indices) {
            if (minutesPresent[i]) {
                if (first == -1) first = i
                if (prev != -1) {
                    val diff = i - prev
                    if (diff < minDiff) minDiff = diff
                }
                prev = i
                last = i
            }
        }

        // wrap-around difference between the last and first time points
        val wrapDiff = 24 * 60 - last + first
        if (wrapDiff < minDiff) minDiff = wrapDiff

        return minDiff
    }
}
```

## Dart

```dart
class Solution {
  int findMinDifference(List<String> timePoints) {
    const int dayMinutes = 24 * 60;
    List<bool> seen = List.filled(dayMinutes, false);

    for (var tp in timePoints) {
      int hour = int.parse(tp.substring(0, 2));
      int minute = int.parse(tp.substring(3, 5));
      int total = hour * 60 + minute;
      if (seen[total]) return 0; // duplicate time
      seen[total] = true;
    }

    int prev = -1;
    int first = -1;
    int last = -1;
    int ans = dayMinutes;

    for (int i = 0; i < dayMinutes; ++i) {
      if (seen[i]) {
        if (prev != -1) {
          int diff = i - prev;
          if (diff < ans) ans = diff;
        } else {
          first = i;
        }
        prev = i;
        last = i;
      }
    }

    // circular difference between last and first
    int circularDiff = dayMinutes - last + first;
    if (circularDiff < ans) ans = circularDiff;

    return ans;
  }
}
```

## Golang

```go
func findMinDifference(timePoints []string) int {
	const dayMinutes = 24 * 60
	seen := make([]bool, dayMinutes)

	for _, t := range timePoints {
		hour := int(t[0]-'0')*10 + int(t[1]-'0')
		minute := int(t[3]-'0')*10 + int(t[4]-'0')
		total := hour*60 + minute
		if seen[total] {
			return 0
		}
		seen[total] = true
	}

	first, prev, last := -1, -1, -1
	minDiff := dayMinutes // maximum possible difference is 1440

	for i := 0; i < dayMinutes; i++ {
		if !seen[i] {
			continue
		}
		if first == -1 {
			first = i
			prev = i
		} else {
			if d := i - prev; d < minDiff {
				minDiff = d
			}
			prev = i
		}
		last = i
	}

	// wrap-around difference between last and first
	if wrap := dayMinutes - last + first; wrap < minDiff {
		minDiff = wrap
	}
	return minDiff
}
```

## Ruby

```ruby
def find_min_difference(time_points)
  minutes_present = Array.new(24 * 60, false)

  time_points.each do |tp|
    h = tp[0..1].to_i
    m = tp[3..4].to_i
    total = h * 60 + m
    return 0 if minutes_present[total]

    minutes_present[total] = true
  end

  prev = nil
  first = nil
  last = nil
  min_diff = 24 * 60

  (0...24 * 60).each do |i|
    next unless minutes_present[i]

    if !prev.nil?
      diff = i - prev
      min_diff = diff if diff < min_diff
    else
      first = i
    end
    prev = i
    last = i
  end

  wrap_diff = (first + 24 * 60) - last
  min_diff = wrap_diff if wrap_diff < min_diff
  min_diff
end
```

## Scala

```scala
object Solution {
  def findMinDifference(timePoints: List[String]): Int = {
    val totalMinutes = 24 * 60
    val present = new Array[Boolean](totalMinutes)

    for (tp <- timePoints) {
      val h = tp.substring(0, 2).toInt
      val m = tp.substring(3, 5).toInt
      val minutes = h * 60 + m
      if (present(minutes)) return 0
      present(minutes) = true
    }

    var first = -1
    var prev = -1
    var last = -1
    var ans = Int.MaxValue

    for (i <- 0 until totalMinutes) {
      if (present(i)) {
        if (first == -1) first = i
        if (prev != -1) {
          val diff = i - prev
          if (diff < ans) ans = diff
        }
        prev = i
        last = i
      }
    }

    val wrapDiff = totalMinutes - last + first
    Math.min(ans, wrapDiff)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        // Boolean bucket for each minute of the day
        let mut seen = [false; 1440];
        for tp in time_points.iter() {
            let b = tp.as_bytes();
            // Parse "HH:MM"
            let hour = (b[0] - b'0') as i32 * 10 + (b[1] - b'0') as i32;
            let minute = (b[3] - b'0') as i32 * 10 + (b[4] - b'0') as i32;
            let total = (hour * 60 + minute) as usize;
            if seen[total] {
                return 0; // duplicate time -> minimum difference is zero
            }
            seen[total] = true;
        }

        let mut prev: Option<usize> = None;
        let mut first = 0usize;
        let mut last = 0usize;
        let mut min_diff = i32::MAX;

        for i in 0..1440 {
            if seen[i] {
                if let Some(p) = prev {
                    let diff = (i - p) as i32;
                    if diff < min_diff {
                        min_diff = diff;
                    }
                } else {
                    first = i; // first occurring time
                }
                prev = Some(i);
                last = i;
            }
        }

        // Account for circular difference between last and first times
        let wrap = (1440 + first - last) as i32;
        if wrap < min_diff {
            min_diff = wrap;
        }

        min_diff
    }
}
```

## Racket

```racket
(define/contract (find-min-difference timePoints)
  (-> (listof string?) exact-integer?)
  (let* ([day-minutes 1440]
         [present (make-vector day-minutes #f)]
         ;; Fill the bucket and detect duplicates
         [duplicate?
          (let loop ((lst timePoints))
            (cond
              [(null? lst) #f]
              [else
               (define s (car lst))
               (define h (string->number (substring s 0 2)))
               (define m (string->number (substring s 3 5)))
               (define total (+ (* h 60) m))
               (if (vector-ref present total)
                   #t
                   (begin
                     (vector-set! present total #t)
                     (loop (cdr lst))))]))])
    (if duplicate?
        0
        ;; Compute the minimal difference
        (let loop ((i 0) (prev -1) (first -1) (last -1) (ans day-minutes))
          (cond
            [(= i day-minutes)
             (define wrap-diff (- (+ day-minutes first) last))
             (min ans wrap-diff)]
            [else
             (if (vector-ref present i)
                 (let* ([new-ans (if (= prev -1) ans (min ans (- i prev)))]
                        [new-first (if (= first -1) i first)]
                        [new-last i])
                   (loop (+ i 1) i new-first new-last new-ans))
                 (loop (+ i 1) prev first last ans))])))))
```

## Erlang

```erlang
-spec find_min_difference(TimePoints :: [unicode:unicode_binary()]) -> integer().
find_min_difference(TimePoints) ->
    Minutes = lists:map(fun parse_time/1, TimePoints),
    Sorted = lists:sort(Minutes),
    case Sorted of
        [] -> 0;
        [First | Rest] ->
            compute_min(Rest, First, First, 1440)
    end.

parse_time(Time) ->
    <<H1, H2, $:, M1, M2>> = Time,
    Hour = (H1 - $0) * 10 + (H2 - $0),
    Min = (M1 - $0) * 10 + (M2 - $0),
    Hour * 60 + Min.

compute_min([], First, Prev, Ans) ->
    Wrap = 1440 - Prev + First,
    erlang:min(Ans, Wrap);
compute_min([Curr | Tail], First, Prev, Ans) ->
    Diff = Curr - Prev,
    NewAns = if Diff < Ans -> Diff; true -> Ans end,
    compute_min(Tail, First, Curr, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_difference(time_points :: [String.t]) :: integer
  def find_min_difference(time_points) do
    # Convert times to minutes while checking for duplicates.
    {duplicate, minutes_rev} =
      Enum.reduce_while(time_points, {false, []}, fn tp, {_dup, acc} ->
        <<h1, h2, ?:, m1, m2>> = tp
        hour = (h1 - ?0) * 10 + (h2 - ?0)
        minute = (m1 - ?0) * 10 + (m2 - ?0)
        total = hour * 60 + minute

        if Enum.member?(acc, total) do
          {:halt, {true, []}}
        else
          {:cont, {false, [total | acc]}}
        end
      end)

    if duplicate do
      0
    else
      minutes = Enum.reverse(minutes_rev)
      sorted = Enum.sort(minutes)

      # Minimum difference between adjacent times.
      {min_adj, _} =
        Enum.reduce(sorted, {1_000_000, nil}, fn val, {cur_min, prev} ->
          if is_nil(prev) do
            {cur_min, val}
          else
            diff = val - prev
            new_min = if diff < cur_min, do: diff, else: cur_min
            {new_min, val}
          end
        end)

      first = hd(sorted)
      last = List.last(sorted)
      wrap = 1440 - last + first

      min(min_adj, wrap)
    end
  end
end
```
