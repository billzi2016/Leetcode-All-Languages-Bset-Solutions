# 2827. Number of Beautiful Integers in the Range

## Cpp

```cpp
class Solution {
public:
    int numberOfBeautifulIntegers(int low, int high, int k) {
        return (int)(countUpTo(high, k) - countUpTo((long long)low - 1, k));
    }
private:
    static const int MAXLEN = 10;
    static const int OFFSET = 10; // to shift diff index
    vector<int> digits;
    int K;
    int L;
    long long memo[MAXLEN + 1][21][2 * MAXLEN + 1][2];
    bool seen[MAXLEN + 1][21][2 * MAXLEN + 1][2];

    long long dfs(int pos, int mod, int diff, bool started, bool tight) {
        if (pos == L) {
            return (started && diff == 0 && mod == 0) ? 1LL : 0LL;
        }
        if (!tight && seen[pos][mod][diff + OFFSET][started]) {
            return memo[pos][mod][diff + OFFSET][started];
        }
        int limit = tight ? digits[pos] : 9;
        long long res = 0;
        for (int d = 0; d <= limit; ++d) {
            bool nStarted = started || (d != 0);
            int nMod = (mod * 10 + d) % K;
            int nDiff = diff;
            if (nStarted) {
                if ((d & 1) == 0) nDiff++; // even digit
                else nDiff--;               // odd digit
            }
            bool nTight = tight && (d == limit);
            res += dfs(pos + 1, nMod, nDiff, nStarted, nTight);
        }
        if (!tight) {
            seen[pos][mod][diff + OFFSET][started] = true;
            memo[pos][mod][diff + OFFSET][started] = res;
        }
        return res;
    }

    long long countUpTo(long long n, int k) {
        if (n <= 0) return 0;
        K = k;
        digits.clear();
        while (n > 0) {
            digits.push_back((int)(n % 10));
            n /= 10;
        }
        reverse(digits.begin(), digits.end());
        L = (int)digits.size();
        memset(seen, 0, sizeof(seen));
        return dfs(0, 0, 0, false, true);
    }
};
```

## Java

```java
class Solution {
    public int numberOfBeautifulIntegers(int low, int high, int k) {
        return (int) (count(high, k) - count(low - 1, k));
    }

    private long count(int n, int k) {
        if (n <= 0) return 0;
        String s = Integer.toString(n);
        int len = s.length();
        // diff range [-len, len] -> size 2*len+1
        Long[][][][] memo = new Long[len + 1][k][2 * len + 1][2];
        return dfs(0, 0, 0, false, true, s, k, memo);
    }

    private long dfs(int pos, int rem, int diff, boolean started, boolean tight,
                     String s, int k, Long[][][][] memo) {
        if (pos == s.length()) {
            return (started && diff == 0 && rem == 0) ? 1L : 0L;
        }
        if (!tight) {
            int idx = diff + s.length(); // shift to non‑negative
            int stIdx = started ? 1 : 0;
            Long cached = memo[pos][rem][idx][stIdx];
            if (cached != null) return cached;
        }

        int limit = tight ? s.charAt(pos) - '0' : 9;
        long ans = 0;
        for (int d = 0; d <= limit; ++d) {
            boolean nextStarted = started || d != 0;
            int nextRem = rem;
            int nextDiff = diff;
            if (nextStarted) {
                nextRem = (rem * 10 + d) % k;
                if ((d & 1) == 0) { // even
                    nextDiff++;
                } else {
                    nextDiff--;
                }
                // prune impossible states
                if (Math.abs(nextDiff) > s.length() - pos - 1) {
                    continue;
                }
            }
            ans += dfs(pos + 1, nextRem, nextDiff, nextStarted,
                       tight && d == limit, s, k, memo);
        }

        if (!tight) {
            int idx = diff + s.length();
            int stIdx = started ? 1 : 0;
            memo[pos][rem][idx][stIdx] = ans;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        from functools import lru_cache

        def count_upto(n):
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, diff, rem, tight, started):
                if pos == m:
                    return int(started and diff == 0 and rem == 0)
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    nstarted = started or (d != 0)
                    ndiff = diff
                    nrem = rem
                    if nstarted:
                        if d % 2 == 0:
                            ndiff += 1
                        else:
                            ndiff -= 1
                        nrem = (rem * 10 + d) % k
                    total += dp(pos + 1, ndiff, nrem, ntight, nstarted)
                return total

            # diff offset not needed in cache because we store actual integer diff; range limited by length.
            return dp(0, 0, 0, True, False)

        return count_upto(high) - count_upto(low - 1)
```

