# 3398. Smallest Substring With Identical Characters I

## Cpp

```cpp
class Solution {
public:
    bool canAchieve(const string& s, int numOps, int L) {
        const int INF = 1e9;
        int n = s.size();
        vector<vector<int>> dpPrev(2, vector<int>(L + 1, INF));
        // initialize first character
        for (int c = 0; c <= 1; ++c) {
            int cost = (s[0] - '0' != c);
            dpPrev[c][1] = cost;
        }
        for (int i = 1; i < n; ++i) {
            vector<vector<int>> dpCurr(2, vector<int>(L + 1, INF));
            for (int pc = 0; pc <= 1; ++pc) {
                for (int len = 1; len <= L; ++len) {
                    int curCost = dpPrev[pc][len];
                    if (curCost == INF) continue;
                    for (int nc = 0; nc <= 1; ++nc) {
                        int nlen = (nc == pc) ? len + 1 : 1;
                        if (nlen > L) continue;
                        int add = (s[i] - '0' != nc);
                        dpCurr[nc][nlen] = min(dpCurr[nc][nlen], curCost + add);
                    }
                }
            }
            dpPrev.swap(dpCurr);
        }
        int best = INF;
        for (int c = 0; c <= 1; ++c)
            for (int len = 1; len <= L; ++len)
                best = min(best, dpPrev[c][len]);
        return best <= numOps;
    }

    int minLength(string s, int numOps) {
        int n = s.size();
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (canAchieve(s, numOps, mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int low = 1, high = n, ans = n;
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (canAchieve(s, numOps, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean canAchieve(String s, int maxOps, int limit) {
        int n = s.length();
        final int INF = 1_000_000;
        int[][] prev = new int[2][limit + 2];
        int[][] cur = new int[2][limit + 2];

        for (int c = 0; c < 2; ++c) {
            for (int l = 1; l <= limit; ++l) prev[c][l] = INF;
        }
        // initialize first character
        int firstBit = s.charAt(0) - '0';
        for (int c = 0; c < 2; ++c) {
            prev[c][1] = (firstBit == c) ? 0 : 1;
        }

        for (int i = 1; i < n; ++i) {
            int bit = s.charAt(i) - '0';
            for (int c = 0; c < 2; ++c) {
                for (int l = 1; l <= limit; ++l) cur[c][l] = INF;
            }
            for (int pc = 0; pc < 2; ++pc) {
                for (int plen = 1; plen <= limit; ++plen) {
                    int prevCost = prev[pc][plen];
                    if (prevCost == INF) continue;
                    for (int c = 0; c < 2; ++c) {
                        int cost = prevCost + ((bit == c) ? 0 : 1);
                        if (c == pc) {
                            if (plen + 1 <= limit) {
                                cur[c][plen + 1] = Math.min(cur[c][plen + 1], cost);
                            }
                        } else {
                            cur[c][1] = Math.min(cur[c][1], cost);
                        }
                    }
                }
            }
            // swap
            int[][] tmp = prev;
            prev = cur;
            cur = tmp;
        }

        int best = INF;
        for (int c = 0; c < 2; ++c) {
            for (int l = 1; l <= limit; ++l) {
                best = Math.min(best, prev[c][l]);
            }
        }
        return best <= maxOps;
    }
}
```

## Python

