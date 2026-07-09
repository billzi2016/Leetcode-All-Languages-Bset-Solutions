# 3621. Number of Integers With Popcount-Depth Equal to K I

## Cpp

```cpp
class Solution {
public:
    long long popcountDepth(long long n, int k) {
        if (n <= 0) return 0;
        // depth for values up to 64
        const int MAXV = 65;
        vector<int> depth(MAXV, -1);
        depth[1] = 0;
        for (int i = 2; i < MAXV; ++i) {
            int x = i, d = 0;
            while (x != 1 && x > 0) {
                x = __builtin_popcountll(x);
                ++d;
            }
            depth[i] = (x == 1 ? d : -1);
        }

        if (k == 0) {
            // only number 1 has depth 0
            return n >= 1 ? 1 : 0;
        }

        int targetDepth = k - 1; // we need popcount(x) to have this depth

        // extract bits of n
        vector<int> bits;
        for (int i = 63; i >= 0; --i) {
            if ((n >> i) & 1LL) {
                for (int j = i; j >= 0; --j) bits.push_back((n >> j) & 1);
                break;
            }
        }
        int len = bits.size();
        // dp[pos][cnt][tight]
        vector<vector<long long>> cur(len + 1, vector<long long>(2, 0));
        vector<vector<long long>> nxt(len + 1, vector<long long>(2, 0));
        // start with zero bits processed, cnt=0, tight=1
        vector<vector<long long>> dp_cnt_tight(len + 1, vector<long long>(2, 0));
        dp_cnt_tight[0][1] = 1;

        for (int pos = 0; pos < len; ++pos) {
            // reset next layer
            vector<vector<long long>> ndp(len + 1, vector<long long>(2, 0));
            for (int cnt = 0; cnt <= pos; ++cnt) {
                for (int tight = 0; tight <= 1; ++tight) {
                    long long ways = dp_cnt_tight[cnt][tight];
                    if (!ways) continue;
                    int limit = tight ? bits[pos] : 1;
                    for (int b = 0; b <= limit; ++b) {
                        int ntight = (tight && b == limit) ? 1 : 0;
                        ndp[cnt + b][ntight] += ways;
                    }
                }
            }
            dp_cnt_tight.swap(ndp);
        }

        // total numbers for each popcount
        vector<long long> cntWays(len + 1, 0);
        for (int cnt = 0; cnt <= len; ++cnt) {
            cntWays[cnt] = dp_cnt_tight[cnt][0] + dp_cnt_tight[cnt][1];
        }

        long long ans = 0;
        for (int cnt = 1; cnt <= len; ++cnt) { // cnt=0 corresponds to number 0, ignore
            if (depth[cnt] == targetDepth) {
                ans += cntWays[cnt];
            }
        }

        // exclude the number 1 when k==1 because its depth is 0 not 1
        if (k == 1 && n >= 1) {
            ans -= 1;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long popcountDepth(long n, int k) {
        if (k == 0) {
            return n >= 1 ? 1L : 0L;
        }
        // precompute combinations up to 64
        long[][] comb = new long[65][65];
        for (int i = 0; i <= 64; i++) {
            comb[i][0] = comb[i][i] = 1L;
            for (int j = 1; j < i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        // depth for popcount values up to 64
        int[] depth = new int[65];
        for (int i = 0; i < depth.length; i++) depth[i] = -1;
        depth[1] = 0;
        for (int i = 2; i <= 64; i++) {
            int pc = Integer.bitCount(i);
            depth[i] = 1 + depth[pc];
        }

        // count numbers in [0, n] with exact number of ones
        int msb = 63 - Long.numberOfLeadingZeros(n);
        int maxBits = msb + 1;
        long[] cnt = new long[maxBits + 1];
        int onesSoFar = 0;
        for (int i = msb; i >= 0; i--) {
            if (((n >> i) & 1L) != 0) {
                int remaining = i;
                for (int j = 0; j <= remaining; j++) {
                    cnt[onesSoFar + j] += comb[remaining][j];
                }
                onesSoFar++;
            }
        }
        // include n itself
        cnt[onesSoFar]++;

        long ans = 0L;
        int targetDepth = k - 1;
        for (int t = 0; t < cnt.length; t++) {
            if (depth[t] == targetDepth) {
                ans += cnt[t];
            }
        }
        // exclude the number 1 which has depth 0, not 1
        if (k == 1 && n >= 1) {
            ans--;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def popcountDepth(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        from math import comb

        maxbits = n.bit_length()
        # count numbers in [0, n] with exactly t ones
        cnt = [0] * (maxbits + 1)
        ones_sofar = 0
        bits = [(n >> i) & 1 for i in range(maxbits - 1, -1, -1)]

        for idx, b in enumerate(bits):
            remaining = maxbits - idx - 1
            if b == 1:
                # set this bit to 0 and choose remaining bits freely
                for total in range(ones_sofar, maxbits + 1):
                    need = total - ones_sofar
                    if 0 <= need <= remaining:
                        cnt[total] += comb(remaining, need)
                ones_sofar += 1

        # include n itself
        cnt[ones_sofar] += 1

        # precompute depth for values up to at least maxbits (and up to 64 for safety)
        limit = max(maxbits, 64)
        depth = [0] * (limit + 1)
        depth[1] = 0
        for i in range(2, limit + 1):
            depth[i] = 1 + depth[i.bit_count()]

        ans = 0
        if k == 0 and n >= 1:
            ans += 1  # only number 1 has depth 0

        for ones in range(1, maxbits + 1):
            d = 1 + depth[ones]  # depth of any number with this popcount (except the number 1)
            if d == k:
                add = cnt[ones]
                if ones == 1:
                    add -= 1  # exclude the number 1 which has depth 0
                ans += add

        return ans
```

