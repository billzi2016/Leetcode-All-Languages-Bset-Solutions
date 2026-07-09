# 2406. Divide Intervals Into Minimum Number of Groups

## Cpp

```cpp
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<pair<int,int>> events;
        events.reserve(intervals.size() * 2);
        for (const auto& iv : intervals) {
            int l = iv[0];
            int r = iv[1];
            events.emplace_back(l, 1);          // interval starts
            events.emplace_back(r + 1, -1);     // interval ends (inclusive)
        }
        sort(events.begin(), events.end());
        int cur = 0, ans = 0;
        for (const auto& e : events) {
            cur += e.second;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minGroups(int[][] intervals) {
        java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>();
        int maxGroups = 0;
        for (int[] interval : intervals) {
            int start = interval[0];
            // Release groups whose intervals end before the current start (strictly less)
            while (!pq.isEmpty() && pq.peek() < start) {
                pq.poll();
            }
            pq.offer(interval[1]); // occupy a group with this interval's end
            maxGroups = Math.max(maxGroups, pq.size());
        }
        return maxGroups;
    }
}
```

## Python

```python
class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()
        cur = ans = 0
        for _, delta in events:
            cur += delta
            if cur > ans:
                ans = cur
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()
        cur = ans = 0
        i = 0
        n = len(events)
        while i < n:
            point = events[i][0]
            delta = 0
            while i < n and events[i][0] == point:
                delta += events[i][1]
                i += 1
            cur += delta
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int point;
    int delta; // +1 for start, -1 for end+1
} Event;

static int cmpEvent(const void *a, const void *b) {
    const Event *ea = (const Event *)a;
    const Event *eb = (const Event *)b;
    if (ea->point != eb->point)
        return ea->point - eb->point;
    // for same point, apply -1 before +1
    return ea->delta - eb->delta;
}

int minGroups(int** intervals, int intervalsSize, int* intervalsColSize){
    if (intervalsSize == 0) return 0;
    int total = intervalsSize * 2;
    Event *events = (Event *)malloc(sizeof(Event) * total);
    int idx = 0;
    for (int i = 0; i < intervalsSize; ++i) {
        int l = intervals[i][0];
        int r = intervals[i][1];
        events[idx].point = l;
        events[idx].delta = 1;
        ++idx;
        events[idx].point = r + 1;
        events[idx].delta = -1;
        ++idx;
    }
    qsort(events, total, sizeof(Event), cmpEvent);
    int cur = 0, best = 0;
    for (int i = 0; i < total; ++i) {
        cur += events[i].delta;
        if (cur > best) best = cur;
    }
    free(events);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinGroups(int[][] intervals) {
        int n = intervals.Length;
        var events = new (int point, int delta)[2 * n];
        int idx = 0;
        foreach (var iv in intervals) {
            events[idx++] = (iv[0], 1);
            events[idx++] = (iv[1] + 1, -1);
        }
        Array.Sort(events, (a, b) => {
            if (a.point != b.point) return a.point.CompareTo(b.point);
            // start (+1) should be processed before end (-1)
            return b.delta.CompareTo(a.delta);
        });
        int cur = 0, max = 0;
        foreach (var e in events) {
            cur += e.delta;
            if (cur > max) max = cur;
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minGroups = function(intervals) {
    const events = [];
    for (const [l, r] of intervals) {
        events.push([l, 1]);          // interval starts
        events.push([r + 1, -1]);     // interval ends (inclusive)
    }
    events.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        // start (+1) should come before end (-1) at the same point
        return b[1] - a[1];
    });
    
    let cur = 0, max = 0;
    for (const [, delta] of events) {
        cur += delta;
        if (cur > max) max = cur;
    }
    return max;
};
```

## Typescript

```typescript
function minGroups(intervals: number[][]): number {
    const events: [number, number][] = [];
    for (const [l, r] of intervals) {
        events.push([l, 1]);
        events.push([r + 1, -1]);
    }
    events.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

    let cur = 0;
    let max = 0;
    for (const [, delta] of events) {
        cur += delta;
        if (cur > max) max = cur;
    }
    return max;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function minGroups($intervals) {
        $events = [];
        foreach ($intervals as $int) {
            $l = $int[0];
            $r = $int[1];
            $events[] = [$l, 1];          // interval starts
            $events[] = [$r + 1, -1];     // interval ends (inclusive)
        }

        usort($events, function ($a, $b) {
            if ($a[0] == $b[0]) {
                // start (+1) should be processed before end (-1) at same point,
                // though with r+1 this rarely happens.
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });

        $curr = 0;
        $max = 0;
        foreach ($events as $e) {
            $curr += $e[1];
            if ($curr > $max) {
                $max = $curr;
            }
        }

        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func minGroups(_ intervals: [[Int]]) -> Int {
        var events = [(Int, Int)]()
        events.reserveCapacity(intervals.count * 2)
        for interval in intervals {
            let left = interval[0]
            let right = interval[1]
            events.append((left, 1))
            events.append((right + 1, -1))
        }
        events.sort { (a, b) -> Bool in
            if a.0 == b.0 {
                return a.1 > b.1   // start (+1) before end (-1) at same point
            } else {
                return a.0 < b.0
            }
        }
        var current = 0
        var maxGroups = 0
        for event in events {
            current += event.1
            if current > maxGroups {
                maxGroups = current
            }
        }
        return maxGroups
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minGroups(intervals: Array<IntArray>): Int {
        val events = ArrayList<Pair<Int, Int>>(intervals.size * 2)
        for (intv in intervals) {
            val l = intv[0]
            val r = intv[1]
            events.add(Pair(l, 1))
            events.add(Pair(r + 1, -1))
        }
        events.sortWith(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        var current = 0
        var maxGroups = 0
        for ((_, delta) in events) {
            current += delta
            if (current > maxGroups) maxGroups = current
        }
        return maxGroups
    }
}
```

