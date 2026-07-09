# 3386. Button with Longest Push Time

## Cpp

```cpp
class Solution {
public:
    int buttonWithLongestTime(vector<vector<int>>& events) {
        int bestIdx = -1;
        int maxDuration = -1;
        int prevTime = 0;
        for (const auto& e : events) {
            int idx = e[0];
            int time = e[1];
            int duration = time - prevTime;
            if (duration > maxDuration || (duration == maxDuration && idx < bestIdx)) {
                maxDuration = duration;
                bestIdx = idx;
            }
            prevTime = time;
        }
        return bestIdx;
    }
};
```

## Java

```java
class Solution {
    public int buttonWithLongestTime(int[][] events) {
        int prevTime = 0;
        int maxDuration = -1;
        int answerIdx = Integer.MAX_VALUE;
        for (int[] e : events) {
            int idx = e[0];
            int time = e[1];
            int duration = time - prevTime;
            if (duration > maxDuration || (duration == maxDuration && idx < answerIdx)) {
                maxDuration = duration;
                answerIdx = idx;
            }
            prevTime = time;
        }
        return answerIdx;
    }
}
```

## Python

```python
class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        n = len(events)
        next_time = {}
        max_duration = -1
        result_index = None

        for i in range(n - 1, -1, -1):
            idx, t = events[i]
            if idx in next_time:
                duration = next_time[idx] - t
            else:
                if i + 1 < n:
                    duration = events[i + 1][1] - t
                else:
                    duration = 0
            next_time[idx] = t

            if duration > max_duration or (duration == max_duration and (result_index is None or idx < result_index)):
                max_duration = duration
                result_index = idx

        return result_index
```

## Python3

```python
class Solution:
    def buttonWithLongestTime(self, events):
        last_time = events[-1][1]
        next_time = {}
        best_idx = None
        best_len = -1

        for idx, t in reversed(events):
            if idx in next_time:
                duration = next_time[idx] - t
            else:
                duration = last_time - t

            if duration > best_len or (duration == best_len and (best_idx is None or idx < best_idx)):
                best_len = duration
                best_idx = idx

            next_time[idx] = t

        return best_idx
```

## C

```c
#include <limits.h>

int buttonWithLongestTime(int** events, int eventsSize, int* eventsColSize) {
    int prev_time = 0;
    int max_duration = -1;
    int answer = INT_MAX;

    for (int i = 0; i < eventsSize; ++i) {
        int idx = events[i][0];
        int time = events[i][1];
        int duration = time - prev_time;

        if (duration > max_duration || (duration == max_duration && idx < answer)) {
            max_duration = duration;
            answer = idx;
        }
        prev_time = time;
    }

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int ButtonWithLongestTime(int[][] events) {
        int prevTime = 0;
        int maxDiff = -1;
        int resultIdx = int.MaxValue;

        foreach (var e in events) {
            int idx = e[0];
            int time = e[1];
            int diff = time - prevTime;

            if (diff > maxDiff || (diff == maxDiff && idx < resultIdx)) {
                maxDiff = diff;
                resultIdx = idx;
            }

            prevTime = time;
        }

        return resultIdx;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var buttonWithLongestTime = function(events) {
    let prevTime = 0;
    let maxDuration = -1;
    let answerIndex = Infinity;
    
    for (const [idx, time] of events) {
        const duration = time - prevTime;
        if (duration > maxDuration || (duration === maxDuration && idx < answerIndex)) {
            maxDuration = duration;
            answerIndex = idx;
        }
        prevTime = time;
    }
    
    return answerIndex;
};
```

## Typescript

```typescript
function buttonWithLongestTime(events: number[][]): number {
    let prevTime = 0;
    let maxDuration = -1;
    let resultIndex = Number.MAX_SAFE_INTEGER;

    for (const [idx, time] of events) {
        const duration = time - prevTime;
        if (duration > maxDuration || (duration === maxDuration && idx < resultIndex)) {
            maxDuration = duration;
            resultIndex = idx;
        }
        prevTime = time;
    }

    return resultIndex;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function buttonWithLongestTime($events) {
        $prevTime = 0;
        $maxDuration = -1;
        $answer = null;

        foreach ($events as $event) {
            $index = $event[0];
            $time = $event[1];
            $duration = $time - $prevTime;

            if ($duration > $maxDuration || ($duration == $maxDuration && $index < $answer)) {
                $maxDuration = $duration;
                $answer = $index;
            }

            $prevTime = $time;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func buttonWithLongestTime(_ events: [[Int]]) -> Int {
        var maxDuration = 0
        var answer = Int.max
        var prevTime = 0
        
        for e in events {
            let index = e[0]
            let time = e[1]
            let duration = time - prevTime
            if duration > maxDuration || (duration == maxDuration && index < answer) {
                maxDuration = duration
                answer = index
            }
            prevTime = time
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buttonWithLongestTime(events: Array<IntArray>): Int {
        var prevTime = 0
        var maxDuration = -1
        var answer = -1
        for (event in events) {
            val index = event[0]
            val time = event[1]
            val duration = time - prevTime
            if (duration > maxDuration || (duration == maxDuration && index < answer)) {
                maxDuration = duration
                answer = index
            }
            prevTime = time
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int buttonWithLongestTime(List<List<int>> events) {
    int prevTime = 0;
    int maxDuration = -1;
    int answerIndex = 0;

    for (var event in events) {
      int index = event[0];
      int time = event[1];
      int duration = time - prevTime;

      if (duration > maxDuration ||
          (duration == maxDuration && index < answerIndex)) {
        maxDuration = duration;
        answerIndex = index;
      }

      prevTime = time;
    }

    return answerIndex;
  }
}
```

