# 3470. Permutations IV

## Cpp

```cpp
class Solution {
public:
    vector<int> permute(int n, long long k) {
        const unsigned long long INF = 4000000000000000000ULL;
        vector<unsigned long long> fact(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            __uint128_t val = (__uint128_t)fact[i - 1] * i;
            fact[i] = (val > INF) ? INF : (unsigned long long)val;
        }
        int totalOdd = (n + 1) / 2;
        int totalEven = n / 2;
        vector<bool> used(n + 1, false);
        vector<int> ans;
        int usedOdd = 0, usedEven = 0;

        auto countWays = [&](int oddRem, int evenRem, int startParity)->unsigned long long{
            if (oddRem < 0 || evenRem < 0) return 0ULL;
            int len = oddRem + evenRem;
            if (len == 0) return 1ULL;
            int needOdd, needEven;
            if (startParity == 1) { // start with odd
                needOdd = (len + 1) / 2;
                needEven = len / 2;
            } else { // start with even
                needEven = (len + 1) / 2;
                needOdd = len / 2;
            }
            if (oddRem != needOdd || evenRem != needEven) return 0ULL;
            __uint128_t val = (__uint128_t)fact[oddRem] * fact[evenRem];
            return (val > INF) ? INF : (unsigned long long)val;
        };

        for (int pos = 0; pos < n; ++pos) {
            bool placed = false;
            for (int v = 1; v <= n; ++v) {
                if (used[v]) continue;
                if (!ans.empty() && (v % 2 == ans.back() % 2)) continue; // same parity adjacent not allowed
                int oddRem = totalOdd - usedOdd - (v % 2);
                int evenRem = totalEven - usedEven - (v % 2 == 0);
                unsigned long long ways;
                if (pos == n - 1) {
                    ways = 1ULL; // last element
                } else {
                    int nextStartParity = (v % 2 == 0) ? 1 : 0; // opposite parity for the next position
                    ways = countWays(oddRem, evenRem, nextStartParity);
                }
                if (ways >= (unsigned long long)k) {
                    ans.push_back(v);
                    used[v] = true;
                    if (v % 2) ++usedOdd; else ++usedEven;
                    placed = true;
                    break;
                } else {
                    k -= ways;
                }
            }
            if (!placed) return {};
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final long INF = (long)4e18;
    private long[] fact;

    public int[] permute(int n, long k) {
        precomputeFact(n);
        int oddTotal = (n + 1) / 2;
        int evenTotal = n / 2;
        long totalWays = mulCap(fact[oddTotal], fact[evenTotal]);
        if (k > totalWays) return new int[0];

        boolean[] used = new boolean[n + 1];
        int[] res = new int[n];
        int oRem = oddTotal, eRem = evenTotal;
        int prevParity = -1; // -1 means no previous element

        for (int pos = 0; pos < n; pos++) {
            boolean placed = false;
            for (int v = 1; v <= n; v++) {
                if (used[v]) continue;
                int parity = v & 1; // 1 odd, 0 even
                if (prevParity != -1 && parity != (1 - prevParity)) continue;

                int oRem2 = oRem - (parity == 1 ? 1 : 0);
                int eRem2 = eRem - (parity == 0 ? 1 : 0);

                long cnt = countWays(oRem2, eRem2, parity == 1 ? 0 : 1);
                if (k > cnt) {
                    k -= cnt;
                } else {
                    res[pos] = v;
                    used[v] = true;
                    oRem = oRem2;
                    eRem = eRem2;
                    prevParity = parity;
                    placed = true;
                    break;
                }
            }
            if (!placed) return new int[0];
        }
        return res;
    }

    private void precomputeFact(int n) {
        fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = mulCap(fact[i - 1], i);
        }
    }

    private long countWays(int oRem, int eRem, int nextParity) {
        int len = oRem + eRem;
        if (len == 0) return (oRem == 0 && eRem == 0) ? 1 : 0;

        int oddSlots = (nextParity == 1) ? ((len + 1) / 2) : (len / 2);
        int evenSlots = len - oddSlots;
        if (oddSlots != oRem || evenSlots != eRem) return 0;
        return mulCap(fact[oddSlots], fact[evenSlots]);
    }

    private long mulCap(long a, long b) {
        if (a == 0 || b == 0) return 0;
        if (a > INF / b) return INF;
        long res = a * b;
        return res >= INF ? INF : res;
    }
}
```

## Python

```python
class Solution(object):
    def permute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        def count_possible(o, e, last_parity):
            """return number of alternating completions given remaining odds o,
               evens e and the parity of the previously placed element."""
            m = o + e
            if m == 0:
                return 1
            next_parity = 1 - last_parity  # must place opposite parity next
            needed_odds = (m + (1 if next_parity == 1 else 0)) // 2
            if o != needed_odds:
                return 0
            return fact[o] * fact[e]

        used = [False] * (n + 1)
        odds_left = (n + 1) // 2
        evens_left = n // 2
        res = []
        prev_parity = None

        for pos in range(n):
            chosen = False
            for x in range(1, n + 1):
                if used[x]:
                    continue
                cur_parity = x & 1  # 1 for odd, 0 for even
                if prev_parity is not None and cur_parity == prev_parity:
                    continue
                # compute remaining counts after picking x
                o_rem = odds_left - (1 if cur_parity == 1 else 0)
                e_rem = evens_left - (1 if cur_parity == 0 else 0)

                cnt = count_possible(o_rem, e_rem, cur_parity)
                if k > cnt:
                    k -= cnt
                    continue
                # pick x
                res.append(x)
                used[x] = True
                odds_left = o_rem
                evens_left = e_rem
                prev_parity = cur_parity
                chosen = True
                break
            if not chosen:
                return []
        return res
```

## Python3

