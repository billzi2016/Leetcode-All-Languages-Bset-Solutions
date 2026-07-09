# 2376. Count Special Integers

## Cpp

```cpp
class Solution {
public:
    long long perm(int m, int k) {
        long long res = 1;
        for (int i = 0; i < k; ++i) res *= (m - i);
        return res;
    }
    
    int countSpecialNumbers(int n) {
        string s = to_string(n);
        int len = s.size();
        long long ans = 0;
        
        // numbers with length less than len
        for (int l = 1; l < len; ++l) {
            ans += 9 * perm(9, l - 1);
        }
        
        int usedMask = 0;
        for (int i = 0; i < len; ++i) {
            int cur = s[i] - '0';
            for (int d = (i == 0 ? 1 : 0); d < cur; ++d) {
                if (usedMask & (1 << d)) continue;
                ans += perm(10 - (__builtin_popcount(usedMask) + 1), len - i - 1);
            }
            if (usedMask & (1 << cur)) {
                return (int)ans;
            }
            usedMask |= (1 << cur);
        }
        // n itself is special
        ans += 1;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countSpecialNumbers(int n) {
        String s = Integer.toString(n);
        int len = s.length();
        long ans = 0;
        // Count numbers with length less than len
        for (int k = 1; k < len; ++k) {
            long cnt = 9;
            int available = 9;
            for (int i = 1; i < k; ++i) {
                cnt *= available;
                --available;
            }
            ans += cnt;
        }
        boolean[] used = new boolean[10];
        for (int i = 0; i < len; ++i) {
            int cur = s.charAt(i) - '0';
            for (int d = (i == 0 ? 1 : 0); d < cur; ++d) {
                if (!used[d]) {
                    int remain = len - i - 1;
                    int unusedDigits = 10 - (i + 1);
                    ans += perm(unusedDigits, remain);
                }
            }
            if (used[cur]) {
                return (int) ans;
            }
            used[cur] = true;
        }
        // n itself is special
        ans += 1;
        return (int) ans;
    }

    private long perm(int m, int k) {
        if (k > m) return 0;
        long res = 1;
        for (int i = 0; i < k; ++i) {
            res *= (m - i);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        L = len(s)

        # count numbers with length less than L
        total = 0
        for k in range(1, L):
            cnt = 9  # first digit cannot be zero
            avail = 9  # remaining digits after picking the first (including zero)
            for i in range(k - 1):
                cnt *= (avail - i)
            total += cnt

        used = set()
        for i, ch in enumerate(s):
            cur = int(ch)

            start_digit = 1 if i == 0 else 0
            for d in range(start_digit, cur):
                if d in used:
                    continue
                remaining = L - i - 1
                avail = 10 - (i + 1)  # digits left after choosing d
                if remaining > avail:
                    continue
                cnt = 1
                for j in range(remaining):
                    cnt *= (avail - j)
                total += cnt

            if cur in used:
                break
            used.add(cur)
        else:
            total += 1  # n itself is special

        return total
```

## Python3

```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # helper to compute P(k, r) = k * (k-1) * ... * (k-r+1)
        def perm(k: int, r: int) -> int:
            if r > k:
                return 0
            res = 1
            for i in range(r):
                res *= k - i
            return res

        ans = 0
        # numbers with length less than m
        for l in range(1, m):
            ans += 9 * perm(9, l - 1)

        used = set()
        for i, ch in enumerate(s):
            cur = int(ch)
            start = 1 if i == 0 else 0
            for d in range(start, cur):
                if d in used:
                    continue
                remaining = m - i - 1
                ans += perm(10 - (i + 1), remaining)
            if cur in used:
                break
            used.add(cur)
        else:
            # n itself has all distinct digits
            ans += 1

        return ans
```

## C

