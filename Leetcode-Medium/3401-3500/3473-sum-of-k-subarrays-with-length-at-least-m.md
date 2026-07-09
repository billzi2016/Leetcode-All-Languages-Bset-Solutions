# 3473. Sum of K Subarrays With Length at Least M

## Cpp

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums, int k, int m) {
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 1; i <= n; ++i) pref[i] = pref[i - 1] + nums[i - 1];
        const long long NEG = -(1LL << 60);
        vector<vector<long long>> dp(k + 1, vector<long long>(n + 1, NEG));
        for (int i = 0; i <= n; ++i) dp[0][i] = 0;
        for (int t = 1; t <= k; ++t) {
            long long best = NEG;
            for (int i = 1; i <= n; ++i) {
                if (i - m >= 0) {
                    int s = i - m + 1; // start index (1‑based)
                    long long prev = dp[t - 1][s - 1];
                    if (prev != NEG) best = max(best, prev - pref[s - 1]);
                }
                dp[t][i] = dp[t][i - 1];
                if (best != NEG) dp[t][i] = max(dp[t][i], pref[i] + best);
            }
        }
        return (int)dp[k][n];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxSum(int[] nums, int k, int m) {
        int n = nums.length;
        long[] pre = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            pre[i] = pre[i - 1] + nums[i - 1];
        }
        long NEG = Long.MIN / 4;
        long[] dpPrev = new long[n + 1];
        Arrays.fill(dpPrev, NEG);
        dpPrev[0] = 0; // zero subarrays sum to 0

        for (int t = 1; t <= k; t++) {
            long[] dpCurr = new long[n + 1];
            Arrays.fill(dpCurr, NEG);
            long bestPrev = NEG;
            for (int i = 1; i <= n; i++) {
                if (i - m >= 0) {
                    int s = i - m;
                    long cand = dpPrev[s] - pre[s];
                    if (cand > bestPrev) bestPrev = cand;
                }
                long notTake = dpCurr[i - 1];
                long take = NEG;
                if (bestPrev != NEG) {
                    take = bestPrev + pre[i];
                }
                dpCurr[i] = Math.max(notTake, take);
            }
            dpPrev = dpCurr;
        }
        return (int) dpPrev[n];
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums, k, m):
        """
        :type nums: List[int]
        :type k: int
        :type m: int
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        NEG_INF = -10**18
        dp = [[NEG_INF] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0

        for t in range(1, k + 1):
            best = NEG_INF
            # handle positions before we can place a subarray of length m
            for i in range(1, m):
                dp[t][i] = dp[t][i - 1]
            for i in range(m, n + 1):
                j = i - m
                cand = dp[t - 1][j] - pre[j]
                if cand > best:
                    best = cand
                val = pre[i] + best
                # choose not to end a subarray at i or take the best ending here
                if dp[t][i - 1] > val:
                    dp[t][i] = dp[t][i - 1]
                else:
                    dp[t][i] = val

        return dp[k][n]
```

## Python3

```python
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        NEG_INF = -10**18
        dp = [[NEG_INF] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0

        for t in range(1, k + 1):
            best_prev = NEG_INF
            for i in range(1, n + 1):
                if i - m >= 0:
                    val = dp[t - 1][i - m] - pref[i - m]
                    if val > best_prev:
                        best_prev = val
                cand = NEG_INF
                if best_prev != NEG_INF:
                    cand = pref[i] + best_prev
                not_take = dp[t][i - 1]
                dp[t][i] = not_take if not_take > cand else cand

        return dp[k][n]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maxSum(int* nums, int numsSize, int k, int m) {
    int n = numsSize;
    long long *pref = (long long*)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 1; i <= n; ++i) {
        pref[i] = pref[i - 1] + nums[i - 1];
    }

    const long long NEG_INF = -(1LL << 60);
    int stride = n + 1;
    long long *dp = (long long*)malloc((k + 1) * stride * sizeof(long long));
    for (int t = 0; t <= k; ++t) {
        for (int i = 0; i <= n; ++i) {
            dp[t * stride + i] = NEG_INF;
        }
    }
    for (int i = 0; i <= n; ++i) dp[i] = 0; // dp[0][i] = 0

    for (int t = 1; t <= k; ++t) {
        long long best = NEG_INF;
        for (int i = 1; i <= n; ++i) {
            if (i - m >= 0) {
                long long cand = dp[(t - 1) * stride + (i - m)] - pref[i - m];
                if (cand > best) best = cand;
            }
            long long cur = dp[t * stride + (i - 1)];
            if (best != NEG_INF) {
                long long take = pref[i] + best;
                if (take > cur) cur = take;
            }
            dp[t * stride + i] = cur;
        }
    }

    int result = (int)dp[k * stride + n];
    free(pref);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSum(int[] nums, int k, int m) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        const long NEG = long.MinValue / 4;
        long[,] dp = new long[k + 1, n + 1];

        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i, j] = NEG;
            }
        }

        for (int j = 0; j <= n; j++) dp[0, j] = 0;

        for (int i = 1; i <= k; i++) {
            long best = NEG;
            for (int j = 1; j <= n; j++) {
                if (j - m >= 0) {
                    long cand = dp[i - 1, j - m] - prefix[j - m];
                    if (cand > best) best = cand;
                }
                long val = dp[i, j - 1];
                if (best != NEG) {
                    long take = best + prefix[j];
                    if (take > val) val = take;
                }
                dp[i, j] = val;
            }
        }

        return (int)dp[k, n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} m
 * @return {number}
 */
var maxSum = function(nums, k, m) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }

    let dpPrev = new Array(n + 1).fill(Number.NEGATIVE_INFINITY);
    dpPrev[0] = 0;

    for (let t = 1; t <= k; ++t) {
        const dpCurr = new Array(n + 1).fill(Number.NEGATIVE_INFINITY);
        let best = Number.NEGATIVE_INFINITY;
        for (let i = 1; i <= n; ++i) {
            if (i >= m) {
                const s = i - m;
                const cand = dpPrev[s] - pref[s];
                if (cand > best) best = cand;
                const val = pref[i] + best;
                dpCurr[i] = Math.max(dpCurr[i - 1], val);
            } else {
                dpCurr[i] = dpCurr[i - 1];
            }
        }
        dpPrev = dpCurr;
    }

    return dpPrev[n];
};
```

## Typescript

```typescript
function maxSum(nums: number[], k: number, m: number): number {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; ++i) pref[i] = pref[i - 1] + nums[i - 1];

    let dpPrev = new Array(n + 1).fill(Number.NEGATIVE_INFINITY);
    dpPrev[0] = 0;

    for (let t = 1; t <= k; ++t) {
        const dpCurr = new Array(n + 1).fill(Number.NEGATIVE_INFINITY);
        let best = Number.NEGATIVE_INFINITY;
        for (let i = m; i <= n; ++i) {
            const j = i - m;
            const candBest = dpPrev[j] - pref[j];
            if (candBest > best) best = candBest;

            const cand = best + pref[i];
            dpCurr[i] = Math.max(dpCurr[i - 1], cand);
        }
        // propagate for positions before m
        for (let i = 1; i < m && i <= n; ++i) {
            if (dpCurr[i - 1] > dpCurr[i]) dpCurr[i] = dpCurr[i - 1];
        }
        dpPrev = dpCurr;
    }

    return dpPrev[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $m
     * @return Integer
     */
    function maxSum($nums, $k, $m) {
        $n = count($nums);
        // prefix sums
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $prefix[$i] = $prefix[$i - 1] + $nums[$i - 1];
        }

        $negInf = -(1 << 60); // sufficiently small negative number

        // dp[i][j]: max sum using i subarrays within first j elements
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, $negInf));
        for ($j = 0; $j <= $n; $j++) {
            $dp[0][$j] = 0;
        }

        for ($i = 1; $i <= $k; $i++) {
            $bestPrev = $negInf;
            for ($j = 1; $j <= $n; $j++) {
                if ($j >= $m) {
                    $t = $j - $m + 1; // start index of the shortest allowed subarray ending at j
                    $candidate = $dp[$i - 1][$t - 1] - $prefix[$t - 1];
                    if ($candidate > $bestPrev) {
                        $bestPrev = $candidate;
                    }
                }

                $val = $dp[$i][$j - 1]; // not using element j
                if ($bestPrev != $negInf) {
                    $temp = $bestPrev + $prefix[$j];
                    if ($temp > $val) {
                        $val = $temp;
                    }
                }
                $dp[$i][$j] = $val;
            }
        }

        return $dp[$k][$n];
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        let n = nums.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        let NEG = Int.min / 4
        var dpPrev = [Int](repeating: 0, count: n + 1)   // dp for t-1
        var dpCurr = [Int](repeating: NEG, count: n + 1) // dp for current t
        
        if k == 0 { return 0 }
        
        for _ in 1...k {
            var best = NEG
            dpCurr[0] = NEG
            for i in 1...n {
                let p = i - m
                if p >= 0 {
                    let cand = dpPrev[p] - prefix[p]
                    if cand > best { best = cand }
                }
                var val = dpCurr[i - 1]   // not taking a subarray ending at i
                if best > NEG {
                    let cand = prefix[i] + best
                    if cand > val { val = cand }
                }
                dpCurr[i] = val
            }
            dpPrev = dpCurr
        }
        return dpPrev[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums: IntArray, k: Int, m: Int): Int {
        val n = nums.size
        val pref = IntArray(n + 1)
        for (i in 1..n) {
            pref[i] = pref[i - 1] + nums[i - 1]
        }
        val NEG = Int.MIN_VALUE / 4
        var dpPrev = IntArray(n + 1) { 0 } // zero subarrays sum to 0
        for (t in 1..k) {
            val dpCurr = IntArray(n + 1) { NEG }
            var best = NEG
            for (i in 1..n) {
                if (i - m >= 0) {
                    val s = i - m
                    val candBest = dpPrev[s] - pref[s]
                    if (candBest > best) best = candBest
                }
                var value = dpCurr[i - 1]
                if (best != NEG) {
                    val cand = pref[i] + best
                    if (cand > value) value = cand
                }
                dpCurr[i] = value
            }
            dpPrev = dpCurr
        }
        return dpPrev[n]
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<int> nums, int k, int m) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }
    const int INF_NEG = -1 << 60; // sufficiently small negative value

    // dp[t][i]: max sum using t subarrays within first i elements
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n + 1, INF_NEG));
    for (int i = 0; i <= n; ++i) {
      dp[0][i] = 0;
    }

    for (int t = 1; t <= k; ++t) {
      int best = INF_NEG; // max of dp[t-1][j] - prefix[j] for j <= i-m
      for (int i = 1; i <= n; ++i) {
        if (i - m >= 0) {
          int j = i - m;
          int candidatePrev = dp[t - 1][j];
          if (candidatePrev != INF_NEG) {
            int val = candidatePrev - prefix[j];
            if (val > best) best = val;
          }
        }

        int take = INF_NEG;
        if (best != INF_NEG) {
          take = best + prefix[i];
        }
        int notTake = dp[t][i - 1];
        dp[t][i] = notTake > take ? notTake : take;
      }
    }

    return dp[k][n];
  }
}
```

## Golang

```go
func maxSum(nums []int, k int, m int) int {
    n := len(nums)
    pref := make([]int64, n+1)
    for i := 1; i <= n; i++ {
        pref[i] = pref[i-1] + int64(nums[i-1])
    }
    const INF int64 = -1 << 60
    dp := make([][]int64, k+1)
    for i := 0; i <= k; i++ {
        dp[i] = make([]int64, n+1)
        for j := 0; j <= n; j++ {
            dp[i][j] = INF
        }
    }
    for j := 0; j <= n; j++ {
        dp[0][j] = 0
    }

    for i := 1; i <= k; i++ {
        best := INF
        for j := 1; j <= n; j++ {
            if j-m >= 0 {
                cand := dp[i-1][j-m] - pref[j-m]
                if cand > best {
                    best = cand
                }
            }
            val := dp[i][j-1]
            if best != INF {
                take := pref[j] + best
                if take > val {
                    val = take
                }
            }
            dp[i][j] = val
        }
    }
    return int(dp[k][n])
}
```

## Ruby

```ruby
def max_sum(nums, k, m)
  n = nums.length
  ps = Array.new(n + 1, 0)
  (1..n).each { |i| ps[i] = ps[i - 1] + nums[i - 1] }

  neg_inf = -10**18
  dp_prev = Array.new(n + 1, 0) # zero subarrays sum to 0

  1.upto(k) do |_t|
    dp_cur = Array.new(n + 1, neg_inf)
    best = neg_inf
    (1..n).each do |i|
      if i - m >= 0
        cand = dp_prev[i - m] - ps[i - m]
        best = cand > best ? cand : best
      end
      take = best == neg_inf ? neg_inf : ps[i] + best
      not_take = dp_cur[i - 1]
      dp_cur[i] = take > not_take ? take : not_take
    end
    dp_prev = dp_cur
  end

  dp_prev[n]
end
```

## Scala

```scala
object Solution {
    def maxSum(nums: Array[Int], k: Int, m: Int): Int = {
        val n = nums.length
        val pre = new Array[Int](n + 1)
        for (i <- 0 until n) pre(i + 1) = pre(i) + nums(i)

        val NEG = -1000000000
        var dpPrev = Array.fill(n + 1)(NEG)
        dpPrev(0) = 0

        for (_ <- 1 to k) {
            val dpCurr = Array.fill(n + 1)(NEG)
            var best = NEG
            // propagate for i < m (cannot finish a subarray yet)
            for (i <- 1 until m) {
                dpCurr(i) = dpCurr(i - 1)
            }
            for (i <- m to n) {
                val p = i - m
                if (dpPrev(p) != NEG) {
                    best = math.max(best, dpPrev(p) - pre(p))
                }
                var cand = NEG
                if (best != NEG) cand = best + pre(i)
                dpCurr(i) = math.max(dpCurr(i - 1), cand)
            }
            dpPrev = dpCurr
        }

        dpPrev(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32, m: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        let m_usize = m as usize;

        // prefix sums
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }

        const NEG_INF: i64 = -9_000_000_000_000_i64; // sufficiently small

        // dp for t = 0
        let mut dp_prev = vec![0i64; n + 1];

        for _ in 1..=k_usize {
            let mut dp_curr = vec![NEG_INF; n + 1];
            let mut best = NEG_INF;

            // i is the exclusive end index of a subarray
            for i in m_usize..=n {
                let s = i - m_usize;
                let cand = dp_prev[s] - pref[s];
                if cand > best {
                    best = cand;
                }
                let val = best + pref[i];
                let prev = dp_curr[i - 1];
                dp_curr[i] = if val > prev { val } else { prev };
            }

            dp_prev = dp_curr;
        }

        dp_prev[n] as i32
    }
}
```

## Racket

```racket
(define/contract (max-sum nums k m)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (pref (make-vector (+ n 1) 0)))
    ;; prefix sums
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! pref i
                   (+ (vector-ref pref (- i 1))
                      (vector-ref arr (- i 1)))))
    (define NEG -1000000000000000) ; sufficiently small negative
    ;; dp for 0 subarrays: all zeros
    (let ((prev (make-vector (+ n 1) 0)))
      (for ([t (in-range 1 (+ k 1))])
        (define curr (make-vector (+ n 1) NEG))
        (vector-set! curr 0 NEG)
        (for ([i (in-range 1 (+ n 1))])
          (define best (vector-ref curr (- i 1))) ; not take ending at i
          ;; consider taking a subarray ending at i with length >= m
          (let loop ((len m) (best-so-far best))
            (if (> len i)
                (vector-set! curr i best-so-far)
                (let* ((j (- i len))
                       (candidate (+ (vector-ref prev j)
                                     (- (vector-ref pref i) (vector-ref pref j)))))
                  (loop (+ len 1)
                        (if (> candidate best-so-far) candidate best-so-far))))))
        (set! prev curr))
      (vector-ref prev n))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum/3]).

-spec max_sum(Nums :: [integer()], K :: integer(), M :: integer()) -> integer().
max_sum(Nums, K, M) ->
    N = length(Nums),
    Prefix = build_prefix(Nums, N),
    NegInf = -1000000000,
    DPPrev = array:new(N+1, {default, 0}),
    ResultDP = loop_t(1, K, M, N, Prefix, DPPrev, NegInf),
    array:get(N, ResultDP).

build_prefix(Nums, N) ->
    A0 = array:new(N+1, {default, 0}),
    build_prefix_loop(Nums, 1, 0, A0).

build_prefix_loop([], _Idx, _Acc, Arr) -> Arr;
build_prefix_loop([H|T], Idx, Acc, Arr) ->
    NewAcc = Acc + H,
    Arr1 = array:set(Idx, NewAcc, Arr),
    build_prefix_loop(T, Idx+1, NewAcc, Arr1).

loop_t(T, K, _M, _N, _Prefix, DPPrev, _NegInf) when T > K ->
    DPPrev;
loop_t(T, K, M, N, Prefix, DPPrev, NegInf) ->
    CurrDP = compute_layer(1, N, M, Prefix, DPPrev, NegInf,
                           array:new(N+1, {default, NegInf})),
    loop_t(T+1, K, M, N, Prefix, CurrDP, NegInf).

compute_layer(I, N, _M, _Prefix, _DPPrev, _NegInf, CurrArr) when I > N ->
    CurrArr;
compute_layer(I, N, M, Prefix, DPPrev, NegInf, CurrArr) ->
    PrevVal = array:get(I-1, CurrArr),
    Best0 = PrevVal,
    MaxLen = I,
    Best = loop_len(M, MaxLen, I, Prefix, DPPrev, NegInf, Best0),
    NewCurrArr = array:set(I, Best, CurrArr),
    compute_layer(I+1, N, M, Prefix, DPPrev, NegInf, NewCurrArr).

loop_len(Len, MaxLen, _I, _Prefix, _DPPrev, _NegInf, Best) when Len > MaxLen ->
    Best;
loop_len(Len, MaxLen, I, Prefix, DPPrev, NegInf, Best) ->
    StartIdx = I - Len,
    Sum = array:get(I, Prefix) - array:get(StartIdx, Prefix),
    PrevDPVal = array:get(StartIdx, DPPrev),
    Candidate = case PrevDPVal of
        NegInf -> NegInf;
        _ -> PrevDPVal + Sum
    end,
    NewBest = if Candidate > Best -> Candidate; true -> Best end,
    loop_len(Len+1, MaxLen, I, Prefix, DPPrev, NegInf, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer], k :: integer, m :: integer) :: integer
  def max_sum(nums, k, m) do
    n = length(nums)

    # prefix sums: ps[0] = 0, ps[i] = sum of first i elements (1-indexed)
    ps_list = [0] ++ Enum.scan(nums, 0, fn x, acc -> acc + x end)
    ps_arr = :array.from_list(ps_list)

    neg_inf = -1_000_000_000

    # dp for 0 subarrays: all zeros
    dp_prev = :array.new(n + 1, default: 0)

    dp_k =
      Enum.reduce(1..k, dp_prev, fn _t, prev_row ->
        cur_arr = :array.new(n + 1, default: neg_inf)

        {_, cur_filled} =
          Enum.reduce(m..n, {neg_inf, cur_arr}, fn i, {best, arr} ->
            s = i - m + 1
            val_prev = :array.get(s - 1, prev_row)
            ps_s_1 = :array.get(s - 1, ps_arr)
            cand_best = val_prev - ps_s_1
            best2 = if cand_best > best, do: cand_best, else: best

            cur_without = :array.get(i - 1, arr)
            candidate = best2 + :array.get(i, ps_arr)

            new_val = if candidate > cur_without, do: candidate, else: cur_without
            {:ok, arr2} = :array.set(i, new_val, arr)
            {best2, arr2}
          end)

        cur_filled
      end)

    :array.get(n, dp_k)
  end
end
```