```python
from typing import List

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        INF = 10**18

        # precompute factorials
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i
            if fact[i] > INF:
                fact[i] = INF

        def count(o: int, e: int, start_parity: int) -> int:
            """number of alternating permutations for remaining o odds and e evens,
               where the next element must have parity start_parity (1 odd, 0 even)."""
            total = o + e
            if total == 0:
                return 1
            # required number of odds in the pattern starting with start_parity
            need_odds = (total + 1) // 2 if start_parity == 1 else total // 2
            if o != need_odds or e != total - need_odds:
                return 0
            val = fact[o] * fact[e]
            return val if val <= INF else INF

        # split numbers into odds and evens, sorted
        odds = [i for i in range(1, n + 1) if i % 2 == 1]
        evens = [i for i in range(1, n + 1) if i % 2 == 0]

        total_perm = 0
        # total permutations possible
        if n % 2 == 1:
            total_perm = count(len(odds), len(evens), 1)
        else:
            total_perm = count(len(odds), len(evens), 1) + count(len(odds), len(evens), 0)

        if k > total_perm:
            return []

        result: List[int] = []
        prev_parity = None  # parity of last placed element

        while len(result) < n:
            if prev_parity is None:
                # first position: consider all remaining numbers in increasing order
                candidates = sorted(odds + evens)
                chosen = False
                for x in candidates:
                    p = x & 1
                    o_rem = len(odds) - (p == 1)
                    e_rem = len(evens) - (p == 0)
                    block = count(o_rem, e_rem, 1 - p)
                    if k > block:
                        k -= block
                        continue
                    # select x
                    result.append(x)
                    if p == 1:
                        odds.remove(x)
                    else:
                        evens.remove(x)
                    prev_parity = p
                    chosen = True
                    break
                if not chosen:
                    return []
            else:
                needed = 1 - prev_parity  # parity required now
                candidates = odds if needed == 1 else evens
                o_rem = len(odds)
                e_rem = len(evens)

                new_o = o_rem - (needed == 1)
                new_e = e_rem - (needed == 0)
                block_per_candidate = count(new_o, new_e, prev_parity)
                if block_per_candidate == 0:
                    return []

                idx = (k - 1) // block_per_candidate
                if idx >= len(candidates):
                    return []
                x = candidates[idx]
                result.append(x)
                # remove selected element
                if needed == 1:
                    odds.pop(idx)
                else:
                    evens.pop(idx)

                k -= idx * block_per_candidate
                prev_parity = needed

        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define INF ((unsigned long long)4000000000000000000ULL)  // sufficiently large > 1e15

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* permute(int n, long long k_ll, int* returnSize) {
    unsigned long long k = (unsigned long long)k_ll;
    int maxOdd = (n + 1) / 2;
    int maxEven = n / 2;

    static unsigned long long dp[101][101][2];
    for (int o = 0; o <= maxOdd; ++o) {
        for (int e = 0; e <= maxEven; ++e) {
            if (o == 0 && e == 0) {
                dp[o][e][0] = dp[o][e][1] = 1;
                continue;
            }
            // start with even
            unsigned long long valEven = 0;
            if (e > 0) {
                __int128 mul = (__int128)e * dp[o][e - 1][1];
                valEven = (mul > INF) ? INF : (unsigned long long)mul;
            }
            dp[o][e][0] = valEven;

            // start with odd
            unsigned long long valOdd = 0;
            if (o > 0) {
                __int128 mul = (__int128)o * dp[o - 1][e][0];
                valOdd = (mul > INF) ? INF : (unsigned long long)mul;
            }
            dp[o][e][1] = valOdd;
        }
    }

    unsigned long long total = dp[maxOdd][maxEven][0] + dp[maxOdd][maxEven][1];
    if (total < k) {
        *returnSize = 0;
        return NULL;
    }

    int* ans = (int*)malloc(sizeof(int) * n);
    char used[101] = {0};

    int oRem = maxOdd, eRem = maxEven;
    int prevParity = -1; // -1 means no previous
    for (int pos = 0; pos < n; ++pos) {
        for (int x = 1; x <= n; ++x) {
            if (used[x]) continue;
            int parity = x & 1; // 1 odd, 0 even
            if (prevParity != -1 && parity == prevParity) continue;

            int o2 = oRem - (parity ? 1 : 0);
            int e2 = eRem - (parity ? 0 : 1);
            unsigned long long cnt = dp[o2][e2][parity ^ 1];
            if (k > cnt) {
                k -= cnt;
                continue;
            }
            // choose x
            ans[pos] = x;
            used[x] = 1;
            prevParity = parity;
            oRem = o2;
            eRem = e2;
            break;
        }
    }

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    const long LIMIT = (long)4e18;
    long[,,] dp;
    bool[,,] vis;

    long Count(int o, int e, int prev)
    {
        if (o == 0 && e == 0) return 1;
        if (vis[o, e, prev]) return dp[o, e, prev];
        long res = 0;
        if (prev == 2) // none
        {
            if (o > 0)
            {
                long add = (long)o * Count(o - 1, e, 1);
                res += add;
                if (res > LIMIT) { res = LIMIT; }
            }
            if (e > 0)
            {
                long add = (long)e * Count(o, e - 1, 0);
                res += add;
                if (res > LIMIT) { res = LIMIT; }
            }
        }
        else if (prev == 0) // previous even, need odd
        {
            if (o > 0)
            {
                long add = (long)o * Count(o - 1, e, 1);
                res += add;
                if (res > LIMIT) { res = LIMIT; }
            }
        }
        else // prev == 1, previous odd, need even
        {
            if (e > 0)
            {
                long add = (long)e * Count(o, e - 1, 0);
                res += add;
                if (res > LIMIT) { res = LIMIT; }
            }
        }

        vis[o, e, prev] = true;
        dp[o, e, prev] = res;
        return res;
    }

    public int[] Permute(int n, long k)
    {
        int oddTotal = (n + 1) / 2;
        int evenTotal = n / 2;

        dp = new long[oddTotal + 1, evenTotal + 1, 3];
        vis = new bool[oddTotal + 1, evenTotal + 1, 3];

        if (Count(oddTotal, evenTotal, 2) < k)
            return new int[0];

        bool[] used = new bool[n + 1];
        List<int> ans = new List<int>();
        int oddRem = oddTotal;
        int evenRem = evenTotal;

        for (int pos = 0; pos < n; ++pos)
        {
            int prevParity = -1;
            if (pos > 0) prevParity = ans[pos - 1] % 2;

            for (int cand = 1; cand <= n; ++cand)
            {
                if (used[cand]) continue;
                int candParity = cand % 2;
                if (prevParity != -1 && candParity == prevParity) continue;

                int oRem = oddRem - (candParity == 1 ? 1 : 0);
                int eRem = evenRem - (candParity == 0 ? 1 : 0);

                long cnt = Count(oRem, eRem, candParity);
                if (cnt >= k)
                {
                    ans.Add(cand);
                    used[cand] = true;
                    if (candParity == 1) oddRem--; else evenRem--;
                    break;
                }
                else
                {
                    k -= cnt;
                }
            }
        }

        return ans.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var permute = function(n, k) {
    const LIMIT = 10n ** 18n; // cap to avoid overflow
    // memo[o][e][p] where p:0 even needed,1 odd needed
    const memo = Array.from({length: n + 1}, () =>
        Array.from({length: n + 1}, () => [null, null])
    );

    function count(o, e, p) {
        if (o === 0 && e === 0) return 1n;
        const cached = memo[o][e][p];
        if (cached !== null) return cached;
        let res = 0n;
        if (p === 1) { // need odd
            if (o > 0) {
                res += BigInt(o) * count(o - 1, e, 0);
            }
        } else { // need even
            if (e > 0) {
                res += BigInt(e) * count(o, e - 1, 1);
            }
        }
        if (res > LIMIT) res = LIMIT;
        memo[o][e][p] = res;
        return res;
    }

    let kBig = BigInt(k);
    const used = new Array(n + 1).fill(false);
    const totalOdds = Math.ceil(n / 2);
    const totalEvens = Math.floor(n / 2);
    let remOdd = totalOdds, remEven = totalEvens;
    const ans = [];

    for (let pos = 0; pos < n; ++pos) {
        let placed = false;
        for (let cand = 1; cand <= n; ++cand) {
            if (used[cand]) continue;
            const parity = cand % 2 === 0 ? 0 : 1; // 0 even,1 odd

            // start position constraints
            if (pos === 0) {
                if (n % 2 === 1 && parity !== 1) continue; // n odd -> must start odd
            } else {
                const need = 1 - ans[pos - 1] % 2;
                if (parity !== need) continue;
            }

            const oAfter = remOdd - (parity === 1 ? 1 : 0);
            const eAfter = remEven - (parity === 0 ? 1 : 0);
            const nextNeed = 1 - parity; // parity required for the following element
            const cnt = count(oAfter, eAfter, nextNeed);

            if (kBig > cnt) {
                kBig -= cnt;
            } else {
                // choose this candidate
                ans.push(cand);
                used[cand] = true;
                remOdd = oAfter;
                remEven = eAfter;
                placed = true;
                break;
            }
        }
        if (!placed) return [];
    }

    return ans;
};
```

