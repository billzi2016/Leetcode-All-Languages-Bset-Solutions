# 2589. Minimum Time to Complete All Tasks

## Cpp

```cpp
class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        // Sort tasks by their ending time
        sort(tasks.begin(), tasks.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[1] != b[1]) return a[1] < b[1];
                 return a[0] < b[0];
             });
        
        const int MAX_TIME = 2000;
        vector<char> used(MAX_TIME + 2, 0); // 1-indexed time points
        int totalOn = 0;
        
        for (const auto& task : tasks) {
            int start = task[0];
            int end   = task[1];
            int dur   = task[2];
            
            // Count already scheduled seconds within [start, end]
            int have = 0;
            for (int t = start; t <= end; ++t) {
                if (used[t]) ++have;
            }
            
            int need = dur - have;
            // Schedule needed seconds as late as possible
            for (int t = end; t >= start && need > 0; --t) {
                if (!used[t]) {
                    used[t] = 1;
                    ++totalOn;
                    --need;
                }
            }
        }
        
        return totalOn;
    }
};
```

## Java

```java
class Solution {
    public int findMinimumTime(int[][] tasks) {
        java.util.Arrays.sort(tasks, (a, b) -> Integer.compare(a[1], b[1]));
        boolean[] on = new boolean[2002]; // indices up to 2000
        int total = 0;
        for (int[] task : tasks) {
            int start = task[0];
            int end = task[1];
            int dur = task[2];
            int already = 0;
            for (int t = start; t <= end; ++t) {
                if (on[t]) already++;
            }
            int need = dur - already;
            for (int t = end; need > 0 && t >= start; --t) {
                if (!on[t]) {
                    on[t] = true;
                    total++;
                    need--;
                }
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # sort by end time
        tasks.sort(key=lambda x: x[1])
        max_time = 0
        for s, e, _ in tasks:
            if e > max_time:
                max_time = e

        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, idx, val):
                while idx <= self.n:
                    self.bit[idx] += val
                    idx += idx & -idx

            def sum(self, idx):
                res = 0
                while idx > 0:
                    res += self.bit[idx]
                    idx -= idx & -idx
                return res

        bit = BIT(max_time)
        used = [False] * (max_time + 1)  # 1-indexed

        for start, end, dur in tasks:
            already = bit.sum(end) - bit.sum(start - 1)
            need = dur - already
            pos = end
            while need > 0 and pos >= start:
                if not used[pos]:
                    used[pos] = True
                    bit.add(pos, 1)
                    need -= 1
                pos -= 1

        return bit.sum(max_time)
```

## Python3

```python
from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Sort tasks by their end time (greedy order)
        tasks.sort(key=lambda x: x[1])
        max_end = max(t[1] for t in tasks)
        used = [False] * (max_end + 2)   # index from 0..max_end
        total_on = 0

        for start, end, duration in tasks:
            # Count already selected seconds within the interval
            already = 0
            for t in range(start, end + 1):
                if used[t]:
                    already += 1

            need = duration - already
            if need <= 0:
                continue

            # Add needed seconds as late as possible
            for t in range(end, start - 1, -1):
                if not used[t]:
                    used[t] = True
                    total_on += 1
                    need -= 1
                    if need == 0:
                        break

        return total_on
```

## C

