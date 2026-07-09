# 0813. Largest Sum of Averages

## Cpp

```cpp
class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        auto avg = [&](int l, int r) -> double { // [l, r)
            return (prefix[r] - prefix[l]) / (r - l);
        };
        
        vector<double> dp(n, 0.0);
        for (int i = 0; i < n; ++i) {
            dp[i] = avg(i, n); // one group
        }
        
        for (int groups = 2; groups <= k; ++groups) {
            vector<double> ndp(n, 0.0);
            for (int i = 0; i < n; ++i) {
                double best = 0.0;
                // ensure enough elements left for remaining groups-1
                for (int j = i + 1; j <= n - (groups - 1); ++j) {
                    double cand = avg(i, j) + dp[j];
                    if (cand > best) best = cand;
                }
                ndp[i] = best;
            }
            dp.swap(ndp);
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public double largestSumOfAverages(int[] nums, int k) {
        int n = nums.length;
        double[] prefix = new double[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        // dp[i]: best score for subarray starting at i with current number of groups
        double[] dp = new double[n];
        for (int i = 0; i < n; i++) {
            dp[i] = (prefix[n] - prefix[i]) / (n - i);
        }

        // iterate over number of groups from 2 to k
        for (int groups = 2; groups <= k; groups++) {
            double[] ndp = new double[n];
            // we need at least 'groups' elements remaining starting from i
            for (int i = 0; i <= n - groups; i++) {
                double best = 0.0;
                // first group ends at j-1, next start at j
                // ensure enough elements left for the remaining groups
                for (int j = i + 1; j <= n - (groups - 1); j++) {
                    double avg = (prefix[j] - prefix[i]) / (j - i);
                    double candidate = avg + dp[j];
                    if (candidate > best) {
                        best = candidate;
                    }
                }
                ndp[i] = best;
            }
            dp = ndp;
        }

        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        # prefix sums
        pref = [0.0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def avg(i, j):
            return (pref[j] - pref[i]) / (j - i)

        # dp[i]: best score for subarray starting at i using at most current groups
        dp = [0.0] * n
        for i in range(n):
            dp[i] = avg(i, n)

        # iterate adding more groups up to k
        for groups in range(2, k + 1):
            newdp = [0.0] * n
            # we need at least 'groups' elements from i onward
            limit_i = n - groups + 1
            for i in range(limit_i):
                best = 0.0
                # j is the start of the next segment; must leave enough elements for remaining groups-1
                max_j = n - (groups - 1)
                for j in range(i + 1, max_j + 1):
                    cur = avg(i, j) + dp[j]
                    if cur > best:
                        best = cur
                newdp[i] = best
            dp = newdp

        return dp[0]
```

## Python3

```python
class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def avg(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        dp = [0.0] * n
        for i in range(n):
            dp[i] = avg(i, n)

        for parts in range(2, k + 1):
            new_dp = [0.0] * n
            # i can go up to n-parts because we need at least (parts-1) elements after i
            for i in range(n - parts + 1):
                best = 0.0
                # j is the start of the next segment; must leave enough elements for remaining parts-1
                limit = n - (parts - 1)
                for j in range(i + 1, limit + 1):
                    cur = avg(i, j) + dp[j]
                    if cur > best:
                        best = cur
                new_dp[i] = best
            dp = new_dp

        return dp[0]
```

## C