## Typescript

```typescript
function permute(n: number, k: number): number[] {
    const INF = 1e18;
    const oddsTotal = Math.ceil(n / 2);
    const evensTotal = Math.floor(n / 2);

    // dp[o][e][lastParity] where lastParity: 0 even, 1 odd
    const dp: number[][][] = Array.from({ length: oddsTotal + 1 }, () =>
        Array.from({ length: evensTotal + 1 }, () => [-1, -1])
    );

    function mulCap(a: number, b: number): number {
        if (a === 0 || b === 0) return 0;
        if (a > INF / b) return INF;
        const v = a * b;
        return v > INF ? INF : v;
    }

    function count(o: number, e: number, last: number): number {
        if (o === 0 && e === 0) return 1;
        const cached = dp[o][e][last];
        if (cached !== -1) return cached;

        const need = 1 - last; // parity needed next
        let res = 0;
        if (need === 1) { // need odd
            if (o > 0) {
                const sub = count(o - 1, e, 1);
                res = mulCap(o, sub);
            }
        } else { // need even
            if (e > 0) {
                const sub = count(o, e - 1, 0);
                res = mulCap(e, sub);
            }
        }
        dp[o][e][last] = res;
        return res;
    }

    const used = new Array(n + 1).fill(false);
    let remainingOdds = oddsTotal;
    let remainingEvens = evensTotal;
    let prevParity = -1; // undefined for first position
    const ans: number[] = [];

    for (let pos = 0; pos < n; pos++) {
        let placed = false;
        for (let cand = 1; cand <= n; cand++) {
            if (used[cand]) continue;
            const parity = cand % 2 === 0 ? 0 : 1;

            // first position constraints
            if (pos === 0) {
                if (n % 2 === 1 && parity !== 1) continue; // must start odd when n is odd
            } else {
                if (parity === prevParity) continue; // need opposite parity
            }

            const o = remainingOdds - (parity === 1 ? 1 : 0);
            const e = remainingEvens - (parity === 0 ? 1 : 0);
            const cnt = count(o, e, parity);

            if (k > cnt) {
                k -= cnt;
            } else {
                // choose this candidate
                ans.push(cand);
                used[cand] = true;
                remainingOdds = o;
                remainingEvens = e;
                prevParity = parity;
                placed = true;
                break;
            }
        }
        if (!placed) return [];
    }

    return ans;
}
```

