# 2741. Special Permutations

## Cpp

```cpp
class Solution {
public:
    int specialPerm(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int n = nums.size();
        vector<vector<char>> ok(n, vector<char>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) if (i != j) {
                if (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0)
                    ok[i][j] = 1;
            }
        }
        int fullMask = (1 << n) - 1;
        vector<vector<int>> dp(1 << n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[1 << i][i] = 1;
        }
        for (int mask = 1; mask <= fullMask; ++mask) {
            for (int last = 0; last < n; ++last) if (dp[mask][last]) {
                int cur = dp[mask][last];
                for (int nxt = 0; nxt < n; ++nxt) if (!(mask & (1 << nxt)) && ok[last][nxt]) {
                    int nmask = mask | (1 << nxt);
                    dp[nmask][nxt] += cur;
                    if (dp[nmask][nxt] >= MOD) dp[nmask][nxt] -= MOD;
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += dp[fullMask][i];
        }
        return ans % MOD;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int specialPerm(int[] nums) {
        int n = nums.length;
        boolean[][] ok = new boolean[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0) ok[i][j] = true;
            }
        }
        int totalMask = 1 << n;
        long[][] dp = new long[totalMask][n];
        for (int i = 0; i < n; ++i) {
            dp[1 << i][i] = 1;
        }
        for (int mask = 1; mask < totalMask; ++mask) {
            for (int last = 0; last < n; ++last) {
                if ((mask & (1 << last)) == 0) continue;
                long cur = dp[mask][last];
                if (cur == 0) continue;
                int remain = (~mask) & (totalMask - 1);
                for (int nxt = 0; nxt < n; ++nxt) {
                    if ((remain & (1 << nxt)) != 0 && ok[last][nxt]) {
                        int nextMask = mask | (1 << nxt);
                        dp[nextMask][nxt] = (dp[nextMask][nxt] + cur) % MOD;
                    }
                }
            }
        }
        long ans = 0;
        int fullMask = totalMask - 1;
        for (int i = 0; i < n; ++i) {
            ans += dp[fullMask][i];
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # adjacency matrix: can move from i to j if condition holds
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        can[i][j] = True

        size = 1 << n
        dp = [[0] * n for _ in range(size)]
        for i in range(n):
            dp[1 << i][i] = 1

        full_mask = size - 1
        for mask in range(size):
            # iterate over possible last elements in current mask
            for last in range(n):
                if not (mask >> last) & 1:
                    continue
                cur = dp[mask][last]
                if cur == 0:
                    continue
                # try to add a new element next
                remaining = full_mask ^ mask
                nxt = remaining
                while nxt:
                    lsb = nxt & -nxt
                    j = (lsb.bit_length() - 1)
                    if can[last][j]:
                        dp[mask | lsb][j] = (dp[mask | lsb][j] + cur) % MOD
                    nxt -= lsb

        ans = sum(dp[full_mask]) % MOD
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # adjacency matrix: can move from i to j if condition holds
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    can[i][j] = True

        size = 1 << n
        dp = [[0] * n for _ in range(size)]
        for i in range(n):
            dp[1 << i][i] = 1

        full_mask = size - 1
        for mask in range(size):
            # iterate over possible last elements in current mask
            for last in range(n):
                if not (mask >> last) & 1:
                    continue
                cur = dp[mask][last]
                if cur == 0:
                    continue
                remaining = full_mask ^ mask
                m = remaining
                while m:
                    lowbit = m & -m
                    nxt = lowbit.bit_length() - 1
                    if can[last][nxt]:
                        dp[mask | (1 << nxt)][nxt] = (dp[mask | (1 << nxt)][nxt] + cur) % MOD
                    m ^= lowbit

        ans = sum(dp[full_mask]) % MOD
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int specialPerm(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int n = numsSize;
    int fullMask = 1 << n;

    bool can[14][14];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) {
                can[i][j] = false;
            } else {
                can[i][j] = (nums[i] % nums[j] == 0) || (nums[j] % nums[i] == 0);
            }
        }
    }

    long long *dp = (long long *)calloc((size_t)fullMask * n, sizeof(long long));
    if (!dp) return 0;

    for (int i = 0; i < n; ++i) {
        dp[((1 << i) * n) + i] = 1;
    }

    for (int mask = 0; mask < fullMask; ++mask) {
        for (int last = 0; last < n; ++last) {
            if (!(mask & (1 << last))) continue;
            long long cur = dp[mask * n + last];
            if (!cur) continue;
            for (int nxt = 0; nxt < n; ++nxt) {
                if (mask & (1 << nxt)) continue;
                if (!can[last][nxt]) continue;
                int nmask = mask | (1 << nxt);
                dp[nmask * n + nxt] = (dp[nmask * n + nxt] + cur) % MOD;
            }
        }
    }

    long long ans = 0;
    int finalMask = fullMask - 1;
    for (int i = 0; i < n; ++i) {
        ans = (ans + dp[finalMask * n + i]) % MOD;
    }

    free(dp);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int SpecialPerm(int[] nums) {
        const long MOD = 1000000007L;
        int n = nums.Length;
        bool[,] can = new bool[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long a = nums[i], b = nums[j];
                if (a % b == 0 || b % a == 0) can[i, j] = true;
            }
        }

        int fullMask = (1 << n) - 1;
        long[,] dp = new long[1 << n, n];

        for (int i = 0; i < n; i++) {
            dp[1 << i, i] = 1;
        }

        for (int mask = 0; mask <= fullMask; mask++) {
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0) continue;
                long cur = dp[mask, last];
                if (cur == 0) continue;
                int remaining = (~mask) & fullMask;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((remaining & (1 << nxt)) != 0 && can[last, nxt]) {
                        int nextMask = mask | (1 << nxt);
                        dp[nextMask, nxt] = (dp[nextMask, nxt] + cur) % MOD;
                    }
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + dp[fullMask, i]) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var specialPerm = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const fullMask = (1 << n) - 1;

    // precompute compatibility
    const can = Array.from({length: n}, () => new Array(n).fill(false));
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const a = nums[i], b = nums[j];
            if (a % b === 0 || b % a === 0) can[i][j] = true;
        }
    }

    // dp[mask][last]
    const dp = Array.from({length: 1 << n}, () => new Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        dp[1 << i][i] = 1;
    }

    for (let mask = 1; mask <= fullMask; ++mask) {
        for (let last = 0; last < n; ++last) {
            if ((mask & (1 << last)) === 0) continue;
            const cur = dp[mask][last];
            if (!cur) continue;
            for (let nxt = 0; nxt < n; ++nxt) {
                if (mask & (1 << nxt)) continue;
                if (!can[last][nxt]) continue;
                const nextMask = mask | (1 << nxt);
                dp[nextMask][nxt] = (dp[nextMask][nxt] + cur) % MOD;
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        ans = (ans + dp[fullMask][i]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function specialPerm(nums: number[]): number {
    const MOD = 1_000_000_007;
    const n = nums.length;
    const can: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (nums[i] % nums[j] === 0 || nums[j] % nums[i] === 0) {
                can[i][j] = true;
            }
        }
    }

    const size = 1 << n;
    const dp: number[][] = Array.from({ length: size }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        dp[1 << i][i] = 1;
    }

    for (let mask = 0; mask < size; mask++) {
        for (let last = 0; last < n; last++) {
            const cur = dp[mask][last];
            if (!cur) continue;
            for (let nxt = 0; nxt < n; nxt++) {
                if ((mask >> nxt) & 1) continue;
                if (can[last][nxt]) {
                    const nmask = mask | (1 << nxt);
                    dp[nmask][nxt] = (dp[nmask][nxt] + cur) % MOD;
                }
            }
        }
    }

    let ans = 0;
    const fullMask = size - 1;
    for (let i = 0; i < n; i++) {
        ans = (ans + dp[fullMask][i]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialPerm($nums) {
        $n = count($nums);
        $mod = 1000000007;
        $fullMask = (1 << $n) - 1;

        // Precompute compatibility matrix
        $allowed = array_fill(0, $n, array_fill(0, $n, false));
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == $j) continue;
                $a = $nums[$i];
                $b = $nums[$j];
                if ($a % $b == 0 || $b % $a == 0) {
                    $allowed[$i][$j] = true;
                }
            }
        }

        // DP[mask][last]
        $dp = array_fill(0, 1 << $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $dp[1 << $i][$i] = 1;
        }

        for ($mask = 0; $mask <= $fullMask; $mask++) {
            for ($last = 0; $last < $n; $last++) {
                if (!($mask & (1 << $last))) continue;
                $cur = $dp[$mask][$last];
                if ($cur == 0) continue;

                $remaining = $fullMask ^ $mask;
                for ($next = 0; $next < $n; $next++) {
                    if ($remaining & (1 << $next)) {
                        if ($allowed[$last][$next]) {
                            $newMask = $mask | (1 << $next);
                            $dp[$newMask][$next] = ($dp[$newMask][$next] + $cur) % $mod;
                        }
                    }
                }
            }
        }

        $ans = 0;
        foreach ($dp[$fullMask] as $val) {
            $ans = ($ans + $val) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func specialPerm(_ nums: [Int]) -> Int {
        let n = nums.count
        let fullMask = 1 << n
        let MOD = 1_000_000_007
        
        var can = Array(repeating: Array(repeating: false, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n where i != j {
                if nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0 {
                    can[i][j] = true
                }
            }
        }
        
        var dp = Array(repeating: Array(repeating: 0, count: n), count: fullMask)
        for i in 0..<n {
            dp[1 << i][i] = 1
        }
        
        for mask in 0..<fullMask {
            for last in 0..<n where (mask & (1 << last)) != 0 && dp[mask][last] > 0 {
                let cur = dp[mask][last]
                for nxt in 0..<n where (mask & (1 << nxt)) == 0 && can[last][nxt] {
                    let newMask = mask | (1 << nxt)
                    var val = dp[newMask][nxt] + cur
                    if val >= MOD { val -= MOD }
                    dp[newMask][nxt] = val
                }
            }
        }
        
        var ans = 0
        let finalMask = fullMask - 1
        for i in 0..<n {
            ans += dp[finalMask][i]
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun specialPerm(nums: IntArray): Int {
        val n = nums.size
        val can = Array(n) { BooleanArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i == j) continue
                val a = nums[i]
                val b = nums[j]
                if (a % b == 0 || b % a == 0) can[i][j] = true
            }
        }
        val fullMask = (1 shl n) - 1
        val MOD = 1_000_000_007L
        val dp = Array(1 shl n) { LongArray(n) }
        for (i in 0 until n) {
            dp[1 shl i][i] = 1L
        }
        for (mask in 0..fullMask) {
            for (last in 0 until n) {
                if ((mask and (1 shl last)) == 0) continue
                val cur = dp[mask][last]
                if (cur == 0L) continue
                for (next in 0 until n) {
                    if ((mask and (1 shl next)) != 0) continue
                    if (!can[last][next]) continue
                    val newMask = mask or (1 shl next)
                    dp[newMask][next] = (dp[newMask][next] + cur) % MOD
                }
            }
        }
        var ans = 0L
        for (i in 0 until n) {
            ans = (ans + dp[fullMask][i]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int specialPerm(List<int> nums) {
    final int n = nums.length;
    final int fullMask = (1 << n) - 1;

    // Precompute divisibility relations
    List<List<bool>> can = List.generate(n, (_) => List.filled(n, false));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        int a = nums[i], b = nums[j];
        can[i][j] = (a % b == 0) || (b % a == 0);
      }
    }

    // Memoization table: dp[mask][last]
    List<List<int>> memo =
        List.generate(1 << n, (_) => List.filled(n, -1));

    int dfs(int mask, int last) {
      if (mask == fullMask) return 1;
      int cached = memo[mask][last];
      if (cached != -1) return cached;

      int res = 0;
      for (int nxt = 0; nxt < n; nxt++) {
        if ((mask & (1 << nxt)) == 0 && can[last][nxt]) {
          res += dfs(mask | (1 << nxt), nxt);
          if (res >= _mod) res -= _mod;
        }
      }
      memo[mask][last] = res;
      return res;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      ans += dfs(1 << i, i);
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func specialPerm(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	// Precompute adjacency: can[i][j] is true if nums[i] and nums[j] satisfy the condition.
	can := make([][]bool, n)
	for i := 0; i < n; i++ {
		can[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			a, b := nums[i], nums[j]
			if a%b == 0 || b%a == 0 {
				can[i][j] = true
			}
		}
	}

	size := 1 << n
	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	// Initialize DP with each single-element permutation.
	for i := 0; i < n; i++ {
		dp[1<<i][i] = 1
	}

	for mask := 0; mask < size; mask++ {
		for last := 0; last < n; last++ {
			cur := dp[mask][last]
			if cur == 0 {
				continue
			}
			for nxt := 0; nxt < n; nxt++ {
				if mask>>nxt&1 == 1 {
					continue
				}
				if can[last][nxt] {
					nMask := mask | (1 << nxt)
					dp[nMask][nxt] = (dp[nMask][nxt] + cur) % mod
				}
			}
		}
	}

	fullMask := size - 1
	ans := 0
	for i := 0; i < n; i++ {
		ans = (ans + dp[fullMask][i]) % mod
	}
	return ans
}
```

