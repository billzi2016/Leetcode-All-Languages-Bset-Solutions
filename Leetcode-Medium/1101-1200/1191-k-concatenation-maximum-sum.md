# 1191. K-Concatenation Maximum Sum

## Cpp

```cpp
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        const long long MOD = 1000000007LL;
        long long total = 0;
        for (int v : arr) total += v;

        // Kadane for single array
        long long cur = 0, bestSingle = 0;
        for (int v : arr) {
            cur = max(0LL, cur + v);
            bestSingle = max(bestSingle, cur);
        }
        if (k == 1) return (int)(bestSingle % MOD);

        // Max prefix sum
        long long pref = LLONG_MIN, sum = 0;
        for (int v : arr) {
            sum += v;
            pref = max(pref, sum);
        }

        // Max suffix sum
        long long suff = LLONG_MIN; 
        sum = 0;
        for (int i = (int)arr.size() - 1; i >= 0; --i) {
            sum += arr[i];
            suff = max(suff, sum);
        }

        // Kadane on two concatenated copies
        cur = 0;
        long long bestTwo = 0;
        int n = arr.size();
        for (int i = 0; i < 2 * n; ++i) {
            long long v = arr[i % n];
            cur = max(0LL, cur + v);
            bestTwo = max(bestTwo, cur);
        }

        long long ans = bestTwo;
        if (total > 0) {
            ans = max(ans, pref + suff + (long long)(k - 2) * total);
        }
        ans %= MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int kConcatenationMaxSum(int[] arr, int k) {
        long totalSum = 0;
        long maxPrefix = Long.MIN_VALUE;
        long cur = 0;
        for (int num : arr) {
            cur += num;
            if (cur > maxPrefix) maxPrefix = cur;
        }
        totalSum = cur;
        
        long maxSuffix = Long.MIN_VALUE;
        cur = 0;
        for (int i = arr.length - 1; i >= 0; --i) {
            cur += arr[i];
            if (cur > maxSuffix) maxSuffix = cur;
        }
        
        // Kadane's algorithm for maximum subarray sum (non-empty)
        long maxKadane = Long.MIN_VALUE;
        long bestEndingHere = 0;
        for (int num : arr) {
            bestEndingHere = Math.max(num, bestEndingHere + num);
            maxKadane = Math.max(maxKadane, bestEndingHere);
        }
        
        if (k == 1) {
            long ans = Math.max(0L, maxKadane);
            return (int)(ans % MOD);
        }
        
        long candidate;
        if (totalSum > 0) {
            candidate = maxPrefix + maxSuffix + (long)(k - 2) * totalSum;
        } else {
            candidate = maxPrefix + maxSuffix;
        }
        long ans = Math.max(maxKadane, candidate);
        ans = Math.max(0L, ans);
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Kadane's algorithm for one copy
        cur = best = arr[0]
        for x in arr[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        max_one = max(0, best)

        if k == 1:
            return max_one % MOD

        total = sum(arr)

        # maximum prefix sum
        pref_sum = 0
        max_pref = -10**18
        for x in arr:
            pref_sum += x
            if pref_sum > max_pref:
                max_pref = pref_sum

        # maximum suffix sum
        suff_sum = 0
        max_suff = -10**18
        for x in reversed(arr):
            suff_sum += x
            if suff_sum > max_suff:
                max_suff = suff_sum

        candidate2 = max_pref + max_suff + max(0, total) * (k - 2)
        ans = max(max_one, candidate2)

        return ans % MOD
```

## Python3

```python
from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Kadane's algorithm for max subarray sum (allow empty)
        cur = 0
        max_sub = 0
        for x in arr:
            cur = max(0, cur + x)
            max_sub = max(max_sub, cur)
        
        if k == 1:
            return max_sub % MOD
        
        total = sum(arr)
        
        # max prefix sum
        pref = 0
        max_pref = float('-inf')
        for x in arr:
            pref += x
            max_pref = max(max_pref, pref)
        
        # max suffix sum
        suff = 0
        max_suff = float('-inf')
        for x in reversed(arr):
            suff += x
            max_suff = max(max_suff, suff)
        
        if total > 0:
            ans = max(max_sub, max_pref + max_suff + (k - 2) * total)
        else:
            ans = max(max_sub, max_pref + max_suff)
        
        return ans % MOD
```

