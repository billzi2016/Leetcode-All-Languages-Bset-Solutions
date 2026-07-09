# 1723. Find Minimum Time to Finish All Jobs

## Cpp

```cpp
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        sort(jobs.rbegin(), jobs.rend());
        int n = jobs.size();
        long long sum = 0, mx = 0;
        for (int t : jobs) { sum += t; mx = max<long long>(mx, t); }
        if (k >= n) return mx;
        long long lo = mx, hi = sum;
        vector<int> workers(k);
        function<bool(int,long long)> dfs = [&](int idx, long long limit)->bool{
            if (idx == n) return true;
            int cur = jobs[idx];
            unordered_set<int> seen;
            for (int i = 0; i < k; ++i) {
                if (workers[i] + cur > limit) continue;
                if (seen.count(workers[i])) continue;
                seen.insert(workers[i]);
                workers[i] += cur;
                if (dfs(idx + 1, limit)) return true;
                workers[i] -= cur;
                if (workers[i] == 0) break; // symmetry pruning
            }
            return false;
        };
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            fill(workers.begin(), workers.end(), 0);
            if (dfs(0, mid)) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        Arrays.sort(jobs);
        int n = jobs.length;
        int lo = 0, hi = 0;
        for (int job : jobs) {
            lo = Math.max(lo, job);
            hi += job;
        }
        int[] workloads = new int[k];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canAssign(jobs, workloads, n - 1, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean canAssign(int[] jobs, int[] workloads, int idx, int limit) {
        if (idx < 0) return true;
        int cur = jobs[idx];
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < workloads.length; i++) {
            if (workloads[i] + cur <= limit && !seen.contains(workloads[i])) {
                seen.add(workloads[i]);
                workloads[i] += cur;
                if (canAssign(jobs, workloads, idx - 1, limit)) return true;
                workloads[i] -= cur;
            }
            if (workloads[i] == 0) break;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        n = len(jobs)
        if k >= n:
            return max(jobs)

        jobs.sort(reverse=True)
        lo, hi = max(jobs), sum(jobs)

        def can(limit):
            workloads = [0] * k

            def dfs(idx):
                if idx == n:
                    return True
                cur = jobs[idx]
                seen = set()
                for i in range(k):
                    if workloads[i] + cur <= limit and workloads[i] not in seen:
                        seen.add(workloads[i])
                        workloads[i] += cur
                        if dfs(idx + 1):
                            return True
                        workloads[i] -= cur
                    if workloads[i] == 0:  # symmetry pruning
                        break
                return False

            return dfs(0)

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
class Solution:
    def minimumTimeRequired(self, jobs, k):
        from math import inf
        n = len(jobs)
        total = sum(jobs)
        lo, hi = max(jobs), total

        # precompute sums for all masks (will be recomputed each check? we can compute once)
        mask_sum = [0] * (1 << n)
        for mask in range(1, 1 << n):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            mask_sum[mask] = mask_sum[mask ^ lsb] + jobs[idx]

        def can(limit):
            full = (1 << n) - 1
            dp = [k + 1] * (full + 1)
            dp[0] = 0
            for mask in range(1, full + 1):
                sub = mask
                # iterate over submasks
                while sub:
                    if mask_sum[sub] <= limit:
                        prev = dp[mask ^ sub] + 1
                        if prev < dp[mask]:
                            dp[mask] = prev
                            if dp[mask] == 1:  # cannot get better than 1
                                break
                    sub = (sub - 1) & mask
            return dp[full] <= k

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int *g_jobs;
static int g_n;
static int g_k;
static int g_limit;
static int g_loads[12];

int cmp_desc(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return bi - ai;
}

bool dfs(int idx) {
    if (idx == g_n) return true;
    int cur = g_jobs[idx];
    for (int i = 0; i < g_k; ++i) {
        if (g_loads[i] + cur > g_limit) continue;
        if (i > 0 && g_loads[i] == g_loads[i - 1]) continue;
        g_loads[i] += cur;
        if (dfs(idx + 1)) return true;
        g_loads[i] -= cur;
        if (g_loads[i] == 0) break;
    }
    return false;
}

bool canFinish(int limit) {
    g_limit = limit;
    for (int i = 0; i < g_k; ++i) g_loads[i] = 0;
    return dfs(0);
}

int minimumTimeRequired(int* jobs, int jobsSize, int k) {
    g_jobs = jobs;
    g_n = jobsSize;
    g_k = k;
    qsort(g_jobs, g_n, sizeof(int), cmp_desc);
    long sum = 0;
    int maxv = 0;
    for (int i = 0; i < g_n; ++i) {
        sum += g_jobs[i];
        if (g_jobs[i] > maxv) maxv = g_jobs[i];
    }
    int low = maxv, high = (int)sum;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (canFinish(mid))
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution {
    private int[] _jobs;
    private int _n;
    private int _k;
    private int _limit;
    private int[] _workloads;

    public int MinimumTimeRequired(int[] jobs, int k) {
        // Sort jobs in descending order for better pruning
        Array.Sort(jobs);
        Array.Reverse(jobs);
        _jobs = jobs;
        _n = jobs.Length;
        _k = k;
        _workloads = new int[k];

        int low = 0, high = 0;
        foreach (int job in jobs) {
            low = Math.Max(low, job); // at least the largest single job
            high += job;               // at most sum of all jobs
        }

        while (low < high) {
            int mid = low + (high - low) / 2;
            _limit = mid;
            Array.Clear(_workloads, 0, k);
            if (CanAssign(0)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    private bool CanAssign(int idx) {
        if (idx == _n) return true; // all jobs assigned
        int curJob = _jobs[idx];
        for (int i = 0; i < _k; i++) {
            if (_workloads[i] + curJob <= _limit) {
                _workloads[i] += curJob;
                if (CanAssign(idx + 1)) return true;
                _workloads[i] -= curJob;
            }
            // Prune: if this worker has no jobs yet, or adding the job fills him to the limit,
            // there's no need to try other workers with the same state.
            if (_workloads[i] == 0 || _workloads[i] + curJob == _limit) break;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} jobs
 * @param {number} k
 * @return {number}
 */
var minimumTimeRequired = function(jobs, k) {
    // Sort jobs descending to assign larger ones first (better pruning)
    jobs.sort((a, b) => b - a);
    const n = jobs.length;
    let ans = jobs.reduce((s, v) => s + v, 0); // upper bound
    const loads = new Array(k).fill(0);

    function dfs(idx) {
        if (idx === n) {
            const curMax = Math.max(...loads);
            if (curMax < ans) ans = curMax;
            return;
        }
        const job = jobs[idx];
        for (let i = 0; i < k; ++i) {
            // Prune if this assignment already exceeds current best answer
            if (loads[i] + job >= ans) continue;

            // Skip symmetric states: if another worker has the same load, 
            // assigning to this one would be equivalent.
            let duplicate = false;
            for (let j = 0; j < i; ++j) {
                if (loads[j] === loads[i]) {
                    duplicate = true;
                    break;
                }
            }
            if (duplicate) continue;

            loads[i] += job;
            dfs(idx + 1);
            loads[i] -= job;

            // If we placed the current job into an empty worker,
            // no need to try other empty workers (symmetry).
            if (loads[i] === 0) break;
        }
    }

    dfs(0);
    return ans;
};
```

