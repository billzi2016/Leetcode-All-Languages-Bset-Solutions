# 1943. Describe the Painting

## Cpp

```cpp
class Solution {
public:
    vector<vector<long long>> splitPainting(vector<vector<int>>& segments) {
        vector<pair<int,long long>> events;
        events.reserve(segments.size()*2);
        for (auto &seg : segments) {
            int l = seg[0], r = seg[1];
            long long c = seg[2];
            events.emplace_back(l,  c);
            events.emplace_back(r, -c);
        }
        sort(events.begin(), events.end(),
             [](const auto& a, const auto& b){ return a.first < b.first; });
        
        vector<vector<long long>> res;
        long long curSum = 0;
        size_t i = 0;
        while (i < events.size()) {
            int pos = events[i].first;
            // apply all deltas at this position
            while (i < events.size() && events[i].first == pos) {
                curSum += events[i].second;
                ++i;
            }
            if (i == events.size()) break; // no further interval
            
            int nextPos = events[i].first;
            if (curSum > 0) {
                if (!res.empty() && res.back()[2] == curSum && res.back()[1] == pos) {
                    res.back()[1] = nextPos; // merge with previous
                } else {
                    res.push_back({(long long)pos, (long long)nextPos, curSum});
                }
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Long>> splitPainting(int[][] segments) {
        TreeMap<Integer, Long> diff = new TreeMap<>();
        for (int[] seg : segments) {
            int start = seg[0];
            int end = seg[1];
            long color = seg[2];
            diff.merge(start, color, Long::sum);
            diff.merge(end, -color, Long::sum);
        }
        List<List<Long>> res = new ArrayList<>();
        long curSum = 0;
        Integer prevPos = null;
        for (Map.Entry<Integer, Long> entry : diff.entrySet()) {
            int pos = entry.getKey();
            if (prevPos != null && curSum > 0) {
                List<Long> interval = Arrays.asList(
                        prevPos.longValue(),
                        (long) pos,
                        curSum
                );
                res.add(interval);
            }
            curSum += entry.getValue();
            prevPos = pos;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for l, r, c in segments:
            events.append((l, c))
            events.append((r, -c))
        events.sort()
        
        res = []
        cur_sum = 0
        prev_pos = None
        i = 0
        n = len(events)
        while i < n:
            pos = events[i][0]
            if prev_pos is not None and prev_pos < pos and cur_sum > 0:
                res.append([prev_pos, pos, cur_sum])
            # process all events at this position
            while i < n and events[i][0] == pos:
                cur_sum += events[i][1]
                i += 1
            prev_pos = pos
        return res
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        for l, r, c in segments:
            diff[l] += c
            diff[r] -= c

        positions = sorted(diff.keys())
        res = []
        cur_sum = 0
        prev = None

        for pos in positions:
            if prev is not None and cur_sum > 0 and prev < pos:
                if res and res[-1][2] == cur_sum and res[-1][1] == prev:
                    res[-1][1] = pos
                else:
                    res.append([prev, pos, cur_sum])
            cur_sum += diff[pos]
            prev = pos

        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int pos;
    long long delta;
} Event;

static int cmpEvent(const void *a, const void *b) {
    int pa = ((const Event *)a)->pos;
    int pb = ((const Event *)b)->pos;
    return (pa > pb) - (pa < pb);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
long long** splitPainting(int** segments, int segmentsSize, int* segmentsColSize,
                          int* returnSize, int** returnColumnSizes) {
    int totalEvents = segmentsSize * 2;
    Event *events = (Event *)malloc(sizeof(Event) * totalEvents);
    for (int i = 0; i < segmentsSize; ++i) {
        int start = segments[i][0];
        int end   = segments[i][1];
        long long color = (long long)segments[i][2];
        events[2*i].pos = start;
        events[2*i].delta = color;
        events[2*i+1].pos = end;
        events[2*i+1].delta = -color;
    }

    qsort(events, totalEvents, sizeof(Event), cmpEvent);

    int maxIntervals = segmentsSize * 2; // upper bound
    long long **result = (long long **)malloc(sizeof(long long *) * maxIntervals);
    int *colSizes = (int *)malloc(sizeof(int) * maxIntervals);
    int idx = 0;

    long long curSum = 0;
    int prevPos = events[0].pos;
    int i = 0;
    while (i < totalEvents) {
        int curPos = events[i].pos;
        if (curPos > prevPos && curSum > 0) {
            long long *seg = (long long *)malloc(sizeof(long long) * 3);
            seg[0] = (long long)prevPos;
            seg[1] = (long long)curPos;
            seg[2] = curSum;
            result[idx] = seg;
            colSizes[idx] = 3;
            ++idx;
        }
        // apply all deltas at curPos
        while (i < totalEvents && events[i].pos == curPos) {
            curSum += events[i].delta;
            ++i;
        }
        prevPos = curPos;
    }

    free(events);
    *returnSize = idx;
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<long>> SplitPainting(int[][] segments) {
        var diff = new SortedDictionary<int, long>();
        void Add(int point, long delta) {
            if (diff.ContainsKey(point)) {
                diff[point] += delta;
                if (diff[point] == 0) diff.Remove(point);
            } else {
                diff[point] = delta;
            }
        }

        foreach (var seg in segments) {
            int start = seg[0];
            int end = seg[1];
            long color = seg[2];
            Add(start, color);
            Add(end, -color);
        }

        var result = new List<IList<long>>();
        long prev = -1;
        long curSum = 0;

        foreach (var kvp in diff) {
            int x = kvp.Key;
            if (prev != -1 && curSum > 0) {
                result.Add(new List<long> { prev, x, curSum });
            }
            curSum += kvp.Value;
            prev = x;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} segments
 * @return {number[][]}
 */
var splitPainting = function(segments) {
    const events = [];
    for (const [l, r, c] of segments) {
        events.push([l, c]);   // start adds color sum
        events.push([r, -c]);  // end subtracts color sum
    }
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    const res = [];
    let curSum = 0;
    let prevPos = null;
    let i = 0;
    while (i < events.length) {
        const pos = events[i][0];
        if (prevPos !== null && prevPos < pos && curSum > 0) {
            res.push([prevPos, pos, curSum]);
        }
        // apply all deltas at this position
        while (i < events.length && events[i][0] === pos) {
            curSum += events[i][1];
            i++;
        }
        prevPos = pos;
    }
    return res;
};
```