## C

```c
#include <limits.h>

int kConcatenationMaxSum(int* arr, int arrSize, int k) {
    const long long MOD = 1000000007LL;
    
    long long maxSub = LLONG_MIN;
    long long cur = 0;
    long long sumAll = 0;
    for (int i = 0; i < arrSize; ++i) {
        long long x = arr[i];
        if (cur > 0)
            cur += x;
        else
            cur = x;
        if (cur > maxSub) maxSub = cur;
        sumAll += x;
    }
    
    long long pref = LLONG_MIN, cum = 0;
    for (int i = 0; i < arrSize; ++i) {
        cum += arr[i];
        if (cum > pref) pref = cum;
    }
    
    long long suff = LLONG_MIN;
    cum = 0;
    for (int i = arrSize - 1; i >= 0; --i) {
        cum += arr[i];
        if (cum > suff) suff = cum;
    }
    
    long long ans;
    if (k == 1) {
        ans = maxSub;
    } else {
        if (sumAll > 0) {
            long long candidate = pref + suff + (long long)(k - 2) * sumAll;
            ans = maxSub > candidate ? maxSub : candidate;
        } else {
            long long candidate = pref + suff;
            ans = maxSub > candidate ? maxSub : candidate;
        }
    }
    
    if (ans < 0) ans = 0;
    ans %= MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int KConcatenationMaxSum(int[] arr, int k) {
        const long MOD = 1000000007L;
        
        // Kadane's algorithm for one copy (allow empty subarray)
        long maxKadane = 0, cur = 0;
        foreach (int v in arr) {
            cur = Math.Max(0, cur + v);
            maxKadane = Math.Max(maxKadane, cur);
        }
        if (k == 1) return (int)(maxKadane % MOD);
        
        // Total sum of the original array
        long total = 0;
        foreach (int v in arr) total += v;
        
        // Maximum prefix sum
        long prefSum = 0, maxPref = long.MinValue;
        foreach (int v in arr) {
            prefSum += v;
            if (prefSum > maxPref) maxPref = prefSum;
        }
        
        // Maximum suffix sum
        long suffSum = 0, maxSuff = long.MinValue;
        for (int i = arr.Length - 1; i >= 0; --i) {
            suffSum += arr[i];
            if (suffSum > maxSuff) maxSuff = suffSum;
        }
        
        // If total sum is positive, we can add it (k-2) more times
        long extra = total > 0 ? total * (k - 2) : 0;
        long candidate = maxPref + maxSuff + extra;
        
        long ans = Math.Max(maxKadane, candidate);
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var kConcatenationMaxSum = function(arr, k) {
    const MOD = 1000000007;
    
    // Kadane for single array (allow empty subarray)
    let cur = 0, best = 0;
    for (let x of arr) {
        cur = Math.max(0, cur + x);
        if (cur > best) best = cur;
    }
    
    if (k === 1) return best % MOD;
    
    // total sum, max prefix, max suffix
    let total = 0;
    for (let x of arr) total += x;
    
    let maxPrefix = -Infinity, sum = 0;
    for (let x of arr) {
        sum += x;
        if (sum > maxPrefix) maxPrefix = sum;
    }
    
    let maxSuffix = -Infinity; sum = 0;
    for (let i = arr.length - 1; i >= 0; --i) {
        sum += arr[i];
        if (sum > maxSuffix) maxSuffix = sum;
    }
    
    let ans = best;
    if (total > 0) {
        const candidate = maxPrefix + maxSuffix + (k - 2) * total;
        if (candidate > ans) ans = candidate;
    } else {
        const candidate = maxPrefix + maxSuffix;
        if (candidate > ans) ans = candidate;
    }
    
    return ((ans % MOD) + MOD) % MOD;
};
```