## Typescript

```typescript
function minimumTimeRequired(jobs: number[], k: number): number {
    const n = jobs.length;
    const fullMask = 1 << n;

    // precompute sum of each subset
    const subsetSum = new Array(fullMask).fill(0);
    for (let mask = 1; mask < fullMask; ++mask) {
        const lsb = mask & -mask;                     // lowest set bit
        const idx = Math.round(Math.log2(lsb));       // index of that job
        subsetSum[mask] = subsetSum[mask ^ lsb] + jobs[idx];
    }

    const maxJob = Math.max(...jobs);
    const total = jobs.reduce((a, b) => a + b, 0);

    const canFinish = (limit: number): boolean => {
        const dp = new Array(fullMask).fill(k + 1);
        dp[0] = 0;
        for (let mask = 1; mask < fullMask; ++mask) {
            // enumerate submasks
            let sub = mask;
            while (sub) {
                if (subsetSum[sub] <= limit) {
                    const prev = dp[mask ^ sub];
                    if (prev + 1 < dp[mask]) dp[mask] = prev + 1;
                }
                sub = (sub - 1) & mask;
            }
        }
        return dp[fullMask - 1] <= k;
    };

    let lo = maxJob, hi = total;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (canFinish(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $jobs
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeRequired($jobs, $k) {
        $n = count($jobs);
        $fullMask = (1 << $n) - 1;

        // precompute sum of each subset
        $sums = array_fill(0, 1 << $n, 0);
        for ($mask = 1; $mask < (1 << $n); $mask++) {
            for ($i = 0; $i < $n; $i++) {
                if ($mask & (1 << $i)) {
                    $sums[$mask] = $sums[$mask ^ (1 << $i)] + $jobs[$i];
                    break;
                }
            }
        }

        $low = max($jobs);
        $high = array_sum($jobs);

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canFinish($mid, $k, $fullMask, $sums)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    /**
     * @param int $limit
     * @param int $k
     * @param int $fullMask
     * @param array $sums
     * @return bool
     */
    private function canFinish($limit, $k, $fullMask, $sums) {
        $totalMasks = count($sums);
        // valid subsets whose sum does not exceed limit
        $valid = array_fill(0, $totalMasks, false);
        for ($mask = 0; $mask < $totalMasks; $mask++) {
            if ($sums[$mask] <= $limit) {
                $valid[$mask] = true;
            }
        }

        $visited = array_fill(0, $totalMasks, false);
        $current = [0];
        $visited[0] = true;

        for ($i = 0; $i < $k; $i++) {
            $next = [];
            foreach ($current as $curMask) {
                $rem = $fullMask ^ $curMask; // jobs not yet assigned
                $sub = $rem;
                while ($sub) {
                    if ($valid[$sub]) {
                        $newMask = $curMask | $sub;
                        if (!$visited[$newMask]) {
                            if ($newMask == $fullMask) {
                                return true;
                            }
                            $visited[$newMask] = true;
                            $next[] = $newMask;
                        }
                    }
                    $sub = ($sub - 1) & $rem; // next submask
                }
            }
            if (empty($next)) {
                break;
            }
            $current = $next;
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTimeRequired(_ jobs: [Int], _ k: Int) -> Int {
        let sortedJobs = jobs.sorted(by: >)
        var low = sortedJobs.max()!
        var high = sortedJobs.reduce(0, +)
        var workers = Array(repeating: 0, count: k)

        func canAssign(_ limit: Int) -> Bool {
            for i in 0..<k { workers[i] = 0 }

            func dfs(_ idx: Int) -> Bool {
                if idx == sortedJobs.count { return true }
                let job = sortedJobs[idx]
                var seen = Set<Int>()
                for i in 0..<k {
                    if workers[i] + job <= limit && !seen.contains(workers[i]) {
                        seen.insert(workers[i])
                        workers[i] += job
                        if dfs(idx + 1) { return true }
                        workers[i] -= job
                    }
                    if workers[i] == 0 { break } // avoid symmetric empty assignments
                }
                return false
            }

            return dfs(0)
        }

        while low < high {
            let mid = (low + high) / 2
            if canAssign(mid) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTimeRequired(jobs: IntArray, k: Int): Int {
        val sortedJobs = jobs.sortedDescending().toIntArray()
        var left = sortedJobs.maxOrNull()!!
        var right = sortedJobs.sum()
        while (left < right) {
            val mid = (left + right) ushr 1
            if (canFinish(sortedJobs, k, mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }

    private fun canFinish(jobs: IntArray, k: Int, limit: Int): Boolean {
        val workloads = IntArray(k)
        fun dfs(idx: Int): Boolean {
            if (idx == jobs.size) return true
            val cur = jobs[idx]
            val seen = HashSet<Int>()
            for (i in 0 until k) {
                if (workloads[i] + cur <= limit && seen.add(workloads[i])) {
                    workloads[i] += cur
                    if (dfs(idx + 1)) return true
                    workloads[i] -= cur
                }
                // If this worker has no jobs assigned yet, avoid trying other empty workers (symmetry)
                if (workloads[i] == 0) break
            }
            return false
        }
        return dfs(0)
    }
}
```

