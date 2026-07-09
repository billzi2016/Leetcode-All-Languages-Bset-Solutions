# 2432. The Employee That Worked on the Longest Task

## Cpp

```cpp
class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) {
        int prev = 0;
        int bestId = -1;
        int maxDur = -1;
        for (const auto& log : logs) {
            int id = log[0];
            int leave = log[1];
            int dur = leave - prev;
            if (dur > maxDur || (dur == maxDur && id < bestId)) {
                maxDur = dur;
                bestId = id;
            }
            prev = leave;
        }
        return bestId;
    }
};
```

## Java

```java
class Solution {
    public int hardestWorker(int n, int[][] logs) {
        int prev = 0;
        int maxDuration = -1;
        int employeeId = Integer.MAX_VALUE;
        for (int[] log : logs) {
            int id = log[0];
            int leave = log[1];
            int duration = leave - prev;
            if (duration > maxDuration || (duration == maxDuration && id < employeeId)) {
                maxDuration = duration;
                employeeId = id;
            }
            prev = leave;
        }
        return employeeId;
    }
}
```

## Python

```python
class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        max_time = -1
        ans = 0
        prev = 0
        for emp_id, leave in logs:
            duration = leave - prev
            if duration > max_time or (duration == max_time and emp_id < ans):
                max_time = duration
                ans = emp_id
            prev = leave
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = -1
        employee_id = 0
        prev_leave = 0
        for emp, leave in logs:
            duration = leave - prev_leave
            if duration > max_time or (duration == max_time and emp < employee_id):
                max_time = duration
                employee_id = emp
            prev_leave = leave
        return employee_id
```

## C

```c
#include <limits.h>

int hardestWorker(int n, int** logs, int logsSize, int* logsColSize) {
    int prev = 0;
    int maxDur = -1;
    int ans = INT_MAX;
    for (int i = 0; i < logsSize; ++i) {
        int id = logs[i][0];
        int leave = logs[i][1];
        int dur = leave - prev;
        if (dur > maxDur || (dur == maxDur && id < ans)) {
            maxDur = dur;
            ans = id;
        }
        prev = leave;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int HardestWorker(int n, int[][] logs) {
        int previousLeave = 0;
        int maxDuration = -1;
        int resultId = 0;

        foreach (var log in logs) {
            int employeeId = log[0];
            int leaveTime = log[1];
            int duration = leaveTime - previousLeave;

            if (duration > maxDuration || (duration == maxDuration && employeeId < resultId)) {
                maxDuration = duration;
                resultId = employeeId;
            }

            previousLeave = leaveTime;
        }

        return resultId;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} logs
 * @return {number}
 */
var hardestWorker = function(n, logs) {
    let maxDuration = -1;
    let resultId = 0;
    let prevLeave = 0;
    
    for (const [id, leave] of logs) {
        const duration = leave - prevLeave;
        if (duration > maxDuration || (duration === maxDuration && id < resultId)) {
            maxDuration = duration;
            resultId = id;
        }
        prevLeave = leave;
    }
    
    return resultId;
};
```

## Typescript

```typescript
function hardestWorker(n: number, logs: number[][]): number {
    let maxTime = -1;
    let result = 0;
    let prevLeave = 0;
    for (const [id, leave] of logs) {
        const duration = leave - prevLeave;
        if (duration > maxTime || (duration === maxTime && id < result)) {
            maxTime = duration;
            result = id;
        }
        prevLeave = leave;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $logs
     * @return Integer
     */
    function hardestWorker($n, $logs) {
        $prev = 0;
        $maxTime = -1;
        $ans = PHP_INT_MAX;

        foreach ($logs as $log) {
            $id = $log[0];
            $leave = $log[1];
            $duration = $leave - $prev;

            if ($duration > $maxTime || ($duration == $maxTime && $id < $ans)) {
                $maxTime = $duration;
                $ans = $id;
            }

            $prev = $leave;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func hardestWorker(_ n: Int, _ logs: [[Int]]) -> Int {
        var previousLeave = 0
        var maxDuration = -1
        var resultId = 0
        
        for log in logs {
            let id = log[0]
            let leaveTime = log[1]
            let duration = leaveTime - previousLeave
            
            if duration > maxDuration || (duration == maxDuration && id < resultId) {
                maxDuration = duration
                resultId = id
            }
            
            previousLeave = leaveTime
        }
        
        return resultId
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hardestWorker(n: Int, logs: Array<IntArray>): Int {
        var prevLeave = 0
        var maxDuration = -1
        var resultId = 0
        for (log in logs) {
            val id = log[0]
            val leave = log[1]
            val duration = leave - prevLeave
            if (duration > maxDuration || (duration == maxDuration && id < resultId)) {
                maxDuration = duration
                resultId = id
            }
            prevLeave = leave
        }
        return resultId
    }
}
```