## Php

```php
class Solution {
    const CAP = 1000000000000000000; // 1e18, safe upper bound for k (<=1e15)

    private function mulCap(int $a, int $b): int {
        $cap = self::CAP;
        if ($a == 0 || $b == 0) return 0;
        if ($a > intdiv($cap, $b)) return $cap;
        $res = $a * $b;
        return $res > $cap ? $cap : $res;
    }

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function permute($n, $k) {
        // precompute factorials with cap
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $prev = $fact[$i - 1];
            if ($prev > intdiv(self::CAP, $i)) {
                $fact[$i] = self::CAP;
            } else {
                $val = $prev * $i;
                $fact[$i] = $val > self::CAP ? self::CAP : $val;
            }
        }

        // remaining numbers separated by parity
        $oddRemaining  = [];
        $evenRemaining = [];
        for ($i = 1; $i <= $n; $i++) {
            if (($i & 1) == 0) $evenRemaining[] = $i;
            else $oddRemaining[] = $i;
        }
        $oCnt = count($oddRemaining);
        $eCnt = count($evenRemaining);

        $answer = [];
        $startParity = null; // 0 -> odd, 1 -> even

        for ($pos = 0; $pos < $n; $pos++) {
            $candidates = [];

            if ($startParity === null) {
                foreach ($oddRemaining as $v) $candidates[] = $v;
                foreach ($evenRemaining as $v) $candidates[] = $v;
                sort($candidates);
            } else {
                // required parity for this position
                $requiredParity = ($startParity == 0)
                    ? (($pos % 2 == 0) ? 0 : 1)
                    : (($pos % 2 == 0) ? 1 : 0);
                if ($requiredParity == 0) {
                    foreach ($oddRemaining as $v) $candidates[] = $v;
                } else {
                    foreach ($evenRemaining as $v) $candidates[] = $v;
                }
                sort($candidates);
            }

            $picked = false;
            foreach ($candidates as $cand) {
                $newStartParity = $startParity;
                if ($newStartParity === null) {
                    $newStartParity = ($cand % 2 == 0) ? 1 : 0;
                }
                $newOCnt = $oCnt;
                $newECnt = $eCnt;
                if (($cand & 1) == 0) $newECnt--;
                else $newOCnt--;

                // compute needed odd/even slots for the remaining positions
                $needOdd = 0;
                $needEven = 0;
                for ($i = $pos + 1; $i < $n; $i++) {
                    $par = ($newStartParity == 0)
                        ? (($i % 2 == 0) ? 0 : 1)
                        : (($i % 2 == 0) ? 1 : 0);
                    if ($par == 0) $needOdd++;
                    else $needEven++;
                }

                if ($newOCnt != $needOdd || $newECnt != $needEven) {
                    $cnt = 0;
                } else {
                    $cnt = $this->mulCap($fact[$newOCnt], $fact[$newECnt]);
                }

                if ($k > $cnt) {
                    $k -= $cnt;
                } else {
                    // choose this candidate
                    $answer[] = $cand;
                    if (($cand & 1) == 0) {
                        $idx = array_search($cand, $evenRemaining);
                        if ($idx !== false) array_splice($evenRemaining, $idx, 1);
                        $eCnt--;
                    } else {
                        $idx = array_search($cand, $oddRemaining);
                        if ($idx !== false) array_splice($oddRemaining, $idx, 1);
                        $oCnt--;
                    }
                    $startParity = $newStartParity;
                    $picked = true;
                    break;
                }
            }

            if (!$picked) {
                return [];
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func permute(_ n: Int, _ kInput: Int) -> [Int] {
        let INF: UInt64 = UInt64.max / 4
        func mulCap(_ a: UInt64, _ b: UInt64) -> UInt64 {
            if a == 0 || b == 0 { return 0 }
            if a > INF / b { return INF }
            return a * b
        }

        // factorials with cap
        var fact = [UInt64](repeating: 1, count: n + 1)
        for i in 1...n {
            fact[i] = mulCap(fact[i - 1], UInt64(i))
        }

        let totalOdds = (n + 1) / 2
        let totalEvens = n / 2

        var total = mulCap(fact[totalOdds], fact[totalEvens])
        if n % 2 == 0 {
            total = mulCap(total, 2)
        }

        var k = UInt64(kInput)
        if k > total { return [] }

        var oddsSet = Set<Int>()
        var evensSet = Set<Int>()
        for i in 1...n {
            if i % 2 == 1 {
                oddsSet.insert(i)
            } else {
                evensSet.insert(i)
            }
        }

        var result: [Int] = []
        var prevParity: Int? = nil   // 0 even, 1 odd

        for _ in 0..<n {
            for cand in 1...n {
                let isAvailable: Bool
                if cand % 2 == 1 {
                    isAvailable = oddsSet.contains(cand)
                } else {
                    isAvailable = evensSet.contains(cand)
                }
                if !isAvailable { continue }

                // parity constraint with previous element
                if let pp = prevParity, (cand % 2) == pp {
                    continue
                }

                var oRem = oddsSet.count
                var eRem = evensSet.count
                if cand % 2 == 1 {
                    oRem -= 1
                } else {
                    eRem -= 1
                }

                var cnt: UInt64 = 0
                if oRem == 0 && eRem == 0 {
                    cnt = 1
                } else {
                    // required start parity for the rest is opposite of cand's parity
                    let neededStartParity = (cand % 2) ^ 1   // 0 even, 1 odd

                    var feasible = false
                    if oRem == eRem {
                        feasible = true
                    } else if oRem == eRem + 1 {
                        feasible = (neededStartParity == 1)
                    } else if eRem == oRem + 1 {
                        feasible = (neededStartParity == 0)
                    }

                    if feasible {
                        cnt = mulCap(fact[oRem], fact[eRem])
                    }
                }

                if k > cnt {
                    k -= cnt
                    continue
                } else {
                    // choose cand
                    result.append(cand)
                    if cand % 2 == 1 {
                        oddsSet.remove(cand)
                    } else {
                        evensSet.remove(cand)
                    }
                    prevParity = cand % 2
                    break
                }
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun permute(n: Int, kInput: Long): IntArray {
        var k = kInput
        val LIMIT = 1_000_000_000_000_000_000L // 1e18, enough to cap counts above k (<=1e15)
        val fact = LongArray(n + 1)
        fact[0] = 1L
        for (i in 1..n) {
            val prev = fact[i - 1]
            fact[i] = if (prev > LIMIT / i) LIMIT else prev * i
        }

        var oddRem = (n + 1) / 2
        var evenRem = n / 2
        val used = BooleanArray(n + 1)
        val res = IntArray(n)
        var prevParity = -1 // -1: none, 0: even, 1: odd

        for (pos in 0 until n) {
            var chosen = -1
            for (cand in 1..n) {
                if (used[cand]) continue
                val candParity = cand and 1 // 1 odd, 0 even
                if (prevParity != -1 && candParity == prevParity) continue

                val oRem = oddRem - if (candParity == 1) 1 else 0
                val eRem = evenRem - if (candParity == 0) 1 else 0
                val nextStartParity = 1 - candParity
                val cnt = countWays(oRem, eRem, nextStartParity, fact, LIMIT)

                if (cnt >= k) {
                    chosen = cand
                    used[cand] = true
                    res[pos] = cand
                    oddRem = oRem
                    evenRem = eRem
                    prevParity = candParity
                    break
                } else {
                    k -= cnt
                }
            }
            if (chosen == -1) return intArrayOf()
        }
        return res
    }

    private fun countWays(o: Int, e: Int, startParity: Int, fact: LongArray, LIMIT: Long): Long {
        val len = o + e
        val needOdd: Int
        val needEven: Int
        if (startParity == 1) { // start with odd
            needOdd = (len + 1) / 2
            needEven = len / 2
        } else { // start with even
            needOdd = len / 2
            needEven = (len + 1) / 2
        }
        if (o != needOdd || e != needEven) return 0L
        var res = fact[o]
        val fE = fact[e]
        if (res > LIMIT / fE) return LIMIT
        res *= fE
        return if (res > LIMIT) LIMIT else res
    }
}
```