```c
#include <stdlib.h>

double largestSumOfAverages(int* nums, int numsSize, int k) {
    int n = numsSize;
    double *prefix = (double*)malloc((n + 1) * sizeof(double));
    prefix[0] = 0.0;
    for (int i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    double *dpPrev = (double*)malloc(n * sizeof(double));
    double *dpCurr = (double*)malloc(n * sizeof(double));

    // Base case: one partition (average of the suffix)
    for (int i = 0; i < n; ++i) {
        dpPrev[i] = (prefix[n] - prefix[i]) / (n - i);
    }

    int maxParts = k;
    if (maxParts > n) maxParts = n;

    for (int parts = 2; parts <= maxParts; ++parts) {
        for (int i = 0; i < n; ++i) {
            double best = (prefix[n] - prefix[i]) / (n - i); // no further split
            for (int j = i + 1; j < n; ++j) {
                double avg = (prefix[j] - prefix[i]) / (j - i);
                double cand = avg + dpPrev[j];
                if (cand > best) best = cand;
            }
            dpCurr[i] = best;
        }
        double *tmp = dpPrev;
        dpPrev = dpCurr;
        dpCurr = tmp;
    }

    double result = dpPrev[0];
    free(prefix);
    free(dpPrev);
    free(dpCurr);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public double LargestSumOfAverages(int[] nums, int k)
    {
        int n = nums.Length;
        double[] prefix = new double[n + 1];
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + nums[i];

        double Avg(int i, int j) => (prefix[j] - prefix[i]) / (j - i);

        double[,] dp = new double[k + 1, n];
        // base case: one group
        for (int i = 0; i < n; i++)
            dp[1, i] = Avg(i, n);

        for (int groups = 2; groups <= k; groups++)
        {
            // need at least 'groups' elements remaining
            for (int i = 0; i <= n - groups; i++)
            {
                double best = 0.0;
                // split point j: first group is [i, j)
                // leave at least groups-1 elements after j
                for (int j = i + 1; j <= n - (groups - 1); j++)
                {
                    double cur = Avg(i, j) + dp[groups - 1, j];
                    if (cur > best) best = cur;
                }
                dp[groups, i] = best;
            }
        }

        return dp[k, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestSumOfAverages = function(nums, k) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }
    // base dp for 1 group: average of suffix starting at i
    let dp = new Array(n);
    for (let i = 0; i < n; ++i) {
        dp[i] = (pref[n] - pref[i]) / (n - i);
    }

    for (let groups = 2; groups <= k; ++groups) {
        const ndp = new Array(n).fill(0);
        // we need at least 'groups' elements from position i to end
        for (let i = 0; i <= n - groups; ++i) {
            let best = -Infinity;
            // j is the start of the next group, must leave enough elements for remaining groups-1
            for (let j = i + 1; j <= n - (groups - 1); ++j) {
                const curAvg = (pref[j] - pref[i]) / (j - i);
                const candidate = curAvg + dp[j];
                if (candidate > best) best = candidate;
            }
            ndp[i] = best;
        }
        dp = ndp;
    }

    return dp[0];
};
```

## Typescript

