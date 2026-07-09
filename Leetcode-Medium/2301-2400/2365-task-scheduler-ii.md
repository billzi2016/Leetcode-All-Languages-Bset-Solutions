# 2365. Task Scheduler II

## Cpp

```cpp
class Solution {
public:
    long long taskSchedulerII(std::vector<int>& tasks, int space) {
        std::unordered_map<int, long long> lastDay;
        long long day = 0; // days elapsed
        for (int t : tasks) {
            if (lastDay.find(t) != lastDay.end()) {
                long long earliest = lastDay[t] + (long long)space + 1;
                if (day + 1 < earliest) day = earliest;
                else day += 1;
            } else {
                day += 1;
            }
            lastDay[t] = day;
        }
        return day;
    }
};
```

## Java

```java
class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        java.util.HashMap<Integer, Long> lastDay = new java.util.HashMap<>();
        long day = 1L;
        for (int t : tasks) {
            if (!lastDay.containsKey(t)) {
                lastDay.put(t, day);
                day++;
            } else {
                long earliest = lastDay.get(t) + (long) space + 1L;
                if (day < earliest) {
                    day = earliest;
                }
                lastDay.put(t, day);
                day++;
            }
        }
        return day - 1;
    }
}
```

## Python

```python
class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        last_day = {}
        cur_day = 1
        for t in tasks:
            if t in last_day:
                earliest = last_day[t] + space + 1
                if cur_day < earliest:
                    cur_day = earliest
            last_day[t] = cur_day
            cur_day += 1
        return cur_day - 1
```

## Python3

```python
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {}
        day = 0
        for t in tasks:
            earliest = day + 1
            if t in last_day:
                earliest = max(earliest, last_day[t] + space + 1)
            day = earliest
            last_day[t] = day
        return day
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long key;
    long long val;
    int used;
} Entry;

long long taskSchedulerII(int* tasks, int tasksSize, int space) {
    const int MOD = 262147; // a prime > 2 * 1e5
    Entry *table = (Entry *)calloc(MOD, sizeof(Entry));
    long long curDay = 1;
    
    for (int i = 0; i < tasksSize; ++i) {
        long long t = tasks[i];
        int idx = (unsigned long long)t % MOD;
        while (table[idx].used && table[idx].key != t) {
            idx = (idx + 1) % MOD;
        }
        if (!table[idx].used) {               // first occurrence
            table[idx].key = t;
            table[idx].val = curDay;
            table[idx].used = 1;
            ++curDay;
        } else {                               // seen before
            long long earliest = table[idx].val + (long long)space + 1LL;
            if (curDay < earliest) curDay = earliest;
            table[idx].val = curDay;           // schedule now
            ++curDay;
        }
    }
    
    free(table);
    return curDay - 1;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long TaskSchedulerII(int[] tasks, int space) {
        var lastDay = new Dictionary<int, long>();
        long currentDay = 0;
        foreach (int task in tasks) {
            long earliest = currentDay + 1;
            if (lastDay.TryGetValue(task, out long prev)) {
                long need = prev + space + 1L;
                if (need > earliest) earliest = need;
            }
            currentDay = earliest;
            lastDay[task] = currentDay;
        }
        return currentDay;
    }
}
```

## Javascript

```javascript
var taskSchedulerII = function(tasks, space) {
    const last = new Map();
    let curDay = 0;
    for (const t of tasks) {
        let earliest = last.has(t) ? last.get(t) + space + 1 : 1;
        if (curDay + 1 > earliest) earliest = curDay + 1;
        curDay = earliest;
        last.set(t, curDay);
    }
    return curDay;
};
```

## Typescript

```typescript
function taskSchedulerII(tasks: number[], space: number): number {
    const last = new Map<number, number>();
    let curDay = 0;
    for (const t of tasks) {
        if (!last.has(t)) {
            curDay += 1;
        } else {
            const prev = last.get(t)!;
            const earliest = prev + space + 1;
            curDay = Math.max(curDay + 1, earliest);
        }
        last.set(t, curDay);
    }
    return curDay;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer $space
     * @return Integer
     */
    function taskSchedulerII($tasks, $space) {
        $last = [];
        $curDay = 0;
        foreach ($tasks as $t) {
            if (!array_key_exists($t, $last)) {
                $curDay += 1;
            } else {
                $earliest = $last[$t] + $space + 1;
                if ($curDay + 1 < $earliest) {
                    $curDay = $earliest;
                } else {
                    $curDay += 1;
                }
            }
            $last[$t] = $curDay;
        }
        return $curDay;
    }
}
```

## Swift

