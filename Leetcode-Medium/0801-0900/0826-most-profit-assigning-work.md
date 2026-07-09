# 0826. Most Profit Assigning Work

## Cpp

```cpp
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = difficulty.size();
        vector<pair<int,int>> jobs;
        jobs.reserve(n);
        for (int i = 0; i < n; ++i) {
            jobs.emplace_back(difficulty[i], profit[i]);
        }
        sort(jobs.begin(), jobs.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){ return a.first < b.first; });
        sort(worker.begin(), worker.end());
        
        long long total = 0;
        int idx = 0;
        int best = 0;
        for (int ability : worker) {
            while (idx < n && jobs[idx].first <= ability) {
                best = max(best, jobs[idx].second);
                ++idx;
            }
            total += best;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int n = difficulty.length;
        int[][] jobs = new int[n][2];
        for (int i = 0; i < n; i++) {
            jobs[i][0] = difficulty[i];
            jobs[i][1] = profit[i];
        }
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));

        int[] diffSorted = new int[n];
        int[] maxProf = new int[n];
        for (int i = 0; i < n; i++) {
            diffSorted[i] = jobs[i][0];
            if (i == 0) {
                maxProf[i] = jobs[i][1];
            } else {
                maxProf[i] = Math.max(maxProf[i - 1], jobs[i][1]);
            }
        }

        long total = 0;
        for (int ability : worker) {
            int idx = Arrays.binarySearch(diffSorted, ability);
            if (idx < 0) {
                idx = -idx - 2; // insertion point - 1
            }
            if (idx >= 0) {
                total += maxProf[idx];
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # Pair each job's difficulty with its profit and sort by difficulty.
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        # Sort workers' abilities.
        worker.sort()
        
        total_profit = 0
        max_profit_so_far = 0
        i = 0
        n = len(jobs)
        
        for ability in worker:
            # Advance through jobs that this worker can do,
            # updating the best profit seen so far.
            while i < n and jobs[i][0] <= ability:
                if jobs[i][1] > max_profit_so_far:
                    max_profit_so_far = jobs[i][1]
                i += 1
            total_profit += max_profit_so_far
        
        return total_profit
```

## Python3

```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        worker.sort()
        i = 0
        best = 0
        total = 0
        n = len(jobs)
        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                if jobs[i][1] > best:
                    best = jobs[i][1]
                i += 1
            total += best
        return total
```

## C

```c
#include <stdlib.h>

typedef struct {
    int diff;
    int profit;
} Job;

static int cmpJob(const void *a, const void *b) {
    int d1 = ((const Job *)a)->diff;
    int d2 = ((const Job *)b)->diff;
    return d1 - d2;
}

static int cmpInt(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int maxProfitAssignment(int* difficulty, int difficultySize,
                        int* profit, int profitSize,
                        int* worker, int workerSize) {
    if (difficultySize == 0 || workerSize == 0) return 0;

    Job *jobs = (Job *)malloc(sizeof(Job) * difficultySize);
    for (int i = 0; i < difficultySize; ++i) {
        jobs[i].diff = difficulty[i];
        jobs[i].profit = profit[i];
    }

    qsort(jobs, difficultySize, sizeof(Job), cmpJob);
    qsort(worker, workerSize, sizeof(int), cmpInt);

    long long total = 0;
    int idx = 0;
    int best = 0;

    for (int i = 0; i < workerSize; ++i) {
        while (idx < difficultySize && jobs[idx].diff <= worker[i]) {
            if (jobs[idx].profit > best) best = jobs[idx].profit;
            ++idx;
        }
        total += best;
    }

    free(jobs);
    return (int)total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int n = difficulty.Length;
        var jobs = new Tuple<int, int>[n];
        for (int i = 0; i < n; i++) {
            jobs[i] = Tuple.Create(difficulty[i], profit[i]);
        }
        Array.Sort(jobs, (a, b) => a.Item1.CompareTo(b.Item1));
        Array.Sort(worker);
        
        int idx = 0;
        int bestProfit = 0;
        long total = 0;
        foreach (int ability in worker) {
            while (idx < n && jobs[idx].Item1 <= ability) {
                if (jobs[idx].Item2 > bestProfit) {
                    bestProfit = jobs[idx].Item2;
                }
                idx++;
            }
            total += bestProfit;
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} difficulty
 * @param {number[]} profit
 * @param {number[]} worker
 * @return {number}
 */
var maxProfitAssignment = function(difficulty, profit, worker) {
    const n = difficulty.length;
    const jobs = new Array(n);
    for (let i = 0; i < n; ++i) {
        jobs[i] = [difficulty[i], profit[i]];
    }
    // Sort jobs by difficulty
    jobs.sort((a, b) => a[0] - b[0]);

    // Precompute the maximum profit up to each difficulty
    const maxProf = new Array(n);
    let curMax = 0;
    for (let i = 0; i < n; ++i) {
        if (jobs[i][1] > curMax) curMax = jobs[i][1];
        maxProf[i] = curMax;
    }

    // Sort workers by ability
    worker.sort((a, b) => a - b);

    let total = 0;
    let idx = 0; // pointer in jobs
    for (const ability of worker) {
        while (idx < n && jobs[idx][0] <= ability) {
            ++idx;
        }
        if (idx > 0) {
            total += maxProf[idx - 1];
        }
    }
    return total;
};
```