```typescript
function largestSumOfAverages(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const avg = (i: number, j: number): number => (prefix[j] - prefix[i]) / (j - i);

    // dp[i] = best score for subarray starting at i with current number of parts
    let dp = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        dp[i] = avg(i, n); // base case: only one part
    }

    for (let parts = 2; parts <= k; ++parts) {
        const ndp = new Array(n).fill(0);
        // we need at least (parts-1) elements after i to form remaining groups
        for (let i = 0; i <= n - parts; ++i) {
            let best = 0;
            const maxJ = n - (parts - 1); // last possible split point
            for (let j = i + 1; j <= maxJ; ++j) {
                const candidate = avg(i, j) + dp[j];
                if (candidate > best) best = candidate;
            }
            ndp[i] = best;
        }
        dp = ndp;
    }

    return dp[0];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function largestSumOfAverages($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0.0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }

        // dp[i]: best score for subarray starting at i with current number of groups
        $dp = array_fill(0, $n, 0.0);
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = ($prefix[$n] - $prefix[$i]) / ($n - $i);
        }

        // iterate groups from 2 to k
        for ($group = 2; $group <= $k; $group++) {
            $new = array_fill(0, $n, 0.0);
            // i can go up to n - group (at least one element per remaining group)
            for ($i = 0; $i <= $n - $group; $i++) {
                $best = 0.0;
                // j is end index of first group (exclusive), must leave at least group-1 elements
                for ($j = $i + 1; $j <= $n - ($group - 1); $j++) {
                    $avg = ($prefix[$j] - $prefix[$i]) / ($j - $i);
                    $candidate = $avg + $dp[$j];
                    if ($candidate > $best) {
                        $best = $candidate;
                    }
                }
                $new[$i] = $best;
            }
            $dp = $new;
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func largestSumOfAverages(_ nums: [Int], _ k: Int) -> Double {
        let n = nums.count
        var prefix = [Double](repeating: 0.0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Double(nums[i])
        }
        func avg(_ i: Int, _ j: Int) -> Double {
            return (prefix[j] - prefix[i]) / Double(j - i)
        }

        var dp = [Double](repeating: 0.0, count: n)
        for i in 0..<n {
            dp[i] = avg(i, n)
        }
        if k == 1 { return dp[0] }

        var groups = 2
        while groups <= k {
            var newDp = [Double](repeating: 0.0, count: n)
            let maxStart = n - (groups - 1) // earliest index where we can still have enough elements left
            for i in 0..<n {
                if i >= maxStart {
                    newDp[i] = dp[i]
                    continue
                }
                var best = 0.0
                var j = i + 1
                while j <= n - (groups - 1) {
                    let candidate = avg(i, j) + dp[j]
                    if candidate > best { best = candidate }
                    j += 1
                }
                newDp[i] = best
            }
            dp = newDp
            groups += 1
        }

        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestSumOfAverages(nums: IntArray, k: Int): Double {
        val n = nums.size
        val prefix = DoubleArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        fun avg(l: Int, r: Int): Double { // [l, r)
            return (prefix[r] - prefix[l]) / (r - l)
        }

        var dp = DoubleArray(n + 1)
        for (i in n - 1 downTo 0) {
            dp[i] = avg(i, n)
        }
        dp[n] = 0.0

        var groups = 1
        while (groups < k) {
            val newDp = DoubleArray(n + 1)
            newDp[n] = 0.0
            for (i in n - 1 downTo 0) {
                var best = avg(i, n)
                var j = i + 1
                while (j < n) {
                    val candidate = avg(i, j) + dp[j]
                    if (candidate > best) best = candidate
                    j++
                }
                newDp[i] = best
            }
            dp = newDp
            groups++
        }

        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  double largestSumOfAverages(List<int> nums, int k) {
    int n = nums.length;
    List<double> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + nums[i];
    }

    // dp[i]: best score for subarray starting at i with current number of groups
    List<double> dp = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      dp[i] = (prefix[n] - prefix[i]) / (n - i);
    }

    for (int groups = 2; groups <= k; groups++) {
      List<double> newDp = List.filled(n, 0);
      // Need at least 'groups' elements from i to end
      for (int i = 0; i <= n - groups; i++) {
        double best = 0;
        // j is the start of the next segment; ensure enough elements left for remaining groups-1
        for (int j = i + 1; j <= n - (groups - 1); j++) {
          double avg = (prefix[j] - prefix[i]) / (j - i);
          double candidate = avg + dp[j];
          if (candidate > best) best = candidate;
        }
        newDp[i] = best;
      }
      dp = newDp;
    }

    return dp[0];
  }
}
```

## Golang

```go
func largestSumOfAverages(nums []int, k int) float64 {
    n := len(nums)
    prefix := make([]float64, n+1)
    for i, v := range nums {
        prefix[i+1] = prefix[i] + float64(v)
    }

    // dp[i]: best score for subarray starting at i with current number of groups
    dp := make([]float64, n)
    for i := 0; i < n; i++ {
        dp[i] = (prefix[n] - prefix[i]) / float64(n-i)
    }

    for groups := 2; groups <= k; groups++ {
        ndp := make([]float64, n)
        // we need at least 'groups' elements from i to end
        limit := n - groups + 1
        for i := 0; i < limit; i++ {
            best := 0.0
            // j is the start index of the next group
            // ensure enough elements remain for (groups-1) groups
            maxJ := n - (groups - 1)
            for j := i + 1; j <= maxJ; j++ {
                avg := (prefix[j] - prefix[i]) / float64(j-i)
                cand := avg + dp[j]
                if cand > best {
                    best = cand
                }
            }
            ndp[i] = best
        }
        dp = ndp
    }

    return dp[0]
}
```

