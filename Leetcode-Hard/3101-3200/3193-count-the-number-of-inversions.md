# 3193. Count the Number of Inversions

## Cpp

```cpp
class Solution {
public:
    int numberOfPermutations(int n, vector<vector<int>>& requirements) {
        const int MOD = 1000000007;
        const int MAXC = 400; // given constraint
        
        vector<int> req(n, -1);
        for (auto &r : requirements) {
            req[r[0]] = r[1];
        }
        
        vector<int> dp(MAXC + 1, 0), ndp(MAXC + 1, 0);
        dp[0] = 1; // empty prefix
        
        for (int len = 1; len <= n; ++len) { // current length
            // prefix sums of previous dp
            vector<int> pref(MAXC + 1, 0);
            long long cur = 0;
            for (int j = 0; j <= MAXC; ++j) {
                cur += dp[j];
                if (cur >= MOD) cur -= MOD;
                pref[j] = (int)cur;
            }
            
            fill(ndp.begin(), ndp.end(), 0);
            int maxInvAdd = len - 1; // new element can add at most len-1 inversions
            for (int j = 0; j <= MAXC; ++j) {
                int left = j - min(j, maxInvAdd);
                long long val = pref[j];
                if (left > 0) {
                    val -= pref[left - 1];
                }
                val %= MOD;
                if (val < 0) val += MOD;
                ndp[j] = (int)val;
            }
            
            // enforce requirement for this prefix length-1 index
            int idx = len - 1;
            if (req[idx] != -1) {
                int target = req[idx];
                for (int j = 0; j <= MAXC; ++j) {
                    if (j != target) ndp[j] = 0;
                }
            }
            
            dp.swap(ndp);
        }
        
        // final answer: only the required count at n-1 remains non-zero
        int finalIdx = n - 1;
        if (req[finalIdx] != -1) {
            return dp[req[finalIdx]];
        } else {
            long long ans = 0;
            for (int v : dp) {
                ans += v;
                if (ans >= MOD) ans -= MOD;
            }
            return (int)ans;
        }
    }
};
```

## Java

```java
class Solution {
    public int numberOfPermutations(int n, int[][] requirements) {
        final int MOD = 1_000_000_007;
        int maxCnt = 0;
        int[] required = new int[n];
        java.util.Arrays.fill(required, -1);
        for (int[] req : requirements) {
            int end = req[0];
            int cnt = req[1];
            required[end] = cnt;
            if (cnt > maxCnt) maxCnt = cnt;
        }
        long[] dpPrev = new long[maxCnt + 1];
        long[] dpCurr = new long[maxCnt + 1];
        dpPrev[0] = 1;
        for (int i = 1; i <= n; i++) {
            long[] cum = new long[maxCnt + 1];
            cum[0] = dpPrev[0];
            for (int j = 1; j <= maxCnt; j++) {
                cum[j] = (cum[j - 1] + dpPrev[j]) % MOD;
            }
            int limit = i - 1;
            for (int j = 0; j <= maxCnt; j++) {
                long val = cum[j];
                int left = j - limit;
                if (left > 0) {
                    val -= cum[left - 1];
                    if (val < 0) val += MOD;
                }
                dpCurr[j] = val % MOD;
            }
            int reqCnt = required[i - 1];
            if (reqCnt != -1) {
                for (int j = 0; j <= maxCnt; j++) {
                    if (j != reqCnt) dpCurr[j] = 0;
                }
            }
            long[] tmp = dpPrev;
            dpPrev = dpCurr;
            dpCurr = tmp;
        }
        int finalCnt = required[n - 1];
        return (int) (dpPrev[finalCnt] % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # map each prefix end index to required inversion count
        req = [-1] * n
        maxInv = 0
        for end, cnt in requirements:
            req[end] = cnt
            if cnt > maxInv:
                maxInv = cnt

        dp = [0] * (maxInv + 1)
        dp[0] = 1  # empty permutation has 0 inversions

        for length in range(1, n + 1):
            new_dp = [0] * (maxInv + 1)

            # prefix sums of previous dp for O(maxInv) transition
            pref = [0] * (maxInv + 2)
            for i in range(maxInv + 1):
                pref[i + 1] = (pref[i] + dp[i]) % MOD

            max_possible = min(maxInv, length * (length - 1) // 2)
            limit_k = length - 1  # maximum new inversions added when inserting the largest element

            for inv in range(0, max_possible + 1):
                left = inv - limit_k
                if left < 0:
                    left = 0
                # sum dp[inv - k] for k=0..min(inv,limit_k)
                new_dp[inv] = (pref[inv + 1] - pref[left]) % MOD

            idx = length - 1
            if req[idx] != -1:
                need = req[idx]
                filtered = [0] * (maxInv + 1)
                if need <= maxInv:
                    filtered[need] = new_dp[need]
                new_dp = filtered

            dp = new_dp

        final_need = req[n - 1]
        return dp[final_need] % MOD
```

