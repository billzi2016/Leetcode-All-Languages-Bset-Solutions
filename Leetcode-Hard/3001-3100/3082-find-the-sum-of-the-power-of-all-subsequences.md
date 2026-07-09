# 3082. Find the Sum of the Power of All Subsequences

## Cpp

```cpp
class Solution {
public:
    int sumOfPower(vector<int>& nums, int k) {
        const int MOD = 1'000'000'007;
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        dp[0][0] = 1;
        for (int x : nums) {
            if (x > k) continue; // cannot contribute to sum k
            for (int len = n - 1; len >= 0; --len) {
                for (int s = k - x; s >= 0; --s) {
                    int cur = dp[len][s];
                    if (!cur) continue;
                    int &dest = dp[len + 1][s + x];
                    dest += cur;
                    if (dest >= MOD) dest -= MOD;
                }
            }
        }
        vector<int> pow2(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (pow2[i - 1] * 2LL) % MOD;
        }
        long long ans = 0;
        for (int len = 1; len <= n; ++len) {
            ans += (long long)dp[len][k] * pow2[n - len];
            if (ans >= (1LL << 62)) ans %= MOD; // avoid overflow
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int sumOfPower(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[k + 1][n + 1];
        dp[0][0] = 1; // empty subsequence
        
        for (int num : nums) {
            if (num > k) continue;
            for (int s = k; s >= num; --s) {
                for (int len = n; len >= 1; --len) {
                    dp[s][len] = (dp[s][len] + dp[s - num][len - 1]) % MOD;
                }
            }
        }
        
        int[] pow2 = new int[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (int)((pow2[i - 1] * 2L) % MOD);
        }
        
        long ans = 0;
        for (int len = 1; len <= n; ++len) {
            if (dp[k][len] != 0) {
                ans = (ans + dp[k][len] * 1L * pow2[n - len]) % MOD;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfPower(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # dp[sum][len] = number of subsequences with given sum and length
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for num in nums:
            if num > k:
                continue
            for s in range(k, num - 1, -1):
                prev = dp[s - num]
                cur = dp[s]
                # iterate lengths descending to avoid reuse within same iteration
                for l in range(n - 1, -1, -1):
                    if prev[l]:
                        cur[l + 1] = (cur[l + 1] + prev[l]) % MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        ans = 0
        for length in range(n + 1):
            cnt = dp[k][length]
            if cnt:
                ans = (ans + cnt * pow2[n - length]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # precompute powers of two
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # dp[sum][len] = number of subsequences with given sum and length
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1  # empty subsequence

        for x in nums:
            # update in reverse to avoid reuse within same iteration
            for s in range(k, x - 1, -1):
                prev = dp[s - x]
                cur = dp[s]
                for l in range(n - 1, -1, -1):
                    if prev[l]:
                        cur[l + 1] = (cur[l + 1] + prev[l]) % MOD

        ans = 0
        for length in range(1, n + 1):
            cnt = dp[k][length]
            if cnt:
                ans = (ans + cnt * pow2[n - length]) % MOD
        return ans
```

## C