## Typescript

```typescript
function kConcatenationMaxSum(arr: number[], k: number): number {
    const MOD = 1000000007;
    // Kadane for max subarray sum (empty allowed)
    let cur = 0, maxSub = 0;
    for (const v of arr) {
        cur = Math.max(0, cur + v);
        if (cur > maxSub) maxSub = cur;
    }
    if (k === 1) return maxSub % MOD;

    // total sum
    let total = 0;
    for (const v of arr) total += v;

    // max prefix sum
    let pref = -Infinity, sum = 0;
    for (const v of arr) {
        sum += v;
        if (sum > pref) pref = sum;
    }

    // max suffix sum
    let suff = -Infinity;
    sum = 0;
    for (let i = arr.length - 1; i >= 0; --i) {
        sum += arr[i];
        if (sum > suff) suff = sum;
    }

    let ans = Math.max(maxSub, pref + suff);
    if (total > 0) {
        const candidate = pref + suff + (k - 2) * total;
        if (candidate > ans) ans = candidate;
    }
    return ((ans % MOD) + MOD) % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function kConcatenationMaxSum($arr, $k) {
        $mod = 1000000007;
        $n = count($arr);
        
        // Kadane for single array (allow empty subarray)
        $maxKadane = 0;
        $cur = 0;
        foreach ($arr as $v) {
            $cur = max(0, $cur + $v);
            if ($cur > $maxKadane) $maxKadane = $cur;
        }
        
        if ($k == 1) {
            return $maxKadane % $mod;
        }
        
        // total sum of the array
        $total = 0;
        foreach ($arr as $v) {
            $total += $v;
        }
        
        // max prefix sum
        $prefixSum = 0;
        $maxPrefix = PHP_INT_MIN;
        foreach ($arr as $v) {
            $prefixSum += $v;
            if ($prefixSum > $maxPrefix) $maxPrefix = $prefixSum;
        }
        
        // max suffix sum
        $suffixSum = 0;
        $maxSuffix = PHP_INT_MIN;
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffixSum += $arr[$i];
            if ($suffixSum > $maxSuffix) $maxSuffix = $suffixSum;
        }
        
        // candidate using two concatenations
        $candidate = $maxPrefix + $maxSuffix;
        if ($total > 0) {
            $candidate = max($candidate, $maxPrefix + $maxSuffix + ($k - 2) * $total);
        }
        
        $ans = max($maxKadane, $candidate);
        $ans %= $mod;
        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func kConcatenationMaxSum(_ arr: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var total: Int64 = 0
        for v in arr { total += Int64(v) }
        
        // Kadane's algorithm for max subarray sum (non‑empty)
        var maxEnding: Int64 = 0
        var maxKadane: Int64 = Int64.min
        for v in arr {
            let val = Int64(v)
            maxEnding = max(val, maxEnding + val)
            maxKadane = max(maxKadane, maxEnding)
        }
        
        // Maximum prefix sum
        var cur: Int64 = 0
        var maxPrefix: Int64 = Int64.min
        for v in arr {
            cur += Int64(v)
            if cur > maxPrefix { maxPrefix = cur }
        }
        
        // Maximum suffix sum
        cur = 0
        var maxSuffix: Int64 = Int64.min
        for v in arr.reversed() {
            cur += Int64(v)
            if cur > maxSuffix { maxSuffix = cur }
        }
        
        var answer: Int64 = 0
        if k == 1 {
            answer = max(0, maxKadane)
        } else {
            if total > 0 {
                let candidate = maxPrefix + maxSuffix + (Int64(k) - 2) * total
                answer = max(maxKadane, candidate)
            } else {
                let candidate = maxPrefix + maxSuffix
                answer = max(maxKadane, candidate)
            }
            answer = max(0, answer)
        }
        
        return Int(answer % Int64(MOD))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kConcatenationMaxSum(arr: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L

        fun kadane(a: IntArray): Long {
            var maxEnding = 0L
            var maxSoFar = 0L
            for (v in a) {
                maxEnding = kotlin.math.max(0L, maxEnding + v)
                maxSoFar = kotlin.math.max(maxSoFar, maxEnding)
            }
            return maxSoFar
        }

        val kadaneOne = kadane(arr)
        if (k == 1) return ((kadaneOne % MOD).toInt())

        var total = 0L
        for (v in arr) total += v

        var prefixSum = 0L
        var maxPrefix = Long.MIN_VALUE
        for (v in arr) {
            prefixSum += v
            if (prefixSum > maxPrefix) maxPrefix = prefixSum
        }

        var suffixSum = 0L
        var maxSuffix = Long.MIN_VALUE
        for (i in arr.size - 1 downTo 0) {
            suffixSum += arr[i]
            if (suffixSum > maxSuffix) maxSuffix = suffixSum
        }

        var ans = kadaneOne
        if (total > 0) {
            val candidate = maxPrefix + maxSuffix + total * (k - 2).toLong()
            ans = kotlin.math.max(ans, candidate)
        } else {
            val candidate = maxPrefix + maxSuffix
            ans = kotlin.math.max(ans, candidate)
        }

        return ((ans % MOD + MOD) % MOD).toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int _MOD = 1000000007;

  int kConcatenationMaxSum(List<int> arr, int k) {
    int n = arr.length;
    int total = 0;
    for (int v in arr) total += v;

    // Kadane's algorithm for max subarray sum (non‑empty)
    int cur = 0;
    int maxSub = -(1 << 60);
    for (int v in arr) {
      cur = cur > 0 ? cur + v : v;
      if (cur > maxSub) maxSub = cur;
    }

    // Max prefix sum
    int maxPrefix = -(1 << 60);
    int sum = 0;
    for (int v in arr) {
      sum += v;
      if (sum > maxPrefix) maxPrefix = sum;
    }

    // Max suffix sum
    int maxSuffix = -(1 << 60);
    sum = 0;
    for (int i = n - 1; i >= 0; --i) {
      sum += arr[i];
      if (sum > maxSuffix) maxSuffix = sum;
    }

    int ans;
    if (k == 1) {
      ans = maxSub;
    } else {
      if (total > 0) {
        int candidate = maxPrefix + maxSuffix + total * (k - 2);
        ans = max(maxSub, candidate);
      } else {
        int candidate = maxPrefix + maxSuffix;
        ans = max(maxSub, candidate);
      }
    }

    if (ans < 0) ans = 0;
    return ans % _MOD;
  }
}
```

