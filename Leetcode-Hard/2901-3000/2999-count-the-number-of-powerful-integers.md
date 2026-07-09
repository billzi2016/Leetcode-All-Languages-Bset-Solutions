# 2999. Count the Number of Powerful Integers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        auto calc = [&](long long x)->long long{
            if (x <= 0) return 0;
            string X = to_string(x);
            int n = X.size();
            int m = s.size();
            if (n < m) return 0;
            // precompute powers of (limit+1)
            vector<long long> pw(n - m + 2, 1);
            for (int i = 1; i < (int)pw.size(); ++i) pw[i] = pw[i-1] * (limit + 1LL);
            
            long long total = 0;
            // iterate over possible prefix lengths k
            for (int k = 0; k <= n - m; ++k) {
                if (k + m < n) {
                    // all numbers with this prefix length are automatically <= x
                    if (k == 0) {
                        total += 1; // only suffix s
                    } else {
                        // first digit cannot be zero, others any 0..limit
                        total += (long long)limit * pw[k-1];
                    }
                } else { // k + m == n
                    // need to respect the upper bound X
                    long long cntLess = 0;
                    bool prefixPossible = true; // whether we can match the prefix exactly so far
                    for (int i = 0; i < k && prefixPossible; ++i) {
                        int cur = X[i] - '0';
                        int startDigit = (i == 0 ? 1 : 0);
                        int maxAllowed = min(cur - 1, limit);
                        if (maxAllowed >= startDigit) {
                            cntLess += (long long)(maxAllowed - startDigit + 1) * pw[k - i - 1];
                        }
                        if (cur > limit) {
                            prefixPossible = false; // cannot place cur digit, equality impossible
                            break;
                        }
                    }
                    total += cntLess;
                    // check equality case
                    bool equalPrefix = true;
                    for (int i = 0; i < k && equalPrefix; ++i) {
                        if ((X[i] - '0') > limit) equalPrefix = false;
                    }
                    if (equalPrefix) {
                        // compare suffix s with the corresponding part of X
                        string suffixX = X.substr(k); // length m
                        if (s <= suffixX) total += 1;
                    }
                }
            }
            return total;
        };
        
        long long ans = calc(finish) - calc(start - 1);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private String suffix;
    private int limit;
    private long[] pow; // (limit+1)^i

    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        this.suffix = s;
        this.limit = limit;
        precomputePowers(20);
        return count(finish) - count(start - 1);
    }

    private void precomputePowers(int maxExp) {
        pow = new long[maxExp + 1];
        pow[0] = 1L;
        long base = (long) limit + 1;
        for (int i = 1; i <= maxExp; ++i) {
            pow[i] = pow[i - 1] * base;
        }
    }

    private long count(long x) {
        if (x <= 0) return 0L;
        String xs = Long.toString(x);
        int n = xs.length();
        int lenS = suffix.length();

        long ans = 0L;

        // lengths strictly less than n
        for (int L = lenS; L < n; ++L) {
            int p = L - lenS;
            if (p == 0) {
                ans += 1L; // the number equals suffix itself
            } else {
                ans += (long) limit * pow[p - 1];
            }
        }

        // length equal to n
        if (n >= lenS) {
            int p = n - lenS;
            if (p == 0) {
                // only the suffix, compare directly
                if (suffix.compareTo(xs) <= 0) ans += 1L;
            } else {
                boolean broken = false;
                for (int i = 0; i < p; ++i) {
                    int xDigit = xs.charAt(i) - '0';
                    int startDigit = (i == 0) ? 1 : 0;

                    int maxLess = Math.min(limit, xDigit - 1);
                    if (maxLess >= startDigit) {
                        long ways = pow[p - i - 1];
                        ans += (long) (maxLess - startDigit + 1) * ways;
                    }

                    if (xDigit > limit) {
                        broken = true;
                        break;
                    }
                    // else continue with tight condition
                }
                if (!broken) {
                    String suffixX = xs.substring(p);
                    if (suffix.compareTo(suffixX) <= 0) ans += 1L;
                }
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        L = len(s)

        def count_upto(x):
            if x <= 0:
                return 0
            xs = str(x)
            n = len(xs)
            if n < L:
                return 0

            total = 0
            # lengths shorter than n
            for length in range(L, n):
                k = length - L
                if k == 0:
                    total += 1  # only s itself
                else:
                    total += limit * ((limit + 1) ** (k - 1))

            # length equal to n
            k = n - L

            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos, tight):
                if pos == k:  # prefix done, check suffix
                    if tight:
                        return 1 if s <= xs[k:] else 0
                    else:
                        return 1
                low = 1 if pos == 0 else 0
                hi = int(xs[pos]) if tight else limit
                if hi > limit:
                    hi = limit
                res = 0
                for d in range(low, hi + 1):
                    new_tight = tight and (d == int(xs[pos]))
                    res += dfs(pos + 1, new_tight)
                return res

            total += dfs(0, True)
            return total

        return count_upto(finish) - count_upto(start - 1)
```

## Python3

```python
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        L = len(s)
        # precompute powers of (limit+1)
        max_len = 20
        pow_lim = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow_lim[i] = pow_lim[i - 1] * (limit + 1)

        def count_upto(x: int) -> int:
            if x <= 0:
                return 0
            xs = str(x)
            n = len(xs)
            if n < L:
                return 0

            total = 0
            # lengths shorter than n
            for length in range(L, n):
                p = length - L
                if p == 0:
                    total += 1  # just s itself
                else:
                    total += limit * pow_lim[p - 1]

            # length equal to n
            p = n - L
            if p == 0:
                if int(s) <= x:
                    total += 1
                return total

            pref = xs[:p]
            suff = xs[p:]

            for i, ch in enumerate(pref):
                cur = ord(ch) - 48
                low = 1 if i == 0 else 0
                max_allowed_less = min(cur - 1, limit)
                if max_allowed_less >= low:
                    cnt = max_allowed_less - low + 1
                    total += cnt * pow_lim[p - i - 1]
                # cannot continue equality
                if cur > limit or (i == 0 and cur == 0):
                    break
            else:
                # prefix exactly equals pref and all digits within limit
                if int(s) <= int(suff):
                    total += 1

            return total

        return count_upto(finish) - count_upto(start - 1)
```

## C

```c
#include <stdio.h>
#include <string.h>

static const char *suf;
static int sufLen;
static int LIM;

static char X[32];
static int N, PRELEN;
static long long memo[20][2]; // memo[pos][0] for tight==0

static long long dfs(int pos, int tight) {
    if (pos == N) return 1LL;
    if (!tight && memo[pos][0] != -1) return memo[pos][0];

    int bound = tight ? (X[pos] - '0') : LIM;
    if (bound > LIM) bound = LIM; // enforce digit limit

    long long res = 0;
    if (pos >= PRELEN) { // suffix part, fixed digit
        int d = suf[pos - PRELEN] - '0';
        if (d > bound) {
            res = 0;
        } else {
            int nextTight = tight && (d == (X[pos] - '0'));
            res = dfs(pos + 1, nextTight);
        }
    } else { // prefix part, free digits
        int startDigit = (pos == 0) ? 1 : 0; // no leading zero for whole number
        for (int d = startDigit; d <= bound; ++d) {
            int nextTight = tight && (d == (X[pos] - '0'));
            res += dfs(pos + 1, nextTight);
        }
    }

    if (!tight) memo[pos][0] = res;
    return res;
}

static long long pow_ll(long long base, int exp) {
    long long r = 1;
    while (exp--) r *= base;
    return r;
}

static long long countUpTo(long long Xval) {
    if (Xval <= 0) return 0LL;

    sprintf(X, "%lld", Xval);
    N = strlen(X);

    if (sufLen > N) return 0LL;

    long long total = 0;

    // lengths smaller than N
    for (int L = sufLen; L < N; ++L) {
        int pre = L - sufLen;
        if (pre == 0) {
            total += 1LL;
        } else {
            total += LIM * pow_ll(LIM + 1, pre - 1);
        }
    }

    // length equal to N
    PRELEN = N - sufLen;
    if (PRELEN == 0) {
        if (strcmp(suf, X) <= 0) total += 1LL;
    } else {
        memset(memo, -1, sizeof(memo));
        total += dfs(0, 1);
    }

    return total;
}

long long numberOfPowerfulInt(long long start, long long finish, int limit, char* s) {
    suf = s;
    sufLen = strlen(s);
    LIM = limit;

    long long ans = countUpTo(finish) - countUpTo(start - 1);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long NumberOfPowerfulInt(long start, long finish, int limit, string s) {
        // Precompute powers of (limit+1)
        int maxLen = Math.Max(finish.ToString().Length, s.Length) + 2;
        long[] pow = new long[maxLen];
        pow[0] = 1;
        long baseVal = limit + 1L;
        for (int i = 1; i < maxLen; i++) {
            pow[i] = pow[i - 1] * baseVal;
        }

        long CountUpTo(long x) {
            if (x <= 0) return 0;
            string xs = x.ToString();
            int lenX = xs.Length;
            int lenS = s.Length;
            long total = 0;

            // lengths shorter than lenX
            for (int L = lenS; L < lenX; L++) {
                int p = L - lenS;
                if (p == 0) {
                    total += 1; // just the suffix itself
                } else {
                    // first digit cannot be zero, choices from 1..limit
                    total += limit * pow[p - 1];
                }
            }

            // length equal to lenX
            if (lenX >= lenS) {
                int p = lenX - lenS;
                if (p == 0) {
                    // only suffix, compare directly
                    if (String.Compare(s, xs, StringComparison.Ordinal) <= 0) total += 1;
                } else {
                    long add = 0;
                    bool equalSoFar = true;
                    for (int i = 0; i < p; i++) {
                        int boundDigit = xs[i] - '0';
                        int low = (i == 0) ? 1 : 0;

                        int maxLess = Math.Min(limit, boundDigit - 1);
                        if (maxLess >= low) {
                            long cntChoices = maxLess - low + 1L;
                            add += cntChoices * pow[p - i - 1];
                        }

                        if (boundDigit > limit) {
                            equalSoFar = false;
                            break;
                        }
                    }
                    if (equalSoFar) {
                        string suffixX = xs.Substring(p);
                        if (String.Compare(s, suffixX, StringComparison.Ordinal) <= 0) add += 1;
                    }
                    total += add;
                }
            }

            return total;
        }

        long ans = CountUpTo(finish) - CountUpTo(start - 1);
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} start
 * @param {number} finish
 * @param {number} limit
 * @param {string} s
 * @return {number}
 */
var numberOfPowerfulInt = function(start, finish, limit, s) {
    const base = limit + 1;
    // count powerful integers in [1..x]
    const countUpTo = (x) => {
        if (x <= 0) return 0;
        const xs = String(x);
        const n = xs.length;
        const lenS = s.length;
        if (n < lenS) return 0;

        // precompute powers of (limit+1)
        const maxPreLen = n - lenS;
        const pow = new Array(maxPreLen + 1);
        pow[0] = 1;
        for (let i = 1; i <= maxPreLen; ++i) {
            pow[i] = pow[i - 1] * base;
        }

        let total = 0;

        // lengths strictly smaller than n
        for (let totalLen = lenS; totalLen < n; ++totalLen) {
            const preLen = totalLen - lenS;
            if (preLen === 0) {
                total += 1; // just s itself
            } else {
                total += limit * pow[preLen - 1];
            }
        }

        // length equal to n
        const preLen = n - lenS;
        if (preLen === 0) {
            // only s, check if it fits in xs
            if (s <= xs) total += 1;
        } else {
            const P = xs.slice(0, preLen);
            const Q = xs.slice(preLen); // suffix part of x

            // count prefixes A < P respecting digit limits
            let cntLess = 0;
            let prefixValid = true;
            for (let i = 0; i < preLen; ++i) {
                const b = Number(P[i]);
                const startDigit = i === 0 ? 1 : 0;
                const maxD = Math.min(limit, b - 1);
                if (maxD >= startDigit) {
                    cntLess += (maxD - startDigit + 1) * pow[preLen - i - 1];
                }
                if (b > limit) {
                    prefixValid = false;
                    break;
                }
            }
            total += cntLess;

            // equality case: prefix equals P and suffix s <= Q
            if (prefixValid && s <= Q) {
                total += 1;
            }
        }

        return total;
    };

    return countUpTo(finish) - countUpTo(start - 1);
};
```

## Typescript

```typescript
function numberOfPowerfulInt(start: number, finish: number, limit: number, s: string): number {
    const suffixVal = Number(s);
    const lenS = s.length;
    const pow10Big = 10n ** BigInt(lenS);

    // count numbers <= x that are powerful
    function countUpTo(x: number): number {
        if (x < suffixVal) return 0;
        const xBig = BigInt(x);
        const suffixBig = BigInt(suffixVal);
        if (pow10Big > xBig - suffixBig + 1n) {
            // maxPrefix would be negative
            return 0;
        }
        const maxPrefixBig = (xBig - suffixBig) / pow10Big; // floor division
        const maxPrefix = Number(maxPrefixBig); // safe, <= 1e15

        // digit DP: count numbers in [0, maxPrefix] where each digit <= limit
        const digits = Array.from(String(maxPrefix), ch => Number(ch));
        const n = digits.length;
        const memo: number[][] = Array.from({ length: n + 1 }, () => Array(2).fill(-1));

        function dfs(pos: number, tight: number): number {
            if (pos === n) return 1; // valid number formed
            const mem = memo[pos][tight];
            if (mem !== -1) return mem;
            let res = 0;
            const maxDigit = tight ? digits[pos] : limit;
            for (let d = 0; d <= maxDigit; ++d) {
                if (d > limit) break; // redundant due to maxDigit bound
                const nextTight = tight && d === digits[pos] ? 1 : 0;
                res += dfs(pos + 1, nextTight);
            }
            memo[pos][tight] = res;
            return res;
        }

        return dfs(0, 1);
    }

    const totalFinish = countUpTo(finish);
    const totalStartMinus = start > 1 ? countUpTo(start - 1) : (start === 1 ? 0 : countUpTo(start - 1));
    return totalFinish - totalStartMinus;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $start
     * @param Integer $finish
     * @param Integer $limit
     * @param String $s
     * @return Integer
     */
    function numberOfPowerfulInt($start, $finish, $limit, $s) {
        return $this->calc($finish, $limit, $s) - $this->calc($start - 1, $limit, $s);
    }

    private function calc($x, $limit, $s) {
        if ($x <= 0) return 0;
        $xs = strval($x);
        $n = strlen($xs);
        $lenS = strlen($s);
        if ($lenS > $n) return 0;

        $ans = 0;
        // lengths shorter than n
        for ($L = $lenS; $L < $n; $L++) {
            $k = $L - $lenS; // prefix length
            if ($k == 0) {
                $ans += 1; // just s itself
            } else {
                $ans += $limit * $this->powInt($limit + 1, $k - 1);
            }
        }

        // length equal to n
        $k = $n - $lenS; // prefix length for this length
        for ($i = 0; $i < $n; $i++) {
            if ($i < $k) { // prefix part
                $low = ($i == 0) ? 1 : 0;
                $high = $limit;
                $cur = intval($xs[$i]);

                $maxLess = min($high, $cur - 1);
                if ($maxLess >= $low) {
                    $cntSmallerDigits = $maxLess - $low + 1;
                    $remPrefix = $k - $i - 1;
                    $ans += $cntSmallerDigits * $this->powInt($limit + 1, $remPrefix);
                }

                if ($cur < $low || $cur > $high) {
                    return $ans; // cannot match further
                }
            } else { // suffix part (must equal s)
                $sIdx = $i - $k;
                $need = intval($s[$sIdx]);
                $cur = intval($xs[$i]);

                if ($need < $cur) {
                    $ans += 1; // this exact prefix with smaller suffix digit makes number < x
                    return $ans;
                } elseif ($need > $cur) {
                    return $ans; // exceeds x, stop
                }
            }
        }

        // all digits matched exactly
        $ans += 1;
        return $ans;
    }

    private function powInt($base, $exp) {
        $result = 1;
        while ($exp > 0) {
            if ($exp & 1) {
                $result *= $base;
            }
            $base *= $base;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPowerfulInt(_ start: Int, _ finish: Int, _ limit: Int, _ s: String) -> Int {
        let limitLL = Int64(limit)
        let sStr = s
        let lenS = sStr.count
        
        // Precompute powers of (limit+1)
        let maxDigits = String(finish).count + 2
        var powVals = [Int64](repeating: 0, count: maxDigits)
        powVals[0] = 1
        for i in 1..<maxDigits {
            powVals[i] = powVals[i - 1] * Int64(limit + 1)
        }
        
        func countUpTo(_ x: Int64) -> Int64 {
            if x <= 0 { return 0 }
            let xs = String(x)
            let lenX = xs.count
            if lenX < lenS { return 0 }
            
            var ans: Int64 = 0
            
            // Count numbers with total length less than lenX
            if lenS < lenX {
                for totalLen in lenS...(lenX - 1) {
                    let pre = totalLen - lenS
                    if pre == 0 {
                        ans += 1   // just s
                    } else {
                        // first digit cannot be zero, choices from 1..limit => limit options
                        let add = limitLL * powVals[pre - 1]
                        ans += add
                    }
                }
            }
            
            // Same length case
            let preLen = lenX - lenS
            if preLen == 0 {
                if sStr <= xs { ans += 1 }
                return ans
            }
            
            // Convert x digits to array of Int
            let xDigits = Array(xs.utf8).map { Int($0 - 48) }
            var broken = false
            
            for i in 0..<preLen {
                let cur = xDigits[i]
                let lowBound = (i == 0) ? 1 : 0
                if cur < lowBound {
                    broken = true
                    break
                }
                // Count digits less than cur that are allowed
                let maxLess = min(limit, cur - 1)
                if maxLess >= lowBound {
                    let cntLess = maxLess - lowBound + 1
                    let remaining = preLen - i - 1
                    ans += Int64(cntLess) * powVals[remaining]
                }
                // If current digit exceeds limit, cannot continue exact match
                if cur > limit {
                    broken = true
                    break
                }
                // otherwise continue with tight condition
            }
            
            if !broken {
                // Prefix matches exactly, compare suffix
                let startIdx = xs.index(xs.startIndex, offsetBy: preLen)
                let suffixXStr = String(xs[startIdx...])
                if sStr <= suffixXStr {
                    ans += 1
                }
            }
            
            return ans
        }
        
        let finishLL = Int64(finish)
        let startMinusOneLL = Int64(start) - 1
        let result = countUpTo(finishLL) - countUpTo(startMinusOneLL)
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long {
        val suffix = s
        fun count(x: Long): Long {
            if (x <= 0L) return 0L
            val str = x.toString()
            val n = str.length
            val digits = IntArray(n) { str[it] - '0' }
            val lenS = suffix.length
            if (lenS > n) return 0L

            val memo = Array(n + 1) { Array(2) { LongArray(2) { -1L } } }

            fun dfs(pos: Int, tight: Int, started: Int): Long {
                if (pos == n) {
                    return if (started == 1) 1L else 0L
                }
                val cached = memo[pos][tight][started]
                if (cached != -1L) return cached

                val rem = n - pos
                var res = 0L
                when {
                    rem < lenS -> {
                        // not enough digits left to place the suffix
                        res = 0L
                    }
                    rem > lenS -> {
                        val maxBound = if (tight == 1) digits[pos] else 9
                        val upper = kotlin.math.min(limit, maxBound)
                        for (d in 0..upper) {
                            val newStarted = if (started == 1 || d != 0) 1 else 0
                            val newTight = if (tight == 1 && d == digits[pos]) 1 else 0
                            res += dfs(pos + 1, newTight, newStarted)
                        }
                    }
                    else -> { // rem == lenS, must match suffix exactly
                        var ok = true
                        var newTight = tight
                        for (k in 0 until lenS) {
                            val idx = pos + k
                            val need = suffix[k] - '0'
                            if (need > limit) { ok = false; break }
                            if (newTight == 1) {
                                if (need > digits[idx]) { ok = false; break }
                                newTight = if (need == digits[idx]) 1 else 0
                            }
                        }
                        if (ok) {
                            // after placing suffix, number is complete; started becomes true because suffix has no leading zero
                            res += dfs(n, newTight, 1)
                        }
                    }
                }

                memo[pos][tight][started] = res
                return res
            }

            return dfs(0, 1, 0)
        }

        return count(finish) - count(start - 1)
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPowerfulInt(int start, int finish, int limit, String s) {
    // Helper to compute a^b
    int powInt(int a, int b) {
      int res = 1;
      while (b > 0) {
        if ((b & 1) == 1) res *= a;
        a *= a;
        b >>= 1;
      }
      return res;
    }

    // Count powerful integers in [1..x]
    int countUpTo(int x) {
      if (x <= 0) return 0;
      String xs = x.toString();
      List<int> xDigits = xs.codeUnits.map((c) => c - 48).toList();
      int n = xDigits.length;
      int m = s.length;
      List<int> sDigits = s.codeUnits.map((c) => c - 48).toList();

      // If the total length is less than suffix length, impossible
      if (n < m) return 0;

      int total = 0;

      // Lengths smaller than n
      for (int L = m; L < n; ++L) {
        int pLen = L - m;
        if (pLen == 0) {
          // The number is exactly s
          total += 1;
        } else {
          // First digit cannot be zero, each digit <= limit
          total += limit * powInt(limit + 1, pLen - 1);
        }
      }

      // Length equal to n
      int p = n - m; // prefix length
      List<List<int?>> memo = List.generate(n + 1, (_) => List.filled(2, null));

      int dfs(int pos, bool tight) {
        if (pos == n) return 1;
        int ti = tight ? 1 : 0;
        var cached = memo[pos][ti];
        if (cached != null) return cached;

        int res = 0;
        if (pos < p) {
          int low = (pos == 0) ? 1 : 0;
          int up = limit;
          if (tight) {
            up = xDigits[pos] < limit ? xDigits[pos] : limit;
          }
          for (int d = low; d <= up; ++d) {
            bool nextTight = tight && (d == xDigits[pos]);
            res += dfs(pos + 1, nextTight);
          }
        } else {
          int fd = sDigits[pos - p];
          if (fd > limit) {
            res = 0;
          } else if (tight) {
            int xi = xDigits[pos];
            if (fd > xi) {
              res = 0;
            } else {
              bool nextTight = fd == xi;
              res = dfs(pos + 1, nextTight);
            }
          } else {
            res = dfs(pos + 1, false);
          }
        }

        memo[pos][ti] = res;
        return res;
      }

      total += dfs(0, true);
      return total;
    }

    int ans = countUpTo(finish) - countUpTo(start - 1);
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
)

func numberOfPowerfulInt(start int64, finish int64, limit int, s string) int64 {
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	count := func(x int64) int64 {
		if x <= 0 {
			return 0
		}
		xs := strconv.FormatInt(x, 10)
		n := len(xs)
		lenS := len(s)

		// precompute powers of (limit+1)
		maxP := n
		pow := make([]int64, maxP+1)
		pow[0] = 1
		base := int64(limit + 1)
		for i := 1; i <= maxP; i++ {
			pow[i] = pow[i-1] * base
		}

		var total int64

		// lengths smaller than n
		for L := lenS; L < n; L++ {
			p := L - lenS
			if p == 0 {
				total += 1 // the number is exactly s
			} else {
				if limit == 0 {
					continue
				}
				cnt := int64(limit) * pow[p-1]
				total += cnt
			}
		}

		// length equal to n
		if n < lenS {
			return total
		}
		prefixLen := n - lenS
		if prefixLen == 0 {
			if s <= xs {
				total++
			}
			return total
		}

		// process prefix with tight constraint
		for i := 0; i < prefixLen; i++ {
			xi := int(xs[i] - '0')
			low := 0
			if i == 0 {
				low = 1
			}
			maxDigit := limit

			upperLess := min(maxDigit, xi-1)
			if upperLess >= low {
				cntDigits := upperLess - low + 1
				remaining := prefixLen - i - 1
				total += int64(cntDigits) * pow[remaining]
			}

			if xi > maxDigit {
				return total
			}
			// else continue with equality path
		}

		// prefix equals X's prefix, compare suffix
		if s <= xs[prefixLen:] {
			total++
		}
		return total
	}

	return count(finish) - count(start-1)
}
```

## Ruby

```ruby
def number_of_powerful_int(start, finish, limit, s)
  def count_up_to(x, limit, s)
    return 0 if x <= 0
    xs = x.to_s
    len_x = xs.length
    len_s = s.length
    return 0 if len_x < len_s

    max_pre = len_x - len_s
    pow = Array.new(max_pre + 1, 1)
    (1..max_pre).each { |i| pow[i] = pow[i - 1] * (limit + 1) }

    total = 0

    # lengths strictly less than len_x
    (len_s...len_x).each do |l|
      pre = l - len_s
      if pre == 0
        total += 1
      else
        total += limit * pow[pre - 1]
      end
    end

    # length equal to len_x
    pre = max_pre
    if pre == 0
      total += 1 if s <= xs
    else
      equal_possible = true
      (0...pre).each do |i|
        xi = xs.getbyte(i) - 48
        low = (i == 0 ? 1 : 0)
        max_allowed = limit

        upper = [xi - 1, max_allowed].min
        if upper >= low
          cnt = upper - low + 1
          total += cnt * pow[pre - i - 1]
        end

        if xi < low || xi > max_allowed
          equal_possible = false
          break
        end
      end
      if equal_possible
        suffix_x = xs[-len_s, len_s]
        total += 1 if s <= suffix_x
      end
    end

    total
  end

  count_up_to(finish, limit, s) - count_up_to(start - 1, limit, s)
end
```

## Scala

```scala
object Solution {
    def numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long = {
        val sLong = s.toLong
        val limitPlusOne = limit + 1

        // precompute powers of (limit+1) up to needed size
        val pow = new Array[Long](20)
        pow(0) = 1L
        for (i <- 1 until pow.length) {
            pow(i) = pow(i - 1) * limitPlusOne
        }

        def countUpTo(x: Long): Long = {
            if (x <= 0) return 0L
            val str = x.toString
            val n = str.length
            val digits = new Array[Int](n)
            var i = 0
            while (i < n) {
                digits(i) = str.charAt(i) - '0'
                i += 1
            }
            val lenS = s.length
            if (lenS > n) return 0L

            var total: Long = 0L

            // lengths strictly less than n
            var L = lenS
            while (L < n) {
                val p = L - lenS
                if (p == 0) {
                    total += 1L
                } else {
                    // first digit cannot be zero, choices = limit (1..limit)
                    total += limit.toLong * pow(p - 1)
                }
                L += 1
            }

            // length equal to n
            val p = n - lenS
            if (p == 0) {
                if (sLong <= x) total += 1L
            } else {
                var eq: Long = 1L
                var less: Long = 0L
                var pos = 0
                while (pos < p) {
                    val maxD = digits(pos)
                    var newEq: Long = 0L
                    var newLess: Long = 0L
                    val startDigit = if (pos == 0) 1 else 0
                    var d = startDigit
                    while (d <= limit) {
                        if (eq != 0) {
                            if (d == maxD) newEq += eq
                            else if (d < maxD) newLess += eq
                        }
                        d += 1
                    }
                    val choices = limit - startDigit + 1
                    newLess += less * choices
                    eq = newEq
                    less = newLess
                    pos += 1
                }

                var totalPrefixes: Long = less
                if (eq != 0) {
                    var suffixVal: Long = 0L
                    var idx = p
                    while (idx < n) {
                        suffixVal = suffixVal * 10 + digits(idx)
                        idx += 1
                    }
                    if (sLong <= suffixVal) totalPrefixes += eq
                }
                total += totalPrefixes
            }

            total
        }

        countUpTo(finish) - countUpTo(start - 1)
    }
}
```

## Rust

```rust
use std::cmp::{min};

impl Solution {
    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        fn pow(mut base: i64, mut exp: usize) -> i64 {
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res *= base;
                }
                base *= base;
                exp >>= 1;
            }
            res
        }

        fn count_upto(x: i64, limit: i32, s: &str) -> i64 {
            if x <= 0 {
                return 0;
            }
            let xs = x.to_string();
            let n = xs.len();
            let m = s.len();
            if n < m {
                return 0;
            }
            let limit_i64 = limit as i64;
            let mut total: i64 = 0;

            // lengths shorter than n
            for len in m..n {
                let pref_len = len - m;
                if pref_len == 0 {
                    total += 1; // just s itself
                } else {
                    // first digit cannot be zero
                    total += limit_i64 * pow(limit_i64 + 1, pref_len - 1);
                }
            }

            // length equal to n
            let prefix_len = n - m;
            if prefix_len == 0 {
                // only s
                if s <= xs.as_str() {
                    total += 1;
                }
                return total;
            }

            let xb: Vec<u8> = xs.bytes().collect();

            let mut tight = true;
            for i in 0..prefix_len {
                if !tight {
                    break;
                }
                let low = if i == 0 { 1 } else { 0 };
                let xi = (xb[i] - b'0') as i32;
                let max_allowed = min(limit, xi);
                // digits less than xi while still tight
                for d in low..=max_allowed {
                    if d < xi {
                        let rem = prefix_len - i - 1;
                        total += pow(limit_i64 + 1, rem);
                    }
                }
                // check if we can keep tight
                if xi < low || xi > limit {
                    tight = false;
                    break;
                }
                // otherwise continue with tight true
            }

            if tight {
                // prefix matches x's prefix, need to compare suffixes
                let suffix_x = &xs[n - m..];
                if s <= suffix_x {
                    total += 1;
                }
            }

            total
        }

        let cnt_finish = count_upto(finish, limit, &s);
        let cnt_start_minus_one = count_upto(start - 1, limit, &s);
        cnt_finish - cnt_start_minus_one
    }
}
```

## Racket

```racket
(define/contract (number-of-powerful-int start finish limit s)
  (-> exact-integer? exact-integer? exact-integer? string? exact-integer?)

  (define (pow base exp)
    (let loop ((b base) (e exp) (res 1))
      (if (= e 0)
          res
          (loop (* b b) (quotient e 2) (if (odd? e) (* res b) res)))))

  (define (int->digits n)
    (let loop ((x n) (acc '()))
      (if (= x 0)
          (if (null? acc) '(0) (reverse acc))
          (loop (quotient x 10) (cons (remainder x 10) acc)))))

  (define s-int (string->number s))
  (define m (string-length s))

  (define (count-up-to x)
    (if (<= x 0)
        0
        (let* ((digits (int->digits x))
               (n (length digits)))
          (if (< n m)
              0
              (let ((pow10-m (pow 10 m))
                    (limit-plus-1 (+ limit 1)))
                (define total-less-len
                  (let loop ((len m) (acc 0))
                    (if (> len (- n 1))
                        acc
                        (let ((p (- len m)))
                          (if (= p 0)
                              (loop (+ len 1) (+ acc 1)) ; only s itself
                              (loop (+ len 1)
                                    (+ acc (* limit (pow limit-plus-1 (- p 1))))))))))
                ;; handle length == n
                (let* ((p (- n m))
                       (suffix-x (remainder x pow10-m)))
                  (if (= p 0)
                      (+ total-less-len (if (<= s-int x) 1 0))
                      (let loop ((pos 0) (tight 1) (loose 0))
                        (if (= pos p)
                            (let ((cnt (+ loose
                                          (if (> tight 0)
                                              (if (<= s-int suffix-x) 1 0)
                                              0))))
                              (+ total-less-len cnt))
                            (let* ((digit-x (list-ref digits pos))
                                   (low (if (= pos 0) 1 0))
                                   (max-digit limit)
                                   ;; transitions from tight state
                                   (ub-tight (min max-digit digit-x))
                                   (cnt-eq (if (and (> ub-tight low) (= digit-x ub-tight)) 1 0))
                                   (cnt-less (if (> ub-tight low) (- (+ ub-tight -1) low + 1) 0))
                                   ;; careful: compute number of choices less than digit_x within allowed range
                                   (less-choices (max 0 (- (min max-digit digit-x) low)))
                                   (eq-choice (if (and (>= digit-x low) (<= digit-x max-digit)) 1 0))
                                   (new-tight (* tight eq-choice))
                                   (new-loose (+ (* loose limit-plus-1)
                                                 (* tight less-choices))))
                              (loop (+ pos 1) new-tight new-loose)))))))))))

  (- (count-up-to finish) (count-up-to (- start 1))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_powerful_int/4]).

-spec number_of_powerful_int(integer(), integer(), integer(), unicode:unicode_binary()) -> integer().
number_of_powerful_int(Start, Finish, Limit, S) ->
    SChars = unicode:characters_to_list(S),
    CountFinish = count_upto(Finish, Limit, SChars),
    CountStartMinus1 =
        case Start of
            1 -> 0;
            _ -> count_upto(Start - 1, Limit, SChars)
        end,
    CountFinish - CountStartMinus1.

%% count numbers <= X that are powerful
count_upto(X, Limit, SChars) when X >= 0 ->
    SInt = list_to_integer(SChars),
    if X < SInt -> 0;
       true -> do_count(X, Limit, SChars)
    end.

do_count(X, Limit, SChars) ->
    XStr = integer_to_list(X),
    N = length(XStr),
    M = length(SChars),
    if N < M -> 0;
       true ->
           Base = Limit + 1,
           PowList = build_powers(Base, N), % PowList !! K = Base^K
           LessLengths = count_less_lengths(N, M, Limit, PowList),
           SameLength = count_same_length(XStr, N, M, Limit, SChars, PowList),
           LessLengths + SameLength
    end.

%% sum for total lengths strictly less than N
count_less_lengths(N, M, Limit, PowList) ->
    lists:foldl(fun(Len, Acc) ->
        PreLen = Len - M,
        Add =
            case PreLen of
                0 -> 1;
                _ -> Limit * pow_at(PowList, PreLen - 1)
            end,
        Acc + Add
    end, 0, lists:seq(M, N - 1)).

%% count for length equal to N
count_same_length(_XStr, N, M, _Limit, _SChars, _PowList) when N < M ->
    0;
count_same_length(XStr, N, M, Limit, SChars, PowList) ->
    case N =:= M of
        true ->
            %% only suffix part exists
            case le_string(SChars, XStr) of
                true -> 1;
                false -> 0
            end;
        false ->
            PreLen = N - M,
            PrefixChars = lists:sublist(XStr, PreLen),
            SuffixXChars = lists:nthtail(PreLen, XStr),
            PrefixDigits = [C - $0 || C <- PrefixChars],
            PrefixLess = count_prefix_less(PrefixDigits, Limit, PowList, 0),
            EqualPossible = all_digits_le_limit(PrefixDigits, Limit),
            AddEqual =
                case EqualPossible andalso le_string(SChars, SuffixXChars) of
                    true -> 1;
                    false -> 0
                end,
            PrefixLess + AddEqual
    end.

%% count prefixes strictly less than given prefix
count_prefix_less([], _Limit, _PowList, _Pos) ->
    0;
count_prefix_less([Cur|Rest], Limit, PowList, Pos) ->
    Remaining = length(Rest),
    MinDigit = if Pos == 0 -> 1; true -> 0 end,
    MaxLess = min(Cur - 1, Limit),
    Add =
        case MaxLess >= MinDigit of
            true -> (MaxLess - MinDigit + 1) * pow_at(PowList, Remaining);
            false -> 0
        end,
    Continue =
        if Cur =< Limit ->
                count_prefix_less(Rest, Limit, PowList, Pos + 1);
           true -> 0
        end,
    Add + Continue.

all_digits_le_limit(Digits, Limit) ->
    lists:all(fun(D) -> D =< Limit end, Digits).

%% lexical numeric comparison of equal‑length strings (char codes)
le_string([], []) -> true;
le_string([A|As], [B|Bs]) ->
    if A < B -> true;
       A > B -> false;
       true -> le_string(As, Bs)
    end.

%% power list utilities
build_powers(Base, Max) ->
    build_powers_iter(Base, Max, 0, 1, []).

build_powers_iter(_Base, Max, I, _Curr, Acc) when I > Max ->
    lists:reverse(Acc);
build_powers_iter(Base, Max, I, Curr, Acc) ->
    NewAcc = [Curr | Acc],
    build_powers_iter(Base, Max, I + 1, Curr * Base, NewAcc).

pow_at(PowList, K) ->
    lists:nth(K + 1, PowList).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_powerful_int(start :: integer, finish :: integer, limit :: integer, s :: String.t) :: integer
  def number_of_powerful_int(start, finish, limit, s) do
    s_int = String.to_integer(s)
    len_s = String.length(s)

    count_up_to = fn x ->
      if x < s_int do
        0
      else
        n = Integer.digits(x) |> length()
        pow10_len_s = ipow(10, len_s)

        # numbers with length less than n
        total_less =
          cond do
            len_s > n - 1 -> 0
            true ->
              base_total = if len_s < n, do: 1, else: 0   # the number equal to s when its length is smaller than n
              Enum.reduce((len_s + 1)..(n - 1), base_total, fn cur_len, acc ->
                p = cur_len - len_s
                acc + limit * ipow(limit + 1, p - 1)
              end)
          end

        # numbers with length exactly n
        total_eq =
          cond do
            n < len_s -> 0
            n == len_s ->
              if s_int <= x, do: 1, else: 0
            true ->
              p = n - len_s
              max_pref = div(x - s_int, pow10_len_s)
              count_prefix_le(max_pref, p, limit)
          end

        total_less + total_eq
      end
    end

    count_up_to.(finish) - count_up_to.(start - 1)
  end

  # integer exponentiation
  defp ipow(_base, 0), do: 1
  defp ipow(base, exp) when exp > 0 do
    if rem(exp, 2) == 0 do
      half = ipow(base, div(exp, 2))
      half * half
    else
      base * ipow(base, exp - 1)
    end
  end

  # count p‑digit prefixes (no leading zero) whose value <= max_val,
  # each digit in [0, limit] and first digit >= 1.
  defp count_prefix_le(max_val, p, limit) do
    digits = Integer.digits(max_val)
    padding = List.duplicate(0, p - length(digits))
    ds = padding ++ digits

    dp_initial = %{true => 1, false => 0}

    final_dp =
      Enum.reduce(0..p - 1, dp_initial, fn idx, dp ->
        new_dp = %{true => 0, false => 0}
        Enum.each([true, false], fn tight ->
          cnt = Map.get(dp, tight, 0)
          if cnt > 0 do
            lo = if idx == 0, do: 1, else: 0
            ub = if tight, do: Enum.at(ds, idx), else: limit
            for d <- lo..ub do
              new_tight = tight && d == Enum.at(ds, idx)
              cur = Map.get(new_dp, new_tight, 0)
              new_dp = Map.put(new_dp, new_tight, cur + cnt)
            end
          end
        end)
        new_dp
      end)

    Map.get(final_dp, true, 0) + Map.get(final_dp, false, 0)
  end
end
```
