# 0057. Insert Interval

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int n = intervals.size();
        int i = 0;
        // Add all intervals ending before newInterval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            res.push_back(intervals[i]);
            ++i;
        }
        // Merge overlapping intervals with newInterval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            ++i;
        }
        // Add the merged interval
        res.push_back(newInterval);
        // Append the rest of the intervals
        while (i < n) {
            res.push_back(intervals[i]);
            ++i;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        java.util.List<int[]> res = new java.util.ArrayList<>();
        int i = 0;
        // Add all intervals that end before the new interval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            res.add(intervals[i]);
            i++;
        }
        // Merge overlapping intervals with the new interval
        int start = newInterval[0];
        int end = newInterval[1];
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        res.add(new int[]{start, end});
        // Add the remaining intervals
        while (i < n) {
            res.add(intervals[i]);
            i++;
        }
        return res.toArray(new int[res.size()][]);
    }
}
```

## Python

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        res = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # Add all intervals ending before the new interval starts
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # Add the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

## Python3

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        # Add the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
```

## C

```c
#include <stdlib.h>

int** insert(int** intervals, int intervalsSize, int* intervalsColSize,
             int* newInterval, int newIntervalSize,
             int* returnSize, int** returnColumnSizes) {
    int maxSize = intervalsSize + 1;
    int** result = (int**)malloc(maxSize * sizeof(int*));
    int* colSizes = (int*)malloc(maxSize * sizeof(int));

    int count = 0;
    int i = 0;

    // Add all intervals that end before the new interval starts
    while (i < intervalsSize && intervals[i][1] < newInterval[0]) {
        int* cur = (int*)malloc(2 * sizeof(int));
        cur[0] = intervals[i][0];
        cur[1] = intervals[i][1];
        result[count++] = cur;
        i++;
    }

    // Merge overlapping intervals
    int mergedStart = newInterval[0];
    int mergedEnd   = newInterval[1];
    while (i < intervalsSize && intervals[i][0] <= mergedEnd) {
        if (intervals[i][0] < mergedStart) mergedStart = intervals[i][0];
        if (intervals[i][1] > mergedEnd)   mergedEnd   = intervals[i][1];
        i++;
    }
    int* merged = (int*)malloc(2 * sizeof(int));
    merged[0] = mergedStart;
    merged[1] = mergedEnd;
    result[count++] = merged;

    // Add the remaining intervals
    while (i < intervalsSize) {
        int* cur = (int*)malloc(2 * sizeof(int));
        cur[0] = intervals[i][0];
        cur[1] = intervals[i][1];
        result[count++] = cur;
        i++;
    }

    // Set return values
    *returnSize = count;
    *returnColumnSizes = colSizes;
    for (int j = 0; j < count; ++j) {
        colSizes[j] = 2;
    }

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        var result = new System.Collections.Generic.List<int[]>();
        int i = 0;
        int n = intervals.Length;

        // Add all intervals that end before the new interval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.Add(intervals[i]);
            i++;
        }

        // Merge overlapping intervals with the new interval
        int start = newInterval[0];
        int end = newInterval[1];
        while (i < n && intervals[i][0] <= end) {
            start = System.Math.Min(start, intervals[i][0]);
            end = System.Math.Max(end, intervals[i][1]);
            i++;
        }
        result.Add(new int[] { start, end });

        // Add the remaining intervals
        while (i < n) {
            result.Add(intervals[i]);
            i++;
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    const res = [];
    let i = 0;
    const n = intervals.length;

    // Add all intervals that end before the new interval starts
    while (i < n && intervals[i][1] < newInterval[0]) {
        res.push(intervals[i]);
        i++;
    }

    // Merge overlapping intervals with the new interval
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    res.push(newInterval);

    // Add the remaining intervals
    while (i < n) {
        res.push(intervals[i]);
        i++;
    }

    return res;
};
```

## Typescript

