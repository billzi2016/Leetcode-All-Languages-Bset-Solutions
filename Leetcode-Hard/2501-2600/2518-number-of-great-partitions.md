# 2518. Number of Great Partitions

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1'000'000'007;
    
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int countPartitions(vector<int>& nums, int k) {
        long long totalSum = 0;
        for (int x : nums) totalSum += x;
        if (totalSum < 2LL * k) return 0;
        
        vector<int> dp(k, 0);
        dp[0] = 1;
        for (int x : nums) {
            // only consider contributions that keep sum < k
            for (int s = k - 1; s >= 0; --s) {
                if (dp[s] == 0) continue;
                long long ns = (long long)s + x;
                if (ns < k) {
                    dp[ns] += dp[s];
                    if (dp[ns] >= MOD) dp[ns] -= MOD;
                }
            }
        }
        long long cnt = 0;
        for (int s = 0; s < k; ++s) {
            cnt += dp[s];
            if (cnt >= MOD) cnt -= MOD;
        }
        
        long long totalWays = modPow(2, nums.size());
        long long ans = (totalWays - (2LL * cnt) % MOD + MOD) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int countPartitions(int[] nums, int k) {
        long totalSum = 0L;
        for (int v : nums) totalSum += v;
        if (totalSum < 2L * k) return 0;
        
        int n = nums.length;
        // dp[s] = number of subsets with sum exactly s (s < k)
        int[] dp = new int[k];
        dp[0] = 1;
        for (int v : nums) {
            if (v >= k) continue; // cannot be part of a subset with sum < k
            for (int s = k - 1; s >= v; --s) {
                dp[s] += dp[s - v];
                if (dp[s] >= MOD) dp[s] -= MOD;
            }
        }
        long cntLessK = 0;
        for (int s = 0; s < k; ++s) {
            cntLessK += dp[s];
        }
        cntLessK %= MOD;
        
        long totalWays = modPow(2, n);
        long ans = (totalWays - (2L * cntLessK) % MOD + MOD) % MOD;
        return (int) ans;
    }
    
    private long modPow(long base, int exp) {
        long res = 1;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total_sum = sum(nums)
        n = len(nums)
        if total_sum < 2 * k:
            return 0

        # dp[s] = number of subsets with sum exactly s (s < k)
        dp = [0] * k
        dp[0] = 1
        for x in nums:
            if x >= k:
                continue
            for s in range(k - 1 - x, -1, -1):
                if dp[s]:
                    dp[s + x] = (dp[s + x] + dp[s]) % MOD

        cnt = sum(dp) % MOD  # subsets with sum < k
        total = pow(2, n, MOD)
        ans = (total - 2 * cnt) % MOD
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        total_sum = sum(nums)
        n = len(nums)
        if total_sum < 2 * k:
            return 0

        dp = [0] * k  # dp[s] = number of subsets with exact sum s (s < k)
        dp[0] = 1
        for num in nums:
            if num >= k:
                continue
            limit = k - 1 - num
            for s in range(limit, -1, -1):
                if dp[s]:
                    dp[s + num] = (dp[s + num] + dp[s]) % MOD

        low = sum(dp) % MOD  # subsets with sum < k
        total_subsets = pow(2, n, MOD)
        ans = (total_subsets - 2 * low) % MOD
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

int countPartitions(int* nums, int numsSize, int k) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];
    if (total < 2LL * k) return 0;

    int *dp = (int *)calloc(k, sizeof(int));
    dp[0] = 1;

    for (int i = 0; i < numsSize; ++i) {
        long long val = nums[i];
        if (val >= k) continue; // adding it will always exceed k-1
        for (int s = k - 1; s >= 0; --s) {
            if (dp[s]) {
                int ns = s + (int)val;
                if (ns < k) {
                    dp[ns] += dp[s];
                    if (dp[ns] >= MOD) dp[ns] -= MOD;
                }
            }
        }
    }

    long long less = 0;
    for (int s = 0; s < k; ++s) {
        less += dp[s];
        if (less >= MOD) less -= MOD;
    }
    free(dp);

    long long pow2 = 1;
    for (int i = 0; i < numsSize; ++i) {
        pow2 <<= 1;
        if (pow2 >= MOD) pow2 %= MOD;
    }

    long long ans = (pow2 - (2LL * less) % MOD + MOD) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    
    public int CountPartitions(int[] nums, int k) {
        long totalSum = 0;
        foreach (int v in nums) totalSum += v;
        if (totalSum < 2L * k) return 0;

        int n = nums.Length;
        long totalWays = ModPow(2, n);
        
        // dp[s] = number of subsets with sum exactly s (s < k)
        long[] dp = new long[k];
        dp[0] = 1;
        foreach (int val in nums) {
            if (val >= k) continue; // adding this value will exceed k-1 for any existing sum
            for (int s = k - 1 - val; s >= 0; --s) {
                dp[s + val] += dp[s];
                if (dp[s + val] >= MOD) dp[s + val] -= MOD;
            }
        }

        long lessThanK = 0;
        for (int i = 0; i < k; ++i) {
            lessThanK += dp[i];
            if (lessThanK >= MOD) lessThanK -= MOD;
        }

        long bad = (2L * lessThanK) % MOD;
        long ans = totalWays - bad;
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
    
    private long ModPow(long baseVal, int exp) {
        long result = 1;
        long b = baseVal % MOD;
        int e = exp;
        while (e > 0) {
            if ((e & 1) == 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            e >>= 1;
        }
        return result;
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
var countPartitions = function(nums, k) {
    const MOD = 1000000007;
    const n = nums.length;
    let totalSum = 0;
    for (const v of nums) totalSum += v;
    if (totalSum < 2 * k) return 0;

    // dp[s] = number of subsets with sum exactly s (s < k)
    const dp = new Array(k).fill(0);
    dp[0] = 1;
    for (const num of nums) {
        if (num >= k) continue; // cannot contribute to sums < k
        for (let s = k - 1; s >= num; --s) {
            dp[s] = (dp[s] + dp[s - num]) % MOD;
        }
    }

    let cntLessK = 0;
    for (let s = 0; s < k; ++s) {
        cntLessK = (cntLessK + dp[s]) % MOD;
    }

    // fast modular exponentiation using BigInt
    const modPow = (base, exp) => {
        let result = 1n;
        let b = BigInt(base);
        let e = BigInt(exp);
        const MOD_BI = 1000000007n;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD_BI;
            b = (b * b) % MOD_BI;
            e >>= 1n;
        }
        return Number(result);
    };

    const totalSubsets = modPow(2, n);
    let ans = (totalSubsets - (2 * cntLessK) % MOD + MOD) % MOD;
    return ans;
};
```

## Typescript

```typescript
function countPartitions(nums: number[], k: number): number {
    const MOD_BIG = 1000000007n;
    const MOD_NUM = 1000000007;
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;
    if (total < 2 * k) return 0;

    // dp[s] = number of subsets with sum exactly s (s < k)
    const dp = new Array(k).fill(0);
    dp[0] = 1;
    for (const num of nums) {
        if (num >= k) continue; // cannot contribute to a sum < k
        for (let s = k - 1; s >= num; --s) {
            dp[s] = (dp[s] + dp[s - num]) % MOD_NUM;
        }
    }

    let cntLessK = 0;
    for (let s = 0; s < k; ++s) {
        cntLessK = (cntLessK + dp[s]) % MOD_NUM;
    }

    // compute 2^n mod MOD using bigint
    let pow2 = 1n;
    let base = 2n;
    let exp = BigInt(n);
    while (exp > 0n) {
        if (exp & 1n) pow2 = (pow2 * base) % MOD_BIG;
        base = (base * base) % MOD_BIG;
        exp >>= 1n;
    }

    const bad = (2n * BigInt(cntLessK)) % MOD_BIG;
    let ans = (pow2 - bad) % MOD_BIG;
    if (ans < 0) ans += MOD_BIG;
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countPartitions($nums, $k) {
        $mod = 1000000007;
        $n = count($nums);
        $sum = 0;
        foreach ($nums as $v) {
            $sum += $v;
        }
        if ($sum < 2 * $k) {
            return 0;
        }

        // total subsets = 2^n mod MOD
        $total = 1;
        for ($i = 0; $i < $n; $i++) {
            $total = ($total * 2) % $mod;
        }

        // dp[s] = number of subsets with sum exactly s (s < k)
        $dp = array_fill(0, $k, 0);
        $dp[0] = 1;

        foreach ($nums as $num) {
            if ($num >= $k) {
                continue; // cannot contribute to sums < k
            }
            $limit = $k - 1 - $num;
            for ($s = $limit; $s >= 0; $s--) {
                $ns = $s + $num;
                $dp[$ns] = ($dp[$ns] + $dp[$s]) % $mod;
            }
        }

        $bad = 0;
        foreach ($dp as $val) {
            $bad = ($bad + $val) % $mod;
        }

        // answer = total - 2 * bad (mod MOD)
        $ans = ($total - (2 * $bad) % $mod + $mod) % $mod;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var totalSum: Int64 = 0
        for v in nums { totalSum += Int64(v) }
        if totalSum < Int64(2 * k) {
            return 0
        }
        let n = nums.count
        var total = 1
        for _ in 0..<n {
            total = (total * 2) % MOD
        }
        var dp = [Int](repeating: 0, count: k)
        dp[0] = 1
        for v in nums where v < k {
            var s = k - 1
            while s >= v {
                let sum = dp[s] + dp[s - v]
                dp[s] = sum >= MOD ? sum - MOD : sum
                s -= 1
            }
        }
        var low = 0
        for cnt in dp {
            low += cnt
            if low >= MOD { low -= MOD }
        }
        var ans = total - (2 * low % MOD)
        ans %= MOD
        if ans < 0 { ans += MOD }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L
        var totalSum = 0L
        for (v in nums) totalSum += v.toLong()
        if (totalSum < 2L * k) return 0

        val dp = LongArray(k)
        dp[0] = 1L
        for (num in nums) {
            if (num >= k) continue
            val v = num
            for (s in k - 1 - v downTo 0) {
                dp[s + v] = (dp[s + v] + dp[s]) % MOD
            }
        }

        var cnt = 0L
        for (x in dp) {
            cnt += x
            if (cnt >= MOD) cnt -= MOD
        }

        val total = modPow(2L, nums.size.toLong(), MOD)
        var ans = (total - (2L * cnt % MOD) + MOD) % MOD
        return ans.toInt()
    }

    private fun modPow(base: Long, exp: Long, mod: Long): Long {
        var b = base % mod
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = (res * b) % mod
            }
            b = (b * b) % mod
            e = e shr 1
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countPartitions(List<int> nums, int k) {
    int n = nums.length;
    int totalSum = 0;
    for (var v in nums) totalSum += v;
    if (totalSum < 2 * k) return 0;

    // dp[s] = number of subsets with sum exactly s (s < k)
    List<int> dp = List.filled(k, 0);
    dp[0] = 1;
    for (int num in nums) {
      if (num >= k) continue; // cannot contribute to sums < k
      for (int s = k - 1 - num; s >= 0; --s) {
        int ns = s + num;
        dp[ns] += dp[s];
        if (dp[ns] >= _mod) dp[ns] -= _mod;
      }
    }

    int cntLessK = 0;
    for (int v in dp) {
      cntLessK += v;
      if (cntLessK >= _mod) cntLessK -= _mod;
    }

    int totalWays = _powMod(2, n);
    int ans = (totalWays - (2 * cntLessK) % _mod + _mod) % _mod;
    return ans;
  }

  int _powMod(int base, int exp) {
    long result = 1;
    long b = base.toLong();
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      e >>= 1;
    }
    return result.toInt();
  }
}

// Helper extensions for long arithmetic (since Dart int is arbitrary precision, we can use it directly)
extension on int {
  int toLong() => this;
}
```

## Golang

```go
func countPartitions(nums []int, k int) int {
	const MOD int64 = 1_000_000_007
	n := len(nums)
	total := 0
	for _, v := range nums {
		total += v
	}
	if total < 2*k {
		return 0
	}

	dp := make([]int64, k) // sums 0..k-1
	dp[0] = 1
	for _, v := range nums {
		if v >= k {
			continue
		}
		val := v
		for s := k - 1 - val; s >= 0; s-- {
			dp[s+val] = (dp[s+val] + dp[s]) % MOD
		}
	}

	var cntLessK int64
	for s := 0; s < k; s++ {
		cntLessK = (cntLessK + dp[s]) % MOD
	}

	// compute 2^n mod MOD
	pow2 := int64(1)
	base := int64(2)
	exp := n
	for exp > 0 {
		if exp&1 == 1 {
			pow2 = (pow2 * base) % MOD
		}
		base = (base * base) % MOD
		exp >>= 1
	}

	ans := (pow2 - (2*cntLessK)%MOD + MOD) % MOD
	return int(ans)
}
```

## Ruby

```ruby
def count_partitions(nums, k)
  mod = 1_000_000_007
  total_sum = nums.sum
  return 0 if total_sum < 2 * k

  dp = Array.new(k, 0)
  dp[0] = 1
  nums.each do |num|
    (k - 1).downto(0) do |s|
      next if dp[s].zero?
      ns = s + num
      dp[ns] = (dp[ns] + dp[s]) % mod if ns < k
    end
  end

  small = dp.sum % mod
  total_subsets = 1
  nums.size.times { total_subsets = (total_subsets * 2) % mod }

  (total_subsets - (2 * small) % mod) % mod
end
```

## Scala

```scala
object Solution {
    def countPartitions(nums: Array[Int], k: Int): Int = {
        val MOD = 1000000007L
        val totalSum = nums.foldLeft(0L)(_ + _)
        if (totalSum < 2L * k) return 0

        val dp = new Array[Long](k)
        dp(0) = 1L
        for (num <- nums) {
            val v = num.toLong
            var s = k - 1
            while (s >= 0) {
                if (dp(s) != 0 && s + v < k) {
                    val ns = (s + v).toInt
                    dp(ns) = (dp(ns) + dp(s)) % MOD
                }
                s -= 1
            }
        }

        var bad = 0L
        var i = 0
        while (i < k) {
            bad = (bad + dp(i)) % MOD
            i += 1
        }

        // total subsets = 2^n mod MOD
        var total = 1L
        var base = 2L
        var exp = nums.length
        var e = exp
        while (e > 0) {
            if ((e & 1) == 1) total = (total * base) % MOD
            base = (base * base) % MOD
            e >>= 1
        }

        val ans = (total - (2L * bad % MOD) + MOD) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let total_sum: i64 = nums.iter().map(|&x| x as i64).sum();
        if total_sum < 2 * k as i64 {
            return 0;
        }
        let k_usize = k as usize;
        // dp[s] = number of subsets with sum exactly s (s < k)
        let mut dp = vec![0i64; k_usize];
        dp[0] = 1;
        for &val in &nums {
            if val as i32 >= k {
                continue;
            }
            let v = val as usize;
            for s in (v..k_usize).rev() {
                dp[s] = (dp[s] + dp[s - v]) % MOD;
            }
        }
        let mut cnt: i64 = 0;
        for &x in &dp {
            cnt += x;
            if cnt >= MOD { cnt -= MOD; }
        }
        // total subsets = 2^n
        let mut total: i64 = 1;
        let mut base: i64 = 2;
        let mut exp = n;
        while exp > 0 {
            if exp & 1 == 1 {
                total = total * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        let ans = (total - (2 * cnt % MOD) + MOD) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (let* ((res (if (odd? e) (modulo (* res b) MOD) res))
               (b (modulo (* b b) MOD)))
          (loop b (quotient e 2) res)))))

(define/contract (count-partitions nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (total-sum (apply + nums)))
    (if (< total-sum (* 2 k))
        0
        (let* ((dp (make-vector k 0))
               (_ (vector-set! dp 0 1))
               (process
                (lambda (x)
                  (when (< x k)
                    (for ([s (in-range (sub1 k) -1 -1)])
                      (let ((val (vector-ref dp s)))
                        (when (> val 0)
                          (define ns (+ s x))
                          (when (< ns k)
                            (vector-set! dp ns
                                         (modulo (+ (vector-ref dp ns) val) MOD)))))))))
               (_ (for-each process nums))
               (cnt (let loop ((i 0) (acc 0))
                      (if (= i k)
                          acc
                          (loop (+ i 1) (modulo (+ acc (vector-ref dp i)) MOD)))))
               (total (pow-mod 2 n))
               (ans (modulo (- total (modulo (* 2 cnt) MOD)) MOD)))
          ans))))
```

## Erlang

```erlang
-module(solution).
-export([count_partitions/2]).

-define(MOD, 1000000007).

count_partitions(Nums, K) ->
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    if
        Sum < 2 * K -> 0;
        true ->
            Total = powmod(2, length(Nums), ?MOD),
            CntLessK = cnt_less_k(Nums, K),
            Bad = (2 * CntLessK) rem ?MOD,
            ((Total - Bad + ?MOD) rem ?MOD)
    end.

cnt_less_k(Nums, K) ->
    InitMap = #{0 => 1},
    Map = lists:foldl(fun(X, M) -> update_map(M, X, K) end, InitMap, Nums),
    maps:fold(fun(_Key, Val, Acc) -> (Acc + Val) rem ?MOD end, 0, Map).

update_map(Map, X, K) ->
    maps:fold(
        fun(Sum, Cnt, Acc) ->
            NewSum = Sum + X,
            if
                NewSum < K ->
                    Old = maps:get(NewSum, Acc, 0),
                    maps:put(NewSum, (Old + Cnt) rem ?MOD, Acc);
                true -> Acc
            end
        end,
        Map,
        Map).

powmod(Base, Exp, Mod) ->
    powmod(Base rem Mod, Exp, Mod, 1).

powmod(_Base, 0, _Mod, Acc) ->
    Acc;
powmod(Base, Exp, Mod, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem Mod,
    powmod((Base * Base) rem Mod, Exp bsr 1, Mod, NewAcc);
powmod(Base, Exp, Mod, Acc) ->
    powmod((Base * Base) rem Mod, Exp bsr 1, Mod, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec count_partitions(nums :: [integer], k :: integer) :: integer
  def count_partitions(nums, k) do
    total_sum = Enum.sum(nums)

    if total_sum < 2 * k do
      0
    else
      n = length(nums)
      total_subsets = pow_mod(2, n, @mod)

      # dp array for sums < k
      dp = :array.new(k, default: 0) |> :array.set(0, 1)

      dp =
        Enum.reduce(nums, dp, fn v, acc_dp ->
          if v < k do
            max_s = k - 1 - v

            seq = :lists.seq(max_s, 0, -1)

            Enum.reduce(seq, acc_dp, fn s, cur_dp ->
              cnt = :array.get(s, cur_dp)

              if cnt != 0 do
                new_val = (:array.get(s + v, cur_dp) + cnt) |> rem(@mod)
                :array.set(s + v, new_val, cur_dp)
              else
                cur_dp
              end
            end)
          else
            acc_dp
          end
        end)

      f =
        Enum.reduce(0..(k - 1), 0, fn i, sum ->
          (sum + :array.get(i, dp)) |> rem(@mod)
        end)

      bad = (2 * f) |> rem(@mod)
      ans = total_subsets - bad
      ans = if ans < 0, do: ans + @mod, else: ans
      ans
    end
  end

  defp pow_mod(_base, 0, _mod), do: 1

  defp pow_mod(base, exp, mod) when exp > 0 do
    rec_pow(base, exp, 1, mod)
  end

  defp rec_pow(_base, 0, acc, _mod), do: acc

  defp rec_pow(base, exp, acc, mod) do
    acc = if Bitwise.band(exp, 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    rec_pow(base, div(exp, 2), acc, mod)
  end
end
```