## Dart

```dart
class Solution {
  int minimumTimeRequired(List<int> jobs, int k) {
    // Sort jobs in descending order to improve pruning.
    jobs.sort((a, b) => b.compareTo(a));

    int low = jobs.reduce((a, b) => a > b ? a : b); // max job time
    int high = jobs.fold(0, (sum, v) => sum + v);   // total time

    List<int> workloads = List.filled(k, 0);

    bool canAssign(int limit) {
      for (int i = 0; i < k; ++i) workloads[i] = 0;

      bool dfs(int idx) {
        if (idx == jobs.length) return true;
        int cur = jobs[idx];
        Set<int> seen = {};

        for (int i = 0; i < k; ++i) {
          if (workloads[i] + cur <= limit && !seen.contains(workloads[i])) {
            seen.add(workloads[i]);
            workloads[i] += cur;
            if (dfs(idx + 1)) return true;
            workloads[i] -= cur;
          }
          // If this worker has no jobs, further empty workers are symmetric.
          if (workloads[i] == 0) break;
        }
        return false;
      }

      return dfs(0);
    }

    while (low < high) {
      int mid = (low + high) >> 1;
      if (canAssign(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func minimumTimeRequired(jobs []int, k int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(jobs)))
    n := len(jobs)
    total := 0
    for _, v := range jobs {
        total += v
    }
    // If workers are more than jobs, answer is max job time.
    if k >= n {
        return jobs[0]
    }

    workloads := make([]int, k)
    ans := total

    var dfs func(idx int)
    dfs = func(idx int) {
        if idx == n {
            curMax := 0
            for _, w := range workloads {
                if w > curMax {
                    curMax = w
                }
            }
            if curMax < ans {
                ans = curMax
            }
            return
        }

        seen := make(map[int]bool)
        for i := 0; i < k; i++ {
            if seen[workloads[i]] {
                continue
            }
            seen[workloads[i]] = true

            workloads[i] += jobs[idx]

            // prune if current max already not better than best answer
            curMax := 0
            for _, w := range workloads {
                if w > curMax {
                    curMax = w
                }
            }
            if curMax < ans {
                dfs(idx + 1)
            }

            workloads[i] -= jobs[idx]

            // If this worker was idle before assigning current job,
            // no need to try other idle workers (symmetry pruning).
            if workloads[i] == 0 {
                break
            }
        }
    }

    dfs(0)
    return ans
}
```

