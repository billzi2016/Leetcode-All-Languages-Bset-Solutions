# 1235. Maximum Profit in Job Scheduling

## Cpp

```cpp
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        struct Job {int s, e, p;};
        vector<Job> jobs(n);
        for (int i = 0; i < n; ++i) jobs[i] = {startTime[i], endTime[i], profit[i]};
        sort(jobs.begin(), jobs.end(), [](const Job& a, const Job& b){ return a.s < b.s; });
        
        vector<int> starts(n);
        for (int i = 0; i < n; ++i) starts[i] = jobs[i].s;
        
        vector<long long> dp(n + 1, 0); // dp[i]: max profit from i to end
        for (int i = n - 1; i >= 0; --i) {
            int nxt = lower_bound(starts.begin(), starts.end(), jobs[i].e) - starts.begin();
            long long take = jobs[i].p + dp[nxt];
            long long skip = dp[i + 1];
            dp[i] = max(take, skip);
        }
        return (int)dp[0];
    }
};
```

## Java

```java
class Solution {
    private static class Job {
        int start;
        int end;
        int profit;
        Job(int s, int e, int p) {
            this.start = s;
            this.end = e;
            this.profit = p;
        }
    }

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        Job[] jobs = new Job[n];
        for (int i = 0; i < n; i++) {
            jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
        }
        java.util.Arrays.sort(jobs, (a, b) -> Integer.compare(a.start, b.start));

        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = jobs[i].start;
        }

        long[] dp = new long[n + 1]; // dp[i]: max profit from i to end
        for (int i = n - 1; i >= 0; i--) {
            int nextIdx = lowerBound(starts, jobs[i].end);
            long include = jobs[i].profit + dp[nextIdx];
            long exclude = dp[i + 1];
            dp[i] = Math.max(include, exclude);
        }
        return (int) dp[0];
    }

    // first index with value >= target
    private int lowerBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        starts = [job[0] for job in jobs]
        ends = [job[1] for job in jobs]
        profits = [job[2] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)  # dp[i]: max profit from i-th job to end
        for i in range(n - 1, -1, -1):
            nxt = bisect.bisect_left(starts, ends[i])
            dp[i] = max(profits[i] + dp[nxt], dp[i + 1])
        return dp[0]
```

## Python3

```python
from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        ends = [job[1] for job in jobs]
        dp = [0] * (n + 1)  # dp[i]: max profit using first i jobs (sorted by end)

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            # Find the last job that ends <= start time of current job
            idx = bisect_right(ends, s, 0, i - 1)
            dp[i] = max(dp[i - 1], p + dp[idx])

        return dp[n]
```

## C

```c
#include <stdlib.h>

struct Job {
    int start;
    int end;
    int profit;
};

static int cmpJob(const void *a, const void *b) {
    const struct Job *ja = (const struct Job *)a;
    const struct Job *jb = (const struct Job *)b;
    if (ja->start < jb->start) return -1;
    if (ja->start > jb->start) return 1;
    return 0;
}

int jobScheduling(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int* profit, int profitSize) {
    int n = startTimeSize;
    struct Job *jobs = (struct Job *)malloc(n * sizeof(struct Job));
    for (int i = 0; i < n; ++i) {
        jobs[i].start = startTime[i];
        jobs[i].end   = endTime[i];
        jobs[i].profit= profit[i];
    }
    qsort(jobs, n, sizeof(struct Job), cmpJob);

    long long *dp = (long long *)malloc((n + 1) * sizeof(long long));
    dp[n] = 0;

    for (int i = n - 1; i >= 0; --i) {
        int lo = i + 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (jobs[mid].start >= jobs[i].end)
                hi = mid;
            else
                lo = mid + 1;
        }
        long long include = (long long)jobs[i].profit + dp[lo];
        long long exclude = dp[i + 1];
        dp[i] = include > exclude ? include : exclude;
    }

    int result = (int)dp[0];
    free(jobs);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int JobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.Length;
        var jobs = new (int start, int end, int profit)[n];
        for (int i = 0; i < n; i++) {
            jobs[i] = (startTime[i], endTime[i], profit[i]);
        }
        Array.Sort(jobs, (a, b) => a.start.CompareTo(b.start));

        var starts = new int[n];
        var ends = new int[n];
        var profits = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = jobs[i].start;
            ends[i] = jobs[i].end;
            profits[i] = jobs[i].profit;
        }

        var dp = new int[n + 1]; // dp[n] = 0 by default
        for (int i = n - 1; i >= 0; i--) {
            int nextIdx = LowerBound(starts, i + 1, n, ends[i]);
            int include = profits[i] + dp[nextIdx];
            int exclude = dp[i + 1];
            dp[i] = include > exclude ? include : exclude;
        }
        return dp[0];
    }

    private int LowerBound(int[] arr, int left, int right, int target) {
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (arr[mid] < target)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function(startTime, endTime, profit) {
    const n = startTime.length;
    const jobs = new Array(n);
    for (let i = 0; i < n; ++i) {
        jobs[i] = { s: startTime[i], e: endTime[i], p: profit[i] };
    }
    // sort by start time
    jobs.sort((a, b) => a.s - b.s);
    const starts = jobs.map(job => job.s);

    const dp = new Array(n + 1).fill(0); // dp[n] = 0

    function lowerBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }

    for (let i = n - 1; i >= 0; --i) {
        const nextIdx = lowerBound(starts, jobs[i].e);
        dp[i] = Math.max(dp[i + 1], jobs[i].p + dp[nextIdx]);
    }
    return dp[0];
};
```