## Dart

```dart
class Solution {
  List<int> permute(int n, int k) {
    // Precompute factorials up to n using BigInt
    List<BigInt> fact = List.filled(n + 1, BigInt.one);
    for (int i = 1; i <= n; ++i) {
      fact[i] = fact[i - 1] * BigInt.from(i);
    }

    // Helper to count completions given remaining odds/even counts and last parity
    BigInt countWays(int o, int e, int lastParity) {
      if (o < 0 || e < 0) return BigInt.zero;
      int len = o + e;
      if (len == 0) return BigInt.one;
      int startParity = 1 - lastParity; // opposite parity for next position
      int oddsSlots, evensSlots;
      if (startParity == 1) {
        oddsSlots = (len + 1) ~/ 2;
        evensSlots = len ~/ 2;
      } else {
        evensSlots = (len + 1) ~/ 2;
        oddsSlots = len ~/ 2;
      }
      if (oddsSlots != o || evensSlots != e) return BigInt.zero;
      return fact[oddsSlots] * fact[evensSlots];
    }

    int totalOdds = (n + 1) ~/ 2;
    int totalEvens = n ~/ 2;

    List<bool> used = List.filled(n + 1, false);
    List<int> result = [];

    BigInt K = BigInt.from(k);

    int remainingOdds = totalOdds;
    int remainingEvens = totalEvens;

    for (int pos = 0; pos < n; ++pos) {
      bool placed = false;
      for (int num = 1; num <= n; ++num) {
        if (used[num]) continue;
        int parity = num % 2; // 1 odd, 0 even

        // Determine if this number can be placed at current position
        if (pos == 0) {
          if (n % 2 == 1 && parity != 1) continue; // n odd -> must start with odd
        } else {
          int requiredParity = 1 - (result[pos - 1] % 2);
          if (parity != requiredParity) continue;
        }

        // Simulate picking this number
        int o = remainingOdds - (parity == 1 ? 1 : 0);
        int e = remainingEvens - (parity == 0 ? 1 : 0);

        BigInt cnt = countWays(o, e, parity);
        if (cnt >= K) {
          // Choose this number
          result.add(num);
          used[num] = true;
          if (parity == 1) remainingOdds--; else remainingEvens--;
          placed = true;
          break;
        } else {
          K -= cnt;
        }
      }
      if (!placed) {
        return [];
      }
    }

    return result;
  }
}
```

## Golang