## Ruby

```ruby
def special_perm(nums)
  mod = 1_000_000_007
  n = nums.length
  can = Array.new(n) { [] }
  n.times do |i|
    n.times do |j|
      next if i == j
      a = nums[i]
      b = nums[j]
      can[i] << j if (a % b).zero? || (b % a).zero?
    end
  end

  size = 1 << n
  dp = Array.new(size) { Array.new(n, 0) }

  n.times do |i|
    dp[1 << i][i] = 1
  end

  (size).times do |mask|
    n.times do |last|
      cur = dp[mask][last]
      next if cur.zero?
      can[last].each do |nxt|
        bit = 1 << nxt
        next if (mask & bit) != 0
        new_mask = mask | bit
        dp[new_mask][nxt] = (dp[new_mask][nxt] + cur) % mod
      end
    end
  end

  full = size - 1
  ans = 0
  n.times { |i| ans = (ans + dp[full][i]) % mod }
  ans
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007

  def specialPerm(nums: Array[Int]): Int = {
    val n = nums.length
    val can = Array.ofDim[Boolean](n, n)
    for (i <- 0 until n; j <- 0 until n if i != j) {
      can(i)(j) = (nums(i) % nums(j) == 0) || (nums(j) % nums(i) == 0)
    }

    val size = 1 << n
    val dp = Array.ofDim[Long](size, n)

    for (i <- 0 until n) {
      dp(1 << i)(i) = 1L
    }

    for (mask <- 0 until size) {
      for (last <- 0 until n if ((mask >> last) & 1) == 1) {
        val cur = dp(mask)(last)
        if (cur != 0) {
          var nxt = 0
          while (nxt < n) {
            if (((mask >> nxt) & 1) == 0 && can(last)(nxt)) {
              val newMask = mask | (1 << nxt)
              dp(newMask)(nxt) = (dp(newMask)(nxt) + cur) % MOD
            }
            nxt += 1
          }
        }
      }
    }

    var ans: Long = 0L
    val fullMask = size - 1
    for (i <- 0 until n) {
      ans = (ans + dp(fullMask)(i)) % MOD
    }
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn special_perm(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        const MOD: i64 = 1_000_000_007;
        // adjacency matrix: can[i][j] true if nums[i] and nums[j] satisfy the condition
        let mut can = vec![vec![false; n]; n];
        for i in 0..n {
            for j in 0..n {
                if i == j { continue; }
                let a = nums[i] as i64;
                let b = nums[j] as i64;
                if a % b == 0 || b % a == 0 {
                    can[i][j] = true;
                }
            }
        }

        let size = 1usize << n;
        // dp[mask][last] = number of ways to form permutation represented by mask ending with index last
        let mut dp = vec![vec![0i64; n]; size];
        for i in 0..n {
            dp[1 << i][i] = 1;
        }

        for mask in 0..size {
            for last in 0..n {
                let cur = dp[mask][last];
                if cur == 0 { continue; }
                for nxt in 0..n {
                    if (mask >> nxt) & 1 == 1 { continue; }
                    if can[last][nxt] {
                        let nmask = mask | (1 << nxt);
                        dp[nmask][nxt] = (dp[nmask][nxt] + cur) % MOD;
                    }
                }
            }
        }

        let full_mask = size - 1;
        let mut ans: i64 = 0;
        for last in 0..n {
            ans = (ans + dp[full_mask][last]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (special-perm nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (adj (make-vector n))
         (full-mask (sub1 (arithmetic-shift 1 n)))
         (MOD 1000000007))
    ;; build adjacency matrix
    (for ([i (in-range n)])
      (let ((row (make-vector n #f)))
        (for ([j (in-range n)])
          (when (not (= i j))
            (define xi (vector-ref vec i))
            (define xj (vector-ref vec j))
            (vector-set! row j (or (= (modulo xi xj) 0)
                                   (= (modulo xj xi) 0)))))
        (vector-set! adj i row)))
    ;; memoization table
    (define memo (make-vector (* (add1 full-mask) n) -1))
    (letrec ((dfs (lambda (mask last)
                    (let ((idx (+ (* mask n) last)))
                      (if (not (= (vector-ref memo idx) -1))
                          (vector-ref memo idx)
                          (let ((res
                                 (if (= mask full-mask)
                                     1
                                     (let loop ((j 0) (sum 0))
                                       (if (= j n)
                                           sum
                                           (let ((bit (arithmetic-shift 1 j)))
                                             (if (and (= (bitwise-and mask bit) 0)
                                                      (vector-ref (vector-ref adj last) j))
                                                 (loop (+ j 1)
                                                       (modulo (+ sum (dfs (bitwise-ior mask bit) j)) MOD))
                                                 (loop (+ j 1) sum))))))))
                            (vector-set! memo idx res)
                            res)))))
      (let ((total 0))
        (for ([i (in-range n)])
          (set! total (modulo (+ total (dfs (arithmetic-shift 1 i) i)) MOD)))
        total))))
```

