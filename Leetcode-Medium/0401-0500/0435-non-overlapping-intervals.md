# 0435. Non-overlapping Intervals

## Cpp

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[1] == b[1]) return a[0] < b[0];
                 return a[1] < b[1];
             });
        int removals = 0;
        int prevEnd = intervals[0][1];
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] >= prevEnd) {
                prevEnd = intervals[i][1];
            } else {
                ++removals;
            }
        }
        return removals;
    }
};
```

## Java

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int count = 1; // at least one interval can be kept
        int end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }
        return intervals.length - count;
    }
}
```

## Python

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        non_overlap = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                non_overlap += 1
                end = intervals[i][1]
        return len(intervals) - non_overlap
```

## Python3

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        kept = 1
        for s, e in intervals[1:]:
            if s >= end:
                kept += 1
                end = e
        return len(intervals) - kept
```

## C

```c
#include <stdlib.h>

static int compareIntervals(const void *a, const void *b) {
    int *ia = *(int **)a;
    int *ib = *(int **)b;
    if (ia[1] != ib[1])
        return ia[1] - ib[1];
    return ia[0] - ib[0];
}

int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    if (intervalsSize == 0)
        return 0;
    
    qsort(intervals, intervalsSize, sizeof(int *), compareIntervals);
    
    int count = 1;
    int prev_end = intervals[0][1];
    
    for (int i = 1; i < intervalsSize; ++i) {
        if (intervals[i][0] >= prev_end) {
            ++count;
            prev_end = intervals[i][1];
        }
    }
    
    return intervalsSize - count;
}
```

## Csharp

```csharp
public class Solution
{
    public int EraseOverlapIntervals(int[][] intervals)
    {
        if (intervals == null || intervals.Length == 0) return 0;

        Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1]));

        int nonOverlapCount = 1;
        int prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.Length; i++)
        {
            if (intervals[i][0] >= prevEnd)
            {
                nonOverlapCount++;
                prevEnd = intervals[i][1];
            }
        }

        return intervals.Length - nonOverlapCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    if (!intervals || intervals.length === 0) return 0;
    
    // Sort by end time ascending
    intervals.sort((a, b) => a[1] - b[1]);
    
    let removals = 0;
    let prevEnd = intervals[0][1];
    
    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        if (start >= prevEnd) {
            // No overlap, keep this interval
            prevEnd = end;
        } else {
            // Overlap, need to remove one interval (the current one)
            removals++;
        }
    }
    
    return removals;
};
```

## Typescript

```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
    if (!intervals || intervals.length === 0) return 0;
    const sorted = intervals.slice().sort((a, b) => a[1] - b[1]);
    let nonOverlapCount = 0;
    let prevEnd = Number.NEGATIVE_INFINITY;
    for (const [start, end] of sorted) {
        if (start >= prevEnd) {
            nonOverlapCount++;
            prevEnd = end;
        }
    }
    return intervals.length - nonOverlapCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function eraseOverlapIntervals($intervals) {
        $n = count($intervals);
        if ($n === 0) {
            return 0;
        }
        usort($intervals, function($a, $b) {
            if ($a[1] == $b[1]) {
                return $a[0] <=> $b[0];
            }
            return $a[1] <=> $b[1];
        });
        $count = 0;
        $prevEnd = PHP_INT_MIN;
        foreach ($intervals as $int) {
            if ($int[0] >= $prevEnd) {
                $count++;
                $prevEnd = $int[1];
            }
        }
        return $n - $count;
    }
}
```

## Swift

```swift
class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        if intervals.isEmpty { return 0 }
        let sorted = intervals.sorted { $0[1] < $1[1] }
        var count = 0
        var currentEnd = Int.min
        for interval in sorted {
            if interval[0] >= currentEnd {
                count += 1
                currentEnd = interval[1]
            }
        }
        return intervals.count - count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
        if (intervals.isEmpty()) return 0
        intervals.sortWith(compareBy({ it[1] }, { it[0] }))
        var count = 1
        var end = intervals[0][1]
        for (i in 1 until intervals.size) {
            val start = intervals[i][0]
            if (start >= end) {
                count++
                end = intervals[i][1]
            }
        }
        return intervals.size - count
    }
}
```