```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
    const result: number[][] = [];
    let i = 0;
    const n = intervals.length;

    // Add all intervals that end before the new interval starts
    while (i < n && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // Merge overlapping intervals with the new interval
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.push(newInterval);

    // Add the remaining intervals
    while (i < n) {
        result.push(intervals[i]);
        i++;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @param Integer[] $newInterval
     * @return Integer[][]
     */
    function insert($intervals, $newInterval) {
        $n = count($intervals);
        $res = [];
        $i = 0;

        // Add all intervals that end before the new interval starts
        while ($i < $n && $intervals[$i][1] < $newInterval[0]) {
            $res[] = $intervals[$i];
            $i++;
        }

        // Merge overlapping intervals with the new interval
        while ($i < $n && $intervals[$i][0] <= $newInterval[1]) {
            $newInterval[0] = min($newInterval[0], $intervals[$i][0]);
            $newInterval[1] = max($newInterval[1], $intervals[$i][1]);
            $i++;
        }

        // Add the merged new interval
        $res[] = $newInterval;

        // Append the remaining intervals
        while ($i < $n) {
            $res[] = $intervals[$i];
            $i++;
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var result = [[Int]]()
        var i = 0
        let n = intervals.count
        var merged = newInterval
        
        // Add all intervals that end before the new interval starts
        while i < n && intervals[i][1] < merged[0] {
            result.append(intervals[i])
            i += 1
        }
        
        // Merge overlapping intervals with the new interval
        while i < n && intervals[i][0] <= merged[1] {
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1
        }
        result.append(merged)
        
        // Add the remaining intervals after the new interval
        while i < n {
            result.append(intervals[i])
            i += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        val result = mutableListOf<IntArray>()
        var i = 0
        val n = intervals.size

        // Add all intervals that end before the new interval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i])
            i++
        }

        var start = newInterval[0]
        var end = newInterval[1]

        // Merge overlapping intervals with the new interval
        while (i < n && intervals[i][0] <= end) {
            start = kotlin.math.min(start, intervals[i][0])
            end = kotlin.math.max(end, intervals[i][1])
            i++
        }
        result.add(intArrayOf(start, end))

        // Add the remaining intervals after the new interval
        while (i < n) {
            result.add(intervals[i])
            i++
        }

        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> insert(List<List<int>> intervals, List<int> newInterval) {
    int n = intervals.length;
    int i = 0;
    List<List<int>> res = [];

    // Add all intervals that end before the new interval starts
    while (i < n && intervals[i][1] < newInterval[0]) {
      res.add(intervals[i]);
      i++;
    }

    // Merge overlapping intervals with the new interval
    int start = newInterval[0];
    int end = newInterval[1];
    while (i < n && intervals[i][0] <= end) {
      start = start < intervals[i][0] ? start : intervals[i][0];
      end = end > intervals[i][1] ? end : intervals[i][1];
      i++;
    }
    res.add([start, end]);

    // Add the remaining intervals
    while (i < n) {
      res.add(intervals[i]);
      i++;
    }

    return res;
  }
}
```

## Golang

```go
func insert(intervals [][]int, newInterval []int) [][]int {
    n := len(intervals)
    i := 0
    res := make([][]int, 0, n+1)

    // Add all intervals that end before the new interval starts.
    for i < n && intervals[i][1] < newInterval[0] {
        res = append(res, intervals[i])
        i++
    }

    // Merge overlapping intervals with the new interval.
    start, end := newInterval[0], newInterval[1]
    for i < n && intervals[i][0] <= end {
        if intervals[i][0] < start {
            start = intervals[i][0]
        }
        if intervals[i][1] > end {
            end = intervals[i][1]
        }
        i++
    }
    res = append(res, []int{start, end})

    // Append the remaining intervals.
    for i < n {
        res = append(res, intervals[i])
        i++
    }

    return res
}
```

## Ruby

```ruby
def insert(intervals, new_interval)
  res = []
  i = 0
  n = intervals.length

  while i < n && intervals[i][1] < new_interval[0]
    res << intervals[i]
    i += 1
  end

  while i < n && intervals[i][0] <= new_interval[1]
    new_interval[0] = [new_interval[0], intervals[i][0]].min
    new_interval[1] = [new_interval[1], intervals[i][1]].max
    i += 1
  end

  res << new_interval

  while i < n
    res << intervals[i]
    i += 1
  end

  res
end
```

## Scala

