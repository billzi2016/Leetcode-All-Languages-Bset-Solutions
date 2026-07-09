# 0639. Decode Ways II

## Cpp

```cpp
class Solution {
public:
    int numDecodings(string s) {
        const int MOD = 1000000007;
        auto single = [&](char c) -> long long {
            if (c == '*') return 9;
            if (c != '0') return 1;
            return 0;
        };
        auto pairCount = [&](char p, char c) -> long long {
            if (p == '*') {
                if (c == '*') return 15; // 11-19 and 21-26
                // p can be '1' or '2'
                long long cnt = 1; // as '1' + c always valid
                if (c <= '6') cnt += 1; // also as '2' + c
                return cnt;
            }
            if (p == '1') {
                if (c == '*') return 9; // 11-19
                return 1;               // any digit forms valid 10-19
            }
            if (p == '2') {
                if (c == '*') return 6; // 21-26
                if (c <= '6') return 1;
                return 0;
            }
            return 0;
        };
        
        long long dp0 = 1; // empty prefix
        long long dp1 = single(s[0]) % MOD; // first character
        
        for (size_t i = 2; i <= s.size(); ++i) {
            char prev = s[i - 2];
            char curc = s[i - 1];
            long long waysSingle = single(curc);
            long long waysPair = pairCount(prev, curc);
            long long cur = (waysSingle * dp1 + waysPair * dp0) % MOD;
            dp0 = dp1;
            dp1 = cur;
        }
        return static_cast<int>(dp1);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int numDecodings(String s) {
        int n = s.length();
        long a = 1; // dp[i-2]
        long b = singleWays(s.charAt(0));
        if (n == 1) return (int) (b % MOD);
        for (int i = 1; i < n; i++) {
            char curChar = s.charAt(i);
            char prevChar = s.charAt(i - 1);

            long waysSingle = singleWays(curChar) * b % MOD;
            long waysDouble = doubleWays(prevChar, curChar) * a % MOD;

            long cur = (waysSingle + waysDouble) % MOD;
            a = b;
            b = cur;
        }
        return (int) (b % MOD);
    }

    private long singleWays(char ch) {
        if (ch == '*') return 9L;
        if (ch != '0') return 1L;
        return 0L;
    }

    private long doubleWays(char prev, char cur) {
        if (prev == '*' && cur == '*') {
            // 11-19 (9) + 21-26 (6)
            return 15L;
        }
        if (prev == '*') {
            // cur is a digit
            if (cur <= '6') return 2L; // can be 1 or 2
            else return 1L;           // only 1
        }
        if (cur == '*') {
            if (prev == '1') return 9L;
            if (prev == '2') return 6L;
            return 0L;
        }
        int num = (prev - '0') * 10 + (cur - '0');
        return (num >= 10 && num <= 26) ? 1L : 0L;
    }
}
```

## Python

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7

        def single(c):
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1

        def pair(p, c):
            # returns number of ways to decode two-character string p+c
            if p == '*' and c == '*':
                # 11-19 (9) + 21-26 (6)
                return 15
            if p == '*':
                # p can be 1 or 2 depending on c
                if '0' <= c <= '6':
                    return 2  # 10-16 and 20-26
                else:
                    return 1  # only 1x (17-19)
            if c == '*':
                if p == '1':
                    return 9
                if p == '2':
                    return 6
                return 0
            # both are digits
            two = int(p) * 10 + int(c)
            return 1 if 10 <= two <= 26 else 0

        n = len(s)
        a = 1  # dp[i-2]
        b = single(s[0]) % MOD  # dp[i-1] after first char
        if b == 0:
            return 0

        for i in range(1, n):
            c = s[i]
            p = s[i - 1]

            cnt1 = single(c)
            cnt2 = pair(p, c)

            cur = (cnt1 * b + cnt2 * a) % MOD
            a, b = b, cur

        return b
