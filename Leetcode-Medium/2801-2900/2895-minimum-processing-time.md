# 2895. Minimum Processing Time

## Cpp

```cpp
class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        sort(processorTime.begin(), processorTime.end());
        sort(tasks.begin(), tasks.end(), greater<int>());
        long long ans = 0;
        int n = processorTime.size();
        for (int i = 0; i < n; ++i) {
            long long cur = (long long)processorTime[i] + tasks[4 * i];
            if (cur > ans) ans = cur;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        int n = processorTime.size();
        int[] proc = new int[n];
        for (int i = 0; i < n; i++) {
            proc[i] = processorTime.get(i);
        }
        int m = tasks.size(); // equals 4 * n
        int[] t = new int[m];
        for (int i = 0; i < m; i++) {
            t[i] = tasks.get(i);
        }

        Arrays.sort(proc);   // ascending
        Arrays.sort(t);      // ascending

        long answer = 0;
        for (int i = 0; i < n; i++) {
            int idx = m - 1 - 4 * i;          // largest task assigned to processor i
            long cur = (long) proc[i] + t[idx];
            if (cur > answer) {
                answer = cur;
            }
        }
        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0
        for i, p in enumerate(processorTime):
            # the largest task assigned to this processor is at position 4*i
            cur = p + tasks[4 * i]
            if cur > ans:
                ans = cur
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        max_time = 0
        for i, p in enumerate(processorTime):
            cur = p + tasks[i * 4]
            if cur > max_time:
                max_time = cur
        return max_time
```

## C

```c
#include <stdlib.h>

static int cmp_asc(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

static int cmp_desc(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (y > x) - (y < x);
}

int minProcessingTime(int* processorTime, int processorTimeSize, int* tasks, int tasksSize) {
    qsort(processorTime, processorTimeSize, sizeof(int), cmp_asc);
    qsort(tasks, tasksSize, sizeof(int), cmp_desc);

    long maxFinish = 0;
    for (int i = 0; i < processorTimeSize; ++i) {
        int base = processorTime[i];
        for (int k = 0; k < 4; ++k) {
            int idx = i * 4 + k;
            long finish = (long)base + tasks[idx];
            if (finish > maxFinish) maxFinish = finish;
        }
    }
    return (int)maxFinish;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinProcessingTime(IList<int> processorTime, IList<int> tasks) {
        int n = processorTime.Count;
        int[] proc = new int[n];
        for (int i = 0; i < n; i++) proc[i] = processorTime[i];
        Array.Sort(proc); // ascending

        int m = tasks.Count; // should be 4 * n
        int[] t = new int[m];
        for (int i = 0; i < m; i++) t[i] = tasks[i];
        Array.Sort(t); // ascending

        long answer = 0;
        for (int i = 0; i < n; i++) {
            int idx = m - 1 - i * 4; // largest remaining task for this processor
            long cur = (long)proc[i] + t[idx];
            if (cur > answer) answer = cur;
        }
        return (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} processorTime
 * @param {number[]} tasks
 * @return {number}
 */
var minProcessingTime = function(processorTime, tasks) {
    processorTime.sort((a, b) => a - b);
    tasks.sort((a, b) => b - a);
    let ans = 0;
    const n = processorTime.length;
    for (let i = 0; i < n; ++i) {
        const cur = processorTime[i] + tasks[4 * i];
        if (cur > ans) ans = cur;
    }
    return ans;
};
```

## Typescript

