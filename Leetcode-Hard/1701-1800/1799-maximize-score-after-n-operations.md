# 1799. Maximize Score After N Operations

## Cpp

```cpp
class Solution {
public:
    int maxScore(vector<int>& nums) {
        int m = nums.size(); // 2 * n, where n <= 7
        vector<vector<int>> gc(m, vector<int>(m));
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j < m; ++j) {
                gc[i][j] = std::gcd(nums[i], nums[j]);
            }
        }
        int totalMask = 1 << m;
        const int NEG_INF = -1e9;
        vector<int> dp(totalMask, NEG_INF);
        dp[0] = 0;
        for (int mask = 0; mask < totalMask; ++mask) {
            int used = __builtin_popcount(mask);
            if (used % 2 != 0) continue; // only consider states with even count
            int op = used / 2 + 1; // next operation index (1‑based)
            // find first unused i to reduce repetitions
            for (int i = 0; i < m; ++i) {
                if (mask & (1 << i)) continue;
                for (int j = i + 1; j < m; ++j) {
                    if (mask & (1 << j)) continue;
                    int newMask = mask | (1 << i) | (1 << j);
                    dp[newMask] = max(dp[newMask], dp[mask] + op * gc[i][j]);
                }
            }
        }
        return dp[totalMask - 1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxScore(int[] nums) {
        int m = nums.length;
        int totalMask = 1 << m;
        int[] dp = new int[totalMask];
        Arrays.fill(dp, -1);
        dp[0] = 0;

        for (int mask = 0; mask < totalMask; ++mask) {
            if (dp[mask] == -1) continue;
            int used = Integer.bitCount(mask);
            if ((used & 1) == 1) continue; // only even counts are reachable
            int op = used / 2 + 1;

            for (int i = 0; i < m; ++i) {
                if ((mask & (1 << i)) != 0) continue;
                for (int j = i + 1; j < m; ++j) {
                    if ((mask & (1 << j)) != 0) continue;
                    int newMask = mask | (1 << i) | (1 << j);
                    int score = dp[mask] + op * gcd(nums[i], nums[j]);
                    if (score > dp[newMask]) dp[newMask] = score;
                }
            }
        }

        return dp[totalMask - 1];
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd
        m = len(nums)
        # precompute gcd for all pairs
        g = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(i+1, m):
                g[i][j] = gcd(nums[i], nums[j])
        from functools import lru_cache

        @lru_cache(None)
        def dfs(mask):
            if mask == (1 << m) - 1:
                return 0
            used = bin(mask).count('1')
            op = used // 2 + 1
            best = 0
            # find first unused index to reduce symmetry
            i = 0
            while i < m and (mask >> i) & 1:
                i += 1
            for j in range(i+1, m):
                if not (mask >> j) & 1:
                    new_mask = mask | (1 << i) | (1 << j)
                    cur = op * g[i][j] + dfs(new_mask)
                    if cur > best:
                        best = cur
            return best

        return dfs(0)
```

## Python3

```python
from typing import List
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        full_mask = (1 << m) - 1
        dp = [-1] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            if dp[mask] < 0:
                continue
            used = bin(mask).count("1")
            if used == m:
                continue
            op = used // 2 + 1
            # find first unused index to reduce duplicate work (optional)
            for i in range(m):
                if mask >> i & 1:
                    continue
                for j in range(i + 1, m):
                    if mask >> j & 1:
                        continue
                    new_mask = mask | (1 << i) | (1 << j)
                    score = dp[mask] + op * math.gcd(nums[i], nums[j])
                    if score > dp[new_mask]:
                        dp[new_mask] = score
        return dp[full_mask]
```

## C