```c
#include <stdlib.h>

typedef struct {
    int s;
    int e;
    int d;
} Task;

static int cmpTask(const void *a, const void *b) {
    const Task *ta = (const Task *)a;
    const Task *tb = (const Task *)b;
    if (ta->e != tb->e) return ta->e - tb->e;
    return ta->s - tb->s;
}

int findMinimumTime(int** tasks, int tasksSize, int* tasksColSize){
    Task *arr = (Task*)malloc(sizeof(Task) * tasksSize);
    for (int i = 0; i < tasksSize; ++i) {
        arr[i].s = tasks[i][0];
        arr[i].e = tasks[i][1];
        arr[i].d = tasks[i][2];
    }
    
    qsort(arr, tasksSize, sizeof(Task), cmpTask);
    
    int on[2001] = {0};   // time points are 1..2000
    int total = 0;
    
    for (int i = 0; i < tasksSize; ++i) {
        Task t = arr[i];
        int already = 0;
        for (int tm = t.s; tm <= t.e; ++tm) {
            if (on[tm]) already++;
        }
        int need = t.d - already;
        for (int tm = t.e; need > 0 && tm >= t.s; --tm) {
            if (!on[tm]) {
                on[tm] = 1;
                total++;
                need--;
            }
        }
    }
    
    free(arr);
    return total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int FindMinimumTime(int[][] tasks) {
        Array.Sort(tasks, (a, b) => a[1].CompareTo(b[1]));
        int maxEnd = 0;
        foreach (var t in tasks) if (t[1] > maxEnd) maxEnd = t[1];
        bool[] on = new bool[maxEnd + 2];
        int total = 0;
        foreach (var task in tasks) {
            int l = task[0], r = task[1], d = task[2];
            int have = 0;
            for (int t = l; t <= r; ++t)
                if (on[t]) have++;
            int need = d - have;
            for (int t = r; t >= l && need > 0; --t) {
                if (!on[t]) {
                    on[t] = true;
                    total++;
                    need--;
                }
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var findMinimumTime = function(tasks) {
    // sort by end time ascending
    tasks.sort((a, b) => a[1] - b[1]);
    const MAX_TIME = 2000;
    const on = new Array(MAX_TIME + 2).fill(false);
    let total = 0;
    
    for (const [start, end, dur] of tasks) {
        // count already scheduled seconds within the interval
        let have = 0;
        for (let t = start; t <= end; ++t) {
            if (on[t]) have++;
        }
        let need = dur - have;
        // schedule remaining needed seconds as late as possible
        for (let t = end; need > 0 && t >= start; --t) {
            if (!on[t]) {
                on[t] = true;
                total++;
                need--;
            }
        }
    }
    
    return total;
};
```

## Typescript

```typescript
function findMinimumTime(tasks: number[][]): number {
    // Sort tasks by their end time (ascending)
    tasks.sort((a, b) => a[1] - b[1]);

    // Determine the maximum time point needed for array size
    let maxEnd = 0;
    for (const t of tasks) {
        if (t[1] > maxEnd) maxEnd = t[1];
    }

    const on: boolean[] = new Array(maxEnd + 2).fill(false);

    for (const [start, end, duration] of tasks) {
        // Count already turned‑on seconds within the interval
        let have = 0;
        for (let t = start; t <= end; ++t) {
            if (on[t]) have++;
        }

        let need = duration - have;
        // Turn on additional seconds as late as possible
        for (let t = end; need > 0 && t >= start; --t) {
            if (!on[t]) {
                on[t] = true;
                need--;
            }
        }
    }

    // Total turned‑on time
    let total = 0;
    for (let t = 1; t <= maxEnd; ++t) {
        if (on[t]) total++;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function findMinimumTime($tasks) {
        // Sort tasks by end time ascending
        usort($tasks, function($a, $b) {
            if ($a[1] == $b[1]) {
                return $a[0] <=> $b[0];
            }
            return $a[1] <=> $b[1];
        });

        // Maximum possible time based on constraints (2000)
        $maxTime = 2000;
        $used = array_fill(0, $maxTime + 2, false);
        $answer = 0;

        foreach ($tasks as $task) {
            [$start, $end, $duration] = $task;
            // Count already selected times within [start, end]
            $already = 0;
            for ($t = $start; $t <= $end; $t++) {
                if ($used[$t]) {
                    $already++;
                }
            }

            $need = $duration - $already;
            // Add needed times as late as possible
            for ($t = $end; $need > 0 && $t >= $start; $t--) {
                if (!$used[$t]) {
                    $used[$t] = true;
                    $answer++;
                    $need--;
                }
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func findMinimumTime(_ tasks: [[Int]]) -> Int {
        // Sort tasks by their end time (ascending)
        let sortedTasks = tasks.sorted { $0[1] < $1[1] }
        // Time points are in [1, 2000]; use an extra slot for safety
        var on = Array(repeating: false, count: 2002)
        var totalOnTime = 0
        
        for task in sortedTasks {
            let start = task[0]
            let end = task[1]
            let duration = task[2]
            
            // Count already turned‑on seconds within the interval
            var alreadyOn = 0
            if start <= end {
                for t in start...end where on[t] {
                    alreadyOn += 1
                }
            }
            
            var need = duration - alreadyOn
            var time = end
            // Turn on the latest possible seconds until requirement is met
            while need > 0 && time >= start {
                if !on[time] {
                    on[time] = true
                    totalOnTime += 1
                    need -= 1
                }
                time -= 1
            }
        }
        
        return totalOnTime
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinimumTime(tasks: Array<IntArray>): Int {
        val sorted = tasks.sortedWith(compareBy<IntArray> { it[1] }.thenBy { it[0] })
        val maxTime = 2000
        val on = BooleanArray(maxTime + 2)
        var total = 0
        for (task in sorted) {
            val start = task[0]
            val end = task[1]
            val dur = task[2]
            var already = 0
            for (t in start..end) {
                if (on[t]) already++
            }
            var need = dur - already
            var t = end
            while (need > 0 && t >= start) {
                if (!on[t]) {
                    on[t] = true
                    total++
                    need--
                }
                t--
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int findMinimumTime(List<List<int>> tasks) {
    // Sort tasks by their end time
    tasks.sort((a, b) => a[1].compareTo(b[1]));

    // Determine the maximum time point needed for array size
    int maxEnd = 0;
    for (var t in tasks) {
      if (t[1] > maxEnd) maxEnd = t[1];
    }

    // Boolean array indicating whether the computer is on at each second
    List<bool> on = List.filled(maxEnd + 2, false);
    int totalOn = 0;

    for (var task in tasks) {
      int start = task[0];
      int end = task[1];
      int dur = task[2];

      // Count already selected seconds within the interval
      int have = 0;
      for (int i = start; i <= end; i++) {
        if (on[i]) have++;
      }

      int need = dur - have;
      if (need <= 0) continue;

      // Turn on the computer at the latest possible unused seconds
      for (int i = end; i >= start && need > 0; i--) {
        if (!on[i]) {
          on[i] = true;
          totalOn++;
          need--;
        }
      }
    }

    return totalOn;
  }
}
```

