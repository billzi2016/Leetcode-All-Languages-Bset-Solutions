# 3343. Count Number of Balanced Permutations

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1'000'000'007;
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }

    int countBalancedPermutations(string num) {
        int n = num.size();
        vector<int> cnt(10,0);
        long long totalSum = 0;
        for(char c: num){
            int d = c - '0';
            cnt[d]++; 
            totalSum += d;
        }
        if (totalSum % 2) return 0;
        int target = totalSum / 2;

        int evenCnt = (n + 1) / 2; // indices 0,2,...
        int oddCnt = n / 2;

        // factorials
        vector<long long> fact(n+1), invFact(n+1);
        fact[0] = 1;
        for(int i=1;i<=n;i++) fact[i] = fact[i-1]*i%MOD;
        invFact[n] = modpow(fact[n], MOD-2);
        for(int i=n;i>0;i--) invFact[i-1] = invFact[i]*i%MOD;

        // DP
        vector<vector<int>> cur(target+1, vector<int>(evenCnt+1, 0));
        vector<vector<int>> nxt(target+1, vector<int>(evenCnt+1, 0));
        cur[0][0] = 1;
        for(int d=0; d<=9; ++d){
            int c = cnt[d];
            if(c==0) continue;
            // reset nxt
            for(int s=0;s<=target;++s)
                fill(nxt[s].begin(), nxt[s].end(), 0);
            for(int s=0; s<=target; ++s){
                for(int e=0; e<=evenCnt; ++e){
                    int val = cur[s][e];
                    if(!val) continue;
                    for(int k=0; k<=c; ++k){
                        int ns = s + k*d;
                        if(ns > target) break;
                        int ne = e + k;
                        if(ne > evenCnt) continue;
                        long long add = (long long)val * invFact[k] % MOD * invFact[c - k] % MOD;
                        nxt[ns][ne] = (nxt[ns][ne] + add) % MOD;
                    }
                }
            }
            cur.swap(nxt);
        }

        int waysInvProd = cur[target][evenCnt];
        long long ans = waysInvProd * fact[evenCnt] % MOD * fact[oddCnt] % MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    
    private long modPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }
    
    public int countBalancedPermutations(String num) {
        int n = num.length();
        int[] cnt = new int[10];
        int totalSum = 0;
        for (char ch : num.toCharArray()) {
            int d = ch - '0';
            cnt[d]++;
            totalSum += d;
        }
        if ((totalSum & 1) == 1) return 0; // odd total sum cannot be balanced
        int target = totalSum / 2;
        int oddCount = n / 2;               // positions with index 1,3,...
        int evenCount = n - oddCount;       // positions with index 0,2,...
        
        // factorials up to n
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        
        long[][] dp = new long[oddCount + 1][target + 1];
        dp[0][0] = 1;
        
        for (int digit = 0; digit <= 9; digit++) {
            int c = cnt[digit];
            if (c == 0) continue;
            long[][] ndp = new long[oddCount + 1][target + 1];
            for (int usedOdd = 0; usedOdd <= oddCount; usedOdd++) {
                for (int sum = 0; sum <= target; sum++) {
                    long cur = dp[usedOdd][sum];
                    if (cur == 0) continue;
                    // distribute k copies of this digit to odd positions
                    for (int k = 0; k <= c; k++) {
                        int newOdd = usedOdd + k;
                        if (newOdd > oddCount) break;
                        int newSum = sum + digit * k;
                        if (newSum > target) break;
                        long ways = cur * invFact[k] % MOD * invFact[c - k] % MOD;
                        ndp[newOdd][newSum] += ways;
                        if (ndp[newOdd][newSum] >= MOD) ndp[newOdd][newSum] -= MOD;
                    }
                }
            }
            dp = ndp;
        }
        
        long res = dp[oddCount][target];
        res = res * fact[oddCount] % MOD;
        res = res * fact[evenCount] % MOD;
        return (int) res;
    }
}
```

## Python

```python
import sys

MOD = 10**9 + 7

class Solution(object):
    def countBalancedPermutations(self, num):
        """
        :type num: str
        :rtype: int
        """
        n = len(num)
        cnt = [0] * 10
        total_sum = 0
        for ch in num:
            d = ord(ch) - 48
            cnt[d] += 1
            total_sum += d

        if total_sum % 2 != 0:
            return 0

        half_sum = total_sum // 2
        odd_cnt = n // 2          # positions with index 1,3,...
        even_cnt = n - odd_cnt    # positions with index 0,2,...

        max_n = n
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        # dp[sum][odd_used]
        dp = [[0] * (odd_cnt + 1) for _ in range(half_sum + 1)]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            ndp = [[0] * (odd_cnt + 1) for _ in range(half_sum + 1)]
            for s in range(half_sum + 1):
                row = dp[s]
                if not any(row):
                    continue
                for o_used in range(odd_cnt + 1):
                    cur = row[o_used]
                    if cur == 0:
                        continue
                    # place j copies of digit d into odd positions
                    max_j = min(c, odd_cnt - o_used)
                    for j in range(max_j + 1):
                        ns = s + d * j
                        no = o_used + j
                        if ns > half_sum:
                            break
                        val = cur * inv_fact[j] % MOD * inv_fact[c - j] % MOD
                        ndp[ns][no] = (ndp[ns][no] + val) % MOD
            dp = ndp

        res = dp[half_sum][odd_cnt]
        if res == 0:
            return 0
        res = res * fact[odd_cnt] % MOD
        res = res * fact[even_cnt] % MOD
        return res