```python
class Solution(object):
    def minLength(self, s, numOps):
        """
        :type s: str
        :type numOps: int
        :rtype: int
        """
        n = len(s)

        def feasible(L):
            INF = 10 ** 9
            # dp_prev[c][len] = minimal flips up to previous position
            dp_prev = [[INF] * (L + 1) for _ in range(2)]
            # initialize first character
            dp_prev[0][1] = 0 if s[0] == '0' else 1
            dp_prev[1][1] = 0 if s[0] == '1' else 1

            for i in range(1, n):
                dp_curr = [[INF] * (L + 1) for _ in range(2)]
                # best cost when previous char is opposite
                best_prev_diff_0 = min(dp_prev[1])  # now we place '0'
                best_prev_diff_1 = min(dp_prev[0])  # now we place '1'

                cost0 = 0 if s[i] == '0' else 1
                cost1 = 0 if s[i] == '1' else 1

                # place '0' at position i
                dp_curr[0][1] = best_prev_diff_0 + cost0
                for l in range(2, L + 1):
                    if dp_prev[0][l - 1] < INF:
                        dp_curr[0][l] = dp_prev[0][l - 1] + cost0

                # place '1' at position i
                dp_curr[1][1] = best_prev_diff_1 + cost1
                for l in range(2, L + 1):
                    if dp_prev[1][l - 1] < INF:
                        dp_curr[1][l] = dp_prev[1][l - 1] + cost1

                dp_prev = dp_curr

            min_flips = min(min(row) for row in dp_prev)
            return min_flips <= numOps

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## Python3

```python
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        INF = 10 ** 9

        # predicate: can we achieve max run length <= L with at most numOps flips?
        def feasible(L: int) -> bool:
            # dp[c][len] = min flips up to current position, ending with char c and run length len
            dp_prev = [[INF] * (L + 1) for _ in range(2)]
            first_bit = int(s[0])
            for c in (0, 1):
                dp_prev[c][1] = 0 if first_bit == c else 1

            for i in range(1, n):
                cur_bit = int(s[i])
                dp_cur = [[INF] * (L + 1) for _ in range(2)]
                for pc in (0, 1):
                    row = dp_prev[pc]
                    for pl in range(1, L + 1):
                        prev_cost = row[pl]
                        if prev_cost == INF:
                            continue
                        # keep same character
                        c = pc
                        nl = pl + 1
                        if nl <= L:
                            cost = prev_cost + (0 if cur_bit == c else 1)
                            if cost < dp_cur[c][nl]:
                                dp_cur[c][nl] = cost
                        # switch character
                        c = 1 - pc
                        nl = 1
                        cost = prev_cost + (0 if cur_bit == c else 1)
                        if cost < dp_cur[c][nl]:
                            dp_cur[c][nl] = cost
                dp_prev = dp_cur

            min_flips = INF
            for c in (0, 1):
                for l in range(1, L + 1):
                    if dp_prev[c][l] < min_flips:
                        min_flips = dp_prev[c][l]
            return min_flips <= numOps

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
#include <string.h>
#include <limits.h>

static int canAchieve(int L, const char *s, int n, int k) {
    const int INF = INT_MAX / 2;
    static int dp[2][2][1005];
    // initialize first character
    for (int c = 0; c <= 1; ++c)
        for (int len = 1; len <= L; ++len)
            dp[0][c][len] = INF;
    for (int c = 0; c <= 1; ++c) {
        int cost = ((s[0] - '0') != c);
        dp[0][c][1] = cost;
    }

    int cur = 1, prev = 0;
    for (int i = 1; i < n; ++i) {
        for (int c = 0; c <= 1; ++c)
            for (int len = 1; len <= L; ++len)
                dp[cur][c][len] = INF;

        for (int pc = 0; pc <= 1; ++pc) {
            for (int pl = 1; pl <= L; ++pl) {
                int prevCost = dp[prev][pc][pl];
                if (prevCost == INF) continue;
                for (int c = 0; c <= 1; ++c) {
                    int newLen = (c == pc) ? pl + 1 : 1;
                    if (newLen > L) continue;
                    int cost = prevCost + ((s[i] - '0') != c);
                    if (cost < dp[cur][c][newLen])
                        dp[cur][c][newLen] = cost;
                }
            }
        }
        int tmp = prev; prev = cur; cur = tmp;
    }

    int best = INF;
    for (int c = 0; c <= 1; ++c)
        for (int len = 1; len <= L; ++len)
            if (dp[prev][c][len] < best) best = dp[prev][c][len];

    return best <= k;
}