```c
#include <string.h>

int sumOfPower(int* nums, int numsSize, int k) {
    const int MOD = 1000000007;
    static long long dp[101][101];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    for (int i = 0; i < numsSize; ++i) {
        int a = nums[i];
        if (a > k) continue;
        for (int sum = k; sum >= a; --sum) {
            for (int sz = numsSize; sz >= 1; --sz) {
                dp[sum][sz] = (dp[sum][sz] + dp[sum - a][sz - 1]) % MOD;
            }
        }
    }

    long long pow2[101];
    pow2[0] = 1;
    for (int i = 1; i <= numsSize; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    long long ans = 0;
    for (int sz = 0; sz <= numsSize; ++sz) {
        if (dp[k][sz]) {
            ans = (ans + dp[k][sz] * pow2[numsSize - sz]) % MOD;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfPower(int[] nums, int k) {
        const int MOD = 1000000007;
        int n = nums.Length;
        long[,] dp = new long[k + 1, n + 1];
        dp[0, 0] = 1;
        foreach (int x in nums) {
            for (int sum = k; sum >= x; --sum) {
                for (int len = n - 1; len >= 0; --len) {
                    long prev = dp[sum - x, len];
                    if (prev != 0) {
                        dp[sum, len + 1] = (dp[sum, len + 1] + prev) % MOD;
                    }
                }
            }
        }
        long[] pow2 = new long[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long ans = 0;
        for (int len = 1; len <= n; ++len) {
            long cnt = dp[k, len];
            if (cnt != 0) {
                ans = (ans + cnt * pow2[n - len]) % MOD;
            }
        }
        return (int)ans;
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
var sumOfPower = function(nums, k) {
    const MOD = 1000000007;
    const n = nums.length;
    // precompute powers of 2 modulo MOD
    const pow2 = new Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    // dp[s][len] = number of subsequences with sum s and length len
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(0));
    dp[0][0] = 1;
    for (let idx = 0; idx < n; ++idx) {
        const val = nums[idx];
        if (val > k) continue; // cannot contribute to sum k
        for (let s = k - val; s >= 0; --s) {
            for (let len = idx; len >= 0; --len) {
                const cur = dp[s][len];
                if (cur !== 0) {
                    const ns = s + val;
                    const nl = len + 1;
                    dp[ns][nl] = (dp[ns][nl] + cur) % MOD;
                }
            }
        }
    }
    let ans = 0;
    for (let len = 1; len <= n; ++len) {
        const cnt = dp[k][len];
        if (cnt !== 0) {
            ans = (ans + cnt * pow2[n - len]) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function sumOfPower(nums: number[], k: number): number {
    const MOD = 1000000007;
    const n = nums.length;

    // precompute powers of two modulo MOD
    const pow2: number[] = new Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    // dp[s][len] = number of subsequences with sum s and length len
    const dp: number[][] = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(0));
    dp[0][0] = 1;

    for (const num of nums) {
        if (num > k) continue; // cannot contribute to sum k
        for (let s = k; s >= num; s--) {
            const prev = dp[s - num];
            const cur = dp[s];
            for (let len = n; len >= 1; len--) {
                const add = prev[len - 1];
                if (add !== 0) {
                    cur[len] = (cur[len] + add) % MOD;
                }
            }
        }
    }

    let ans = 0;
    const modBig = BigInt(MOD);
    for (let len = 1; len <= n; len++) {
        const cnt = dp[k][len];
        if (cnt === 0) continue;
        const add = Number((BigInt(cnt) * BigInt(pow2[n - len])) % modBig);
        ans += add;
        if (ans >= MOD) ans -= MOD;
    }

    return ans;
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
    function sumOfPower($nums, $k) {
        $mod = 1000000007;
        $n = count($nums);
        // dp[sum][size] = number of subsets with given sum and size
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, 0));
        $dp[0][0] = 1;

        foreach ($nums as $num) {
            for ($s = $k; $s >= $num; --$s) {
                for ($j = $n; $j >= 1; --$j) {
                    $dp[$s][$j] = ($dp[$s][$j] + $dp[$s - $num][$j - 1]) % $mod;
                }
            }
        }

        // precompute powers of two
        $pow2 = array_fill(0, $n + 1, 0);
        $pow2[0] = 1;
        for ($i = 1; $i <= $n; ++$i) {
            $pow2[$i] = ($pow2[$i - 1] * 2) % $mod;
        }

        $ans = 0;
        for ($j = 0; $j <= $n; ++$j) {
            $cnt = $dp[$k][$j];
            if ($cnt == 0) continue;
            $add = ($cnt * $pow2[$n - $j]) % $mod;
            $ans = ($ans + $add) % $mod;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfPower(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        // precompute powers of two
        var pow2 = [Int](repeating: 0, count: n + 1)
        pow2[0] = 1
        if n > 0 {
            for i in 1...n {
                pow2[i] = Int((Int64(pow2[i - 1]) * 2) % Int64(MOD))
            }
        }
        // dp[sum][len] = number of subsequences with given sum and length
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: k + 1)
        dp[0][0] = 1
        for num in nums {
            if num > k { continue }
            for s in stride(from: k, through: num, by: -1) {
                for len in stride(from: n, through: 1, by: -1) {
                    let add = dp[s - num][len - 1]
                    if add != 0 {
                        var value = dp[s][len] + add
                        if value >= MOD { value -= MOD }
                        dp[s][len] = value
                    }
                }
            }
        }
        var ans = 0
        for len in 1...n {
            let cnt = dp[k][len]
            if cnt == 0 { continue }
            let contrib = Int((Int64(cnt) * Int64(pow2[n - len])) % Int64(MOD))
            ans += contrib
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfPower(nums: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L
        val n = nums.size
        val dp = Array(k + 1) { LongArray(n + 1) }
        dp[0][0] = 1L

        for (num in nums) {
            if (num > k) continue
            for (s in k downTo num) {
                val prev = s - num
                for (len in n downTo 1) {
                    dp[s][len] = (dp[s][len] + dp[prev][len - 1]) % MOD
                }
            }
        }

        val pow2 = LongArray(n + 1)
        pow2[0] = 1L
        for (i in 1..n) {
            pow2[i] = (pow2[i - 1] * 2L) % MOD
        }

        var ans = 0L
        for (len in 0..n) {
            val cnt = dp[k][len]
            if (cnt != 0L) {
                ans = (ans + cnt * pow2[n - len]) % MOD
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumOfPower(List<int> nums, int k) {
    const int MOD = 1000000007;
    int n = nums.length;
    // dp[sum][len] = number of subsequences with given sum and length
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n + 1, 0));
    dp[0][0] = 1;

    for (int num in nums) {
      for (int s = k; s >= num; --s) {
        for (int len = n; len >= 1; --len) {
          int prev = dp[s - num][len - 1];
          if (prev != 0) {
            dp[s][len] = (dp[s][len] + prev) % MOD;
          }
        }
      }
    }

    // precompute powers of two
    List<int> pow2 = List.filled(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    int ans = 0;
    for (int len = 1; len <= n; ++len) {
      int cnt = dp[k][len];
      if (cnt != 0) {
        ans = (ans + cnt * pow2[n - len]) % MOD;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func sumOfPower(nums []int, k int) int {
	const MOD int64 = 1000000007
	n := len(nums)

	// precompute powers of two modulo MOD
	pow2 := make([]int64, n+1)
	pow2[0] = 1
	for i := 1; i <= n; i++ {
		pow2[i] = (pow2[i-1] * 2) % MOD
	}

	// dp[sum][len] = number of subsequences with given sum and length
	dp := make([][]int64, k+1)
	for s := 0; s <= k; s++ {
		dp[s] = make([]int64, n+1)
	}
	dp[0][0] = 1

	for _, num := range nums {
		if num > k {
			continue
		}
		for s := k; s >= num; s-- {
			for l := n; l >= 1; l-- {
				if dp[s-num][l-1] != 0 {
					dp[s][l] = (dp[s][l] + dp[s-num][l-1]) % MOD
				}
			}
		}
	}

	ans := int64(0)
	for l := 1; l <= n; l++ {
		if cnt := dp[k][l]; cnt != 0 {
			ans = (ans + cnt*pow2[n-l]) % MOD
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def sum_of_power(nums, k)
  n = nums.length
  pow2 = Array.new(n + 1, 1)
  (1..n).each { |i| pow2[i] = (pow2[i - 1] * 2) % MOD }

  dp = Array.new(k + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1

  nums.each do |x|
    next if x > k
    k.downto(x) do |s|
      n.downto(1) do |len|
        val = dp[s - x][len - 1]
        next if val.zero?
        dp[s][len] = (dp[s][len] + val) % MOD
      end
    end
  end

  ans = 0
  (0..n).each do |len|
    cnt = dp[k][len]
    next if cnt.zero?
    ans = (ans + cnt * pow2[n - len]) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
    def sumOfPower(nums: Array[Int], k: Int): Int = {
        val MOD = 1000000007L
        val n = nums.length
        // dp[sum][size] = number of subsets with given sum and size
        val dp = Array.ofDim[Long](k + 1, n + 1)
        dp(0)(0) = 1L

        for (num <- nums) {
            if (num <= k) {
                for (s <- k to num by -1) {
                    val prev = s - num
                    for (sz <- n - 1 to 0 by -1) {
                        val cnt = dp(prev)(sz)
                        if (cnt != 0L) {
                            dp(s)(sz + 1) = (dp(s)(sz + 1) + cnt) % MOD
                        }
                    }
                }
            }
        }

        // precompute powers of two
        val pow2 = Array.ofDim[Long](n + 1)
        pow2(0) = 1L
        for (i <- 1 to n) {
            pow2(i) = (pow2(i - 1) * 2) % MOD
        }

        var ans = 0L
        for (sz <- 1 to n) {
            val cnt = dp(k)(sz)
            if (cnt != 0L) {
                ans = (ans + cnt * pow2(n - sz)) % MOD
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_power(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let k_usize = k as usize;

        // dp[sum][len] = number of subsequences with given sum and length
        let mut dp = vec![vec![0i64; n + 1]; k_usize + 1];
        dp[0][0] = 1;

        for &val_i32 in nums.iter() {
            let val = val_i32 as usize;
            if val > k_usize {
                continue;
            }
            for s in (val..=k_usize).rev() {
                for len in (1..=n).rev() {
                    let add = dp[s - val][len - 1];
                    if add != 0 {
                        dp[s][len] = (dp[s][len] + add) % MOD;
                    }
                }
            }
        }

        // precompute powers of two
        let mut pow2 = vec![0i64; n + 1];
        pow2[0] = 1;
        for i in 1..=n {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }

        let mut ans: i64 = 0;
        for len in 1..=n {
            let cnt = dp[k_usize][len];
            if cnt != 0 {
                ans = (ans + cnt * pow2[n - len] % MOD) % MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (sum-of-power nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (dp (make-vector (+ k 1) (lambda () (make-vector (+ n 1) 0)))))
    ;; base case: empty subset has sum 0 and size 0
    (vector-set! (vector-ref dp 0) 0 1)
    ;; process each number
    (for ([num nums])
      (when (<= num k)
        (for ([s (in-range k (- num) -1)]) ; descending sums
          (let ((prev (- s num)))
            (for ([size (in-range n 0 -1)]) ; descending sizes (n .. 1)
              (define add (vector-ref (vector-ref dp prev) (- size 1)))
              (when (not (= add 0))
                (define cur (vector-ref (vector-ref dp s) size))
                (vector-set! (vector-ref dp s) size
                             (modulo (+ cur add) MOD))))))))
    ;; precompute powers of two modulo MOD
    (let ((pow2 (make-vector (+ n 1) 0)))
      (vector-set! pow2 0 1)
      (for ([i (in-range 1 (+ n 1))])
        (vector-set! pow2 i (modulo (* 2 (vector-ref pow2 (- i 1))) MOD)))
      ;; accumulate answer
      (let loop ((j 0) (acc 0))
        (if (> j n)
            acc
            (let* ((cnt (vector-ref (vector-ref dp k) j))
                   (add (modulo (* cnt (vector-ref pow2 (- n j))) MOD)))
              (loop (+ j 1) (modulo (+ acc add) MOD))))))))
```

