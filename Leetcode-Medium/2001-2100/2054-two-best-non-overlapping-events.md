# 2054. Two Best Non-Overlapping Events

## Cpp

```cpp
class Solution {
public:
    int maxTwoEvents(std::vector<std::vector<int>>& events) {
        std::sort(events.begin(), events.end(),
                  [](const auto& a, const auto& b){ return a[0] < b[0]; });
        int n = events.size();
        std::vector<int> starts(n);
        for (int i = 0; i < n; ++i) starts[i] = events[i][0];
        
        std::vector<long long> suffixMax(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffixMax[i] = std::max(suffixMax[i + 1], (long long)events[i][2]);
        }
        
        long long ans = suffixMax[0]; // best single event
        for (int i = 0; i < n; ++i) {
            int end = events[i][1];
            long long val = events[i][2];
            int idx = std::lower_bound(starts.begin(), starts.end(), end + 1) - starts.begin();
            if (idx < n) {
                ans = std::max(ans, val + suffixMax[idx]);
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxTwoEvents(int[][] events) {
        // Sort events by start time
        java.util.Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (x, y) -> Integer.compare(x[0], y[0]) // compare by end time
        );
        
        int maxPrev = 0; // best value of an event that ended before current start
        int answer = 0;
        
        for (int[] e : events) {
            int start = e[0];
            int end = e[1];
            int val = e[2];
            
            while (!pq.isEmpty() && pq.peek()[0] < start) {
                maxPrev = Math.max(maxPrev, pq.poll()[1]);
            }
            
            answer = Math.max(answer, Math.max(val, maxPrev + val));
            pq.offer(new int[]{end, val});
        }
        
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events by their ending time
        events.sort(key=lambda x: x[1])
        ends = [e for _, e, _ in events]

        # prefix_max[i] = max value among events[0..i]
        prefix_max = []
        cur_max = 0
        for s, e, v in events:
            if v > cur_max:
                cur_max = v
            prefix_max.append(cur_max)

        import bisect
        ans = 0
        for s, e, v in events:
            # Find the last event that ends before this event starts (strictly less)
            idx = bisect.bisect_left(ends, s) - 1
            if idx >= 0:
                ans = max(ans, v + prefix_max[idx])
            else:
                ans = max(ans, v)
        return ans
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by their ending time
        events.sort(key=lambda x: x[1])
        ends = [e[1] for e in events]

        # best_prefix[i] = maximum value among events[0..i]
        best_prefix = []
        cur_max = 0
        for ev in events:
            cur_max = max(cur_max, ev[2])
            best_prefix.append(cur_max)

        ans = 0
        for i, ev in enumerate(events):
            start, _, val = ev
            # Consider taking only this event
            ans = max(ans, val)
            # Find the best non‑overlapping previous event
            idx = bisect.bisect_left(ends, start) - 1
            if idx >= 0:
                ans = max(ans, val + best_prefix[idx])

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int s;
    int e;
    int v;
} Event;

static int cmpEvent(const void *a, const void *b) {
    const Event *ea = (const Event *)a;
    const Event *eb = (const Event *)b;
    if (ea->s != eb->s) return ea->s - eb->s;
    return ea->e - eb->e;
}

int maxTwoEvents(int** events, int eventsSize, int* eventsColSize) {
    int n = eventsSize;
    if (n == 0) return 0;

    Event *ev = (Event *)malloc(sizeof(Event) * n);
    for (int i = 0; i < n; ++i) {
        ev[i].s = events[i][0];
        ev[i].e = events[i][1];
        ev[i].v = events[i][2];
    }

    qsort(ev, n, sizeof(Event), cmpEvent);

    int *suffixMax = (int *)malloc(sizeof(int) * (n + 1));
    suffixMax[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        suffixMax[i] = ev[i].v > suffixMax[i + 1] ? ev[i].v : suffixMax[i + 1];
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (ev[i].v > ans) ans = ev[i].v;   // single event case

        // binary search first event with start > current end
        int lo = i + 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (ev[mid].s > ev[i].e)
                hi = mid;
            else
                lo = mid + 1;
        }
        if (lo < n) {
            int cand = ev[i].v + suffixMax[lo];
            if (cand > ans) ans = cand;
        }
    }

    free(suffixMax);
    free(ev);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxTwoEvents(int[][] events)
    {
        // Sort events by start time
        Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));
        int n = events.Length;

        // suffixMax[i] = max value among events starting at index i or later
        int[] suffixMax = new int[n + 1];
        for (int i = n - 1; i >= 0; --i)
        {
            suffixMax[i] = Math.Max(events[i][2], suffixMax[i + 1]);
        }

        // Extract start times for binary search
        int[] starts = new int[n];
        for (int i = 0; i < n; ++i) starts[i] = events[i][0];

        int answer = suffixMax[0]; // best single event

        for (int i = 0; i < n; ++i)
        {
            int end = events[i][1];
            // Find first event with start > current end
            int lo = i + 1, hi = n;
            while (lo < hi)
            {
                int mid = (lo + hi) >> 1;
                if (starts[mid] > end) hi = mid;
                else lo = mid + 1;
            }
            int nxt = lo; // index of next non‑overlapping event
            if (nxt < n)
            {
                answer = Math.Max(answer, events[i][2] + suffixMax[nxt]);
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    const n = events.length;
    // Sort events by start time.
    const byStart = events.slice().sort((a, b) => a[0] - b[0]);
    // Sort events by end time, keep only end and value.
    const byEnd = events.map(e => [e[1], e[2]]).sort((a, b) => a[0] - b[0]);

    let maxPrev = 0;   // best value of an event that ends before current start
    let ans = 0;
    let i = 0;         // pointer in byEnd

    for (const ev of byStart) {
        const start = ev[0];
        const val = ev[2];

        while (i < n && byEnd[i][0] < start) { // end < start (non‑overlapping)
            maxPrev = Math.max(maxPrev, byEnd[i][1]);
            i++;
        }
        ans = Math.max(ans, maxPrev + val);
    }

    return ans;
};
```