```

## Python3

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # dp[-1] = 1
        a = 1  # dp[i-2]
        # dp[0]
        c0 = s[0]
        if c0 == '*':
            b = 9
        elif c0 == '0':
            b = 0
        else:
            b = 1

        for i in range(1, n):
            cur = s[i]
            prev = s[i - 1]

            # single character decoding ways multiplied by dp[i-1] (b)
            if cur == '*':
                single = 9 * b
            elif cur != '0':
                single = b
            else:
                single = 0

            # two-character decoding ways multiplied by dp[i-2] (a)
            double = 0
            if prev == '*':
                if cur == '*':
                    double = 15 * a          # 11-19 and 21-26
                elif cur == '0':
                    double = 2 * a           # 10 or 20
                elif '1' <= cur <= '6':
                    double = 2 * a           # 11-16 or 21-26
                else:  # '7'-'9'
                    double = 1 * a           # only 17-19
            elif prev == '1':
                if cur == '*':
                    double = 9 * a           # 11-19
                else:
                    double = a               # 10-19
            elif prev == '2':
                if cur == '*':
                    double = 6 * a           # 21-26
                elif cur <= '6':
                    double = a               # 20-26
                else:
                    double = 0

            cur_dp = (single + double) % MOD
            a, b = b, cur_dp

        return b % MOD
```

## C

```c
#include <string.h>

static inline int singleWays(char c) {
    if (c == '*') return 9;
    return (c != '0') ? 1 : 0;
}

static inline int pairWays(char a, char b) {
    if (a == '*' && b == '*')
        return 15;                     // 11-19 (9) + 21-26 (6)
    if (a == '*') {
        // b is digit
        if (b >= '0' && b <= '6')
            return 2;                  // 1b or 2b
        else
            return 1;                  // only 1b
    }
    if (b == '*') {
        if (a == '1')
            return 9;                  // 11-19
        if (a == '2')
            return 6;                  // 21-26
        return 0;
    }
    int num = (a - '0') * 10 + (b - '0');
    return (num >= 10 && num <= 26) ? 1 : 0;
}

int numDecodings(char* s) {
    const int MOD = 1000000007;
    int n = strlen(s);
    long long prev = 1;      // dp[i-1], initially dp[0]
    long long prevPrev = 0;  // dp[i-2], initially undefined
    for (int i = 1; i <= n; ++i) {
        char curChar = s[i - 1];
        long long single = ((long long)singleWays(curChar) * prev) % MOD;
        long long pair = 0;
        if (i >= 2) {
            char prevChar = s[i - 2];
            pair = ((long long)pairWays(prevChar, curChar) * prevPrev) % MOD;
        }
        long long cur = (single + pair) % MOD;
        prevPrev = prev;
        prev = cur;
    }
    return (int)prev;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int NumDecodings(string s) {
        if (string.IsNullOrEmpty(s)) return 0;
        
        long prev2 = 1; // dp[i-2]
        long prev = SingleWays(s[0]) % MOD; // dp[i-1] for i=0
        
        for (int i = 1; i < s.Length; i++) {
            long curSingle = (SingleWays(s[i]) * prev) % MOD;
            long pairCount = PairWays(s[i - 1], s[i]);
            long curPair = (pairCount * prev2) % MOD;
            long cur = (curSingle + curPair) % MOD;
            
            prev2 = prev;
            prev = cur;
        }
        
        return (int)(prev % MOD);
    }
    
    private int SingleWays(char c) {
        if (c == '*') return 9;
        return c != '0' ? 1 : 0;
    }
    
    private int PairWays(char first, char second) {
        if (first == '*' && second == '*')
            return 15; // 11-19 (9) + 21-26 (6)
        
        if (first == '*') {
            // second is a digit
            if (second >= '0' && second <= '6')
                return 2; // can be 1 or 2
            else
                return 1; // only 1
        }
        
        if (second == '*') {
            if (first == '1')
                return 9; // 11-19
            if (first == '2')
                return 6; // 21-26
            return 0;
        }
        
        int val = (first - '0') * 10 + (second - '0');
        return (val >= 10 && val <= 26) ? 1 : 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    if (n === 0) return 0;

    // ways for empty prefix
    let dpPrev2 = 1; // dp[i-2]
    // ways for first character
    let dpPrev1 = s[0] === '*' ? 9 : (s[0] !== '0' ? 1 : 0);

    for (let i = 1; i < n; ++i) {
        const curChar = s[i];
        const prevChar = s[i - 1];

        // single character decoding ways
        let single = 0;
        if (curChar === '*') {
            single = 9;
        } else if (curChar !== '0') {
            single = 1;
        }

        // two-character decoding ways
        let pair = 0;
        if (prevChar === '*' && curChar === '*') {
            // 11-19 and 21-26
            pair = 15;
        } else if (prevChar === '*') {
            // prev can be 1 or 2
            if (curChar >= '0' && curChar <= '6') {
                pair = 2; // 1x or 2x
            } else {
                pair = 1; // only 1x
            }
        } else if (curChar === '*') {
            if (prevChar === '1') {
                pair = 9; // 11-19
            } else if (prevChar === '2') {
                pair = 6; // 21-26
            }
        } else {
            const num = (prevChar.charCodeAt(0) - 48) * 10 + (curChar.charCodeAt(0) - 48);
            if (num >= 10 && num <= 26) {
                pair = 1;
            }
        }

        const cur = (single * dpPrev1 + pair * dpPrev2) % MOD;
        dpPrev2 = dpPrev1;
        dpPrev1 = cur;
    }

    return dpPrev1;
};
```