## Golang

```go
package main

import "sort"

func findMinimumTime(tasks [][]int) int {
	// Sort tasks by increasing end time
	sort.Slice(tasks, func(i, j int) bool {
		if tasks[i][1] == tasks[j][1] {
			return tasks[i][0] < tasks[j][0]
		}
		return tasks[i][1] < tasks[j][1]
	})

	const maxT = 2005
	on := make([]bool, maxT)
	total := 0

	for _, t := range tasks {
		l, r, d := t[0], t[1], t[2]

		// Count already turned‑on seconds within [l, r]
		cnt := 0
		for i := l; i <= r; i++ {
			if on[i] {
				cnt++
			}
		}

		need := d - cnt
		// Turn on the latest possible unused seconds
		for i := r; i >= l && need > 0; i-- {
			if !on[i] {
				on[i] = true
				total++
				need--
			}
		}
	}

	return total
}
```

## Ruby

```ruby
def find_minimum_time(tasks)
  # Sort tasks by their ending time
  tasks.sort_by! { |t| t[1] }

  max_time = tasks.map { |t| t[1] }.max
  on = Array.new(max_time + 2, false)

  tasks.each do |start_i, end_i, duration_i|
    # Count already turned‑on seconds within the interval
    have = 0
    (start_i..end_i).each { |t| have += 1 if on[t] }

    need = duration_i - have
    t = end_i
    while need > 0 && t >= start_i
      unless on[t]
        on[t] = true
        need -= 1
      end
      t -= 1
    end
  end

  on.count(true)
end
```

## Scala

```scala
object Solution {
    def findMinimumTime(tasks: Array[Array[Int]]): Int = {
        val sorted = tasks.sortBy(_(1)) // sort by end time ascending
        val maxTime = 2000
        val on = new Array[Boolean](maxTime + 2) // indices 0..2001, we use 1..2000
        var total = 0

        for (task <- sorted) {
            val s = task(0)
            val e = task(1)
            val d = task(2)

            var already = 0
            var t = s
            while (t <= e) {
                if (on(t)) already += 1
                t += 1
            }

            var need = d - already
            var time = e
            while (need > 0 && time >= s) {
                if (!on(time)) {
                    on(time) = true
                    total += 1
                    need -= 1
                }
                time -= 1
            }
        }

        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_minimum_time(tasks: Vec<Vec<i32>>) -> i32 {
        // Convert tasks to (start, end, duration) tuples with usize indices
        let mut task_vec: Vec<(usize, usize, usize)> = tasks
            .iter()
            .map(|v| (v[0] as usize, v[1] as usize, v[2] as usize))
            .collect();

        // Sort by increasing end time
        task_vec.sort_by_key(|&(_, e, _)| e);

        // Determine the maximum end time to size the selection array
        let max_end = task_vec.iter().map(|&(_, e, _)| e).max().unwrap_or(0);
        let mut selected = vec![false; max_end + 2]; // index up to max_end inclusive

        for (start, end, dur) in task_vec {
            // Count already selected seconds within the interval
            let mut already = 0usize;
            for t in start..=end {
                if selected[t] {
                    already += 1;
                }
            }

            if already >= dur {
                continue;
            }

            // Need to add (dur - already) more seconds, preferring latest possible times
            let mut need = dur - already;
            let mut t = end;
            while need > 0 && t >= start {
                if !selected[t] {
                    selected[t] = true;
                    need -= 1;
                }
                if t == 0 {
                    break; // safety, though start ≥ 1
                }
                t -= 1;
            }
        }

        // Total seconds the computer is on
        selected.iter().filter(|&&b| b).count() as i32
    }
}
```