## Typescript

```typescript
function maxProfitAssignment(difficulty: number[], profit: number[], worker: number[]): number {
    const n = difficulty.length;
    const jobs: [number, number][] = new Array(n);
    for (let i = 0; i < n; i++) {
        jobs[i] = [difficulty[i], profit[i]];
    }
    jobs.sort((a, b) => a[0] - b[0]); // sort by difficulty
    worker.sort((a, b) => a - b); // sort workers

    let total = 0;
    let maxProfit = 0;
    let idx = 0;

    for (const ability of worker) {
        while (idx < n && jobs[idx][0] <= ability) {
            if (jobs[idx][1] > maxProfit) {
                maxProfit = jobs[idx][1];
            }
            idx++;
        }
        total += maxProfit;
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $difficulty
     * @param Integer[] $profit
     * @param Integer[] $worker
     * @return Integer
     */
    function maxProfitAssignment($difficulty, $profit, $worker) {
        $n = count($difficulty);
        $jobs = [];
        for ($i = 0; $i < $n; $i++) {
            $jobs[] = ['d' => $difficulty[$i], 'p' => $profit[$i]];
        }
        usort($jobs, function($a, $b) {
            return $a['d'] <=> $b['d'];
        });
        sort($worker);
        
        $total = 0;
        $maxProfit = 0;
        $idx = 0;
        $jobCount = count($jobs);
        foreach ($worker as $ability) {
            while ($idx < $jobCount && $jobs[$idx]['d'] <= $ability) {
                if ($jobs[$idx]['p'] > $maxProfit) {
                    $maxProfit = $jobs[$idx]['p'];
                }
                $idx++;
            }
            $total += $maxProfit;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfitAssignment(_ difficulty: [Int], _ profit: [Int], _ worker: [Int]) -> Int {
        let n = difficulty.count
        var jobs = [(diff: Int, prof: Int)]()
        jobs.reserveCapacity(n)
        for i in 0..<n {
            jobs.append((difficulty[i], profit[i]))
        }
        jobs.sort { $0.diff < $1.diff }
        
        let sortedWorkers = worker.sorted()
        var total = 0
        var maxProf = 0
        var idx = 0
        
        for ability in sortedWorkers {
            while idx < jobs.count && ability >= jobs[idx].diff {
                if jobs[idx].prof > maxProf {
                    maxProf = jobs[idx].prof
                }
                idx += 1
            }
            total += maxProf
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfitAssignment(difficulty: IntArray, profit: IntArray, worker: IntArray): Int {
        val n = difficulty.size
        val jobs = Array(n) { i -> intArrayOf(difficulty[i], profit[i]) }
        java.util.Arrays.sort(jobs) { a, b -> a[0] - b[0] }

        java.util.Arrays.sort(worker)

        var idx = 0
        var best = 0
        var total = 0L

        for (ability in worker) {
            while (idx < n && jobs[idx][0] <= ability) {
                if (jobs[idx][1] > best) best = jobs[idx][1]
                idx++
            }
            total += best
        }

        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxProfitAssignment(List<int> difficulty, List<int> profit, List<int> worker) {
    int n = difficulty.length;
    // Pair each job's difficulty with its profit
    List<List<int>> jobs = List.generate(n, (i) => [difficulty[i], profit[i]]);
    // Sort jobs by difficulty ascending
    jobs.sort((a, b) => a[0].compareTo(b[0]));
    // Prefix max profit so that profit at each index is the best up to that difficulty
    for (int i = 1; i < n; ++i) {
      if (jobs[i][1] < jobs[i - 1][1]) {
        jobs[i][1] = jobs[i - 1][1];
      }
    }
    // Sort workers by ability
    List<int> sortedWorkers = List.from(worker);
    sortedWorkers.sort();
    int totalProfit = 0;
    int maxProfitSoFar = 0;
    int jobIdx = 0;
    for (int ability in sortedWorkers) {
      while (jobIdx < n && jobs[jobIdx][0] <= ability) {
        maxProfitSoFar = jobs[jobIdx][1];
        jobIdx++;
      }
      totalProfit += maxProfitSoFar;
    }
    return totalProfit;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	type job struct {
		d int
		p int
	}
	n := len(difficulty)
	jobs := make([]job, n)
	for i := 0; i < n; i++ {
		jobs[i] = job{d: difficulty[i], p: profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i].d < jobs[j].d })
	sort.Ints(worker)

	maxProfit := 0
	total := 0
	idx := 0
	for _, ability := range worker {
		for idx < n && jobs[idx].d <= ability {
			if jobs[idx].p > maxProfit {
				maxProfit = jobs[idx].p
			}
			idx++
		}
		total += maxProfit
	}
	return total
}
```