## Typescript

```typescript
function numDecodings(s: string): number {
    const MOD = 1000000007;
    const n = s.length;

    // dp[i-2]
    let a = 1;
    // dp[i-1] for the first character
    let b = 0;
    const first = s[0];
    if (first === '*') {
        b = 9;
    } else if (first !== '0') {
        b = 1;
    }

    for (let i = 2; i <= n; i++) {
        const curChar = s[i - 1];
        const prevChar = s[i - 2];

        // single character decoding ways
        let singleWays = 0;
        if (curChar === '*') {
            singleWays = 9;
        } else if (curChar !== '0') {
            singleWays = 1;
        }

        let cur = (b * singleWays) % MOD;

        // two-character decoding ways
        let doubleWays = 0;
        if (prevChar === '1') {
            doubleWays = curChar === '*' ? 9 : 1;
        } else if (prevChar === '2') {
            if (curChar === '*') {
                doubleWays = 6;
            } else if (curChar >= '0' && curChar <= '6') {
                doubleWays = 1;
            }
        } else if (prevChar === '*') {
            if (curChar === '*') {
                doubleWays = 15; // 11-19 and 21-26
            } else if (curChar >= '0' && curChar <= '6') {
                doubleWays = 2; // 1x or 2x
            } else {
                doubleWays = 1; // only 1x
            }
        }

        cur = (cur + a * doubleWays) % MOD;

        // shift dp values
        a = b;
        b = cur;
    }

    return b % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numDecodings($s) {
        $mod = 1000000007;
        $n = strlen($s);
        // dp0: ways up to i-2, dp1: ways up to i-1
        $dp0 = 1; // empty string
        // initialize dp1 for first character
        $first = $s[0];
        if ($first === '*') {
            $dp1 = 9;
        } elseif ($first !== '0') {
            $dp1 = 1;
        } else {
            $dp1 = 0;
        }

        for ($i = 1; $i < $n; ++$i) {
            $cur = $s[$i];
            $prev = $s[$i - 1];

            // single character decoding
            if ($cur === '*') {
                $single = (9 * $dp1) % $mod;
            } elseif ($cur !== '0') {
                $single = $dp1;
            } else {
                $single = 0;
            }

            // two-character decoding
            $pair = 0;
            if ($prev === '*' && $cur === '*') {
                // ** -> 11-19 (9) and 21-26 (6)
                $pair = (15 * $dp0) % $mod;
            } elseif ($prev === '*') {
                if ($cur >= '0' && $cur <= '6') {
                    // * can be 1 or 2
                    $pair = (2 * $dp0) % $mod;
                } else { // 7-9
                    $pair = $dp0 % $mod; // only 1
                }
            } elseif ($cur === '*') {
                if ($prev === '1') {
                    $pair = (9 * $dp0) % $mod;
                } elseif ($prev === '2') {
                    $pair = (6 * $dp0) % $mod;
                }
            } else {
                $two = intval($prev . $cur);
                if ($two >= 10 && $two <= 26) {
                    $pair = $dp0 % $mod;
                }
            }

            $currWays = ($single + $pair) % $mod;

            // shift dp values
            $dp0 = $dp1;
            $dp1 = $currWays;
        }

        return $dp1;
    }
}
```