## Python3

```python
import math

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if n < 1:
            return 0
        # precompute depth for possible popcounts (up to 64 bits)
        max_bits = n.bit_length()
        limit = max(64, max_bits + 2)
        depth = [10] * (limit + 1)  # large sentinel
        depth[1] = 0
        for i in range(2, limit + 1):
            x = i
            d = 0
            while x != 1:
                x = bin(x).count('1')
                d += 1
            depth[i] = d

        # helper: count numbers in [0, n] with exactly j ones
        def count_exact(j: int) -> int:
            if j < 0:
                return 0
            ans = 0
            ones_sofar = 0
            for pos in range(max_bits - 1, -1, -1):
                if (n >> pos) & 1:
                    # set this bit to 0, choose remaining needed ones from lower bits
                    need = j - ones_sofar
                    if 0 <= need <= pos:
                        ans += math.comb(pos, need)
                    ones_sofar += 1
            if ones_sofar == j:
                ans += 1
            return ans

        # k == 0 : only number 1 qualifies
        if k == 0:
            return 1 if n >= 1 else 0

        target_depth = k - 1
        total = 0
        for ones in range(1, max_bits + 1):
            if depth[ones] == target_depth:
                total += count_exact(ones)

        # exclude the number 1 which has depth 0 but was counted when k==1 (popcnt=1)
        if k == 1 and n >= 1:
            total -= 1

        return total
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

long long popcountDepth(long long n, int k) {
    if (n <= 0) return 0;
    static int depth[65];
    for (int i = 0; i < 65; ++i) depth[i] = -1;
    function<int(int)> dfs = [&](int x) -> int {
        if (x == 1) return 0;
        if (depth[x] != -1) return depth[x];
        int pc = __builtin_popcount(x);
        depth[x] = 1 + dfs(pc);
        return depth[x];
    };
    for (int i = 1; i < 65; ++i) dfs(i);

    if (k == 0) return n >= 1 ? 1 : 0;

    vector<int> bits;
    for (int i = 63; i >= 0; --i) {
        if ((n >> i) & 1LL) {
            for (int j = i; j >= 0; --j)
                bits.push_back((n >> j) & 1LL);
            break;
        }
    }
    int len = bits.size();
    vector<vector<long long>> dp(2, vector<long long>(len + 1, 0));
    dp[1][0] = 1;
    for (int pos = 0; pos < len; ++pos) {
        vector<vector<long long>> ndp(2, vector<long long>(len + 1, 0));
        for (int tight = 0; tight <= 1; ++tight) {
            for (int ones = 0; ones <= len; ++ones) {
                long long cur = dp[tight][ones];
                if (!cur) continue;
                int maxBit = tight ? bits[pos] : 1;
                for (int b = 0; b <= maxBit; ++b) {
                    int ntight = (tight && b == maxBit);
                    ndp[ntight][ones + b] += cur;
                }
            }
        }
        dp.swap(ndp);
    }

    vector<long long> cnt(len + 1, 0);
    for (int tight = 0; tight <= 1; ++tight)
        for (int ones = 0; ones <= len; ++ones)
            cnt[ones] += dp[tight][ones];

    long long ans = 0;
    for (int c = 1; c <= len; ++c) {
        if (depth[c] == k - 1) {
            long long add = cnt[c];
            if (c == 1 && n >= 1) add -= 1; // exclude the number 1
            ans += add;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long PopcountDepth(long n, int k) {
        const int MAX = 64;
        // Precompute combinations C[i][j]
        long[,] C = new long[MAX + 1, MAX + 1];
        for (int i = 0; i <= MAX; i++) {
            C[i, 0] = C[i, i] = 1;
            for (int j = 1; j < i; j++) {
                C[i, j] = C[i - 1, j - 1] + C[i - 1, j];
            }
        }

        // Precompute depth for numbers up to MAX
        int[] depth = new int[MAX + 1];
        depth[0] = -1;
        for (int i = 1; i <= MAX; i++) {
            int d = 0;
            int x = i;
            while (x != 1) {
                x = Popcnt(x);
                d++;
            }
            depth[i] = d;
        }

        // Helper: count numbers in [0, n] with exactly target ones
        long CountOnes(int target) {
            if (target < 0) return 0;
            long res = 0;
            int onesSoFar = 0;

            int msb = -1;
            for (int i = MAX - 1; i >= 0; --i) {
                if (((n >> i) & 1L) != 0) {
                    msb = i;
                    break;
                }
            }
            if (msb == -1) { // n == 0
                return target == 0 ? 1 : 0;
            }

            for (int i = msb; i >= 0; --i) {
                bool bit = ((n >> i) & 1L) != 0;
                if (bit) {
                    int remaining = i;
                    int need = target - onesSoFar;
                    if (need >= 0 && need <= remaining) {
                        res += C[remaining, need];
                    }
                    onesSoFar++;
                    if (onesSoFar > target) break;
                }
            }
            if (onesSoFar == target) {
                res += 1; // n itself
            }
            return res;
        }

        long ans = 0;
        if (k == 0) {
            if (n >= 1) ans = 1; // only the number 1
            return ans;
        }

        for (int j = 1; j <= MAX; j++) {
            if (j == 1) {
                if (k == 1) {
                    long cnt = CountOnes(1);
                    // exclude the number 1 itself, whose depth is 0
                    cnt -= 1;
                    ans += cnt;
                }
                continue;
            }
            int totalDepth = 1 + depth[j];
            if (totalDepth == k) {
                ans += CountOnes(j);
            }
        }

        return ans;
    }

    private int Popcnt(int x) {
        int cnt = 0;
        while (x > 0) {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var popcountDepth = function(n, k) {
    // precompute binomial coefficients up to 60 (enough for given constraints)
    const MAXB = 60;
    const C = Array.from({length: MAXB + 1}, () => new Array(MAXB + 1).fill(0));
    for (let i = 0; i <= MAXB; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    // popcount for small integers
    const popcnt = (x) => {
        let cnt = 0;
        while (x > 0) {
            cnt += x & 1;
            x >>>= 1;
        }
        return cnt;
    };

    // depth for values up to MAXB
    const depth = new Array(MAXB + 1).fill(0);
    depth[1] = 0;
    for (let i = 2; i <= MAXB; i++) {
        depth[i] = 1 + depth[popcnt(i)];
    }

    // binary representation of n
    const bits = n.toString(2).split('').map(ch => ch === '1' ? 1 : 0);
    const L = bits.length;

    // cnt[j]: numbers in [0, n] with exactly j ones
    const cnt = new Array(L + 1).fill(0);
    let onesSeen = 0;
    for (let i = 0; i < L; i++) {
        if (bits[i] === 1) {
            const rem = L - i - 1;
            // set this bit to 0, distribute remaining ones
            for (let t = 0; t <= rem; t++) {
                cnt[onesSeen + t] += C[rem][t];
            }
            onesSeen++;
        }
    }
    // include n itself
    cnt[onesSeen] += 1;
    // exclude zero
    cnt[0] -= 1;

    if (k === 0) {
        return n >= 1 ? 1 : 0; // only number 1 has depth 0
    }

    let ans = 0;
    for (let j = 1; j <= L; j++) {
        if (1 + depth[j] === k) {
            let add = cnt[j];
            if (j === 1 && k === 1) {
                // remove the number 1 whose depth is actually 0
                add -= 1;
            }
            ans += add;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function popcountDepth(n: number, k: number): number {
    const MAX_BITS = 60; // enough for n <= 1e15
    // popcount of a Number (<= 2^53)
    function pc(x: number): number {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    }

    // depth for values up to MAX_BITS
    const depth = new Array(MAX_BITS + 1).fill(0);
    depth[1] = 0;
    for (let i = 2; i <= MAX_BITS; i++) {
        let cur = i, steps = 0;
        while (cur !== 1) {
            cur = pc(cur);
            steps++;
        }
        depth[i] = steps;
    }

    if (k === 0) {
        return n >= 1 ? 1 : 0; // only the number 1
    }

    // binomial coefficients C[n][k]
    const C: number[][] = Array.from({ length: MAX_BITS + 1 }, () => new Array(MAX_BITS + 1).fill(0));
    for (let i = 0; i <= MAX_BITS; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    const bits = n.toString(2);
    const L = bits.length;

    function countWithOnes(target: number): number {
        if (target < 0) return 0;
        let res = 0;
        let onesSoFar = 0;
        for (let idx = 0; idx < L; idx++) {
            if (bits[idx] === '1') {
                const remaining = L - idx - 1;
                const need = target - onesSoFar;
                if (need >= 0 && need <= remaining) {
                    res += C[remaining][need];
                }
                onesSoFar++;
                if (onesSoFar > target) break;
            }
        }
        if (onesSoFar === target) {
            res += 1; // n itself
        }
        return res;
    }

    let ans = 0;
    for (let j = 1; j <= MAX_BITS; j++) {
        if (depth[j] === k - 1) {
            ans += countWithOnes(j);
        }
    }

    // exclude the number 1 which has depth 0, not k>0
    if (k === 1 && n >= 1) {
        ans -= 1;
    }

    return ans;
}
```