```c
#include <string.h>

static int digits[12];
static int len;
static long long dp[11][1024][2][2];

static long long dfs(int pos, int mask, int tight, int started) {
    if (pos == len) return started ? 1LL : 0LL;
    long long *memo = &dp[pos][mask][tight][started];
    if (*memo != -1) return *memo;

    long long res = 0;
    int limit = tight ? digits[pos] : 9;
    for (int d = 0; d <= limit; ++d) {
        int ntight = tight && (d == limit);
        if (!started && d == 0) {
            // still leading zeros
            res += dfs(pos + 1, mask, ntight, 0);
        } else {
            if (mask & (1 << d)) continue; // digit already used
            res += dfs(pos + 1, mask | (1 << d), ntight, 1);
        }
    }
    *memo = res;
    return res;
}

int countSpecialNumbers(int n) {
    // extract digits
    len = 0;
    while (n > 0) {
        digits[len++] = n % 10;
        n /= 10;
    }
    if (len == 0) { // n == 0, though constraints say n >=1
        return 0;
    }
    // reverse to most significant first
    for (int i = 0; i < len / 2; ++i) {
        int tmp = digits[i];
        digits[i] = digits[len - 1 - i];
        digits[len - 1 - i] = tmp;
    }

    memset(dp, -1, sizeof(dp));
    return (int)dfs(0, 0, 1, 0);
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int CountSpecialNumbers(int n) {
        string s = n.ToString();
        int len = s.Length;
        long ans = 0;

        // count numbers with length less than len
        for (int L = 1; L < len; L++) {
            ans += 9 * Permute(9, L - 1);
        }

        int usedMask = 0;
        for (int i = 0; i < len; i++) {
            int curDigit = s[i] - '0';
            int start = (i == 0) ? 1 : 0;
            for (int d = start; d < curDigit; d++) {
                if ((usedMask & (1 << d)) != 0) continue;
                ans += Permute(10 - (i + 1), len - i - 1);
            }
            if ((usedMask & (1 << curDigit)) != 0) {
                // duplicate digit, cannot form further numbers
                return (int)ans;
            }
            usedMask |= 1 << curDigit;
        }

        // n itself is special
        ans += 1;
        return (int)ans;
    }

    private long Permute(int available, int k) {
        long res = 1;
        for (int i = 0; i < k; i++) {
            res *= (available - i);
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countSpecialNumbers = function(n) {
    const digits = String(n).split('').map(ch => +ch);
    const len = digits.length;
    let ans = 0;

    // Count numbers with length less than len
    for (let l = 1; l < len; ++l) {
        ans += 9 * perm(9, l - 1);
    }

    let usedMask = 0;
    for (let i = 0; i < len; ++i) {
        const cur = digits[i];
        const start = i === 0 ? 1 : 0;
        for (let d = start; d < cur; ++d) {
            if ((usedMask >> d) & 1) continue;
            ans += perm(10 - (i + 1), len - i - 1);
        }
        // If current digit already used, cannot proceed further
        if ((usedMask >> cur) & 1) {
            return ans;
        }
        usedMask |= 1 << cur;
    }

    // n itself is special
    return ans + 1;
};

function perm(available, k) {
    let res = 1;
    for (let i = 0; i < k; ++i) {
        res *= (available - i);
    }
    return res;
}
```

## Typescript

```typescript
function countSpecialNumbers(n: number): number {
    const s = n.toString();
    const L = s.length;
    let total = 0;

    // Count numbers with length less than L
    for (let len = 1; len < L; ++len) {
        total += 9 * perm(9, len - 1);
    }

    const used = new Set<number>();
    for (let i = 0; i < L; ++i) {
        const cur = s.charCodeAt(i) - 48;
        const start = i === 0 ? 1 : 0;
        for (let d = start; d < cur; ++d) {
            if (!used.has(d)) {
                total += perm(10 - (i + 1), L - i - 1);
            }
        }
        if (used.has(cur)) {
            return total;
        }
        used.add(cur);
    }

    // n itself is special
    return total + 1;
}

function perm(m: number, k: number): number {
    let res = 1;
    for (let i = 0; i < k; ++i) {
        res *= (m - i);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countSpecialNumbers($n) {
        $s = strval($n);
        $len = strlen($s);
        $ans = 0;

        // helper: permutation P(available, k)
        $perm = function($available, $k) {
            if ($k == 0) return 1;
            $res = 1;
            for ($i = 0; $i < $k; $i++) {
                $res *= ($available - $i);
            }
            return $res;
        };

        // count numbers with length less than len
        for ($l = 1; $l < $len && $l <= 10; $l++) {
            $ans += 9 * $perm(9, $l - 1);
        }

        // digit DP for same length
        $usedMask = 0;
        for ($i = 0; $i < $len; $i++) {
            $digit = intval($s[$i]);
            $start = ($i == 0) ? 1 : 0;

            for ($d = $start; $d < $digit; $d++) {
                if (($usedMask & (1 << $d)) != 0) continue;
                // count ways to fill remaining positions
                $remaining = $len - $i - 1;
                // number of digits already used after placing d
                $usedCount = $this->popcnt($usedMask) + 1;
                $available = 10 - $usedCount;
                $ans += $perm($available, $remaining);
            }

            if (($usedMask & (1 << $digit)) != 0) {
                return $ans; // cannot use further digits
            }
            $usedMask |= (1 << $digit);
        }

        // n itself is special
        $ans += 1;
        return $ans;
    }

    private function popcnt($x) {
        $c = 0;
        while ($x) {
            $c += $x & 1;
            $x >>= 1;
        }
        return $c;
    }
}
```