## Swift

```swift
class Solution {
    func numDecodings(_ s: String) -> Int {
        let MOD: Int64 = 1_000_000_007
        let chars = Array(s)
        if chars.isEmpty { return 0 }
        
        // dp[i-2]
        var a: Int64 = 1
        // dp[i-1] for first character
        var b: Int64 = singleWays(chars[0])
        if b == 0 { return 0 }
        if chars.count == 1 {
            return Int(b % MOD)
        }
        
        for i in 1..<chars.count {
            let curChar = chars[i]
            var cur: Int64 = 0
            
            // single character contribution
            if curChar == "*" {
                cur += (9 * b) % MOD
            } else if curChar != "0" {
                cur += b
            }
            
            // pair contribution with previous character
            let prevChar = chars[i - 1]
            var pairWays: Int64 = 0
            
            if prevChar == "*" && curChar == "*" {
                pairWays = (15 * a) % MOD          // ** -> 11-19 (9) + 21-26 (6)
            } else if prevChar == "*" {
                // * followed by digit
                if let d = curChar.wholeNumberValue {
                    if d <= 6 {
                        pairWays = (2 * a) % MOD   // can be 1d or 2d
                    } else {
                        pairWays = a % MOD         // only 1d is valid
                    }
                }
            } else if curChar == "*" {
                // digit followed by *
                if prevChar == "1" {
                    pairWays = (9 * a) % MOD       // 11-19
                } else if prevChar == "2" {
                    pairWays = (6 * a) % MOD       // 21-26
                }
            } else {
                // both are digits
                if let p = prevChar.wholeNumberValue,
                   let c = curChar.wholeNumberValue {
                    let num = p * 10 + c
                    if num >= 10 && num <= 26 {
                        pairWays = a % MOD
                    }
                }
            }
            
            cur = (cur + pairWays) % MOD
            
            // shift dp values
            a = b
            b = cur
        }
        
        return Int(b % MOD)
    }
    
    private func singleWays(_ ch: Character) -> Int64 {
        if ch == "*" { return 9 }
        if ch == "0" { return 0 }
        return 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1000000007L

    fun numDecodings(s: String): Int {
        if (s.isEmpty()) return 0
        var dpPrevPrev = 1L                     // ways for empty prefix
        var dpPrev = singleWays(s[0]) % MOD      // ways for first character

        for (i in 1 until s.length) {
            val cur = s[i]
            val prev = s[i - 1]

            val single = (singleWays(cur) * dpPrev) % MOD
            val pair = (doubleWays(prev, cur) * dpPrevPrev) % MOD
            val current = (single + pair) % MOD

            dpPrevPrev = dpPrev
            dpPrev = current
        }
        return (dpPrev % MOD).toInt()
    }

    private fun singleWays(c: Char): Long {
        return when (c) {
            '*' -> 9L
            '0' -> 0L
            else -> 1L
        }
    }

    private fun doubleWays(p: Char, c: Char): Long {
        return when {
            p == '*' && c == '*' -> 15L                     // ** can be 11-19 (9) or 21-26 (6)
            p == '*' -> {
                if (c in '0'..'6') 2L else if (c in '7'..'9') 1L else 0L
            }
            c == '*' -> {
                when (p) {
                    '1' -> 9L
                    '2' -> 6L
                    else -> 0L
                }
            }
            else -> {
                val num = (p - '0') * 10 + (c - '0')
                if (num in 10..26) 1L else 0L
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;

  int numDecodings(String s) {
    int n = s.length;
    if (n == 0) return 0;
    int prev2 = 1; // dp[i-2]
    int prev1 = _single(s.codeUnitAt(0));
    for (int i = 1; i < n; ++i) {
      int curChar = s.codeUnitAt(i);
      int prevChar = s.codeUnitAt(i - 1);
      int singleCount = _single(curChar);
      int doubleCount = _double(prevChar, curChar);
      int curWays = ((singleCount * prev1) % MOD + (doubleCount * prev2) % MOD) % MOD;
      prev2 = prev1;
      prev1 = curWays;
    }
    return prev1 % MOD;
  }

  int _single(int ch) {
    if (ch == 42) { // '*'
      return 9;
    } else if (ch >= 49 && ch <= 57) { // '1'..'9'
      return 1;
    } else { // '0'
      return 0;
    }
  }

  int _double(int p, int c) {
    if (p == 42 && c == 42) {
      return 15; // '**' -> 11-19 and 21-26
    }
    if (p == 42) { // previous '*', current digit
      if (c >= 48 && c <= 57) {
        if (c <= 54) { // '0'..'6'
          return 2;   // can be 1x or 2x
        } else {
          return 1;   // only 1x
        }
      }
    } else if (c == 42) { // current '*', previous digit
      if (p == 49) { // '1*'
        return 9;
      } else if (p == 50) { // '2*'
        return 6;
      } else {
        return 0;
      }
    } else { // both digits
      int num = (p - 48) * 10 + (c - 48);
      if (num >= 10 && num <= 26) {
        return 1;
      }
    }
    return 0;
  }
}
```