## Typescript

```typescript
function maxTwoEvents(events: number[][]): number {
    // Sort events by their start time
    events.sort((a, b) => a[0] - b[0]);
    const n = events.length;
    const starts = new Array<number>(n);
    for (let i = 0; i < n; ++i) starts[i] = events[i][0];

    // maxSuffix[i] = maximum value among events from i to end
    const maxSuffix = new Array<number>(n + 1);
    maxSuffix[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        maxSuffix[i] = Math.max(events[i][2], maxSuffix[i + 1]);
    }

    let ans = maxSuffix[0]; // best single event

    for (let i = 0; i < n; ++i) {
        const end = events[i][1];
        // binary search first index with start > end
        let lo = i + 1, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (starts[mid] > end) hi = mid;
            else lo = mid + 1;
        }
        const nxt = lo;
        if (nxt < n) {
            ans = Math.max(ans, events[i][2] + maxSuffix[nxt]);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxTwoEvents($events) {
        $times = [];
        foreach ($events as $ev) {
            $s = $ev[0];
            $e = $ev[1];
            $v = $ev[2];
            $times[] = [$s, 1, $v];          // start
            $times[] = [$e + 1, 0, $v];      // end (exclusive)
        }
        usort($times, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1]; // process ends before starts at same time
            }
            return $a[0] <=> $b[0];
        });
        $maxValue = 0;
        $ans = 0;
        foreach ($times as $t) {
            [$time, $type, $value] = $t;
            if ($type == 1) { // start
                $candidate = $value + $maxValue;
                if ($candidate > $ans) {
                    $ans = $candidate;
                }
            } else { // end
                if ($value > $maxValue) {
                    $maxValue = $value;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxTwoEvents(_ events: [[Int]]) -> Int {
        var points = [(time: Int, type: Int, value: Int)]()
        points.reserveCapacity(events.count * 2)
        for ev in events {
            let s = ev[0]
            let e = ev[1]
            let v = ev[2]
            points.append((time: s, type: 1, value: v))          // start
            points.append((time: e + 1, type: 0, value: v))      // end (exclusive)
        }
        points.sort {
            if $0.time == $1.time {
                return $0.type < $1.type   // end (0) before start (1) at same time
            } else {
                return $0.time < $1.time
            }
        }
        var maxEnded = 0
        var answer = 0
        for p in points {
            if p.type == 0 {
                if p.value > maxEnded { maxEnded = p.value }
            } else {
                let candidate = p.value + maxEnded
                if candidate > answer { answer = candidate }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTwoEvents(events: Array<IntArray>): Int {
        val n = events.size
        events.sortWith(compareBy({ it[0] }, { it[1] }))
        val starts = IntArray(n)
        val ends = IntArray(n)
        val vals = IntArray(n)
        for (i in 0 until n) {
            starts[i] = events[i][0]
            ends[i] = events[i][1]
            vals[i] = events[i][2]
        }
        val suffixMax = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            suffixMax[i] = maxOf(vals[i], suffixMax[i + 1])
        }
        var ans = 0
        for (i in 0 until n) {
            ans = maxOf(ans, vals[i]) // single event
            val idx = lowerBound(starts, ends[i])
            if (idx < n) {
                ans = maxOf(ans, vals[i] + suffixMax[idx])
            }
        }
        return ans
    }

    private fun lowerBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (arr[m] > target) {
                r = m
            } else {
                l = m + 1
            }
        }
        return l
    }
}
```