## Python3

```python
from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX_INV = 400  # given constraint for cnti
        
        req = {e: c for e, c in requirements}
        
        dp = [0] * (MAX_INV + 1)
        dp[0] = 1  # empty permutation has 0 inversions
        
        for i in range(1, n + 1):
            newdp = [0] * (MAX_INV + 1)
            pref = [0] * (MAX_INV + 1)
            pref[0] = dp[0]
            for k in range(1, MAX_INV + 1):
                pref[k] = (pref[k - 1] + dp[k]) % MOD
            for k in range(MAX_INV + 1):
                val = pref[k]
                if k >= i:
                    val -= pref[k - i]
                newdp[k] = val % MOD
            
            end_idx = i - 1
            if end_idx in req:
                cnt = req[end_idx]
                if cnt > MAX_INV:
                    return 0
                filtered = [0] * (MAX_INV + 1)
                filtered[cnt] = newdp[cnt]
                newdp = filtered
            
            dp = newdp
        
        return sum(dp) % MOD
```

## C

```c
#include <string.h>
#define MOD 1000000007

int numberOfPermutations(int n, int** requirements, int requirementsSize, int* requirementsColSize) {
    const int MAXC = 400;
    int req[305];
    for (int i = 0; i <= n; ++i) req[i] = -1;
    for (int i = 0; i < requirementsSize; ++i) {
        int endi = requirements[i][0];
        int cnti = requirements[i][1];
        req[endi] = cnti;
    }

    static int dpPrev[401], dpCurr[401], pref[402];
    memset(dpPrev, 0, sizeof(dpPrev));
    dpPrev[0] = 1;

    for (int i = 1; i <= n; ++i) {
        /* prefix sums of dpPrev */
        pref[0] = 0;
        for (int j = 0; j <= MAXC; ++j) {
            int v = pref[j] + dpPrev[j];
            if (v >= MOD) v -= MOD;
            pref[j + 1] = v;
        }

        int maxAdd = i - 1;  // new element can add at most i-1 inversions
        for (int j = 0; j <= MAXC; ++j) {
            int left = j - maxAdd;
            if (left < 0) left = 0;
            int val = pref[j + 1] - pref[left];
            if (val < 0) val += MOD;
            dpCurr[j] = val;
        }

        /* apply requirement for prefix length i (index i-1) */
        int idx = i - 1;
        if (req[idx] != -1) {
            int need = req[idx];
            for (int j = 0; j <= MAXC; ++j) {
                if (j != need) dpCurr[j] = 0;
            }
        }

        memcpy(dpPrev, dpCurr, sizeof(dpPrev));
        memset(dpCurr, 0, sizeof(dpCurr));
    }

    int ans = 0;
    if (req[n - 1] != -1) {
        int need = req[n - 1];
        if (need >= 0 && need <= MAXC) ans = dpPrev[need];
        else ans = 0;
    } else {
        for (int j = 0; j <= MAXC; ++j) {
            ans += dpPrev[j];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfPermutations(int n, int[][] requirements) {
        const int MOD = 1000000007;
        var reqMap = new System.Collections.Generic.Dictionary<int, int>();
        int maxC = 0;
        foreach (var r in requirements) {
            int end = r[0];
            int cnt = r[1];
            reqMap[end] = cnt;
            if (cnt > maxC) maxC = cnt;
        }

        int[] dpPrev = new int[maxC + 1];
        dpPrev[0] = 1;

        for (int i = 1; i <= n; i++) {
            int[] dpCurr = new int[maxC + 1];
            long windowSum = 0;
            for (int j = 0; j <= maxC; j++) {
                windowSum += dpPrev[j];
                if (j - i >= 0) {
                    windowSum -= dpPrev[j - i];
                }
                windowSum %= MOD;
                if (windowSum < 0) windowSum += MOD;
                dpCurr[j] = (int)windowSum;
            }

            int endIdx = i - 1;
            if (reqMap.TryGetValue(endIdx, out int requiredCnt)) {
                for (int j = 0; j <= maxC; j++) {
                    if (j != requiredCnt) dpCurr[j] = 0;
                }
            }

            dpPrev = dpCurr;
        }

        if (reqMap.TryGetValue(n - 1, out int finalCnt)) {
            return dpPrev[finalCnt];
        } else {
            long ans = 0;
            foreach (int v in dpPrev) {
                ans += v;
            }
            return (int)(ans % MOD);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} requirements
 * @return {number}
 */
var numberOfPermutations = function(n, requirements) {
    const MOD = 1000000007;
    const MAX_INV = 400; // per constraints
    
    // map prefix length (endi+1) -> required inversion count
    const reqMap = new Map();
    for (const [endi, cnt] of requirements) {
        reqMap.set(endi + 1, cnt);
    }
    
    let dpPrev = new Array(MAX_INV + 1).fill(0);
    dpPrev[0] = 1; // empty permutation
    
    for (let len = 1; len <= n; ++len) {
        const dpCurr = new Array(MAX_INV + 1).fill(0);
        let windowSum = 0;
        for (let inv = 0; inv <= MAX_INV; ++inv) {
            // add dpPrev[inv] to sliding window
            windowSum = (windowSum + dpPrev[inv]) % MOD;
            // remove element that slides out of window size 'len'
            if (inv - len >= 0) {
                windowSum = (windowSum - dpPrev[inv - len] + MOD) % MOD;
            }
            dpCurr[inv] = windowSum;
        }
        // enforce requirement for this prefix length, if any
        if (reqMap.has(len)) {
            const need = reqMap.get(len);
            const filtered = new Array(MAX_INV + 1).fill(0);
            if (need <= MAX_INV) {
                filtered[need] = dpCurr[need];
            }
            // replace dpCurr with filtered version
            for (let i = 0; i <= MAX_INV; ++i) dpCurr[i] = filtered[i];
        }
        dpPrev = dpCurr;
    }
    
    let ans = 0;
    for (const val of dpPrev) {
        ans = (ans + val) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfPermutations(n: number, requirements: number[][]): number {
    const MOD = 1000000007;
    let maxCnt = 0;
    for (const [, cnt] of requirements) {
        if (cnt > maxCnt) maxCnt = cnt;
    }
    const required = new Array(n + 1).fill(-1);
    for (const [endi, cnt] of requirements) {
        required[endi + 1] = cnt;
    }

    let dp: number[] = new Array(maxCnt + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        const ndp: number[] = new Array(maxCnt + 1).fill(0);
        let prefix = 0;
        for (let j = 0; j <= maxCnt; j++) {
            prefix = (prefix + dp[j]) % MOD;
            if (j >= i) {
                prefix = (prefix - dp[j - i] + MOD) % MOD;
            }
            ndp[j] = prefix;
        }
        const req = required[i];
        if (req !== -1) {
            for (let j = 0; j <= maxCnt; j++) {
                if (j !== req) ndp[j] = 0;
            }
        }
        dp = ndp;
    }

    const finalReq = required[n];
    if (finalReq !== -1) {
        return dp[finalReq] ?? 0;
    } else {
        let ans = 0;
        for (const v of dp) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return ans;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $requirements
     * @return Integer
     */
    function numberOfPermutations($n, $requirements) {
        $mod = 1000000007;
        // find maximum required inversion count to limit DP size
        $maxCnt = 0;
        foreach ($requirements as $r) {
            if ($r[1] > $maxCnt) $maxCnt = $r[1];
        }
        $MAX = $maxCnt; // dp dimensions: 0..MAX

        // map end index to required count, -1 means no requirement
        $req = array_fill(0, $n, -1);
        foreach ($requirements as $r) {
            $req[$r[0]] = $r[1];
        }

        // dp for length 0: only 0 inversions
        $dpPrev = array_fill(0, $MAX + 1, 0);
        $dpPrev[0] = 1;

        for ($i = 1; $i <= $n; $i++) {
            $dpCurr = array_fill(0, $MAX + 1, 0);

            // prefix sums of dpPrev
            $pref = array_fill(0, $MAX + 1, 0);
            $sum = 0;
            for ($j = 0; $j <= $MAX; $j++) {
                $sum += $dpPrev[$j];
                if ($sum >= $mod) $sum -= $mod;
                $pref[$j] = $sum;
            }

            // maximum possible inversions with i elements (capped by MAX)
            $maxInvI = min($MAX, intdiv($i * ($i - 1), 2));

            for ($j = 0; $j <= $maxInvI; $j++) {
                $k = min($j, $i - 1);
                $left = $j - $k;
                if ($left > 0) {
                    $val = $pref[$j] - $pref[$left - 1];
                } else {
                    $val = $pref[$j];
                }
                $val %= $mod;
                if ($val < 0) $val += $mod;
                $dpCurr[$j] = $val;
            }

            // apply requirement for prefix ending at index i-1
            $idx = $i - 1;
            if ($req[$idx] != -1) {
                $need = $req[$idx];
                for ($j = 0; $j <= $MAX; $j++) {
                    if ($j != $need) $dpCurr[$j] = 0;
                }
            }

            $dpPrev = $dpCurr;
        }

        // final answer: requirement at end index n-1 must exist per problem statement
        $finalIdx = $n - 1;
        if ($req[$finalIdx] != -1) {
            $cnt = $req[$finalIdx];
            return $cnt <= $MAX ? $dpPrev[$cnt] : 0;
        } else {
            $ans = 0;
            for ($j = 0; $j <= $MAX; $j++) {
                $ans += $dpPrev[$j];
                if ($ans >= $mod) $ans -= $mod;
            }
            return $ans;
        }
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPermutations(_ n: Int, _ requirements: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var reqDict = [Int:Int]()
        var maxK = 0
        for r in requirements {
            let end = r[0]
            let cnt = r[1]
            reqDict[end] = cnt
            if cnt > maxK { maxK = cnt }
        }
        var dpPrev = [Int](repeating: 0, count: maxK + 1)
        dpPrev[0] = 1
        
        for i in 1...n {
            var newDP = [Int](repeating: 0, count: maxK + 1)
            var prefix = 0
            for j in 0...maxK {
                prefix += dpPrev[j]
                if prefix >= MOD { prefix -= MOD }
                if j >= i {
                    prefix -= dpPrev[j - i]
                    if prefix < 0 { prefix += MOD }
                }
                newDP[j] = prefix
            }
            if let need = reqDict[i - 1] {
                if need > maxK { return 0 }
                for j in 0...maxK where j != need {
                    newDP[j] = 0
                }
            }
            dpPrev = newDP
        }
        
        var ans = 0
        for v in dpPrev {
            ans += v
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun numberOfPermutations(n: Int, requirements: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        var maxCnt = 0
        val reqMap = HashMap<Int, Int>()
        for (req in requirements) {
            val len = req[0] + 1 // prefix length
            val cnt = req[1]
            reqMap[len] = cnt
            if (cnt > maxCnt) maxCnt = cnt
        }
        // dp[j]: number of permutations of current length with j inversions
        var dp = LongArray(maxCnt + 1)
        dp[0] = 1L
        for (i in 1..n) {
            val newDp = LongArray(maxCnt + 1)
            var cum = 0L
            for (j in 0..maxCnt) {
                cum += dp[j]
                if (j >= i) {
                    cum -= dp[j - i]
                }
                // keep cum within [0, MOD)
                var v = cum % MOD
                if (v < 0) v += MOD
                newDp[j] = v
            }
            val requiredCnt = reqMap[i]
            if (requiredCnt != null) {
                for (j in 0..maxCnt) {
                    if (j != requiredCnt) newDp[j] = 0L
                }
            }
            dp = newDp
        }
        val finalCnt = reqMap[n] ?: return 0
        return (dp[finalCnt] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPermutations(int n, List<List<int>> requirements) {
    const int MOD = 1000000007;
    final Map<int, int> req = {};
    int maxCnt = 0;
    for (var r in requirements) {
      int end = r[0];
      int cnt = r[1];
      req[end] = cnt;
      if (cnt > maxCnt) maxCnt = cnt;
    }

    List<int> dp = List.filled(maxCnt + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
      List<int> ndp = List.filled(maxCnt + 1, 0);
      int limitInv = i * (i - 1) ~/ 2;
      if (limitInv > maxCnt) limitInv = maxCnt;

      int windowSum = 0;
      for (int j = 0; j <= limitInv; ++j) {
        windowSum += dp[j];
        if (windowSum >= MOD) windowSum -= MOD;
        if (j - i >= 0) {
          windowSum -= dp[j - i];
          if (windowSum < 0) windowSum += MOD;
        }
        ndp[j] = windowSum;
      }

      int endIdx = i - 1;
      if (req.containsKey(endIdx)) {
        int requiredCnt = req[endIdx]!;
        for (int j = 0; j <= maxCnt; ++j) {
          if (j != requiredCnt) ndp[j] = 0;
        }
      }

      dp = ndp;
    }

    int finalCnt = req[n - 1]!;
    return dp[finalCnt];
  }
}
```