## Typescript

```typescript
function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    const n = startTime.length;
    const jobs = new Array(n);
    for (let i = 0; i < n; i++) {
        jobs[i] = { start: startTime[i], end: endTime[i], profit: profit[i] };
    }
    // sort by start time
    jobs.sort((a, b) => a.start - b.start);
    const starts = jobs.map(j => j.start);

    const dp = new Array(n + 1).fill(0); // dp[n] = 0

    function lowerBound(arr: number[], target: number): number {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    for (let i = n - 1; i >= 0; i--) {
        const nextIdx = lowerBound(starts, jobs[i].end);
        dp[i] = Math.max(jobs[i].profit + dp[nextIdx], dp[i + 1]);
    }
    return dp[0];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer[] $profit
     * @return Integer
     */
    function jobScheduling($startTime, $endTime, $profit) {
        $n = count($startTime);
        if ($n == 0) return 0;
        $jobs = [];
        for ($i = 0; $i < $n; $i++) {
            $jobs[] = [$startTime[$i], $endTime[$i], $profit[$i]];
        }
        usort($jobs, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        $starts = [];
        for ($i = 0; $i < $n; $i++) {
            $starts[] = $jobs[$i][0];
        }
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $nextIdx = $this->lowerBound($starts, $jobs[$i][1]);
            $include = $jobs[$i][2] + ($nextIdx < $n ? $dp[$nextIdx] : 0);
            $exclude = ($i + 1 < $n) ? $dp[$i + 1] : 0;
            $dp[$i] = max($include, $exclude);
        }
        return $dp[0];
    }

    private function lowerBound($arr, $target) {
        $l = 0;
        $r = count($arr);
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] < $target) {
                $l = $mid + 1;
            } else {
                $r = $mid;
            }
        }
        return $l;
    }
}
```

## Swift

```swift
class Solution {
    func jobScheduling(_ startTime: [Int], _ endTime: [Int], _ profit: [Int]) -> Int {
        let n = startTime.count
        var jobs = [(start: Int, end: Int, profit: Int)]()
        jobs.reserveCapacity(n)
        for i in 0..<n {
            jobs.append((start: startTime[i], end: endTime[i], profit: profit[i]))
        }
        jobs.sort { $0.start < $1.start }
        var starts = [Int]()
        starts.reserveCapacity(n)
        for job in jobs {
            starts.append(job.start)
        }
        var dp = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let nextIdx = lowerBound(starts, jobs[i].end)
            let includeProfit = jobs[i].profit + dp[nextIdx]
            let excludeProfit = dp[i + 1]
            dp[i] = max(includeProfit, excludeProfit)
        }
        return dp[0]
    }

    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var left = 0
        var right = arr.count
        while left < right {
            let mid = (left + right) >> 1
            if arr[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun jobScheduling(startTime: IntArray, endTime: IntArray, profit: IntArray): Int {
        val n = startTime.size
        data class Job(val s: Int, val e: Int, val p: Int)
        val jobs = Array(n) { i -> Job(startTime[i], endTime[i], profit[i]) }
        java.util.Arrays.sort(jobs) { a, b -> a.s.compareTo(b.s) }

        val starts = IntArray(n) { jobs[it].s }
        val dp = LongArray(n + 1)

        for (i in n - 1 downTo 0) {
            val next = lowerBound(starts, jobs[i].e)
            val include = jobs[i].p.toLong() + dp[next]
            val exclude = dp[i + 1]
            dp[i] = if (include > exclude) include else exclude
        }
        return dp[0].toInt()
    }

    private fun lowerBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (arr[m] < target) {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
}
```

## Dart