## Dart

```dart
class Solution {
  int maxTwoEvents(List<List<int>> events) {
    List<List<int>> times = [];
    for (var e in events) {
      int s = e[0];
      int en = e[1];
      int v = e[2];
      times.add([s, 1, v]); // start
      times.add([en + 1, 0, v]); // end+1
    }
    times.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return a[1] - b[1]; // end (0) before start (1)
    });
    int maxVal = 0;
    int ans = 0;
    for (var t in times) {
      if (t[1] == 0) {
        if (t[2] > maxVal) maxVal = t[2];
      } else {
        int sum = t[2] + maxVal;
        if (sum > ans) ans = sum;
      }
    }
    return ans;
  }
}
```

## Golang

```go
type eventPoint struct {
    time int
    typ  int // 0 = end, 1 = start
    val  int
}

func maxTwoEvents(events [][]int) int {
    points := make([]eventPoint, 0, len(events)*2)
    for _, e := range events {
        s, en, v := e[0], e[1], e[2]
        points = append(points, eventPoint{time: s, typ: 1, val: v})
        points = append(points, eventPoint{time: en + 1, typ: 0, val: v})
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].time != points[j].time {
            return points[i].time < points[j].time
        }
        return points[i].typ < points[j].typ // end (0) before start (1)
    })

    maxVal := 0
    ans := 0
    for _, p := range points {
        if p.typ == 1 { // start
            if maxVal+p.val > ans {
                ans = maxVal + p.val
            }
        } else { // end
            if p.val > maxVal {
                maxVal = p.val
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_two_events(events)
  times = []
  events.each do |s, e, v|
    times << [s, 1, v]       # start
    times << [e + 1, 0, v]   # end (exclusive)
  end

  times.sort_by! { |t| [t[0], t[1]] }

  max_val = 0
  ans = 0
  times.each do |_, typ, val|
    if typ == 0
      max_val = val if val > max_val
    else
      cur = max_val + val
      ans = cur if cur > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def maxTwoEvents(events: Array[Array[Int]]): Int = {
    // Convert to tuple and sort by start time
    val ev = events.map(a => (a(0), a(1), a(2))).sortBy(_._1)
    val n = ev.length
    if (n == 0) return 0

    // Array of start times for binary search
    val starts = new Array[Int](n)
    var i = 0
    while (i < n) {
      starts(i) = ev(i)._1
      i += 1
    }

    // suffixMax[i] = max value among events from i to end
    val suffixMax = new Array[Int](n + 1)
    i = n - 1
    while (i >= 0) {
      suffixMax(i) = math.max(ev(i)._3, suffixMax(i + 1))
      i -= 1
    }

    var ans = 0
    i = 0
    while (i < n) {
      val curVal = ev(i)._3
      if (curVal > ans) ans = curVal

      // binary search for first event with start > current end
      var lo = i + 1
      var hi = n
      val curEnd = ev(i)._2
      while (lo < hi) {
        val mid = lo + ((hi - lo) >> 1)
        if (starts(mid) > curEnd) hi = mid else lo = mid + 1
      }
      if (lo < n) {
        val sum = curVal + suffixMax(lo)
        if (sum > ans) ans = sum
      }

      i += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_two_events(events: Vec<Vec<i32>>) -> i32 {
        // Convert to tuple vector and sort by start time
        let mut ev: Vec<(i32, i32, i32)> = events
            .into_iter()
            .map(|v| (v[0], v[1], v[2]))
            .collect();
        ev.sort_by_key(|e| e.0);
        let n = ev.len();

        // suffix_max[i] = max value among events[i..]
        let mut suffix_max = vec![0; n + 1];
        for i in (0..n).rev() {
            suffix_max[i] = std::cmp::max(ev[i].2, suffix_max[i + 1]);
        }

        let mut best_single = 0;
        let mut best_pair = 0;

        for &(start, end, value) in &ev {
            if value > best_single {
                best_single = value;
            }
            // first index with start > current event's end
            let nxt = ev.partition_point(|&(s, _, _)| s <= end);
            let total = if nxt < n { value + suffix_max[nxt] } else { value };
            if total > best_pair {
                best_pair = total;
            }
        }

        std::cmp::max(best_single, best_pair)
    }
}
```