## Swift

```swift
class Solution {
    func countSpecialNumbers(_ n: Int) -> Int {
        let digits = String(n).compactMap { $0.wholeNumberValue }
        let m = digits.count
        var ans = 0
        
        func perm(_ a: Int, _ b: Int) -> Int {
            if b == 0 { return 1 }
            var res = 1
            for i in 0..<b {
                res *= (a - i)
            }
            return res
        }
        
        // Count numbers with length less than m
        if m > 1 {
            for len in 1..<(m) {
                ans += 9 * perm(9, len - 1)
            }
        }
        
        var used = Set<Int>()
        for i in 0..<m {
            let cur = digits[i]
            let start = (i == 0) ? 1 : 0
            if start < cur {
                for x in start..<cur {
                    if !used.contains(x) {
                        let remaining = m - i - 1
                        let available = 10 - (i + 1)
                        ans += perm(available, remaining)
                    }
                }
            }
            if used.contains(cur) {
                break
            }
            used.insert(cur)
            if i == m - 1 {
                ans += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSpecialNumbers(n: Int): Int {
        val s = n.toString()
        val len = s.length
        var ans = 0L

        // Count numbers with length less than len
        for (l in 1 until len) {
            var cnt = 9L
            var available = 9
            var k = l - 1
            while (k > 0) {
                cnt *= available
                available--
                k--
            }
            ans += cnt
        }

        var mask = 0
        for (i in 0 until len) {
            val cur = s[i] - '0'
            val start = if (i == 0) 1 else 0
            for (d in start until cur) {
                if ((mask and (1 shl d)) == 0) {
                    var used = Integer.bitCount(mask) + 1 // include digit d
                    var avail = 10 - used
                    var add = 1L
                    var remaining = len - i - 1
                    while (remaining > 0) {
                        add *= avail
                        avail--
                        remaining--
                    }
                    ans += add
                }
            }
            if ((mask and (1 shl cur)) != 0) {
                return ans.toInt()
            }
            mask = mask or (1 shl cur)
        }

        // n itself is special
        ans += 1
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countSpecialNumbers(int n) {
    String s = n.toString();
    int len = s.length;
    int ans = 0;

    // Count numbers with length less than len
    for (int k = 1; k < len; ++k) {
      ans += 9 * _perm(9, k - 1);
    }

    int usedMask = 0;
    int usedCnt = 0;

    for (int i = 0; i < len; ++i) {
      int cur = s.codeUnitAt(i) - 48;
      int start = (i == 0) ? 1 : 0;
      for (int d = start; d < cur; ++d) {
        if ((usedMask >> d & 1) == 0) {
          int remaining = len - i - 1;
          int available = 10 - (usedCnt + 1);
          ans += _perm(available, remaining);
        }
      }
      if ((usedMask >> cur & 1) == 1) {
        return ans;
      }
      usedMask |= (1 << cur);
      usedCnt++;
    }

    // n itself is special
    return ans + 1;
  }

  int _perm(int m, int r) {
    if (r > m) return 0;
    int res = 1;
    for (int i = 0; i < r; ++i) {
      res *= (m - i);
    }
    return res;
  }
}
```

## Golang

```go
func countSpecialNumbers(n int) int {
	// Extract digits of n into a slice (most significant first)
	digits := []int{}
	for x := n; x > 0; x /= 10 {
		digits = append(digits, x%10)
	}
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		digits[i], digits[j] = digits[j], digits[i]
	}
	length := len(digits)

	// Count numbers with length less than the length of n
	res := 0
	for l := 1; l < length; l++ {
		cnt := 9 // first digit cannot be zero
		available := 9
		for i := 1; i < l; i++ {
			cnt *= available
			available--
		}
		res += cnt
	}

	used := make([]bool, 10)
	for i, d := range digits {
		start := 0
		if i == 0 {
			start = 1 // leading zero not allowed
		}
		for cand := start; cand < d; cand++ {
			if !used[cand] {
				remaining := length - i - 1
				availableDigits := 10 - (i + 1) // digits left after picking this candidate
				perm := 1
				for k := 0; k < remaining; k++ {
					perm *= (availableDigits - k)
				}
				res += perm
			}
		}
		if used[d] {
			return res
		}
		used[d] = true
	}
	// n itself has all distinct digits
	return res + 1
}
```