## Dart

```dart
class Solution {
  int eraseOverlapIntervals(List<List<int>> intervals) {
    if (intervals.isEmpty) return 0;
    intervals.sort((a, b) => a[1].compareTo(b[1]));
    int count = 1;
    int end = intervals[0][1];
    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] >= end) {
        count++;
        end = intervals[i][1];
      }
    }
    return intervals.length - count;
  }
}
```

## Golang

```go
package main

import "sort"

func eraseOverlapIntervals(intervals [][]int) int {
	if len(intervals) == 0 {
		return 0
	}
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] < intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})
	count := 1
	end := intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] >= end {
			count++
			end = intervals[i][1]
		}
	}
	return len(intervals) - count
}
```

## Ruby

```ruby
def erase_overlap_intervals(intervals)
  return 0 if intervals.empty?
  intervals.sort_by! { |i| i[1] }
  count = 1
  prev_end = intervals[0][1]
  intervals[1..-1].each do |int|
    if int[0] >= prev_end
      count += 1
      prev_end = int[1]
    end
  end
  intervals.length - count
end
```

## Scala

```scala
object Solution {
    def eraseOverlapIntervals(intervals: Array[Array[Int]]): Int = {
        if (intervals.isEmpty) return 0
        val sorted = intervals.sortBy(arr => arr(1))
        var count = 1
        var end = sorted(0)(1)
        var i = 1
        while (i < sorted.length) {
            if (sorted(i)(0) >= end) {
                count += 1
                end = sorted(i)(1)
            }
            i += 1
        }
        intervals.length - count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        if intervals.is_empty() {
            return 0;
        }
        intervals.sort_unstable_by(|a, b| a[1].cmp(&b[1]));
        let mut removals: i32 = 0;
        let mut prev_end = intervals[0][1];
        for i in 1..intervals.len() {
            if intervals[i][0] >= prev_end {
                prev_end = intervals[i][1];
            } else {
                removals += 1;
            }
        }
        removals
    }
}
```

## Racket

```racket
(define/contract (erase-overlap-intervals intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted (sort intervals
                       (lambda (a b) (< (cadr a) (cadr b)))))
         (n (length sorted)))
    (if (= n 0)
        0
        (let loop ((rest (cdr sorted))
                   (prev-end (cadr (car sorted)))
                   (kept 1))
          (if (null? rest)
              (- n kept)
              (let* ((curr (car rest))
                     (start (car curr))
                     (end   (cadr curr)))
                (if (>= start prev-end)
                    (loop (cdr rest) end (+ kept 1))
                    (loop (cdr rest) prev-end kept))))))))
```

## Erlang

```erlang
-module(solution).
-export([erase_overlap_intervals/1]).

-spec erase_overlap_intervals(Intervals :: [[integer()]]) -> integer().
erase_overlap_intervals(Intervals) ->
    Sorted = lists:sort(fun([_, End1], [_, End2]) -> End1 =< End2 end, Intervals),
    {Count, _} = lists:foldl(
        fun([Start, End], {Cnt, PrevEnd}) ->
            if
                Start >= PrevEnd -> {Cnt + 1, End};
                true -> {Cnt, PrevEnd}
            end
        end,
        {0, -1000000},
        Sorted),
    length(Intervals) - Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec erase_overlap_intervals(intervals :: [[integer]]) :: integer
  def erase_overlap_intervals(intervals) do
    sorted = Enum.sort_by(intervals, fn [_s, e] -> e end)

    {keep, _} =
      Enum.reduce(sorted, {0, -1_000_000_000}, fn [s, e], {cnt, prev_end} ->
        if s >= prev_end do
          {cnt + 1, e}
        else
          {cnt, prev_end}
        end
      end)

    length(intervals) - keep
  end
end
```