## Python3

```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = list(map(int, str(n)))
            m = len(s)

            @lru_cache(None)
            def dfs(pos: int, mod: int, diff: int, started: bool, tight: bool) -> int:
                if pos == m:
                    return int(started and diff == 0 and mod == 0)
                limit = s[pos] if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    nstarted = started or d != 0
                    # update modulo
                    if not nstarted:
                        nmod = 0
                    else:
                        if started:
                            nmod = (mod * 10 + d) % k
                        else:
                            nmod = d % k
                    # update diff
                    ndiff = diff
                    if nstarted:
                        ndiff += 1 if d % 2 == 0 else -1
                    total += dfs(pos + 1, nmod, ndiff, nstarted, ntight)
                return total

            return dfs(0, 0, 0, False, True)

        return count_upto(high) - count_upto(low - 1)
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static string S;
static int K, L, OFFSET;
static long long dp[12][21][22][2];

long long dfs(int pos, int mod, int diff, bool started, bool tight) {
    if (pos == L) {
        return (started && diff == 0 && mod == 0) ? 1LL : 0LL;
    }
    if (!tight) {
        int idx = diff + OFFSET;
        long long &res = dp[pos][mod][idx][started];
        if (res != -1) return res;
        long long ans = 0;
        for (int d = 0; d <= 9; ++d) {
            bool n_started = started || (d != 0);
            int n_mod = (mod * 10 + d) % K;
            int n_diff = diff;
            if (n_started) {
                if (d % 2 == 0) ++n_diff;
                else --n_diff;
            }
            ans += dfs(pos + 1, n_mod, n_diff, n_started, false);
        }
        return res = ans;
    } else {
        int limit = S[pos] - '0';
        long long ans = 0;
        for (int d = 0; d <= limit; ++d) {
            bool n_started = started || (d != 0);
            int n_mod = (mod * 10 + d) % K;
            int n_diff = diff;
            if (n_started) {
                if (d % 2 == 0) ++n_diff;
                else --n_diff;
            }
            ans += dfs(pos + 1, n_mod, n_diff, n_started, tight && d == limit);
        }
        return ans;
    }
}

static long long countUpTo(int n) {
    if (n <= 0) return 0;
    S = to_string(n);
    L = (int)S.size();
    OFFSET = L;                     // diff range [-L, L]
    memset(dp, -1, sizeof(dp));
    return dfs(0, 0, 0, false, true);
}

int numberOfBeautifulIntegers(int low, int high, int k) {
    K = k;
    long long ans = countUpTo(high) - countUpTo(low - 1);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private int[] digits;
    private int len;
    private int kMod;
    private long[,,,] memo; // pos, diff+offset, rem, started(0/1)
    private int offset;

    public int NumberOfBeautifulIntegers(int low, int high, int k)
    {
        long result = Count(high) - Count(low - 1);
        return (int)result;
    }

    private long Count(long n)
    {
        if (n <= 0) return 0;
        var list = new List<int>();
        while (n > 0)
        {
            list.Add((int)(n % 10));
            n /= 10;
        }
        list.Reverse();
        digits = list.ToArray();
        len = digits.Length;
        kMod = Math.Max(1, k); // k is always >=1
        offset = len; // diff ranges from -len..len

        memo = new long[len + 1, 2 * len + 1, kMod, 2];
        for (int i = 0; i <= len; i++)
            for (int d = 0; d < 2 * len + 1; d++)
                for (int r = 0; r < kMod; r++)
                    memo[i, d, r, 0] = memo[i, d, r, 1] = -1;

        return Dfs(0, 0, 0, false, true);
    }

    private long Dfs(int pos, int diff, int rem, bool started, bool tight)
    {
        if (pos == len)
        {
            return (started && diff == 0 && rem == 0) ? 1L : 0L;
        }

        if (!tight)
        {
            int sIdx = started ? 1 : 0;
            long cached = memo[pos, diff + offset, rem, sIdx];
            if (cached != -1) return cached;
        }

        int limit = tight ? digits[pos] : 9;
        long ans = 0;
        for (int d = 0; d <= limit; d++)
        {
            bool nStarted = started || d != 0;
            int ndiff = diff;
            if (nStarted)
            {
                if ((d & 1) == 0) // even
                    ndiff += 1;
                else
                    ndiff -= 1;
            }
            int nrem = (rem * 10 + d) % kMod;
            ans += Dfs(pos + 1, ndiff, nrem, nStarted, tight && d == limit);
        }

        if (!tight)
        {
            int sIdx = started ? 1 : 0;
            memo[pos, diff + offset, rem, sIdx] = ans;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @param {number} k
 * @return {number}
 */
var numberOfBeautifulIntegers = function(low, high, k) {
    const countUpTo = (n) => {
        if (n <= 0) return 0;
        const digits = String(n).split('').map(ch => ch.charCodeAt(0) - 48);
        const len = digits.length;
        const memo = new Map(); // only for non‑tight states

        const dfs = (pos, diff, rem, started, tight) => {
            if (pos === len) {
                return (started && diff === 0 && rem === 0) ? 1 : 0;
            }
            const key = `${pos},${diff},${rem},${started ? 1 : 0},${tight ? 1 : 0}`;
            if (!tight && memo.has(key)) return memo.get(key);

            const limit = tight ? digits[pos] : 9;
            let total = 0;
            for (let d = 0; d <= limit; ++d) {
                const nextTight = tight && d === limit;
                const nextStarted = started || d !== 0;

                let ndiff = diff;
                let nrem = rem;
                if (nextStarted) {
                    // update remainder
                    nrem = (rem * 10 + d) % k;
                    // update even/odd balance
                    ndiff += (d % 2 === 0) ? 1 : -1;
                } else {
                    // still leading zeros: number is zero so far
                    nrem = 0;
                }

                total += dfs(pos + 1, ndiff, nrem, nextStarted, nextTight);
            }

            if (!tight) memo.set(key, total);
            return total;
        };

        return dfs(0, 0, 0, false, true);
    };

    return countUpTo(high) - countUpTo(low - 1);
};
```