## Golang

```go
func numberOfPermutations(n int, requirements [][]int) int {
	const MOD int = 1000000007
	maxInv := 400
	totalMax := n * (n - 1) / 2
	if totalMax < maxInv {
		maxInv = totalMax
	}
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, maxInv+1)
	}
	dp[0][0] = 1

	reqMap := make(map[int]int)
	for _, r := range requirements {
		reqMap[r[0]] = r[1]
	}

	for i := 1; i <= n; i++ {
		for j := 0; j <= maxInv; j++ {
			val := dp[i-1][j]
			if j > 0 {
				val += dp[i][j-1]
				if val >= MOD {
					val -= MOD
				}
			}
			if j >= i {
				val -= dp[i-1][j-i]
				if val < 0 {
					val += MOD
				}
			}
			dp[i][j] = val
		}
		if cnt, ok := reqMap[i-1]; ok {
			for j := 0; j <= maxInv; j++ {
				if j != cnt {
					dp[i][j] = 0
				}
			}
		}
	}

	ans := 0
	for j := 0; j <= maxInv; j++ {
		ans += dp[n][j]
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
def number_of_permutations(n, requirements)
  mod = 1_000_000_007
  max_c = 0
  req = Array.new(n + 1, -1) # length i => requirement for prefix of size i
  requirements.each do |endi, cnt|
    len = endi + 1
    req[len] = cnt
    max_c = cnt if cnt > max_c
  end

  dp_prev = Array.new(max_c + 1, 0)
  dp_prev[0] = 1

  (1..n).each do |i|
    max_inv_i = i * (i - 1) / 2
    limit = [max_c, max_inv_i].min

    # prefix sums of dp_prev up to 'limit'
    pref = Array.new(limit + 1, 0)
    sum = 0
    j = 0
    while j <= limit
      sum += dp_prev[j]
      sum -= mod if sum >= mod
      pref[j] = sum
      j += 1
    end

    dp_curr = Array.new(max_c + 1, 0)
    j = 0
    while j <= limit
      left = j - i
      val = pref[j]
      val -= pref[left] if left >= 0
      val += mod if val < 0
      dp_curr[j] = val % mod
      j += 1
    end

    # enforce requirement for this length, if any
    if req[i] != -1
      needed = req[i]
      return 0 if needed > limit
      filtered = Array.new(max_c + 1, 0)
      filtered[needed] = dp_curr[needed]
      dp_curr = filtered
    end

    dp_prev = dp_curr
  end

  final_cnt = req[n]
  final_cnt == -1 ? 0 : dp_prev[final_cnt] % mod
end
```