## Ruby

```ruby
def count_special_numbers(n)
  s = n.to_s
  len = s.length

  perm = ->(m, r) {
    res = 1
    i = 0
    while i < r
      res *= (m - i)
      i += 1
    end
    res
  }

  ans = 0
  (1...len).each do |k|
    ans += 9 * perm.call(9, k - 1)
  end

  used = Array.new(10, false)
  broke = false

  (0...len).each do |i|
    cur = s.getbyte(i) - 48
    start_digit = i == 0 ? 1 : 0
    d = start_digit
    while d < cur
      unless used[d]
        remaining = len - i - 1
        avail = 10 - (i + 1)
        ans += perm.call(avail, remaining)
      end
      d += 1
    end

    if used[cur]
      broke = true
      break
    end
    used[cur] = true
  end

  ans += 1 unless broke
  ans
end
```

## Scala

```scala
object Solution {
    def countSpecialNumbers(n: Int): Int = {
        val s = n.toString
        val len = s.length
        var ans: Long = 0L

        // Count numbers with length less than len
        for (k <- 1 until len) {
            var cnt = 9L
            var available = 9
            var i = 1
            while (i < k) {
                cnt *= available
                available -= 1
                i += 1
            }
            ans += cnt
        }

        // Count numbers with the same length
        var usedMask = 0
        for (i <- 0 until len) {
            val curDigit = s.charAt(i) - '0'
            val start = if (i == 0) 1 else 0
            for (d <- start until curDigit) {
                if ((usedMask & (1 << d)) == 0) {
                    var cnt = 1L
                    var rem = len - i - 1
                    var avail = 10 - (i + 1)
                    while (rem > 0) {
                        cnt *= avail
                        avail -= 1
                        rem -= 1
                    }
                    ans += cnt
                }
            }
            if ((usedMask & (1 << curDigit)) != 0) {
                return ans.toInt
            }
            usedMask |= (1 << curDigit)
        }

        // n itself is special
        ans + 1L toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_special_numbers(n: i32) -> i32 {
        let digits: Vec<i32> = n
            .to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap() as i32)
            .collect();
        let len = digits.len();

        fn perm(mut m: i32, k: i32) -> i32 {
            let mut res = 1;
            for _ in 0..k {
                res *= m;
                m -= 1;
            }
            res
        }

        let mut total: i32 = 0;

        // numbers with fewer digits than n
        for l in 1..len {
            total += 9 * perm(9, (l - 1) as i32);
        }

        let mut used_mask: u16 = 0;
        for (i, &d) in digits.iter().enumerate() {
            let start = if i == 0 { 1 } else { 0 };
            for cand in start..d {
                if ((used_mask >> cand) & 1) == 0 {
                    let rem = (len - i - 1) as i32;
                    let avail = 10 - (i as i32) - 1; // digits left after picking cand
                    total += perm(avail, rem);
                }
            }

            if ((used_mask >> d) & 1) == 1 {
                return total;
            }
            used_mask |= 1 << d;
        }

        total + 1
    }
}
```

## Racket

```racket
(define/contract (count-special-numbers n)
  (-> exact-integer? exact-integer?)
  (let* ((digits
          (let loop ((x n) (lst '()))
            (if (= x 0)
                (list->vector (reverse lst))
                (loop (quotient x 10) (cons (remainder x 10) lst)))))
         (len (vector-length digits)))
    ;; permutation nPk
    (define (perm n k)
      (let loop ((i 0) (res 1))
        (if (= i k) res
            (loop (+ i 1) (* res (- n i))))))
    ;; count numbers with length < len
    (define less-count
      (let loop ((k 1) (acc 0))
        (if (> k len)
            acc
            (let ((cnt (* 9 (perm 9 (- k 1)))))
              (loop (+ k 1) (+ acc cnt))))))
    ;; memoization table for DP
    (define memo (make-hash))
    (define (dfs pos used tight)
      (if (= pos len)
          1
          (let* ((key (list pos used (if tight 1 0)))
                 (cached (hash-ref memo key #f)))
            (if cached
                cached
                (let* ((limit (if tight (vector-ref digits pos) 9))
                       (start (if (= pos 0) 1 0))
                       (res
                        (let loop ((d start) (sum 0))
                          (cond
                            [(> d limit) sum]
                            [else
                             (define bit (arithmetic-shift 1 d))
                             (if (zero? (bitwise-and used bit))
                                 (let ((new-used (bitwise-ior used bit)))
                                   (if (= d limit)
                                       (loop (+ d 1) (+ sum (dfs (+ pos 1) new-used tight)))
                                       (loop (+ d 1) (+ sum (dfs (+ pos 1) new-used #f)))))
                                 (loop (+ d 1) sum))]))))
                  (hash-set! memo key res)
                  res))))))
    (+ less-count (dfs 0 0 #t))))
```

