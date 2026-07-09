# 1751. Maximum Number of Events That Can Be Attended II

## Cpp

```cpp
class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        sort(events.begin(), events.end()); // sort by start day
        
        vector<int> starts(n);
        for (int i = 0; i < n; ++i) starts[i] = events[i][0];
        
        // precompute next index for each event
        vector<int> nxt(n);
        for (int i = 0; i < n; ++i) {
            int idx = lower_bound(starts.begin() + i + 1, starts.end(), events[i][1] + 1) - starts.begin();
            nxt[i] = idx;
        }
        
        vector<vector<long long>> dp(k + 1, vector<long long>(n + 1, 0));
        for (int cnt = 1; cnt <= k; ++cnt) {
            for (int i = n - 1; i >= 0; --i) {
                long long take = events[i][2] + dp[cnt - 1][nxt[i]];
                long long skip = dp[cnt][i + 1];
                dp[cnt][i] = max(take, skip);
            }
        }
        return (int)dp[k][0];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxValue(int[][] events, int k) {
        int n = events.length;
        // Sort events by start day
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));
        
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = events[i][0];
        }
        
        // Precompute next index for each event
        int[] nextIdx = new int[n];
        for (int i = 0; i < n; i++) {
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (starts[mid] > events[i][1]) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            nextIdx[i] = lo; // could be n
        }
        
        long[][] dp = new long[k + 1][n + 1]; // initialized to 0
        
        for (int i = n - 1; i >= 0; i--) {
            int value = events[i][2];
            int nxt = nextIdx[i];
            for (int cnt = 1; cnt <= k; cnt++) {
                long skip = dp[cnt][i + 1];
                long take = value + dp[cnt - 1][nxt];
                dp[cnt][i] = Math.max(skip, take);
            }
        }
        
        return (int) dp[k][0];
    }
}
```

## Python

```python
class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Sort events by start day
        events.sort(key=lambda x: x[0])
        n = len(events)
        starts = [e[0] for e in events]

        import bisect
        # Precompute the next index for each event using binary search
        next_idx = [bisect.bisect_right(starts, events[i][1]) for i in range(n)]

        # dp[c][i] = max value we can obtain attending at most c events from i..end
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(n - 1, -1, -1):
            val = events[i][2]
            nxt = next_idx[i]
            # iterate over possible counts
            for c in range(1, k + 1):
                take = val + dp[c - 1][nxt]
                skip = dp[c][i + 1]
                dp[c][i] = take if take > skip else skip

        return dp[k][0]
```

## Python3