## Scala

```scala
object Solution {
  def numberOfPermutations(n: Int, requirements: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val maxInv = 400
    val req = Array.fill[Int](n)(-1)
    for (r <- requirements) {
      val endi = r(0)
      val cnti = r(1)
      req(endi) = cnti
    }

    var dpPrev = new Array[Int](maxInv + 1)
    dpPrev(0) = 1

    for (i <- 1 to n) {
      val dpCurr = new Array[Int](maxInv + 1)
      var prefix: Long = 0L
      // sliding window of size i over dpPrev
      for (j <- 0 to maxInv) {
        prefix = (prefix + dpPrev(j)) % MOD
        if (j - i >= 0) {
          prefix = (prefix - dpPrev(j - i) + MOD) % MOD
        }
        dpCurr(j) = prefix.toInt
      }

      val requiredCnt = req(i - 1)
      if (requiredCnt != -1) {
        for (j <- 0 to maxInv) {
          if (j != requiredCnt) dpCurr(j) = 0
        }
      }
      dpPrev = dpCurr
    }

    val finalReq = req(n - 1)
    if (finalReq == -1) {
      var ans: Long = 0L
      for (v <- dpPrev) ans = (ans + v) % MOD
      ans.toInt
    } else {
      dpPrev(finalReq)
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_permutations(n: i32, requirements: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        // map end index to required inversion count
        let mut req: Vec<Option<usize>> = vec![None; n_usize];
        let mut max_cnt: usize = 0;
        for r in requirements.iter() {
            let endi = r[0] as usize;
            let cnti = r[1] as usize;
            req[endi] = Some(cnti);
            if cnti > max_cnt {
                max_cnt = cnti;
            }
        }

        // dp vectors: cur[j] = number of permutations of current length with j inversions
        let mut cur = vec![0i64; max_cnt + 1];
        cur[0] = 1;

        for i in 1..=n_usize {
            let limit = std::cmp::min(i * (i - 1) / 2, max_cnt);
            // prefix sums of previous dp
            let mut pref = vec![0i64; max_cnt + 1];
            pref[0] = cur[0];
            for j in 1..=max_cnt {
                pref[j] = (pref[j - 1] + cur[j]) % MOD;
            }
            // compute next dp
            let mut next = vec![0i64; max_cnt + 1];
            for j in 0..=limit {
                let left = if j >= i { j - i } else { 0 };
                let mut val = pref[j];
                if left > 0 {
                    val = (val + MOD - pref[left - 1]) % MOD;
                }
                next[j] = val;
            }
            // enforce requirement at prefix length i (index i-1)
            if let Some(cnt) = req[i - 1] {
                if cnt > limit {
                    return 0;
                }
                for j in 0..=max_cnt {
                    if j != cnt {
                        next[j] = 0;
                    }
                }
            }
            cur = next;
        }

        // final answer: requirement at full length must exist per problem statement
        let ans = match req[n_usize - 1] {
            Some(cnt) => cur[cnt],
            None => cur.iter().fold(0i64, |acc, &v| (acc + v) % MOD),
        };
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (number-of-permutations n requirements)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((maxC (apply max (map second requirements)))
         (req (make-vector n -1))) ; -1 means no requirement
    (for ([pair requirements])
      (vector-set! req (first pair) (second pair)))
    (define dpPrev (make-vector (+ maxC 1) 0))
    (vector-set! dpPrev 0 1)
    (let loop ((len 1) (dpPrev dpPrev))
      (if (> len n)
          (let ((finalCnt (vector-ref req (- n 1))))
            (modulo (vector-ref dpPrev finalCnt) MOD))
          (let* ((limit maxC)
                 (dpCurr (make-vector (+ maxC 1) 0))
                 (pref (make-vector (+ maxC 1) 0)))
            ;; prefix sums of dpPrev
            (let inner ((j 0) (acc 0))
              (when (<= j limit)
                (set! acc (+ acc (vector-ref dpPrev j)))
                (when (>= acc MOD) (set! acc (- acc MOD)))
                (vector-set! pref j acc)
                (inner (add1 j) acc)))
            ;; compute dpCurr using prefix sums
            (let inner ((j 0))
              (when (<= j limit)
                (define left (if (>= (- j len) 0)
                                 (vector-ref pref (- j len))
                                 0))
                (define val (- (vector-ref pref j) left))
                (when (< val 0) (set! val (+ val MOD)))
                (vector-set! dpCurr j (modulo val MOD))
                (inner (add1 j))))
            ;; enforce requirement at this prefix if any
            (let ((reqCnt (vector-ref req (- len 1))))
              (when (not (= reqCnt -1))
                (for ([j limit])
                  (unless (= j reqCnt)
                    (vector-set! dpCurr j 0)))))
            (loop (add1 len) dpCurr))))))

;; Contract
(provide number-of-permutations)
```