```c
#include <limits.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int maxScore(int* nums, int numsSize) {
    int m = numsSize;                 // 2 * n
    int fullMask = (1 << m) - 1;
    static int dp[1 << 14];
    for (int i = 0; i <= fullMask; ++i) dp[i] = INT_MIN;
    dp[0] = 0;

    for (int mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] == INT_MIN) continue;
        int used = __builtin_popcount(mask);
        if (used == m) continue;
        int op = used / 2 + 1; // next operation index (1‑based)

        for (int i = 0; i < m; ++i) {
            if (mask & (1 << i)) continue;
            for (int j = i + 1; j < m; ++j) {
                if (mask & (1 << j)) continue;
                int newMask = mask | (1 << i) | (1 << j);
                int g = gcd_int(nums[i], nums[j]);
                int val = dp[mask] + op * g;
                if (val > dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[fullMask];
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    private int n;
    private int len;
    private int[,] gcdCache;
    private int[] dp;
    private int fullMask;

    public int MaxScore(int[] nums) {
        len = nums.Length;
        n = len / 2;
        gcdCache = new int[len, len];
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                gcdCache[i, j] = Gcd(nums[i], nums[j]);
            }
        }
        fullMask = (1 << len) - 1;
        dp = new int[1 << len];
        Array.Fill(dp, -1);
        return Dfs(0);
    }

    private int Dfs(int mask) {
        if (mask == fullMask) return 0;
        if (dp[mask] != -1) return dp[mask];

        int used = BitOperations.PopCount((uint)mask);
        int op = used / 2 + 1;

        int i = 0;
        while (((mask >> i) & 1) == 1) i++;

        int best = 0;
        for (int j = i + 1; j < len; j++) {
            if ((mask & (1 << j)) != 0) continue;
            int newMask = mask | (1 << i) | (1 << j);
            int score = op * gcdCache[i, j] + Dfs(newMask);
            if (score > best) best = score;
        }

        dp[mask] = best;
        return best;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    const m = nums.length; // 2 * n, where n <= 7
    const totalMask = 1 << m;
    const memo = new Array(totalMask).fill(-1);
    
    // precompute gcd for all pairs
    const g = Array.from({ length: m }, () => Array(m).fill(0));
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    for (let i = 0; i < m; ++i) {
        for (let j = i + 1; j < m; ++j) {
            g[i][j] = gcd(nums[i], nums[j]);
        }
    }
    
    const dfs = (mask) => {
        if (mask === totalMask - 1) return 0;
        if (memo[mask] !== -1) return memo[mask];
        
        // count bits set in mask
        let cnt = 0;
        for (let t = mask; t; t &= t - 1) cnt++;
        const op = Math.floor(cnt / 2) + 1; // current operation index (1‑based)
        
        let best = 0;
        for (let i = 0; i < m; ++i) {
            if ((mask >> i) & 1) continue;
            for (let j = i + 1; j < m; ++j) {
                if ((mask >> j) & 1) continue;
                const newMask = mask | (1 << i) | (1 << j);
                const score = op * g[i][j] + dfs(newMask);
                if (score > best) best = score;
            }
        }
        memo[mask] = best;
        return best;
    };
    
    return dfs(0);
};
```

## Typescript