```python
class Solution:
    def maxValue(self, events, k):
        from bisect import bisect_right
        # Sort events by start day
        events.sort(key=lambda x: x[0])
        n = len(events)
        starts = [e[0] for e in events]
        # Precompute next index for each event (first with start > current end)
        nxt = [bisect_right(starts, events[i][1]) for i in range(n)]
        # dp[c][i]: max value using at most c events from i..n-1
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        # Fill DP bottom-up
        for i in range(n - 1, -1, -1):
            val = events[i][2]
            next_i = nxt[i]
            for c in range(1, k + 1):
                take = val + dp[c - 1][next_i]
                skip = dp[c][i + 1]
                dp[c][i] = take if take > skip else skip
        return dp[k][0]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
    int val;
} Event;

static int cmpEvent(const void *a, const void *b) {
    const Event *ea = (const Event *)a;
    const Event *eb = (const Event *)b;
    if (ea->start != eb->start) return ea->start - eb->start;
    return ea->end - eb->end;
}

int maxValue(int** events, int eventsSize, int* eventsColSize, int k) {
    if (eventsSize == 0 || k == 0) return 0;

    Event *ev = (Event *)malloc(eventsSize * sizeof(Event));
    for (int i = 0; i < eventsSize; ++i) {
        ev[i].start = events[i][0];
        ev[i].end   = events[i][1];
        ev[i].val   = events[i][2];
    }
    qsort(ev, eventsSize, sizeof(Event), cmpEvent);

    int n = eventsSize;
    int *starts = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) starts[i] = ev[i].start;

    int *nextIdx = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int target = ev[i].end + 1;
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (starts[mid] >= target)
                hi = mid;
            else
                lo = mid + 1;
        }
        nextIdx[i] = lo; // may be n
    }

    long long *dp = (long long *)calloc((k + 1) * (n + 1), sizeof(long long));
    #define IDX(c,i) ((c)*(n+1)+(i))

    for (int cnt = 1; cnt <= k; ++cnt) {
        for (int i = n - 1; i >= 0; --i) {
            long long take = ev[i].val + dp[IDX(cnt - 1, nextIdx[i])];
            long long skip = dp[IDX(cnt, i + 1)];
            dp[IDX(cnt, i)] = (take > skip ? take : skip);
        }
    }

    int result = (int)dp[IDX(k, 0)];

    free(ev);
    free(starts);
    free(nextIdx);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxValue(int[][] events, int k) {
        int n = events.Length;
        Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) starts[i] = events[i][0];

        int[] nextIdx = new int[n];
        for (int i = 0; i < n; i++) {
            int lo = i + 1, hi = n;
            int end = events[i][1];
            while (lo < hi) {
                int mid = lo + ((hi - lo) >> 1);
                if (starts[mid] > end) hi = mid;
                else lo = mid + 1;
            }
            nextIdx[i] = lo;
        }

        long[,] dp = new long[k + 1, n + 1];
        for (int i = n - 1; i >= 0; --i) {
            int val = events[i][2];
            int nxt = nextIdx[i];
            for (int rem = 1; rem <= k; ++rem) {
                long skip = dp[rem, i + 1];
                long take = val + dp[rem - 1, nxt];
                dp[rem, i] = skip > take ? skip : take;
            }
        }

        return (int)dp[k, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValue = function(events, k) {
    // Sort events by start day
    events.sort((a, b) => a[0] - b[0]);
    const n = events.length;
    const starts = events.map(e => e[0]);

    // Precompute next index for each event using binary search
    const nextIdx = new Array(n);
    for (let i = 0; i < n; i++) {
        let lo = i + 1, hi = n;
        const endDay = events[i][1];
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (starts[mid] > endDay) hi = mid;
            else lo = mid + 1;
        }
        nextIdx[i] = lo; // first event with start > current end
    }

    // dp[count][i] = max value using at most 'count' events from i..n-1
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(0));

    for (let cnt = 1; cnt <= k; cnt++) {
        for (let i = n - 1; i >= 0; i--) {
            const take = events[i][2] + dp[cnt - 1][nextIdx[i]];
            const skip = dp[cnt][i + 1];
            dp[cnt][i] = take > skip ? take : skip;
        }
    }

    return dp[k][0];
};
```

## Typescript

```typescript
function maxValue(events: number[][], k: number): number {
    // Sort events by start day
    events.sort((a, b) => a[0] - b[0]);
    const n = events.length;
    const starts = events.map(e => e[0]);

    // Precompute next index for each event using binary search
    const nextIdx = new Array<number>(n);
    for (let i = 0; i < n; ++i) {
        let l = 0, r = n;
        const endDay = events[i][1];
        while (l < r) {
            const m = (l + r) >> 1;
            if (starts[m] > endDay) r = m;
            else l = m + 1;
        }
        nextIdx[i] = l; // could be n
    }

    // dp[c][i]: max value using at most c events from i..n-1
    const dp: Float64Array[] = Array.from({ length: k + 1 }, () => new Float64Array(n + 1));

    for (let cnt = 1; cnt <= k; ++cnt) {
        const cur = dp[cnt];
        const prev = dp[cnt - 1];
        // iterate events backwards
        for (let i = n - 1; i >= 0; --i) {
            const skip = cur[i + 1];
            const take = events[i][2] + prev[nextIdx[i]];
            cur[i] = skip > take ? skip : take;
        }
    }

    return dp[k][0];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $events
     * @param Integer $k
     * @return Integer
     */
    function maxValue($events, $k) {
        // Sort events by start day
        usort($events, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        $n = count($events);
        if ($n == 0 || $k == 0) return 0;

        // Extract start days for binary search
        $starts = [];
        foreach ($events as $ev) {
            $starts[] = $ev[0];
        }

        // Precompute next index for each event
        $nextIdx = array_fill(0, $n, $n);
        for ($i = 0; $i < $n; $i++) {
            $target = $events[$i][1]; // end day of current event
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($starts[$mid] > $target) {
                    $hi = $mid;
                } else {
                    $lo = $mid + 1;
                }
            }
            $nextIdx[$i] = $lo; // could be $n (no further event)
        }

        // DP table: dp[count][index]
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, 0));

        for ($i = $n - 1; $i >= 0; $i--) {
            $value = $events[$i][2];
            $next = $nextIdx[$i];
            for ($cnt = 1; $cnt <= $k; $cnt++) {
                $skip = $dp[$cnt][$i + 1];
                $take = $value + $dp[$cnt - 1][$next];
                $dp[$cnt][$i] = ($skip > $take) ? $skip : $take;
            }
        }

        return $dp[$k][0];
    }
}
```