## Ruby

```ruby
def minimum_time_required(jobs, k)
  n = jobs.size
  return jobs.max if k >= n

  jobs.sort!.reverse!
  @jobs = jobs
  @k = k
  @ans = jobs.sum
  @workers = Array.new(k, 0)

  dfs(0)
  @ans
end

def dfs(idx)
  if idx == @jobs.size
    max_load = @workers.max
    @ans = max_load if max_load < @ans
    return
  end

  cur = @jobs[idx]
  seen = {}
  @k.times do |i|
    next if @workers[i] + cur >= @ans
    next if seen[@workers[i]]
    seen[@workers[i]] = true

    @workers[i] += cur
    dfs(idx + 1)
    @workers[i] -= cur
  end
end
```

## Scala

```scala
object Solution {
  def minimumTimeRequired(jobs: Array[Int], k: Int): Int = {
    val sortedJobs = jobs.sorted(Ordering.Int.reverse)
    var lo = sortedJobs.max
    var hi = sortedJobs.sum

    def canAssign(limit: Int): Boolean = {
      val workloads = new Array[Int](k)

      def dfs(idx: Int): Boolean = {
        if (idx == sortedJobs.length) return true
        val cur = sortedJobs(idx)
        var seen = Set[Int]()
        for (i <- 0 until k) {
          if (workloads(i) + cur <= limit && !seen.contains(workloads(i))) {
            seen += workloads(i)
            workloads(i) += cur
            if (dfs(idx + 1)) return true
            workloads(i) -= cur
          }
          if (workloads(i) == 0) {
            // assigning to another empty worker would be symmetric
            return false
          }
        }
        false
      }

      dfs(0)
    }

    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (canAssign(mid)) hi = mid else lo = mid + 1
    }
    lo
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time_required(jobs: Vec<i32>, k: i32) -> i32 {
        let n = jobs.len();
        // pre‑compute sums of all subsets
        let full = 1usize << n;
        let mut sum = vec![0i32; full];
        for mask in 1..full {
            let idx = mask.trailing_zeros() as usize;          // least significant set bit
            let prev = mask ^ (1usize << idx);
            sum[mask] = sum[prev] + jobs[idx];
        }

        let mut lo = *jobs.iter().max().unwrap();               // at least the biggest job
        let mut hi = sum[full - 1];                             // at most total time

        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if Self::can_finish(&sum, n, k as usize, mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }

    fn can_finish(sum: &Vec<i32>, n: usize, k: usize, limit: i32) -> bool {
        let full = 1usize << n;
        let mut dp = vec![k + 1; full];
        dp[0] = 0;

        for mask in 0..full {
            if dp[mask] >= k { continue; }
            let remaining = (!mask) & (full - 1);
            let mut sub = remaining;
            while sub > 0 {
                if sum[sub] <= limit {
                    let new_mask = mask | sub;
                    if dp[new_mask] > dp[mask] + 1 {
                        dp[new_mask] = dp[mask] + 1;
                    }
                }
                sub = (sub - 1) & remaining; // next subset
            }
        }
        dp[full - 1] <= k
    }
}
```