```typescript
function maxScore(nums: number[]): number {
    const m = nums.length;
    const totalMask = 1 << m;
    const dp = new Array<number>(totalMask).fill(-Infinity);
    dp[0] = 0;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    const pairGcd = Array.from({ length: m }, () => new Array<number>(m).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = i + 1; j < m; j++) {
            pairGcd[i][j] = gcd(nums[i], nums[j]);
        }
    }

    const popcnt = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    for (let mask = 0; mask < totalMask; mask++) {
        if (dp[mask] === -Infinity) continue;
        const usedBits = popcnt(mask);
        if (usedBits === m) continue;
        const op = (usedBits >> 1) + 1; // operation index

        for (let i = 0; i < m; i++) {
            if ((mask >> i) & 1) continue;
            for (let j = i + 1; j < m; j++) {
                if ((mask >> j) & 1) continue;
                const newMask = mask | (1 << i) | (1 << j);
                const score = dp[mask] + op * pairGcd[i][j];
                if (score > dp[newMask]) dp[newMask] = score;
            }
        }
    }

    return dp[totalMask - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxScore($nums) {
        $n = count($nums);
        // precompute gcd for all pairs
        $gcd = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $g = $this->gcd($nums[$i], $nums[$j]);
                $gcd[$i][$j] = $g;
                $gcd[$j][$i] = $g;
            }
        }

        $fullMask = (1 << $n) - 1;
        $memo = [];

        $dfs = function($mask) use (&$dfs, &$memo, $gcd, $n, $fullMask) {
            if ($mask === $fullMask) {
                return 0;
            }
            if (isset($memo[$mask])) {
                return $memo[$mask];
            }

            // count used bits
            $cnt = 0;
            $tmp = $mask;
            while ($tmp) {
                $cnt += $tmp & 1;
                $tmp >>= 1;
            }
            $op = ($cnt >> 1) + 1; // number of operation (1-indexed)

            $best = 0;
            for ($i = 0; $i < $n; $i++) {
                if (($mask >> $i) & 1) continue;
                for ($j = $i + 1; $j < $n; $j++) {
                    if (($mask >> $j) & 1) continue;
                    $newMask = $mask | (1 << $i) | (1 << $j);
                    $score = $op * $gcd[$i][$j] + $dfs($newMask);
                    if ($score > $best) {
                        $best = $score;
                    }
                }
            }

            $memo[$mask] = $best;
            return $best;
        };

        return $dfs(0);
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let m = nums.count
        let totalMask = 1 << m
        var dp = Array(repeating: 0, count: totalMask)
        
        // Precompute GCD for all pairs
        var gcdCache = Array(repeating: Array(repeating: 0, count: m), count: m)
        for i in 0..<m {
            for j in i+1..<m {
                gcdCache[i][j] = Self.gcd(nums[i], nums[j])
            }
        }
        
        for mask in 0..<totalMask {
            let usedCount = mask.nonzeroBitCount
            if usedCount % 2 != 0 { continue } // only states with even number of used elements are valid
            let operation = usedCount / 2 + 1
            
            // try picking two unused indices
            for i in 0..<m where ((mask >> i) & 1) == 0 {
                for j in (i+1)..<m where ((mask >> j) & 1) == 0 {
                    let newMask = mask | (1 << i) | (1 << j)
                    let addedScore = operation * gcdCache[i][j]
                    let candidate = dp[mask] + addedScore
                    if candidate > dp[newMask] {
                        dp[newMask] = candidate
                    }
                }
            }
        }
        
        return dp[totalMask - 1]
    }
    
    private static func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray): Int {
        val m = nums.size
        val totalMask = 1 shl m
        val dp = IntArray(totalMask) { -1 }
        dp[0] = 0

        // precompute gcd for all pairs
        val g = Array(m) { IntArray(m) }
        for (i in 0 until m) {
            for (j in i + 1 until m) {
                g[i][j] = gcd(nums[i], nums[j])
                g[j][i] = g[i][j]
            }
        }

        for (mask in 0 until totalMask) {
            val cur = dp[mask]
            if (cur < 0) continue
            val used = Integer.bitCount(mask)
            if (used == m) continue
            val op = used / 2 + 1

            for (i in 0 until m) {
                if ((mask and (1 shl i)) != 0) continue
                for (j in i + 1 until m) {
                    if ((mask and (1 shl j)) != 0) continue
                    val newMask = mask or (1 shl i) or (1 shl j)
                    val score = cur + op * g[i][j]
                    if (score > dp[newMask]) dp[newMask] = score
                }
            }
        }

        return dp[totalMask - 1]
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<int> nums) {
    int m = nums.length;
    List<List<int>> gcdTable = List.generate(m, (_) => List.filled(m, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = i + 1; j < m; ++j) {
        int g = _gcd(nums[i], nums[j]);
        gcdTable[i][j] = g;
      }
    }

    List<int> memo = List.filled(1 << m, -1);

    int popCount(int x) {
      int cnt = 0;
      while (x > 0) {
        cnt += x & 1;
        x >>= 1;
      }
      return cnt;
    }

    int dfs(int mask) {
      if (memo[mask] != -1) return memo[mask];
      int used = popCount(mask);
      if (used == m) return memo[mask] = 0;

      int op = used ~/ 2 + 1; // operation index (1‑based)
      int best = 0;
      for (int i = 0; i < m; ++i) {
        if ((mask >> i) & 1 == 1) continue;
        for (int j = i + 1; j < m; ++j) {
          if ((mask >> j) & 1 == 1) continue;
          int newMask = mask | (1 << i) | (1 << j);
          int val = op * gcdTable[i][j] + dfs(newMask);
          if (val > best) best = val;
        }
      }
      return memo[mask] = best;
    }

    return dfs(0);
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func maxScore(nums []int) int {
	m := len(nums)
	fullMask := (1 << m) - 1
	dp := make([]int, 1<<m)
	for i := range dp {
		dp[i] = -1
	}
	var dfs func(mask int) int
	dfs = func(mask int) int {
		if mask == fullMask {
			return 0
		}
		if dp[mask] != -1 {
			return dp[mask]
		}
		used := bits.OnesCount(uint(mask))
		op := used/2 + 1
		best := 0
		for i := 0; i < m; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			for j := i + 1; j < m; j++ {
				if mask&(1<<j) != 0 {
					continue
				}
				newMask := mask | (1 << i) | (1 << j)
				score := op * gcd(nums[i], nums[j]) + dfs(newMask)
				if score > best {
					best = score
				}
			}
		}
		dp[mask] = best
		return best
	}
	return dfs(0)
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
def max_score(nums)
  m = nums.length
  size = 1 << m
  dp = Array.new(size, -1 << 60)
  dp[0] = 0

  # precompute gcd for all pairs
  gcd = Array.new(m) { Array.new(m, 0) }
  (0...m).each do |i|
    ((i + 1)...m).each do |j|
      g = nums[i].gcd(nums[j])
      gcd[i][j] = g
      gcd[j][i] = g
    end
  end

  # popcount for each mask
  pc = Array.new(size, 0)
  (1...size).each { |i| pc[i] = pc[i >> 1] + (i & 1) }

  (0...size).each do |mask|
    cnt = pc[mask]
    next if cnt.odd?
    op_idx = cnt / 2 + 1

    i = 0
    while i < m
      if (mask & (1 << i)).zero?
        j = i + 1
        while j < m
          if (mask & (1 << j)).zero?
            new_mask = mask | (1 << i) | (1 << j)
            val = dp[mask] + op_idx * gcd[i][j]
            dp[new_mask] = val if val > dp[new_mask]
          end
          j += 1
        end
      end
      i += 1
    end
  end

  dp[size - 1]
end
```