## Golang

```go
func numDecodings(s string) int {
	const MOD int64 = 1000000007
	n := len(s)
	if n == 0 {
		return 0
	}
	var prevPrev int64 = 1 // dp[0]
	var prev int64

	// initialize dp for first character
	switch s[0] {
	case '*':
		prev = 9
	case '0':
		prev = 0
	default:
		prev = 1
	}
	prev %= MOD

	for i := 1; i < n; i++ {
		var cur int64
		ch := s[i]

		// single character decoding
		if ch == '*' {
			cur = (cur + 9*prev) % MOD
		} else if ch != '0' {
			cur = (cur + prev) % MOD
		}

		// two-character decoding with previous character
		prevCh := s[i-1]
		switch prevCh {
		case '1':
			if ch == '*' {
				cur = (cur + 9*prevPrev) % MOD
			} else {
				cur = (cur + prevPrev) % MOD
			}
		case '2':
			if ch == '*' {
				cur = (cur + 6*prevPrev) % MOD
			} else if ch <= '6' {
				cur = (cur + prevPrev) % MOD
			}
		case '*':
			if ch == '*' {
				cur = (cur + 15*prevPrev) % MOD
			} else if ch <= '6' {
				cur = (cur + 2*prevPrev) % MOD
			} else {
				cur = (cur + prevPrev) % MOD
			}
		}

		prevPrev, prev = prev, cur%MOD
	}
	return int(prev % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def num_decodings(s)
  return 0 if s.empty?
  n = s.length
  a = 1 # dp[i-2]
  # first character single ways
  c0 = s.getbyte(0)
  b = (c0 == 42 ? 9 : (c0 >= 49 && c0 <= 57 ? 1 : 0)) % MOD # dp[i-1]

  (1...n).each do |i|
    p = s.getbyte(i - 1)
    c = s.getbyte(i)

    # single character decoding ways
    single = if c == 42
               9
             elsif c >= 49 && c <= 57
               1
             else
               0
             end

    # two-character decoding ways
    pair = case p
           when 49 # '1'
             c == 42 ? 9 : 1
           when 50 # '2'
             if c == 42
               6
             elsif c >= 48 && c <= 54 # '0'..'6'
               1
             else
               0
             end
           when 42 # '*'
             if c == 42
               15
             elsif c >= 48 && c <= 54 # '0'..'6'
               2
             else
               1
             end
           else
             0
           end

    cur = (single * b + pair * a) % MOD
    a, b = b, cur
  end

  b
end
```