## Erlang

```erlang
-module(solution).
-export([number_of_permutations/2]).

-define(MOD, 1000000007).

-spec number_of_permutations(N :: integer(), Requirements :: [[integer()]]) -> integer().
number_of_permutations(N, Requirements) ->
    ReqMap = maps:from_list([{End, Cnt} || [End, Cnt] <- Requirements]),
    MaxCnt = lists:max([Cnt || [_E, Cnt] <- Requirements]),
    InitDP = [1] ++ lists:duplicate(MaxCnt, 0),
    Indexes = lists:seq(0, MaxCnt),
    FinalDP = dp_loop(1, N, InitDP, ReqMap, MaxCnt, Indexes),
    case maps:find(N - 1, ReqMap) of
        {ok, Cnt} when Cnt =< MaxCnt ->
            lists:nth(Cnt + 1, FinalDP);
        _ -> 0
    end.

dp_loop(I, N, DP, _ReqMap, _MaxCnt, _Indexes) when I > N ->
    DP;
dp_loop(I, N, Prev, ReqMap, MaxCnt, Indexes) ->
    PrefixList = prefix(Prev),
    PrefixTuple = list_to_tuple(PrefixList),
    NewDP = build_new(Indexes, PrefixTuple, I),
    case maps:find(I - 1, ReqMap) of
        {ok, Cnt} when Cnt =< MaxCnt ->
            Filtered = [if Idx == Cnt -> Val else 0 end || {Idx, Val} <- lists:zip(Indexes, NewDP)],
            dp_loop(I + 1, N, Filtered, ReqMap, MaxCnt, Indexes);
        {ok, _Cnt} -> % required count exceeds MaxCnt => impossible
            Zero = lists:duplicate(MaxCnt + 1, 0),
            dp_loop(N + 1, N, Zero, ReqMap, MaxCnt, Indexes);
        error ->
            dp_loop(I + 1, N, NewDP, ReqMap, MaxCnt, Indexes)
    end.

prefix(List) ->
    {RevPref, _} = lists:foldl(
        fun(Val, {Acc, Sum}) ->
                NewSum = (Sum + Val) rem ?MOD,
                {[NewSum | Acc], NewSum}
        end,
        {[], 0},
        List),
    lists:reverse(RevPref).

build_new([], _PrefixTuple, _I) -> [];
build_new([J | Rest], PrefixTuple, I) ->
    PrefJ = element(J + 1, PrefixTuple),
    Sub = if J >= I -> element(J - I + 1, PrefixTuple) else 0 end,
    Val = (PrefJ - Sub + ?MOD) rem ?MOD,
    [Val | build_new(Rest, PrefixTuple, I)].
```