## Php

```php
class Solution {
    private $C = [];
    private $depth = [];

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function popcountDepth($n, $k) {
        $max = 64;
        // precompute combinations C[i][j]
        for ($i = 0; $i <= $max; $i++) {
            $this->C[$i] = array_fill(0, $i + 1, 0);
            $this->C[$i][0] = 1;
            $this->C[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $this->C[$i][$j] = $this->C[$i - 1][$j - 1] + $this->C[$i - 1][$j];
            }
        }

        // precompute depth for numbers up to max
        $memo = [];
        $this->depth[1] = 0;
        for ($i = 2; $i <= $max; $i++) {
            $this->depth[$i] = $this->calcDepth($i, $memo);
        }

        if ($k == 0) {
            return $n >= 1 ? 1 : 0;
        }

        $target = $k - 1;
        $ans = 0;
        for ($j = 1; $j <= $max; $j++) {
            if ($this->depth[$j] == $target) {
                $cnt = $this->countExactOnes($n, $j);
                $ans += $cnt;
            }
        }

        // exclude the number 1 which was counted when k==1
        if ($k == 1) {
            $ans -= 1;
        }

        return $ans;
    }

    private function calcDepth(int $x, array &$memo): int {
        if ($x == 1) return 0;
        if (isset($memo[$x])) return $memo[$x];
        $pc = $this->popcountInt($x);
        $memo[$x] = 1 + $this->calcDepth($pc, $memo);
        return $memo[$x];
    }

    private function popcountInt(int $x): int {
        $cnt = 0;
        while ($x > 0) {
            $cnt += $x & 1;
            $x >>= 1;
        }
        return $cnt;
    }

    private function countExactOnes(int $n, int $ones): int {
        if ($ones < 0) return 0;
        // extract bits of n (least significant first)
        $bits = [];
        $temp = $n;
        while ($temp > 0) {
            $bits[] = $temp & 1;
            $temp >>= 1;
        }
        $len = count($bits);
        $remaining = $ones;
        $cnt = 0;

        for ($i = $len - 1; $i >= 0; $i--) {
            if ($bits[$i] == 1) {
                if ($remaining <= $i && $remaining >= 0) {
                    $cnt += $this->C[$i][$remaining];
                }
                $remaining--;
                if ($remaining < 0) break;
            }
        }

        if ($remaining == 0) {
            $cnt += 1; // n itself
        }

        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func popcountDepth(_ n: Int, _ k: Int) -> Int {
        if n <= 0 { return 0 }
        
        // Precompute depth for values up to 64
        var depth = Array(repeating: -1, count: 65)
        func getDepth(_ v: Int) -> Int {
            if v == 1 { return 0 }
            if depth[v] != -1 { return depth[v] }
            let pc = v.nonzeroBitCount
            let d = 1 + getDepth(pc)
            depth[v] = d
            return d
        }
        for i in 2...64 {
            _ = getDepth(i)
        }
        
        // Binary representation of n (most significant bit first)
        var bits: [Int] = []
        var temp = n
        while temp > 0 {
            bits.append(temp & 1)
            temp >>= 1
        }
        if bits.isEmpty { bits.append(0) }
        bits.reverse()
        let L = bits.count
        
        // dp[pos][cnt][tight]
        var dp = Array(
            repeating: Array(
                repeating: Array(repeating: Int64(0), count: 2),
                count: L + 1
            ),
            count: L + 1
        )
        dp[0][0][1] = 1
        
        if L > 0 {
            for pos in 0..<L {
                for cnt in 0...pos {
                    for tight in 0...1 {
                        let cur = dp[pos][cnt][tight]
                        if cur == 0 { continue }
                        let limit = (tight == 1) ? bits[pos] : 1
                        for b in 0...limit {
                            let ntight = (tight == 1 && b == limit) ? 1 : 0
                            dp[pos + 1][cnt + b][ntight] += cur
                        }
                    }
                }
            }
        }
        
        var finalCounts = Array(repeating: Int64(0), count: L + 1)
        for cnt in 0...L {
            finalCounts[cnt] = dp[L][cnt][0] + dp[L][cnt][1]
        }
        // Exclude the number 0
        if finalCounts[0] > 0 { finalCounts[0] -= 1 }
        
        var ans: Int64 = 0
        if k == 0 {
            ans = n >= 1 ? 1 : 0
        } else {
            let targetDepth = k - 1
            for cnt in 1...L {
                if depth[cnt] == targetDepth {
                    ans += finalCounts[cnt]
                }
            }
            // Exclude the number 1 which was incorrectly counted when k == 1
            if k == 1 && n >= 1 { ans -= 1 }
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun popcountDepth(n: Long, k: Int): Long {
        if (n <= 0L) return 0L
        val MAX_BITS = 61

        // Precompute combinations C[i][j] for i,j up to MAX_BITS
        val comb = Array(MAX_BITS + 1) { LongArray(MAX_BITS + 1) }
        for (i in 0..MAX_BITS) {
            comb[i][0] = 1L
            comb[i][i] = 1L
            for (j in 1 until i) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }

        // Precompute depth for popcount values up to MAX_BITS
        val depth = IntArray(MAX_BITS + 1)
        depth[1] = 0
        for (i in 2..MAX_BITS) {
            val pc = Integer.bitCount(i)
            depth[i] = 1 + depth[pc]
        }

        if (k == 0) {
            return if (n >= 1L) 1L else 0L
        }

        // Count numbers <= n with exactly j ones in binary representation
        val cnt = LongArray(MAX_BITS + 1)
        var onesSeen = 0
        for (i in MAX_BITS - 1 downTo 0) {
            if ((n and (1L shl i)) != 0L) {
                val rem = i
                for (t in 0..rem) {
                    cnt[onesSeen + t] += comb[rem][t]
                }
                onesSeen++
            }
        }
        // Include n itself
        cnt[onesSeen]++

        var ans = 0L
        for (j in 1..MAX_BITS) {
            if (depth[j] == k - 1) {
                ans += cnt[j]
            }
        }
        // Exclude the number 1 when k == 1 because its depth is 0
        if (k == 1 && n >= 1L) {
            ans -= 1L
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int popcountDepth(int n, int k) {
    if (n < 1) return 0;
    if (k == 0) {
      // only the number 1 has depth 0
      return n >= 1 ? 1 : 0;
    }

    // binary representation of n (most significant bit first)
    List<int> bits = [];
    int temp = n;
    while (temp > 0) {
      bits.add(temp & 1);
      temp >>= 1;
    }
    bits = bits.reversed.toList();
    int L = bits.length; // maximum possible number of ones

    // binomial coefficients C[i][j] for i,j <= L
    List<List<int>> C = List.generate(L + 1, (_) => List.filled(L + 1, 0));
    for (int i = 0; i <= L; ++i) {
      C[i][0] = C[i][i] = 1;
      for (int j = 1; j < i; ++j) {
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
      }
    }

    // cnt[j] = numbers in [0, n] with exactly j ones
    List<int> cnt = List.filled(L + 1, 0);
    int onesSeen = 0;
    for (int i = 0; i < L; ++i) {
      if (bits[i] == 1) {
        int remaining = L - i - 1;
        // set this bit to 0 and choose need ones among remaining bits
        for (int j = onesSeen; j <= L; ++j) {
          int need = j - onesSeen;
          if (need <= remaining) {
            cnt[j] += C[remaining][need];
          }
        }
        onesSeen++; // keep this bit as 1 and continue
      }
    }
    // include n itself
    cnt[onesSeen] += 1;

    // depth for popcount values up to L
    List<int> depth = List.filled(L + 1, -1);
    depth[1] = 0;
    int computeDepth(int x) {
      if (depth[x] != -1) return depth[x];
      int pc = 0;
      int y = x;
      while (y > 0) {
        pc += y & 1;
        y >>= 1;
      }
      depth[x] = 1 + computeDepth(pc);
      return depth[x];
    }

    for (int j = 2; j <= L; ++j) computeDepth(j);

    int target = k - 1;
    int ans = 0;
    for (int j = 1; j <= L; ++j) {
      if (depth[j] == target) {
        ans += cnt[j];
      }
    }

    // exclude the number 1 which was counted in cnt[1] but has depth 0
    if (k == 1 && n >= 1) {
      ans -= 1;
    }

    return ans;
  }
}
```