## Typescript

```typescript
function splitPainting(segments: number[][]): number[][] {
    const events: [number, number][] = [];
    for (const seg of segments) {
        const [l, r, c] = seg;
        events.push([l, c]);
        events.push([r, -c]);
    }
    events.sort((a, b) => a[0] - b[0]);

    const result: number[][] = [];
    let i = 0;
    let curSum = 0;
    let prevPos: number | null = null;

    while (i < events.length) {
        const pos = events[i][0];
        if (prevPos !== null && pos > prevPos && curSum > 0) {
            result.push([prevPos, pos, curSum]);
        }
        // apply all deltas at this position
        while (i < events.length && events[i][0] === pos) {
            curSum += events[i][1];
            i++;
        }
        prevPos = pos;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $segments
     * @return Integer[][]
     */
    function splitPainting($segments) {
        $events = [];
        foreach ($segments as $seg) {
            [$l, $r, $c] = $seg;
            $events[$l] = ($events[$l] ?? 0) + $c;
            $events[$r] = ($events[$r] ?? 0) - $c;
        }
        ksort($events, SORT_NUMERIC);
        $prev = null;
        $currSum = 0;
        $result = [];
        foreach ($events as $pos => $delta) {
            if ($prev !== null && $currSum > 0 && $prev < $pos) {
                $result[] = [$prev, $pos, $currSum];
            }
            $currSum += $delta;
            $prev = $pos;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func splitPainting(_ segments: [[Int]]) -> [[Int]] {
        var events = [(pos: Int, delta: Int)]()
        for seg in segments {
            let l = seg[0]
            let r = seg[1]
            let c = seg[2]
            events.append((l, c))
            events.append((r, -c))
        }
        events.sort { $0.pos < $1.pos }
        
        var result = [[Int]]()
        var curSum = 0
        var i = 0
        while i < events.count {
            let currentPos = events[i].pos
            // apply all changes at current position
            while i < events.count && events[i].pos == currentPos {
                curSum += events[i].delta
                i += 1
            }
            if i < events.count {
                let nextPos = events[i].pos
                if curSum > 0 {
                    result.append([currentPos, nextPos, curSum])
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitPainting(segments: Array<IntArray>): List<List<Long>> {
        val diff = java.util.TreeMap<Int, Long>()
        for (seg in segments) {
            val l = seg[0]
            val r = seg[1]
            val c = seg[2].toLong()
            diff[l] = (diff[l] ?: 0L) + c
            diff[r] = (diff[r] ?: 0L) - c
        }
        val result = mutableListOf<List<Long>>()
        var curSum = 0L
        var prevPos = 0
        var first = true
        for ((pos, delta) in diff.entries) {
            if (!first) {
                if (curSum > 0 && prevPos < pos) {
                    result.add(listOf(prevPos.toLong(), pos.toLong(), curSum))
                }
            } else {
                first = false
            }
            curSum += delta
            prevPos = pos
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> splitPainting(List<List<int>> segments) {
    final Map<int, int> diff = {};
    for (var seg in segments) {
      int l = seg[0];
      int r = seg[1];
      int c = seg[2];
      diff[l] = (diff[l] ?? 0) + c;
      diff[r] = (diff[r] ?? 0) - c;
    }
    final List<int> points = diff.keys.toList()..sort();
    final List<List<int>> ans = [];
    int currSum = 0;
    int? prevPos;
    for (int x in points) {
      if (prevPos != null && prevPos! < x && currSum > 0) {
        ans.add([prevPos!, x, currSum]);
      }
      currSum += diff[x]!;
      prevPos = x;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func splitPainting(segments [][]int) [][]int64 {
	diff := make(map[int]int64)
	for _, seg := range segments {
		l, r, c := seg[0], seg[1], int64(seg[2])
		diff[l] += c
		diff[r] -= c
	}
	keys := make([]int, 0, len(diff))
	for k := range diff {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	var res [][]int64
	var cur int64
	var prev int
	first := true
	for _, x := range keys {
		if !first && cur > 0 && prev < x {
			res = append(res, []int64{int64(prev), int64(x), cur})
		}
		cur += diff[x]
		prev = x
		first = false
	}
	return res
}
```

