# 2719. Count of Integers

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    string s;
    int n, minSum, maxSum;
    int dp[23][401][2][2];
    
    int dfs(int idx, int sum, bool tight, bool started) {
        if (sum > maxSum) return 0;
        if (idx == n) {
            return (sum >= minSum && sum <= maxSum) ? 1 : 0;
        }
        int &memo = dp[idx][sum][tight][started];
        if (!tight && memo != -1) return memo;
        long long ans = 0;
        int limit = tight ? s[idx] - '0' : 9;
        for (int d = 0; d <= limit; ++d) {
            bool ntight = tight && (d == limit);
            bool nstarted = started || d != 0;
            int nsum = sum + d; // leading zeros add zero anyway
            ans += dfs(idx + 1, nsum, ntight, nstarted);
        }
        ans %= MOD;
        if (!tight) memo = (int)ans;
        return (int)ans;
    }
    
    int countUpTo(const string& num) {
        s = num;
        n = s.size();
        memset(dp, -1, sizeof(dp));
        return dfs(0, 0, true, false);
    }
    
    string decOne(string str) {
        int i = (int)str.size() - 1;
        while (i >= 0 && str[i] == '0') {
            str[i] = '9';
            --i;
        }
        if (i >= 0) {
            str[i]--;
        }
        // remove leading zeros
        int pos = 0;
        while (pos + 1 < (int)str.size() && str[pos] == '0') ++pos;
        if (pos > 0) str = str.substr(pos);
        return str;
    }
    
    int count(string num1, string num2, int min_sum, int max_sum) {
        minSum = min_sum;
        maxSum = max_sum;
        int total2 = countUpTo(num2);
        string prev = decOne(num1);
        int total1 = countUpTo(prev);
        int ans = total2 - total1;
        if (ans < 0) ans += MOD;
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private String s;
    private int n;
    private int minSum, maxSum;
    private int[][][] memo;

    private int dfs(int pos, int tight, int sum) {
        if (sum > maxSum) return 0;
        if (pos == n) {
            return (sum >= minSum && sum <= maxSum) ? 1 : 0;
        }
        if (memo[pos][tight][sum] != -1) return memo[pos][tight][sum];
        int limit = tight == 1 ? s.charAt(pos) - '0' : 9;
        long res = 0;
        for (int d = 0; d <= limit; ++d) {
            int ntight = (tight == 1 && d == limit) ? 1 : 0;
            int newSum = sum + d;
            if (newSum > maxSum) continue;
            res += dfs(pos + 1, ntight, newSum);
            if (res >= MOD) res -= MOD;
        }
        memo[pos][tight][sum] = (int) res;
        return memo[pos][tight][sum];
    }

    private int countUpTo(String str) {
        this.s = str;
        this.n = str.length();
        memo = new int[n + 1][2][maxSum + 1];
        for (int i = 0; i <= n; ++i) {
            for (int t = 0; t < 2; ++t) {
                java.util.Arrays.fill(memo[i][t], -1);
            }
        }
        return dfs(0, 1, 0);
    }

    private String decrement(String str) {
        char[] arr = str.toCharArray();
        int i = arr.length - 1;
        while (i >= 0 && arr[i] == '0') {
            arr[i] = '9';
            --i;
        }
        if (i < 0) return "0";
        arr[i]--;
        return new String(arr);
    }

    public int count(String num1, String num2, int min_sum, int max_sum) {
        this.minSum = min_sum;
        this.maxSum = max_sum;
        int cntUpper = countUpTo(num2);
        String prev = decrement(num1);
        int cntLower = countUpTo(prev);
        int ans = cntUpper - cntLower;
        if (ans < 0) ans += MOD;
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def count(self, num1, num2, min_sum, max_sum):
        MOD = 10**9 + 7

        def dec_str(s):
            # returns string representation of (int(s) - 1), assuming s >= "1"
            i = len(s) - 1
            while i >= 0 and s[i] == '0':
                i -= 1
            if i < 0:
                return "0"
            lst = list(s)
            lst[i] = str(int(lst[i]) - 1)
            for j in range(i + 1, len(s)):
                lst[j] = '9'
            res = ''.join(lst).lstrip('0')
            return res if res else "0"

        def count_up_to(num):
            digits = list(map(int, num))
            n = len(digits)

            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos, tight, cur_sum):
                if pos == n:
                    return 1 if min_sum <= cur_sum <= max_sum else 0
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ns = cur_sum + d
                    if ns > max_sum:   # prune, further digits only increase sum
                        continue
                    ntight = tight and (d == limit)
                    total += dfs(pos + 1, ntight, ns)
                return total % MOD

            return dfs(0, True, 0)

        prev_num1 = dec_str(num1)
        ans = count_up_to(num2) - count_up_to(prev_num1)
        return ans % MOD
```

## Python3

```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        from functools import lru_cache

        def dec_str(s: str) -> str:
            # subtract 1 from a non-negative integer string
            if s == "0":
                return "0"
            lst = list(s)
            i = len(lst) - 1
            while i >= 0 and lst[i] == '0':
                lst[i] = '9'
                i -= 1
            if i >= 0:
                lst[i] = str(int(lst[i]) - 1)
            # strip leading zeros
            res = ''.join(lst).lstrip('0')
            return res if res else "0"

        def count_upto(s: str) -> int:
            digits = list(map(int, s))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos: int, tight: bool, cur_sum: int) -> int:
                if cur_sum > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= cur_sum <= max_sum else 0
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    total += dfs(pos + 1, ntight, cur_sum + d)
                return total % MOD

            return dfs(0, True, 0)

        total_up_to_num2 = count_upto(num2)
        num1_minus_one = dec_str(num1)
        total_up_to_before_num1 = count_upto(num1_minus_one) if num1_minus_one != "0" else 0
        ans = (total_up_to_num2 - total_up_to_before_num1) % MOD
        return ans