```

## Python3

```python
import sys

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        cnt = [0] * 10
        total = 0
        for ch in num:
            d = ord(ch) - 48
            cnt[d] += 1
            total += d

        if total & 1:
            return 0
        target = total // 2

        odd_cnt = n // 2          # positions with index 1,3,...
        even_cnt = n - odd_cnt    # positions with index 0,2,...

        if target > 9 * odd_cnt:
            return 0

        max_n = n
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        dp = [[0] * (target + 1) for _ in range(odd_cnt + 1)]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            ndp = [[0] * (target + 1) for _ in range(odd_cnt + 1)]
            for used_odd in range(odd_cnt + 1):
                row = dp[used_odd]
                for cur_sum in range(target + 1):
                    cur_val = row[cur_sum]
                    if cur_val == 0:
                        continue
                    max_j = min(c, odd_cnt - used_odd)
                    for j in range(max_j + 1):
                        new_odd = used_odd + j
                        new_sum = cur_sum + d * j
                        if new_sum > target:
                            break
                        add = cur_val * inv_fact[j] % MOD * inv_fact[c - j] % MOD
                        ndp[new_odd][new_sum] = (ndp[new_odd][new_sum] + add) % MOD
            dp = ndp

        res = dp[odd_cnt][target]
        if res == 0:
            return 0
        res = res * fact[odd_cnt] % MOD
        res = res * fact[even_cnt] % MOD
        return res
```

## C

```c
#include <string.h>
#include <stdlib.h>

#define MOD 1000000007
static long long modpow(long long a,long long e){
    long long r=1;
    while(e){
        if(e&1) r=r*a%MOD;
        a=a*a%MOD;
        e>>=1;
    }
    return r;
}