## Ruby

```ruby
def max_profit_assignment(difficulty, profit, worker)
  jobs = difficulty.each_with_index.map { |d, idx| [d, profit[idx]] }
  jobs.sort_by! { |pair| pair[0] }
  worker.sort!
  i = 0
  maxp = 0
  total = 0
  n = jobs.length
  worker.each do |ability|
    while i < n && jobs[i][0] <= ability
      maxp = [maxp, jobs[i][1]].max
      i += 1
    end
    total += maxp
  end
  total
end
```

## Scala

```scala
object Solution {
    def maxProfitAssignment(difficulty: Array[Int], profit: Array[Int], worker: Array[Int]): Int = {
        val jobs = difficulty.zip(profit).sortBy(_._1)
        val sortedWorkers = worker.sorted
        var i = 0
        var best = 0
        var total: Long = 0L
        for (ability <- sortedWorkers) {
            while (i < jobs.length && jobs(i)._1 <= ability) {
                if (jobs(i)._2 > best) best = jobs(i)._2
                i += 1
            }
            total += best
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, worker: Vec<i32>) -> i32 {
        let mut jobs: Vec<(i32, i32)> = difficulty.into_iter().zip(profit.into_iter()).collect();
        jobs.sort_by_key(|&(d, _)| d);
        let mut workers = worker;
        workers.sort();

        let mut max_profit = 0;
        let mut total = 0;
        let mut idx = 0usize;

        for ability in workers {
            while idx < jobs.len() && jobs[idx].0 <= ability {
                if jobs[idx].1 > max_profit {
                    max_profit = jobs[idx].1;
                }
                idx += 1;
            }
            total += max_profit;
        }

        total
    }
}
```

## Racket

```racket
(define/contract (max-profit-assignment difficulty profit worker)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((jobs (map cons difficulty profit))
         (sorted-jobs (sort jobs (lambda (a b) (< (car a) (car b)))))
         (job-vec (list->vector sorted-jobs))
         (n (vector-length job-vec))
         (sorted-workers (sort worker <)))
    (let loop ((ws sorted-workers) (i 0) (maxp 0) (total 0))
      (if (null? ws)
          total
          (let* ((ability (car ws))
                 ;; advance through jobs that this worker can do,
                 ;; updating the running maximum profit.
                 (adv-result
                  (let inner ((idx i) (cur maxp))
                    (if (and (< idx n)
                             (<= (car (vector-ref job-vec idx)) ability))
                        (inner (+ idx 1) (max cur (cdr (vector-ref job-vec idx))))
                        (list idx cur)))))
            (define new-i (first adv-result))
            (define new-maxp (second adv-result))
            (loop (cdr ws) new-i new-maxp (+ total new-maxp)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_profit_assignment/3]).

-spec max_profit_assignment(Difficulty :: [integer()], Profit :: [integer()], Worker :: [integer()]) -> integer().
max_profit_assignment(Difficulty, Profit, Worker) ->
    JobList = [{D, P} || {D, P} <- lists:zip(Difficulty, Profit)],
    SortedJobs = lists:keysort(1, JobList),
    SortedWorkers = lists:sort(Worker),
    process_workers(SortedWorkers, SortedJobs, 0, 0).

process_workers([], _Jobs, _MaxSoFar, Acc) ->
    Acc;
process_workers([W | Ws], Jobs, MaxSoFar, Acc) ->
    {RemainingJobs, NewMax} = advance_jobs(W, Jobs, MaxSoFar),
    process_workers(Ws, RemainingJobs, NewMax, Acc + NewMax).

advance_jobs(_WorkerAbility, [], Max) ->
    {[], Max};
advance_jobs(WorkerAbility, [{D, P} | Rest] = Jobs, Max) when D =< WorkerAbility ->
    UpdatedMax = if P > Max -> P; true -> Max end,
    advance_jobs(WorkerAbility, Rest, UpdatedMax);
advance_jobs(_WorkerAbility, Jobs, Max) ->
    {Jobs, Max}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit_assignment(difficulty :: [integer], profit :: [integer], worker :: [integer]) :: integer
  def max_profit_assignment(difficulty, profit, worker) do
    jobs =
      Enum.zip(difficulty, profit)
      |> Enum.sort_by(fn {d, _p} -> d end)

    sorted_workers = Enum.sort(worker)

    process(sorted_workers, jobs, 0, 0)
  end

  defp process([], _jobs, _cur_max, sum), do: sum

  defp process([w | ws], jobs, cur_max, sum) do
    {remaining_jobs, new_max} = advance_jobs(jobs, cur_max, w)
    process(ws, remaining_jobs, new_max, sum + new_max)
  end

  defp advance_jobs([], cur_max, _ability), do: {[], cur_max}

  defp advance_jobs([{d, p} | rest], cur_max, ability) when d <= ability do
    new_max = if p > cur_max, do: p, else: cur_max
    advance_jobs(rest, new_max, ability)
  end

  defp advance_jobs(jobs, cur_max, _ability), do: {jobs, cur_max}
end
```