## Golang

```go
import "math/bits"

var comb [65][65]int64

func init() {
	for i := 0; i <= 64; i++ {
		comb[i][0] = 1
		comb[i][i] = 1
		for j := 1; j < i; j++ {
			comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
		}
	}
}

func countWithOnes(n int64, ones int) int64 {
	if ones < 0 {
		return 0
	}
	var res int64
	cur := 0
	for i := 63; i >= 0; i-- {
		if (n>>i)&1 == 1 {
			need := ones - cur
			if need >= 0 && need <= i {
				res += comb[i][need]
			}
			cur++
		}
	}
	if cur == ones {
		res++
	}
	return res
}

func popcountDepth(n int64, k int) int64 {
	if n < 1 {
		return 0
	}
	if k == 0 {
		if n >= 1 {
			return 1
		}
		return 0
	}
	const maxVal = 64
	depth := make([]int, maxVal+1)
	for i := 2; i <= maxVal; i++ {
		x := i
		d := 0
		for x != 1 {
			x = bits.OnesCount(uint(x))
			d++
		}
		depth[i] = d
	}
	var ans int64
	for j := 1; j <= maxVal; j++ {
		targetDepth := 1 + depth[j]
		if targetDepth == k {
			cnt := countWithOnes(n, j)
			if j == 1 && k == 1 {
				// exclude the number 1 itself (depth 0)
				if n >= 1 {
					cnt--
				}
			}
			ans += cnt
		}
	}
	return ans
}
```