```dart
class Solution {
  int jobScheduling(List<int> startTime, List<int> endTime, List<int> profit) {
    int n = startTime.length;
    List<_Job> jobs = List.generate(
        n,
        (i) => _Job(startTime[i], endTime[i], profit[i]),
        growable: false);
    jobs.sort((a, b) => a.start.compareTo(b.start));

    List<int> starts = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      starts[i] = jobs[i].start;
    }

    List<int> dp = List.filled(n + 1, 0);

    for (int i = n - 1; i >= 0; i--) {
      int nextIdx = _lowerBound(starts, jobs[i].end);
      int includeProfit = jobs[i].profit + dp[nextIdx];
      int excludeProfit = dp[i + 1];
      dp[i] = includeProfit > excludeProfit ? includeProfit : excludeProfit;
    }

    return dp[0];
  }

  int _lowerBound(List<int> arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}

class _Job {
  final int start;
  final int end;
  final int profit;
  _Job(this.start, this.end, this.profit);
}
```

## Golang

```go
package main

import "sort"

type Job struct {
	start  int
	end    int
	profit int
}

func jobScheduling(startTime []int, endTime []int, profit []int) int {
	n := len(startTime)
	jobs := make([]Job, n)
	for i := 0; i < n; i++ {
		jobs[i] = Job{startTime[i], endTime[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i].start < jobs[j].start })

	starts := make([]int, n)
	for i := 0; i < n; i++ {
		starts[i] = jobs[i].start
	}

	dp := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		nextIdx := sort.Search(n, func(k int) bool { return starts[k] >= jobs[i].end })
		take := jobs[i].profit + dp[nextIdx]
		if take > dp[i+1] {
			dp[i] = take
		} else {
			dp[i] = dp[i+1]
		}
	}
	return dp[0]
}
```

## Ruby

```ruby
def job_scheduling(start_time, end_time, profit)
  jobs = start_time.zip(end_time, profit)
  jobs.sort_by! { |s, _e, _p| s }
  n = jobs.length
  starts = jobs.map { |s, _, _| s }
  dp = Array.new(n + 1, 0)

  (n - 1).downto(0) do |i|
    s, e, p = jobs[i]
    lo = i + 1
    hi = n
    while lo < hi
      mid = (lo + hi) / 2
      if starts[mid] >= e
        hi = mid
      else
        lo = mid + 1
      end
    end
    next_idx = lo
    dp[i] = [dp[i + 1], p + dp[next_idx]].max
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def jobScheduling(startTime: Array[Int], endTime: Array[Int], profit: Array[Int]): Int = {
        val n = startTime.length
        case class Job(s: Int, e: Int, p: Int)
        val jobs = new Array[Job](n)
        var i = 0
        while (i < n) {
            jobs(i) = Job(startTime(i), endTime(i), profit(i))
            i += 1
        }
        java.util.Arrays.sort(jobs, new java.util.Comparator[Job] {
            override def compare(a: Job, b: Job): Int = Integer.compare(a.e, b.e)
        })
        val ends = new Array[Int](n)
        i = 0
        while (i < n) {
            ends(i) = jobs(i).e
            i += 1
        }
        val dp = new Array[Long](n)
        var idx = 0
        while (idx < n) {
            // profit if we take this job
            val start = jobs(idx).s
            val pos = java.util.Arrays.binarySearch(ends, 0, idx, start)
            val prevIdx = if (pos >= 0) pos else -pos - 2
            val incl = jobs(idx).p.toLong + (if (prevIdx >= 0) dp(prevIdx) else 0L)
            val excl = if (idx > 0) dp(idx - 1) else 0L
            dp(idx) = Math.max(incl, excl)
            idx += 1
        }
        dp(n - 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let n = start_time.len();
        #[derive(Clone)]
        struct Job {
            start: i32,
            end: i32,
            profit: i32,
        }
        let mut jobs: Vec<Job> = (0..n)
            .map(|i| Job {
                start: start_time[i],
                end: end_time[i],
                profit: profit[i],
            })
            .collect();
        jobs.sort_by_key(|j| j.start);
        let starts: Vec<i32> = jobs.iter().map(|j| j.start).collect();
        let mut dp: Vec<i64> = vec![0; n + 1];
        for i in (0..n).rev() {
            let idx = match starts.binary_search(&jobs[i].end) {
                Ok(pos) => pos,
                Err(pos) => pos,
            };
            let include = jobs[i].profit as i64 + dp[idx];
            let exclude = dp[i + 1];
            dp[i] = if include > exclude { include } else { exclude };
        }
        dp[0] as i32
    }
}
```

## Racket