## Typescript

```typescript
function numberOfBeautifulIntegers(low: number, high: number, k: number): number {
    const count = (n: number): number => {
        if (n <= 0) return 0;
        const digits = Array.from(String(n), ch => Number(ch));
        const len = digits.length;
        const memo = new Map<string, number>();

        const dfs = (
            pos: number,
            tight: boolean,
            started: boolean,
            diff: number,
            mod: number
        ): number => {
            if (pos === len) {
                return started && diff === 0 && mod === 0 ? 1 : 0;
            }
            const key = `${pos}|${tight ? 1 : 0}|${started ? 1 : 0}|${diff}|${mod}`;
            if (!tight && memo.has(key)) return memo.get(key)!;

            const limit = tight ? digits[pos] : 9;
            let total = 0;
            for (let d = 0; d <= limit; ++d) {
                const ntight = tight && d === limit;
                const nstarted = started || d !== 0;
                let ndiff = diff;
                if (nstarted) {
                    ndiff += d % 2 === 0 ? 1 : -1;
                }
                const nmod = (mod * 10 + d) % k;
                total += dfs(pos + 1, ntight, nstarted, ndiff, nmod);
            }

            if (!tight) memo.set(key, total);
            return total;
        };

        return dfs(0, true, false, 0, 0);
    };

    return count(high) - count(low - 1);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @param Integer $k
     * @return Integer
     */
    function numberOfBeautifulIntegers($low, $high, $k) {
        return $this->countUpTo($high, $k) - $this->countUpTo($low - 1, $k);
    }

    private function countUpTo($n, $k) {
        if ($n <= 0) return 0;
        $digits = array_map('intval', str_split((string)$n));
        $len = count($digits);
        $memo = [];

        $dfs = function($pos, $tight, $diff, $rem, $started) use (&$dfs, &$memo, $digits, $len, $k) {
            if ($pos == $len) {
                return ($started && $diff == 0 && $rem == 0) ? 1 : 0;
            }
            $key = $pos . ',' . ($tight ? 1 : 0) . ',' . $diff . ',' . $rem . ',' . ($started ? 1 : 0);
            if (!$tight && isset($memo[$key])) {
                return $memo[$key];
            }

            $limit = $tight ? $digits[$pos] : 9;
            $res = 0;
            for ($d = 0; $d <= $limit; ++$d) {
                $newStarted = $started || $d != 0;
                $newDiff = $diff;
                $newRem = $rem;
                if ($newStarted) {
                    // update diff: even digit adds +1, odd subtracts -1
                    if (($d & 1) == 0) {
                        $newDiff += 1;
                    } else {
                        $newDiff -= 1;
                    }
                    $newRem = ($rem * 10 + $d) % $k;
                }
                $newTight = $tight && ($d == $limit);
                $res += $dfs($pos + 1, $newTight, $newDiff, $newRem, $newStarted);
            }

            if (!$tight) {
                $memo[$key] = $res;
            }
            return $res;
        };

        return $dfs(0, true, 0, 0, false);
    }
}
```