int minLength(char* s, int numOps) {
    int n = strlen(s);
    int low = 1, high = n, ans = n;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (canAchieve(mid, s, n, numOps)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinLength(string s, int numOps)
    {
        int n = s.Length;
        int[] prefOnes = new int[n + 1];
        for (int i = 0; i < n; i++)
            prefOnes[i + 1] = prefOnes[i] + (s[i] == '1' ? 1 : 0);

        bool Can(int L)
        {
            const int INF = 1_000_000;
            int[,] dp = new int[n + 1, 2];
            for (int i = 0; i <= n; i++)
                dp[i, 0] = dp[i, 1] = INF;
            dp[0, 0] = dp[0, 1] = 0;

            for (int i = 1; i <= n; i++)
            {
                int maxLen = Math.Min(L, i);
                for (int len = 1; len <= maxLen; len++)
                {
                    int l = i - len;
                    int ones = prefOnes[i] - prefOnes[l];
                    int zeros = len - ones;

                    // make segment all '0' -> cost = ones, previous char must be '1'
                    if (dp[l, 1] + ones < dp[i, 0])
                        dp[i, 0] = dp[l, 1] + ones;
                    // make segment all '1' -> cost = zeros, previous char must be '0'
                    if (dp[l, 0] + zeros < dp[i, 1])
                        dp[i, 1] = dp[l, 0] + zeros;
                }
            }

            int best = Math.Min(dp[n, 0], dp[n, 1]);
            return best <= numOps;
        }

        int lo = 1, hi = n, ans = n;
        while (lo <= hi)
        {
            int mid = (lo + hi) / 2;
            if (Can(mid))
            {
                ans = mid;
                hi = mid - 1;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} numOps
 * @return {number}
 */
var minLength = function(s, numOps) {
    const n = s.length;
    const INF = 1e9;

    // check if we can achieve max run length <= L with at most numOps flips
    const feasible = (L) => {
        // dp0[runLen] = min flips ending with '0' having current run length = runLen
        // dp1 similarly for '1'
        let dp0 = new Array(L + 1).fill(INF);
        let dp1 = new Array(L + 1).fill(INF);

        // first character
        if (s[0] === '0') {
            dp0[1] = 0;
            dp1[1] = 1;
        } else {
            dp0[1] = 1;
            dp1[1] = 0;
        }

        for (let i = 1; i < n; ++i) {
            const ndp0 = new Array(L + 1).fill(INF);
            const ndp1 = new Array(L + 1).fill(INF);
            const ch = s[i];

            for (let rl = 1; rl <= L; ++rl) {
                if (dp0[rl] < INF) {
                    // keep '0'
                    if (rl + 1 <= L) {
                        ndp0[rl + 1] = Math.min(ndp0[rl + 1], dp0[rl] + (ch === '0' ? 0 : 1));
                    }
                    // switch to '1'
                    ndp1[1] = Math.min(ndp1[1], dp0[rl] + (ch === '1' ? 0 : 1));
                }
                if (dp1[rl] < INF) {
                    // keep '1'
                    if (rl + 1 <= L) {
                        ndp1[rl + 1] = Math.min(ndp1[rl + 1], dp1[rl] + (ch === '1' ? 0 : 1));
                    }
                    // switch to '0'
                    ndp0[1] = Math.min(ndp0[1], dp1[rl] + (ch === '0' ? 0 : 1));
                }
            }

            dp0 = ndp0;
            dp1 = ndp1;
        }

        let best = INF;
        for (let rl = 1; rl <= L; ++rl) {
            if (dp0[rl] < best) best = dp0[rl];
            if (dp1[rl] < best) best = dp1[rl];
        }
        return best <= numOps;
    };

    let lo = 1, hi = n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (feasible(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function minLength(s: string, numOps: number): number {
    const n = s.length;
    if (n === 0) return 0;

    const INF = 1e9;

    function can(L: number): boolean {
        // dp for previous position
        let prev0 = new Array(L + 1).fill(INF);
        let prev1 = new Array(L + 1).fill(INF);

        const firstOrig = s.charCodeAt(0) - 48; // 0 or 1
        prev0[1] = firstOrig === 0 ? 0 : 1;
        prev1[1] = firstOrig === 1 ? 0 : 1;

        for (let i = 1; i < n; i++) {
            const curOrig = s.charCodeAt(i) - 48;
            let next0 = new Array(L + 1).fill(INF);
            let next1 = new Array(L + 1).fill(INF);

            for (let len = 1; len <= L; len++) {
                const val0 = prev0[len];
                if (val0 < INF) {
                    // continue with 0
                    const cost0 = curOrig === 0 ? 0 : 1;
                    const newLen0 = len + 1;
                    if (newLen0 <= L && next0[newLen0] > val0 + cost0) {
                        next0[newLen0] = val0 + cost0;
                    }
                    // switch to 1
                    const cost1 = curOrig === 1 ? 0 : 1;
                    if (next1[1] > val0 + cost1) {
                        next1[1] = val0 + cost1;
                    }
                }

                const val1 = prev1[len];
                if (val1 < INF) {
                    // switch to 0
                    const cost0 = curOrig === 0 ? 0 : 1;
                    if (next0[1] > val1 + cost0) {
                        next0[1] = val1 + cost0;
                    }
                    // continue with 1
                    const cost1 = curOrig === 1 ? 0 : 1;
                    const newLen1 = len + 1;
                    if (newLen1 <= L && next1[newLen1] > val1 + cost1) {
                        next1[newLen1] = val1 + cost1;
                    }
                }
            }

            prev0 = next0;
            prev1 = next1;
        }

        for (let len = 1; len <= L; len++) {
            if (prev0[len] <= numOps || prev1[len] <= numOps) return true;
        }
        return false;
    }

    let low = 1, high = n;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (can(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $numOps
     * @return Integer
     */
    function minLength($s, $numOps) {
        $n = strlen($s);
        $lo = 1;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->canAchieve($s, $numOps, $mid)) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo;
    }

    private function canAchieve(string $s, int $k, int $L): bool {
        $n = strlen($s);
        $INF = $n + 5; // larger than any possible flips
        // dp[c][len] = minimal flips up to current position,
        // where current character is c (0/1) and its run length is len (1..L)
        $dp = [
            array_fill(0, $L + 1, $INF),
            array_fill(0, $L + 1, $INF)
        ];
        $firstChar = intval($s[0]);
        for ($c = 0; $c <= 1; $c++) {
            $dp[$c][1] = ($firstChar == $c) ? 0 : 1;
        }

        for ($i = 1; $i < $n; $i++) {
            $ch = intval($s[$i]);
            $newdp = [
                array_fill(0, $L + 1, $INF),
                array_fill(0, $L + 1, $INF)
            ];
            for ($pc = 0; $pc <= 1; $pc++) {
                for ($plen = 1; $plen <= $L; $plen++) {
                    $prev = $dp[$pc][$plen];
                    if ($prev > $k) continue; // pruning, cannot be better than k
                    if ($prev >= $INF) continue;
                    for ($curc = 0; $curc <= 1; $curc++) {
                        $add = ($ch == $curc) ? 0 : 1;
                        $cost = $prev + $add;
                        if ($cost > $k) {
                            // still store, but it won't be useful later
                        }
                        if ($curc == $pc) {
                            $newLen = $plen + 1;
                            if ($newLen <= $L && $cost < $newdp[$curc][$newLen]) {
                                $newdp[$curc][$newLen] = $cost;
                            }
                        } else {
                            // start new run of length 1
                            if ($cost < $newdp[$curc][1]) {
                                $newdp[$curc][1] = $cost;
                            }
                        }
                    }
                }
            }
            $dp = $newdp;
        }

        for ($c = 0; $c <= 1; $c++) {
            for ($len = 1; $len <= $L; $len++) {
                if ($dp[$c][$len] <= $k) return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func minLength(_ s: String, _ numOps: Int) -> Int {
        let arr = s.map { $0 == "1" ? 1 : 0 }
        let n = arr.count
        var lo = 1, hi = n
        while lo < hi {
            let mid = (lo + hi) / 2
            if can(mid, arr, numOps) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }

    private func can(_ L: Int, _ arr: [Int], _ k: Int) -> Bool {
        let n = arr.count
        if L == 0 { return false }
        let INF = Int.max / 2
        var dpPrev = Array(repeating: Array(repeating: INF, count: L + 1), count: 2)
        dpPrev[0][1] = (arr[0] == 0) ? 0 : 1
        dpPrev[1][1] = (arr[0] == 1) ? 0 : 1

        if n == 1 {
            return min(dpPrev[0][1], dpPrev[1][1]) <= k
        }

        for i in 1..<n {
            var dpCurr = Array(repeating: Array(repeating: INF, count: L + 1), count: 2)
            for prevChar in 0...1 {
                for lenPrev in 1...L {
                    let curVal = dpPrev[prevChar][lenPrev]
                    if curVal >= INF { continue }
                    // set current char to 0
                    var newLen = (prevChar == 0) ? lenPrev + 1 : 1
                    if newLen <= L {
                        let cost = curVal + ((arr[i] == 0) ? 0 : 1)
                        if cost < dpCurr[0][newLen] { dpCurr[0][newLen] = cost }
                    }
                    // set current char to 1
                    newLen = (prevChar == 1) ? lenPrev + 1 : 1
                    if newLen <= L {
                        let cost = curVal + ((arr[i] == 1) ? 0 : 1)
                        if cost < dpCurr[1][newLen] { dpCurr[1][newLen] = cost }
                    }
                }
            }
            dpPrev = dpCurr
        }

        var best = INF
        for c in 0...1 {
            for len in 1...L {
                let v = dpPrev[c][len]
                if v < best { best = v }
            }
        }
        return best <= k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minLength(s: String, numOps: Int): Int {
        val n = s.length
        fun can(limit: Int): Boolean {
            val INF = 1_000_000_0
            var dp0 = IntArray(limit + 2) { INF }
            var dp1 = IntArray(limit + 2) { INF }
            // initialize for first character
            dp0[1] = if (s[0] == '0') 0 else 1
            dp1[1] = if (s[0] == '1') 0 else 1

            for (i in 1 until n) {
                val ndp0 = IntArray(limit + 2) { INF }
                val ndp1 = IntArray(limit + 2) { INF }
                val origIsZero = s[i] == '0'

                // previous ending with '0'
                for (len in 1..limit) {
                    val cur = dp0[len]
                    if (cur >= INF) continue
                    // keep '0'
                    if (len + 1 <= limit) {
                        val cost = cur + if (origIsZero) 0 else 1
                        if (cost < ndp0[len + 1]) ndp0[len + 1] = cost
                    }
                    // switch to '1'
                    val costSwitch = cur + if (!origIsZero) 0 else 1
                    if (costSwitch < ndp1[1]) ndp1[1] = costSwitch
                }

                // previous ending with '1'
                for (len in 1..limit) {
                    val cur = dp1[len]
                    if (cur >= INF) continue
                    // keep '1'
                    if (len + 1 <= limit) {
                        val cost = cur + if (!origIsZero) 0 else 1
                        if (cost < ndp1[len + 1]) ndp1[len + 1] = cost
                    }
                    // switch to '0'
                    val costSwitch = cur + if (origIsZero) 0 else 1
                    if (costSwitch < ndp0[1]) ndp0[1] = costSwitch
                }

                dp0 = ndp0
                dp1 = ndp1
            }

            var best = INF
            for (len in 1..limit) {
                if (dp0[len] < best) best = dp0[len]
                if (dp1[len] < best) best = dp1[len]
            }
            return best <= numOps
        }

        var lo = 1
        var hi = n
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (can(mid)) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
}
```

## Dart

```dart
class Solution {
  int minLength(String s, int numOps) {
    int n = s.length;
    List<int> prefZero = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefZero[i + 1] = prefZero[i] + (s.codeUnitAt(i) == 48 ? 1 : 0); // '0' ascii 48
    }

    bool can(int L) {
      const int INF = 1 << 30;
      List<int> dp = List.filled(n + 1, INF);
      dp[0] = 0;
      for (int i = 1; i <= n; i++) {
        int start = i - L;
        if (start < 0) start = 0;
        for (int j = start; j < i; j++) {
          int len = i - j;
          int zeros = prefZero[i] - prefZero[j];
          int ones = len - zeros;
          int segCost = zeros < ones ? zeros : ones;
          int cand = dp[j] + segCost;
          if (cand < dp[i]) dp[i] = cand;
        }
      }
      return dp[n] <= numOps;
    }

    int lo = 1, hi = n, ans = n;
    while (lo <= hi) {
      int mid = (lo + hi) >> 1;
      if (can(mid)) {
        ans = mid;
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minLength(s string, numOps int) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	low, high := 1, n
	for low < high {
		mid := (low + high) / 2
		if feasible(s, mid, numOps) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}

func feasible(s string, L int, k int) bool {
	const INF = 1 << 30
	n := len(s)

	// dpPrev[c][len] = min flips up to current position ending with char c and run length len
	dpPrev := make([][]int, 2)
	for i := 0; i < 2; i++ {
		dpPrev[i] = make([]int, L+1)
		for j := 0; j <= L; j++ {
			dpPrev[i][j] = INF
		}
	}
	// initialize with first character
	firstBit := int(s[0] - '0')
	for c := 0; c < 2; c++ {
		cost := 0
		if firstBit != c {
			cost = 1
		}
		dpPrev[c][1] = cost
	}

	// process remaining characters
	for i := 1; i < n; i++ {
		curBit := int(s[i] - '0')
		dpNext := make([][]int, 2)
		for c := 0; c < 2; c++ {
			dpNext[c] = make([]int, L+1)
			for j := 0; j <= L; j++ {
				dpNext[c][j] = INF
			}
		}
		for prevC := 0; prevC < 2; prevC++ {
			for runLen := 1; runLen <= L; runLen++ {
				val := dpPrev[prevC][runLen]
				if val == INF {
					continue
				}
				for newC := 0; newC < 2; newC++ {
					newRun := 1
					if newC == prevC {
						if runLen+1 > L {
							continue
						}
						newRun = runLen + 1
					}
					add := 0
					if curBit != newC {
						add = 1
					}
					newCost := val + add
					if dpNext[newC][newRun] > newCost {
						dpNext[newC][newRun] = newCost
					}
				}
			}
		}
		dpPrev = dpNext
	}

	best := INF
	for c := 0; c < 2; c++ {
		for runLen := 1; runLen <= L; runLen++ {
			if dpPrev[c][runLen] < best {
				best = dpPrev[c][runLen]
			}
		}
	}
	return best <= k
}
```

## Ruby

```ruby
def min_length(s, num_ops)
  n = s.length
  a = s.bytes.map { |b| b - 48 } # convert '0'/'1' to integers

  inf = 1 << 30

  feasible = lambda do |limit|
    dp = Array.new(2) { Array.new(limit + 1, inf) }
    [0, 1].each { |c| dp[c][1] = (a[0] == c ? 0 : 1) }

    (1...n).each do |i|
      ndp = Array.new(2) { Array.new(limit + 1, inf) }
      [0, 1].each do |prev_c|
        (1..limit).each do |len|
          cur_cost = dp[prev_c][len]
          next if cur_cost >= inf
          [0, 1].each do |new_c|
            add = (a[i] == new_c ? 0 : 1)
            if new_c == prev_c
              new_len = len + 1
              next if new_len > limit
            else
              new_len = 1
            end
            total = cur_cost + add
            ndp[new_c][new_len] = total if total < ndp[new_c][new_len]
          end
        end
      end
      dp = ndp
    end

    min_cost = inf
    [0, 1].each do |c|
      (1..limit).each { |len| min_cost = dp[c][len] if dp[c][len] < min_cost }
    end
    min_cost <= num_ops
  end

  low = 1
  high = n
  while low < high
    mid = (low + high) / 2
    if feasible.call(mid)
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def minLength(s: String, numOps: Int): Int = {
        val n = s.length
        val arr = s.toCharArray.map(c => c - '0')
        def feasible(L: Int): Boolean = {
            val INF = 1_000_000
            var dpPrev = Array.fill(2, L + 2)(INF)
            for (ch <- 0 to 1) {
                val cost = if (arr(0) != ch) 1 else 0
                dpPrev(ch)(1) = cost
            }
            var i = 1
            while (i < n) {
                val dpCurr = Array.fill(2, L + 2)(INF)
                for (pc <- 0 to 1) {
                    var pl = 1
                    while (pl <= L) {
                        val prevCost = dpPrev(pc)(pl)
                        if (prevCost < INF) {
                            for (ch <- 0 to 1) {
                                val add = if (arr(i) != ch) 1 else 0
                                if (ch == pc) {
                                    val nl = pl + 1
                                    if (nl <= L) {
                                        val newCost = prevCost + add
                                        if (newCost < dpCurr(ch)(nl)) dpCurr(ch)(nl) = newCost
                                    }
                                } else {
                                    val nl = 1
                                    val newCost = prevCost + add
                                    if (newCost < dpCurr(ch)(nl)) dpCurr(ch)(nl) = newCost
                                }
                            }
                        }
                        pl += 1
                    }
                }
                dpPrev = dpCurr
                i += 1
            }
            var minCost = INF
            for (c <- 0 to 1; l <- 1 to L) {
                if (dpPrev(c)(l) < minCost) minCost = dpPrev(c)(l)
            }
            minCost <= numOps
        }

        var low = 1
        var high = n
        while (low < high) {
            val mid = (low + high) >>> 1
            if (feasible(mid)) high = mid else low = mid + 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_length(s: String, num_ops: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();

        // predicate: can we achieve max run length <= limit with at most k flips
        fn feasible(bytes: &[u8], limit: usize, k: i32) -> bool {
            const INF: i32 = 1_000_000_000;
            let n = bytes.len();
            // dp[c][len] where c=0/1, len in 1..=limit
            let mut prev = vec![vec![INF; limit + 1]; 2];
            for cur in 0..2 {
                let cost = if bytes[0] == b'0' + cur as u8 { 0 } else { 1 };
                prev[cur][1] = cost;
            }

            for i in 1..n {
                let mut cur_dp = vec![vec![INF; limit + 1]; 2];
                for pc in 0..2 {
                    for plen in 1..=limit {
                        let base = prev[pc][plen];
                        if base == INF {
                            continue;
                        }
                        for nc in 0..2 {
                            let nlen = if nc == pc { plen + 1 } else { 1 };
                            if nlen > limit {
                                continue;
                            }
                            let add = if bytes[i] == b'0' + nc as u8 { 0 } else { 1 };
                            let val = base + add;
                            if val < cur_dp[nc][nlen] {
                                cur_dp[nc][nlen] = val;
                            }
                        }
                    }
                }
                prev = cur_dp;
            }

            let mut best = INF;
            for c in 0..2 {
                for len in 1..=limit {
                    if prev[c][len] < best {
                        best = prev[c][len];
                    }
                }
            }
            best <= k
        }

        let mut lo = 1usize;
        let mut hi = n;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if feasible(bytes, mid, num_ops) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
```

## Racket

```racket
(define/contract (min-length s numOps)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (INF 1000000))

    ;; convert character to integer 0 or 1
    (define (char->int ch) (if (char=? ch #\1) 1 0))

    ;; predicate: can we achieve max run length <= L with at most numOps flips?
    (define (feasible? L)
      (let* ((dp-prev (list (make-vector (+ L 1) INF)   ; for ending char '0'
                            (make-vector (+ L 1) INF))) ; for ending char '1'
             (first-val (char->int (string-ref s 0))))
        ;; initialize first position
        (vector-set! (list-ref dp-prev 0) 1 (if (= first-val 0) 0 1))
        (vector-set! (list-ref dp-prev 1) 1 (if (= first-val 1) 0 1))

        ;; process remaining positions
        (let loop ((i 2) (dp-prev dp-prev))
          (if (> i n)
              ;; after processing all characters, check minimal flips used
              (let ((ok? #f))
                (for ([c (in-range 2)])
                  (let ((vec (list-ref dp-prev c)))
                    (for ([len (in-range 1 (+ L 1))])
                      (when (<= (vector-ref vec len) numOps)
                        (set! ok? #t)))))
                ok?)
              (let* ((dp-curr (list (make-vector (+ L 1) INF)
                                    (make-vector (+ L 1) INF)))
                     (cur-char (char->int (string-ref s (- i 1)))))
                (for ([prevc (in-range 2)])
                  (let ((prev-vec (list-ref dp-prev prevc)))
                    (for ([lenPrev (in-range 1 (+ L 1))])
                      (let ((prev-cost (vector-ref prev-vec lenPrev)))
                        (when (< prev-cost INF)
                          (for ([ch (in-range 2)])
                            (define newLen (if (= ch prevc) (+ lenPrev 1) 1))
                            (when (<= newLen L)
                              (define add (if (= cur-char ch) 0 1))
                              (define newCost (+ prev-cost add))
                              (let ((curr-vec (list-ref dp-curr ch)))
                                (when (< newCost (vector-ref curr-vec newLen))
                                  (vector-set! curr-vec newLen newCost))))))))))
                (loop (+ i 1) dp-curr))))))

    ;; binary search on answer
    (let loop ((lo 1) (hi n))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (feasible? mid)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_length/2]).

-define(INF, 1000000000).

-spec min_length(S :: unicode:unicode_binary(), NumOps :: integer()) -> integer().
min_length(S, NumOps) ->
    CharList = [B - $0 || B <- binary:bin_to_list(S)],
    N = length(CharList),
    binary_search(1, N, CharList, NumOps).

binary_search(Low, High, _CharList, _K) when Low >= High ->
    Low;
binary_search(Low, High, CharList, K) ->
    Mid = (Low + High) div 2,
    case feasible(Mid, CharList, K) of
        true -> binary_search(Low, Mid, CharList, K);
        false -> binary_search(Mid + 1, High, CharList, K)
    end.

feasible(MaxRun, CharList, K) ->
    [First | Rest] = CharList,
    Cost0 = if First == 0 -> 0; true -> 1 end,
    Cost1 = if First == 1 -> 0; true -> 1 end,
    PrevZero = maps:put(1, Cost0, #{}),
    PrevOne  = maps:put(1, Cost1, #{}),
    {FinalZero, FinalOne} =
        lists:foldl(
            fun(Char, {PZ, PO}) ->
                process_char(PZ, PO, Char, MaxRun)
            end,
            {PrevZero, PrevOne},
            Rest
        ),
    MinCost = min_maps(FinalZero, FinalOne),
    MinCost =< K.

process_char(PrevZero, PrevOne, Char, MaxRun) ->
    {NZ0, NO0} = {#{}, #{}},
    {NZ1, NO1} =
        maps:fold(
            fun(Len, Cost, {NZAcc, NOAcc}) ->
                NZAcc2 = case Len + 1 =< MaxRun of
                    true ->
                        C0 = Cost + (if Char == 0 -> 0; true -> 1 end),
                        maybe_min_put(NZAcc, Len + 1, C0);
                    false -> NZAcc
                end,
                C1 = Cost + (if Char == 1 -> 0; true -> 1 end),
                NOAcc2 = maybe_min_put(NOAcc, 1, C1),
                {NZAcc2, NOAcc2}
            end,
            {NZ0, NO0},
            PrevZero
        ),
    {NZ2, NO2} =
        maps:fold(
            fun(Len, Cost, {NZAcc, NOAcc}) ->
                NOAcc2 = case Len + 1 =< MaxRun of
                    true ->
                        C1 = Cost + (if Char == 1 -> 0; true -> 1 end),
                        maybe_min_put(NOAcc, Len + 1, C1);
                    false -> NOAcc
                end,
                C0 = Cost + (if Char == 0 -> 0; true -> 1 end),
                NZAcc2 = maybe_min_put(NZAcc, 1, C0),
                {NZAcc2, NOAcc2}
            end,
            {NZ1, NO1},
            PrevOne
        ),
    {NZ2, NO2}.

maybe_min_put(Map, Key, Val) ->
    case maps:get(Key, Map, ?INF) of
        Existing when Existing =< Val -> Map;
        _ -> maps:put(Key, Val, Map)
    end.

min_maps(MapA, MapB) ->
    MinA = min_map_value(MapA),
    MinB = min_map_value(MapB),
    if MinA =< MinB -> MinA; true -> MinB end.

min_map_value(Map) ->
    Values = [V || {_K, V} <- maps:to_list(Map)],
    case Values of
        [] -> ?INF;
        _ -> lists:min(Values)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_length(s :: String.t(), num_ops :: integer) :: integer
  def min_length(s, num_ops) do
    n = String.length(s)
    prefix = build_prefix(s, n)

    binary_search(1, n, s, n, num_ops, prefix)
  end

  # Build prefix sum array of number of '1's.
  defp build_prefix(s, n) do
    arr = :array.new(n + 1, default: 0)

    {arr_final, _} =
      Enum.reduce(0..(n - 1), {arr, 0}, fn i, {a, sum} ->
        bit = if :binary.at(s, i) == ?1, do: 1, else: 0
        new_sum = sum + bit
        a2 = :array.set(i + 1, new_sum, a)
        {a2, new_sum}
      end)

    arr_final
  end

  # Binary search for minimal feasible maximum run length.
  defp binary_search(low, high, s, n, k, prefix) do
    if low < high do
      mid = div(low + high, 2)

      if feasible?(n, k, mid, prefix) do
        binary_search(low, mid, s, n, k, prefix)
      else
        binary_search(mid + 1, high, s, n, k, prefix)
      end
    else
      low
    end
  end

  # Check if we can achieve max run length <= m with at most k flips.
  defp feasible?(n, k, m, prefix) do
    inf = 1_000_000
    dp0 = :array.new(n + 1, default: inf)
    dp1 = :array.new(n + 1, default: inf)

    dp0 = :array.set(0, 0, dp0)
    dp1 = :array.set(0, 0, dp1)

    {dp0_final, dp1_final} =
      Enum.reduce(1..n, {dp0, dp1}, fn i, {dp0_acc, dp1_acc} ->
        max_len = if m < i, do: m, else: i

        {min0, min1} =
          Enum.reduce(1..max_len, {inf, inf}, fn len, {cur0, cur1} ->
            j = i - len + 1
            prev_idx = j - 1

            ones = :array.get(i, prefix) - :array.get(j - 1, prefix)
            cost0 = ones
            cost1 = len - ones

            {prev_for_0, prev_for_1} =
              if prev_idx == 0 do
                {0, 0}
              else
                {:array.get(prev_idx, dp1_acc), :array.get(prev_idx, dp0_acc)}
              end

            cand0 = prev_for_0 + cost0
            cand1 = prev_for_1 + cost1

            {min(cur0, cand0), min(cur1, cand1)}
          end)

        dp0_new = :array.set(i, min0, dp0_acc)
        dp1_new = :array.set(i, min1, dp1_acc)
        {dp0_new, dp1_new}
      end)

    final_min = Enum.min([:array.get(n, dp0_final), :array.get(n, dp1_final)])
    final_min <= k
  end
end
```
