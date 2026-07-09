# 3336. Find the Number of Subsequences With Equal GCD

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        const int MAXV = 200;
        static int dp[201][201];
        static int ndp[201][201];
        for (int i = 0; i <= MAXV; ++i)
            for (int j = 0; j <= MAXV; ++j)
                dp[i][j] = 0;
        dp[0][0] = 1; // both groups empty
        
        for (int v : nums) {
            for (int i = 0; i <= MAXV; ++i)
                for (int j = 0; j <= MAXV; ++j)
                    ndp[i][j] = 0;
            
            for (int g1 = 0; g1 <= MAXV; ++g1) {
                for (int g2 = 0; g2 <= MAXV; ++g2) {
                    int cur = dp[g1][g2];
                    if (!cur) continue;
                    
                    // skip current element
                    ndp[g1][g2] = (ndp[g1][g2] + cur) % MOD;
                    
                    // put into group 1
                    int ng1 = g1 == 0 ? v : std::gcd(g1, v);
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD;
                    
                    // put into group 2
                    int ng2 = g2 == 0 ? v : std::gcd(g2, v);
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD;
                }
            }
            // swap dp and ndp
            for (int i = 0; i <= MAXV; ++i)
                for (int j = 0; j <= MAXV; ++j)
                    dp[i][j] = ndp[i][j];
        }
        
        long long ans = 0;
        for (int g = 1; g <= MAXV; ++g) {
            ans += dp[g][g];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private static final int MAXV = 200;

    public int subsequencePairCount(int[] nums) {
        long[][] dp = new long[MAXV + 1][MAXV + 1];
        dp[0][0] = 1; // both groups empty

        for (int v : nums) {
            long[][] ndp = new long[MAXV + 1][MAXV + 1];
            for (int g1 = 0; g1 <= MAXV; ++g1) {
                for (int g2 = 0; g2 <= MAXV; ++g2) {
                    long cur = dp[g1][g2];
                    if (cur == 0) continue;
                    // leave unused
                    ndp[g1][g2] = (ndp[g1][g2] + cur) % MOD;
                    // assign to group1
                    int ng1 = (g1 == 0) ? v : gcd(g1, v);
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD;
                    // assign to group2
                    int ng2 = (g2 == 0) ? v : gcd(g2, v);
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD;
                }
            }
            dp = ndp;
        }

        long ordered = 0;
        for (int g = 1; g <= MAXV; ++g) {
            ordered = (ordered + dp[g][g]) % MOD;
        }

        // unordered pairs: divide by 2 modulo MOD
        long inv2 = (MOD + 1L) / 2;
        long result = ordered * inv2 % MOD;
        return (int) result;
    }

    private static int gcd(int a, int b) {
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
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd
        MOD = 10**9 + 7
        MAXV = 200
        M = MAXV + 1  # include zero for empty subsequence

        cur = [[0] * M for _ in range(M)]
        cur[0][0] = 1  # both subsequences are empty initially

        for x in nums:
            nxt = [[0] * M for _ in range(M)]
            for g1 in range(M):
                row = cur[g1]
                for g2 in range(M):
                    val = row[g2]
                    if not val:
                        continue
                    # skip current element
                    nxt[g1][g2] = (nxt[g1][g2] + val) % MOD

                    # assign to first subsequence
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    nxt[ng1][g2] = (nxt[ng1][g2] + val) % MOD

                    # assign to second subsequence
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    nxt[g1][ng2] = (nxt[g1][ng2] + val) % MOD
            cur = nxt

        ans = 0
        for g in range(1, M):
            ans = (ans + cur[g][g]) % MOD
        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 200  # given constraint for nums[i]
        dp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        dp[0][0] = 1  # both subsequences empty so far

        for v in nums:
            newdp = [row[:] for row in dp]  # copy for the "skip" option
            for g1 in range(MAXV + 1):
                row = dp[g1]
                for g2 in range(MAXV + 1):
                    cnt = row[g2]
                    if not cnt:
                        continue
                    # assign v to first subsequence
                    ng1 = v if g1 == 0 else math.gcd(g1, v)
                    newdp[ng1][g2] = (newdp[ng1][g2] + cnt) % MOD
                    # assign v to second subsequence
                    ng2 = v if g2 == 0 else math.gcd(g2, v)
                    newdp[g1][ng2] = (newdp[g1][ng2] + cnt) % MOD
            dp = newdp

        ans = sum(dp[g][g] for g in range(1, MAXV + 1)) % MOD
        return ans
```

## C

```c
#include <stddef.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int subsequencePairCount(int* nums, int numsSize) {
    const int MOD = 1000000007;
    static int dp[201][201][4];
    static int ndp[201][201][4];

    for (int i = 0; i <= 200; ++i)
        for (int j = 0; j <= 200; ++j)
            for (int m = 0; m < 4; ++m)
                dp[i][j][m] = 0;

    dp[0][0][0] = 1;

    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        for (int i = 0; i <= 200; ++i)
            for (int j = 0; j <= 200; ++j)
                for (int m = 0; m < 4; ++m)
                    ndp[i][j][m] = 0;

        for (int g1 = 0; g1 <= 200; ++g1) {
            for (int g2 = 0; g2 <= 200; ++g2) {
                for (int mask = 0; mask < 4; ++mask) {
                    int cur = dp[g1][g2][mask];
                    if (!cur) continue;

                    // skip current element
                    ndp[g1][g2][mask] += cur;
                    if (ndp[g1][g2][mask] >= MOD) ndp[g1][g2][mask] -= MOD;

                    // assign to first subsequence
                    {
                        int nmask = mask | 1;
                        int ng1 = (mask & 1) ? gcd_int(g1, x) : x;
                        ndp[ng1][g2][nmask] += cur;
                        if (ndp[ng1][g2][nmask] >= MOD) ndp[ng1][g2][nmask] -= MOD;
                    }

                    // assign to second subsequence
                    {
                        int nmask = mask | 2;
                        int ng2 = (mask & 2) ? gcd_int(g2, x) : x;
                        ndp[g1][ng2][nmask] += cur;
                        if (ndp[g1][ng2][nmask] >= MOD) ndp[g1][ng2][nmask] -= MOD;
                    }
                }
            }
        }

        // swap dp and ndp
        for (int i = 0; i <= 200; ++i)
            for (int j = 0; j <= 200; ++j)
                for (int m = 0; m < 4; ++m)
                    dp[i][j][m] = ndp[i][j][m];
    }

    long long ans = 0;
    for (int g = 1; g <= 200; ++g) {
        ans += dp[g][g][3];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
public class Solution {
    private const int MOD = 1000000007;
    private static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int SubsequencePairCount(int[] nums) {
        const int MAXV = 200;
        int[,] cur = new int[MAXV + 1, MAXV + 1];
        cur[0, 0] = 1;

        foreach (int val in nums) {
            int[,] nxt = new int[MAXV + 1, MAXV + 1];
            for (int g1 = 0; g1 <= MAXV; ++g1) {
                for (int g2 = 0; g2 <= MAXV; ++g2) {
                    int ways = cur[g1, g2];
                    if (ways == 0) continue;

                    // ignore current element
                    nxt[g1, g2] = (nxt[g1, g2] + ways) % MOD;

                    // put into first subsequence
                    int ng1 = g1 == 0 ? val : Gcd(g1, val);
                    nxt[ng1, g2] = (nxt[ng1, g2] + ways) % MOD;

                    // put into second subsequence
                    int ng2 = g2 == 0 ? val : Gcd(g2, val);
                    nxt[g1, ng2] = (nxt[g1, ng2] + ways) % MOD;
                }
            }
            cur = nxt;
        }

        long ans = 0;
        for (int g = 1; g <= MAXV; ++g) {
            ans += cur[g, g];
        }
        ans %= MOD;
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
var subsequencePairCount = function(nums) {
    const MOD = 1000000007;
    const MAX = 200; // maximum possible value of nums[i] and gcd
    
    // dp[g1][g2] : number of ways after processing some elements,
    // where current GCD of group1 is g1 (0 means empty),
    // and GCD of group2 is g2 (0 means empty).
    let dp = Array.from({length: MAX + 1}, () => Array(MAX + 1).fill(0));
    dp[0][0] = 1;
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    for (const x of nums) {
        // ndp will hold the new states after considering current element
        let ndp = Array.from({length: MAX + 1}, () => Array(MAX + 1).fill(0));
        
        // Option 1: put current element into none of the groups (copy old state)
        for (let g1 = 0; g1 <= MAX; ++g1) {
            const dpRow = dp[g1];
            const ndpRow = ndp[g1];
            for (let g2 = 0; g2 <= MAX; ++g2) {
                const val = dpRow[g2];
                if (val !== 0) {
                    ndpRow[g2] = (ndpRow[g2] + val) % MOD;
                }
            }
        }
        
        // Options 2 & 3: put current element into group1 or group2
        for (let g1 = 0; g1 <= MAX; ++g1) {
            for (let g2 = 0; g2 <= MAX; ++g2) {
                const val = dp[g1][g2];
                if (val === 0) continue;
                
                // assign to group1
                const ng1 = g1 === 0 ? x : gcd(g1, x);
                ndp[ng1][g2] = (ndp[ng1][g2] + val) % MOD;
                
                // assign to group2
                const ng2 = g2 === 0 ? x : gcd(g2, x);
                ndp[g1][ng2] = (ndp[g1][ng2] + val) % MOD;
            }
        }
        
        dp = ndp;
    }
    
    // Sum over states where both groups are non‑empty and have equal GCD
    let ans = 0;
    for (let g = 1; g <= MAX; ++g) {
        ans = (ans + dp[g][g]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function subsequencePairCount(nums: number[]): number {
    const MOD = 1_000_000_007;
    const MAXV = 200;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let dp: number[][] = Array.from({ length: MAXV + 1 }, () => new Array(MAXV + 1).fill(0));
    dp[0][0] = 1;

    for (const x of nums) {
        const ndp: number[][] = dp.map(row => row.slice());

        for (let g1 = 0; g1 <= MAXV; ++g1) {
            const row = dp[g1];
            for (let g2 = 0; g2 <= MAXV; ++g2) {
                const val = row[g2];
                if (val === 0) continue;

                // assign to first subsequence
                const ng1 = g1 === 0 ? x : gcd(g1, x);
                ndp[ng1][g2] = (ndp[ng1][g2] + val) % MOD;

                // assign to second subsequence
                const ng2 = g2 === 0 ? x : gcd(g2, x);
                ndp[g1][ng2] = (ndp[g1][ng2] + val) % MOD;
            }
        }

        dp = ndp;
    }

    let ans = 0;
    for (let g = 1; g <= MAXV; ++g) {
        ans = (ans + dp[g][g]) % MOD;
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
    function subsequencePairCount($nums) {
        $MOD = 1000000007;
        $MAXV = 200;

        // Initialize dp[a][b] where a,b are GCDs (0 means empty)
        $dp = array_fill(0, $MAXV + 1, array_fill(0, $MAXV + 1, 0));
        $dp[0][0] = 1;

        foreach ($nums as $x) {
            // Prepare next dp
            $next = array_fill(0, $MAXV + 1, array_fill(0, $MAXV + 1, 0));

            for ($a = 0; $a <= $MAXV; ++$a) {
                for ($b = 0; $b <= $MAXV; ++$b) {
                    $val = $dp[$a][$b];
                    if ($val == 0) continue;

                    // Option 1: put element into none
                    $next[$a][$b] = ($next[$a][$b] + $val) % $MOD;

                    // Option 2: put element into A
                    $newA = ($a == 0) ? $x : $this->gcd($a, $x);
                    $next[$newA][$b] = ($next[$newA][$b] + $val) % $MOD;

                    // Option 3: put element into B
                    $newB = ($b == 0) ? $x : $this->gcd($b, $x);
                    $next[$a][$newB] = ($next[$a][$newB] + $val) % $MOD;
                }
            }

            $dp = $next;
        }

        $ans = 0;
        for ($g = 1; $g <= $MAXV; ++$g) {
            $ans = ($ans + $dp[$g][$g]) % $MOD;
        }
        return $ans;
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
class Solution {
    private let MOD = 1_000_000_007
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 {
            let t = x % y
            x = y
            y = t
        }
        return x
    }
    
    func subsequencePairCount(_ nums: [Int]) -> Int {
        let maxVal = 200
        var dp = Array(repeating: Array(repeating: 0, count: maxVal + 1), count: maxVal + 1)
        dp[0][0] = 1
        
        for x in nums {
            var newdp = Array(repeating: Array(repeating: 0, count: maxVal + 1), count: maxVal + 1)
            for g1 in 0...maxVal {
                for g2 in 0...maxVal {
                    let cur = dp[g1][g2]
                    if cur == 0 { continue }
                    
                    // assign to none
                    newdp[g1][g2] = (newdp[g1][g2] + cur) % MOD
                    
                    // assign to first subsequence
                    let ng1 = g1 == 0 ? x : gcd(g1, x)
                    newdp[ng1][g2] = (newdp[ng1][g2] + cur) % MOD
                    
                    // assign to second subsequence
                    let ng2 = g2 == 0 ? x : gcd(g2, x)
                    newdp[g1][ng2] = (newdp[g1][ng2] + cur) % MOD
                }
            }
            dp = newdp
        }
        
        var ans = 0
        for g in 1...maxVal {
            ans = (ans + dp[g][g]) % MOD
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }

    fun subsequencePairCount(nums: IntArray): Int {
        val maxV = 200
        var dp = Array(maxV + 1) { LongArray(maxV + 1) }
        dp[0][0] = 1L

        for (v in nums) {
            val ndp = Array(maxV + 1) { LongArray(maxV + 1) }
            for (g1 in 0..maxV) {
                val row = dp[g1]
                for (g2 in 0..maxV) {
                    val cnt = row[g2]
                    if (cnt == 0L) continue
                    // assign to none
                    ndp[g1][g2] = (ndp[g1][g2] + cnt) % MOD
                    // assign to first subsequence
                    val ng1 = if (g1 == 0) v else gcd(g1, v)
                    ndp[ng1][g2] = (ndp[ng1][g2] + cnt) % MOD
                    // assign to second subsequence
                    val ng2 = if (g2 == 0) v else gcd(g2, v)
                    ndp[g1][ng2] = (ndp[g1][ng2] + cnt) % MOD
                }
            }
            dp = ndp
        }

        var ans = 0L
        for (g in 1..maxV) {
            ans = (ans + dp[g][g]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int subsequencePairCount(List<int> nums) {
    int maxV = 200;
    List<List<int>> cur =
        List.generate(maxV + 1, (_) => List.filled(maxV + 1, 0));
    cur[0][0] = 1;

    for (int x in nums) {
      List<List<int>> nxt =
          List.generate(maxV + 1, (_) => List.filled(maxV + 1, 0));
      for (int g1 = 0; g1 <= maxV; ++g1) {
        for (int g2 = 0; g2 <= maxV; ++g2) {
          int val = cur[g1][g2];
          if (val == 0) continue;
          // ignore
          nxt[g1][g2] = (nxt[g1][g2] + val) % _mod;
          // put in A
          int ng1 = g1 == 0 ? x : _gcd(g1, x);
          nxt[ng1][g2] = (nxt[ng1][g2] + val) % _mod;
          // put in B
          int ng2 = g2 == 0 ? x : _gcd(g2, x);
          nxt[g1][ng2] = (nxt[g1][ng2] + val) % _mod;
        }
      }
      cur = nxt;
    }

    int ans = 0;
    for (int g = 1; g <= maxV; ++g) {
      ans = (ans + cur[g][g]) % _mod;
    }
    return ans;
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
	"math"
)

const MOD int = 1_000_000_007

func subsequencePairCount(nums []int) int {
	const MAXV = 200
	// dp[ga][gb]
	cur := make([][]int, MAXV+1)
	nxt := make([][]int, MAXV+1)
	for i := 0; i <= MAXV; i++ {
		cur[i] = make([]int, MAXV+1)
		nxt[i] = make([]int, MAXV+1)
	}
	cur[0][0] = 1

	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	for _, x := range nums {
		// reset nxt
		for i := 0; i <= MAXV; i++ {
			for j := 0; j <= MAXV; j++ {
				nxt[i][j] = 0
			}
		}
		for ga := 0; ga <= MAXV; ga++ {
			for gb := 0; gb <= MAXV; gb++ {
				val := cur[ga][gb]
				if val == 0 {
					continue
				}
				// assign to none
				nxt[ga][gb] = (nxt[ga][gb] + val) % MOD

				// assign to A
				newGa := x
				if ga != 0 {
					newGa = gcd(ga, x)
				}
				nxt[newGa][gb] = (nxt[newGa][gb] + val) % MOD

				// assign to B
				newGb := x
				if gb != 0 {
					newGb = gcd(gb, x)
				}
				nxt[ga][newGb] = (nxt[ga][newGb] + val) % MOD
			}
		}
		cur, nxt = nxt, cur
	}

	ans := 0
	for g := 1; g <= MAXV; g++ {
		ans = (ans + cur[g][g]) % MOD
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def subsequence_pair_count(nums)
  max_val = 200
  dp = Array.new(max_val + 1) { Array.new(max_val + 1, 0) }
  dp[0][0] = 1

  nums.each do |x|
    newdp = Array.new(max_val + 1) { Array.new(max_val + 1, 0) }
    (0..max_val).each do |g1|
      row = dp[g1]
      (0..max_val).each do |g2|
        val = row[g2]
        next if val == 0

        # ignore current element
        newdp[g1][g2] = (newdp[g1][g2] + val) % MOD

        # assign to first subsequence
        ng1 = g1.zero? ? x : g1.gcd(x)
        newdp[ng1][g2] = (newdp[ng1][g2] + val) % MOD

        # assign to second subsequence
        ng2 = g2.zero? ? x : g2.gcd(x)
        newdp[g1][ng2] = (newdp[g1][ng2] + val) % MOD
      end
    end
    dp = newdp
  end

  ans = 0
  (1..max_val).each do |g|
    ans = (ans + dp[g][g]) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

    private def gcd(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        x
    }

    def subsequencePairCount(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        val maxVal = nums.max
        var dp = Array.ofDim[Long](maxVal + 1, maxVal + 1)
        dp(0)(0) = 1L

        for (x <- nums) {
            val ndp = Array.ofDim[Long](maxVal + 1, maxVal + 1)
            var g1 = 0
            while (g1 <= maxVal) {
                var g2 = 0
                while (g2 <= maxVal) {
                    val cur = dp(g1)(g2)
                    if (cur != 0L) {
                        // skip the element
                        ndp(g1)(g2) = (ndp(g1)(g2) + cur) % MOD
                        // assign to first subsequence
                        val ng1 = if (g1 == 0) x else gcd(g1, x)
                        ndp(ng1)(g2) = (ndp(ng1)(g2) + cur) % MOD
                        // assign to second subsequence
                        val ng2 = if (g2 == 0) x else gcd(g2, x)
                        ndp(g1)(ng2) = (ndp(g1)(ng2) + cur) % MOD
                    }
                    g2 += 1
                }
                g1 += 1
            }
            dp = ndp
        }

        var ans: Long = 0L
        var g = 1
        while (g <= maxVal) {
            ans = (ans + dp(g)(g)) % MOD
            g += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let max_v = 200usize;
        // dp[g1][g2] where g1,g2 are current GCDs (0 means empty)
        let mut dp = vec![vec![0i64; max_v + 1]; max_v + 1];
        dp[0][0] = 1;
        for &val in nums.iter() {
            let x = val as usize;
            let mut ndp = dp.clone(); // case: ignore current element
            for g1 in 0..=max_v {
                for g2 in 0..=max_v {
                    let cur = dp[g1][g2];
                    if cur == 0 {
                        continue;
                    }
                    // put into seq1
                    let ng1 = if g1 == 0 { x } else { gcd(g1, x) };
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD;
                    // put into seq2
                    let ng2 = if g2 == 0 { x } else { gcd(g2, x) };
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD;
                }
            }
            dp = ndp;
        }
        let mut ans: i64 = 0;
        for g in 1..=max_v {
            ans = (ans + dp[g][g]) % MOD;
        }
        ans as i32
    }
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (subsequence-pair-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((maxv 200)
         (size (+ maxv 1))
         (dp (make-vector size)))
    ;; initialize dp matrix
    (for ([i (in-range size)])
      (vector-set! dp i (make-vector size 0)))
    ;; empty state
    (let ((row0 (vector-ref dp 0)))
      (vector-set! row0 0 1))
    ;; helper to add with modulo
    (define (add! mat i j val)
      (let* ((row (vector-ref mat i))
             (old (vector-ref row j))
             (new (+ old val)))
        (when (>= new MOD) (set! new (- new MOD)))
        (vector-set! row j new)))
    ;; process each element
    (for ([x nums])
      (let ((newdp (make-vector size)))
        (for ([i (in-range size)])
          (vector-set! newdp i (make-vector size 0)))
        (for ([g1 (in-range size)])
          (let ((row-old (vector-ref dp g1)))
            (for ([g2 (in-range size)])
              (define c (vector-ref row-old g2))
              (when (> c 0)
                ;; assign to none
                (add! newdp g1 g2 c)
                ;; assign to group1
                (let ((ng1 (if (= g1 0) x (gcd g1 x))))
                  (add! newdp ng1 g2 c))
                ;; assign to group2
                (let ((ng2 (if (= g2 0) x (gcd g2 x))))
                  (add! newdp g1 ng2 c))))))
        (set! dp newdp)))
    ;; sum states where both groups non‑empty and GCDs equal
    (let ((ans 0))
      (for ([g (in-range 1 size)])
        (define val (vector-ref (vector-ref dp g) g))
        (when (> val 0)
          (set! ans (+ ans val))
          (when (>= ans MOD) (set! ans (- ans MOD)))))
      ans)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec subsequence_pair_count(Nums :: [integer()]) -> integer().
subsequence_pair_count(Nums) ->
    DP0 = #{ {0,0,0} => 1 },
    DPFinal = lists:foldl(
        fun(Num, DPAcc) ->
            NewDP0 = DPAcc,
            maps:fold(
                fun({G1,G2,Mask}, C, Acc) ->
                    % assign to seq1
                    NewMask1 = Mask bor 1,
                    NewG1 = case (Mask band 1) of
                                0 -> Num;
                                _ -> erlang:gcd(G1, Num)
                            end,
                    Key1 = {NewG1, G2, NewMask1},
                    Acc1 = maps:update_with(
                        Key1,
                        fun(Old) -> (Old + C) rem ?MOD end,
                        C rem ?MOD,
                        Acc),
                    % assign to seq2
                    NewMask2 = Mask bor 2,
                    NewG2 = case (Mask band 2) of
                                0 -> Num;
                                _ -> erlang:gcd(G2, Num)
                            end,
                    Key2 = {G1, NewG2, NewMask2},
                    maps:update_with(
                        Key2,
                        fun(Old) -> (Old + C) rem ?MOD end,
                        C rem ?MOD,
                        Acc1)
                end,
                NewDP0,
                DPAcc)
        end,
        DP0,
        Nums),
    Result = maps:fold(
        fun({G1,G2,Mask}, C, Sum) ->
            if Mask == 3, G1 == G2 -> (Sum + C) rem ?MOD;
               true -> Sum
            end
        end,
        0,
        DPFinal),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec subsequence_pair_count(nums :: [integer]) :: integer
  def subsequence_pair_count(nums) do
    # dp map: {gcd_seq1, gcd_seq2} => count of assignments for processed prefix
    init_dp = %{{0, 0} => 1}

    final_dp =
      Enum.reduce(nums, init_dp, fn x, dp ->
        Enum.reduce(dp, dp, fn {{g1, g2}, cnt}, acc ->
          # assign current element to seq1
          ng1 = if g1 == 0, do: x, else: Integer.gcd(g1, x)
          key1 = {ng1, g2}
          val1 = Map.get(acc, key1, 0) + cnt
          acc = Map.put(acc, key1, rem(val1, @mod))

          # assign current element to seq2
          ng2 = if g2 == 0, do: x, else: Integer.gcd(g2, x)
          key2 = {g1, ng2}
          val2 = Map.get(acc, key2, 0) + cnt
          Map.put(acc, key2, rem(val2, @mod))
        end)
      end)

    Enum.reduce(final_dp, 0, fn {{g, g}, cnt}, ans when g != 0 ->
      (ans + cnt) |> rem(@mod)
    end)
  end
end
```