```typescript
function minProcessingTime(processorTime: number[], tasks: number[]): number {
    processorTime.sort((a, b) => a - b);
    tasks.sort((a, b) => b - a);
    let result = 0;
    for (let i = 0; i < processorTime.length; ++i) {
        const cur = processorTime[i] + tasks[4 * i];
        if (cur > result) result = cur;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $processorTime
     * @param Integer[] $tasks
     * @return Integer
     */
    function minProcessingTime($processorTime, $tasks) {
        sort($processorTime);          // ascending
        rsort($tasks);                 // descending

        $ans = 0;
        $n = count($processorTime);
        for ($i = 0; $i < $n; $i++) {
            $candidate = $processorTime[$i] + $tasks[4 * $i];
            if ($candidate > $ans) {
                $ans = $candidate;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minProcessingTime(_ processorTime: [Int], _ tasks: [Int]) -> Int {
        let n = processorTime.count
        let sortedProcessors = processorTime.sorted()
        let sortedTasksDesc = tasks.sorted(by: >)
        var result = 0
        for i in 0..<n {
            let candidate = sortedProcessors[i] + sortedTasksDesc[4 * i]
            if candidate > result {
                result = candidate
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minProcessingTime(processorTime: List<Int>, tasks: List<Int>): Int {
        val procSorted = processorTime.sorted()
        val taskSortedDesc = tasks.sortedDescending()
        var maxTime = 0L
        for (i in procSorted.indices) {
            val sum = procSorted[i].toLong() + taskSortedDesc[4 * i].toLong()
            if (sum > maxTime) maxTime = sum
        }
        return maxTime.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minProcessingTime(List<int> processorTime, List<int> tasks) {
    processorTime.sort();
    tasks.sort((a, b) => b - a);
    int n = processorTime.length;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int candidate = processorTime[i] + tasks[4 * i];
      if (candidate > ans) ans = candidate;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func minProcessingTime(processorTime []int, tasks []int) int {
    sort.Ints(processorTime)
    sort.Slice(tasks, func(i, j int) bool { return tasks[i] > tasks[j] })
    maxTime := 0
    for i := 0; i < len(processorTime); i++ {
        cur := processorTime[i] + tasks[4*i]
        if cur > maxTime {
            maxTime = cur
        }
    }
    return maxTime
}
```

## Ruby

```ruby
def min_processing_time(processor_time, tasks)
  processor_time.sort!
  tasks.sort!.reverse!
  max_time = 0
  processor_time.each_with_index do |pt, i|
    candidate = pt + tasks[4 * i]
    max_time = candidate if candidate > max_time
  end
  max_time
end
```

## Scala

```scala
object Solution {
    def minProcessingTime(processorTime: List[Int], tasks: List[Int]): Int = {
        val procSorted = processorTime.sorted
        val tasksDesc = tasks.sortWith(_ > _)
        var maxFinish: Long = 0L
        for (i <- procSorted.indices) {
            val longestTask = tasksDesc(4 * i)
            val finish = procSorted(i).toLong + longestTask.toLong
            if (finish > maxFinish) maxFinish = finish
        }
        maxFinish.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_processing_time(mut processor_time: Vec<i32>, mut tasks: Vec<i32>) -> i32 {
        // Sort processors ascending and tasks descending
        processor_time.sort_unstable();
        tasks.sort_unstable_by(|a, b| b.cmp(a));

        let n = processor_time.len();
        let mut max_time: i64 = 0;
        for i in 0..n {
            let sum = processor_time[i] as i64 + tasks[4 * i] as i64;
            if sum > max_time {
                max_time = sum;
            }
        }
        max_time as i32
    }
}
```

## Racket

```racket
(define/contract (min-processing-time processorTime tasks)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((proc-vec (list->vector (sort processorTime <)))
         (tasks-vec (list->vector (sort tasks >))))
    (let loop ((i 0) (n (vector-length proc-vec)) (max-time 0))
      (if (= i n)
          max-time
          (let* ((completion (+ (vector-ref proc-vec i)
                                (vector-ref tasks-vec (* i 4)))))
            (loop (+ i 1) n (if (> completion max-time) completion max-time)))))))
```

## Erlang

```erlang
-spec min_processing_time([integer()], [integer()]) -> integer().
min_processing_time(ProcessorTime, Tasks) ->
    Ps = lists:sort(ProcessorTime),
    TsDesc = lists:reverse(lists:sort(Tasks)),
    loop(Ps, TsDesc, 0).

loop([], _, Max) -> Max;
loop([P|RestPs], [T|TsRest], Max) ->
    Candidate = P + T,
    NewMax = erlang:max(Candidate, Max),
    TsNext = lists:nthtail(3, TsRest),
    loop(RestPs, TsNext, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_processing_time(processor_time :: [integer], tasks :: [integer]) :: integer
  def min_processing_time(processor_time, tasks) do
    proc_sorted = Enum.sort(processor_time)
    task_sorted = Enum.sort(tasks, &>=/2)
    task_groups = Enum.chunk_every(task_sorted, 4)

    Enum.zip(proc_sorted, task_groups)
    |> Enum.reduce(0, fn {pt, [max_task | _]}, acc ->
      cand = pt + max_task
      if cand > acc, do: cand, else: acc
    end)
  end
end
```