## Scala

```scala
object Solution {
    def maxScore(nums: Array[Int]): Int = {
        val m = nums.length
        val fullMask = (1 << m) - 1
        val dp = Array.fill(1 << m)(-1)

        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            x
        }

        // precompute gcd for all pairs
        val g = Array.ofDim[Int](m, m)
        for (i <- 0 until m) {
            for (j <- i + 1 until m) {
                g(i)(j) = gcd(nums(i), nums(j))
                g(j)(i) = g(i)(j)
            }
        }

        def dfs(mask: Int): Int = {
            if (mask == fullMask) return 0
            if (dp(mask) != -1) return dp(mask)

            // find first unused index to reduce symmetry
            var i = 0
            while (((mask >> i) & 1) == 1) i += 1

            var best = 0
            var j = i + 1
            while (j < m) {
                if (((mask >> j) & 1) == 0) {
                    val newMask = mask | (1 << i) | (1 << j)
                    val opIdx = Integer.bitCount(mask) / 2 + 1
                    val score = opIdx * g(i)(j) + dfs(newMask)
                    if (score > best) best = score
                }
                j += 1
            }

            dp(mask) = best
            best
        }

        dfs(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        fn dfs(mask: usize, nums: &Vec<i32>, memo: &mut Vec<i32>) -> i32 {
            if mask == (1usize << nums.len()) - 1 {
                return 0;
            }
            if memo[mask] != -1 {
                return memo[mask];
            }
            let used = mask.count_ones() as usize;
            let op = (used / 2 + 1) as i32;
            let mut best = 0i32;
            let n = nums.len();
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    continue;
                }
                for j in (i + 1)..n {
                    if (mask >> j) & 1 == 1 {
                        continue;
                    }
                    let new_mask = mask | (1usize << i) | (1usize << j);
                    let g = gcd(nums[i], nums[j]);
                    let score = op * g + dfs(new_mask, nums, memo);
                    if score > best {
                        best = score;
                    }
                }
            }
            memo[mask] = best;
            best
        }

        let m = nums.len();
        let size = 1usize << m;
        let mut memo = vec![-1i32; size];
        dfs(0, &nums, &mut memo)
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-score nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([arr (list->vector nums)]
         [m (vector-length arr)]
         [total-mask (sub1 (arithmetic-shift 1 m))]
         [dp (make-vector (arithmetic-shift 1 m) -1)])
    (define (popcnt x)
      (let loop ((y x) (c 0))
        (if (zero? y)
            c
            (loop (arithmetic-shift y -1) (+ c (bitwise-and y 1))))))
    (define (dfs mask)
      (if (= mask total-mask)
          0
          (let ([cached (vector-ref dp mask)])
            (if (not (= cached -1))
                cached
                (let* ([taken (popcnt mask)]
                       [op (+ (quotient taken 2) 1)])
                  (let loop-i ((i 0) (best 0))
                    (if (>= i m)
                        (begin (vector-set! dp mask best) best)
                        (if (zero? (bitwise-and mask (arithmetic-shift 1 i)))
                            (let inner-loop ((j (+ i 1)) (best-inner best))
                              (if (>= j m)
                                  (loop-i (+ i 1) best-inner)
                                  (if (zero? (bitwise-and mask (arithmetic-shift 1 j)))
                                      (let* ([new-mask (bitwise-ior mask
                                                                    (arithmetic-shift 1 i)
                                                                    (arithmetic-shift 1 j))]
                                             [gain (* op (gcd (vector-ref arr i) (vector-ref arr j)))]
                                             [cand (+ gain (dfs new-mask))])
                                        (inner-loop (+ j 1) (if (> cand best-inner) cand best-inner)))
                                      (inner-loop (+ j 1) best-inner))))
                            (loop-i (+ i 1) best)))))))))
    (dfs 0)))
```