## Ruby

```ruby
def popcount_depth(n, k)
  # binary representation bits from MSB to LSB
  bits = n.to_s(2).chars.map { |c| c.ord - 48 }
  len = bits.length
  max_ones = len

  # dp[pos][ones][tight] => count
  dp = Array.new(len + 1) { Array.new(max_ones + 1) { [0, 0] } }
  dp[0][0][1] = 1

  (0...len).each do |pos|
    limit_bit = bits[pos]
    (0..pos).each do |ones|
      2.times do |tight|
        cur = dp[pos][ones][tight]
        next if cur == 0
        max_bit = tight == 1 ? limit_bit : 1
        (0..max_bit).each do |b|
          new_ones = ones + b
          new_tight = (tight == 1 && b == limit_bit) ? 1 : 0
          dp[pos + 1][new_ones][new_tight] += cur
        end
      end
    end
  end

  cnt = Array.new(max_ones + 1, 0)
  (0..max_ones).each do |j|
    cnt[j] = dp[len][j][0] + dp[len][j][1]
  end
  # exclude number 0
  cnt[0] -= 1 if cnt[0] > 0

  # precompute depth for possible popcounts (0..max_ones)
  depth = Array.new(max_ones + 1, -1)
  (0..max_ones).each do |j|
    next if j == 0
    d = 0
    x = j
    while x != 1
      x = x.to_s(2).count('1')
      d += 1
    end
    depth[j] = d
  end

  if k == 0
    return n >= 1 ? 1 : 0
  else
    target = k - 1
    ans = 0
    (0..max_ones).each do |j|
      next unless depth[j] == target
      ans += cnt[j]
    end
    # remove the special case of x = 1 which was counted when j = 1 and k = 1
    if k == 1 && n >= 1
      ans -= 1
    end
    return ans
  end
end
```