int countBalancedPermutations(char* num) {
    int n = strlen(num);
    int cnt[10] = {0};
    int total = 0;
    for (int i = 0; i < n; ++i) {
        int d = num[i] - '0';
        cnt[d]++;
        total += d;
    }
    if (total % 2) return 0;
    int target = total / 2;
    int oddCnt = n / 2;               // positions with index 1,3,...
    int evenCnt = n - oddCnt;

    static long long fact[81], invFact[81];
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i-1] * i % MOD;
    invFact[n] = modpow(fact[n], MOD - 2);
    for (int i = n; i >= 1; --i) invFact[i-1] = invFact[i] * i % MOD;

    static long long dp[81][361];
    static long long ndp[81][361];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    for (int d = 0; d <= 9; ++d) {
        int c = cnt[d];
        if (c == 0) continue;               // no effect
        memset(ndp, 0, sizeof(ndp));
        for (int used = 0; used <= oddCnt; ++used) {
            for (int sum = 0; sum <= target; ++sum) {
                long long cur = dp[used][sum];
                if (!cur) continue;
                for (int j = 0; j <= c; ++j) {
                    int nUsed = used + j;
                    if (nUsed > oddCnt) break;
                    int nSum = sum + d * j;
                    if (nSum > target) break;
                    long long val = cur * invFact[j] % MOD * invFact[c - j] % MOD;
                    ndp[nUsed][nSum] += val;
                    if (ndp[nUsed][nSum] >= MOD) ndp[nUsed][nSum] -= MOD;
                }
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }

    long long ways = dp[oddCnt][target];
    if (!ways) return 0;
    ways = ways * fact[oddCnt] % MOD;
    ways = ways * fact[evenCnt] % MOD;
    return (int)ways;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int CountBalancedPermutations(string num) {
        int n = num.Length;
        int[] cnt = new int[10];
        int total = 0;
        foreach (char ch in num) {
            int d = ch - '0';
            cnt[d]++;
            total += d;
        }
        if ((total & 1) == 1) return 0;
        int target = total / 2;
        int evenSlots = (n + 1) / 2; // indices 0,2,...
        int oddSlots = n / 2;
        
        // factorials
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        long[,] dp = new long[evenSlots + 1, target + 1];
        dp[0, 0] = 1;
        
        for (int d = 0; d <= 9; ++d) {
            int c = cnt[d];
            if (c == 0) continue; // no effect
            long[,] next = new long[evenSlots + 1, target + 1];
            for (int used = 0; used <= evenSlots; ++used) {
                for (int sum = 0; sum <= target; ++sum) {
                    long cur = dp[used, sum];
                    if (cur == 0) continue;
                    int maxK = Math.Min(c, evenSlots - used);
                    for (int k = 0; k <= maxK; ++k) {
                        int newUsed = used + k;
                        int newSum = sum + k * d;
                        if (newSum > target) break;
                        long add = cur * invFact[k] % MOD * invFact[c - k] % MOD;
                        long val = next[newUsed, newSum] + add;
                        if (val >= MOD) val -= MOD;
                        next[newUsed, newSum] = val;
                    }
                }
            }
            dp = next;
        }
        
        long ways = dp[evenSlots, target];
        ways = ways * fact[evenSlots] % MOD;
        ways = ways * fact[oddSlots] % MOD;
        return (int)ways;
    }
    
    private static long ModPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {number}
 */
var countBalancedPermutations = function(num) {
    const MOD = 1000000007n;
    const n = num.length;
    const cnt = Array(10).fill(0);
    let total = 0;
    for (let ch of num) {
        const d = ch.charCodeAt(0) - 48;
        cnt[d]++;
        total += d;
    }
    if (total % 2 !== 0) return 0;
    const target = total / 2;
    const oddCnt = Math.floor(n / 2); // positions with index 1,3,...
    
    // precompute factorials and inverse factorials up to n
    const fact = Array(n + 1).fill(0n);
    const invFact = Array(n + 1).fill(0n);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base, exp) => {
        let b = base % MOD;
        let e = exp;
        let res = 1n;
        while (e > 0) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const C = (N, K) => {
        if (K < 0 || K > N) return 0n;
        return (((fact[N] * invFact[K]) % MOD) * invFact[N - K]) % MOD;
    };
    
    // suffix sums of remaining digit counts
    const suff = Array(11).fill(0);
    for (let i = 9; i >= 0; --i) {
        suff[i] = cnt[i] + suff[i + 1];
    }
    
    const memo = new Map();
    const dfs = (i, sumNeeded, oddRemain) => {
        if (sumNeeded < 0 || oddRemain < 0) return 0n;
        if (i === 10) {
            return (sumNeeded === 0 && oddRemain === 0) ? 1n : 0n;
        }
        const key = i + '|' + sumNeeded + '|' + oddRemain;
        if (memo.has(key)) return memo.get(key);
        const totalRem = suff[i]; // digits from i..9 not yet placed
        const evenRemain = totalRem - oddRemain;
        let res = 0n;
        const maxJ = Math.min(cnt[i], oddRemain);
        const minJ = Math.max(0, cnt[i] - evenRemain); // need enough even slots
        for (let j = minJ; j <= maxJ; ++j) {
            const newSum = sumNeeded - j * i;
            if (newSum < 0) continue;
            const waysOdd = C(oddRemain, j);
            const waysEven = C(evenRemain, cnt[i] - j);
            const sub = dfs(i + 1, newSum, oddRemain - j);
            res = (res + ((waysOdd * waysEven) % MOD) * sub) % MOD;
        }
        memo.set(key, res);
        return res;
    };
    
    const ans = dfs(0, target, oddCnt);
    return Number(ans);
};
```

## Typescript

```typescript
function countBalancedPermutations(num: string): number {
    const MOD = 1000000007n;
    const n = num.length;
    const cnt = new Array(10).fill(0);
    let totalSum = 0;
    for (const ch of num) {
        const d = ch.charCodeAt(0) - 48;
        cnt[d]++;
        totalSum += d;
    }
    if (totalSum % 2 !== 0) return 0;
    const target = totalSum / 2;
    const evenCnt = Math.ceil(n / 2); // indices 0,2,...
    const oddCnt = n - evenCnt;

    const maxN = n;
    const fac: bigint[] = new Array(maxN + 1);
    const invFac: bigint[] = new Array(maxN + 1);
    fac[0] = 1n;
    for (let i = 1; i <= maxN; ++i) fac[i] = fac[i - 1] * BigInt(i) % MOD;

    function modPow(base: bigint, exp: bigint): bigint {
        let res = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    }

    invFac[maxN] = modPow(fac[maxN], MOD - 2n);
    for (let i = maxN; i > 0; --i) {
        invFac[i - 1] = invFac[i] * BigInt(i) % MOD;
    }

    function C(n: number, k: number): bigint {
        if (k < 0 || k > n) return 0n;
        return fac[n] * invFac[k] % MOD * invFac[n - k] % MOD;
    }

    // dp[usedEven][sumEven] = ways
    const dp: bigint[][] = Array.from({ length: evenCnt + 1 }, () => new Array(target + 1).fill(0n));
    dp[0][0] = 1n;

    let processedTotal = 0;
    for (let d = 0; d <= 9; ++d) {
        const c = cnt[d];
        if (c === 0) continue;
        const ndp: bigint[][] = Array.from({ length: evenCnt + 1 }, () => new Array(target + 1).fill(0n));
        for (let used = 0; used <= evenCnt; ++used) {
            const evenRemBase = evenCnt - used;
            for (let sum = 0; sum <= target; ++sum) {
                const curVal = dp[used][sum];
                if (curVal === 0n) continue;
                const oddUsedSoFar = processedTotal - used;
                const oddRemBase = oddCnt - oddUsedSoFar;
                // j = number of digit d placed in even positions
                const maxJ = Math.min(c, evenRemBase);
                for (let j = 0; j <= maxJ; ++j) {
                    const k = c - j; // placed in odd positions
                    if (k > oddRemBase) continue;
                    const newUsed = used + j;
                    const newSum = sum + d * j;
                    if (newSum > target) continue;
                    let ways = curVal;
                    ways = ways * C(evenRemBase, j) % MOD;
                    ways = ways * C(oddRemBase, k) % MOD;
                    ndp[newUsed][newSum] = (ndp[newUsed][newSum] + ways) % MOD;
                }
            }
        }
        for (let i = 0; i <= evenCnt; ++i) {
            dp[i] = ndp[i];
        }
        processedTotal += c;
    }

    const ans = dp[evenCnt][target] % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param String $num
     * @return Integer
     */
    function countBalancedPermutations($num) {
        $n = strlen($num);
        $cnt = array_fill(0, 10, 0);
        $totalSum = 0;
        for ($i = 0; $i < $n; ++$i) {
            $d = intval($num[$i]);
            $cnt[$d]++;
            $totalSum += $d;
        }
        if ($totalSum % 2 != 0) return 0;
        $target = intdiv($totalSum, 2);
        $oddSlots = intdiv($n, 2);               // positions with index %2 == 1
        $evenSlots = $n - $oddSlots;             // positions with index %2 == 0

        if ($target > $oddSlots * 9) return 0;

        // factorials and inverse factorials
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; ++$i) {
            $fact[$i] = ($fact[$i - 1] * $i) % self::MOD;
        }
        $invFact = array_fill(0, $n + 1, 1);
        $invFact[$n] = $this->modPow($fact[$n], self::MOD - 2);
        for ($i = $n; $i >= 1; --$i) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % self::MOD;
        }

        // combination function
        $comb = function($a, $b) use (&$fact, &$invFact) {
            if ($b < 0 || $b > $a) return 0;
            return ((($fact[$a] * $invFact[$b]) % self::MOD) * $invFact[$a - $b]) % self::MOD;
        };

        // suffix sums of counts for quick remaining digit count
        $suffix = array_fill(0, 11, 0);
        for ($i = 9; $i >= 0; --$i) {
            $suffix[$i] = $suffix[$i + 1] + $cnt[$i];
        }

        $memo = [];

        $dfs = function($digit, $remainSum, $oddLeft) use (
            &$dfs, &$cnt, &$comb, &$suffix, &$memo
        ) {
            if ($digit == 10) {
                return ($remainSum == 0 && $oddLeft == 0) ? 1 : 0;
            }
            $key = $digit . '|' . $remainSum . '|' . $oddLeft;
            if (isset($memo[$key])) return $memo[$key];

            $totalRem = $suffix[$digit];
            $evenLeft = $totalRem - $oddLeft;

            $ans = 0;
            $maxK = min($cnt[$digit], $oddLeft);
            for ($k = 0; $k <= $maxK; ++$k) {
                $needEven = $cnt[$digit] - $k;
                if ($needEven > $evenLeft) continue;

                $newSum = $remainSum - $k * $digit;
                if ($newSum < 0) continue;

                $waysOdd = $comb($oddLeft, $k);
                $waysEven = $comb($evenLeft, $needEven);
                $ways = ($waysOdd * $waysEven) % self::MOD;

                $sub = $dfs($digit + 1, $newSum, $oddLeft - $k);
                if ($sub != 0) {
                    $ans = ($ans + $ways * $sub) % self::MOD;
                }
            }

            $memo[$key] = $ans;
            return $ans;
        };

        return $dfs(0, $target, $oddSlots);
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func countBalancedPermutations(_ num: String) -> Int {
        var cnt = [Int](repeating: 0, count: 10)
        var totalSum = 0
        for ch in num {
            let d = Int(ch.unicodeScalars.first!.value - Unicode.Scalar("0").value)
            cnt[d] += 1
            totalSum += d
        }
        if totalSum % 2 != 0 { return 0 }
        let targetSum = totalSum / 2
        let n = num.count
        let evenCnt = (n + 1) / 2   // positions with index 0,2,...
        let oddCnt = n / 2
        
        // factorials and inverse factorials up to n
        var fact = [Int](repeating: 1, count: n + 1)
        for i in 1...n {
            fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
        }
        func modPow(_ base: Int, _ exp: Int) -> Int {
            var result = 1
            var b = base % MOD
            var e = exp
            while e > 0 {
                if e & 1 == 1 {
                    result = Int((Int64(result) * Int64(b)) % Int64(MOD))
                }
                b = Int((Int64(b) * Int64(b)) % Int64(MOD))
                e >>= 1
            }
            return result
        }
        var invFact = [Int](repeating: 1, count: n + 1)
        invFact[n] = modPow(fact[n], MOD - 2)
        if n > 0 {
            for i in stride(from: n, to: 0, by: -1) {
                invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
            }
        }
        
        // DP[e][s] = sum of product of inverse factorials for processed digits
        var dp = Array(repeating: Array(repeating: 0, count: targetSum + 1), count: evenCnt + 1)
        dp[0][0] = 1
        
        for digit in 0...9 {
            let c = cnt[digit]
            if c == 0 { continue }
            var next = Array(repeating: Array(repeating: 0, count: targetSum + 1), count: evenCnt + 1)
            for eUsed in 0...evenCnt {
                for sUsed in 0...targetSum {
                    let curVal = dp[eUsed][sUsed]
                    if curVal == 0 { continue }
                    // choose k copies of this digit to go to even positions
                    var maxK = c
                    if eUsed + maxK > evenCnt { maxK = evenCnt - eUsed }
                    for k in 0...maxK {
                        let newE = eUsed + k
                        let newS = sUsed + k * digit
                        if newS > targetSum { continue }
                        // factor = invFact[k] * invFact[c - k]
                        let factor = Int((Int64(invFact[k]) * Int64(invFact[c - k])) % Int64(MOD))
                        let add = Int((Int64(curVal) * Int64(factor)) % Int64(MOD))
                        next[newE][newS] += add
                        if next[newE][newS] >= MOD { next[newE][newS] -= MOD }
                    }
                }
            }
            dp = next
        }
        
        let ways = dp[evenCnt][targetSum]
        var ans = Int((Int64(ways) * Int64(fact[evenCnt])) % Int64(MOD))
        ans = Int((Int64(ans) * Int64(fact[oddCnt])) % Int64(MOD))
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*
const val MOD = 1_000_000_007L

class Solution {
    private lateinit var cnt: IntArray
    private lateinit var suffixCnt: IntArray
    private lateinit var fact: LongArray
    private lateinit var invFact: LongArray
    private lateinit var dp: Array<Array<LongArray>>
    private var target = 0
    private var oddTotal = 0

    fun countBalancedPermutations(num: String): Int {
        val n = num.length
        cnt = IntArray(10)
        for (ch in num) cnt[ch - '0']++
        var totalSum = 0
        for (d in 0..9) totalSum += d * cnt[d]
        if (totalSum % 2 != 0) return 0
        target = totalSum / 2
        oddTotal = n / 2          // floor(n/2)
        precomputeFactorials(n)
        suffixCnt = IntArray(11)
        for (i in 9 downTo 0) {
            suffixCnt[i] = suffixCnt[i + 1] + cnt[i]
        }
        dp = Array(11) { Array(target + 1) { LongArray(oddTotal + 1) { -1L } } }
        val ans = dfs(0, target, oddTotal)
        return (ans % MOD).toInt()
    }

    private fun dfs(digit: Int, sum: Int, oddLeft: Int): Long {
        if (sum < 0) return 0
        if (digit == 10) {
            return if (sum == 0 && oddLeft == 0) 1L else 0L
        }
        val memo = dp[digit][sum][oddLeft]
        if (memo != -1L) return memo

        var res = 0L
        val cntD = cnt[digit]
        val totalRem = suffixCnt[digit]          // digits remaining including current
        val evenLeft = totalRem - oddLeft         // slots for even positions among remaining digits

        val low = maxOf(0, cntD - evenLeft)
        val high = minOf(cntD, oddLeft)

        for (j in low..high) {
            val newSum = sum - j * digit
            if (newSum < 0) continue
            val waysOdd = comb(oddLeft, j)
            val waysEven = comb(evenLeft, cntD - j)
            val sub = dfs(digit + 1, newSum, oddLeft - j)
            res = (res + waysOdd * waysEven % MOD * sub) % MOD
        }

        dp[digit][sum][oddLeft] = res
        return res
    }

    private fun comb(n: Int, k: Int): Long {
        if (k < 0 || k > n) return 0L
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    }

    private fun precomputeFactorials(limit: Int) {
        fact = LongArray(limit + 1)
        invFact = LongArray(limit + 1)
        fact[0] = 1L
        for (i in 1..limit) fact[i] = fact[i - 1] * i % MOD
        invFact[limit] = modPow(fact[limit], MOD - 2)
        for (i in limit downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
    }

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) res = res * b % MOD
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }
}
```

## Dart

```dart
import 'dart:io';

class Solution {
  static const int MOD = 1000000007;
  late List<int> _fact;
  late List<int> _invFact;
  late List<int> _cnt;
  late List<List<List<int>>> _dp;

  int _modPow(int a, int e) {
    int res = 1;
    int base = a % MOD;
    while (e > 0) {
      if ((e & 1) == 1) {
        res = (res * base) % MOD;
      }
      base = (base * base) % MOD;
      e >>= 1;
    }
    return res;
  }

  void _initFactorials(int n) {
    _fact = List.filled(n + 1, 0);
    _invFact = List.filled(n + 1, 0);
    _fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
      _fact[i] = (_fact[i - 1] * i) % MOD;
    }
    _invFact[n] = _modPow(_fact[n], MOD - 2);
    for (int i = n; i > 0; --i) {
      _invFact[i - 1] = (_invFact[i] * i) % MOD;
    }
  }

  int _dfs(int idx, int sum, int oddLeft) {
    if (idx == 10) {
      return (sum == 0 && oddLeft == 0) ? 1 : 0;
    }
    int memo = _dp[idx][sum][oddLeft];
    if (memo != -1) return memo;

    int cnti = _cnt[idx];
    int maxJ = cnti < oddLeft ? cnti : oddLeft;
    int res = 0;
    for (int j = 0; j <= maxJ; ++j) {
      int add = j * idx;
      if (add > sum) break;
      int sub = _dfs(idx + 1, sum - add, oddLeft - j);
      if (sub == 0) continue;
      int term = (_invFact[j] * _invFact[cnti - j]) % MOD;
      term = (term * sub) % MOD;
      res += term;
      if (res >= MOD) res -= MOD;
    }
    _dp[idx][sum][oddLeft] = res;
    return res;
  }

  int countBalancedPermutations(String num) {
    int n = num.length;
    _cnt = List.filled(10, 0);
    int totalSum = 0;
    for (int i = 0; i < n; ++i) {
      int d = num.codeUnitAt(i) - 48;
      _cnt[d]++;
      totalSum += d;
    }
    if ((totalSum & 1) == 1) return 0;
    int half = totalSum ~/ 2;

    int oddCnt = n ~/ 2; // positions with odd index
    int evenCnt = n - oddCnt;

    _initFactorials(n);
    _dp = List.generate(
        11,
        (_) => List.generate(
            half + 1, (_) => List.filled(oddCnt + 1, -1)));

    int waysDenominator = _dfs(0, half, oddCnt);
    int ans = (((_fact[oddCnt] * _fact[evenCnt]) % MOD) *
        waysDenominator) %
        MOD;
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

const MOD int64 = 1000000007

func countBalancedPermutations(num string) int {
	n := len(num)
	cnt := [10]int{}
	total := 0
	for _, ch := range num {
		d := int(ch - '0')
		cnt[d]++
		total += d
	}
	if total%2 != 0 {
		return 0
	}
	half := total / 2
	eCnt := (n + 1) / 2 // positions with even index (0‑based)
	oCnt := n / 2

	maxN := n
	fact := make([]int64, maxN+1)
	invFact := make([]int64, maxN+1)
	fact[0] = 1
	for i := 1; i <= maxN; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	modPow := func(a, b int64) int64 {
		res := int64(1)
		a %= MOD
		for b > 0 {
			if b&1 == 1 {
				res = res * a % MOD
			}
			a = a * a % MOD
			b >>= 1
		}
		return res
	}
	invFact[maxN] = modPow(fact[maxN], MOD-2)
	for i := maxN; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	// dp[sum][usedEven]
	dp := make([][]int64, half+1)
	for i := 0; i <= half; i++ {
		dp[i] = make([]int64, eCnt+1)
	}
	dp[0][0] = 1

	for d := 0; d < 10; d++ {
		c := cnt[d]
		if c == 0 {
			continue
		}
		ndp := make([][]int64, half+1)
		for i := 0; i <= half; i++ {
			ndp[i] = make([]int64, eCnt+1)
		}
		valEven := int64(d) // digit value for sum contribution
		for s := 0; s <= half; s++ {
			for used := 0; used <= eCnt; used++ {
				cur := dp[s][used]
				if cur == 0 {
					continue
				}
				// distribute k copies of digit d to even positions
				maxK := c
				if maxK > eCnt-used {
					maxK = eCnt - used
				}
				for k := 0; k <= maxK; k++ {
					newSum := s + k*int(valEven)
					if newSum > half {
						break
					}
					newUsed := used + k
					weight := cur * invFact[k] % MOD * invFact[c-k] % MOD
					ndp[newSum][newUsed] = (ndp[newSum][newUsed] + weight) % MOD
				}
			}
		}
		dp = ndp
	}

	ans := dp[half][eCnt]
	ans = ans * fact[eCnt] % MOD
	ans = ans * fact[oCnt] % MOD
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e, mod)
  result = 1
  a %= mod
  while e > 0
    result = result * a % mod if (e & 1) == 1
    a = a * a % mod
    e >>= 1
  end
  result
end

# @param {String} num
# @return {Integer}
def count_balanced_permutations(num)
  n = num.length
  cnt = Array.new(10, 0)
  total = 0
  num.each_char do |ch|
    d = ch.ord - 48
    cnt[d] += 1
    total += d
  end

  return 0 if (total & 1) == 1
  target_sum = total / 2
  even_cnt = (n + 1) / 2   # positions with index 0,2,...
  odd_cnt = n / 2          # positions with index 1,3,...

  # factorials and inverse factorials up to n
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(n + 1, 1)
  inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }

  # dp[count_of_even_positions][sum_on_even] = accumulated weight
  dp = Array.new(even_cnt + 1) { Array.new(target_sum + 1, 0) }
  dp[0][0] = 1

  cnt.each_with_index do |c, d|
    next if c == 0
    ndp = Array.new(even_cnt + 1) { Array.new(target_sum + 1, 0) }
    (0..even_cnt).each do |used|
      (0..target_sum).each do |sum|
        cur = dp[used][sum]
        next if cur == 0
        max_k = [c, even_cnt - used].min
        (0..max_k).each do |k|
          new_used = used + k
          new_sum = sum + d * k
          next if new_sum > target_sum
          weight = cur * inv_fact[k] % MOD * inv_fact[c - k] % MOD
          ndp[new_used][new_sum] = (ndp[new_used][new_sum] + weight) % MOD
        end
      end
    end
    dp = ndp
  end

  res = dp[even_cnt][target_sum]
  return 0 if res == 0
  res = res * fact[even_cnt] % MOD
  res = res * fact[odd_cnt] % MOD
  res
end
```

## Scala

```scala
object Solution {
  private val MOD: Long = 1000000007L

  def countBalancedPermutations(num: String): Int = {
    val n = num.length
    val cnt = new Array[Int](10)
    var totalSum = 0
    for (ch <- num) {
      val d = ch - '0'
      cnt(d) += 1
      totalSum += d
    }
    if ((totalSum & 1) == 1) return 0

    val target = totalSum / 2
    val oddPos = n / 2               // number of odd indices (1,3,...)
    val evenPos = n - oddPos          // number of even indices (0,2,...)

    // factorials and inverse factorials up to n
    val fact = new Array[Long](n + 1)
    val invFact = new Array[Long](n + 1)
    fact(0) = 1L
    var i = 1
    while (i <= n) {
      fact(i) = fact(i - 1) * i % MOD
      i += 1
    }
    invFact(n) = modPow(fact(n), MOD - 2)
    i = n
    while (i > 0) {
      invFact(i - 1) = invFact(i) * i % MOD
      i -= 1
    }

    // dp[sum][oddCount] = sum of product of inverse factorials for processed digits
    val dp = Array.ofDim[Long](target + 1, oddPos + 1)
    dp(0)(0) = 1L

    var digit = 0
    while (digit <= 9) {
      val c = cnt(digit)
      if (c > 0) {
        val next = Array.ofDim[Long](target + 1, oddPos + 1)
        var sum = 0
        while (sum <= target) {
          var o = 0
          while (o <= oddPos) {
            val cur = dp(sum)(o)
            if (cur != 0L) {
              var j = 0
              while (j <= c) {
                val newSum = sum + digit * j
                if (newSum > target) {
                  // since digit >=0, further j will only increase sum
                  // break out of inner loop
                  j = c + 1
                } else {
                  val newO = o + j
                  if (newO <= oddPos) {
                    var add = cur * invFact(j) % MOD
                    add = add * invFact(c - j) % MOD
                    next(newSum)(newO) = (next(newSum)(newO) + add) % MOD
                  }
                  j += 1
                }
              }
            }
            o += 1
          }
          sum += 1
        }
        // copy next to dp for next iteration
        var s = 0
        while (s <= target) {
          var o2 = 0
          while (o2 <= oddPos) {
            dp(s)(o2) = next(s)(o2)
            o2 += 1
          }
          s += 1
        }
      }
      digit += 1
    }

    var ans = dp(target)(oddPos)
    ans = ans * fact(oddPos) % MOD
    ans = ans * fact(evenPos) % MOD
    (ans % MOD).toInt
  }

  private def modPow(base: Long, exp: Long): Long = {
    var b = base % MOD
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1L) == 1L) res = res * b % MOD
      b = b * b % MOD
      e >>= 1
    }
    res
  }
}
```

## Rust

```rust
use std::cmp::min;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res: i64 = 1;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}