## Golang

```go
func kConcatenationMaxSum(arr []int, k int) int {
	const MOD int64 = 1000000007

	maxInt64 := func(a, b int64) int64 {
		if a > b {
			return a
		}
		return b
	}

	// Kadane's algorithm for non‑empty subarray maximum sum
	kadane := func(nums []int) int64 {
		var maxEnding, maxSoFar int64 = 0, -(1 << 60)
		for _, v := range nums {
			val := int64(v)
			if maxEnding < 0 {
				maxEnding = val
			} else {
				maxEnding += val
			}
			if maxEnding > maxSoFar {
				maxSoFar = maxEnding
			}
		}
		return maxSoFar
	}

	n := len(arr)

	// total sum, prefix max, suffix max
	var totalSum int64
	var maxPrefix int64 = -(1 << 60)
	var cur int64 = 0
	for i := 0; i < n; i++ {
		cur += int64(arr[i])
		if cur > maxPrefix {
			maxPrefix = cur
		}
	}
	totalSum = cur

	var maxSuffix int64 = -(1 << 60)
	cur = 0
	for i := n - 1; i >= 0; i-- {
		cur += int64(arr[i])
		if cur > maxSuffix {
			maxSuffix = cur
		}
	}

	bestSingle := kadane(arr)
	if bestSingle < 0 {
		bestSingle = 0
	}
	if k == 1 {
		return int(bestSingle % MOD)
	}

	ans := maxPrefix + maxSuffix
	if totalSum > 0 {
		ans += int64(k-2) * totalSum
	}
	if ans < bestSingle {
		ans = bestSingle
	}
	if ans < 0 {
		ans = 0
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
def k_concatenation_max_sum(arr, k)
  mod = 1_000_000_007
  total = arr.sum

  # Kadane's algorithm allowing empty subarray
  max_sub = 0
  cur = 0
  arr.each do |x|
    cur = [cur + x, 0].max
    max_sub = [max_sub, cur].max
  end

  return max_sub % mod if k == 1

  # Maximum prefix sum (allow empty)
  pref_max = 0
  cur = 0
  arr.each do |x|
    cur += x
    pref_max = [pref_max, cur].max
  end

  # Maximum suffix sum (allow empty)
  suff_max = 0
  cur = 0
  arr.reverse_each do |x|
    cur += x
    suff_max = [suff_max, cur].max
  end

  if total > 0
    candidate = pref_max + suff_max + (k - 2) * total
    ans = [max_sub, candidate].max
  else
    candidate = pref_max + suff_max
    ans = [max_sub, candidate].max
  end

  ans % mod
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L
    def kConcatenationMaxSum(arr: Array[Int], k: Int): Int = {
        // Kadane for single array
        var maxEnding = 0L
        var maxSoFar = Long.MinValue
        for (x <- arr) {
            maxEnding = Math.max(x.toLong, maxEnding + x)
            maxSoFar = Math.max(maxSoFar, maxEnding)
        }
        val ansSingle = Math.max(0L, maxSoFar)

        if (k == 1) return ((ansSingle % MOD).toInt)

        // total sum
        var totalSum = 0L
        for (x <- arr) totalSum += x

        // max prefix sum
        var cur = 0L
        var maxPrefix = Long.MinValue
        for (x <- arr) {
            cur += x
            if (cur > maxPrefix) maxPrefix = cur
        }

        // max suffix sum
        cur = 0L
        var maxSuffix = Long.MinValue
        for (i <- (arr.length - 1) to 0 by -1) {
            cur += arr(i)
            if (cur > maxSuffix) maxSuffix = cur
        }

        var answer = ansSingle
        if (totalSum > 0) {
            val candidate = maxPrefix + maxSuffix + (k - 2).toLong * totalSum
            answer = Math.max(answer, candidate)
        } else {
            val candidate = maxPrefix + maxSuffix
            answer = Math.max(answer, candidate)
        }

        answer = Math.max(answer, 0L)
        ((answer % MOD).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_concatenation_max_sum(arr: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut total: i64 = 0;
        for &v in &arr {
            total += v as i64;
        }

        // Kadane's algorithm allowing empty subarray
        let mut cur_max: i64 = 0;
        let mut best_one: i64 = 0;
        for &v in &arr {
            cur_max = (cur_max + v as i64).max(0);
            if cur_max > best_one {
                best_one = cur_max;
            }
        }

        if k == 1 {
            return (best_one % MOD) as i32;
        }

        // max prefix sum
        let mut cur: i64 = 0;
        let mut max_prefix: i64 = std::i64::MIN;
        for &v in &arr {
            cur += v as i64;
            if cur > max_prefix {
                max_prefix = cur;
            }
        }

        // max suffix sum
        cur = 0;
        let mut max_suffix: i64 = std::i64::MIN;
        for &v in arr.iter().rev() {
            cur += v as i64;
            if cur > max_suffix {
                max_suffix = cur;
            }
        }

        let k_i64 = k as i64;
        let candidate = if total > 0 {
            max_prefix + max_suffix + (k_i64 - 2) * total
        } else {
            max_prefix + max_suffix
        };

        let ans = std::cmp::max(best_one, candidate);
        ((ans % MOD + MOD) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (k-concatenation-max-sum arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((total (foldl + 0 arr))
         ;; Kadane's algorithm allowing empty subarray
         (kadane
           (let ((cur 0) (best 0))
             (for ([x arr])
               (set! cur (+ cur x))
               (when (> cur best) (set! best cur))
               (when (< cur 0) (set! cur 0)))
             best))
         ;; maximum prefix sum (non‑empty)
         (prefix-max
           (let ((cur 0) (best (car arr)))
             (for ([x arr])
               (set! cur (+ cur x))
               (when (> cur best) (set! best cur)))
             best))
         ;; maximum suffix sum (non‑empty)
         (suffix-max
           (let ((cur 0) (rev (reverse arr)) (best (car rev)))
             (for ([x rev])
               (set! cur (+ cur x))
               (when (> cur best) (set! best cur)))
             best))
         (answer
           (if (= k 1)
               kadane
               (let ((candidate2
                       (if (> total 0)
                           (+ prefix-max suffix-max (* (- k 2) total))
                           (+ prefix-max suffix-max))))
                 (max kadane candidate2)))))
    (modulo answer MOD)))
```