## Scala

```scala
object Solution {
    def popcountDepth(n: Long, k: Int): Long = {
        val MAX = 64
        // Precompute combinations C[n][k]
        val comb = Array.ofDim[Long](MAX + 1, MAX + 1)
        for (i <- 0 to MAX) {
            comb(i)(0) = 1L
            comb(i)(i) = 1L
            var j = 1
            while (j < i) {
                comb(i)(j) = comb(i - 1)(j - 1) + comb(i - 1)(j)
                j += 1
            }
        }

        // Precompute depth for values up to MAX
        val depth = Array.fill[Int](MAX + 1)(0)
        depth(1) = 0
        for (i <- 2 to MAX) {
            var v = i
            var d = 0
            while (v != 1) {
                v = java.lang.Long.bitCount(v)
                d += 1
            }
            depth(i) = d
        }

        // Extract bits of n (most significant first)
        val bits = new scala.collection.mutable.ArrayBuffer[Int]()
        var temp = n
        if (temp == 0L) {
            bits += 0
        } else {
            while (temp > 0) {
                bits += ((temp & 1L).toInt)
                temp >>= 1
            }
            bits.reverseInPlace()
        }
        val len = bits.length

        // cnt[j] = number of integers in [0, n] with exactly j ones
        val cnt = Array.fill[Long](MAX + 1)(0L)

        var onesSoFar = 0
        for (i <- 0 until len) {
            if (bits(i) == 1) {
                val remaining = len - i - 1
                var addOnes = 0
                while (addOnes <= remaining) {
                    cnt(onesSoFar + addOnes) += comb(remaining)(addOnes)
                    addOnes += 1
                }
                onesSoFar += 1
            }
        }
        // Include n itself
        cnt(onesSoFar) += 1

        if (k == 0) {
            if (n >= 1L) 1L else 0L
        } else {
            val target = k - 1
            var ans = 0L
            for (j <- 1 to MAX) {
                if (depth(j) == target) {
                    ans += cnt(j)
                }
            }
            // Exclude the number 1 which was counted when k == 1
            if (k == 1 && n >= 1L) ans -= 1L
            ans
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn popcount_depth(n: i64, k: i32) -> i64 {
        let n_u = n as u64;
        if n_u == 0 {
            return 0;
        }
        // depth 0 only the number 1
        if k == 0 {
            return if n_u >= 1 { 1 } else { 0 };
        }

        // binary length of n
        let mut len = 0usize;
        while (1u64 << len) <= n_u && len < 64 {
            len += 1;
        }
        // precompute combinations C[i][j] for i,j up to len
        let mut comb = vec![vec![0i64; len + 1]; len + 1];
        for i in 0..=len {
            comb[i][0] = 1;
            comb[i][i] = 1;
            for j in 1..i {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        // depth of popcount values up to len
        let mut depth = vec![0i32; len + 1];
        if len >= 1 {
            depth[1] = 0;
        }
        for v in 2..=len {
            let mut cur = v;
            let mut d = 0;
            while cur != 1 {
                cur = (cur as u32).count_ones() as usize;
                d += 1;
            }
            depth[v] = d;
        }

        // helper: count numbers <= n with exactly j ones
        fn count_with_ones(n: u64, len: usize, comb: &Vec<Vec<i64>>, j: usize) -> i64 {
            let mut cnt: i64 = 0;
            let mut ones_sofar = 0usize;
            for pos in (0..len).rev() {
                if ((n >> pos) & 1) == 1 {
                    // set this bit to 0, choose remaining ones among lower bits
                    if j >= ones_sofar {
                        let need = j - ones_sofar;
                        if need <= pos {
                            cnt += comb[pos][need];
                        }
                    }
                    ones_sofar += 1;
                }
            }
            if ones_sofar == j {
                cnt += 1; // n itself
            }
            // exclude zero when j == 0 (not needed for our main loop)
            if j == 0 && n >= 0 {
                cnt -= 1;
            }
            cnt
        }

        let mut ans: i64 = 0;
        for j in 1..=len {
            if depth[j] == k - 1 {
                ans += count_with_ones(n_u, len, &comb, j);
            }
        }
        // exclude the number 1 when k == 1 (its depth is 0)
        if k == 1 {
            ans -= 1;
        }
        ans
    }
}
```