## Scala

```scala
object Solution {
    def numDecodings(s: String): Int = {
        val MOD = 1000000007L
        var dp0 = 1L // ways for prefix ending two positions before
        var dp1 = 1L // ways for prefix ending at previous position (empty string initially)

        for (i <- s.indices) {
            val c = s.charAt(i)
            // single character decoding count
            val single: Long = c match {
                case '*' => 9L
                case '0' => 0L
                case _   => 1L
            }

            // two-character decoding count
            var doubleWays: Long = 0L
            if (i > 0) {
                val p = s.charAt(i - 1)
                (p, c) match {
                    case ('*', '*') =>
                        doubleWays = 15L // 11-19 (9) + 21-26 (6)
                    case ('*', d) if d >= '0' && d <= '9' =>
                        if (d <= '6') doubleWays = 2L else doubleWays = 1L
                    case ('1', '*') =>
                        doubleWays = 9L // 11-19
                    case ('1', d) if d >= '0' && d <= '9' =>
                        doubleWays = 1L // 10-19
                    case ('2', '*') =>
                        doubleWays = 6L // 21-26
                    case ('2', d) if d >= '0' && d <= '6' =>
                        doubleWays = 1L // 20-26 where second digit <=6
                    case _ => // other previous digits give no valid two-digit decode
                        doubleWays = 0L
                }
            }

            val cur = ((single * dp1) % MOD + (doubleWays * dp0) % MOD) % MOD
            dp0 = dp1
            dp1 = cur
        }

        dp1.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();

        // dp0: ways for prefix ending two positions before
        // dp1: ways for prefix ending at previous position
        let mut dp0: i64 = 1; // empty string

        let first = bytes[0];
        let mut dp1: i64 = match first {
            b'*' => 9,
            b'0' => 0,
            _ => 1,
        };

        for i in 1..n {
            let c = bytes[i];
            let p = bytes[i - 1];

            // Single character decoding ways
            let single = match c {
                b'*' => 9,
                b'0' => 0,
                _ => 1,
            } as i64;

            let mut cur = (dp1 * single) % MOD;

            // Two-character decoding ways
            let pair: i64 = match p {
                b'*' => match c {
                    b'*' => 15,               // ** -> 11-19 and 21-26
                    b'0'..=b'6' => 2,         // *0~*6 -> 10-16 or 20-26
                    b'7'..=b'9' => 1,         // *7~*9 -> only 17-19
                    _ => 0,
                },
                b'1' => match c {
                    b'*' => 9,                // 1*
                    _ => 1,                   // 10-19
                },
                b'2' => match c {
                    b'*' => 6,                // 2*
                    b'0'..=b'6' => 1,         // 20-26
                    _ => 0,
                },
                _ => 0,
            };

            cur = (cur + dp0 * pair) % MOD;

            dp0 = dp1;
            dp1 = cur;
        }

        dp1 as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

;; count ways for a single character
(define (single-count ch)
  (cond [(char=? ch #\*) 9]
        [(char=? ch #\0) 0]
        [else 1]))

;; count ways for a pair of characters (previous, current)
(define (two-count p c)
  (cond
    [(and (char=? p #\*) (char=? c #\*)) 15]
    [(char=? p #\*)
     (cond [(char=? c #\0) 2]                                   ; "*0" -> "10","20"
           [(and (char>=? c #\1) (char<=? c #\6)) 2]            ; "*1".."*6"
           [else 1])]                                          ; "*7".."*9"
    [(char=? c #\*)
     (cond [(char=? p #\1) 9]
           [(char=? p #\2) 6]
           [else 0])]
    [else
     (let* ((d1 (- (char->integer p) 48))
            (d2 (- (char->integer c) 48))
            (num (+ (* d1 10) d2)))
       (if (and (>= num 10) (<= num 26)) 1 0))]))

;; main function
(define/contract (num-decodings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (dp0 1)                                            ; ways for empty prefix
         (first-char (if (> n 0) (string-ref s 0) #\0))
         (dp1 (modulo (* (single-count first-char) dp0) MOD))) ; ways for first character
    (if (= n 0)
        0
        (let loop ((i 1) (prev2 dp0) (prev dp1))
          (if (= i n)
              prev
              (let* ((c (string-ref s i))
                     (p (string-ref s (- i 1)))
                     (single (* (single-count c) prev))
                     (pair   (* (two-count p c) prev2))
                     (cur (modulo (+ single pair) MOD)))
                (loop (+ i 1) prev cur)))))))
```