## Racket

```racket
(define/contract (max-two-events events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted (sort events (lambda (a b) (< (first a) (first b))))]
         [n (length sorted)]
         [ev-vec (list->vector sorted)]
         [starts (make-vector n)]
         [ends (make-vector n)]
         [vals (make-vector n)])
    ;; fill vectors with start, end, value
    (for ([i (in-range n)])
      (let* ([e (vector-ref ev-vec i)]
             [s (first e)]
             [en (second e)]
             [v (third e)])
        (vector-set! starts i s)
        (vector-set! ends i en)
        (vector-set! vals i v)))
    ;; suffix maximum of single-event values
    (define suffix (make-vector (+ n 1) 0))
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ([v (vector-ref vals i)]
             [next (vector-ref suffix (+ i 1))])
        (vector-set! suffix i (if (> v next) v next))))
    ;; binary search for first event with start > given end
    (define (next-index end)
      (let loop ([lo 0] [hi n])
        (if (= lo hi)
            lo
            (let* ([mid (quotient (+ lo hi) 2)]
                   [s (vector-ref starts mid)])
              (if (> s end)
                  (loop lo mid)
                  (loop (+ mid 1) hi))))))
    ;; compute answer
    (define ans 0)
    (for ([i (in-range n)])
      (let* ([v (vector-ref vals i)]
             [e (vector-ref ends i)]
             [j (next-index e)]
             [candidate (+ v (if (< j n) (vector-ref suffix j) 0))])
        (when (> candidate ans) (set! ans candidate))
        (when (> v ans) (set! ans v))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_two_events/1]).

-spec max_two_events(Events :: [[integer()]]) -> integer().
max_two_events(Events) ->
    Times = lists:foldl(
        fun([S, E, V], Acc) ->
            [{S, 1, V}, {E + 1, 0, V} | Acc]
        end,
        [],
        Events
    ),
    Sorted = lists:sort(Times),
    process(Sorted, 0, 0).

process([], _MaxVal, Ans) -> Ans;
process([{_, 0, V} | Rest], MaxVal, Ans) ->
    NewMax = if V > MaxVal -> V; true -> MaxVal end,
    process(Rest, NewMax, Ans);
process([{_, 1, V} | Rest], MaxVal, Ans) ->
    Sum = MaxVal + V,
    NewAns = if Sum > Ans -> Sum; true -> Ans end,
    process(Rest, MaxVal, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_two_events(events :: [[integer]]) :: integer
  def max_two_events(events) do
    times =
      Enum.flat_map(events, fn [s, e, v] ->
        [{e + 1, 0, v}, {s, 1, v}]
      end)

    sorted = Enum.sort_by(times, fn {t, kind, _v} -> {t, kind} end)

    {ans, _max_val} =
      Enum.reduce(sorted, {0, 0}, fn
        {_t, 1, v}, {ans, max_val} ->
          new_ans = max(ans, v + max_val)
          {new_ans, max_val}
        {_t, 0, v}, {ans, max_val} ->
          new_max = max(max_val, v)
          {ans, new_max}
      end)

    ans
  end
end
```