## Golang

```go
func buttonWithLongestTime(events [][]int) int {
	if len(events) == 0 {
		return 0
	}
	maxDur := events[0][1]
	ans := events[0][0]
	prevTime := events[0][1]

	for i := 1; i < len(events); i++ {
		idx, t := events[i][0], events[i][1]
		dur := t - prevTime
		if dur > maxDur || (dur == maxDur && idx < ans) {
			maxDur = dur
			ans = idx
		}
		prevTime = t
	}
	return ans
}
```

## Ruby

```ruby
def button_with_longest_time(events)
  prev_time = 0
  best_index = nil
  best_duration = -1

  events.each do |index, time|
    duration = time - prev_time
    if duration > best_duration || (duration == best_duration && index < best_index)
      best_duration = duration
      best_index = index
    end
    prev_time = time
  end

  best_index
end
```

## Scala

```scala
object Solution {
    def buttonWithLongestTime(events: Array[Array[Int]]): Int = {
        var prevTime = 0
        var bestIdx = -1
        var bestDur = -1

        for (e <- events) {
            val idx = e(0)
            val time = e(1)
            val dur = time - prevTime
            if (dur > bestDur || (dur == bestDur && idx < bestIdx)) {
                bestDur = dur
                bestIdx = idx
            }
            prevTime = time
        }

        bestIdx
    }
}
```

## Rust

```rust
impl Solution {
    pub fn button_with_longest_time(events: Vec<Vec<i32>>) -> i32 {
        let mut prev_time = 0;
        let mut best_index = 0;
        let mut best_duration = -1;
        for ev in events.iter() {
            let idx = ev[0];
            let time = ev[1];
            let duration = time - prev_time;
            if duration > best_duration || (duration == best_duration && idx < best_index) {
                best_duration = duration;
                best_index = idx;
            }
            prev_time = time;
        }
        best_index
    }
}
```

## Racket

```racket
(define/contract (button-with-longest-time events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let loop ((remaining events) (prev-time 0) (max-dur -1) (best-index 0))
    (if (null? remaining)
        best-index
        (let* ((pair (car remaining))
               (idx (first pair))
               (time (second pair))
               (dur (- time prev-time)))
          (cond
            [(> dur max-dur)
             (loop (cdr remaining) time dur idx)]
            [(and (= dur max-dur) (< idx best-index))
             (loop (cdr remaining) time max-dur idx)]
            [else
             (loop (cdr remaining) time max-dur best-index)])))))
```

## Erlang

```erlang
-module(solution).
-export([button_with_longest_time/1]).

-spec button_with_longest_time(Events :: [[integer()]]) -> integer().
button_with_longest_time([]) ->
    0; % not expected per constraints
button_with_longest_time([First|Rest]) ->
    [Idx0, Time0] = First,
    process(Rest, Time0, Time0, Idx0).

-spec process([[integer()]], integer(), integer(), integer()) -> integer().
process([], _PrevTime, _MaxDur, Ans) ->
    Ans;
process([[Idx, Time]|Tail], PrevTime, MaxDur, Ans) ->
    Dur = Time - PrevTime,
    {NewMax, NewAns} =
        if
            Dur > MaxDur ->
                {Dur, Idx};
            Dur == MaxDur, Idx < Ans ->
                {MaxDur, Idx};
            true ->
                {MaxDur, Ans}
        end,
    process(Tail, Time, NewMax, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec button_with_longest_time(events :: [[integer]]) :: integer
  def button_with_longest_time(events) do
    {best_idx, _max_dur, _prev_t} =
      Enum.reduce(events, {0, -1, 0}, fn [idx, t], {cur_best, cur_max, prev_t} ->
        dur = t - prev_t

        if dur > cur_max or (dur == cur_max and idx < cur_best) do
          {idx, dur, t}
        else
          {cur_best, cur_max, t}
        end
      end)

    best_idx
  end
end
```