## Swift

```swift
class Solution {
    func maxValue(_ events: [[Int]], _ k: Int) -> Int {
        let sortedEvents = events.sorted { $0[0] < $1[0] }
        let n = sortedEvents.count
        var starts = [Int]()
        starts.reserveCapacity(n)
        for e in sortedEvents {
            starts.append(e[0])
        }
        
        // precompute next indices using binary search
        var nextIdx = Array(repeating: n, count: n)
        for i in 0..<n {
            let endDay = sortedEvents[i][1]
            var l = 0
            var r = n
            while l < r {
                let m = (l + r) >> 1
                if starts[m] <= endDay {
                    l = m + 1
                } else {
                    r = m
                }
            }
            nextIdx[i] = l
        }
        
        // dp[count][i] = max value using at most count events from i..n-1
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: k + 1)
        
        if k == 0 || n == 0 { return 0 }
        
        for cnt in 1...k {
            var i = n - 1
            while i >= 0 {
                let take = sortedEvents[i][2] + dp[cnt - 1][nextIdx[i]]
                let skip = dp[cnt][i + 1]
                dp[cnt][i] = max(skip, take)
                i -= 1
            }
        }
        
        return dp[k][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValue(events: Array<IntArray>, k: Int): Int {
        if (events.isEmpty() || k == 0) return 0
        // Sort events by start day
        val sorted = events.sortedBy { it[0] }
        val n = sorted.size
        val starts = IntArray(n) { sorted[it][0] }

        // Precompute next index for each event using binary search
        val nextIdx = IntArray(n)
        for (i in 0 until n) {
            val target = sorted[i][1] + 1 // first start > end
            var l = 0
            var r = n
            while (l < r) {
                val m = (l + r) ushr 1
                if (starts[m] >= target) r = m else l = m + 1
            }
            nextIdx[i] = l // could be n
        }

        // dp[count][i] = max value using at most count events from i..n-1
        val dp = Array(k + 1) { LongArray(n + 1) } // initialized to 0

        for (i in n - 1 downTo 0) {
            for (cnt in 1..k) {
                val skip = dp[cnt][i + 1]
                val take = sorted[i][2].toLong() + dp[cnt - 1][nextIdx[i]]
                dp[cnt][i] = if (skip > take) skip else take
            }
        }

        return dp[k][0].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxValue(List<List<int>> events, int k) {
    // Sort events by start day
    events.sort((a, b) => a[0].compareTo(b[0]));
    int n = events.length;

    // Extract start days for binary search
    List<int> starts = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      starts[i] = events[i][0];
    }

    // Precompute next index for each event
    List<int> next = List.filled(n, n);
    for (int i = 0; i < n; ++i) {
      int lo = 0, hi = n;
      int target = events[i][1]; // end day of current event
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (starts[mid] > target) {
          hi = mid;
        } else {
          lo = mid + 1;
        }
      }
      next[i] = lo; // first event with start > end
    }

    // DP table: dp[count][i] = max value using at most 'count' events from i..n-1
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n + 1, 0));

    for (int i = n - 1; i >= 0; --i) {
      int val = events[i][2];
      int nxt = next[i];
      for (int cnt = 1; cnt <= k; ++cnt) {
        int take = val + dp[cnt - 1][nxt];
        int skip = dp[cnt][i + 1];
        dp[cnt][i] = take > skip ? take : skip;
      }
    }

    return dp[k][0];
  }
}
```

## Golang