## Dart

```dart
class Solution {
  int minGroups(List<List<int>> intervals) {
    List<List<int>> events = [];
    for (var iv in intervals) {
      int start = iv[0];
      int end = iv[1];
      events.add([start, 1]);
      events.add([end + 1, -1]);
    }
    events.sort((a, b) {
      if (a[0] == b[0]) return a[1] - b[1]; // -1 before +1 at same point
      return a[0] - b[0];
    });
    int cur = 0;
    int maxGroups = 0;
    for (var e in events) {
      cur += e[1];
      if (cur > maxGroups) maxGroups = cur;
    }
    return maxGroups;
  }
}
```

## Golang

```go
func minGroups(intervals [][]int) int {
    n := len(intervals)
    starts := make([]int, n)
    ends := make([]int, n)
    for i, iv := range intervals {
        starts[i] = iv[0]
        ends[i] = iv[1]
    }
    sort.Ints(starts)
    sort.Ints(ends)

    cur, maxGroups, i, j := 0, 0, 0, 0
    for i < n {
        if starts[i] > ends[j] {
            cur--
            j++
        } else {
            cur++
            if cur > maxGroups {
                maxGroups = cur
            }
            i++
        }
    }
    return maxGroups
}
```

## Ruby

```ruby
def min_groups(intervals)
  events = []
  intervals.each do |l, r|
    events << [l, 1]
    events << [r + 1, -1]
  end
  events.sort_by! { |p, _| p }
  cur = 0
  max = 0
  events.each do |_p, delta|
    cur += delta
    max = cur if cur > max
  end
  max
end
```

## Scala

```scala
object Solution {
  def minGroups(intervals: Array[Array[Int]]): Int = {
    import scala.collection.mutable.ArrayBuffer
    val events = new ArrayBuffer[(Int, Int)](intervals.length * 2)
    var i = 0
    while (i < intervals.length) {
      val l = intervals(i)(0)
      val r = intervals(i)(1)
      events.append((l, 1))
      events.append((r + 1, -1)) // end is inclusive
      i += 1
    }
    val sorted = events.sortBy(_._1)
    var cur = 0
    var maxGroups = 0
    var idx = 0
    while (idx < sorted.length) {
      cur += sorted(idx)._2
      if (cur > maxGroups) maxGroups = cur
      idx += 1
    }
    maxGroups
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut events = Vec::with_capacity(intervals.len() * 2);
        for iv in intervals.iter() {
            let l = iv[0];
            let r = iv[1];
            events.push((l, 1));
            events.push((r + 1, -1));
        }
        events.sort_by_key(|&(pos, _)| pos);
        let mut cur = 0;
        let mut max_cur = 0;
        for &(_, delta) in events.iter() {
            cur += delta;
            if cur > max_cur {
                max_cur = cur;
            }
        }
        max_cur
    }
}
```

## Racket

```racket
(define/contract (min-groups intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((events
          (let loop ((lst intervals) (acc '()))
            (if (null? lst)
                acc
                (let* ((intv (car lst))
                       (l (first intv))
                       (r (second intv)))
                  (loop (cdr lst)
                        (cons (list (+ r 1) -1)
                              (cons (list l 1) acc)))))))
         (sorted-events (sort events (lambda (a b) (< (first a) (first b))))))
    (let loop ((es sorted-events) (curr 0) (maxc 0))
      (if (null? es)
          maxc
          (let* ((delta (second (car es)))
                 (new-curr (+ curr delta))
                 (new-max (if (> new-curr maxc) new-curr maxc)))
            (loop (cdr es) new-curr new-max)))))
```

## Erlang

```erlang
-module(solution).
-export([min_groups/1]).

-spec min_groups(Intervals :: [[integer()]]) -> integer().
min_groups(Intervals) ->
    Events = lists:foldl(
        fun([L, R], Acc) ->
            [{L, 1}, {R + 1, -1} | Acc]
        end,
        [],
        Intervals
    ),
    Sorted = lists:sort(
        fun({P1, D1}, {P2, D2}) ->
            case P1 < P2 of
                true -> true;
                false when P1 > P2 -> false;
                false -> D1 =< D2  % -1 before +1 at same position
            end
        end,
        Events
    ),
    {Max, _} = lists:foldl(
        fun({_Pos, Delta}, {CurMax, Cur}) ->
            New = Cur + Delta,
            {erlang:max(CurMax, New), New}
        end,
        {0, 0},
        Sorted
    ),
    Max.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_groups(intervals :: [[integer]]) :: integer
  def min_groups(intervals) do
    events =
      Enum.flat_map(intervals, fn [l, r] ->
        [{l, 1}, {r + 1, -1}]
      end)

    sorted =
      Enum.sort(events, fn {a1, v1}, {a2, v2} ->
        if a1 == a2 do
          v1 > v2
        else
          a1 < a2
        end
      end)

    {max_overlap, _} =
      Enum.reduce(sorted, {0, 0}, fn {_pos, delta}, {mx, cur} ->
        cur = cur + delta
        mx = if cur > mx, do: cur, else: mx
        {mx, cur}
      end)

    max_overlap
  end
end
```
