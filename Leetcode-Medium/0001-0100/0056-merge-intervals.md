# 0056. Merge Intervals

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] > merged.back()[1]) {
                merged.push_back(intervals[i]);
            } else {
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            }
        }
        return merged;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][];
        }
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = Math.max(current[1], intervals[i][1]);
            } else {
                merged.add(current);
                current = intervals[i];
            }
        }
        merged.add(current);
        return merged.toArray(new int[merged.size()][]);
    }
}
```

## Python

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for cur in intervals[1:]:
            prev = merged[-1]
            if cur[0] <= prev[1]:  # overlap
                prev[1] = max(prev[1], cur[1])
            else:
                merged.append(cur)
        return merged
```

## Python3

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last = merged[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])
        return merged
```

## C

```c
#include <stdlib.h>

/* Comparator for qsort: sort intervals by their start value */
static int cmpInterval(const void *a, const void *b) {
    const int *ia = *(const int **)a;
    const int *ib = *(const int **)b;
    if (ia[0] < ib[0]) return -1;
    if (ia[0] > ib[0]) return 1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** merge(int** intervals, int intervalsSize, int* intervalsColSize,
            int* returnSize, int*** returnColumnSizes) {
    if (intervalsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    /* Sort intervals by start */
    qsort(intervals, intervalsSize, sizeof(int *), cmpInterval);

    /* Allocate maximum possible space for results */
    int **merged = (int **)malloc(intervalsSize * sizeof(int *));
    int *colSizes = (int *)malloc(intervalsSize * sizeof(int));

    int count = 0;
    int curStart = intervals[0][0];
    int curEnd   = intervals[0][1];

    for (int i = 1; i < intervalsSize; ++i) {
        int start = intervals[i][0];
        int end   = intervals[i][1];
        if (start > curEnd) { /* no overlap, finalize current interval */
            merged[count] = (int *)malloc(2 * sizeof(int));
            merged[count][0] = curStart;
            merged[count][1] = curEnd;
            colSizes[count] = 2;
            ++count;

            curStart = start;
            curEnd   = end;
        } else { /* overlap, merge */
            if (end > curEnd) curEnd = end;
        }
    }

    /* Add the last interval */
    merged[count] = (int *)malloc(2 * sizeof(int));
    merged[count][0] = curStart;
    merged[count][1] = curEnd;
    colSizes[count] = 2;
    ++count;

    *returnSize = count;
    *returnColumnSizes = &colSizes;
    return merged;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] Merge(int[][] intervals) {
        if (intervals == null || intervals.Length == 0) return new int[0][];
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var merged = new List<int[]>();
        int[] current = intervals[0];
        for (int i = 1; i < intervals.Length; i++) {
            int[] interval = intervals[i];
            if (interval[0] <= current[1]) {
                current[1] = Math.Max(current[1], interval[1]);
            } else {
                merged.Add(current);
                current = interval;
            }
        }
        merged.Add(current);
        return merged.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (!intervals || intervals.length <= 1) return intervals;
    
    // Sort intervals by start time
    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [];
    for (const cur of intervals) {
        if (merged.length === 0 || cur[0] > merged[merged.length - 1][1]) {
            // No overlap, add new interval
            merged.push([...cur]);
        } else {
            // Overlap, merge with the last interval
            merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], cur[1]);
        }
    }
    
    return merged;
};
```

## Typescript

```typescript
function merge(intervals: number[][]): number[][] {
    if (intervals.length <= 1) return intervals;
    intervals.sort((a, b) => a[0] - b[0]);
    const merged: number[][] = [];
    let [curStart, curEnd] = intervals[0];
    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        if (start <= curEnd) {
            if (end > curEnd) curEnd = end;
        } else {
            merged.push([curStart, curEnd]);
            curStart = start;
            curEnd = end;
        }
    }
    merged.push([curStart, curEnd]);
    return merged;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer[][]
     */
    function merge($intervals) {
        if (empty($intervals)) {
            return [];
        }
        usort($intervals, function ($a, $b) {
            return $a[0] <=> $b[0];
        });
        $merged = [];
        foreach ($intervals as $int) {
            if (empty($merged) || $int[0] > $merged[count($merged) - 1][1]) {
                $merged[] = $int;
            } else {
                $lastIdx = count($merged) - 1;
                $merged[$lastIdx][1] = max($merged[$lastIdx][1], $int[1]);
            }
        }
        return $merged;
    }
}
```

## Swift

```swift
class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        if intervals.isEmpty { return [] }
        let sorted = intervals.sorted { (a, b) -> Bool in
            if a[0] == b[0] {
                return a[1] < b[1]
            }
            return a[0] < b[0]
        }
        var merged: [[Int]] = []
        for interval in sorted {
            if merged.isEmpty || interval[0] > merged[merged.count - 1][1] {
                merged.append(interval)
            } else {
                merged[merged.count - 1][1] = max(merged[merged.count - 1][1], interval[1])
            }
        }
        return merged
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        if (intervals.isEmpty()) return arrayOf()
        val sorted = intervals.sortedWith(compareBy<IntArray> { it[0] }.thenBy { it[1] })
        val merged = mutableListOf<IntArray>()
        var start = sorted[0][0]
        var end = sorted[0][1]
        for (i in 1 until sorted.size) {
            val curStart = sorted[i][0]
            val curEnd = sorted[i][1]
            if (curStart <= end) {
                if (curEnd > end) end = curEnd
            } else {
                merged.add(intArrayOf(start, end))
                start = curStart
                end = curEnd
            }
        }
        merged.add(intArrayOf(start, end))
        return merged.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> merge(List<List<int>> intervals) {
    if (intervals.isEmpty) return [];
    intervals.sort((a, b) => a[0].compareTo(b[0]));
    List<List<int>> merged = [];
    int start = intervals[0][0];
    int end = intervals[0][1];

    for (int i = 1; i < intervals.length; i++) {
      var cur = intervals[i];
      if (cur[0] <= end) {
        if (cur[1] > end) end = cur[1];
      } else {
        merged.add([start, end]);
        start = cur[0];
        end = cur[1];
      }
    }

    merged.add([start, end]);
    return merged;
  }
}
```

## Golang

```go
package main