## Ruby

```ruby
def largest_sum_of_averages(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0.0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }

  dp = Array.new(n, 0.0)
  (0...n).each do |i|
    dp[i] = (prefix[n] - prefix[i]) / (n - i)
  end

  (2..k).each do |group|
    new_dp = Array.new(n, 0.0)
    max_i = n - group
    (0..max_i).each do |i|
      best = 0.0
      max_j = n - (group - 1)
      ((i + 1)..max_j).each do |j|
        avg = (prefix[j] - prefix[i]) / (j - i)
        val = avg + dp[j]
        best = val if val > best
      end
      new_dp[i] = best
    end
    dp = new_dp
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
  def largestSumOfAverages(nums: Array[Int], K: Int): Double = {
    val n = nums.length
    val prefix = new Array[Double](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i).toDouble
      i += 1
    }

    var dp = new Array[Double](n)
    i = 0
    while (i < n) {
      dp(i) = (prefix(n) - prefix(i)) / (n - i)
      i += 1
    }

    var groups = 2
    while (groups <= K) {
      val ndp = new Array[Double](n)
      i = 0
      while (i < n) {
        var best = 0.0
        var j = i + 1
        val maxJ = n - (groups - 1)
        while (j <= maxJ) {
          val avg = (prefix(j) - prefix(i)) / (j - i)
          val cand = avg + dp(j)
          if (cand > best) best = cand
          j += 1
        }
        ndp(i) = best
        i += 1
      }
      dp = ndp
      groups += 1
    }

    dp(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_sum_of_averages(nums: Vec<i32>, k: i32) -> f64 {
        let n = nums.len();
        let mut prefix = vec![0f64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as f64;
        }

        // dp[i]: best score for subarray starting at i with current number of groups
        let mut dp = vec![0f64; n];
        for i in 0..n {
            dp[i] = (prefix[n] - prefix[i]) / ((n - i) as f64);
        }

        let k_usize = k as usize;
        for groups in 2..=k_usize {
            let mut new_dp = vec![0f64; n];
            // need at least `groups` elements from i to end
            for i in 0..=n - groups {
                let mut best = 0f64;
                // first group ends at j (exclusive), leave enough elements for remaining groups
                for j in i + 1..=n - (groups - 1) {
                    let avg = (prefix[j] - prefix[i]) / ((j - i) as f64);
                    let candidate = avg + dp[j];
                    if candidate > best {
                        best = candidate;
                    }
                }
                new_dp[i] = best;
            }
            dp = new_dp;
        }

        dp[0]
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)

(define/contract (largest-sum-of-averages nums k)
  (-> (listof exact-integer?) exact-integer? flonum?)
  (let* ((n (length nums))
         (pref (make-vector (+ n 1) 0))
         (vec (list->vector nums)))
    ;; build prefix sums
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (vector-ref vec i))))
    (define (avg i j)
      (/ (exact->inexact (- (vector-ref pref j) (vector-ref pref i)))
         (- j i)))
    ;; dp for at most 1 group
    (let ((dp-prev (make-vector (+ n 1) 0.0)))
      (for ([i (in-range n)])
        (vector-set! dp-prev i (avg i n)))
      (vector-set! dp-prev n 0.0)
      ;; iterate groups from 2 to k
      (let loop ((g 2) (dp-prev dp-prev))
        (if (> g k)
            (vector-ref dp-prev 0)
            (let ((dp-curr (make-vector (+ n 1) 0.0)))
              (vector-set! dp-curr n 0.0)
              (for ([i (in-range (- n 1) -1 -1)])
                (let ((best (vector-ref dp-prev i)))
                  (for ([j (in-range (add1 i) (add1 n))])
                    (define cand (+ (avg i j) (vector-ref dp-prev j)))
                    (when (> cand best)
                      (set! best cand)))
                  (vector-set! dp-curr i best)))
              (loop (add1 g) dp-curr))))))))
```