## Ruby

```ruby
def split_painting(segments)
  events = Hash.new(0)
  segments.each do |s, e, c|
    events[s] += c
    events[e] -= c
  end

  positions = events.keys.sort
  res = []
  cur_sum = 0
  prev_pos = nil

  positions.each do |pos|
    if !prev_pos.nil? && cur_sum != 0 && prev_pos < pos
      if !res.empty? && res[-1][2] == cur_sum && res[-1][1] == prev_pos
        res[-1][1] = pos
      else
        res << [prev_pos, pos, cur_sum]
      end
    end
    cur_sum += events[pos]
    prev_pos = pos
  end

  res
end
```

## Scala

```scala
object Solution {
    def splitPainting(segments: Array[Array[Int]]): List[List[Long]] = {
        val events = scala.collection.mutable.ArrayBuffer.empty[(Int, Long)]
        for (seg <- segments) {
            val start = seg(0)
            val end   = seg(1)
            val color = seg(2).toLong
            events.append((start,  color))
            events.append((end,   -color))
        }
        val sorted = events.sortBy(_._1)

        var i = 0
        var curSum: Long = 0L
        var prevPos = -1
        val result = scala.collection.mutable.ListBuffer.empty[List[Long]]

        while (i < sorted.length) {
            val pos = sorted(i)._1
            if (prevPos != -1 && pos > prevPos && curSum > 0) {
                result.append(List(prevPos.toLong, pos.toLong, curSum))
            }
            while (i < sorted.length && sorted(i)._1 == pos) {
                curSum += sorted(i)._2
                i += 1
            }
            prevPos = pos
        }

        result.toList
    }
}
```

## Rust