```scala
object Solution {
    def insert(intervals: Array[Array[Int]], newInterval: Array[Int]): Array[Array[Int]] = {
        val res = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
        var i = 0
        val n = intervals.length
        // make a mutable copy of newInterval to adjust start and end
        val merged = newInterval.clone()
        // Add all intervals that end before the new interval starts
        while (i < n && intervals(i)(1) < merged(0)) {
            res += intervals(i)
            i += 1
        }
        // Merge overlapping intervals
        while (i < n && intervals(i)(0) <= merged(1)) {
            merged(0) = math.min(merged(0), intervals(i)(0))
            merged(1) = math.max(merged(1), intervals(i)(1))
            i += 1
        }
        // Add the merged interval
        res += merged
        // Append the rest of the intervals
        while (i < n) {
            res += intervals(i)
            i += 1
        }
        res.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let n = intervals.len();
        let mut i = 0usize;
        let mut start = new_interval[0];
        let mut end = new_interval[1];

        // Add all intervals that end before the new interval starts
        while i < n && intervals[i][1] < start {
            res.push(intervals[i].clone());
            i += 1;
        }

        // Merge overlapping intervals with the new interval
        while i < n && intervals[i][0] <= end {
            start = start.min(intervals[i][0]);
            end = end.max(intervals[i][1]);
            i += 1;
        }
        res.push(vec![start, end]);

        // Add the remaining intervals
        while i < n {
            res.push(intervals[i].clone());
            i += 1;
        }

        res
    }
}
```

## Racket

```racket
(define/contract (insert intervals newInterval)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof (listof exact-integer?)))
  (let loop ((ints intervals) (new newInterval) (res '()))
    (cond
      [(null? ints)
       (reverse (cons new res))]
      [else
       (let* ((cur (car ints))
              (cur-start (first cur))
              (cur-end (second cur))
              (new-start (first new))
              (new-end (second new)))
         (cond
           [(< cur-end new-start)
            (loop (cdr ints) new (cons cur res))]
           [(> cur-start new-end)
            (let ((before (reverse res)))
              (append before (list new) ints))]
           [else
            (define merged (list (min cur-start new-start)
                                 (max cur-end new-end)))
            (loop (cdr ints) merged res)]))])))
```

## Erlang

```erlang
-spec insert(Intervals :: [[integer()]], NewInterval :: [integer()]) -> [[integer()]].
insert(Intervals, NewInterval) ->
    [Start0, End0] = NewInterval,
    {BeforeRev, Rest1} = split_before(Intervals, Start0),
    Before = lists:reverse(BeforeRev),
    {Merged, After} = merge_overlap(Rest1, Start0, End0),
    Before ++ [Merged] ++ After.

split_before([], _Start) -> {[], []};
split_before([ [S,E] = I | Rest ], Start) when E < Start ->
    {BeforeRev, After} = split_before(Rest, Start),
    {[I | BeforeRev], After};
split_before(Intervals, _Start) -> {[], Intervals}.

merge_overlap([], CurStart, CurEnd) -> {[CurStart, CurEnd], []};
merge_overlap([ [S,E] = I | Rest ], CurStart, CurEnd) ->
    if S =< CurEnd ->
        NewStart = erlang:min(CurStart, S),
        NewEnd   = erlang:max(CurEnd, E),
        merge_overlap(Rest, NewStart, NewEnd);
       true ->
        {[CurStart, CurEnd], [I | Rest]}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec insert(intervals :: [[integer]], new_interval :: [integer]) :: [[integer]]
  def insert([], new_interval), do: [new_interval]
  def insert(intervals, new_interval) do
    merge(intervals, new_interval, [])
  end

  defp merge([], new_int, acc) do
    Enum.reverse([new_int | acc])
  end

  defp merge([[s, e] = cur | rest], [ns, ne] = new_int, acc) do
    cond do
      e < ns ->
        merge(rest, new_int, [cur | acc])

      s > ne ->
        Enum.reverse(acc) ++ [new_int] ++ [cur | rest]

      true ->
        merged = [min(s, ns), max(e, ne)]
        merge(rest, merged, acc)
    end
  end
end
```