```go
func permute(n int, k int64) []int {
	const INF int64 = 2_000_000_000_000_000_000 // sufficiently large
	// precompute factorials with cap at INF
	fact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		if fact[i-1] > INF/int64(i) {
			fact[i] = INF
		} else {
			fact[i] = fact[i-1] * int64(i)
			if fact[i] > INF {
				fact[i] = INF
			}
		}
	}
	mulCap := func(a, b int64) int64 {
		if a == 0 || b == 0 {
			return 0
		}
		if a > INF/b {
			return INF
		}
		res := a * b
		if res > INF {
			return INF
		}
		return res
	}
	// count remaining permutations given counts of odds and evens left,
	// and the parity that must appear next (0 even, 1 odd)
	count := func(oddCnt, evenCnt int, startParity int) int64 {
		m := oddCnt + evenCnt
		var needOdd, needEven int
		if startParity == 0 { // next should be even
			needEven = (m + 1) / 2
			needOdd = m / 2
		} else {
			needOdd = (m + 1) / 2
			needEven = m / 2
		}
		if oddCnt < needOdd || evenCnt < needEven {
			return 0
		}
		// the numbers to place are exactly needOdd odds and needEven evens,
		// which equal oddCnt and evenCnt respectively when condition holds.
		return mulCap(fact[oddCnt], fact[evenCnt])
	}

	used := make([]bool, n+1)
	remainingOdd := 0
	remainingEven := 0
	for i := 1; i <= n; i++ {
		if i&1 == 1 {
			remainingOdd++
		} else {
			remainingEven++
		}
	}

	res := make([]int, 0, n)
	prevParity := -1 // undefined

	for pos := 0; pos < n; pos++ {
		found := false
		for num := 1; num <= n; num++ {
			if used[num] {
				continue
			}
			curParity := num & 1
			if prevParity != -1 && curParity == prevParity {
				continue // adjacent same parity not allowed
			}
			// simulate picking num
			newOdd := remainingOdd
			newEven := remainingEven
			if curParity == 1 {
				newOdd--
			} else {
				newEven--
			}
			nextStartParity := 1 - curParity // opposite for next position
			cnt := count(newOdd, newEven, nextStartParity)
			if k > cnt {
				k -= cnt
				continue
			}
			// pick this number
			res = append(res, num)
			used[num] = true
			remainingOdd = newOdd
			remainingEven = newEven
			prevParity = curParity
			found = true
			break
		}
		if !found {
			return []int{}
		}
	}
	return res
}
```

## Ruby

```ruby
INF = 10**18

def permute(n, k)
  # counts of odds and evens
  o_rem = (n + 1) / 2
  e_rem = n / 2

  # memo dp[o][e][last_parity]
  dp = Array.new(o_rem + 1) { Array.new(e_rem + 1) { [nil, nil] } }

  count = lambda do |o, e, last|
    val = dp[o][e][last]
    return val unless val.nil?
    if o == 0 && e == 0
      res = 1
    else
      need = 1 - last
      if need == 0 # need even
        if e > 0
          sub = count.call(o, e - 1, 0)
          res = e * sub
          res = INF if res > INF
        else
          res = 0
        end
      else # need odd
        if o > 0
          sub = count.call(o - 1, e, 1)
          res = o * sub
          res = INF if res > INF
        else
          res = 0
        end
      end
    end
    dp[o][e][last] = res
    res
  end

  # total number of alternating permutations
  total = 0
  if o_rem > e_rem
    total = o_rem * count.call(o_rem - 1, e_rem, 1)
  else
    total = o_rem * count.call(o_rem - 1, e_rem, 1) + e_rem * count.call(o_rem, e_rem - 1, 0)
  end
  return [] if k > total

  used = Array.new(n + 1, false)
  result = []

  (0...n).each do |pos|
    chosen = nil
    (1..n).each do |num|
      next if used[num]
      parity = num & 1 # 1 odd, 0 even

      if pos == 0
        # first element restriction
        if o_rem > e_rem && parity != 1
          next
        end
      else
        prev_parity = result[-1] & 1
        next if parity == prev_parity
      end

      o_next = o_rem - (parity == 1 ? 1 : 0)
      e_next = e_rem - (parity == 0 ? 1 : 0)

      cnt = count.call(o_next, e_next, parity)
      if k > cnt
        k -= cnt
      else
        chosen = num
        o_rem = o_next
        e_rem = e_next
        break
      end
    end

    return [] unless chosen
    result << chosen
    used[chosen] = true
  end

  result
end
```

## Scala