## Elixir

```elixir
defmodule Solution do
  @modulus 1_000_000_007

  def number_of_permutations(n, requirements) do
    max_c = 400

    # requirement array indexed by prefix length (size)
    req_arr =
      :array.new(n + 1, default: -1)
      |> Enum.reduce(requirements, fn [endi, cnti], acc ->
        :array.set(endi + 1, cnti, acc)
      end)

    # factorials and inverse factorials
    fact = build_fact_tuple(n)
    inv_fact = build_inv_fact_tuple(fact, n)

    binom = fn a, b ->
      if b < 0 or b > a do
        0
      else
        rem(elem(fact, a) * elem(inv_fact, b) |> rem(@modulus) *
              elem(inv_fact, a - b), @modulus)
      end
    end

    # precompute ways[i][g] for i = 0..n-1 , g = 0..i
    ways =
      Enum.map(0..(n - 1), fn i ->
        glist =
          Enum.map(0..i, fn g ->
            sum =
              Enum.reduce(0..(n - 1), 0, fn r, acc ->
                term = rem(binom.(n - 1 - r, g) * binom.(r, i - g), @modulus)
                rem(acc + term, @modulus)
              end)

            sum
          end)

        List.to_tuple(glist)
      end)

    # dp arrays as Erlang :array for efficiency
    dp_cur = :array.new(max_c + 1, default: 0) |> :array.set(0, 1)

    dp_cur =
      Enum.reduce(0..(n - 1), dp_cur, fn i, cur_dp ->
        ways_i = Enum.at(ways, i)
        next_dp = :array.new(max_c + 1, default: 0)

        # iterate over possible current inversion counts
        next_dp =
          Enum.reduce(0..max_c, next_dp, fn j, ndp ->
            val = :array.get(j, cur_dp)

            if val != 0 do
              Enum.reduce(0..i, ndp, fn g, acc_ndp ->
                newj = j + g

                if newj <= max_c do
                  add = rem(val * elem(ways_i, g), @modulus)
                  cur = :array.get(newj, acc_ndp)
                  :array.set(newj, rem(cur + add, @modulus), acc_ndp)
                else
                  acc_ndp
                end
              end)
            else
              ndp
            end
          end)

        # apply requirement for prefix size i+1 if exists
        req_cnt = :array.get(i + 1, req_arr)

        if req_cnt != -1 do
          keep_val = :array.get(req_cnt, next_dp)
          :array.new(max_c + 1, default: 0) |> :array.set(req_cnt, keep_val)
        else
          next_dp
        end
      end)

    final_req = :array.get(n, req_arr)
    :array.get(final_req, dp_cur)
  end

  # build factorial tuple up to n
  defp build_fact_tuple(n) do
    list =
      Enum.reduce(0..n, [], fn i, acc ->
        val =
          if i == 0 do
            1
          else
            prev = List.last(acc)
            rem(prev * i, @modulus)
          end

        acc ++ [val]
      end)

    List.to_tuple(list)
  end

  # build inverse factorial tuple using Fermat's little theorem
  defp build_inv_fact_tuple(fact, n) do
    inv_n = pow_mod(elem(fact, n), @modulus - 2)

    list =
      Enum.reduce((n - 1)..0, [inv_n], fn i, acc ->
        next_val = rem(hd(acc) * (i + 1), @modulus)
        [next_val | acc]
      end)

    List.to_tuple(list)
  end

  # fast modular exponentiation
  defp pow_mod(_base, 0), do: 1

  defp pow_mod(base, exp) when rem(exp, 2) == 0 do
    half = pow_mod(rem(base * base, @modulus), div(exp, 2))
    half
  end

  defp pow_mod(base, exp) do
    half = pow_mod(base, div(exp, 2))
    rem(half * half * base, @modulus)
  end
end
```