```swift
class Solution {
    func taskSchedulerII(_ tasks: [Int], _ space: Int) -> Int {
        var lastDay = [Int: Int]()
        var day = 0
        for t in tasks {
            if let prev = lastDay[t] {
                let allowed = prev + space + 1
                day = max(day + 1, allowed)
            } else {
                day += 1
            }
            lastDay[t] = day
        }
        return day
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun taskSchedulerII(tasks: IntArray, space: Int): Long {
        val lastDay = HashMap<Int, Long>()
        var day = 0L
        val gap = space.toLong()
        for (t in tasks) {
            val prev = lastDay[t]
            day = if (prev == null) {
                day + 1
            } else {
                maxOf(prev + gap + 1, day + 1)
            }
            lastDay[t] = day
        }
        return day
    }
}
```

## Dart

```dart
class Solution {
  int taskSchedulerII(List<int> tasks, int space) {
    final Map<int, int> last = {};
    int day = 0;
    for (final t in tasks) {
      if (!last.containsKey(t)) {
        day += 1;
      } else {
        final int earliest = last[t]! + space + 1;
        final int nextDay = day + 1;
        day = nextDay > earliest ? nextDay : earliest;
      }
      last[t] = day;
    }
    return day;
  }
}
```

## Golang

```go
func taskSchedulerII(tasks []int, space int) int64 {
    last := make(map[int]int64)
    var cur int64 = 1
    s := int64(space)
    for _, t := range tasks {
        if ld, ok := last[t]; ok {
            earliest := ld + s + 1
            if cur < earliest {
                cur = earliest
            }
        }
        last[t] = cur
        cur++
    }
    return cur - 1
}
```

## Ruby

```ruby
def task_scheduler_ii(tasks, space)
  last_day = {}
  current_day = 1
  tasks.each do |t|
    if last_day.key?(t)
      earliest = last_day[t] + space + 1
      scheduled = current_day > earliest ? current_day : earliest
      last_day[t] = scheduled
      current_day = scheduled + 1
    else
      last_day[t] = current_day
      current_day += 1
    end
  end
  current_day - 1
end
```

## Scala

```scala
object Solution {
  def taskSchedulerII(tasks: Array[Int], space: Int): Long = {
    val last = scala.collection.mutable.Map[Int, Long]()
    var day: Long = 0L
    val gap = space.toLong + 1L
    for (t <- tasks) {
      var nextDay = day + 1L
      if (last.contains(t)) {
        val allowed = last(t) + gap
        if (allowed > nextDay) nextDay = allowed
      }
      day = nextDay
      last.update(t, day)
    }
    day
  }
}
```

## Rust

```rust
impl Solution {
    pub fn task_scheduler_ii(tasks: Vec<i32>, space: i32) -> i64 {
        use std::collections::HashMap;
        let mut last_day: HashMap<i32, i64> = HashMap::new();
        let mut day: i64 = 0;
        let s = space as i64;
        for t in tasks {
            if let Some(&prev) = last_day.get(&t) {
                let earliest = prev + s + 1;
                day = std::cmp::max(day + 1, earliest);
            } else {
                day += 1;
            }
            last_day.insert(t, day);
        }
        day
    }
}
```

## Racket

```racket
(define/contract (task-scheduler-ii tasks space)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([last-day (make-hash)])
    (let loop ((remaining tasks) (day 0))
      (if (null? remaining)
          day
          (let* ((t (car remaining))
                 (prev (hash-ref last-day t #f)))
            (if prev
                (let* ((earliest (+ prev space 1))
                       (next-day (add1 day)))
                  (if (>= next-day earliest)
                      (begin
                        (hash-set! last-day t next-day)
                        (loop (cdr remaining) next-day))
                      (begin
                        (hash-set! last-day t earliest)
                        (loop (cdr remaining) earliest))))
                (let ((next-day (add1 day)))
                  (hash-set! last-day t next-day)
                  (loop (cdr remaining) next-day))))))))
```

## Erlang

```erlang
-spec task_scheduler_ii(Tasks :: [integer()], Space :: integer()) -> integer().
task_scheduler_ii(Tasks, Space) ->
    task_sched(Tasks, Space, 0, #{}).

task_sched([], _Space, Day, _Map) ->
    Day;
task_sched([T | Rest], Space, CurrDay, Map) ->
    case maps:find(T, Map) of
        error ->
            NewDay = CurrDay + 1,
            NewMap = maps:put(T, NewDay, Map),
            task_sched(Rest, Space, NewDay, NewMap);
        {ok, LastDay} ->
            Earliest = LastDay + Space + 1,
            NewDay = erlang:max(CurrDay + 1, Earliest),
            NewMap = maps:put(T, NewDay, Map),
            task_sched(Rest, Space, NewDay, NewMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec task_scheduler_ii(tasks :: [integer], space :: integer) :: integer
  def task_scheduler_ii(tasks, space) do
    {day, _} =
      Enum.reduce(tasks, {0, %{}}, fn task, {day, last} ->
        case Map.fetch(last, task) do
          :error ->
            new_day = day + 1
            {new_day, Map.put(last, task, new_day)}

          {:ok, prev} ->
            earliest = prev + space + 1
            new_day = max(day + 1, earliest)
            {new_day, Map.put(last, task, new_day)}
        end
      end)

    day
  end
end
```