## Erlang

```erlang
-module(solution).
-export([count_special_numbers/1]).

-spec count_special_numbers(N :: integer()) -> integer().
count_special_numbers(N) ->
    Digits = [C - $0 || C <- integer_to_list(N)],
    L = length(Digits),
    CountSmall = case L of
        1 -> 0;
        _ -> lists:foldl(fun(Len, Acc) -> Acc + 9 * perm(9, Len - 1) end,
                         0,
                         lists:seq(1, L - 1))
    end,
    {CountSame, _} = process(Digits, 0, 0, 0, 0),
    CountSmall + CountSame.

perm(_, 0) -> 1;
perm(A, K) when K > 0 ->
    perm_loop(A, K, 1).

perm_loop(_, 0, Acc) -> Acc;
perm_loop(A, K, Acc) ->
    perm_loop(A - 1, K - 1, Acc * A).

sum_smaller(Start, End, _Mask, _UsedCnt, _Rem) when Start > End -> 0;
sum_smaller(X, End, Mask, UsedCnt, Rem) when X =< End ->
    case (Mask band (1 bsl X)) of
        0 ->
            Avail = 10 - (UsedCnt + 1),
            Ways = perm(Avail, Rem),
            Ways + sum_smaller(X + 1, End, Mask, UsedCnt, Rem);
        _ ->
            sum_smaller(X + 1, End, Mask, UsedCnt, Rem)
    end.

process([], _Idx, _Mask, _UsedCnt, Acc) ->
    {Acc + 1, ok};
process([D | Rest], Idx, Mask, UsedCnt, Acc) ->
    Start = if Idx == 0 -> 1; true -> 0 end,
    End = D - 1,
    Rem = length(Rest),
    Add = sum_smaller(Start, End, Mask, UsedCnt, Rem),
    NewAcc = Acc + Add,
    case (Mask band (1 bsl D)) of
        0 ->
            NewMask = Mask bor (1 bsl D),
            process(Rest, Idx + 1, NewMask, UsedCnt + 1, NewAcc);
        _ ->
            {NewAcc, stop}
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_special_numbers(n :: integer) :: integer
  def count_special_numbers(n) do
    digits = Integer.digits(n)
    len = length(digits)

    # Count numbers with fewer digits than n
    ans =
      Enum.reduce(1..(len - 1), 0, fn l, acc ->
        acc + 9 * permute(9, l - 1)
      end)

    case dfs(digits, 0, 0, 0, ans) do
      {:stop, res} -> res
      {:ok, res} -> res + 1
    end
  end

  # Recursive digit DP for numbers with the same length as n
  defp dfs(_digits, idx, _mask, _used_cnt, acc) when idx == length(_digits), do: {:ok, acc}

  defp dfs(digits, idx, mask, used_cnt, acc) do
    cur = Enum.at(digits, idx)
    start = if idx == 0, do: 1, else: 0

    acc2 =
      Enum.reduce(start..(cur - 1), acc, fn d, a ->
        if (mask &&& (1 <<< d)) == 0 do
          remaining = length(digits) - idx - 1
          avail = 10 - used_cnt - 1
          a + permute(avail, remaining)
        else
          a
        end
      end)

    # If current digit already used, cannot proceed further
    if (mask &&& (1 <<< cur)) != 0 do
      {:stop, acc2}
    else
      dfs(digits, idx + 1, mask ||| (1 <<< cur), used_cnt + 1, acc2)
    end
  end

  # Permutation: P(m, k) = m * (m-1) * ... * (m-k+1)
  defp permute(_m, 0), do: 1

  defp permute(m, k) when k > 0 do
    Enum.reduce(0..(k - 1), 1, fn i, prod -> prod * (m - i) end)
  end
end
```