```

## C

```c
#include <string.h>
#define MOD 1000000007

static const char *gstr;
static int glen, gmin_sum, gmax_sum;
static int dp[25][401][2];

static int dfs(int pos, int sum, int tight) {
    if (sum > gmax_sum) return 0;
    if (pos == glen) {
        return (sum >= gmin_sum && sum <= gmax_sum) ? 1 : 0;
    }
    int *memo = &dp[pos][sum][tight];
    if (*memo != -1) return *memo;

    long long ans = 0;
    int limit = tight ? (gstr[pos] - '0') : 9;
    for (int d = 0; d <= limit; ++d) {
        int ntight = (tight && d == limit) ? 1 : 0;
        ans += dfs(pos + 1, sum + d, ntight);
        if (ans >= MOD) ans -= MOD;
    }
    *memo = (int)ans;
    return *memo;
}

static int calc(const char *s) {
    gstr = s;
    glen = strlen(s);
    memset(dp, -1, sizeof(dp));
    return dfs(0, 0, 1);
}

static void dec_str(char *s) {
    int n = strlen(s);
    int i = n - 1;
    while (i >= 0 && s[i] == '0') {
        s[i] = '9';
        --i;
    }
    if (i >= 0) {
        s[i]--;
    }
}

int count(char* num1, char* num2, int min_sum, int max_sum) {
    gmin_sum = min_sum;
    gmax_sum = max_sum;

    int up = calc(num2);

    char tmp[25];
    strcpy(tmp, num1);
    dec_str(tmp);
    int down = calc(tmp);

    int ans = up - down;
    if (ans < 0) ans += MOD;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private const long MOD = 1_000_000_007;
    private int _minSum;
    private int _maxSum;
    private string _s;
    private int _len;
    private long[,] _memo;

    public int Count(string num1, string num2, int min_sum, int max_sum)
    {
        _minSum = min_sum;
        _maxSum = max_sum;

        long cntUpper = CountUpTo(num2);
        string lowerMinusOne = Decrement(num1);
        long cntLower = CountUpTo(lowerMinusOne);

        long ans = (cntUpper - cntLower) % MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }

    private long CountUpTo(string s)
    {
        _s = s;
        _len = s.Length;
        _memo = new long[_len, _maxSum + 1];
        for (int i = 0; i < _len; i++)
            for (int j = 0; j <= _maxSum; j++)
                _memo[i, j] = -1;

        return Dfs(0, 0, true);
    }

    private long Dfs(int pos, int sum, bool tight)
    {
        if (sum > _maxSum) return 0;
        if (pos == _len)
            return (sum >= _minSum && sum <= _maxSum) ? 1 : 0;

        if (!tight && _memo[pos, sum] != -1) return _memo[pos, sum];

        int limit = tight ? _s[pos] - '0' : 9;
        long res = 0;
        for (int d = 0; d <= limit; d++)
        {
            res += Dfs(pos + 1, sum + d, tight && d == limit);
            if (res >= MOD) res -= MOD;
        }

        if (!tight) _memo[pos, sum] = res;
        return res;
    }

    private string Decrement(string s)
    {
        char[] arr = s.ToCharArray();
        int i = arr.Length - 1;
        while (i >= 0 && arr[i] == '0')
        {
            arr[i] = '9';
            i--;
        }
        if (i >= 0)
        {
            arr[i] = (char)(arr[i] - 1);
        }

        int start = 0;
        while (start < arr.Length - 1 && arr[start] == '0')
            start++;

        return new string(arr, start, arr.Length - start);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @param {number} min_sum
 * @param {number} max_sum
 * @return {number}
 */
var count = function(num1, num2, min_sum, max_sum) {
    const MOD = 1000000007;

    // subtract 1 from a numeric string (num > "0")
    function decStr(s) {
        let arr = s.split('');
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === '0') {
            arr[i] = '9';
            i--;
        }
        if (i >= 0) {
            arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
        }
        // strip leading zeros, keep at least one digit
        let res = arr.join('').replace(/^0+/, '');
        return res === '' ? '0' : res;
    }

    // count numbers in [0, s] whose digit sum is within [min_sum, max_sum]
    function countUpTo(s) {
        const digits = s.split('').map(ch => ch.charCodeAt(0) - 48);
        const n = digits.length;
        // dp[pos][sum] for the case when tight == false
        const dp = Array.from({ length: n }, () => Array(max_sum + 1).fill(-1));

        function dfs(pos, sum, tight) {
            if (sum > max_sum) return 0;
            if (pos === n) {
                return (sum >= min_sum && sum <= max_sum) ? 1 : 0;
            }
            if (!tight && dp[pos][sum] !== -1) return dp[pos][sum];

            const limit = tight ? digits[pos] : 9;
            let res = 0;
            for (let d = 0; d <= limit; ++d) {
                res += dfs(pos + 1, sum + d, tight && d === limit);
                if (res >= MOD) res -= MOD;
            }

            if (!tight) dp[pos][sum] = res;
            return res;
        }

        return dfs(0, 0, true);
    }

    const totalNum2 = countUpTo(num2);
    const num1MinusOne = decStr(num1);
    const totalNum1Prev = countUpTo(num1MinusOne);

    let ans = totalNum2 - totalNum1Prev;
    if (ans < 0) ans += MOD;
    return ans % MOD;
};
```

## Typescript

```typescript
function count(num1: string, num2: string, min_sum: number, max_sum: number): number {
    const MOD = 1000000007;

    function decStr(s: string): string {
        const arr = s.split('').map(ch => +ch);
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === 0) {
            arr[i] = 9;
            i--;
        }
        if (i >= 0) arr[i]--;
        let start = 0;
        while (start < arr.length - 1 && arr[start] === 0) start++;
        return arr.slice(start).join('');
    }

    function countUpTo(s: string): number {
        const digits = s.split('').map(ch => +ch);
        const n = digits.length;
        const memo = new Map<string, number>();

        function dfs(pos: number, tight: boolean, sum: number): number {
            if (sum > max_sum) return 0;
            if (pos === n) {
                return sum >= min_sum && sum <= max_sum ? 1 : 0;
            }
            if (!tight) {
                const key = pos + ',' + sum;
                const cached = memo.get(key);
                if (cached !== undefined) return cached;
            }

            const limit = tight ? digits[pos] : 9;
            let res = 0;
            for (let d = 0; d <= limit; d++) {
                const ntight = tight && d === limit;
                res += dfs(pos + 1, ntight, sum + d);
                if (res >= MOD) res -= MOD;
            }

            if (!tight) memo.set(pos + ',' + sum, res);
            return res;
        }

        return dfs(0, true, 0);
    }

    const total2 = countUpTo(num2);
    const num1MinusOne = decStr(num1);
    const total1 = countUpTo(num1MinusOne);
    let ans = total2 - total1;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param String $num1
     * @param String $num2
     * @param Integer $min_sum
     * @param Integer $max_sum
     * @return Integer
     */
    function count($num1, $num2, $min_sum, $max_sum) {
        $this->minSum = $min_sum;
        $this->maxSum = $max_sum;

        $cnt2 = $this->countUpTo($num2);
        $prevNum1 = $this->decrementString($num1);
        if ($prevNum1 === null) { // num1 was "0"
            $cnt1 = 0;
        } else {
            $cnt1 = $this->countUpTo($prevNum1);
        }
        $ans = $cnt2 - $cnt1;
        $ans %= self::MOD;
        if ($ans < 0) $ans += self::MOD;
        return $ans;
    }

    private function countUpTo(string $num): int {
        $digits = array_map('intval', str_split($num));
        $len = count($digits);
        $dp = [];

        $dfs = function($pos, $sum, $tight) use (&$dfs, &$dp, $digits, $len) {
            if ($sum > $this->maxSum) return 0; // prune
            if ($pos == $len) {
                return ($sum >= $this->minSum && $sum <= $this->maxSum) ? 1 : 0;
            }
            $key = $pos . '|' . $sum . '|' . ($tight ? 1 : 0);
            if (!$tight && isset($dp[$key])) {
                return $dp[$key];
            }

            $limit = $tight ? $digits[$pos] : 9;
            $res = 0;
            for ($d = 0; $d <= $limit; $d++) {
                $nextTight = $tight && ($d == $limit);
                $res += $dfs($pos + 1, $sum + $d, $nextTight);
                if ($res >= self::MOD) $res -= self::MOD;
            }

            if (!$tight) {
                $dp[$key] = $res;
            }
            return $res;
        };

        return $dfs(0, 0, true) % self::MOD;
    }

    private function decrementString(string $s): ?string {
        // returns null if result would be negative (i.e., s == "0")
        $len = strlen($s);
        $arr = str_split($s);
        $i = $len - 1;
        while ($i >= 0 && $arr[$i] === '0') {
            $arr[$i] = '9';
            $i--;
        }
        if ($i < 0) {
            return null; // underflow
        }
        $arr[$i] = chr(ord($arr[$i]) - 1);
        // remove leading zeros
        $result = ltrim(implode('', $arr), '0');
        return $result === '' ? '0' : $result;
    }
}
```

## Swift

```swift
class Solution {
    let MOD = 1_000_000_007