## Swift

```swift
class Solution {
    func numberOfBeautifulIntegers(_ low: Int, _ high: Int, _ k: Int) -> Int {
        func count(_ n: Int) -> Int {
            if n <= 0 { return 0 }
            let digits = Array(String(n)).map { Int(String($0))! }
            let len = digits.count
            let diffSize = 2 * len + 1   // diff index range after shift
            
            var memo = [Int: Int]()
            
            func dfs(_ idx: Int, _ diff: Int, _ rem: Int, _ started: Bool, _ tight: Bool) -> Int {
                if idx == len {
                    return (started && diff == 0 && rem == 0) ? 1 : 0
                }
                
                if !tight {
                    let diffIdx = diff + len   // shift to non‑negative
                    let key = ((idx * diffSize + diffIdx) * k + rem) * 2 + (started ? 1 : 0)
                    if let cached = memo[key] { return cached }
                    
                    var total = 0
                    for d in 0...9 {
                        let newStarted = started || d != 0
                        var newDiff = diff
                        if newStarted {
                            if d % 2 == 0 {
                                newDiff += 1   // even digit (including zero)
                            } else {
                                newDiff -= 1   // odd digit
                            }
                        }
                        let newRem = (rem * 10 + d) % k
                        total += dfs(idx + 1, newDiff, newRem, newStarted, false)
                    }
                    memo[key] = total
                    return total
                } else {
                    var total = 0
                    let limit = digits[idx]
                    for d in 0...limit {
                        let newTight = tight && (d == limit)
                        let newStarted = started || d != 0
                        var newDiff = diff
                        if newStarted {
                            if d % 2 == 0 {
                                newDiff += 1
                            } else {
                                newDiff -= 1
                            }
                        }
                        let newRem = (rem * 10 + d) % k
                        total += dfs(idx + 1, newDiff, newRem, newStarted, newTight)
                    }
                    return total
                }
            }
            
            return dfs(0, 0, 0, false, true)
        }
        
        return count(high) - count(low - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int {
        fun countUpTo(n: Int): Long {
            if (n <= 0) return 0L
            val digits = n.toString().map { it - '0' }
            val len = digits.size
            val offset = len
            val dp = Array(len) { Array(2 * len + 1) { Array(k) { LongArray(2) { -1L } } } }

            fun dfs(pos: Int, diff: Int, mod: Int, started: Boolean, tight: Boolean): Long {
                if (pos == len) {
                    return if (started && diff == 0 && mod == 0) 1L else 0L
                }
                if (!tight) {
                    val sIdx = if (started) 1 else 0
                    val memo = dp[pos][diff + offset][mod][sIdx]
                    if (memo != -1L) return memo
                }
                var res = 0L
                val limit = if (tight) digits[pos] else 9
                for (d in 0..limit) {
                    val nextStarted = started || d != 0
                    var nextDiff = diff
                    var nextMod = mod
                    if (nextStarted) {
                        if (d % 2 == 0) nextDiff += 1 else nextDiff -= 1
                        nextMod = (mod * 10 + d) % k
                    } else {
                        // still leading zeros: diff and mod stay unchanged (diff is 0, mod is 0)
                        nextDiff = diff
                        nextMod = 0
                    }
                    res += dfs(pos + 1, nextDiff, nextMod, nextStarted, tight && d == limit)
                }
                if (!tight) {
                    val sIdx = if (started) 1 else 0
                    dp[pos][diff + offset][mod][sIdx] = res
                }
                return res
            }

            return dfs(0, 0, 0, false, true)
        }

        val result = countUpTo(high) - countUpTo(low - 1)
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfBeautifulIntegers(int low, int high, int k) {
    return _count(high, k) - _count(low - 1, k);
  }

  late List<int> _digits;
  late List<List<List<List<int>>>> _dp;
  late int _offset;
  late int _k;

  int _dfs(int pos, int diff, int mod, bool started, bool tight) {
    if (pos == _digits.length) {
      return (started && diff == 0 && mod == 0) ? 1 : 0;
    }
    if (!tight) {
      int s = started ? 1 : 0;
      int cached = _dp[pos][diff + _offset][mod][s];
      if (cached != -1) return cached;
    }
    int limit = tight ? _digits[pos] : 9;
    int total = 0;
    for (int d = 0; d <= limit; ++d) {
      bool nStarted = started || d != 0;
      int ndiff = diff;
      if (nStarted) {
        if ((d & 1) == 0) {
          ndiff += 1;
        } else {
          ndiff -= 1;
        }
      }
      int nmod = (mod * 10 + d) % _k;
      total += _dfs(pos + 1, ndiff, nmod, nStarted, tight && d == limit);
    }
    if (!tight) {
      int s = started ? 1 : 0;
      _dp[pos][diff + _offset][mod][s] = total;
    }
    return total;
  }

  int _count(int n, int k) {
    if (n <= 0) return 0;
    _k = k;
    String s = n.toString();
    _digits = List<int>.generate(s.length, (i) => s.codeUnitAt(i) - 48);
    _offset = _digits.length; // max possible absolute diff
    int len = _digits.length;
    _dp = List.generate(
        len,
        (_) => List.generate(2 * len + 1,
            (_) => List.generate(k, (_) => List.filled(2, -1))));
    return _dfs(0, 0, 0, false, true);
  }
}
```