```rust
use std::collections::BTreeMap;

impl Solution {
    pub fn split_painting(segments: Vec<Vec<i32>>) -> Vec<Vec<i64>> {
        let mut diff: BTreeMap<i32, i64> = BTreeMap::new();
        for seg in segments.iter() {
            let start = seg[0];
            let end = seg[1];
            let color = seg[2] as i64;
            *diff.entry(start).or_insert(0) += color;
            *diff.entry(end).or_insert(0) -= color;
        }

        // Collect sorted points with their delta changes
        let points: Vec<(i32, i64)> = diff.into_iter().collect();
        let mut res: Vec<Vec<i64>> = Vec::new();
        let mut cur_sum: i64 = 0;

        for i in 0..points.len() {
            let (pos, delta) = points[i];
            cur_sum += delta;
            if i + 1 < points.len() && cur_sum > 0 {
                let next_pos = points[i + 1].0;
                res.push(vec![pos as i64, next_pos as i64, cur_sum]);
            }
        }

        res
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (split-painting segments)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([events
          (apply append
                 (map (lambda (seg)
                        (match seg
                          [(list l r c) (list (list l c) (list r (- c)))])
                        )
                      segments))]
         [sorted-events (sort events (lambda (a b) (< (first a) (first b))))])
    (define (process evts prev-pos curr-sum acc)
      (if (null? evts)
          (reverse acc)
          (let* ((pos (first (car evts)))
                 (group (take-while (lambda (e) (= (first e) pos)) evts))
                 (rest (drop evts (length group)))
                 (delta-sum (apply + (map second group))))
            (define new-acc
              (if (and prev-pos (< prev-pos pos) (> curr-sum 0))
                  (cons (list prev-pos pos curr-sum) acc)
                  acc))
            (process rest pos (+ curr-sum delta-sum) new-acc))))
    (process sorted-events #f 0 '())))
```

## Erlang

```erlang
-module(solution).
-export([split_painting/1]).

-spec split_painting(Segments :: [[integer()]]) -> [[integer()]].
split_painting(Segments) ->
    Events = lists:foldl(fun([L,R,C], Acc) -> [{L, C}, {R, -C} | Acc] end,
                         [], Segments),
    Sorted = lists:keysort(1, Events),
    process_sorted(Sorted).

process_sorted(Events) ->
    process_sorted(Events, none, 0, []).

process_sorted([], _PrevPos, _CurSum, Acc) ->
    lists:reverse(Acc);
process_sorted([{Pos, Delta} | Rest], none, _CurSum, Acc) ->
    NewSum = Delta,
    process_sorted(Rest, Pos, NewSum, Acc);
process_sorted([{Pos, Delta} | Rest], PrevPos, CurSum, Acc) when Pos == PrevPos ->
    NewSum = CurSum + Delta,
    process_sorted(Rest, PrevPos, NewSum, Acc);
process_sorted([{Pos, Delta} | Rest], PrevPos, CurSum, Acc) ->
    NewAcc = case CurSum of
                0 -> Acc;
                _ -> [[PrevPos, Pos, CurSum] | Acc]
            end,
    NewSum = CurSum + Delta,
    process_sorted(Rest, Pos, NewSum, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec split_painting(segments :: [[integer]]) :: [[integer]]
  def split_painting(segments) do
    events =
      Enum.flat_map(segments, fn [l, r, c] ->
        [{l, c}, {r, -c}]
      end)

    sorted = Enum.sort_by(events, fn {pos, _} -> pos end)

    {stack_rev, _, _} =
      Enum.reduce(sorted, {[], nil, 0}, fn {pos, delta},
                                            {stack_rev, prev_pos, cur_sum} ->
        stack_rev =
          if not is_nil(prev_pos) and prev_pos < pos and cur_sum > 0 do
            case stack_rev do
              [{l, _r, s} | rest] when s == cur_sum ->
                [{l, pos, s} | rest]

              _ ->
                [{prev_pos, pos, cur_sum} | stack_rev]
            end
          else
            stack_rev
          end

        {stack_rev, pos, cur_sum + delta}
      end)

    stack_rev
    |> Enum.reverse()
    |> Enum.map(fn {l, r, s} -> [l, r, s] end)
  end
end
```