## Erlang

```erlang
-spec max_score([integer()]) -> integer().
max_score(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    MaxMask = 1 bsl Len,
    DP0 = maps:put(0, 0, #{}),
    FinalDP = dp_loop(0, MaxMask, Tuple, Len, DP0),
    FinalMask = MaxMask - 1,
    maps:get(FinalMask, FinalDP).

dp_loop(Mask, MaxMask, Tuple, Len, DP) when Mask < MaxMask ->
    case maps:get(Mask, DP, undefined) of
        undefined ->
            dp_loop(Mask + 1, MaxMask, Tuple, Len, DP);
        CurScore ->
            OpIdx = (popcount(Mask) div 2) + 1,
            NewDP = update_pairs(Mask, CurScore, OpIdx, Tuple, Len, DP),
            dp_loop(Mask + 1, MaxMask, Tuple, Len, NewDP)
    end;
dp_loop(_, _, _, _, DP) ->
    DP.

update_pairs(Mask, CurScore, OpIdx, Tuple, Len, DP) ->
    lists:foldl(
      fun(I, AccDP) ->
          case (Mask band (1 bsl I)) of
              0 ->
                  lists:foldl(
                    fun(J, AccDP2) ->
                        case (Mask band (1 bsl J)) of
                            0 ->
                                NewMask = Mask bor (1 bsl I) bor (1 bsl J),
                                A = element(I + 1, Tuple),
                                B = element(J + 1, Tuple),
                                G = gcd(A, B),
                                Score = CurScore + G * OpIdx,
                                Prev = maps:get(NewMask, AccDP2, -1),
                                if Score > Prev ->
                                        maps:put(NewMask, Score, AccDP2);
                                   true -> AccDP2
                                end;
                            _ -> AccDP2
                        end
                    end,
                    AccDP,
                    lists:seq(I + 1, Len - 1)
                  );
              _ -> AccDP
          end
      end,
      DP,
      lists:seq(0, Len - 1)
    ).

popcount(N) when N =:= 0 -> 0;
popcount(N) ->
    (N band 1) + popcount(N bsr 1).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec max_score(nums :: [integer]) :: integer
  def max_score(nums) do
    m = length(nums)

    gcds =
      Enum.reduce(0..(m - 1), %{}, fn i, acc ->
        Enum.reduce((i + 1)..(m - 1), acc, fn j, acc2 ->
          Map.put(acc2, {i, j}, Integer.gcd(Enum.at(nums, i), Enum.at(nums, j)))
        end)
      end)

    {res, _} = dfs(0, 1, %{}, m, gcds)
    res
  end

  defp dfs(mask, op, memo, m, gcds) do
    case Map.fetch(memo, mask) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if mask == (1 <<< m) - 1 do
          {0, Map.put(memo, mask, 0)}
        else
          i = Enum.find(0..(m - 1), fn idx -> (mask &&& (1 <<< idx)) == 0 end)

          {best, memo2} =
            Enum.reduce((i + 1)..(m - 1), {0, memo}, fn j, {cur_best, cur_memo} ->
              if (mask &&& (1 <<< j)) == 0 do
                new_mask = mask ||| (1 <<< i) ||| (1 <<< j)
                {score_rest, memo_next} = dfs(new_mask, op + 1, cur_memo, m, gcds)

                cur = op * Map.get(gcds, {i, j}) + score_rest
                new_best = if cur > cur_best, do: cur, else: cur_best
                {new_best, memo_next}
              else
                {cur_best, cur_memo}
              end
            end)

          memo_final = Map.put(memo2, mask, best)
          {best, memo_final}
        end
    end
  end
end
```
