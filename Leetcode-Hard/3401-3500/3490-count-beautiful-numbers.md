# 3490. Count Beautiful Numbers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using ll = long long;
    
    vector<int> digits;
    // memo[pos][sum] -> map product -> count
    vector<vector<unordered_map<int, ll>>> memo;
    
    ll dfs(int pos, int sum, int prod, bool started, bool tight) {
        if (pos == (int)digits.size()) {
            return (started && sum > 0 && prod % sum == 0) ? 1 : 0;
        }
        if (!tight) {
            auto &mp = memo[pos][sum];
            auto it = mp.find(prod);
            if (it != mp.end()) return it->second;
            ll res = 0;
            int limit = 9;
            for (int d = 0; d <= limit; ++d) {
                bool nStarted = started || d != 0;
                int nSum = sum + (nStarted ? d : 0);
                int nProd = prod;
                if (nStarted) {
                    if (!started) { // first non‑zero digit
                        nProd = d;          // d is non‑zero here
                    } else {
                        if (d == 0) nProd = 0;
                        else if (nProd != 0) nProd *= d;
                    }
                }
                res += dfs(pos + 1, nSum, nProd, nStarted, false);
            }
            mp[prod] = res;
            return res;
        } else {
            ll res = 0;
            int limit = digits[pos];
            for (int d = 0; d <= limit; ++d) {
                bool nTight = tight && (d == limit);
                bool nStarted = started || d != 0;
                int nSum = sum + (nStarted ? d : 0);
                int nProd = prod;
                if (nStarted) {
                    if (!started) { // first non‑zero digit
                        nProd = d;          // d is non‑zero here
                    } else {
                        if (d == 0) nProd = 0;
                        else if (nProd != 0) nProd *= d;
                    }
                }
                res += dfs(pos + 1, nSum, nProd, nStarted, nTight);
            }
            return res;
        }
    }
    
    ll countUpTo(int x) {
        if (x <= 0) return 0;
        digits.clear();
        while (x > 0) {
            digits.push_back(x % 10);
            x /= 10;
        }
        reverse(digits.begin(), digits.end());
        int n = digits.size();
        memo.assign(n, vector<unordered_map<int,ll>>(82));
        return dfs(0, 0, 1, false, true);
    }
    
    int beautifulNumbers(int l, int r) {
        ll ans = countUpTo(r) - countUpTo(l - 1);
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int beautifulNumbers(int l, int r) {
        return (int)(count(r) - count(l - 1));
    }

    private long count(long n) {
        if (n <= 0) return 0;
        char[] digits = Long.toString(n).toCharArray();
        Map<Long, Integer> memo = new HashMap<>();
        return dfs(0, 0, 1L, false, true, digits, memo);
    }

    private long dfs(int pos, int sum, long prod, boolean started, boolean tight,
                     char[] digits, Map<Long, Integer> memo) {
        if (pos == digits.length) {
            if (!started) return 0; // no number formed
            if (prod == 0) return 1; // contains a zero digit
            return (sum > 0 && prod % sum == 0) ? 1 : 0;
        }
        if (!tight) {
            long key = ((long)pos << 56) | ((long)sum << 48) | (prod << 1) | (started ? 1L : 0L);
            Integer cached = memo.get(key);
            if (cached != null) return cached;
            long res = 0;
            for (int d = 0; d <= 9; ++d) {
                boolean nextStarted = started || d != 0;
                int newSum = sum + (nextStarted ? d : 0);
                long newProd;
                if (!started && d == 0) {
                    newProd = prod; // still not started, product irrelevant
                } else if (!started) { // first non‑zero digit
                    newProd = d;
                } else {
                    if (prod == 0 || d == 0) newProd = 0;
                    else newProd = prod * d;
                }
                res += dfs(pos + 1, newSum, newProd, nextStarted, false, digits, memo);
            }
            memo.put(key, (int)res);
            return res;
        } else {
            int limit = digits[pos] - '0';
            long res = 0;
            for (int d = 0; d <= limit; ++d) {
                boolean nextTight = tight && (d == limit);
                boolean nextStarted = started || d != 0;
                int newSum = sum + (nextStarted ? d : 0);
                long newProd;
                if (!started && d == 0) {
                    newProd = prod;
                } else if (!started) {
                    newProd = d;
                } else {
                    if (prod == 0 || d == 0) newProd = 0;
                    else newProd = prod * d;
                }
                res += dfs(pos + 1, newSum, newProd, nextStarted, nextTight, digits, memo);
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def beautifulNumbers(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        from functools import lru_cache

        def count_up_to(x):
            if x <= 0:
                return 0
            digits = list(map(int, str(x)))
            n = len(digits)

            total = 0
            # maximum possible digit sum for numbers up to 10^9 is 81
            for S in range(1, 82):
                @lru_cache(None)
                def dp(pos, tight, started, cur_sum, rem):
                    if pos == n:
                        return int(started and cur_sum == S and rem == 0)
                    limit = digits[pos] if tight else 9
                    ans = 0
                    for d in range(0, limit + 1):
                        ntight = tight and (d == limit)
                        if not started:
                            if d == 0:
                                # still leading zeros
                                ans += dp(pos + 1, ntight, False, 0, 0)
                            else:
                                ns = d
                                if ns > S:
                                    continue
                                nrem = d % S
                                ans += dp(pos + 1, ntight, True, ns, nrem)
                        else:
                            ns = cur_sum + d
                            if ns > S:
                                continue
                            nrem = (rem * d) % S if d != 0 else 0
                            ans += dp(pos + 1, ntight, True, ns, nrem)
                    return ans

                total += dp(0, True, False, 0, 0)
            return total

        return count_up_to(r) - count_up_to(l - 1)
```

## Python3

```python
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(maxsize=None)
            def dfs(pos: int, tight: bool, started: bool, zero_seen: bool,
                    s: int, p: int) -> int:
                if pos == m:
                    if not started:
                        return 0
                    if zero_seen:
                        return 1
                    # no zero digit encountered
                    return 1 if p % s == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    nstarted = started or d != 0
                    if not nstarted:
                        # still leading zeros, nothing counted yet
                        total += dfs(pos + 1, ntight, False, False, 0, 1)
                    else:
                        if zero_seen:
                            # already have a zero digit earlier, condition satisfied
                            total += dfs(pos + 1, ntight, True, True, 0, 0)
                        else:
                            if d == 0:
                                total += dfs(pos + 1, ntight, True, True, 0, 0)
                            else:
                                ns = s + d
                                np = p * d
                                total += dfs(pos + 1, ntight, True, False, ns, np)
                return total

            return dfs(0, True, False, False, 0, 1)

        return count_upto(r) - count_upto(l - 1)
```

## C

```c
#include <string.h>
#include <stddef.h>

static int digits[10];
static int len;
static int targetSum;
static int MOD;                     // current sum value (also modulus)
static long long memo[10][82][82][2]; // pos, sum, mod, leadZero
static char used[10][82][82][2];

static long long dfs(int pos, int sum, int mod, int leadZero, int tight) {
    if (pos == len) {
        return (!leadZero && sum == targetSum && mod == 0) ? 1LL : 0LL;
    }
    if (!tight && used[pos][sum][mod][leadZero]) {
        return memo[pos][sum][mod][leadZero];
    }

    int limit = tight ? digits[pos] : 9;
    long long res = 0;

    for (int d = 0; d <= limit; ++d) {
        int nLead = leadZero && d == 0;
        int nSum = sum;
        int nMod = mod;

        if (!nLead) { // number has started after this digit
            if (leadZero && d > 0) {          // first non‑zero digit
                nSum = sum + d;               // sum is currently 0
                nMod = (MOD == 1) ? 0 : (d % MOD);
            } else {                         // already started before
                nSum = sum + d;
                if (d == 0) {
                    nMod = 0;                 // product becomes zero
                } else {
                    nMod = (mod * d) % MOD;
                }
            }
        } else {
            /* still leading zeros: sum stays 0, mod unchanged */
        }

        if (nSum > targetSum) continue;

        int nTight = tight && (d == limit);
        res += dfs(pos + 1, nSum, nMod, nLead, nTight);
    }

    if (!tight) {
        used[pos][sum][mod][leadZero] = 1;
        memo[pos][sum][mod][leadZero] = res;
    }
    return res;
}

static long long countUpTo(int x) {
    if (x <= 0) return 0LL;

    // extract digits
    len = 0;
    int tmp = x;
    while (tmp > 0) {
        digits[len++] = tmp % 10;
        tmp /= 10;
    }
    // reverse to most significant first
    for (int i = 0; i < len / 2; ++i) {
        int t = digits[i];
        digits[i] = digits[len - 1 - i];
        digits[len - 1 - i] = t;
    }

    long long total = 0;
    for (int s = 1; s <= 81; ++s) {
        if (s > 9 * len) break;          // impossible sum for this length
        targetSum = s;
        MOD = s;

        memset(used, 0, sizeof(used));
        int initMod = (MOD == 1) ? 0 : 1 % MOD;   // product identity modulo s

        total += dfs(0, 0, initMod, 1, 1);
    }
    return total;
}

int beautifulNumbers(int l, int r) {
    if (l > r) return 0;
    long long ans = countUpTo(r) - countUpTo(l - 1);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int BeautifulNumbers(int l, int r)
    {
        return (int)(Count(r) - Count((long)l - 1));
    }

    private long Count(long x)
    {
        if (x < 0) return 0;
        string s = x.ToString();
        int n = s.Length;
        long total = 0;

        for (int targetSum = 1; targetSum <= 81; targetSum++)
        {
            // dp[pos, sum, prodMod, started] = -1 means uncomputed
            var dp = new int[n + 1, 82, 81, 2];
            for (int i = 0; i <= n; i++)
                for (int j = 0; j < 82; j++)
                    for (int k = 0; k < 81; k++)
                        dp[i, j, k, 0] = dp[i, j, k, 1] = -1;

            int ModInit = targetSum == 0 ? 0 : 1 % targetSum; // actually targetSum never zero

            int DFS(int pos, int sum, int prodMod, bool started, bool tight)
            {
                if (pos == n)
                {
                    return (started && sum == targetSum && prodMod == 0) ? 1 : 0;
                }

                if (!tight)
                {
                    int cached = dp[pos, sum, prodMod, started ? 1 : 0];
                    if (cached != -1) return cached;
                }

                int limit = tight ? s[pos] - '0' : 9;
                long res = 0;

                for (int d = 0; d <= limit; d++)
                {
                    bool nStarted = started || d != 0;
                    int nSum = sum + (nStarted ? d : 0);
                    if (nSum > targetSum) continue;

                    int nProdMod;
                    if (!nStarted)
                    {
                        nProdMod = ModInit; // still leading zeros
                    }
                    else
                    {
                        nProdMod = (int)((long)prodMod * d % targetSum);
                    }

                    res += DFS(pos + 1, nSum, nProdMod, nStarted, tight && d == limit);
                }

                if (!tight)
                {
                    dp[pos, sum, prodMod, started ? 1 : 0] = (int)res;
                }
                return (int)res;
            }

            total += DFS(0, 0, ModInit, false, true);
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var beautifulNumbers = function(l, r) {
    const countUpTo = (num) => {
        if (num <= 0) return 0;
        const digits = String(num).split('').map(ch => ch.charCodeAt(0) - 48);
        const n = digits.length;
        let total = 0;

        for (let S = 1; S <= 81; ++S) {
            const memo = new Map();

            const dfs = (pos, tight, started, sum, mod) => {
                if (pos === n) {
                    return (started && sum === S && mod === 0) ? 1 : 0;
                }
                const key = ((pos * 2 + (tight ? 1 : 0)) * 2 + (started ? 1 : 0)) + ',' + sum + ',' + mod;
                if (memo.has(key)) return memo.get(key);

                let res = 0;
                const limit = tight ? digits[pos] : 9;
                for (let d = 0; d <= limit; ++d) {
                    const ntight = tight && (d === limit);
                    const nstarted = started || d !== 0;
                    const nsum = sum + (nstarted ? d : 0);
                    if (nsum > S) continue;

                    let nmod;
                    if (!nstarted) {
                        // still leading zeros, product stays neutral (1 % S)
                        nmod = mod;
                    } else {
                        if (!started && d !== 0) {          // first non‑zero digit
                            nmod = d % S;
                        } else {
                            if (d === 0) nmod = 0;           // any zero makes product zero
                            else nmod = (mod * d) % S;
                        }
                    }

                    res += dfs(pos + 1, ntight, nstarted, nsum, nmod);
                }

                memo.set(key, res);
                return res;
            };

            const initMod = 1 % S; // neutral element for product
            total += dfs(0, true, false, 0, initMod);
        }
        return total;
    };

    return countUpTo(r) - countUpTo(l - 1);
};
```

## Typescript

```typescript
function beautifulNumbers(l: number, r: number): number {
    function countUpTo(x: number, S: number): number {
        if (x <= 0) return 0;
        const digits = String(x).split('').map(ch => +ch);
        const n = digits.length;
        // memo[pos][sum][prodMod][started?1:0] = value or -1
        const memo: number[][][][] = Array.from({ length: n }, () =>
            Array.from({ length: S + 1 }, () =>
                Array.from({ length: S === 0 ? 1 : S }, () => [-1, -1])
            )
        );

        function dfs(pos: number, sum: number, prodMod: number, started: boolean, tight: boolean): number {
            if (pos === n) {
                return (started && sum === S && prodMod === 0) ? 1 : 0;
            }
            if (!tight) {
                const cached = memo[pos][sum][prodMod][started ? 1 : 0];
                if (cached !== -1) return cached;
            }

            const limit = tight ? digits[pos] : 9;
            let res = 0;

            for (let d = 0; d <= limit; d++) {
                const nextStarted = started || d !== 0;
                const add = nextStarted ? d : 0;
                const nextSum = sum + add;
                if (nextSum > S) continue;

                let nextProdMod: number;
                if (!nextStarted) {
                    nextProdMod = 0; // irrelevant before any digit
                } else {
                    if (!started && d !== 0) {
                        // first non‑zero digit
                        nextProdMod = d % S;
                    } else {
                        // already started
                        nextProdMod = d === 0 ? 0 : (prodMod * d) % S;
                    }
                }

                res += dfs(pos + 1, nextSum, nextProdMod, nextStarted, tight && d === limit);
            }

            if (!tight) memo[pos][sum][prodMod][started ? 1 : 0] = res;
            return res;
        }

        return dfs(0, 0, 0, false, true);
    }

    let ans = 0;
    for (let S = 1; S <= 81; S++) {
        ans += countUpTo(r, S) - countUpTo(l - 1, S);
    }
    return ans;
}
```

## Php

```php
class Solution {
    private $digitExp = [
        0 => [0,0,0,0],
        1 => [0,0,0,0],
        2 => [1,0,0,0],
        3 => [0,1,0,0],
        4 => [2,0,0,0],
        5 => [0,0,1,0],
        6 => [1,1,0,0],
        7 => [0,0,0,1],
        8 => [3,0,0,0],
        9 => [0,2,0,0],
    ];
    private $sumInfo = [];

    public function __construct() {
        // precompute factorization of sums 0..81 into primes 2,3,5,7
        for ($s = 0; $s <= 81; $s++) {
            $tmp = $s;
            $e2 = $e3 = $e5 = $e7 = 0;
            if ($tmp == 0) {
                $this->sumInfo[$s] = ['valid'=>false];
                continue;
            }
            while ($tmp % 2 == 0) { $e2++; $tmp /= 2; }
            while ($tmp % 3 == 0) { $e3++; $tmp /= 3; }
            while ($tmp % 5 == 0) { $e5++; $tmp /= 5; }
            while ($tmp % 7 == 0) { $e7++; $tmp /= 7; }
            $valid = ($tmp == 1);
            $this->sumInfo[$s] = [
                'valid' => $valid,
                'e2'    => $e2,
                'e3'    => $e3,
                'e5'    => $e5,
                'e7'    => $e7
            ];
        }
    }

    /**
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function beautifulNumbers($l, $r) {
        return $this->countUpTo($r) - $this->countUpTo($l - 1);
    }

    private function countUpTo($n) {
        if ($n <= 0) return 0;
        $digitsStr = strval($n);
        $len = strlen($digitsStr);
        $digits = [];
        for ($i = 0; $i < $len; $i++) {
            $digits[$i] = intval($digitsStr[$i]);
        }
        $memo = [];
        return $this->dfs(0, 0, 0, 0, 0, 0, false, false, true, $digits, $memo);
    }

    private function dfs($pos, $sum, $e2, $e3, $e5, $e7, $started, $hasZero, $tight, &$digits, &$memo) {
        $len = count($digits);
        if ($pos == $len) {
            if (!$started) return 0;               // no number formed
            if ($hasZero) return 1;                // product is zero -> always beautiful
            // no zero digits, need divisibility check
            if ($sum == 0) return 0;
            $info = $this->sumInfo[$sum];
            if (!$info['valid']) return 0;
            return ($e2 >= $info['e2'] && $e3 >= $info['e3'] && $e5 >= $info['e5'] && $e7 >= $info['e7']) ? 1 : 0;
        }

        if (!$tight) {
            $key = $pos . '|' . $sum . '|' . $e2 . '|' . $e3 . '|' . $e5 . '|' . $e7 . '|' . ($started?1:0) . '|' . ($hasZero?1:0);
            if (isset($memo[$key])) return $memo[$key];
        }

        $limit = $tight ? $digits[$pos] : 9;
        $total = 0;
        for ($d = 0; $d <= $limit; $d++) {
            $newStarted = $started || $d != 0;
            $newHasZero = $hasZero;
            $newSum = $sum;
            $ne2 = $e2; $ne3 = $e3; $ne5 = $e5; $ne7 = $e7;

            if ($newStarted) {
                if ($d == 0) {
                    $newHasZero = true;
                } else {
                    // digit is non-zero
                    $exp = $this->digitExp[$d];
                    $newSum += $d;
                    $ne2 += $exp[0];
                    $ne3 += $exp[1];
                    $ne5 += $exp[2];
                    $ne7 += $exp[3];
                }
            }

            $newTight = $tight && ($d == $limit);
            $total += $this->dfs($pos + 1, $newSum, $ne2, $ne3, $ne5, $ne7, $newStarted, $newHasZero, $newTight, $digits, $memo);
        }

        if (!$tight) {
            $memo[$key] = $total;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulNumbers(_ l: Int, _ r: Int) -> Int {
        let result = countUpTo(r) - countUpTo(l - 1)
        return Int(result)
    }
    
    private func countUpTo(_ n: Int) -> Int64 {
        if n <= 0 { return 0 }
        var digits = [Int]()
        var x = n
        while x > 0 {
            digits.append(x % 10)
            x /= 10
        }
        digits.reverse()
        let len = digits.count
        var total: Int64 = 0
        
        for s in 1...81 {
            struct Key: Hashable {
                let pos: Int
                let tight: Bool
                let sum: Int
                let prod: Int
                let started: Bool
            }
            var memo = [Key: Int64]()
            
            func dfs(_ pos: Int, _ tight: Bool, _ sum: Int, _ prod: Int, _ started: Bool) -> Int64 {
                if pos == len {
                    return (started && sum == s && prod == 0) ? 1 : 0
                }
                let key = Key(pos: pos, tight: tight, sum: sum, prod: prod, started: started)
                if let cached = memo[key] { return cached }
                
                var res: Int64 = 0
                let limit = tight ? digits[pos] : 9
                for d in 0...limit {
                    let newTight = tight && (d == limit)
                    var nStarted = started
                    var nSum = sum
                    var nProd = prod
                    
                    if !started && d == 0 {
                        // still leading zeros, nothing changes
                    } else {
                        nStarted = true
                        nSum += d
                        if started && d == 0 {
                            nProd = 0
                        } else {
                            nProd = (prod * d) % s
                        }
                    }
                    
                    if nSum > s { continue }
                    res += dfs(pos + 1, newTight, nSum, nProd, nStarted)
                }
                
                memo[key] = res
                return res
            }
            
            let initProd = 1 % s
            total += dfs(0, true, 0, initProd, false)
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    private data class State(
        val pos: Int,
        val sum: Int,
        val e2: Int,
        val e3: Int,
        val e5: Int,
        val e7: Int,
        val started: Boolean,
        val hasZero: Boolean
    )

    // required exponents for each possible sum (0..81)
    private val needE2 = IntArray(82)
    private val needE3 = IntArray(82)
    private val needE5 = IntArray(82)
    private val needE7 = IntArray(82)

    init {
        for (s in 1..81) {
            var v = s
            var cnt2 = 0
            while (v % 2 == 0) { cnt2++; v /= 2 }
            var cnt3 = 0
            while (v % 3 == 0) { cnt3++; v /= 3 }
            var cnt5 = 0
            while (v % 5 == 0) { cnt5++; v /= 5 }
            var cnt7 = 0
            while (v % 7 == 0) { cnt7++; v /= 7 }
            needE2[s] = cnt2
            needE3[s] = cnt3
            needE5[s] = cnt5
            needE7[s] = cnt7
        }
    }

    fun beautifulNumbers(l: Int, r: Int): Int {
        return (countUpTo(r) - countUpTo(l - 1)).toInt()
    }

    private fun countUpTo(x: Int): Long {
        if (x <= 0) return 0L
        val digits = x.toString().map { it - '0' }.toIntArray()
        val memo = HashMap<State, Long>()
        fun dfs(pos: Int, tight: Boolean, started: Boolean, hasZero: Boolean,
                sum: Int, e2: Int, e3: Int, e5: Int, e7: Int): Long {
            if (pos == digits.size) {
                if (!started) return 0L
                if (hasZero) return 1L
                // check divisibility using prime exponents
                val req2 = needE2[sum]
                val req3 = needE3[sum]
                val req5 = needE5[sum]
                val req7 = needE7[sum]
                return if (e2 >= req2 && e3 >= req3 && e5 >= req5 && e7 >= req7) 1L else 0L
            }
            if (!tight) {
                val key = State(pos, sum, e2, e3, e5, e7, started, hasZero)
                memo[key]?.let { return it }
            }
            var limit = if (tight) digits[pos] else 9
            var total = 0L
            for (d in 0..limit) {
                val nextTight = tight && d == limit
                val nextStarted = started || d != 0
                var nextHasZero = hasZero
                var ns = sum
                var ne2 = e2
                var ne3 = e3
                var ne5 = e5
                var ne7 = e7
                if (nextStarted) {
                    if (d == 0) {
                        nextHasZero = true
                    } else {
                        ns += d
                        when (d) {
                            2 -> { ne2 = minOf(ne2 + 1, 6) }
                            3 -> { ne3 = minOf(ne3 + 1, 4) }
                            4 -> { ne2 = minOf(ne2 + 2, 6) }
                            5 -> { ne5 = minOf(ne5 + 1, 2) }
                            6 -> {
                                ne2 = minOf(ne2 + 1, 6)
                                ne3 = minOf(ne3 + 1, 4)
                            }
                            7 -> { ne7 = 1 }
                            8 -> { ne2 = minOf(ne2 + 3, 6) }
                            9 -> { ne3 = minOf(ne3 + 2, 4) }
                        }
                    }
                }
                total += dfs(pos + 1, nextTight, nextStarted, nextHasZero,
                             ns, ne2, ne3, ne5, ne7)
            }
            if (!tight) {
                val key = State(pos, sum, e2, e3, e5, e7, started, hasZero)
                memo[key] = total
            }
            return total
        }
        return dfs(0, true, false, false, 0, 0, 0, 0, 0)
    }
}
```

## Dart

```dart
class Solution {
  int beautifulNumbers(int l, int r) {
    return _countUpTo(r) - _countUpTo(l - 1);
  }

  int _countUpTo(int x) {
    if (x <= 0) return 0;
    List<int> digits = _toDigits(x);
    int n = digits.length;

    // Count numbers without any zero digit.
    var memoNoZero = List.generate(n, (_) => List.filled(2, -1));
    int dfsNoZero(int pos, bool tight, bool started) {
      if (pos == n) return started ? 1 : 0;
      if (!tight && memoNoZero[pos][started ? 1 : 0] != -1) {
        return memoNoZero[pos][started ? 1 : 0];
      }
      int limit = tight ? digits[pos] : 9;
      int res = 0;
      for (int d = 0; d <= limit; ++d) {
        bool ntight = tight && d == limit;
        if (!started && d == 0) {
          res += dfsNoZero(pos + 1, ntight, false);
        } else {
          if (d == 0) continue; // zero not allowed after start
          res += dfsNoZero(pos + 1, ntight, true);
        }
      }
      if (!tight) memoNoZero[pos][started ? 1 : 0] = res;
      return res;
    }

    int noZero = dfsNoZero(0, true, false);
    int total = x;
    int ans = total - noZero; // all numbers containing a zero are beautiful

    // Numbers without zeros: need product % sum == 0.
    for (int S = 1; S <= 81; ++S) {
      // dp[pos][tightFlag][started][sum][prodMod]
      var dp = List.generate(
          n,
          (_) => List.generate(
              2,
              (_) => List.generate(
                  2, (_) => List.generate(S + 1, (_) => List.filled(S, -1)))));

      int dfs(int pos, bool tight, bool started, int sum, int prodMod) {
        if (pos == n) {
          return (started && sum == S && prodMod % S == 0) ? 1 : 0;
        }
        if (!tight) {
          int cached = dp[pos][0][started ? 1 : 0][sum][prodMod];
          if (cached != -1) return cached;
        }
        int limit = tight ? digits[pos] : 9;
        int res = 0;
        for (int d = 0; d <= limit; ++d) {
          bool ntight = tight && d == limit;
          if (!started && d == 0) {
            // still leading zeros, product identity is 1 % S
            res += dfs(pos + 1, ntight, false, 0, 1 % S);
          } else {
            if (d == 0) continue; // zero not allowed inside number
            int newSum = sum + d;
            if (newSum > S) continue;
            int newProd = (prodMod * d) % S;
            res += dfs(pos + 1, ntight, true, newSum, newProd);
          }
        }
        if (!tight) dp[pos][0][started ? 1 : 0][sum][prodMod] = res;
        return res;
      }

      ans += dfs(0, true, false, 0, 1 % S);
    }

    return ans;
  }

  List<int> _toDigits(int x) {
    if (x == 0) return [0];
    List<int> rev = [];
    while (x > 0) {
      rev.add(x % 10);
      x ~/= 10;
    }
    return rev.reversed.toList();
  }
}
```

## Golang

```go
package main

import "strconv"

type key struct {
	pos      uint8
	sum      uint8
	e2       uint8
	e3       uint8
	e5       uint8
	e7       uint8
	zeroSeen bool
	started  bool
}

var (
	digits []int
	memo   map[key]int64
)

func dfs(pos int, sum int, e2, e3, e5, e7 uint8, zeroSeen, started, tight bool) int64 {
	if pos == len(digits) {
		if !started {
			return 0
		}
		if zeroSeen {
			return 1
		}
		prod := int64(1)
		for i := uint8(0); i < e2; i++ {
			prod *= 2
		}
		for i := uint8(0); i < e3; i++ {
			prod *= 3
		}
		for i := uint8(0); i < e5; i++ {
			prod *= 5
		}
		for i := uint8(0); i < e7; i++ {
			prod *= 7
		}
		if sum > 0 && prod%int64(sum) == 0 {
			return 1
		}
		return 0
	}

	if !tight {
		k := key{uint8(pos), uint8(sum), e2, e3, e5, e7, zeroSeen, started}
		if v, ok := memo[k]; ok {
			return v
		}
		defer func() {
			memo[k] = dfs(pos, sum, e2, e3, e5, e7, zeroSeen, started, false)
		}()
	}

	limit := 9
	if tight {
		limit = digits[pos]
	}
	var total int64
	for d := 0; d <= limit; d++ {
		ntight := tight && (d == limit)
		nstarted := started || d != 0
		nzero := zeroSeen
		nsum := sum
		ne2, ne3, ne5, ne7 := e2, e3, e5, e7

		if nstarted {
			if d == 0 {
				nzero = true
			} else {
				nsum += d
				switch d {
				case 2:
					ne2++
				case 3:
					ne3++
				case 4:
					ne2 += 2
				case 5:
					ne5++
				case 6:
					ne2++
					ne3++
				case 7:
					ne7++
				case 8:
					ne2 += 3
				case 9:
					ne3 += 2
				}
			}
		}

		if nzero {
			ne2, ne3, ne5, ne7 = 0, 0, 0, 0
		}
		total += dfs(pos+1, nsum, ne2, ne3, ne5, ne7, nzero, nstarted, ntight)
	}
	return total
}

func countUpTo(n int) int64 {
	if n <= 0 {
		return 0
	}
	s := strconv.Itoa(n)
	digits = make([]int, len(s))
	for i, ch := range s {
		digits[i] = int(ch - '0')
	}
	memo = make(map[key]int64)
	return dfs(0, 0, 0, 0, 0, 0, false, false, true)
}

func beautifulNumbers(l int, r int) int {
	return int(countUpTo(r) - countUpTo(l-1))
}
```

## Ruby

```ruby
def beautiful_numbers(l, r)
  def count_up_to(x)
    return 0 if x <= 0
    digits = x.to_s.chars.map(&:to_i)
    n = digits.length
    memo = {}

    dfs = lambda do |pos, tight, started, sum, prod|
      if pos == n
        return (started && prod % sum == 0) ? 1 : 0
      end

      unless tight
        key = [pos, started, sum, prod]
        cached = memo[key]
        return cached if cached
      end

      limit = tight ? digits[pos] : 9
      total = 0

      (0..limit).each do |d|
        ntight = tight && d == limit
        nstarted = started || d != 0
        nsum = sum
        nprod = prod
        if nstarted
          if d == 0
            nprod = 0
          else
            nprod = prod * d
          end
          nsum += d
        end
        total += dfs.call(pos + 1, ntight, nstarted, nsum, nprod)
      end

      unless tight
        memo[[pos, started, sum, prod]] = total
      end
      total
    end

    dfs.call(0, true, false, 0, 1)
  end

  count_up_to(r) - count_up_to(l - 1)
end
```

## Scala

```scala
object Solution {
  def beautifulNumbers(l: Int, r: Int): Int = {
    def countUpTo(x: Int): Long = {
      if (x <= 0) return 0L
      val digits = x.toString.map(_.asDigit).toArray
      val n = digits.length
      import scala.collection.mutable

      val memo = mutable.Map[(Int, Int, Int, Boolean, Boolean), Long]()

      def dfs(pos: Int, sum: Int, prod: Int, zeroSeen: Boolean, started: Boolean, tight: Boolean): Long = {
        if (pos == n) {
          if (!started) 0L
          else if (zeroSeen) 1L
          else if (sum > 0 && prod % sum == 0) 1L
          else 0L
        } else {
          if (!tight) {
            val key = (pos, sum, prod, zeroSeen, started)
            memo.getOrElseUpdate(key, {
              var total = 0L
              val limit = 9
              for (d <- 0 to limit) {
                val ntight = false
                if (!started && d == 0) {
                  total += dfs(pos + 1, sum, prod, zeroSeen, false, ntight)
                } else {
                  if (zeroSeen || d == 0) {
                    total += dfs(pos + 1, 0, 0, true, true, ntight)
                  } else {
                    val newSum = sum + d
                    val newProd = prod * d
                    total += dfs(pos + 1, newSum, newProd, false, true, ntight)
                  }
                }
              }
              total
            })
          } else {
            var total = 0L
            val limit = digits(pos)
            for (d <- 0 to limit) {
              val ntight = tight && d == limit
              if (!started && d == 0) {
                total += dfs(pos + 1, sum, prod, zeroSeen, false, ntight)
              } else {
                if (zeroSeen || d == 0) {
                  total += dfs(pos + 1, 0, 0, true, true, ntight)
                } else {
                  val newSum = sum + d
                  val newProd = prod * d
                  total += dfs(pos + 1, newSum, newProd, false, true, ntight)
                }
              }
            }
            total
          }
        }
      }

      dfs(0, 0, 1, zeroSeen = false, started = false, tight = true)
    }

    (countUpTo(r) - countUpTo(l - 1)).toInt
  }
}
```

## Rust

```rust
use std::cmp::max;

fn count_upto(x: i32) -> i64 {
    if x <= 0 {
        return 0;
    }
    let digits: Vec<i32> = x
        .to_string()
        .chars()
        .map(|c| (c as u8 - b'0') as i32)
        .collect();
    let n = digits.len();

    // helper to compute index in flat memo array
    fn idx(
        pos: usize,
        sum: usize,
        prod: usize,
        started: usize,
        tight: usize,
        n: usize,
        s: usize,
    ) -> usize {
        ((((pos * (s + 1) + sum) * s + prod) * 2 + started) * 2 + tight)
    }

    // recursive DP
    fn dfs(
        pos: usize,
        sum: usize,
        prod: usize,
        started: bool,
        tight: bool,
        digits: &Vec<i32>,
        s: usize,
        n: usize,
        memo: &mut Vec<i64>,
    ) -> i64 {
        if pos == n {
            return if started && sum == s && prod % s == 0 { 1 } else { 0 };
        }
        let ti = if tight { 1 } else { 0 };
        let st = if started { 1 } else { 0 };
        let index = idx(pos, sum, prod, st, ti, n, s);
        if memo[index] != -1 {
            return memo[index];
        }
        let limit = if tight { digits[pos] } else { 9 };
        let mut res: i64 = 0;
        for d in 0..=limit {
            let nd_started = started || d != 0;
            let nd_sum = if nd_started { sum + d as usize } else { sum };
            if nd_sum > s {
                continue;
            }
            let nd_prod = if !nd_started {
                prod
            } else {
                if started && d == 0 {
                    0
                } else {
                    (prod * d as usize) % s
                }
            };
            let nd_tight = tight && d == limit;
            res += dfs(
                pos + 1,
                nd_sum,
                nd_prod,
                nd_started,
                nd_tight,
                digits,
                s,
                n,
                memo,
            );
        }
        memo[index] = res;
        res
    }

    let mut total: i64 = 0;
    for s in 1..=81 {
        // size of memo array
        let size = (n + 1) * (s + 1) * s * 2 * 2;
        let mut memo = vec![-1i64; size];
        let init_prod = 1 % s;
        total += dfs(0, 0, init_prod, false, true, &digits, s, n, &mut memo);
    }
    total
}

impl Solution {
    pub fn beautiful_numbers(l: i32, r: i32) -> i32 {
        let ans = count_upto(r) - count_upto(l - 1);
        ans as i32
    }
}
```

## Racket

```racket
(define (beautiful-numbers l r)
  (-> exact-integer? exact-integer? exact-integer?)
  (define (int->digits n)
    (let loop ((x n) (acc '()))
      (if (= x 0)
          (if (null? acc) '(0) acc)
          (loop (quotient x 10) (cons (remainder x 10) acc)))))
  (define (count-up-to n)
    (if (<= n 0) 0
        (let* ((digits-list (int->digits n))
               (len (length digits-list))
               (digits (list->vector digits-list)))
          (define (count-for-s S)
            (define memo (make-hash))
            (define init-prod (if (= S 1) 0 1)) ; identity modulo S
            (define (key pos sum prod started)
              (list pos sum prod started))
            (define (dfs pos sum prod started tight)
              (if (= pos len)
                  (if (and started (= sum S) (= (modulo prod S) 0)) 1 0)
                  (let ((maxd (if tight (vector-ref digits pos) 9)))
                    (if (not tight)
                        (let ((k (key pos sum prod started)))
                          (hash-ref memo k
                                    (lambda ()
                                      (define total
                                        (let loop ((d 0) (acc 0))
                                          (if (> d maxd)
                                              acc
                                              (let* ((new-started (or started (not (= d 0))))
                                                     (new-sum (if new-started (+ sum d) sum))
                                                     (new-prod (if new-started
                                                                   (modulo (* prod d) S)
                                                                   prod)))
                                                (if (> new-sum S)
                                                    (loop (+ d 1) acc)
                                                    (let ((cnt (dfs (+ pos 1) new-sum new-prod new-started #f)))
                                                      (loop (+ d 1) (+ acc cnt))))))))
                                      (hash-set! memo k total)
                                      total))))
                        (let loop ((d 0) (acc 0))
                          (if (> d maxd)
                              acc
                              (let* ((new-started (or started (not (= d 0))))
                                     (new-sum (if new-started (+ sum d) sum))
                                     (new-prod (if new-started
                                                   (modulo (* prod d) S)
                                                   prod)))
                                (if (> new-sum S)
                                    (loop (+ d 1) acc)
                                    (let ((cnt (dfs (+ pos 1)
                                                    new-sum
                                                    new-prod
                                                    new-started
                                                    (and tight (= d maxd)))))
                                      (loop (+ d 1) (+ acc cnt))))))))))
            (dfs 0 0 init-prod #f #t))
          (let loop ((s 1) (total 0))
            (if (> s 81)
                total
                (loop (+ s 1) (+ total (count-for-s s)))))))))
  (- (count-up-to r) (count-up-to (- l 1))))
```

## Erlang

```erlang
-spec beautiful_numbers(L :: integer(), R :: integer()) -> integer().
beautiful_numbers(L, R) ->
    count(R) - count(L - 1).

%% Count beautiful numbers in [1, N]
count(N) when N < 1 ->
    0;
count(N) ->
    DigitsStr = integer_to_list(N),
    Digits = [C - $0 || C <- DigitsStr],
    dfs(0, true, false, 0, 1, Digits, N).

%% Digit DP with memoization (process dictionary)
dfs(Pos, Tight, Started, Sum, Prod, Digits, N) ->
    case Tight of
        false ->
            Key = {Pos, Started, Sum, Prod, N},
            case get(Key) of
                undefined ->
                    Count = dfs_compute(Pos, Tight, Started, Sum, Prod, Digits, N),
                    put(Key, Count),
                    Count;
                C -> C
            end;
        true ->
            dfs_compute(Pos, Tight, Started, Sum, Prod, Digits, N)
    end.

dfs_compute(Pos, _Tight, Started, Sum, Prod, Digits, _N) ->
    Len = length(Digits),
    if Pos == Len ->
            case Started of
                false -> 0;
                true ->
                    if Prod == 0 ->
                            1;
                       Sum > 0, Prod rem Sum == 0 ->
                            1;
                       true ->
                            0
                    end
            end;
       true ->
            Limit = if _Tight -> lists:nth(Pos + 1, Digits); true -> 9 end,
            loop(0, Limit, Pos, _Tight, Started, Sum, Prod, Digits, _N, 0)
    end.

loop(D, Limit, Pos, Tight, Started, Sum, Prod, Digits, N, Acc) when D =< Limit ->
    NewTight = Tight andalso D == Limit,
    NewStarted = Started orelse D /= 0,
    NewSum = if NewStarted -> Sum + D else Sum end,
    NewProd =
        case {NewStarted, Prod, D} of
            {false, _, _} -> Prod;               % still leading zeros
            {true, 0, _} -> 0;
            {true, _, 0} -> 0;
            {true, P, d} -> P * d
        end,
    Count = dfs(Pos + 1, NewTight, NewStarted, NewSum, NewProd, Digits, N),
    loop(D + 1, Limit, Pos, Tight, Started, Sum, Prod, Digits, N, Acc + Count);
loop(_, _, _, _, _, _, _, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_numbers(l :: integer, r :: integer) :: integer
  def beautiful_numbers(l, r) do
    count_up_to(r) - count_up_to(l - 1)
  end

  # count of beautiful numbers in [1, limit]
  defp count_up_to(limit) when limit <= 0, do: 0

  defp count_up_to(limit) do
    digits = Integer.digits(limit)

    {cnt_nozero, _} = dfs_nozero(0, true, false, digits, %{})
    max_sum = 9 * length(digits)

    sum_good =
      Enum.reduce(1..max_sum, 0, fn s, acc ->
        init_mod = rem(1, s)
        {c, _} = dfs_sum(0, true, false, 0, init_mod, s, digits, %{})
        acc + c
      end)

    limit - cnt_nozero + sum_good
  end

  # DP for counting numbers without any zero digit
  defp dfs_nozero(pos, tight, started, digits, memo) do
    len = length(digits)

    if pos == len do
      {if started, do: 1, else: 0, memo}
    else
      key = {pos, started}

      if !tight and Map.has_key?(memo, key) do
        {Map.get(memo, key), memo}
      else
        max_digit = if tight, do: Enum.at(digits, pos), else: 9

        {total, memo2} =
          Enum.reduce(0..max_digit, {0, memo}, fn d, {acc, mem} ->
            new_started = started or d != 0

            cond do
              new_started and d == 0 ->
                {acc, mem}

              true ->
                new_tight = tight && d == max_digit
                {cnt, mem2} = dfs_nozero(pos + 1, new_tight, new_started, digits, mem)
                {acc + cnt, mem2}
            end
          end)

        memo3 = if !tight, do: Map.put(memo2, key, total), else: memo2
        {total, memo3}
      end
    end
  end

  # DP for counting numbers without zero digit,
  # having sum == s and product % s == 0
  defp dfs_sum(pos, tight, started, cur_sum, cur_mod, s, digits, memo) do
    len = length(digits)

    if pos == len do
      cond =
        started and cur_sum == s and rem(cur_mod, s) == 0

      {if cond, do: 1, else: 0, memo}
    else
      key = {pos, started, cur_sum, cur_mod}

      if !tight and Map.has_key?(memo, key) do
        {Map.get(memo, key), memo}
      else
        max_digit = if tight, do: Enum.at(digits, pos), else: 9

        {total, memo2} =
          Enum.reduce(0..max_digit, {0, memo}, fn d, {acc, mem} ->
            new_started = started or d != 0

            cond do
              # still leading zeros
              not new_started ->
                new_tight = tight && d == max_digit
                init_mod = rem(1, s)
                {cnt, mem2} =
                  dfs_sum(pos + 1, new_tight, false, 0, init_mod, s, digits, mem)

                {acc + cnt, mem2}

              # zero digit not allowed after start
              new_started and d == 0 ->
                {acc, mem}

              true ->
                if cur_sum + d > s do
                  {acc, mem}
                else
                  new_tight = tight && d == max_digit
                  new_mod = rem(cur_mod * d, s)

                  {cnt, mem2} =
                    dfs_sum(
                      pos + 1,
                      new_tight,
                      true,
                      cur_sum + d,
                      new_mod,
                      s,
                      digits,
                      mem
                    )

                  {acc + cnt, mem2}
                end
            end
          end)

        memo3 = if !tight, do: Map.put(memo2, key, total), else: memo2
        {total, memo3}
      end
    end
  end
end
```