```go
import "sort"

func maxValue(events [][]int, k int) int {
    sort.Slice(events, func(i, j int) bool { return events[i][0] < events[j][0] })
    n := len(events)
    starts := make([]int, n)
    for i := 0; i < n; i++ {
        starts[i] = events[i][0]
    }

    nextIdx := make([]int, n)
    for i := 0; i < n; i++ {
        lo, hi := 0, n
        target := events[i][1]
        for lo < hi {
            mid := (lo + hi) / 2
            if starts[mid] > target {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        nextIdx[i] = lo // may be n
    }

    dp := make([][]int64, k+1)
    for i := 0; i <= k; i++ {
        dp[i] = make([]int64, n+1) // initialized to 0
    }

    for cnt := 1; cnt <= k; cnt++ {
        for i := n - 1; i >= 0; i-- {
            take := int64(events[i][2]) + dp[cnt-1][nextIdx[i]]
            if dp[cnt][i+1] > take {
                dp[cnt][i] = dp[cnt][i+1]
            } else {
                dp[cnt][i] = take
            }
        }
    }

    return int(dp[k][0])
}
```

## Ruby

```ruby
def max_value(events, k)
  events.sort_by! { |e| e[0] }
  n = events.length
  starts = events.map { |e| e[0] }

  next_idx = Array.new(n, n)
  (0...n).each do |i|
    end_day = events[i][1]
    l = 0
    r = n
    while l < r
      m = (l + r) / 2
      if starts[m] <= end_day
        l = m + 1
      else
        r = m
      end
    end
    next_idx[i] = l
  end

  dp = Array.new(k + 1) { Array.new(n + 1, 0) }

  (n - 1).downto(0) do |i|
    nxt = next_idx[i]
    val = events[i][2]
    cnt = 1
    while cnt <= k
      skip = dp[cnt][i + 1]
      take = val + dp[cnt - 1][nxt]
      dp[cnt][i] = skip > take ? skip : take
      cnt += 1
    end
  end

  dp[k][0]
end
```

## Scala

```scala
object Solution {
  import scala.collection.Searching._

  def maxValue(events: Array[Array[Int]], k: Int): Int = {
    val sorted = events.sortBy(_(0))
    val n = sorted.length
    val starts = new Array[Int](n)
    val ends = new Array[Int](n)
    val vals = new Array[Int](n)

    var i = 0
    while (i < n) {
      starts(i) = sorted(i)(0)
      ends(i) = sorted(i)(1)
      vals(i) = sorted(i)(2)
      i += 1
    }

    // Precompute next indices using binary search (upper bound on end day)
    val nextIdx = new Array[Int](n)
    i = 0
    while (i < n) {
      val target = ends(i) + 1
      val idx = starts.search(target) match {
        case Found(pos) => pos
        case InsertionPoint(pos) => pos
      }
      nextIdx(i) = idx
      i += 1
    }

    // dp(cnt)(pos): max value using at most cnt events starting from position pos
    val dp = Array.ofDim[Long](k + 1, n + 1)

    var pos = n - 1
    while (pos >= 0) {
      var cnt = 1
      while (cnt <= k) {
        val skip = dp(cnt)(pos + 1)
        val take = vals(pos).toLong + dp(cnt - 1)(nextIdx(pos))
        dp(cnt)(pos) = if (skip > take) skip else take
        cnt += 1
      }
      pos -= 1
    }

    dp(k)(0).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_value(events: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = events.len();
        if n == 0 || k == 0 {
            return 0;
        }
        // Convert and sort by start day
        let mut ev: Vec<(i32, i32, i32)> = events.iter().map(|v| (v[0], v[1], v[2])).collect();
        ev.sort_by_key(|x| x.0);
        let starts: Vec<i32> = ev.iter().map(|&(s, _, _)| s).collect();

        // Precompute next index for each event
        let mut next_idx = vec![n; n];
        for i in 0..n {
            let end_day = ev[i].1;
            // binary search first start > end_day
            let mut l = 0usize;
            let mut r = n;
            while l < r {
                let m = (l + r) / 2;
                if starts[m] <= end_day {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            next_idx[i] = l; // could be n
        }

        let k_usize = k as usize;
        // dp[count][i] = max value using at most count events starting from i
        let mut dp = vec![vec![0i64; n + 1]; k_usize + 1];

        for i in (0..n).rev() {
            for cnt in 1..=k_usize {
                let skip = dp[cnt][i + 1];
                let take = ev[i].2 as i64 + dp[cnt - 1][next_idx[i]];
                dp[cnt][i] = if skip > take { skip } else { take };
            }
        }

        dp[k_usize][0] as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (max-value events k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted (sort events (lambda (a b) (< (first a) (first b)))))
         (n (length sorted))
         (starts (list->vector (map first sorted)))
         (ends   (list->vector (map second sorted)))
         (vals   (list->vector (map third sorted))))
    ;; pre‑compute next index for each event
    (define next-idx (make-vector n 0))
    (for ([i (in-range n)])
      (let* ((target (+ (vector-ref ends i) 1)) ; need start > end
             (lo 0)
             (hi n))
        (let loop ()
          (if (< lo hi)
              (let* ((mid (quotient (+ lo hi) 2))
                     (s   (vector-ref starts mid)))
                (if (< s target)
                    (begin (set! lo (+ mid 1)) (loop))
                    (begin (set! hi mid) (loop))))
              (vector-set! next-idx i lo)))))
    ;; dp[c][i] = max value using at most c events starting from i
    (define dp (make-vector (+ k 1)))
    (for ([c (in-range (+ k 1))])
      (vector-set! dp c (make-vector (+ n 1) 0))) ; extra column for i=n (all zeros)
    ;; fill DP bottom‑up
    (for ([i (in-range (- n 1) -1 -1)])
      (let ((nexti (vector-ref next-idx i)))
        (for ([c (in-range 1 (+ k 1))])
          (define skip (vector-ref (vector-ref dp c) (+ i 1)))
          (define take (+ (vector-ref vals i)
                          (vector-ref (vector-ref dp (- c 1)) nexti)))
          (vector-set! (vector-ref dp c) i (max skip take)))))
    ;; answer
    (vector-ref (vector-ref dp k) 0)))
```