## Golang

```go
package main

import "strconv"

func numberOfBeautifulIntegers(low int, high int, k int) int {
	return int(count(high, k) - count(low-1, k))
}

var (
	digits []int
	memo   [][][][]int64
	K      int
	offset int
)

func count(n int, k int) int64 {
	if n <= 0 {
		return 0
	}
	K = k
	s := strconv.Itoa(n)
	digits = make([]int, len(s))
	for i, ch := range s {
		digits[i] = int(ch - '0')
	}
	maxLen := len(digits)
	offset = maxLen
	diffSize := 2*maxLen + 1

	memo = make([][][][]int64, maxLen+1)
	for i := 0; i <= maxLen; i++ {
		memo[i] = make([][][]int64, diffSize)
		for d := 0; d < diffSize; d++ {
			memo[i][d] = make([][]int64, k)
			for m := 0; m < k; m++ {
				memo[i][d][m] = []int64{-1, -1}
			}
		}
	}

	var dfs func(pos int, diff int, mod int, started bool, tight bool) int64
	dfs = func(pos int, diff int, mod int, started bool, tight bool) int64 {
		if pos == maxLen {
			if started && diff == 0 && mod == 0 {
				return 1
			}
			return 0
		}
		if !tight {
			stIdx := 0
			if started {
				stIdx = 1
			}
			if memo[pos][diff+offset][mod][stIdx] != -1 {
				return memo[pos][diff+offset][mod][stIdx]
			}
		}

		limit := 9
		if tight {
			limit = digits[pos]
		}
		var total int64 = 0
		for d := 0; d <= limit; d++ {
			nStarted := started || d != 0
			nDiff := diff
			nMod := mod
			if nStarted {
				if d%2 == 0 {
					nDiff++
				} else {
					nDiff--
				}
				nMod = (mod*10 + d) % K
			}
			total += dfs(pos+1, nDiff, nMod, nStarted, tight && d == limit)
		}

		if !tight {
			stIdx := 0
			if started {
				stIdx = 1
			}
			memo[pos][diff+offset][mod][stIdx] = total
		}
		return total
	}

	return dfs(0, 0, 0, false, true)
}
```

## Ruby