## Racket

```racket
(define (int-to-bits n)
  (if (= n 0)
      '(0)
      (let loop ((x n) (acc '()))
        (if (= x 0)
            acc
            (loop (arithmetic-shift x -1) (cons (bitwise-and x 1) acc))))))

(define (popcount-depth-of j)
  (let loop ((v j) (d 0))
    (if (= v 1)
        d
        (loop (bitwise-bit-count v) (+ d 1)))))

(define/contract (popcount-depth n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (cond
    [(= k 0) (if (>= n 1) 1 0)]
    [else
     (let* ((bits (int-to-bits n))
            (L (length bits))
            (size (+ L 1))
            (dp0 (make-vector size 0))
            (dp1 (make-vector size 0)))
       (vector-set! dp1 0 1)
       (for ([i (in-range L)])
         (define b (list-ref bits i))
         (define ndp0 (make-vector size 0))
         (define ndp1 (make-vector size 0))
         ;; transitions from tight = 0
         (for ([cnt (in-range size)])
           (define cur (vector-ref dp0 cnt))
           (when (> cur 0)
             ;; put 0
             (let ((newcnt cnt))
               (vector-set! ndp0 newcnt (+ (vector-ref ndp0 newcnt) cur)))
             ;; put 1
             (when (< (+ cnt 1) size)
               (let ((newcnt (+ cnt 1)))
                 (vector-set! ndp0 newcnt (+ (vector-ref ndp0 newcnt) cur))))))
         ;; transitions from tight = 1
         (for ([cnt (in-range size)])
           (define cur (vector-ref dp1 cnt))
           (when (> cur 0)
             (if (= b 0)
                 ;; can only put 0, stay tight
                 (let ((newcnt cnt))
                   (vector-set! ndp1 newcnt (+ (vector-ref ndp1 newcnt) cur)))
                 ;; b == 1
                 (begin
                   ;; choose 0 -> not tight
                   (let ((newcnt cnt))
                     (vector-set! ndp0 newcnt (+ (vector-ref ndp0 newcnt) cur)))
                   ;; choose 1 -> stay tight
                   (let ((newcnt (+ cnt 1)))
                     (when (< newcnt size)
                       (vector-set! ndp1 newcnt (+ (vector-ref ndp1 newcnt) cur)))))))))
         (set! dp0 ndp0)
         (set! dp1 ndp1))
       ;; total counts per popcount
       (define total (make-vector size 0))
       (for ([j (in-range size)])
         (vector-set! total j (+ (vector-ref dp0 j) (vector-ref dp1 j))))
       (define target (- k 1))
       (define ans 0)
       (for ([j (in-range 1 size)]) ; popcount cannot be 0 for positive numbers
         (when (= (popcount-depth-of j) target)
           (let ((cnt (vector-ref total j)))
             (when (and (= j 1) (> n 0))
               (set! cnt (- cnt 1))) ; exclude the number 1 itself
             (set! ans (+ ans cnt)))))
       ans)]))
```

## Erlang