## Erlang

```erlang
-spec max_value(Events :: [[integer()]], K :: integer()) -> integer().
max_value(Events, K) ->
    % Convert each event to a tuple for easier handling
    EventTuples = [list_to_tuple(E) || E <- Events],
    % Sort events by start day
    SortedEvents = lists:sort(fun({S1,_,_},{S2,_,_}) -> S1 =< S2 end,
                              EventTuples),
    N = length(SortedEvents),

    % Extract starts and convert to tuple for O(1) access
    StartsList = [element(1, Ev) || Ev <- SortedEvents],
    StartsTuple = list_to_tuple(StartsList),

    EventsTuple = list_to_tuple(SortedEvents),

    % Pre‑compute next indices using binary search
    NextList = build_next_indices(N, EventsTuple, StartsTuple),
    NextTuple = list_to_tuple(NextList),

    % DP base case for 0 events: all zeros
    ZeroTuple = list_to_tuple(lists:duplicate(N + 1, 0)),

    % Build DP tables for counts 0..K
    DPList = build_dp(K, N, EventsTuple, NextTuple, ZeroTuple),

    % Result is dp[K][0]
    ResultTuple = lists:nth(K + 1, DPList),   % K+1 because list is 1‑based and includes count 0
    element(1, ResultTuple).

%%--------------------------------------------------------------------
%% Build next indices: for each event i find the first index j such that
%% start[j] > end[i]. Returns a list of length N.
%%--------------------------------------------------------------------
-spec build_next_indices(integer(), tuple(), tuple()) -> [integer()].
build_next_indices(N, EventsTuple, StartsTuple) ->
    build_next_indices(0, N - 1, EventsTuple, StartsTuple, []).

-spec build_next_indices(integer(), integer(), tuple(), tuple(), [integer()]) -> [integer()].
build_next_indices(I, MaxI, _EventsTuple, _StartsTuple, Acc) when I > MaxI ->
    lists:reverse(Acc);
build_next_indices(I, MaxI, EventsTuple, StartsTuple, Acc) ->
    {_, End, _} = element(I + 1, EventsTuple),
    NextIdx = binary_search_gt(StartsTuple, End, 0, tuple_size(StartsTuple)),
    build_next_indices(I + 1, MaxI, EventsTuple, StartsTuple, [NextIdx | Acc]).

%% Binary search for first index with value > End (exclusive upper bound)
-spec binary_search_gt(tuple(), integer(), integer(), integer()) -> integer().
binary_search_gt(Tuple, End, Low, High) when Low >= High ->
    Low;
binary_search_gt(Tuple, End, Low, High) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid + 1, Tuple),
    if
        MidVal > End -> binary_search_gt(Tuple, End, Low, Mid);
        true         -> binary_search_gt(Tuple, End, Mid + 1, High)
    end.

%%--------------------------------------------------------------------
%% Build DP tables for counts from 0 to K.
%% Returns a list where element (C+1) is the tuple dp[C] (size N+1).
%%--------------------------------------------------------------------
-spec build_dp(integer(), integer(), tuple(), tuple(), tuple()) -> [tuple()].
build_dp(K, N, EventsTuple, NextTuple, ZeroTuple) ->
    build_dp(1, K, N, EventsTuple, NextTuple, [ZeroTuple]).

-spec build_dp(integer(), integer(), integer(), tuple(), tuple(), [tuple()]) -> [tuple()].
build_dp(Cur, K, _N, _EventsTuple, _NextTuple, Acc) when Cur > K ->
    lists:reverse(Acc);
build_dp(Cur, K, N, EventsTuple, NextTuple, Acc) ->
    PrevTuple = hd(Acc),                     % dp for count Cur-1
    CurrTuple = build_curr(N - 1, [0], PrevTuple, EventsTuple, NextTuple),
    build_dp(Cur + 1, K, N, EventsTuple, NextTuple, [CurrTuple | Acc]).

%%--------------------------------------------------------------------
%% Build DP row for a specific count.
%% Traverses events backwards, accumulating results.
%% Returns a tuple of size N+1 where index 0 corresponds to dp[i].
%%--------------------------------------------------------------------
-spec build_curr(integer(), [integer()], tuple(), tuple(), tuple()) -> tuple().
build_curr(-1, Acc, _PrevTuple, _EventsTuple, _NextTuple) ->
    list_to_tuple(Acc);
build_curr(I, Acc, PrevTuple, EventsTuple, NextTuple) ->
    {_, _, Val} = element(I + 1, EventsTuple),
    NextIdx = element(I + 1, NextTuple),
    Take = Val + element(NextIdx + 1, PrevTuple),
    Skip = hd(Acc),
    Best = if Take > Skip -> Take; true -> Skip end,
    build_curr(I - 1, [Best | Acc], PrevTuple, EventsTuple, NextTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_value(events :: [[integer]], k :: integer) :: integer
  def max_value(events, k) do
    sorted = Enum.sort_by(events, fn [s, _, _] -> s end)
    n = length(sorted)

    starts_list = for [s, _, _] <- sorted, do: s
    ends_list = for [_, e, _] <- sorted, do: e
    vals_list = for [_, _, v] <- sorted, do: v

    starts_t = List.to_tuple(starts_list)
    ends_t = List.to_tuple(ends_list)
    vals_t = List.to_tuple(vals_list)

    next_idx =
      0..(n - 1)
      |> Enum.map(fn i ->
        end_day = elem(ends_t, i + 1)
        binary_search(starts_t, n, end_day)
      end)

    size = (k + 1) * (n + 1)
    dp = :array.new(size, default: 0)

    indices_desc = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    dp =
      Enum.reduce(1..k, dp, fn cnt, dp_acc ->
        Enum.reduce(indices_desc, dp_acc, fn i, dp_inner ->
          skip = :array.get(cnt * (n + 1) + (i + 1), dp_inner)

          take =
            elem(vals_t, i + 1) +
              :array.get((cnt - 1) * (n + 1) + Enum.at(next_idx, i), dp_inner)

          val = if skip > take, do: skip, else: take
          :array.set(cnt * (n + 1) + i, val, dp_inner)
        end)
      end)

    :array.get(k * (n + 1) + 0, dp)
  end

  defp binary_search(starts_t, n, target) do
    lo = 0
    hi = n
    binary_search_loop(starts_t, target, lo, hi)
  end

  defp binary_search_loop(_starts_t, _target, lo, hi) when lo >= hi, do: lo

  defp binary_search_loop(starts_t, target, lo, hi) do
    mid = div(lo + hi, 2)
    start_mid = elem(starts_t, mid + 1)

    if start_mid <= target do
      binary_search_loop(starts_t, target, mid + 1, hi)
    else
      binary_search_loop(starts_t, target, lo, mid)
    end
  end
end
```