## Erlang

```erlang
-module(solution).
-export([k_concatenation_max_sum/2]).

-define(MOD, 1000000007).

k_concatenation_max_sum(Arr, K) ->
    TotalSum = lists:sum(Arr),
    MaxSubarrayOne = max_subarray(Arr),
    MaxPrefix = prefix_max(Arr),
    MaxSuffix = suffix_max(Arr),

    Ans0 = case K of
        1 -> MaxSubarrayOne;
        _ ->
            if TotalSum > 0 ->
                    Temp = MaxPrefix + MaxSuffix + (K - 2) * TotalSum,
                    max(MaxSubarrayOne, Temp);
               true ->
                    Temp = MaxPrefix + MaxSuffix,
                    max(MaxSubarrayOne, Temp)
            end
    end,

    Ans0 rem ?MOD.

max_subarray(List) ->
    {_, Max} = lists:foldl(
        fun(X, {Cur, Best}) ->
                NewCur = max(Cur + X, 0),
                {NewCur, max(Best, NewCur)}
        end,
        {0, 0},
        List),
    Max.

prefix_max(List) ->
    {_, Max} = lists:foldl(
        fun(X, {Cur, Best}) ->
                NewCur = Cur + X,
                {NewCur, max(Best, NewCur)}
        end,
        {0, 0},
        List),
    Max.

suffix_max(List) ->
    Rev = lists:reverse(List),
    prefix_max(Rev).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec k_concatenation_max_sum(arr :: [integer], k :: integer) :: integer
  def k_concatenation_max_sum(arr, k) do
    total = Enum.sum(arr)
    max_one = max_subarray(arr)

    if k == 1 do
      rem(max_one, @mod)
    else
      pref = prefix_max(arr)
      suff = suffix_max(arr)

      candidate =
        if total > 0 do
          pref + suff + (k - 2) * total
        else
          pref + suff
        end

      ans = max(max_one, candidate)
      rem(ans, @mod)
    end
  end

  defp max_subarray(arr) do
    {_cur, best} =
      Enum.reduce(arr, {0, 0}, fn x, {cur, best} ->
        cur = max(0, cur + x)
        best = max(best, cur)
        {cur, best}
      end)

    best
  end

  defp prefix_max(arr) do
    {_sum, pref} =
      Enum.reduce(arr, {0, 0}, fn x, {s, p} ->
        s = s + x
        p = max(p, s)
        {s, p}
      end)

    pref
  end

  defp suffix_max(arr) do
    {_sum, suff} =
      Enum.reduce(Enum.reverse(arr), {0, 0}, fn x, {s, suf} ->
        s = s + x
        suf = max(suf, s)
        {s, suf}
      end)

    suff
  end
end
```