```scala
object Solution {
    def permute(n: Int, kInput: Long): Array[Int] = {
        val totalOdd = (n + 1) / 2
        val totalEven = n / 2
        val INF: Long = 1000000000000000000L

        val dp = Array.ofDim[Long](totalOdd + 1, totalEven + 1, 2)
        for {
            i <- 0 to totalOdd
            j <- 0 to totalEven
            p <- 0 to 1
        } dp(i)(j)(p) = -1L

        def cnt(o: Int, e: Int, last: Int): Long = {
            if (o == 0 && e == 0) return 1L
            val memo = dp(o)(e)(last)
            if (memo != -1L) return memo
            val need = 1 - last
            var res: Long = 0L
            if (need == 0 && e > 0) {
                res = cnt(o, e - 1, 0)
            } else if (need == 1 && o > 0) {
                res = cnt(o - 1, e, 1)
            }
            if (res > INF) res = INF
            dp(o)(e)(last) = res
            res
        }

        var k = kInput
        val used = Array.fill[Boolean](n + 1)(false)
        var remainingOdd = totalOdd
        var remainingEven = totalEven
        var prevParity = -1

        val result = new Array[Int](n)

        for (pos <- 0 until n) {
            var found = false
            var v = 1
            while (v <= n && !found) {
                if (!used(v)) {
                    val parity = v & 1
                    if (prevParity == -1 || parity != prevParity) {
                        val oAfter = remainingOdd - (if (parity == 1) 1 else 0)
                        val eAfter = remainingEven - (if (parity == 0) 1 else 0)
                        if (oAfter >= 0 && eAfter >= 0) {
                            val ways = cnt(oAfter, eAfter, parity)
                            if (k > ways) {
                                k -= ways
                            } else {
                                result(pos) = v
                                used(v) = true
                                remainingOdd = oAfter
                                remainingEven = eAfter
                                prevParity = parity
                                found = true
                            }
                        }
                    }
                }
                v += 1
            }
            if (!found) return Array.emptyIntArray
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn permute(n: i32, mut k: i64) -> Vec<i32> {
        const INF: u128 = 2_000_000_000_000_000_000; // > 1e15
        let n_usize = n as usize;
        // precompute factorials with cap at INF
        let mut fact: Vec<u128> = vec![0; n_usize + 1];
        fact[0] = 1;
        for i in 1..=n_usize {
            let a = fact[i - 1];
            let b = i as u128;
            fact[i] = if a == INF || b == 0 {
                INF
            } else if a > INF / b {
                INF
            } else {
                let v = a * b;
                if v > INF { INF } else { v }
            };
        }

        // helper to multiply with cap
        fn mul_cap(a: u128, b: u128) -> u128 {
            const INF: u128 = 2_000_000_000_000_000_000;
            if a == 0 || b == 0 {
                0
            } else if a > INF / b {
                INF
            } else {
                let v = a * b;
                if v > INF { INF } else { v }
            }
        }

        // count completions given remaining odds/even and required start parity (true=odd)
        fn count_completions(o: i32, e: i32, start_odd: bool, fact: &Vec<u128>) -> u128 {
            const INF: u128 = 2_000_000_000_000_000_000;
            let l = o + e;
            if l == 0 {
                return 1;
            }
            let odd_needed = if start_odd { (l + 1) / 2 } else { l / 2 };
            let even_needed = l - odd_needed;
            if o != odd_needed || e != even_needed {
                return 0;
            }
            mul_cap(fact[o as usize], fact[e as usize])
        }

        // total number of alternating permutations
        let odd_total = (n + 1) / 2; // ceil
        let even_total = n / 2;     // floor
        let mut total = mul_cap(fact[odd_total as usize], fact[even_total as usize]);
        if n % 2 == 0 {
            total = mul_cap(total, 2);
        }
        if (k as u128) > total {
            return Vec::new();
        }

        // used array
        let mut used = vec![false; n_usize + 1];
        let mut result: Vec<i32> = Vec::with_capacity(n_usize);
        let mut odd_rem = odd_total;
        let mut even_rem = even_total;
        let mut prev_parity: Option<bool> = None; // true if odd

        for _pos in 0..n {
            let mut chosen = false;
            for x in 1..=n {
                if used[x as usize] {
                    continue;
                }
                let parity = (x % 2) != 0; // true if odd
                if let Some(p) = prev_parity {
                    if p == parity {
                        continue; // cannot place same parity consecutively
                    }
                }
                // check feasibility after picking x
                let o_next = odd_rem - if parity { 1 } else { 0 };
                let e_next = even_rem - if !parity { 1 } else { 0 };
                if o_next < 0 || e_next < 0 {
                    continue;
                }
                // next required start parity for remaining sequence
                let start_odd_next = !parity;
                let cnt = count_completions(o_next, e_next, start_odd_next, &fact);
                if cnt == 0 {
                    continue;
                }
                if (k as u128) <= cnt {
                    // choose x
                    result.push(x);
                    used[x as usize] = true;
                    odd_rem = o_next;
                    even_rem = e_next;
                    prev_parity = Some(parity);
                    chosen = true;
                    break;
                } else {
                    k -= cnt as i64;
                }
            }
            if !chosen {
                // should not happen because we checked total earlier
                return Vec::new();
            }
        }

        result
    }
}
```

## Racket

```racket
(define INF (expt 10 18))

;; memoization table for DP counts
(define cnt-memo (make-hash))

(define (cnt o e p)
  (cond [(and (= o 0) (= e 0)) 1]
        [else
         (let ([key (list o e p)])
           (if (hash-has-key? cnt-memo key)
               (hash-ref cnt-memo key)
               (let* ([res (if (= p 1)                     ; last is odd, need even next
                               (if (= e 0) 0
                                   (min INF (* e (cnt o (- e 1) 0))))
                               (if (= o 0) 0
                                   (min INF (* o (cnt (- o 1) e 1)))) )])
                 (hash-set! cnt-memo key res)
                 res)))]))

(define/contract (permute n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let* ([total-odd (quotient (+ n 1) 2)]
         [total-even (quotient n 2)]
         [used (make-vector (+ n 1) #f)]
         [start-parities (if (> total-odd total-even)
                             '(1)               ; must start odd
                             '(0 1))]           ; both possible when equal
    (let loop ([pos 0]
               [o total-odd]
               [e total-even]
               [last -1]          ; -1 means no previous element
               [rem k]
               [res '()])
      (if (= pos n)
          (reverse res)                     ; finished
          (let find ((cand 1) (selected #f) (new-rem rem) (new-o o) (new-e e) (new-last last) (new-res res))
            (cond
              [(> cand n)                      ; no candidate fits -> k out of range
               '()]                            ; return empty list
              [selected                         ; already selected, continue outer loop
               (loop (+ pos 1) new-o new-e new-last new-rem new-res)]
              [else
               (if (vector-ref used cand)
                   (find (+ cand 1) #f new-rem o e last res)
                   (let* ([parity (modulo cand 2)]          ; 0 even, 1 odd
                          [valid-start? (or (not (= pos 0))
                                            (member parity start-parities))]
                          [valid-parity? (if (= pos 0)
                                             #t
                                             (= parity (if (= last 0) 1 0)))])
                     (if (and valid-start? valid-parity?)
                         (let* ([remain-o (if (= parity 1) (- o 1) o)]
                                [remain-e (if (= parity 0) (- e 1) e)]
                                [cnt-compl (cnt remain-o remain-e parity)])
                           (if (> new-rem cnt-compl)
                               (begin
                                 (set! new-rem (- new-rem cnt-compl))
                                 (find (+ cand 1) #f new-rem o e last res))
                               ;; choose this candidate
                               (begin
                                 (vector-set! used cand #t)
                                 (find (+ cand 1) #t new-rem remain-o remain-e parity (cons cand res)))))
                         (find (+ cand 1) #f new-rem o e last res))))]))))))
```

## Erlang