## Dart

```dart
class Solution {
  int hardestWorker(int n, List<List<int>> logs) {
    int prevLeave = 0;
    int maxDuration = -1;
    int employeeId = -1;

    for (var log in logs) {
      int id = log[0];
      int leaveTime = log[1];
      int duration = leaveTime - prevLeave;

      if (duration > maxDuration || (duration == maxDuration && id < employeeId)) {
        maxDuration = duration;
        employeeId = id;
      }

      prevLeave = leaveTime;
    }

    return employeeId;
  }
}
```

## Golang

```go
func hardestWorker(n int, logs [][]int) int {
    maxDur := 0
    ans := 0
    prev := 0
    for _, log := range logs {
        id := log[0]
        leave := log[1]
        dur := leave - prev
        if dur > maxDur || (dur == maxDur && id < ans) {
            maxDur = dur
            ans = id
        }
        prev = leave
    }
    return ans
}
```

## Ruby

```ruby
def hardest_worker(n, logs)
  max_time = -1
  answer = n
  prev_leave = 0
  logs.each do |id, leave|
    duration = leave - prev_leave
    if duration > max_time || (duration == max_time && id < answer)
      max_time = duration
      answer = id
    end
    prev_leave = leave
  end
  answer
end
```

## Scala

```scala
object Solution {
    def hardestWorker(n: Int, logs: Array[Array[Int]]): Int = {
        var maxDuration = -1
        var resultId = 0
        var prevLeave = 0
        for (log <- logs) {
            val id = log(0)
            val leave = log(1)
            val duration = leave - prevLeave
            if (duration > maxDuration || (duration == maxDuration && id < resultId)) {
                maxDuration = duration
                resultId = id
            }
            prevLeave = leave
        }
        resultId
    }
}
```

## Rust

```rust
impl Solution {
    pub fn hardest_worker(n: i32, logs: Vec<Vec<i32>>) -> i32 {
        let mut prev = 0;
        let mut max_dur = -1;
        let mut ans = 0;
        for log in logs.iter() {
            let id = log[0];
            let leave = log[1];
            let dur = leave - prev;
            if dur > max_dur || (dur == max_dur && id < ans) {
                max_dur = dur;
                ans = id;
            }
            prev = leave;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (hardest-worker n logs)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let loop ((prev 0) (max-dur -1) (best-id 0) (remaining logs))
    (if (null? remaining)
        best-id
        (let* ((entry (car remaining))
               (id (first entry))
               (leave (second entry))
               (dur (- leave prev)))
          (cond [(> dur max-dur) (loop leave dur id (cdr remaining))]
                [(and (= dur max-dur) (< id best-id)) (loop leave max-dur id (cdr remaining))]
                [else (loop leave max-dur best-id (cdr remaining))])))))
```

## Erlang

```erlang
-spec hardest_worker(N :: integer(), Logs :: [[integer()]]) -> integer().
hardest_worker(_N, Logs) ->
    {_, _, Answer} = lists:foldl(
        fun([Id, Leave], {PrevLeave, MaxDur, CurAns}) ->
            Dur = Leave - PrevLeave,
            case Dur > MaxDur of
                true ->
                    {Leave, Dur, Id};
                false ->
                    case (Dur == MaxDur) andalso (Id < CurAns) of
                        true -> {Leave, MaxDur, Id};
                        false -> {Leave, MaxDur, CurAns}
                    end
            end
        end,
        {0, -1, 0},
        Logs),
    Answer.
```

## Elixir

```elixir
defmodule Solution do
  @spec hardest_worker(n :: integer, logs :: [[integer]]) :: integer
  def hardest_worker(_n, logs) do
    {_, _, ans} =
      Enum.reduce(logs, {0, -1, 0}, fn [id, leave], {prev, max_dur, best_id} ->
        dur = leave - prev

        cond do
          dur > max_dur -> {leave, dur, id}
          dur == max_dur and id < best_id -> {leave, max_dur, id}
          true -> {leave, max_dur, best_id}
        end
      end)

    ans
  end
end
```