```erlang
-module(solution).
-export([popcount_depth/2]).

-spec popcount_depth(N :: integer(), K :: integer()) -> integer().
popcount_depth(N, K) when N >= 1, K >= 0 ->
    Counts = count_ones_up_to(N),
    maps:fold(
        fun(Ones, Cnt, Acc) ->
            case depth(Ones) of
                K -> Acc + Cnt;
                _ -> Acc
            end
        end,
        0,
        Counts).

%% Count numbers in [0, N] grouped by their popcount.
count_ones_up_to(N) ->
    Bits = bits_list(N),
    count_loop(Bits, 0, maps:new()).

%% Recursive processing of bits.
count_loop([], OnesSoFar, Map) ->
    add_count(Map, OnesSoFar, 1); % include N itself
count_loop([Bit | Rest], OnesSoFar, Map) when Bit =:= 1 ->
    Rem = length(Rest),
    NewMap = add_combinations(Rem, OnesSoFar, Map),
    count_loop(Rest, OnesSoFar + 1, NewMap);
count_loop([_Bit | Rest], OnesSoFar, Map) ->
    % Bit == 0
    count_loop(Rest, OnesSoFar, Map).

%% Add combinations for setting current 1-bit to 0 and free lower bits.
add_combinations(Rem, BaseOnes, Map) ->
    add_combination_loop(Rem, 0, BaseOnes, Map).

add_combination_loop(_Rem, J, _BaseOnes, Map) when J > _Rem ->
    Map;
add_combination_loop(Rem, J, BaseOnes, Map) ->
    C = nck(Rem, J),
    UpdatedMap = add_count(Map, BaseOnes + J, C),
    add_combination_loop(Rem, J + 1, BaseOnes, UpdatedMap).

%% Add value to map entry.
add_count(Map, Key, Add) ->
    maps:update_with(Key,
        fun(Old) -> Old + Add end,
        Add,
        Map).

%% Compute n choose k (k <= n <= 64).
nck(N, K) when K < 0; K > N -> 0;
nck(_N, 0) -> 1;
nck(N, K) ->
    K1 = if K > N - K -> N - K; true -> K end,
    nck_mul(N, K1, 1).

nck_mul(_, 0, Acc) -> Acc;
nck_mul(N, K, Acc) ->
    NewAcc = Acc * (N - K + 1) div K,
    nck_mul(N, K - 1, NewAcc).

%% Depth of popcount-depth for a given number.
depth(1) -> 0;
depth(0) -> -1; % never used
depth(N) ->
    1 + depth(popcnt(N)).

%% Popcount of an integer.
popcnt(N) when N >= 0 -> popcnt(N, 0).

popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N band (N - 1), Acc + 1).

%% Convert integer to list of bits (MSB first).
bits_list(N) when N > 0 ->
    lists:reverse(bits_rev(N, [])).

bits_rev(0, Acc) -> Acc;
bits_rev(N, Acc) ->
    bits_rev(N bsr 1, [(N band 1) | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec popcount_depth(n :: integer, k :: integer) :: integer
  def popcount_depth(n, k) do
    cond do
      k == 0 ->
        if n >= 1, do: 1, else: 0

      true ->
        target = k - 1
        max_bits = floor_log2(n) + 1
        total =
          Enum.reduce(1..max_bits, 0, fn j, acc ->
            if depth_of(j) == target do
              acc + count_with_ones(n, j)
            else
              acc
            end
          end)

        # exclude the number 1 which has depth 0, not k>0
        if k == 1 and n >= 1 do
          total - 1
        else
          total
        end
    end
  end

  # count numbers in [0, n] with exactly j ones in binary representation
  defp count_with_ones(n, j) do
    max_pos = floor_log2(n)

    {ans, need} =
      Enum.reduce_while(max_pos..0, {0, j}, fn pos, {acc, need} ->
        if ((n >>> pos) &&& 1) == 1 do
          new_acc = acc + comb(pos, need)
          new_need = need - 1

          if new_need < 0 do
            {:halt, {new_acc, new_need}}
          else
            {:cont, {new_acc, new_need}}
          end
        else
          {:cont, {acc, need}}
        end
      end)

    if need == 0 do
      ans + 1
    else
      ans
    end
  end

  # combination n choose k (k <= n <= 64)
  defp comb(_n, _k) when _k < 0, do: 0
  defp comb(n, k) when k > n, do: 0
  defp comb(n, k) do
    k = if k > n - k, do: n - k, else: k

    Enum.reduce(1..k, 1, fn i, acc ->
      div(acc * (n - k + i), i)
    end)
  end

  # depth of a small integer (<=64) defined by repeated popcount until reaching 1
  defp depth_of(1), do: 0
  defp depth_of(x) when x > 1, do: 1 + depth_of(popcnt(x))

  # popcount for small integers
  defp popcnt(0), do: 0
  defp popcnt(x), do: (x &&& 1) + popcnt(x >>> 1)

  # floor of log2 for positive integer
  defp floor_log2(n) when n > 0 do
    :math.log2(n) |> trunc()
  end
end
```