## Racket

```racket
(define/contract (find-minimum-time tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted (sort tasks
                       (lambda (a b)
                         (< (list-ref a 1) (list-ref b 1)))))
         (max-time (apply max (map (lambda (t) (list-ref t 1)) sorted)))
         (on (make-vector (+ max-time 2) #f))
         (ans 0))
    (for ([task sorted])
      (define start (list-ref task 0))
      (define end   (list-ref task 1))
      (define dur   (list-ref task 2))
      ;; count already selected times within [start, end]
      (define cnt 0)
      (for ([t (in-range start (+ end 1))])
        (when (vector-ref on t)
          (set! cnt (+ cnt 1))))
      (define need (- dur cnt))
      (when (> need 0)
        ;; add needed times as late as possible
        (for ([t (in-range end (- start 1) -1)])
          (when (and (> need 0) (not (vector-ref on t)))
            (vector-set! on t #t)
            (set! ans (+ ans 1))
            (set! need (- need 1))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([find_minimum_time/1]).

find_minimum_time(Tasks) ->
    TasksTuples = [list_to_tuple(T) || T <- Tasks],
    Sorted = lists:sort(fun(A, B) -> element(2, A) < element(2, B) end, TasksTuples),
    {Total, _} = process_tasks(Sorted, #{}, 0),
    Total.

process_tasks([], Map, Total) ->
    {Total, Map};
process_tasks([Task | Rest], Map, Total) ->
    S = element(1, Task),
    E = element(2, Task),
    D = element(3, Task),
    Already = count_in_range(Map, S, E, 0),
    Need = D - Already,
    {NewMap, NewTotal} =
        if
            Need =< 0 -> {Map, Total};
            true -> add_times(E, S, Need, Map, Total)
        end,
    process_tasks(Rest, NewMap, NewTotal).

count_in_range(_Map, Cur, End, Acc) when Cur > End ->
    Acc;
count_in_range(Map, Cur, End, Acc) ->
    NewAcc = case maps:is_key(Cur, Map) of
                true -> Acc + 1;
                false -> Acc
            end,
    count_in_range(Map, Cur + 1, End, NewAcc).

add_times(_E, _S, 0, Map, Total) ->
    {Map, Total};
add_times(E, S, Need, Map, Total) ->
    T = find_latest_not_selected(E, S, Map),
    NewMap = maps:put(T, true, Map),
    add_times(E, S, Need - 1, NewMap, Total + 1).

find_latest_not_selected(Cur, S, _Map) when Cur < S ->
    erlang:error(badarg);
find_latest_not_selected(Cur, S, Map) ->
    case maps:is_key(Cur, Map) of
        false -> Cur;
        true -> find_latest_not_selected(Cur - 1, S, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_minimum_time(tasks :: [[integer]]) :: integer
  def find_minimum_time(tasks) do
    sorted = Enum.sort_by(tasks, fn [_s, e, _d] -> e end)

    final_set =
      Enum.reduce(sorted, MapSet.new(), fn [s, e, d], set ->
        already = count_in_interval(set, s, e)
        need = d - already

        if need > 0 do
          add_times(e, s, need, set)
        else
          set
        end
      end)

    MapSet.size(final_set)
  end

  defp count_in_interval(set, s, e) do
    Enum.count(set, fn t -> t >= s and t <= e end)
  end

  defp add_times(_e, _s, 0, set), do: set
  defp add_times(e, s, need, set) when e < s, do: set
  defp add_times(e, s, need, set) do
    if MapSet.member?(set, e) do
      add_times(e - 1, s, need, set)
    else
      add_times(e - 1, s, need - 1, MapSet.put(set, e))
    end
  end
end
```