pub struct Solution;

impl Solution {
    pub fn count_balanced_permutations(num: String) -> i32 {
        let n = num.len();
        let mut cnt = [0usize; 10];
        let mut total_sum = 0usize;
        for b in num.bytes() {
            let d = (b - b'0') as usize;
            cnt[d] += 1;
            total_sum += d;
        }
        if total_sum % 2 == 1 {
            return 0;
        }
        let target = total_sum / 2;
        let evens = (n + 1) / 2;
        let odds = n / 2;

        // factorials
        let mut fact = vec![0i64; n + 1];
        fact[0] = 1;
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![0i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        // dp[e][s] = sum of product of inverse factorials for processed digits
        let mut dp = vec![vec![0i64; target + 1]; evens + 1];
        dp[0][0] = 1;

        for d in 0..10 {
            let c = cnt[d];
            if c == 0 {
                continue;
            }
            let mut next = vec![vec![0i64; target + 1]; evens + 1];
            for e in 0..=evens {
                for s in 0..=target {
                    let cur = dp[e][s];
                    if cur == 0 {
                        continue;
                    }
                    let max_k = min(c, evens - e);
                    for k in 0..=max_k {
                        let new_s = s + d * k;
                        if new_s > target {
                            continue;
                        }
                        let add = cur
                            * inv_fact[k] % MOD
                            * inv_fact[c - k] % MOD;
                        let ne = e + k;
                        next[ne][new_s] = (next[ne][new_s] + add) % MOD;
                    }
                }
            }
            dp = next;
        }

        let mut ans = dp[evens][target];
        ans = ans * fact[evens] % MOD;
        ans = ans * fact[odds] % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; modular exponentiation
(define (modpow base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (quotient e 2)
              (if (= (bitwise-and e 1) 1)
                  (modulo (* res b) MOD)
                  res)))))

;; create a rows×cols matrix filled with 0
(define (make-2d rows cols)
  (let ((m (make-vector rows)))
    (for ([i (in-range rows)])
      (vector-set! m i (make-vector cols 0)))
    m))

(define/contract (count-balanced-permutations num)
  (-> string? exact-integer?)
  (let* ((n (string-length num))
         ;; count digits
         (cnt (make-vector 10 0))
         (total-sum
          (let loop ((i 0) (s 0))
            (if (= i n)
                s
                (let* ((ch (string-ref num i))
                       (d (- (char->integer ch) (char->integer #\0))))
                  (vector-set! cnt d (+ (vector-ref cnt d) 1))
                  (loop (+ i 1) (+ s d))))))
         ;; early exit if total sum odd
         )
    (if (odd? total-sum)
        0
        (let* ((half-sum (/ total-sum 2))
               (even-cnt (quotient (+ n 1) 2))   ; positions with index 0,2,...
               (odd-cnt  (quotient n 2))         ; positions with index 1,3,...
               
               ;; factorials
               (fact (make-vector (+ n 1) 0))
               (inv-fact (make-vector (+ n 1) 0)))
          
          ;; compute factorials
          (vector-set! fact 0 1)
          (for ([i (in-range 1 (+ n 1))])
            (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
          
          ;; inverse factorials
          (vector-set! inv-fact n (modpow (vector-ref fact n) (- MOD 2)))
          (for ([i (in-range n 0 -1)])
            (when (> i 0)
              (vector-set! inv-fact (- i 1)
                           (modulo (* (vector-ref inv-fact i) i) MOD))))
          
          ;; DP initialization
          (define dp (make-2d (+ even-cnt 1) (+ half-sum 1)))
          (vector-set! (vector-ref dp 0) 0 1)
          
          ;; process each digit
          (for ([digit (in-range 10)])
            (let ((c (vector-ref cnt digit)))
              (when (> c 0)
                (define newdp (make-2d (+ even-cnt 1) (+ half-sum 1)))
                (for ([used (in-range (+ even-cnt 1))])
                  (let ((row-old (vector-ref dp used)))
                    (for ([s (in-range (+ half-sum 1))])
                      (let ((cur (vector-ref row-old s)))
                        (when (> cur 0)
                          (for ([j (in-range (+ c 1))])
                            (define new-used (+ used j))
                            (when (<= new-used even-cnt)
                              (define new-s (+ s (* digit j)))
                              (when (<= new-s half-sum)
                                (define ways
                                  (modulo (* (vector-ref inv-fact j)
                                             (vector-ref inv-fact (- c j))) MOD))
                                (define prev (vector-ref (vector-ref newdp new-used) new-s))
                                (define add (modulo (* cur ways) MOD))
                                (vector-set! (vector-ref newdp new-used) new-s
                                             (modulo (+ prev add) MOD))))))))))
                (set! dp newdp)))))
          
          ;; final answer
          (let ((res (vector-ref (vector-ref dp even-cnt) half-sum)))
            (define ans (modulo (* res (vector-ref fact even-cnt)) MOD))
            (define ans2 (modulo (* ans (vector-ref fact odd-cnt)) MOD))
            ans2))))))
```

## Erlang

```erlang
-module(solution).
-export([count_balanced_permutations/1]).

-define(MOD, 1000000007).

-spec count_balanced_permutations(Num :: unicode:unicode_binary()) -> integer().
count_balanced_permutations(Num) ->
    Digits = binary_to_list(Num),
    N = length(Digits),
    CntsTuple = count_digits(Digits, {0,0,0,0,0,0,0,0,0,0}),
    TotalSum = total_sum(CntsTuple),
    case TotalSum band 1 of
        1 -> 0;
        _ ->
            Target = TotalSum div 2,
            O = N div 2,                     % number of odd indices (floor)
            Fact = factorials(N),
            InvFact = inv_factorials(Fact, N),
            SufTuple = suffix_counts(CntsTuple),
            {Ans,_} = dfs(0, Target, O, CntsTuple, SufTuple, Fact, InvFact, #{}),
            Ans
    end.

%% Count digit frequencies, returning a tuple of size 10.
count_digits([], Cnts) -> Cnts;
count_digits([C|Rest], Cnts) ->
    D = C - $0,
    Pos = D + 1,
    Old = element(Pos, Cnts),
    NewCnts = setelement(Pos, Cnts, Old + 1),
    count_digits(Rest, NewCnts).

%% Compute total sum of digits.
total_sum(CntTuple) -> total_sum(0, CntTuple, 0).
total_sum(I, Tuple, Acc) when I > 9 -> Acc;
total_sum(I, Tuple, Acc) ->
    C = element(I+1, Tuple),
    total_sum(I+1, Tuple, Acc + I*C).

%% Factorials up to N (inclusive), stored in a tuple where index i => i!.
factorials(N) -> factorials(0, N, 1, []).
factorials(I, N, Cur, Acc) when I > N ->
    list_to_tuple(lists:reverse(Acc));
factorials(I, N, Cur, Acc) ->
    NewAcc = [Cur|Acc],
    factorials(I+1, N, (Cur * (I+1)) rem ?MOD, NewAcc).

%% Inverse factorials using Fermat's little theorem.
inv_factorials(FactTuple, N) ->
    InvN = pow_mod(element(N+1, FactTuple), ?MOD-2),
    inv_factorial_build(N, InvN, []).

inv_factorial_build(-1, _, Acc) -> list_to_tuple(lists:reverse(Acc));
inv_factorial_build(I, CurInv, Acc) ->
    NewAcc = [CurInv|Acc],
    NextInv = (CurInv * (I+1)) rem ?MOD,
    inv_factorial_build(I-1, NextInv, NewAcc).

%% Combination n choose k modulo MOD.
comb(N, K, Fact, InvFact) when K < 0; K > N -> 0;
comb(N, K, Fact, InvFact) ->
    F = element(N+1, Fact),
    FK = element(K+1, InvFact),
    FNK = element(N-K+1, InvFact),
    ((F * FK) rem ?MOD * FNK) rem ?MOD.

%% Suffix sums of counts: suffix[I] = sum_{j=I}^{9} cnt[j].
suffix_counts(Cnts) -> suffix_counts(9, Cnts, 0, []).
suffix_counts(-1, _, _AccSum, AccList) ->
    list_to_tuple(lists:reverse(AccList));
suffix_counts(I, Cnts, AccSum, AccList) ->
    C = element(I+1, Cnts),
    NewSum = AccSum + C,
    suffix_counts(I-1, Cnts, NewSum, [NewSum|AccList]).

%% Fast exponentiation modulo MOD.
pow_mod(_Base, 0) -> 1;
pow_mod(Base, Exp) when Exp band 1 =:= 1 ->
    (Base * pow_mod(Base, Exp - 1)) rem ?MOD;
pow_mod(Base, Exp) ->
    Half = pow_mod(Base, Exp div 2),
    (Half * Half) rem ?MOD.

%% Depth‑first search with memoization.
dfs(I, Sum, OddRem, Cnts, Suf, Fact, InvFact, Memo) when Sum < 0; OddRem < 0 ->
    {0, Memo};
dfs(10, Sum, OddRem, _Cnts, _Suf, _Fact, _InvFact, Memo) ->
    Res = if Sum == 0 andalso OddRem == 0 -> 1; true -> 0 end,
    {Res, Memo};
dfs(I, Sum, OddRem, Cnts, Suf, Fact, InvFact, Memo) ->
    case maps:find({I,Sum,OddRem}, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            CntI = element(I+1, Cnts),
            TotalRemain = element(I+1, Suf),          % sum of counts from I to 9
            EvenRem = TotalRemain - OddRem,
            Res =
                if EvenRem < 0 -> 0;
                   true ->
                       MinJ = max(0, CntI - EvenRem),
                       MaxJ = min(CntI, OddRem),
                       {Val, _} = loop_j(I, Sum, OddRem, CntI, EvenRem,
                                         MinJ, MaxJ, Cnts, Suf, Fact, InvFact, Memo, 0),
                       Val
                end,
            NewMemo = maps:put({I,Sum,OddRem}, Res, Memo),
            {Res, NewMemo}
    end.

%% Iterate over possible j (copies of digit I placed in odd positions).
loop_j(_I, _Sum, _OddRem, _CntI, _EvenRem, J, MaxJ, _Cnts, _Suf, _Fact, _InvFact, Memo, Acc) when J > MaxJ ->
    {Acc rem ?MOD, Memo};
loop_j(I, Sum, OddRem, CntI, EvenRem, J, MaxJ, Cnts, Suf, Fact, InvFact, Memo, Acc) ->
    WaysOdd = comb(OddRem, J, Fact, InvFact),
    WaysEven = comb(EvenRem, CntI - J, Fact, InvFact),
    {SubRes, Memo1} = dfs(I+1, Sum - J*I, OddRem - J, Cnts, Suf, Fact, InvFact, Memo),
    Add = ((WaysOdd * WaysEven) rem ?MOD) * SubRes rem ?MOD,
    NewAcc = (Acc + Add) rem ?MOD,
    loop_j(I, Sum, OddRem, CntI, EvenRem, J+1, MaxJ, Cnts, Suf, Fact, InvFact, Memo1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @modulus 1_000_000_007

  @spec count_balanced_permutations(num :: String.t()) :: integer()
  def count_balanced_permutations(num) do
    n = String.length(num)
    digits = String.graphemes(num) |> Enum.map(&String.to_integer/1)

    total_sum = Enum.sum(digits)
    if rem(total_sum, 2) == 1 do
      0
    else
      target = div(total_sum, 2)
      evens = div(n + 1, 2)
      odds = n - evens

      # frequency of each digit 0..9
      cnt =
        Enum.reduce(digits, List.duplicate(0, 10), fn d, acc ->
          List.update_at(acc, d, &(&1 + 1))
        end)

      # factorials and inverse factorials up to n
      fact = build_fact(n)
      inv_fact = build_inv_fact(fact, n)

      dp = %{{0, 0} => 1}

      dp_final =
        Enum.reduce(0..9, dp, fn digit, cur_dp ->
          c = Enum.at(cnt, digit)
          if c == 0 do
            cur_dp
          else
            Enum.reduce(cur_dp, %{}, fn {{s, k}, val}, ndp ->
              for j <- 0..c do
                ns = s + digit * j
                nk = k + j

                cond do
                  ns > target or nk > evens -> nil
                  true ->
                    add =
                      val
                      |> mul_mod(Enum.at(inv_fact, j))
                      |> mul_mod(Enum.at(inv_fact, c - j))

                    key = {ns, nk}
                    Map.update(ndp, key, add, fn existing -> (existing + add) rem @modulus end)
                end
              end
              ndp
            end)
          end
        end)

      ways = Map.get(dp_final, {target, evens}, 0)
      ways
      |> mul_mod(Enum.at(fact, evens))
      |> mul_mod(Enum.at(fact, odds))
    end
  end

  defp build_fact(n) do
    Enum.reduce(0..n, [1], fn i, acc ->
      prev = List.last(acc)
      [(prev * i) rem @modulus | acc]
    end)
    |> Enum.reverse()
  end

  defp build_inv_fact(fact, n) do
    inv_last = pow_mod(Enum.at(fact, n), @modulus - 2)
    {inv_list, _} =
      Enum.reduce((n - 1)..0, {[inv_last], inv_last}, fn i, {list, next_inv} ->
        cur_inv = (next_inv * (i + 1)) rem @modulus
        {[cur_inv | list], cur_inv}
      end)

    inv_list
  end

  defp pow_mod(_base, 0), do: 1

  defp pow_mod(base, exp) when exp > 0 do
    rec_pow(base, exp, 1)
  end

  defp rec_pow(_base, 0, acc), do: acc

  defp rec_pow(base, exp, acc) do
    if rem(exp, 2) == 1 do
      acc = (acc * base) rem @modulus
    else
      acc = acc
    end

    base = (base * base) rem @modulus
    rec_pow(base, div(exp, 2), acc)
  end

  defp mul_mod(a, b), do: rem(a * b, @modulus)
end
```