```racket
(define/contract (job-scheduling startTime endTime profit)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length startTime))
         (jobs (sort (map list startTime endTime profit) < #:key (lambda (j) (first j))))
         (start-vec (for/vector ([j jobs]) (first j)))
         (end-vec   (for/vector ([j jobs]) (second j)))
         (profit-vec (for/vector ([j jobs]) (third j)))
         (dp (make-vector (+ n 1) 0)))
    (define (lower-bound vec target)
      (let loop ((low 0) (high (vector-length vec)))
        (if (= low high)
            low
            (let* ((mid (quotient (+ low high) 2))
                   (val (vector-ref vec mid)))
              (if (< val target)
                  (loop (+ mid 1) high)
                  (loop low mid))))))
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ((next-idx (lower-bound start-vec (vector-ref end-vec i)))
             (take-profit (+ (vector-ref profit-vec i) (vector-ref dp next-idx)))
             (skip-profit (vector-ref dp (+ i 1))))
        (vector-set! dp i (if (> take-profit skip-profit) take-profit skip-profit))))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-export([job_scheduling/3]).

-spec job_scheduling(StartTime :: [integer()], EndTime :: [integer()], Profit :: [integer()]) -> integer().
job_scheduling(StartTime, EndTime, Profit) ->
    Jobs = lists:zipwith(fun(S,E,P) -> {S,E,P} end, StartTime, EndTime, Profit),
    SortedJobs = lists:keysort(1, Jobs),
    Starts = [S || {S,_E,_P} <- SortedJobs],
    Ends   = [E || {_S,E,_P} <- SortedJobs],
    Profits= [P || {_S,_E,P} <- SortedJobs],
    N = length(Starts),
    StartsArr = array:from_list(Starts),
    EndArr = array:from_list(Ends),
    ProfArr = array:from_list(Profits),
    DPInit = array:new(N+1, {default,0}),
    FinalDP = dp_loop(N, N, StartsArr, EndArr, ProfArr, DPInit),
    array:get(1, FinalDP).

dp_loop(I, _N, _StartsArr, _EndArr, _ProfArr, DPArr) when I < 1 ->
    DPArr;
dp_loop(I, N, StartsArr, EndArr, ProfArr, DPArr) ->
    ProfitI = array:get(I, ProfArr),
    EndI = array:get(I, EndArr),
    NextIdx = lower_bound(StartsArr, N, EndI),
    Include = ProfitI + array:get(NextIdx, DPArr),
    Exclude = array:get(I+1, DPArr),
    Best = if Include > Exclude -> Include; true -> Exclude end,
    NewDP = array:set(I, Best, DPArr),
    dp_loop(I-1, N, StartsArr, EndArr, ProfArr, NewDP).

lower_bound(StartsArr, N, Target) ->
    lower_bound(StartsArr, 1, N, Target).

lower_bound(_Arr, Low, High, _Target) when Low > High ->
    Low;
lower_bound(Arr, Low, High, Target) ->
    Mid = (Low + High) div 2,
    Val = array:get(Mid, Arr),
    if
        Val < Target ->
            lower_bound(Arr, Mid+1, High, Target);
        true ->
            lower_bound(Arr, Low, Mid-1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec job_scheduling(start_time :: [integer], end_time :: [integer], profit :: [integer]) :: integer
  def job_scheduling(start_time, end_time, profit) do
    jobs =
      Enum.zip([start_time, end_time, profit])
      |> Enum.sort_by(fn {s, _, _} -> s end)

    n = length(jobs)
    starts = jobs |> Enum.map(&elem(&1, 0)) |> List.to_tuple()
    ends = jobs |> Enum.map(&elem(&1, 1)) |> List.to_tuple()
    profits = jobs |> Enum.map(&elem(&1, 2)) |> List.to_tuple()

    dp_array = :array.new(n + 1, default: 0)

    dp_filled =
      Enum.reduce(Enum.reverse(0..(n - 1)), dp_array, fn i, arr ->
        end_i = elem(ends, i)
        next_idx = binary_search(starts, end_i, i + 1, n)
        profit_i = elem(profits, i)

        take = profit_i + :array.get(next_idx, arr)
        skip = :array.get(i + 1, arr)
        best = if take > skip, do: take, else: skip

        :array.set(i, best, arr)
      end)

    :array.get(0, dp_filled)
  end

  defp binary_search(starts, target, low, high) when low < high do
    mid = div(low + high, 2)

    if elem(starts, mid) < target do
      binary_search(starts, target, mid + 1, high)
    else
      binary_search(starts, target, low, mid)
    end
  end

  defp binary_search(_starts, _target, low, _high), do: low
end
```
