# 3352. Count K-Reducible Numbers Less Than N

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    int countKReducibleNumbers(string s, int k) {
        int len = s.size();
        // precompute combinations C[n][r] modulo MOD
        vector<vector<int>> C(len + 1, vector<int>(len + 1, 0));
        for (int i = 0; i <= len; ++i) {
            C[i][0] = C[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
            }
        }

        // steps[x]: number of operations to reach 1 from x
        vector<int> steps(len + 1, -1);
        function<int(int)> calc = [&](int x) -> int {
            if (x == 1) return 0;
            if (steps[x] != -1) return steps[x];
            int pc = __builtin_popcount(x);
            steps[x] = 1 + calc(pc);
            return steps[x];
        };
        for (int i = 1; i <= len; ++i) calc(i);

        // good popcounts: steps[p] <= k-1
        vector<int> goodList;
        int limit = k - 1;
        for (int p = 1; p <= len; ++p) {
            if (steps[p] <= limit) goodList.push_back(p);
        }

        long long ans = 0;
        int onesSoFar = 0;
        for (int i = 0; i < len; ++i) {
            if (s[i] == '1') {
                int remaining = len - i - 1;
                // set this bit to 0, prefix matches so far
                for (int totalPop : goodList) {
                    int needOnesInSuffix = totalPop - onesSoFar;
                    if (needOnesInSuffix < 0 || needOnesInSuffix > remaining) continue;
                    ans += C[remaining][needOnesInSuffix];
                    if (ans >= MOD) ans -= MOD;
                }
                ++onesSoFar; // keep this bit as 1 for further prefix
            }
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;

    public int countKReducibleNumbers(String s, int k) {
        int L = s.length();
        int maxBits = L; // maximum possible popcount for numbers < n
        int[] steps = new int[maxBits + 1];
        Arrays.fill(steps, -2);
        steps[0] = Integer.MAX_VALUE / 2; // unreachable
        steps[1] = 0;
        for (int i = 2; i <= maxBits; i++) {
            computeSteps(i, steps);
        }

        boolean[] good = new boolean[maxBits + 1];
        int limit = k - 1;
        for (int i = 0; i <= maxBits; i++) {
            if (steps[i] <= limit) {
                good[i] = true;
            }
        }

        long[] curTight = new long[maxBits + 1];
        long[] curLoose = new long[maxBits + 1];
        curTight[0] = 1;

        for (int pos = 0; pos < L; pos++) {
            int bit = s.charAt(pos) - '0';
            long[] nextTight = new long[maxBits + 1];
            long[] nextLoose = new long[maxBits + 1];

            for (int cnt = 0; cnt <= pos; cnt++) {
                long valT = curTight[cnt];
                if (valT != 0) {
                    // place 0
                    if (bit == 0) {
                        nextTight[cnt] = (nextTight[cnt] + valT) % MOD;
                    } else {
                        nextLoose[cnt] = (nextLoose[cnt] + valT) % MOD;
                    }
                    // place 1 if allowed
                    if (bit == 1) {
                        nextTight[cnt + 1] = (nextTight[cnt + 1] + valT) % MOD;
                    }
                }

                long valL = curLoose[cnt];
                if (valL != 0) {
                    // place 0
                    nextLoose[cnt] = (nextLoose[cnt] + valL) % MOD;
                    // place 1
                    nextLoose[cnt + 1] = (nextLoose[cnt + 1] + valL) % MOD;
                }
            }

            curTight = nextTight;
            curLoose = nextLoose;
        }

        long ans = 0;
        for (int cnt = 0; cnt <= maxBits; cnt++) {
            if (good[cnt]) {
                ans += curTight[cnt];
                if (ans >= MOD) ans -= MOD;
                ans += curLoose[cnt];
                if (ans >= MOD) ans -= MOD;
            }
        }

        return (int) (ans % MOD);
    }

    private int computeSteps(int x, int[] steps) {
        if (steps[x] != -2) return steps[x];
        int pc = Integer.bitCount(x);
        steps[x] = 1 + computeSteps(pc, steps);
        return steps[x];
    }
}
```

## Python

```python
class Solution(object):
    def countKReducibleNumbers(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        L = len(s)

        # precompute steps needed to reach 1 for numbers up to L
        max_t = L
        steps = [0] * (max_t + 1)   # steps[t]: operations to turn t into 1
        for t in range(2, max_t + 1):
            x = t
            cnt = 0
            while x != 1:
                x = bin(x).count('1')
                cnt += 1
            steps[t] = cnt

        # allowed popcounts for numbers >1 : steps[popcnt] <= k-1
        limit = k - 1
        allowed = set()
        for t in range(1, max_t + 1):
            if steps[t] <= limit:
                allowed.add(t)

        # digit DP over binary string s (count numbers < n)
        dp_eq = [0] * (L + 1)   # tight == True
        dp_lt = [0] * (L + 1)   # tight == False
        dp_eq[0] = 1

        for i, ch in enumerate(s):
            bit_limit = int(ch)
            ndp_eq = [0] * (L + 1)
            ndp_lt = [0] * (L + 1)

            max_ones_sofar = i  # at most i ones have been placed so far
            for cnt in range(max_ones_sofar + 1):
                val_lt = dp_lt[cnt]
                if val_lt:
                    # already less, can place 0 or 1
                    ndp_lt[cnt] = (ndp_lt[cnt] + val_lt) % MOD          # put 0
                    ndp_lt[cnt + 1] = (ndp_lt[cnt + 1] + val_lt) % MOD  # put 1

                val_eq = dp_eq[cnt]
                if not val_eq:
                    continue
                # tight case, can only use bits up to bit_limit
                for b in (0, 1):
                    if b > bit_limit:
                        break
                    new_cnt = cnt + b
                    if b == bit_limit:   # stays equal
                        ndp_eq[new_cnt] = (ndp_eq[new_cnt] + val_eq) % MOD
                    else:                # becomes less
                        ndp_lt[new_cnt] = (ndp_lt[new_cnt] + val_eq) % MOD

            dp_eq, dp_lt = ndp_eq, ndp_lt

        ans = 0
        for pc in allowed:
            if pc == 0:
                continue
            ans = (ans + dp_lt[pc]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        L = len(s)

        # precompute binomial coefficients modulo MOD
        C = [[0] * (L + 1) for _ in range(L + 1)]
        for i in range(L + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        # steps needed to reduce a number x (<=L) to 1 by popcount iterations
        INF = 10**9
        steps = [INF] * (L + 1)
        if L >= 1:
            steps[1] = 0
        for i in range(2, L + 1):
            pc = bin(i).count('1')
            steps[i] = 1 + steps[pc]

        # allowed popcounts: after first operation we get p,
        # need remaining steps <= k-1 to reach 1
        allowed = [p for p in range(1, L + 1) if steps[p] <= k - 1]

        def count_less_than_n(p: int) -> int:
            """count numbers x with popcount == p and 0 <= x < n (binary string s)."""
            ans = 0
            need = p
            for i, ch in enumerate(s):
                if ch == '1':
                    rem = L - i - 1
                    if need <= rem:
                        ans = (ans + C[rem][need]) % MOD
                    need -= 1
                    if need < 0:
                        break
            # do not include n itself
            return ans

        total = 0
        for p in allowed:
            total = (total + count_less_than_n(p)) % MOD
        return total
```

## C

```c
#include <string.h>
#define MOD 1000000007

int countKReducibleNumbers(char* s, int k) {
    int len = strlen(s);
    int maxCnt = len;

    /* steps[i] = number of operations to reduce i to 1 */
    int steps[801];
    for (int i = 0; i <= maxCnt; ++i) steps[i] = 100;   // large sentinel
    steps[1] = 0;
    for (int i = 2; i <= maxCnt; ++i) {
        int pc = __builtin_popcount(i);
        steps[i] = 1 + steps[pc];
    }

    /* allowed popcounts: after first operation we need remaining steps ≤ k-1 */
    char allowed[801] = {0};
    for (int cnt = 1; cnt <= maxCnt; ++cnt) {
        if (steps[cnt] <= k - 1) allowed[cnt] = 1;
    }

    static int dp[2][801];
    static int ndp[2][801];
    memset(dp, 0, sizeof(dp));
    dp[1][0] = 1;   // tight=1, zero ones so far

    for (int pos = 0; pos < len; ++pos) {
        memset(ndp, 0, sizeof(ndp));
        int limit = s[pos] - '0';
        for (int tight = 0; tight <= 1; ++tight) {
            int maxBit = tight ? limit : 1;
            for (int cnt = 0; cnt <= maxCnt; ++cnt) {
                int val = dp[tight][cnt];
                if (!val) continue;

                /* put 0 */
                {
                    int nt = (tight && 0 == limit) ? 1 : 0;
                    ndp[nt][cnt] += val;
                    if (ndp[nt][cnt] >= MOD) ndp[nt][cnt] -= MOD;
                }
                /* put 1 if allowed */
                if (maxBit == 1) {
                    int nt = (tight && 1 == limit) ? 1 : 0;
                    ndp[nt][cnt + 1] += val;
                    if (ndp[nt][cnt + 1] >= MOD) ndp[nt][cnt + 1] -= MOD;
                }
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }

    long long ans = 0;
    for (int cnt = 1; cnt <= maxCnt; ++cnt) {
        if (allowed[cnt]) {
            ans += dp[0][cnt];
        }
    }
    ans %= MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    private const int MOD = 1000000007;
    public int CountKReducibleNumbers(string s, int k) {
        int L = s.Length;
        // Precompute combinations C[n][r] modulo MOD
        long[,] comb = new long[L + 1, L + 1];
        for (int i = 0; i <= L; i++) {
            comb[i, 0] = comb[i, i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i, j] = (comb[i - 1, j - 1] + comb[i - 1, j]) % MOD;
            }
        }

        // Memoization for steps to reach 1
        int maxVal = Math.Max(L, 1000);
        int[] memo = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) memo[i] = -1;
        memo[1] = 0;

        int Steps(int x) {
            if (memo[x] != -1) return memo[x];
            int pc = BitOperations.PopCount((uint)x);
            memo[x] = 1 + Steps(pc);
            return memo[x];
        }

        // Determine allowed popcount values
        bool[] allowed = new bool[L + 1];
        for (int c = 1; c <= L; c++) {
            if (Steps(c) <= k - 1) allowed[c] = true;
        }

        long ans = 0;
        int onesSoFar = 0;
        for (int i = 0; i < L; i++) {
            if (s[i] == '1') {
                int remaining = L - i - 1;
                for (int c = 1; c <= L; c++) {
                    if (!allowed[c]) continue;
                    int need = c - onesSoFar;
                    if (need < 0 || need > remaining) continue;
                    ans += comb[remaining, need];
                    if (ans >= MOD) ans -= MOD;
                }
                onesSoFar++;
            }
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKReducibleNumbers = function(s, k) {
    const MOD = 1000000007;
    const L = s.length;
    const bits = Array.from(s, ch => ch === '1' ? 1 : 0);
    
    // precompute steps needed to reach 1 for popcount values up to L
    const steps = new Array(L + 1).fill(0);
    steps[1] = 0;
    const popcnt = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    for (let c = 2; c <= L; ++c) {
        steps[c] = 1 + steps[popcnt(c)];
    }
    
    // allowed popcount values where total operations <= k
    const allowed = new Set();
    for (let c = 1; c <= L; ++c) {
        if (steps[c] <= k - 1) allowed.add(c);
    }
    
    // DP: cur[count][tight]
    let cur = Array.from({length: L + 1}, () => [0, 0]);
    cur[0][1] = 1;
    
    for (let i = 0; i < L; ++i) {
        const next = Array.from({length: L + 1}, () => [0, 0]);
        for (let cnt = 0; cnt <= i; ++cnt) {
            for (let tight = 0; tight <= 1; ++tight) {
                const val = cur[cnt][tight];
                if (!val) continue;
                const limit = tight ? bits[i] : 1;
                for (let b = 0; b <= limit; ++b) {
                    const ntight = (tight && b === bits[i]) ? 1 : 0;
                    const ncnt = cnt + b;
                    next[ncnt][ntight] = (next[ncnt][ntight] + val) % MOD;
                }
            }
        }
        cur = next;
    }
    
    let ans = 0;
    for (let cnt = 1; cnt <= L; ++cnt) {
        if (allowed.has(cnt)) {
            ans = (ans + cur[cnt][0]) % MOD; // tight == 0 ensures number < n
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countKReducibleNumbers(s: string, k: number): number {
    const MOD = 1000000007;
    const n = s.length;

    // Precompute combinations C[i][j] modulo MOD
    const C: number[][] = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    C[0][0] = 1;
    for (let i = 1; i <= n; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    // cnt[c] = number of integers x (0 <= x < N) with popcount(x) == c
    const cnt: number[] = new Array(n + 1).fill(0);
    let onesSoFar = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] === '1') {
            const rem = n - i - 1;
            // set this bit to 0, remaining bits can have any distribution
            for (let c = onesSoFar; c <= n; c++) {
                const need = c - onesSoFar;
                if (need > rem) break;
                cnt[c] = (cnt[c] + C[rem][need]) % MOD;
            }
            onesSoFar++;
        }
    }

    // stepsNeeded[c]: number of operations to reduce a number with popcount=c to 1
    const stepsNeeded: number[] = new Array(n + 1).fill(0);
    stepsNeeded[0] = Number.MAX_SAFE_INTEGER; // unused
    if (n >= 1) stepsNeeded[1] = 0;
    for (let c = 2; c <= n; c++) {
        let x = c, pc = 0;
        while (x) {
            pc += x & 1;
            x >>= 1;
        }
        stepsNeeded[c] = 1 + stepsNeeded[pc];
    }

    const limit = k - 1;
    let ans = 0;
    for (let c = 1; c <= n; c++) {
        if (stepsNeeded[c] <= limit) {
            ans = (ans + cnt[c]) % MOD;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function countKReducibleNumbers($s, $k) {
        $mod = 1000000007;
        $len = strlen($s);
        // binomial coefficients C[n][r] modulo mod
        $C = array_fill(0, $len + 1, []);
        $C[0][0] = 1;
        for ($i = 1; $i <= $len; $i++) {
            $C[$i][0] = 1;
            $C[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $C[$i][$j] = ($C[$i - 1][$j - 1] + $C[$i - 1][$j]) % $mod;
            }
        }

        // popcount for numbers up to len
        $popcnt = array_fill(0, $len + 1, 0);
        for ($i = 0; $i <= $len; $i++) {
            $cnt = 0;
            $tmp = $i;
            while ($tmp > 0) {
                $cnt += $tmp & 1;
                $tmp >>= 1;
            }
            $popcnt[$i] = $cnt;
        }

        // steps to reach 1 by repeatedly taking popcount
        $steps = array_fill(0, $len + 1, -1);
        $steps[1] = 0;
        for ($i = 2; $i <= $len; $i++) {
            if ($steps[$i] != -1) continue;
            $stack = [];
            $cur = $i;
            while ($steps[$cur] == -1) {
                $stack[] = $cur;
                if ($cur == 1) { $steps[1] = 0; break; }
                $cur = $popcnt[$cur];
            }
            while (!empty($stack)) {
                $node = array_pop($stack);
                $next = $popcnt[$node];
                $steps[$node] = 1 + $steps[$next];
            }
        }

        // allowed popcount values (after first operation) such that steps <= k-1
        $allowed = [];
        $limit = $k - 1;
        for ($i = 1; $i <= $len; $i++) {
            if ($steps[$i] <= $limit) {
                $allowed[] = $i;
            }
        }

        // digit DP counting numbers < n with popcount in allowed set
        $ans = 0;
        $onesSoFar = 0;
        for ($idx = 0; $idx < $len; $idx++) {
            if ($s[$idx] === '1') {
                $remaining = $len - $idx - 1;
                foreach ($allowed as $target) {
                    $need = $target - $onesSoFar;
                    if ($need >= 0 && $need <= $remaining) {
                        $ans = ($ans + $C[$remaining][$need]) % $mod;
                    }
                }
                $onesSoFar++;
            }
        }

        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countKReducibleNumbers(_ s: String, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let bits = s.map { $0 == "1" ? 1 : 0 }
        let L = bits.count
        
        // Precompute steps to reach 1 for values up to L
        var memo = Array(repeating: -1, count: L + 1)
        func steps(_ x: Int) -> Int {
            if x == 1 { return 0 }
            if x == 0 { return 100 } // unreachable large value
            if memo[x] != -1 { return memo[x] }
            let pc = x.nonzeroBitCount
            let res = 1 + steps(pc)
            memo[x] = res
            return res
        }
        
        var good = Array(repeating: false, count: L + 1)
        if k > 0 {
            for p in 0...L {
                if steps(p) <= k - 1 {
                    good[p] = true
                }
            }
        }
        
        // DP: dpTight0 -> already less, dpTight1 -> still equal so far
        var dpLess = Array(repeating: 0, count: L + 1)
        var dpEqual = Array(repeating: 0, count: L + 1)
        dpEqual[0] = 1
        
        for i in 0..<L {
            let limitBit = bits[i]
            var ndpLess = Array(repeating: 0, count: L + 1)
            var ndpEqual = Array(repeating: 0, count: L + 1)
            for cnt in 0...L {
                let valLess = dpLess[cnt]
                if valLess != 0 {
                    // choose 0
                    ndpLess[cnt] = (ndpLess[cnt] + valLess) % MOD
                    // choose 1
                    if cnt + 1 <= L {
                        ndpLess[cnt + 1] = (ndpLess[cnt + 1] + valLess) % MOD
                    }
                }
                let valEqual = dpEqual[cnt]
                if valEqual != 0 {
                    if limitBit == 0 {
                        // can only put 0, stay equal
                        ndpEqual[cnt] = (ndpEqual[cnt] + valEqual) % MOD
                    } else { // limitBit == 1
                        // put 0 -> becomes less
                        ndpLess[cnt] = (ndpLess[cnt] + valEqual) % MOD
                        // put 1 -> stay equal
                        if cnt + 1 <= L {
                            ndpEqual[cnt + 1] = (ndpEqual[cnt + 1] + valEqual) % MOD
                        }
                    }
                }
            }
            dpLess = ndpLess
            dpEqual = ndpEqual
        }
        
        var ans = 0
        for cnt in 0...L {
            if good[cnt] {
                ans += dpLess[cnt]
                if ans >= MOD { ans -= MOD }
            }
        }
        return ans % MOD
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun countKReducibleNumbers(s: String, k: Int): Int {
        val nBits = s.length
        // precompute steps needed to reach 1 for values up to nBits
        val memo = IntArray(nBits + 1) { -1 }
        fun steps(v: Int): Int {
            if (v == 1) return 0
            var res = memo[v]
            if (res != -1) return res
            val pc = Integer.bitCount(v)
            res = 1 + steps(pc)
            memo[v] = res
            return res
        }
        for (i in 1..nBits) {
            steps(i)
        }

        // dp[countOnes][tight] -> ways
        var dp = Array(nBits + 1) { LongArray(2) }
        dp[0][1] = 1L

        for (idx in s.indices) {
            val ndp = Array(nBits + 1) { LongArray(2) }
            val limitBit = s[idx] - '0'
            for (cnt in 0..nBits) {
                for (tight in 0..1) {
                    val cur = dp[cnt][tight]
                    if (cur == 0L) continue
                    val maxB = if (tight == 1) limitBit else 1
                    for (b in 0..maxB) {
                        val ncnt = cnt + b
                        if (ncnt > nBits) continue
                        val ntight = if (tight == 1 && b == maxB) 1 else 0
                        ndp[ncnt][ntight] = (ndp[ncnt][ntight] + cur) % MOD
                    }
                }
            }
            dp = ndp
        }

        var ans = 0L
        val allowedSteps = k - 1
        for (t in 1..nBits) {
            if (memo[t] <= allowedSteps) {
                ans = (ans + dp[t][0]) % MOD   // tight==0 means strictly less than n
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int MOD = 1000000007;

  int countKReducibleNumbers(String s, int k) {
    int n = s.length;
    // Precompute combinations C[i][j] modulo MOD
    List<List<int>> comb = List.generate(n + 1, (_) => List.filled(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
      comb[i][0] = comb[i][i] = 1;
      for (int j = 1; j < i; ++j) {
        comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
      }
    }

    // Memoization for steps needed to reduce a number to 1
    List<int> memo = List.filled(n + 1, -1);
    int popcnt(int x) {
      int cnt = 0;
      while (x > 0) {
        cnt += x & 1;
        x >>= 1;
      }
      return cnt;
    }

    int steps(int x) {
      if (x == 1) return 0;
      if (memo[x] != -1) return memo[x];
      int pc = popcnt(x);
      memo[x] = 1 + steps(pc);
      return memo[x];
    }

    // Determine allowed counts of set bits
    List<int> allowed = [];
    for (int c = 1; c <= n; ++c) {
      if (steps(c) <= k - 1) allowed.add(c);
    }

    int countWithOnes(int target) {
      int ans = 0;
      int onesSoFar = 0;
      for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
          int rem = n - i - 1;
          int need = target - onesSoFar;
          if (need >= 0 && need <= rem) {
            ans = (ans + comb[rem][need]) % MOD;
          }
          onesSoFar++;
          if (onesSoFar > target) break;
        }
      }
      // Do not include n itself; we only count numbers strictly less than n.
      return ans;
    }

    int result = 0;
    for (int c in allowed) {
      result = (result + countWithOnes(c)) % MOD;
    }
    return result;
  }
}
```

## Golang

```go
import "math/bits"

const MOD = 1000000007

func countKReducibleNumbers(s string, k int) int {
	n := len(s)

	// binomial coefficients C[i][j] modulo MOD
	C := make([][]int64, n+1)
	for i := 0; i <= n; i++ {
		C[i] = make([]int64, n+1)
		C[i][0] = 1
		C[i][i] = 1
		for j := 1; j < i; j++ {
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
		}
	}

	// steps[v]: number of popcount operations to reach 1 from v (v>=1)
	steps := make([]int, n+1)
	if n >= 1 {
		steps[1] = 0
	}
	for v := 2; v <= n; v++ {
		pc := bits.OnesCount(uint(v))
		steps[v] = 1 + steps[pc]
	}

	// allowed popcounts c where total steps ≤ k (i.e., 1+steps[c] ≤ k)
	limit := k - 1
	allowed := []int{}
	for c := 1; c <= n; c++ {
		if steps[c] <= limit {
			allowed = append(allowed, c)
		}
	}

	ans := int64(0)
	cntOnesSoFar := 0
	for i, ch := range s {
		if ch == '1' {
			rem := n - i - 1
			for _, c := range allowed {
				need := c - cntOnesSoFar
				if need < 0 || need > rem {
					continue
				}
				ans = (ans + C[rem][need]) % MOD
			}
			cntOnesSoFar++
		}
	}

	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_k_reducible_numbers(s, k)
  n_len = s.length
  # binomial coefficients
  comb = Array.new(n_len + 1) { Array.new(n_len + 1, 0) }
  (0..n_len).each do |i|
    comb[i][0] = comb[i][i] = 1
    (1...i).each do |j|
      comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
    end
  end

  # steps to reach 1 via popcount repeatedly
  steps = Array.new(n_len + 1, 0)
  steps[1] = 0
  (2..n_len).each do |t|
    pc = t.to_s(2).count('1')
    steps[t] = 1 + steps[pc]
  end

  # allowed popcounts
  allowed = Array.new(n_len + 1, false)
  (1..n_len).each do |p|
    if p == 1
      allowed[p] = k >= 1
    else
      allowed[p] = (1 + steps[p]) <= k
    end
  end
  allowed_ps = []
  (1..n_len).each { |p| allowed_ps << p if allowed[p] }

  ans = 0

  # lengths shorter than n_len
  (1...n_len).each do |len|
    allowed_ps.each do |p|
      next if p > len
      ans += comb[len - 1][p - 1]
      ans -= MOD if ans >= MOD
    end
  end

  # same length, numbers less than s
  cnt_one = 0
  (0...n_len).each do |i|
    if s[i] == '1'
      if i > 0
        remaining = n_len - i - 1
        allowed_ps.each do |p|
          need = p - cnt_one
          next if need < 0 || need > remaining
          ans += comb[remaining][need]
          ans -= MOD if ans >= MOD
        end
      end
      cnt_one += 1
    end
  end

  ans % MOD
end
```

## Scala

```scala
object Solution {
    val MOD = 1000000007L
    def countKReducibleNumbers(s: String, k: Int): Int = {
        val L = s.length

        // Precompute binomial coefficients C[n][r] modulo MOD
        val C = Array.ofDim[Long](L + 1, L + 1)
        for (i <- 0 to L) {
            C(i)(0) = 1L
            C(i)(i) = 1L
            var j = 1
            while (j < i) {
                C(i)(j) = (C(i - 1)(j - 1) + C(i - 1)(j)) % MOD
                j += 1
            }
        }

        // Steps needed to reduce a number <= L to 1 by repeatedly taking popcount
        val steps = Array.fill[Int](L + 1)(0)
        steps(0) = Int.MaxValue // unused
        steps(1) = 0
        for (i <- 2 to L) {
            val pc = Integer.bitCount(i)
            steps(i) = 1 + steps(pc)
        }

        // Allowed popcount values such that after first operation we can finish within k-1 more steps
        val limit = k - 1
        val allowed = scala.collection.mutable.ArrayBuffer[Int]()
        for (c <- 1 to L) {
            if (steps(c) <= limit) allowed += c
        }

        // Count numbers < N with exactly onesNeeded set bits
        def countLessThan(onesNeeded: Int): Long = {
            if (onesNeeded > L) return 0L
            var ans = 0L
            var onesSoFar = 0
            for (i <- 0 until L) {
                if (s.charAt(i) == '1') {
                    val remaining = L - i - 1
                    val need = onesNeeded - onesSoFar
                    if (need >= 0 && need <= remaining) {
                        ans = (ans + C(remaining)(need)) % MOD
                    }
                    onesSoFar += 1
                }
            }
            // Numbers equal to N are not added, so we already have count of numbers < N
            ans
        }

        var total = 0L
        for (c <- allowed) {
            total = (total + countLessThan(c)) % MOD
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_k_reducible_numbers(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();

        // binomial coefficients C[i][j] for 0 <= i,j <= n
        let mut comb = vec![vec![0i64; n + 1]; n + 1];
        for i in 0..=n {
            comb[i][0] = 1;
            comb[i][i] = 1;
            for j in 1..i {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }

        // steps[x]: number of operations to reach 1 from x
        let mut steps = vec![usize::MAX; n + 1];
        if n >= 1 {
            steps[1] = 0;
        }
        for i in 2..=n {
            let pc = i.count_ones() as usize;
            steps[i] = 1 + steps[pc];
        }

        let mut ans: i64 = 0;
        let kk = k as usize;
        if kk == 0 {
            return 0;
        }
        for p in 1..=n {
            if steps[p] <= kk - 1 {
                ans += Self::count_less(bytes, n, p, &comb);
                if ans >= MOD {
                    ans -= MOD;
                }
            }
        }

        (ans % MOD) as i32
    }

    fn count_less(s: &[u8], len: usize, target: usize, comb: &Vec<Vec<i64>>) -> i64 {
        const MOD: i64 = 1_000_000_007;
        let mut res: i64 = 0;
        let mut ones: usize = 0;
        for (i, &c) in s.iter().enumerate() {
            if c == b'1' {
                let remaining = len - i - 1;
                if target >= ones {
                    let need = target - ones;
                    if need <= remaining {
                        res += comb[remaining][need];
                        if res >= MOD {
                            res -= MOD;
                        }
                    }
                }
                ones += 1;
            }
        }
        // numbers equal to n are not counted, so nothing more to add
        res % MOD
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; compute popcount of an integer (0 <= x <= 800)
(define (int-popcnt x)
  (let loop ((y x) (c 0))
    (if (= y 0)
        c
        (loop (arithmetic-shift y -1) (+ c (bitwise-and y 1))))))

;; compute steps to reach 1 via repeated popcount
(define steps-memo (make-vector 801 #f))
(define (steps x)
  (cond [(= x 1) 0]
        [else
         (let ((cached (vector-ref steps-memo x)))
           (if cached
               cached
               (let ((res (+ 1 (steps (int-popcnt x)))))
                 (vector-set! steps-memo x res)
                 res)))]))

;; main function
(define/contract (count-k-reducible-numbers s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((len (string-length s))
         ;; allowed popcounts: dpSteps[p] <= k-1
         (allowed (make-vector (+ len 1) #f)))
    (for ([p (in-range 1 (+ len 1))])
      (when (<= (steps p) (- k 1))
        (vector-set! allowed p #t)))
    ;; DP memoization: key = idx cnt tight
    (define memo (make-hash))
    (define (dp idx cnt tight)
      (if (= idx len)
          (if (and (> cnt 0) (vector-ref allowed cnt)) 1 0)
          (let ((key (list idx cnt tight)))
            (or (hash-ref memo key #f)
                (let* ((limit (if tight
                                  (if (char=? (string-ref s idx) #\1) 1 0)
                                  1))
                       (total
                        (let loop ((b 0) (acc 0))
                          (if (> b limit)
                              acc
                              (let ((new-tight (and tight (= b limit))))
                                (loop (+ b 1)
                                      (modulo (+ acc (dp (+ idx 1) (+ cnt b) new-tight)) MOD)))))))
                  (hash-set! memo key total)
                  total)))))
    (let* ((total (dp 0 0 #t))
           ;; subtract n itself if it satisfies condition
           (pop-n (string-count s #\1))
           (subtract (and (<= pop-n len) (vector-ref allowed pop-n)))
           (ans (if subtract (modulo (- total 1) MOD) (modulo total MOD))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_k_reducible_numbers/2]).

-define(MOD, 1000000007).

count_k_reducible_numbers(S, K) ->
    Bits = [C - $0 || <<C>> <= S],
    L = length(Bits),
    Comb = precompute_comb(L),
    StepsMap = build_steps_map(L),
    Allowed = [C || C <- lists:seq(1, L), maps:get(C, StepsMap) =< K-1],
    Ans = lists:foldl(fun(C, Acc) ->
        CountC = count_less(Bits, C, Comb),
        (Acc + CountC) rem ?MOD
    end, 0, Allowed),
    Ans.

%% precompute binomial coefficients modulo MOD up to n = L
precompute_comb(L) ->
    lists:foldl(fun(N, Rows) ->
        Row = case N of
            0 -> [1];
            _ ->
                PrevRow = lists:nth(N, Rows), % row for N-1
                [case K of
                    0 -> 1;
                    K when K == N -> 1;
                    _ ->
                        (lists:nth(K, PrevRow) + lists:nth(K+1, PrevRow)) rem ?MOD
                 end || K <- lists:seq(0, N)]
        end,
        Rows ++ [Row]
    end, [], lists:seq(0, L)).

%% retrieve C(N,K)
get_comb(Comb, N, K) when K < 0; K > N -> 0;
get_comb(Comb, N, K) ->
    Row = lists:nth(N+1, Comb),
    lists:nth(K+1, Row).

%% count numbers less than the binary number represented by Bits with exactly C ones
count_less(Bits, C, Comb) ->
    Len = length(Bits),
    count_less_loop(Bits, 0, C, Len, Comb, 0).

count_less_loop(_Bits, _Pos, RemOnes, _Len, _Comb, Acc) when RemOnes < 0 ->
    Acc;
count_less_loop([], _Pos, _RemOnes, _Len, _Comb, Acc) ->
    Acc; % reached end, exact match not counted
count_less_loop(Bits, Pos, RemOnes, Len, Comb, Acc) ->
    Bit = lists:nth(Pos+1, Bits),
    Remaining = Len - Pos - 1,
    case Bit of
        1 ->
            Add = get_comb(Comb, Remaining, RemOnes),
            NewAcc = (Acc + Add) rem ?MOD,
            count_less_loop(Bits, Pos+1, RemOnes-1, Len, Comb, NewAcc);
        0 ->
            count_less_loop(Bits, Pos+1, RemOnes, Len, Comb, Acc)
    end.

%% build map of steps needed to reduce i to 1 (i up to L)
build_steps_map(L) ->
    lists:foldl(fun(I, M) ->
        Val = case I of
            0 -> 100; % sentinel large value, never used
            1 -> 0;
            _ -> step_needed(I)
        end,
        maps:put(I, Val, M)
    end, #{}, lists:seq(0, L)).

step_needed(1) -> 0;
step_needed(N) when N > 1 ->
    1 + step_needed(popcnt(N)).

popcnt(0) -> 0;
popcnt(N) ->
    1 + popcnt(N band (N-1)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @modulus 1_000_000_007

  @spec count_k_reducible_numbers(s :: String.t(), k :: integer) :: integer
  def count_k_reducible_numbers(s, k) do
    len = String.length(s)

    binom = build_binom(len)
    steps_map = compute_steps(len)

    allowed_counts =
      1..len
      |> Enum.filter(fn c -> 1 + Map.get(steps_map, c, 0) <= k end)

    chars = String.to_charlist(s)

    {ans, _} =
      Enum.reduce(Enum.with_index(chars), {0, 0}, fn {ch, idx}, {acc, ones_sofar} ->
        if ch == ?1 do
          rem = len - idx - 1

          add =
            Enum.reduce(allowed_counts, 0, fn c, a ->
              need = c - ones_sofar

              if need >= 0 and need <= rem do
                row = Enum.at(binom, rem)
                val = Enum.at(row, need)
                (a + val) |> rem(@modulus)
              else
                a
              end
            end)

          {(acc + add) |> rem(@modulus), ones_sofar + 1}
        else
          {acc, ones_sofar}
        end
      end)

    ans
  end

  defp build_binom(max_n) do
    Enum.reduce(0..max_n, [], fn i, acc ->
      row =
        Enum.map(0..i, fn j ->
          cond do
            j == 0 or j == i -> 1
            true ->
              prev = Enum.at(acc, i - 1)
              (Enum.at(prev, j - 1) + Enum.at(prev, j)) |> rem(@modulus)
          end
        end)

      acc ++ [row]
    end)
  end

  defp compute_steps(max_c) do
    Enum.reduce(0..max_c, %{}, fn c, memo ->
      {val, new_memo} = steps_one(c, memo)
      Map.put(new_memo, c, val)
    end)
  end

  defp steps_one(1, memo), do: {0, memo}
  defp steps_one(0, memo), do: {0, memo}

  defp steps_one(c, memo) do
    case Map.fetch(memo, c) do
      {:ok, v} -> {v, memo}
      :error ->
        pc = popcount(c)
        {sub, memo2} = steps_one(pc, memo)
        {1 + sub, Map.put(memo2, c, 1 + sub)}
    end
  end

  defp popcount(0), do: 0
  defp popcount(n) do
    (n &&& 1) + popcount(n >>> 1)
  end
end
```