import "sort"

func merge(intervals [][]int) [][]int {
	if len(intervals) == 0 {
		return [][]int{}
	}
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	merged := [][]int{{intervals[0][0], intervals[0][1]}}
	for _, iv := range intervals[1:] {
		last := merged[len(merged)-1]
		if iv[0] <= last[1] {
			if iv[1] > last[1] {
				last[1] = iv[1]
			}
		} else {
			merged = append(merged, []int{iv[0], iv[1]})
		}
	}
	return merged
}
```

## Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
  return [] if intervals.empty?
  intervals.sort_by! { |i| i[0] }
  merged = []
  intervals.each do |int|
    if merged.empty? || merged[-1][1] < int[0]
      merged << int.dup
    else
      merged[-1][1] = [merged[-1][1], int[1]].max
    end
  end
  merged
end
```

## Scala

```scala
object Solution {
    def merge(intervals: Array[Array[Int]]): Array[Array[Int]] = {
        if (intervals.isEmpty) return Array.empty
        val sorted = intervals.sortBy(_(0))
        val merged = scala.collection.mutable.ArrayBuffer[Array[Int]]()
        var curStart = sorted(0)(0)
        var curEnd   = sorted(0)(1)

        var i = 1
        while (i < sorted.length) {
            val s = sorted(i)(0)
            val e = sorted(i)(1)
            if (s <= curEnd) {
                curEnd = math.max(curEnd, e)
            } else {
                merged += Array(curStart, curEnd)
                curStart = s
                curEnd = e
            }
            i += 1
        }
        merged += Array(curStart, curEnd)
        merged.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if intervals.is_empty() {
            return vec![];
        }
        intervals.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
        let mut merged: Vec<Vec<i32>> = Vec::new();
        for interval in intervals {
            if merged.is_empty() || merged.last().unwrap()[1] < interval[0] {
                merged.push(interval);
            } else {
                let last = merged.last_mut().unwrap();
                if last[1] < interval[1] {
                    last[1] = interval[1];
                }
            }
        }
        merged
    }
}
```

## Racket

```racket
(define/contract (merge intervals)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((sorted (sort intervals
                       (lambda (a b) (< (first a) (first b)))))
         (merged-rev
          (foldl
            (lambda (int acc)
              (if (null? acc)
                  (list int)
                  (let* ((last-int (car acc))
                         (last-start (first last-int))
                         (last-end   (second last-int))
                         (cur-start  (first int))
                         (cur-end    (second int)))
                    (if (> cur-start last-end) ; no overlap
                        (cons int acc)
                        (let ((new-end (max last-end cur-end)))
                          (cons (list last-start new-end) (cdr acc)))))))
            '()
            sorted)))
    (reverse merged-rev)))
```

## Erlang

```erlang
-module(solution).
-export([merge/1]).

-spec merge(Intervals :: [[integer()]]) -> [[integer()]].
merge(Intervals) ->
    Sorted = lists:sort(fun([S1,_], [S2,_]) -> S1 =< S2 end, Intervals),
    MergedRev = merge_sorted(Sorted, []),
    lists:reverse(MergedRev).

merge_sorted([], Acc) ->
    Acc;
merge_sorted([H|T], []) ->
    merge_sorted(T, [H]);
merge_sorted([[S,E]=Curr | Rest], [Prev=[PS,PE] | AccTail]) ->
    if
        S =< PE ->
            NewPrev = [PS, erlang:max(PE, E)],
            merge_sorted(Rest, [NewPrev | AccTail]);
        true ->
            merge_sorted(Rest, [Curr, Prev | AccTail])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec merge(intervals :: [[integer]]) :: [[integer]]
  def merge([]), do: []

  def merge(intervals) do
    sorted = Enum.sort_by(intervals, fn [s, _] -> s end)

    merged_rev =
      Enum.reduce(sorted, [], fn [s, e], acc ->
        case acc do
          [] ->
            [[s, e]]

          [[last_s, last_e] | rest] ->
            if s <= last_e do
              [[last_s, max(last_e, e)] | rest]
            else
              [[s, e] | acc]
            end
        end
      end)

    Enum.reverse(merged_rev)
  end
end
```