## Erlang

```erlang
-spec sum_of_power(Nums :: [integer()], K :: integer()) -> integer().
sum_of_power(Nums, K) ->
    Mod = 1000000007,
    N = length(Nums),
    DP0 = #{ {0,0} => 1 },
    DP = lists:foldl(
        fun(X, DPAcc) ->
            maps:fold(
                fun({Sum, Len}, Cnt, Acc) ->
                    NewSum = Sum + X,
                    if NewSum =< K ->
                        Key2 = {NewSum, Len+1},
                        maps:update_with(
                            Key2,
                            fun(Old) -> (Old + Cnt) rem Mod end,
                            Cnt rem Mod,
                            Acc);
                       true -> Acc
                    end
                end,
                DPAcc,
                DPAcc)
        end,
        DP0,
        Nums),
    lists:foldl(
        fun(Len, Ans) ->
            Count = maps:get({K, Len}, DP, 0),
            if Count =:= 0 -> Ans;
               true ->
                   Pow = fast_pow(2, N - Len, Mod),
                   (Ans + (Count * Pow) rem Mod) rem Mod
            end
        end,
        0,
        lists:seq(1, N)).

fast_pow(_Base, 0, _Mod) -> 1;
fast_pow(Base, Exp, Mod) ->
    Half = fast_pow(Base, Exp div 2, Mod),
    Res = (Half * Half) rem Mod,
    case Exp band 1 of
        1 -> (Res * Base) rem Mod;
        0 -> Res
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec sum_of_power(nums :: [integer], k :: integer) :: integer
  def sum_of_power(nums, k) do
    mod = 1_000_000_007
    n = length(nums)

    # dp maps {length, sum} -> count of subsequences
    dp_initial = %{{0, 0} => 1}

    dp =
      Enum.reduce(nums, dp_initial, fn a, dp_acc ->
        if a > k do
          dp_acc
        else
          updates =
            Enum.reduce(dp_acc, %{}, fn {{len, sum}, cnt}, upd ->
              ns = sum + a
              nl = len + 1

              if ns <= k do
                key = {nl, ns}
                Map.update(upd, key, cnt, fn existing -> rem(existing + cnt, mod) end)
              else
                upd
              end
            end)

          Map.merge(dp_acc, updates, fn _k, v1, v2 -> rem(v1 + v2, mod) end)
        end
      end)

    # precompute powers of 2 modulo mod: pow2[i] = 2^i % mod
    pow2 =
      Enum.reduce(0..n, [], fn i, acc ->
        val =
          if i == 0 do
            1
          else
            rem(List.last(acc) * 2, mod)
          end

        acc ++ [val]
      end)

    ans =
      dp
      |> Enum.reduce(0, fn {{len, sum}, cnt}, acc ->
        if sum == k do
          add = rem(cnt * Enum.at(pow2, n - len), mod)
          rem(acc + add, mod)
        else
          acc
        end
      end)

    ans
  end
end
```