```erlang
-module(solution).
-export([permute/2]).

-define(INF, 1000000000000000000).

permute(N, K) ->
    MaxOdd = (N + 1) div 2,
    MaxEven = N div 2,
    DP = build_dp(MaxOdd, MaxEven),
    Odds0 = [X || X <- lists:seq(1, N), X rem 2 == 1],
    Evens0 = [X || X <- lists:seq(1, N), X rem 2 == 0],
    case construct(Odds0, Evens0, length(Odds0), length(Evens0), -1, K, DP) of
        {ok, Perm} -> Perm;
        error -> []
    end.

build_dp(MaxOdd, MaxEven) ->
    Empty = maps:new(),
    BaseMap = maps:put({0,0,0}, 1, maps:put({0,0,1}, 1, Empty)),
    lists:foldl(
      fun(O, AccO) ->
          lists:foldl(
            fun(E, AccE) ->
                case {O, E} of
                    {0,0} -> AccE;
                    _ ->
                        Count0 = case O of
                                    0 -> 0;
                                    _ ->
                                        Prev = maps:get({O-1,E,1}, AccE, 0),
                                        min(O * Prev, ?INF)
                                 end,
                        Count1 = case E of
                                    0 -> 0;
                                    _ ->
                                        Prev = maps:get({O,E-1,0}, AccE, 0),
                                        min(E * Prev, ?INF)
                                 end,
                        maps:put({O,E,0}, Count0,
                          maps:put({O,E,1}, Count1, AccE))
                end
            end, AccO, lists:seq(0, MaxEven))
      end, BaseMap, lists:seq(0, MaxOdd)).

construct(Olist, Elist, Ocnt, Ecnt, Prev, K, DP) ->
    case Ocnt + Ecnt of
        0 -> {ok, []};
        _ ->
            All = lists:sort(Olist ++ Elist),
            try_select(All, Olist, Elist, Ocnt, Ecnt, Prev, K, DP)
    end.

try_select([], _Olist, _Elist, _Ocnt, _Ecnt, _Prev, _K, _DP) ->
    error;
try_select([C|Rest], Olist, Elist, Ocnt, Ecnt, Prev, K, DP) ->
    Par = C rem 2,
    if
        Prev =/= -1, Par == Prev ->
            try_select(Rest, Olist, Elist, Ocnt, Ecnt, Prev, K, DP);
        true ->
            NewOcnt = Ocnt - (Par == 1),
            NewEcnt = Ecnt - (Par == 0),
            Count = maps:get({NewOcnt, NewEcnt, Par}, DP, 0),
            if
                K > Count ->
                    try_select(Rest, Olist, Elist, Ocnt, Ecnt, Prev, K-Count, DP);
                true ->
                    NewOlist = if Par == 1 -> lists:delete(C, Olist); true -> Olist end,
                    NewElist = if Par == 0 -> lists:delete(C, Elist); true -> Elist end,
                    case construct(NewOlist, NewElist, NewOcnt, NewEcnt, Par, K, DP) of
                        {ok, RestPerm} -> {ok, [C|RestPerm]};
                        error -> error
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec permute(n :: integer, k :: integer) :: [integer]
  def permute(n, k) do
    total_odds = div(n + 1, 2)
    total_evens = div(n, 2)

    odds = for i <- 1..n, rem(i, 2) == 1, do: i
    evens = for i <- 1..n, rem(i, 2) == 0, do: i

    fact =
      Enum.reduce(0..n, [1], fn i, acc -> [Enum.at(acc, -1) * i | acc] end)
      |> Enum.reverse()

    start_allowed =
      if rem(n, 2) == 1 do
        [1]
      else
        [0, 1]
      end

    total_perm =
      Enum.reduce(start_allowed, 0, fn sp, acc ->
        acc + count(total_odds, total_evens, sp, fact)
      end)

    if k > total_perm do
      []
    else
      dfs(0, n, k, start_allowed, odds, evens, fact, nil)
    end
  end

  defp count(o, e, start_parity, fact) do
    l = o + e

    needed_odds =
      if rem(l, 2) == 0 do
        div(l, 2)
      else
        if start_parity == 1, do: div(l, 2) + 1, else: div(l, 2)
      end

    if o != needed_odds do
      0
    else
      Enum.at(fact, o) * Enum.at(fact, e)
    end
  end

  defp dfs(pos, n, k, start_allowed, odds_rem, evens_rem, fact, prev_parity) do
    if pos == n do
      []
    else
      candidates =
        cond do
          pos == 0 ->
            (odds_rem ++ evens_rem)
            |> Enum.sort()
            |> Enum.filter(fn v -> Enum.member?(start_allowed, rem(v, 2)) end)

          true ->
            needed = 1 - prev_parity

            if needed == 1, do: odds_rem, else: evens_rem
        end

      {chosen_val, new_k, new_odds, new_evens, new_prev} =
        Enum.reduce_while(candidates, {:none, k, odds_rem, evens_rem, prev_parity},
          fn v,
             {_c, curk, o_list, e_list, _pprev} ->
            p = rem(v, 2)

            {o2, e2} =
              if p == 1 do
                {List.delete(o_list, v), e_list}
              else
                {o_list, List.delete(e_list, v)}
              end

            o_cnt = length(o2)
            e_cnt = length(e2)
            need_start = 1 - p
            cnt = count(o_cnt, e_cnt, need_start, fact)

            if cnt >= curk do
              {:halt, {v, curk, o2, e2, p}}
            else
              {:cont, {:none, curk - cnt, o_list, e_list, _pprev}}
            end
          end)

      case chosen_val do
        :none ->
          []

        _ ->
          rest = dfs(pos + 1, n, new_k, start_allowed, new_odds, new_evens, fact, new_prev)
          [chosen_val | rest]
      end
    end
  end
end
```