```ruby
def number_of_beautiful_integers(low, high, k)
  def count_upto(n, k)
    return 0 if n <= 0
    digits = n.to_s.chars.map(&:to_i)
    len = digits.length
    memo = {}
    dfs = lambda do |pos, diff, rem, tight, started|
      if pos == len
        return (started && diff == 0 && rem == 0) ? 1 : 0
      end

      unless tight
        key = [pos, diff, rem, started]
        memo[key] ||= begin
          total = 0
          (0..9).each do |d|
            new_started = started || d != 0
            ndiff = diff
            if new_started
              ndiff += (d.even? ? 1 : -1)
            end
            nrem = (rem * 10 + d) % k
            total += dfs.call(pos + 1, ndiff, nrem, false, new_started)
          end
          total
        end
      else
        limit = digits[pos]
        total = 0
        (0..limit).each do |d|
          new_tight = tight && d == limit
          new_started = started || d != 0
          ndiff = diff
          if new_started
            ndiff += (d.even? ? 1 : -1)
          end
          nrem = (rem * 10 + d) % k
          total += dfs.call(pos + 1, ndiff, nrem, new_tight, new_started)
        end
        total
      end
    end

    dfs.call(0, 0, 0, true, false)
  end

  count_upto(high, k) - count_upto(low - 1, k)
end
```

## Scala

```scala
object Solution {
  def numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int = {
    def count(n: Int): Long = {
      if (n <= 0) return 0L
      val digits = n.toString.map(_.asDigit).toArray
      val len = digits.length
      import scala.collection.mutable
      val memo = mutable.Map[(Int, Int, Int, Boolean), Long]()

      def dfs(pos: Int, diff: Int, rem: Int, started: Boolean, tight: Boolean): Long = {
        if (pos == len) {
          if (started && diff == 0 && rem == 0) 1L else 0L
        } else {
          if (!tight) {
            val key = (pos, diff, rem, started)
            memo.getOrElseUpdate(key, {
              var total = 0L
              for (d <- 0 to 9) {
                val newStarted = started || d != 0
                var newDiff = diff
                var newRem = rem
                if (newStarted) {
                  if ((d & 1) == 0) newDiff += 1 else newDiff -= 1
                  newRem = (rem * 10 + d) % k
                }
                total += dfs(pos + 1, newDiff, newRem, newStarted, false)
              }
              total
            })
          } else {
            var total = 0L
            val limit = digits(pos)
            for (d <- 0 to limit) {
              val newTight = tight && d == limit
              val newStarted = started || d != 0
              var newDiff = diff
              var newRem = rem
              if (newStarted) {
                if ((d & 1) == 0) newDiff += 1 else newDiff -= 1
                newRem = (rem * 10 + d) % k
              }
              total += dfs(pos + 1, newDiff, newRem, newStarted, newTight)
            }
            total
          }
        }
      }

      dfs(0, 0, 0, false, true)
    }

    val result = count(high) - count(low - 1)
    result.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_beautiful_integers(low: i32, high: i32, k: i32) -> i32 {
        fn count_upto(n: i32, k: i32) -> i64 {
            if n <= 0 {
                return 0;
            }
            // extract digits
            let mut digs = Vec::new();
            let mut x = n;
            while x > 0 {
                digs.push((x % 10) as u8);
                x /= 10;
            }
            digs.reverse();
            let len = digs.len();
            let diff_range = 2 * len + 1; // possible diff values from -len..=len
            let offset = len as i32;

            // memo[pos][diff+offset][rem][started] , only for non‑tight states
            let mut memo = vec![-1i64; len * diff_range * (k as usize) * 2];

            fn dfs(
                pos: usize,
                diff: i32,
                rem: i32,
                started: bool,
                tight: bool,
                digs: &Vec<u8>,
                k: i32,
                offset: i32,
                diff_range: usize,
                memo: &mut Vec<i64>,
            ) -> i64 {
                if pos == digs.len() {
                    return if started && diff == 0 && rem == 0 { 1 } else { 0 };
                }
                if !tight {
                    let idx = (((pos * diff_range + (diff + offset) as usize)
                        * k as usize
                        + rem as usize)
                        * 2)
                        + if started { 1 } else { 0 };
                    if memo[idx] != -1 {
                        return memo[idx];
                    }
                }

                let max_digit = if tight { digs[pos] } else { 9 };
                let mut res: i64 = 0;
                for d in 0..=max_digit {
                    let new_started = started || d != 0;
                    let mut new_diff = diff;
                    if new_started {
                        if d % 2 == 0 {
                            new_diff += 1; // even digit
                        } else {
                            new_diff -= 1; // odd digit
                        }
                    }
                    let new_rem = (rem * 10 + d as i32) % k;
                    let new_tight = tight && d == max_digit;
                    res += dfs(
                        pos + 1,
                        new_diff,
                        new_rem,
                        new_started,
                        new_tight,
                        digs,
                        k,
                        offset,
                        diff_range,
                        memo,
                    );
                }

                if !tight {
                    let idx = (((pos * diff_range + (diff + offset) as usize)
                        * k as usize
                        + rem as usize)
                        * 2)
                        + if started { 1 } else { 0 };
                    memo[idx] = res;
                }
                res
            }

            dfs(
                0,
                0,
                0,
                false,
                true,
                &digs,
                k,
                offset,
                diff_range,
                &mut memo,
            )
        }

        let high_cnt = count_upto(high, k);
        let low_cnt = count_upto(low - 1, k);
        (high_cnt - low_cnt) as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-beautiful-integers low high k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (letrec ((count-up-to
            (lambda (n)
              (if (<= n 0) 0
                  (let* ((digits-list
                          (let loop ((x n) (acc '()))
                            (if (= x 0) acc
                                (loop (quotient x 10) (cons (remainder x 10) acc)))))
                         (len (length digits-list))
                         (digits (list->vector digits-list)))
                    (define memo (make-hash))
                    (define (dp idx diff rem tight started)
                      (if (= idx len)
                          (if (and started (= diff 0) (= (modulo rem k) 0)) 1 0)
                          (let ((key (if tight #f (list idx diff rem started))))
                            (if (and (not tight) (hash-has-key? memo key))
                                (hash-ref memo key)
                                (let* ((limit (if tight (vector-ref digits idx) 9)))
                                  (define (iter d acc)
                                    (if (> d limit)
                                        acc
                                        (let* ((new-started (or started (> d 0)))
                                               (values (if new-started
                                                           (list (+ diff (if (even? d) 1 -1))
                                                                 (modulo (+ (* rem 10) d) k))
                                                           (list diff rem))))
                                          (define new-diff (first values))
                                          (define new-rem (second values))
                                          (iter (+ d 1)
                                                (+ acc
                                                   (dp (+ idx 1)
                                                       new-diff
                                                       new-rem
                                                       (and tight (= d limit))
                                                       new-started))))))
                                  (let ((total (iter 0 0)))
                                    (when (not tight) (hash-set! memo key total))
                                    total))))))
                    (dp 0 0 0 #t #f))))))
    (- (count-up-to high) (count-up-to (- low 1)))) )
```