## Erlang

```erlang
-spec largest_sum_of_averages(Nums :: [integer()], K :: integer()) -> float().
largest_sum_of_averages(Nums, K) ->
    N = length(Nums),
    Prefix = build_prefix_tuple(Nums),
    DP0 = init_dp(Prefix, N),
    DPK = compute_k(DP0, Prefix, N, K),
    element(1, DPK).

build_prefix_tuple(Nums) ->
    {RevList,_} = lists:foldl(
        fun(X,{Acc,Sum}) -> {[Sum+X | Acc], Sum+X} end,
        {[0],0},
        Nums),
    list_to_tuple(lists:reverse(RevList)).

init_dp(Prefix,N) ->
    List = [avg(Prefix, I, N) || I <- lists:seq(0,N-1)],
    list_to_tuple(List ++ [0]).

avg(Prefix,I,J) when J > I ->
    Sum = element(J+1, Prefix) - element(I+1, Prefix),
    Len = J - I,
    Sum / Len.

compute_k(DPPrev,_Prefix,_N,1) -> DPPrev;
compute_k(DPPrev, Prefix, N, K) when K > 1 ->
    DPCur = compute_dp(Prefix, DPPrev, N),
    compute_k(DPCur, Prefix, N, K-1).

compute_dp(Prefix, DPPrev, N) ->
    ListRev = compute_i(N-1, [], Prefix, DPPrev, N),
    list_to_tuple(lists:reverse(ListRev ++ [0])).

compute_i(-1, Acc, _Prefix, _DPPrev, _N) -> Acc;
compute_i(I, Acc, Prefix, DPPrev, N) ->
    Max = max_over_j(I+1, N, Prefix, DPPrev, I),
    compute_i(I-1, [Max|Acc], Prefix, DPPrev, N).

max_over_j(JStart, JEnd, Prefix, DPPrev, I) ->
    max_over_j(JStart, JEnd, Prefix, DPPrev, I, 0.0).

max_over_j(J, End, _Prefix, _DPPrev, _I, Max) when J > End -> Max;
max_over_j(J, End, Prefix, DPPrev, I, CurMax) ->
    Val = avg(Prefix, I, J) + element(J+1, DPPrev),
    NewMax = if Val > CurMax -> Val; true -> CurMax end,
    max_over_j(J+1, End, Prefix, DPPrev, I, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_sum_of_averages(nums :: [integer], k :: integer) :: float
  def largest_sum_of_averages(nums, k) do
    n = length(nums)
    prefix = prefix_sums(nums)

    # dp[i] = best score for subarray starting at i using up to current number of groups
    dp_initial =
      for i <- 0..(n - 1) do
        (Enum.at(prefix, n) - Enum.at(prefix, i)) / (n - i)
      end

    dp_final =
      Enum.reduce(2..k, dp_initial, fn group, dp_acc ->
        new_dp =
          for i <- 0..(n - 1) do
            base = (Enum.at(prefix, n) - Enum.at(prefix, i)) / (n - i)

            if i + 1 <= n - (group - 1) do
              Enum.reduce((i + 1)..(n - (group - 1)), base, fn j, best ->
                avg = (Enum.at(prefix, j) - Enum.at(prefix, i)) / (j - i)
                cand = avg + Enum.at(dp_acc, j)

                if cand > best, do: cand, else: best
              end)
            else
              base
            end
          end

        new_dp
      end)

    List.first(dp_final)
  end

  defp prefix_sums(nums) do
    # returns list where prefix[0] = 0 and prefix[i] = sum of first i elements
    Enum.reduce(nums, [0], fn x, acc ->
      [hd(acc) + x | acc]
    end)
    |> Enum.reverse()
  end
end
```