## Erlang

```erlang
-module(solution).
-compile([export_all]).
-define(MOD, 1000000007).

-spec special_perm(Nums :: [integer()]) -> integer().
special_perm(Nums) ->
    N = length(Nums),
    AdjTuple = build_adj_tuple(Nums),
    MaxMask = 1 bsl N,
    InitDP = init_dp(N),
    FinalDP = loop(0, MaxMask, N, AdjTuple, InitDP),
    FullMask = MaxMask - 1,
    sum_fullmask(FinalDP, FullMask, N).

%% Build adjacency tuple where element(Index+1) is list of indices j that can follow i
build_adj_tuple(Nums) ->
    Indices = lists:seq(0, length(Nums) - 1),
    AdjLists = [ [ J || J <- Indices,
                       I /= J,
                       can(lists:nth(I + 1, Nums), lists:nth(J + 1, Nums)) ]
                || I <- Indices ],
    list_to_tuple(AdjLists).

can(A, B) ->
    (A rem B =:= 0) orelse (B rem A =:= 0).

init_dp(N) ->
    maps:from_list([ {{1 bsl I, I}, 1} || I <- lists:seq(0, N - 1) ]).

loop(Mask, MaxMask, _N, _AdjTuple, DP) when Mask >= MaxMask ->
    DP;
loop(Mask, MaxMask, N, AdjTuple, DP) ->
    DP1 = process_mask(Mask, 0, N, AdjTuple, DP),
    loop(Mask + 1, MaxMask, N, AdjTuple, DP1).

process_mask(_Mask, LastIdx, N, _AdjTuple, DP) when LastIdx >= N ->
    DP;
process_mask(Mask, LastIdx, N, AdjTuple, DP) ->
    case maps:find({Mask, LastIdx}, DP) of
        error ->
            process_mask(Mask, LastIdx + 1, N, AdjTuple, DP);
        {ok, Count} ->
            Adj = element(LastIdx + 1, AdjTuple),
            DP2 = try_next(Count, Mask, Adj, DP),
            process_mask(Mask, LastIdx + 1, N, AdjTuple, DP2)
    end.

try_next(_Count, _Mask, [], DP) ->
    DP;
try_next(Count, Mask, [Next | Rest], DP) ->
    Bit = 1 bsl Next,
    case (Mask band Bit) of
        0 ->
            NewMask = Mask bor Bit,
            Key = {NewMask, Next},
            Old = maps:get(Key, DP, 0),
            NewVal = (Old + Count) rem ?MOD,
            DP2 = maps:put(Key, NewVal, DP),
            try_next(Count, Mask, Rest, DP2);
        _ ->
            try_next(Count, Mask, Rest, DP)
    end.

sum_fullmask(DP, FullMask, N) ->
    lists:foldl(fun(I, Acc) ->
        (Acc + maps:get({FullMask, I}, DP, 0)) rem ?MOD
    end, 0, lists:seq(0, N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec special_perm(nums :: [integer]) :: integer
  def special_perm(nums) do
    mod = 1_000_000_007
    n = length(nums)
    full_mask = (1 <<< n) - 1

    adj =
      Enum.map(0..n - 1, fn i ->
        Enum.filter(0..n - 1, fn j ->
          a = Enum.at(nums, i)
          b = Enum.at(nums, j)
          rem(a, b) == 0 or rem(b, a) == 0
        end)
      end)

    init_dp =
      Enum.reduce(0..n - 1, %{}, fn i, acc ->
        Map.put(acc, {1 <<< i, i}, 1)
      end)

    dp =
      Enum.reduce(1..full_mask, init_dp, fn mask, dp_acc ->
        Enum.reduce(0..n - 1, dp_acc, fn last, dp_inner ->
          cnt = Map.get(dp_inner, {mask, last}, 0)

          if cnt == 0 do
            dp_inner
          else
            Enum.reduce(Enum.at(adj, last), dp_inner, fn nxt, dp2 ->
              if (mask &&& (1 <<< nxt)) != 0 do
                dp2
              else
                new_mask = mask ||| (1 <<< nxt)
                key = {new_mask, nxt}
                Map.update(dp2, key, cnt, fn existing -> rem(existing + cnt, mod) end)
              end
            end)
          end
        end)
      end)

    Enum.reduce(0..n - 1, 0, fn i, acc ->
      rem(acc + Map.get(dp, {full_mask, i}, 0), mod)
    end)
  end
end
```