    func count(_ num1: String, _ num2: String, _ min_sum: Int, _ max_sum: Int) -> Int {
        func minusOne(_ s: String) -> String {
            var digits = s.map { Int(String($0))! }
            var i = digits.count - 1
            while i >= 0 && digits[i] == 0 {
                digits[i] = 9
                i -= 1
            }
            if i < 0 { return "0" }
            digits[i] -= 1
            var start = 0
            while start < digits.count - 1 && digits[start] == 0 {
                start += 1
            }
            return digits[start...].map { String($0) }.joined()
        }

        func countUpTo(_ num: String, _ limit: Int) -> Int {
            if limit < 0 { return 0 }
            let digits = num.map { Int(String($0))! }
            let n = digits.count
            var memo = Array(
                repeating: Array(
                    repeating: Array(repeating: -1, count: 2),
                    count: limit + 1),
                count: n + 1)

            func dfs(_ pos: Int, _ sum: Int, _ tight: Bool) -> Int {
                if sum > limit { return 0 }
                if pos == n { return 1 } // valid number (including zero)
                let t = tight ? 1 : 0
                if memo[pos][sum][t] != -1 {
                    return memo[pos][sum][t]
                }
                var res = 0
                let maxDigit = tight ? digits[pos] : 9
                for d in 0...maxDigit {
                    let newTight = tight && (d == maxDigit)
                    res += dfs(pos + 1, sum + d, newTight)
                    if res >= MOD { res -= MOD }
                }
                memo[pos][sum][t] = res
                return res
            }

            return dfs(0, 0, true) % MOD
        }

        let prev = minusOne(num1)

        let totalMax = (countUpTo(num2, max_sum) - countUpTo(prev, max_sum) + MOD) % MOD
        let totalMinMinus = (countUpTo(num2, min_sum - 1) - countUpTo(prev, min_sum - 1) + MOD) % MOD

        var ans = totalMax - totalMinMinus
        if ans < 0 { ans += MOD }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L
    private lateinit var digits: IntArray
    private var n = 0
    private var minSum = 0
    private var maxSum = 0
    private lateinit var memo: Array<LongArray>

    fun count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int {
        minSum = min_sum
        maxSum = max_sum
        val cnt2 = countUpTo(num2)
        val decNum1 = decrement(num1)
        val cnt1 = if (decNum1.isEmpty()) 0L else countUpTo(decNum1)
        var ans = (cnt2 - cnt1) % MOD
        if (ans < 0) ans += MOD
        return ans.toInt()
    }

    private fun countUpTo(s: String): Long {
        n = s.length
        digits = IntArray(n)
        for (i in 0 until n) digits[i] = s[i] - '0'
        memo = Array(n) { LongArray(maxSum + 1) { -1L } }
        return dfs(0, 0, true) % MOD
    }

    private fun dfs(pos: Int, sum: Int, tight: Boolean): Long {
        if (pos == n) {
            return if (sum in minSum..maxSum) 1L else 0L
        }
        if (!tight && memo[pos][sum] != -1L) return memo[pos][sum]
        val limit = if (tight) digits[pos] else 9
        var res = 0L
        for (d in 0..limit) {
            val newSum = sum + d
            if (newSum > maxSum) continue
            val ntight = tight && d == limit
            res += dfs(pos + 1, newSum, ntight)
            if (res >= MOD) res -= MOD
        }
        if (!tight) memo[pos][sum] = res
        return res
    }

    private fun decrement(s: String): String {
        val sb = StringBuilder(s)
        var i = sb.length - 1
        while (i >= 0 && sb[i] == '0') {
            sb.setCharAt(i, '9')
            i--
        }
        if (i < 0) return "" // underflow, shouldn't happen per constraints
        sb.setCharAt(i, (sb[i] - '1'))
        // remove leading zeros
        var start = 0
        while (start < sb.length && sb[start] == '0') start++
        return if (start == sb.length) "0" else sb.substring(start)
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  late List<List<int>> _memo; // memo[pos][sum] for tight == false
  late String _digits;
  late int _minSum, _maxSum;

  int _dfs(int pos, int sum, bool tight) {
    if (pos == _digits.length) {
      return (sum >= _minSum && sum <= _maxSum) ? 1 : 0;
    }
    if (!tight && _memo[pos][sum] != -1) {
      return _memo[pos][sum];
    }
    int limit = tight ? (_digits.codeUnitAt(pos) - 48) : 9;
    int res = 0;
    for (int d = 0; d <= limit; ++d) {
      int newSum = sum + d;
      if (newSum > _maxSum) continue; // prune
      bool nextTight = tight && (d == limit);
      res += _dfs(pos + 1, newSum, nextTight);
      if (res >= MOD) res -= MOD;
    }
    if (!tight) {
      _memo[pos][sum] = res;
    }
    return res;
  }

  int _countUpTo(String n) {
    _digits = n;
    int len = _digits.length;
    _memo = List.generate(len, (_) => List.filled(_maxSum + 1, -1));
    return _dfs(0, 0, true);
  }

  String _decOne(String s) {
    // assumes s > "0"
    List<int> arr = s.codeUnits;
    int i = arr.length - 1;
    while (i >= 0 && arr[i] == 48) { // '0'
      arr[i] = 57; // set to '9'
      i--;
    }
    if (i >= 0) {
      arr[i] -= 1;
    }
    String res = String.fromCharCodes(arr);
    int idx = 0;
    while (idx < res.length - 1 && res.codeUnitAt(idx) == 48) {
      idx++;
    }
    return res.substring(idx);
  }

  int count(String num1, String num2, int min_sum, int max_sum) {
    _minSum = min_sum;
    _maxSum = max_sum;

    int cntUpper = _countUpTo(num2);
    String lowerMinusOne = _decOne(num1);
    int cntLower = _countUpTo(lowerMinusOne);

    int ans = cntUpper - cntLower;
    if (ans < 0) ans += MOD;
    return ans % MOD;
  }
}
```

## Golang

```go
package main

import "strconv"

const MOD int = 1000000007

var (
	digits []int
	n      int
	minS   int
	maxS   int
	dp     [][][]int
)

func dfs(pos, sum, tight int) int {
	if pos == n {
		if sum >= minS && sum <= maxS {
			return 1
		}
		return 0
	}
	if dp[pos][sum][tight] != -1 {
		return dp[pos][sum][tight]
	}
	limit := 9
	if tight == 1 {
		limit = digits[pos]
	}
	res := 0
	for d := 0; d <= limit; d++ {
		ns := sum + d
		if ns > maxS {
			continue
		}
		ntight := 0
		if tight == 1 && d == limit {
			ntight = 1
		}
		res += dfs(pos+1, ns, ntight)
		if res >= MOD {
			res -= MOD
		}
	}
	dp[pos][sum][tight] = res
	return res
}

func countUpTo(s string) int {
	// prepare digits
	n = len(s)
	digits = make([]int, n)
	for i := 0; i < n; i++ {
		digits[i] = int(s[i] - '0')
	}
	// allocate dp with -1
	dp = make([][][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([][]int, maxS+1)
		for j := 0; j <= maxS; j++ {
			dp[i][j] = []int{-1, -1}
		}
	}
	return dfs(0, 0, 1) % MOD
}

func subtractOne(s string) string {
	b := []byte(s)
	i := len(b) - 1
	for i >= 0 && b[i] == '0' {
		b[i] = '9'
		i--
	}
	if i >= 0 {
		b[i]--
	}
	// trim leading zeros
	idx := 0
	for idx < len(b) && b[idx] == '0' {
		idx++
	}
	if idx == len(b) {
		return "0"
	}
	return string(b[idx:])
}

func count(num1 string, num2 string, min_sum int, max_sum int) int {
	minS = min_sum
	maxS = max_sum

	cnt2 := countUpTo(num2)

	var cntPrev int
	if num1 == "0" {
		cntPrev = 0
	} else {
		prev := subtractOne(num1)
		// handle case when prev becomes empty (i.e., original was "0")
		if prev == "" {
			prev = "0"
		}
		// ensure prev is a valid number string
		_, err := strconv.Atoi(prev) // just to avoid unused import warning
		_ = err
		cntPrev = countUpTo(prev)
	}

	ans := cnt2 - cntPrev
	if ans < 0 {
		ans += MOD
	}
	return ans % MOD
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def dec_str(s)
  bytes = s.bytes
  i = bytes.length - 1
  while i >= 0 && bytes[i] == 48 # '0'
    bytes[i] = 57               # '9'
    i -= 1
  end
  if i < 0
    return "0"
  else
    bytes[i] -= 1
    res = bytes.pack('C*')
    res.sub!(/^0+/, '')
    res = '0' if res.empty?
    res
  end
end

def count_up_to(num_str, min_sum, max_sum)
  digits = num_str.each_char.map { |c| c.ord - 48 }
  n = digits.length
  dp = Array.new(2) { Array.new(max_sum + 1, 0) }
  dp[1][0] = 1

  (0...n).each do |pos|
    ndp = Array.new(2) { Array.new(max_sum + 1, 0) }
    [0, 1].each do |tight|
      limit = tight == 1 ? digits[pos] : 9
      (0..max_sum).each do |sum|
        cnt = dp[tight][sum]
        next if cnt == 0
        d = 0
        while d <= limit
          ns = sum + d
          break if ns > max_sum
          ntight = (tight == 1 && d == limit) ? 1 : 0
          ndp[ntight][ns] = (ndp[ntight][ns] + cnt) % MOD
          d += 1
        end
      end
    end
    dp = ndp
  end

  total = 0
  [0, 1].each do |tight|
    (min_sum..max_sum).each do |s|
      total = (total + dp[tight][s]) % MOD
    end
  end
  total
end

# @param {String} num1
# @param {String} num2
# @param {Integer} min_sum
# @param {Integer} max_sum
# @return {Integer}
def count(num1, num2, min_sum, max_sum)
  up = count_up_to(num2, min_sum, max_sum)
  down = count_up_to(dec_str(num1), min_sum, max_sum)
  ans = (up - down) % MOD
  ans += MOD if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int = {

        // digit DP for numbers in [0, num]
        def f(num: String): Int = {
            if (num == "0") return 0
            val digits = num.map(_.asDigit).toArray
            val n = digits.length
            val memo = Array.ofDim[Int](n + 1, 2, max_sum + 1)
            val seen = Array.ofDim[Boolean](n + 1, 2, max_sum + 1)

            def dfs(pos: Int, tight: Int, sum: Int): Int = {
                if (sum > max_sum) return 0
                if (pos == n) {
                    if (sum >= min_sum && sum <= max_sum) 1 else 0
                } else {
                    if (seen(pos)(tight)(sum)) return memo(pos)(tight)(sum)
                    var res = 0L
                    val limit = if (tight == 1) digits(pos) else 9
                    var d = 0
                    while (d <= limit) {
                        val ntight = if (tight == 1 && d == limit) 1 else 0
                        res += dfs(pos + 1, ntight, sum + d)
                        if (res >= MOD) res -= MOD
                        d += 1
                    }
                    seen(pos)(tight)(sum) = true
                    memo(pos)(tight)(sum) = (res % MOD).toInt
                    memo(pos)(tight)(sum)
                }
            }

            dfs(0, 1, 0)
        }

        // decrement a numeric string by one
        def decOne(s: String): String = {
            if (s == "0") return "0"
            val sb = new java.lang.StringBuilder(s)
            var i = sb.length - 1
            while (i >= 0 && sb.charAt(i) == '0') {
                sb.setCharAt(i, '9')
                i -= 1
            }
            if (i >= 0) {
                sb.setCharAt(i, ((sb.charAt(i) - '0' - 1) + '0').toChar)
            }
            var res = sb.toString()
            var idx = 0
            while (idx < res.length && res.charAt(idx) == '0') idx += 1
            if (idx == res.length) "0" else res.substring(idx)
        }

        val prev = decOne(num1)

        val ans = (f(num2).toLong - f(prev).toLong) % MOD
        ((ans + MOD) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    const MOD: i64 = 1_000_000_007;

    pub fn count(num1: String, num2: String, min_sum: i32, max_sum: i32) -> i32 {
        fn dec_str(s: &str) -> String {
            let mut bytes: Vec<u8> = s.as_bytes().to_vec();
            let mut i = bytes.len();
            while i > 0 {
                i -= 1;
                if bytes[i] > b'0' {
                    bytes[i] -= 1;
                    break;
                } else {
                    bytes[i] = b'9';
                }
            }
            // trim leading zeros, keep at least one digit
            let mut start = 0;
            while start + 1 < bytes.len() && bytes[start] == b'0' {
                start += 1;
            }
            String::from_utf8(bytes[start..].to_vec()).unwrap()
        }

        fn dfs(
            pos: usize,
            sum: i32,
            tight: bool,
            digits: &[i32],
            min_sum: i32,
            max_sum: i32,
            memo: &mut Vec<Vec<i64>>,
        ) -> i64 {
            if pos == digits.len() {
                return if sum >= min_sum && sum <= max_sum { 1 } else { 0 };
            }
            if !tight && memo[pos][sum as usize] != -1 {
                return memo[pos][sum as usize];
            }
            let limit = if tight { digits[pos] } else { 9 };
            let mut res: i64 = 0;
            for d in 0..=limit {
                let new_sum = sum + d;
                if new_sum > max_sum {
                    continue;
                }
                let ntight = tight && (d == limit);
                res += dfs(pos + 1, new_sum, ntight, digits, min_sum, max_sum, memo);
                if res >= Self::MOD {
                    res -= Self::MOD;
                }
            }
            res %= Self::MOD;
            if !tight {
                memo[pos][sum as usize] = res;
            }
            res
        }

        fn count_upto(num: &str, min_sum: i32, max_sum: i32) -> i64 {
            let digits: Vec<i32> = num.bytes().map(|b| (b - b'0') as i32).collect();
            let mut memo = vec![vec![-1i64; (max_sum + 1) as usize]; digits.len()];
            dfs(0, 0, true, &digits, min_sum, max_sum, &mut memo)
        }

        let cnt2 = count_upto(&num2, min_sum, max_sum);
        let num1_minus_one = dec_str(&num1);
        let cnt1 = count_upto(&num1_minus_one, min_sum, max_sum);
        let mut ans = (cnt2 - cnt1) % Self::MOD;
        if ans < 0 {
            ans += Self::MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(: dec-string (String -> String))
(define (dec-string s)
  (let ((n (string->number s)))
    (if (= n 0)
        "0"
        (number->string (- n 1)))))

(: count-up-to (String Integer Integer -> Integer))
(define (count-up-to s min-sum max-sum)
  (let* ((digits (map (lambda (c) (- (char->integer c) (char->integer #\0)))
                      (string->list s)))
         (len (length digits))
         (memo (make-hash)))
    (: dfs (Integer Boolean Integer -> Integer))
    (define (dfs idx tight sum)
      (if (= idx len)
          (if (and (>= sum min-sum) (<= sum max-sum)) 1 0)
          (let ((key (list idx (if tight 1 0) sum)))
            (if (hash-has-key? memo key)
                (hash-ref memo key)
                (let* ((limit (if tight (list-ref digits idx) 9))
                       (total
                        (let loop ((d 0) (acc 0))
                          (if (> d limit)
                              acc
                              (let* ((newtight (and tight (= d limit)))
                                     (add (dfs (+ idx 1) newtight (+ sum d))))
                                (loop (+ d 1) (remainder (+ acc add) MOD)))))))
                  (hash-set! memo key total)
                  total)))))
    (dfs 0 #t 0)))

(: count (String String Integer Integer -> Integer))
(define/contract (count num1 num2 min_sum max_sum)
  (-> string? string? exact-integer? exact-integer? exact-integer?)
  (let* ((cnt2 (count-up-to num2 min_sum max_sum))
         (prev1 (dec-string num1))
         (cnt1 (count-up-to prev1 min_sum max_sum))
         (ans (remainder (- cnt2 cnt1) MOD)))
    (if (< ans 0) (+ ans MOD) ans)))
```

## Erlang

```erlang
-module(solution).
-export([count/4]).

-define(MOD, 1000000007).

-spec count(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary(),
            Min_sum :: integer(), Max_sum :: integer()) -> integer().
count(Num1, Num2, Min_sum, Max_sum) ->
    F2 = count_up_to(Num2, Min_sum, Max_sum),
    PrevNum1 = dec_binary(Num1),
    F1 = count_up_to(PrevNum1, Min_sum, Max_sum),
    Res = (F2 - F1) rem ?MOD,
    if Res < 0 -> Res + ?MOD; true -> Res end.

%% Count numbers from 0 to N (inclusive) whose digit sum is in [L,R]
-spec count_up_to(unicode:unicode_binary(), integer(), integer()) -> integer().
count_up_to(NBin, L, R) ->
    Digits = [C - $0 || C <- binary_to_list(NBin)],
    InitDP = #{ {1, 0} => 1 },
    DPFinal = lists:foldl(
        fun(Dig, DPAcc) ->
            maps:fold(
                fun({{Tight, Sum}, Cnt}, Acc) ->
                    MaxD = if Tight == 1 -> Dig; true -> 9 end,
                    lists:foldl(
                        fun(Nd, A) ->
                            NewSum = Sum + Nd,
                            if NewSum > R -> A;
                               true ->
                                   NewTight = if Tight == 1 andalso Nd == Dig -> 1; true -> 0 end,
                                   Key = {NewTight, NewSum},
                                   Prev = maps:get(Key, A, 0),
                                   maps:put(Key, (Prev + Cnt) rem ?MOD, A)
                            end
                        end,
                        Acc,
                        lists:seq(0, MaxD)
                    )
                end,
                #{},
                DPAcc
            )
        end,
        InitDP,
        Digits
    ),
    maps:fold(
        fun({{_Tight, Sum}, Cnt}, Acc) ->
            if Sum >= L, Sum =< R -> (Acc + Cnt) rem ?MOD;
               true -> Acc
            end
        end,
        0,
        DPFinal
    ).

%% Decrement a numeric string represented as binary by one.
-spec dec_binary(unicode:unicode_binary()) -> unicode:unicode_binary().
dec_binary(Bin) ->
    List = binary_to_list(Bin),
    Rev = lists:reverse(List),
    {NewRev, _} = dec_rev(Rev, true),
    list_to_binary(lists:reverse(NewRev)).

-spec dec_rev([integer()], boolean()) -> {[integer()], boolean()}.
dec_rev([], Borrow) ->
    {[], Borrow};
dec_rev([Char | Rest], Borrow) ->
    Digit = Char - $0,
    case Borrow of
        true ->
            if Digit == 0 ->
                    NewDigit = 9,
                    NextBorrow = true;
               true ->
                    NewDigit = Digit - 1,
                    NextBorrow = false
            end;
        false ->
            NewDigit = Digit,
            NextBorrow = false
    end,
    {Tail, FinalBorrow} = dec_rev(Rest, NextBorrow),
    {[NewDigit + $0 | Tail], FinalBorrow}.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec count(String.t(), String.t(), integer(), integer()) :: integer()
  def count(num1, num2, min_sum, max_sum) do
    f2 = calc(num2, min_sum, max_sum)
    num1_minus = dec_str(num1)
    f1 = calc(num1_minus, min_sum, max_sum)
    ans = rem(f2 - f1 + @mod, @mod)
    ans
  end

  # calculate number of integers in [0, n] whose digit sum is within [min_sum, max_sum]
  defp calc(n_str, min_sum, max_sum) do
    digits = String.graphemes(n_str) |> Enum.map(&String.to_integer/1)
    len = length(digits)

    {cnt, _} =
      dfs(0, 0, true, digits, len, min_sum, max_sum, %{})

    cnt
  end

  # depth‑first search with memoization for the non‑tight case
  defp dfs(pos, sum, tight, digits, len, min_sum, max_sum, memo) do
    cond do
      pos == len ->
        if sum >= min_sum and sum <= max_sum, do: {1, memo}, else: {0, memo}

      not tight ->
        key = {pos, sum}
        case :maps.find(key, memo) do
          {:ok, val} -> {val, memo}
          :error ->
            limit = 9

            {cnt, new_memo} =
              Enum.reduce(0..limit, {0, memo}, fn d, {acc_cnt, acc_mem} ->
                new_sum = sum + d

                if new_sum > max_sum do
                  {acc_cnt, acc_mem}
                else
                  {sub_cnt, sub_mem} = dfs(pos + 1, new_sum, false, digits, len, min_sum, max_sum, acc_mem)
                  {(acc_cnt + sub_cnt) |> rem(@mod), sub_mem}
                end
              end)

            {cnt, :maps.put(key, cnt, new_memo)}
        end

      true ->
        limit = Enum.at(digits, pos)

        {cnt, final_memo} =
          Enum.reduce(0..limit, {0, memo}, fn d, {acc_cnt, acc_mem} ->
            new_sum = sum + d

            if new_sum > max_sum do
              {acc_cnt, acc_mem}
            else
              next_tight = d == limit
              {sub_cnt, sub_mem} = dfs(pos + 1, new_sum, next_tight, digits, len, min_sum, max_sum, acc_mem)
              {(acc_cnt + sub_cnt) |> rem(@mod), sub_mem}
            end
          end)

        {cnt, final_memo}
    end
  end

  # subtract one from a numeric string (num >= "1")
  defp dec_str(s) do
    chars = String.to_charlist(s)

    {new_rev, borrow} =
      Enum.reduce(Enum.reverse(chars), {[], 1}, fn c, {acc, b} ->
        cond do
          b == 0 -> {[c | acc], 0}
          c > ?0 -> {[c - 1 | acc], 0}
          true -> {[?9 | acc], 1}
        end
      end)

    # remove leading zeros
    new =
      new_rev
      |> Enum.drop_while(fn ch -> ch == ?0 end)

    if new == [] do
      "0"
    else
      List.to_string(new)
    end
  end
end
```