## Erlang

```erlang
-module(solution).
-export([number_of_beautiful_integers/3]).

-spec number_of_beautiful_integers(Low :: integer(), High :: integer(), K :: integer()) -> integer().
number_of_beautiful_integers(Low, High, K) ->
    CountHigh = count_upto(High, K),
    CountLowMinus1 =
        case Low of
            1 -> 0;
            _ -> count_upto(Low - 1, K)
        end,
    CountHigh - CountLowMinus1.

%% count numbers in [1..N] that are beautiful
-spec count_upto(N :: integer(), K :: integer()) -> integer().
count_upto(N, K) when N >= 1 ->
    Digits = [C - $0 || C <- integer_to_list(N)],
    {Res, _} = dfs(0, 0, 0, 0, false, Digits, K, #{}),
    Res;
count_upto(_, _) -> 0.

%% dfs(Position, DiffEvenMinusOdd, RemainderModK, StartedFlag, TightFlag, DigitsList, K, Memo) ->
%% returns {Count, UpdatedMemo}
-spec dfs(integer(), integer(), integer(), integer(), boolean(),
          [integer()], integer(), map()) -> {integer(), map()}.
dfs(Index, Diff, Rem, Started, _Tight, Digits, _K, Memo)
  when Index == length(Digits) ->
    Count = case {Started, Diff, Rem} of
                {1, 0, 0} -> 1;
                _ -> 0
            end,
    {Count, Memo};
dfs(Index, Diff, Rem, Started, false, Digits, K, Memo) ->
    Key = {Index, Diff, Rem, Started},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            loop_digits(Index, Diff, Rem, Started, false, Digits, K, Memo, 9)
    end;
dfs(Index, Diff, Rem, Started, true, Digits, K, Memo) ->
    MaxDigit = lists:nth(Index + 1, Digits),
    loop_digits(Index, Diff, Rem, Started, true, Digits, K, Memo, MaxDigit).

%% iterate over possible digit choices
-spec loop_digits(integer(), integer(), integer(), integer(), boolean(),
                 [integer()], integer(), map(), integer()) -> {integer(), map()}.
loop_digits(Index, Diff, Rem, Started, Tight, Digits, K, MemoIn, MaxDigit) ->
    loop_digits(Index, Diff, Rem, Started, Tight, Digits, K, MemoIn, 0, MaxDigit).

-spec loop_digits(integer(), integer(), integer(), integer(), boolean(),
                 [integer()], integer(), map(), integer(), integer(), integer())
        -> {integer(), map()}.
%% finished iterating
loop_digits(Index, Diff, Rem, Started, false, _Digits, _K, Memo, Acc, D, Max)
  when D > Max ->
    Key = {Index, Diff, Rem, Started},
    NewMemo = maps:put(Key, Acc, Memo),
    {Acc, NewMemo};
loop_digits(_Index, _Diff, _Rem, _Started, true, _Digits, _K, Memo, Acc, D, Max)
  when D > Max ->
    {Acc, Memo};
%% process current digit
loop_digits(Index, Diff, Rem, Started, Tight, Digits, K, MemoIn,
            Acc, D, Max) when D =< Max ->
    Digit = D,
    NewStarted = if Started == 1 orelse Digit =/= 0 -> 1; true -> 0 end,
    NewDiff = case NewStarted of
                  1 ->
                      if Digit rem 2 == 0 -> Diff + 1;
                         true -> Diff - 1
                      end;
                  0 -> Diff
              end,
    NewRem = case NewStarted of
                 1 -> (Rem * 10 + Digit) rem K;
                 0 -> Rem
             end,
    NewTight = Tight andalso (Digit == Max),
    {SubCount, MemoOut} = dfs(Index + 1, NewDiff, NewRem, NewStarted,
                             NewTight, Digits, K, MemoIn),
    loop_digits(Index, Diff, Rem, Started, Tight, Digits, K,
                MemoOut, Acc + SubCount, D + 1, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_beautiful_integers(low :: integer, high :: integer, k :: integer) :: integer
  def number_of_beautiful_integers(low, high, k) do
    count_upto(high, k) - count_upto(low - 1, k)
  end

  defp count_upto(n, _k) when n < 0, do: 0

  defp count_upto(n, k) do
    digits = Integer.digits(n)

    {cnt, _memo} =
      dfs(0, 0, 0, false, true, digits, k, %{})

    cnt
  end

  defp dfs(pos, mod, diff, started, tight, digits, k, memo) do
    if pos == length(digits) do
      if started and diff == 0 and mod == 0 do
        {1, memo}
      else
        {0, memo}
      end
    else
      key = {pos, mod, diff, started}

      if not tight and Map.has_key?(memo, key) do
        {Map.get(memo, key), memo}
      else
        max_digit = if tight, do: Enum.at(digits, pos), else: 9

        {cnt, new_memo} =
          Enum.reduce(0..max_digit, {0, memo}, fn d, {acc, cur_memo} ->
            new_started = started or d != 0

            new_mod =
              if new_started do
                rem(mod * 10 + d, k)
              else
                mod
              end

            new_diff =
              if new_started do
                if rem(d, 2) == 0, do: diff + 1, else: diff - 1
              else
                diff
              end

            new_tight = tight and d == max_digit

            {c, updated_memo} = dfs(pos + 1, new_mod, new_diff, new_started, new_tight, digits, k, cur_memo)

            {acc + c, updated_memo}
          end)

        if not tight do
          {cnt, Map.put(new_memo, key, cnt)}
        else
          {cnt, new_memo}
        end
      end
    end
  end
end
```