## Racket

```racket
(define/contract (minimum-time-required jobs k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted-jobs (sort jobs >))
         (low (apply max sorted-jobs))
         (high (apply + sorted-jobs)))
    (define (can-assign? limit)
      (let ((n (length sorted-jobs))
            (loads (make-vector k 0)))
        (define (dfs i)
          (if (= i n) #t
              (let ((job (list-ref sorted-jobs i)))
                (let loop ((w 0) (prev -1))
                  (cond
                    [(= w k) #f]
                    [else
                     (define cur (vector-ref loads w))
                     (if (or (> (+ cur job) limit)
                             (= cur prev))
                         (loop (+ w 1) prev)
                         (begin
                           (vector-set! loads w (+ cur job))
                           (if (dfs (+ i 1))
                               #t
                               (begin
                                 (vector-set! loads w cur)
                                 (loop (+ w 1) cur)))))]))))
        (dfs 0)))
    (define (binary lo hi)
      (if (= lo hi) lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (can-assign? mid)
                (binary lo mid)
                (binary (+ mid 1) hi)))))
    (binary low high)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time_required/2]).

-spec minimum_time_required(Jobs :: [integer()], K :: integer()) -> integer().
minimum_time_required(Jobs, K) ->
    SortedJobs = lists:reverse(lists:sort(Jobs)),
    MaxJob = hd(SortedJobs),
    SumJobs = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Jobs),
    binary_search(MaxJob, SumJobs, SortedJobs, K).

binary_search(Low, High, Jobs, K) when Low >= High ->
    Low;
binary_search(Low, High, Jobs, K) ->
    Mid = (Low + High) div 2,
    case feasible(Jobs, K, Mid) of
        true -> binary_search(Low, Mid, Jobs, K);
        false -> binary_search(Mid + 1, High, Jobs, K)
    end.

feasible(Jobs, K, Limit) ->
    Loads = lists:duplicate(K, 0),
    dfs(Jobs, Loads, Limit).

dfs([], _Loads, _Limit) ->
    true;
dfs([Job | Rest], Loads, Limit) ->
    dfs_try(Loads, Job, Rest, Limit, [], 1).

dfs_try(_Loads, _Job, _Rest, _Limit, _Tried, _Pos) when false -> % placeholder for clause ordering
    false.

dfs_try([], _Job, _Rest, _Limit, _Tried, _Pos) ->
    false;
dfs_try(Loads = [Load | Tail], Job, Rest, Limit, Tried, Pos) ->
    case lists:member(Load, Tried) of
        true ->
            dfs_try(Tail, Job, Rest, Limit, Tried, Pos + 1);
        false ->
            NewTried = [Load | Tried],
            case Load + Job =< Limit of
                true ->
                    NewLoads = replace_nth(Loads, Pos, Load + Job),
                    case dfs(Rest, NewLoads, Limit) of
                        true -> true;
                        false ->
                            case Load of
                                0 -> false; % prune symmetric empty workers
                                _ -> dfs_try(Tail, Job, Rest, Limit, NewTried, Pos + 1)
                            end
                    end;
                false ->
                    case Load of
                        0 -> false; % cannot place in any empty worker, prune
                        _ -> dfs_try(Tail, Job, Rest, Limit, NewTried, Pos + 1)
                    end
            end
    end.

replace_nth([_Old | T], 1, New) ->
    [New | T];
replace_nth([H | T], N, New) when N > 1 ->
    [H | replace_nth(T, N - 1, New)].
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time_required(jobs :: [integer], k :: integer) :: integer
  def minimum_time_required(jobs, k) do
    sorted = Enum.sort(jobs, &>=/2)
    low = Enum.max(jobs)
    high = Enum.sum(jobs)

    bin_search(low, high, sorted, k)
  end

  defp bin_search(low, high, jobs, k) when low < high do
    mid = div(low + high, 2)

    if feasible?(jobs, k, mid) do
      bin_search(low, mid, jobs, k)
    else
      bin_search(mid + 1, high, jobs, k)
    end
  end

  defp bin_search(low, _high, _jobs, _k), do: low

  # check if we can assign all jobs with max workload <= limit using at most k workers
  defp feasible?(jobs, k, limit) do
    workers = :array.new(k, default: 0)
    dfs(0, jobs, k, limit, workers)
  end

  defp dfs(idx, jobs, _k, _limit, workers) when idx == length(jobs), do: true

  defp dfs(idx, jobs, k, limit, workers) do
    time = Enum.at(jobs, idx)
    assign(0, time, idx, jobs, k, limit, workers)
  end

  # try to assign current job to a worker starting from index i
  defp assign(i, _time, _idx, _jobs, k, _limit, _workers) when i >= k, do: false

  defp assign(i, time, idx, jobs, k, limit, workers) do
    w = :array.get(i, workers)

    cond do
      w + time <= limit ->
        workers2 = :array.set(i, w + time, workers)

        if dfs(idx + 1, jobs, k, limit, workers2) do
          true
        else
          # prune symmetric states: if this worker was empty before assignment,
          # no need to try other empty workers
          if w == 0 do
            false
          else
            assign(i + 1, time, idx, jobs, k, limit, workers)
          end
        end

      true ->
        # cannot fit into this worker
        if w == 0 do
          false
        else
          assign(i + 1, time, idx, jobs, k, limit, workers)
        end
    end
  end
end
```