## Erlang

```erlang
-module(solution).
-export([num_decodings/1]).
-define(MOD, 1000000007).

-spec num_decodings(S :: unicode:unicode_binary()) -> integer().
num_decodings(S) ->
    List = binary_to_list(S),
    case List of
        [] -> 0;
        [First|Rest] ->
            DP0 = 1,
            DP1 = (single(First) * DP0) rem ?MOD,
            loop(Rest, First, DP0, DP1)
    end.

single($*) -> 9;
single($0) -> 0;
single(C) when C >= $1, C =< $9 -> 1;
single(_) -> 0.

double($*, $*) -> 15;
double($*, D) when D >= $0, D =< $6 -> 2;
double($*, _) -> 1;
double($1, $*) -> 9;
double($1, _) -> 1;
double($2, $*) -> 6;
double($2, D) when D >= $0, D =< $6 -> 1;
double($2, _) -> 0;
double(_, _) -> 0.

loop([], _Prev, _DP_i_2, DP_i_1) ->
    DP_i_1;
loop([C|Rest], Prev, DP_i_2, DP_i_1) ->
    Cur = (single(C) * DP_i_1 + double(Prev, C) * DP_i_2) rem ?MOD,
    loop(Rest, C, DP_i_1, Cur).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_decodings(s :: String.t()) :: integer
  def num_decodings(s) do
    mod = 1_000_000_007
    bytes = :binary.bin_to_list(s)

    [first | rest] = bytes

    prev2 = 1
    prev1 = single(first)
    prev_char = first

    {_, result, _} =
      Enum.reduce(rest, {prev2, prev1, prev_char}, fn cur, {dp_i_2, dp_i_1, prev_c} ->
        s1 = single(cur)
        s2 = double(prev_c, cur)

        cur_dp = rem(s1 * dp_i_1 + s2 * dp_i_2, mod)
        {dp_i_1, cur_dp, cur}
      end)

    result
  end

  defp single(c) do
    cond do
      c == ?* -> 9
      c == ?0 -> 0
      true -> 1
    end
  end

  defp double(prev, cur) do
    if prev == ?* and cur == ?* do
      15
    else
      cond do
        prev == ?* ->
          if cur <= ?6, do: 2, else: 1

        cur == ?* ->
          case prev do
            ?1 -> 9
            ?2 -> 6
            _ -> 0
          end

        true ->
          if (prev == ?1) or (prev == ?2 and cur <= ?6), do: 1, else: 0
      end
    end
  end
end
```
