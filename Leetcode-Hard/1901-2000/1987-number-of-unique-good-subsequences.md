# 1987. Number of Unique Good Subsequences

## Cpp

```cpp
class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        const long long MOD = 1000000007LL;
        long long dp = 0;                 // total distinct good subsequences
        bool hasZero = false, hasOne = false;
        long long extPrev[2] = {0, 0};    // extensions added at last occurrence of '0' and '1'
        
        for (char ch : binary) {
            int idx = ch - '0';
            
            // number of extendable subsequences (all except the single "0")
            long long ext = (dp - (hasZero ? 1LL : 0LL) + MOD) % MOD;
            
            // add the single character if it hasn't appeared yet
            long long addSingle = 0;
            if (idx == 0) {
                if (!hasZero) addSingle = 1;
            } else {
                if (!hasOne) addSingle = 1;
            }
            
            long long newAdd = (ext + addSingle) % MOD;   // total new subsequences this step would create
            long long dup = extPrev[idx];                 // duplicates from previous same character
            
            dp = (dp + newAdd - dup) % MOD;
            if (dp < 0) dp += MOD;
            
            // update flags and stored extension count for future duplicate removal
            if (idx == 0) hasZero = true; else hasOne = true;
            extPrev[idx] = ext;   // only extensions are subject to duplication
        }
        return static_cast<int>(dp);
    }
};
```

## Java

```java
class Solution {
    public int numberOfUniqueGoodSubsequences(String binary) {
        final long MOD = 1_000_000_007L;
        long dp = 0; // count of distinct good subsequences that start with '1'
        long[] prevAdd = new long[2]; // previous addition for '0' and '1'
        boolean hasZero = false;

        for (int i = 0; i < binary.length(); i++) {
            char ch = binary.charAt(i);
            int idx = ch - '0';
            if (ch == '0') hasZero = true;

            long add;
            if (ch == '1') {
                add = (dp + 1) % MOD; // append to existing plus the single "1"
            } else { // ch == '0'
                add = dp % MOD; // can only extend sequences that already start with '1'
            }

            long total = (dp + add - prevAdd[idx]) % MOD;
            if (total < 0) total += MOD;

            dp = total;
            prevAdd[idx] = add;
        }

        if (hasZero) {
            dp = (dp + 1) % MOD; // the subsequence "0"
        }
        return (int) dp;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MOD = 10**9 + 7
        dp0 = 0  # count of distinct good subseqs that end with '0' (includes the single "0")
        dp1 = 0  # count of distinct good subseqs that end with '1'
        have_zero = False  # whether we have seen a '0' (so "0" exists in the set)
        last_base = [0, 0]   # previous base value for each character ('0' index 0, '1' index 1)

        for ch in binary:
            idx = ord(ch) - 48  # 0 or 1
            # number of existing good subseqs (excluding the single "0") that can be extended,
            # plus the empty subsequence.
            base = (dp0 + dp1 - (1 if have_zero else 0) + 1) % MOD

            new_cnt = (base - last_base[idx]) % MOD

            if idx == 0:
                dp0 = (dp0 + new_cnt) % MOD
                have_zero = True
            else:
                dp1 = (dp1 + new_cnt) % MOD

            last_base[idx] = base

        return (dp0 + dp1) % MOD
```

## Python3

```python
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        n = len(binary)
        dp = [0] * (n + 1)          # dp[i]: distinct good subseqs (starting with '1') using first i chars
        last = {'0': -1, '1': -1}   # last occurrence position (1-indexed)

        for i, ch in enumerate(binary, 1):
            add = 1 if ch == '1' else 0
            dup = 0
            prev = last[ch]
            if prev != -1:
                dup = dp[prev - 1]
                if ch == '1':
                    dup += 1
            cur = (2 * dp[i - 1] + add - dup) % MOD
            dp[i] = cur
            last[ch] = i

        ans = dp[n]
        if '0' in binary:
            ans = (ans + 1) % MOD   # the single subsequence "0"
        return ans
```

## C

```c
#include <string.h>
#define MOD 1000000007LL

long long distinctSubseq(char *s, int start, int end) {
    long long dp = 1; // empty subsequence
    long long last[2];
    last[0] = last[1] = -1;
    for (int i = start; i < end; ++i) {
        int c = s[i] - '0';
        long long ndp = (dp * 2) % MOD;
        if (last[c] != -1) {
            ndp = (ndp - last[c] + MOD) % MOD;
        }
        last[c] = dp;
        dp = ndp;
    }
    return dp; // includes empty subsequence
}

int numberOfUniqueGoodSubsequences(char* binary) {
    int n = strlen(binary);
    
    long long totalAll = distinctSubseq(binary, 0, n);          // includes empty
    long long totalNonEmpty = (totalAll - 1 + MOD) % MOD;       // exclude empty
    
    int firstZero = -1;
    for (int i = 0; i < n; ++i) {
        if (binary[i] == '0') { firstZero = i; break; }
    }
    
    if (firstZero == -1) return (int)totalNonEmpty; // no leading-zero issue
    
    long long suffixAll = distinctSubseq(binary, firstZero + 1, n); // includes empty
    long long invalid = (suffixAll - 1 + MOD) % MOD;                // non‑empty strings that start with '0'
    
    long long ans = (totalNonEmpty - invalid + MOD) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int NumberOfUniqueGoodSubsequences(string binary) {
        const int MOD = 1_000_000_007;
        long[] last = new long[2]; // contributions for '0' and '1'
        long total = 0; // distinct good subsequences that start with '1'
        bool hasZero = false;

        foreach (char ch in binary) {
            int bit = ch - '0';
            if (bit == 0) hasZero = true;

            long add = (total + (bit == 1 ? 1 : 0) - last[bit]) % MOD;
            if (add < 0) add += MOD;

            total = (total + add) % MOD;

            long prevTotal = (total - add) % MOD;
            if (prevTotal < 0) prevTotal += MOD;

            long newLast = (prevTotal + (bit == 1 ? 1 : 0)) % MOD;
            last[bit] = newLast;
        }

        long ans = total;
        if (hasZero) {
            ans = (ans + 1) % MOD; // include the subsequence "0"
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} binary
 * @return {number}
 */
var numberOfUniqueGoodSubsequences = function(binary) {
    const MOD = 1000000007;
    let dp = 0; // distinct good subsequences that start with '1'
    const last = { '0': 0, '1': 0 }; // contribution added at previous occurrence
    let hasZero = false;

    for (const ch of binary) {
        if (ch === '0') hasZero = true;
        const add = dp + (ch === '1' ? 1 : 0); // new strings contributed this step before modulo
        let newDp = (dp * 2 + (ch === '1' ? 1 : 0)) % MOD;
        newDp = (newDp - last[ch] + MOD) % MOD; // remove duplicates
        last[ch] = add % MOD; // store contribution for future duplicate removal
        dp = newDp;
    }

    let ans = dp;
    if (hasZero) {
        ans = (ans + 1) % MOD; // include the subsequence "0"
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfUniqueGoodSubsequences(binary: string): number {
    const MOD = 1_000_000_007;
    let dp = 0; // distinct good subsequences that start with '1'
    let lastZero = 0; // contribution when last '0' was seen
    let lastOne = 0;  // contribution when last '1' was seen

    for (const ch of binary) {
        const add = ch === '1' ? 1 : 0;
        let newDp = (dp * 2 + add) % MOD;

        if (ch === '0') {
            if (lastZero !== 0) {
                newDp = (newDp - lastZero + MOD) % MOD;
            }
            // store contribution for future duplicate removal
            lastZero = (dp + add) % MOD; // add is 0 here
        } else { // ch === '1'
            if (lastOne !== 0) {
                newDp = (newDp - lastOne + MOD) % MOD;
            }
            lastOne = (dp + add) % MOD; // dp + 1
        }

        dp = newDp;
    }

    const hasZero = binary.includes('0') ? 1 : 0;
    return (dp + hasZero) % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param String $binary
     * @return Integer
     */
    function numberOfUniqueGoodSubsequences($binary) {
        $MOD = 1000000007;
        // total distinct non‑empty subsequences
        $dp = 1;                     // count of distinct subseqs including empty
        $last = [0, 0];              // previous dp value when '0' or '1' was seen
        $n = strlen($binary);
        for ($i = 0; $i < $n; ++$i) {
            $c = intval($binary[$i]);
            $newDp = ($dp * 2) % $MOD;
            if ($last[$c] != 0) {
                $newDp = ($newDp - $last[$c]) % $MOD;
                if ($newDp < 0) $newDp += $MOD;
            }
            $last[$c] = $dp;
            $dp = $newDp;
        }
        $totalDistinctNonEmpty = ($dp - 1) % $MOD;
        if ($totalDistinctNonEmpty < 0) $totalDistinctNonEmpty += $MOD;

        // find first zero
        $posZero = strpos($binary, '0');
        if ($posZero === false) {
            return $totalDistinctNonEmpty;   // no zero, all subseqs are good
        }

        // distinct subsequences (including empty) of suffix after the first zero
        $suffix = substr($binary, $posZero + 1);
        $dp2 = 1;
        $last2 = [0, 0];
        $len2 = strlen($suffix);
        for ($i = 0; $i < $len2; ++$i) {
            $c = intval($suffix[$i]);
            $newDp2 = ($dp2 * 2) % $MOD;
            if ($last2[$c] != 0) {
                $newDp2 = ($newDp2 - $last2[$c]) % $MOD;
                if ($newDp2 < 0) $newDp2 += $MOD;
            }
            $last2[$c] = $dp2;
            $dp2 = $newDp2;
        }
        $startZero = $dp2;   // includes empty subsequence

        $ans = ($totalDistinctNonEmpty - $startZero + 1) % $MOD;
        if ($ans < 0) $ans += $MOD;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfUniqueGoodSubsequences(_ binary: String) -> Int {
        let MOD = 1_000_000_007
        var dp = 0               // count of distinct good subsequences that start with '1'
        var hasZero = false      // whether there is at least one '0' in the string
        var last = [Int](repeating: 0, count: 2)   // contributions for ending with '0' and '1'
        
        for ch in binary {
            if ch == "0" {
                hasZero = true
                let idx = 0
                var add = dp % MOD               // (dp + 0)
                add = (add - last[idx] + MOD) % MOD
                last[idx] = dp % MOD
                dp = (dp + add) % MOD
            } else { // ch == '1'
                let idx = 1
                var add = (dp + 1) % MOD         // (dp + 1) for single "1"
                add = (add - last[idx] + MOD) % MOD
                last[idx] = (dp + 1) % MOD
                dp = (dp + add) % MOD
            }
        }
        
        let result = (dp + (hasZero ? 1 : 0)) % MOD
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    private fun distinctIncludingEmpty(s: String): Long {
        val n = s.length
        val dp = LongArray(n + 1)
        dp[0] = 1L
        val last = IntArray(2) { -1 }
        for (i in 1..n) {
            val idx = s[i - 1] - '0'
            var cur = (dp[i - 1] * 2) % MOD
            if (last[idx] != -1) {
                cur = (cur - dp[last[idx] - 1] + MOD) % MOD
            }
            dp[i] = cur
            last[idx] = i
        }
        return dp[n]
    }

    fun numberOfUniqueGoodSubsequences(binary: String): Int {
        val totalAll = distinctIncludingEmpty(binary)
        var totalNonEmpty = (totalAll - 1 + MOD) % MOD

        val firstZeroIdx = binary.indexOf('0')
        if (firstZeroIdx == -1) {
            return totalNonEmpty.toInt()
        }

        val suffix = if (firstZeroIdx + 1 < binary.length) binary.substring(firstZeroIdx + 1) else ""
        val startZeroCount = distinctIncludingEmpty(suffix) // includes empty subsequence

        var ans = (totalNonEmpty - startZeroCount + MOD) % MOD
        ans = (ans + 1) % MOD   // add back the single "0"
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int numberOfUniqueGoodSubsequences(String binary) {
    int dp = 0; // count of distinct good subsequences that start with '1'
    List<int> prevAdd = [0, 0]; // previous contribution for '0' and '1'
    bool hasZero = false;

    for (int i = 0; i < binary.length; ++i) {
      int ch = binary.codeUnitAt(i) - 48; // 0 or 1
      if (ch == 0) hasZero = true;

      int add = dp;
      if (ch == 1) {
        add = (add + 1) % _MOD; // can start a new subsequence "1"
      }
      add = (add - prevAdd[ch]) % _MOD;
      if (add < 0) add += _MOD;

      int dpBefore = dp;
      dp = (dp + add) % _MOD;

      // store contribution for future duplicate removal
      int startFlag = (ch == 1) ? 1 : 0;
      prevAdd[ch] = (dpBefore + startFlag) % _MOD;
    }

    int ans = dp;
    if (hasZero) {
      ans = (ans + 1) % _MOD; // add the subsequence "0"
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfUniqueGoodSubsequences(binary string) int {
	const MOD int64 = 1000000007
	n := len(binary)

	// total distinct subsequences (including empty)
	dp := int64(1)
	last := [2]int64{-1, -1}
	for i := 0; i < n; i++ {
		c := binary[i] - '0'
		cur := (dp * 2) % MOD
		if last[c] != -1 {
			cur = (cur - last[c] + MOD) % MOD
		}
		last[c] = dp
		dp = cur
	}
	totalNonEmpty := (dp - 1 + MOD) % MOD

	// find first zero
	pos := -1
	for i := 0; i < n; i++ {
		if binary[i] == '0' {
			pos = i
			break
		}
	}
	if pos == -1 {
		return int(totalNonEmpty)
	}

	// distinct subsequences of suffix after first zero (including empty)
	dpS := int64(1)
	lastS := [2]int64{-1, -1}
	for i := pos + 1; i < n; i++ {
		c := binary[i] - '0'
		cur := (dpS * 2) % MOD
		if lastS[c] != -1 {
			cur = (cur - lastS[c] + MOD) % MOD
		}
		lastS[c] = dpS
		dpS = cur
	}
	invalidCount := (dpS - 1 + MOD) % MOD

	ans := (totalNonEmpty - invalidCount + MOD) % MOD
	return int(ans)
}
```

## Ruby

```ruby
def number_of_unique_good_subsequences(binary)
  mod = 1_000_000_007
  total = 1                     # includes empty subsequence
  last_add = { '0' => 0, '1' => 0 }
  has_zero = false

  binary.each_char do |ch|
    if ch == '1'
      add = total % mod
    else
      add = (total - 1) % mod   # cannot prepend to empty
      has_zero = true
    end

    new_total = (total + add) % mod
    dup = last_add[ch]
    new_total = (new_total - dup) % mod

    last_add[ch] = add
    total = new_total
  end

  ans = (total - 1) % mod        # remove empty subsequence
  ans = (ans + 1) % mod if has_zero   # add the single "0" if any zero exists
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfUniqueGoodSubsequences(binary: String): Int = {
        val MOD = 1000000007L
        var goodStart1 = 0L               // count of distinct good subsequences that start with '1'
        var lastZeroG = 0L                // goodStart1 value at previous occurrence of '0'
        var prevTotalOne = 0L             // total (good + empty) before previous occurrence of '1'
        var hasZero = false

        for (ch <- binary) {
            if (ch == '0') {
                hasZero = true
                val newG = ((2 * goodStart1 % MOD - lastZeroG + MOD) % MOD)
                lastZeroG = goodStart1
                goodStart1 = newG
            } else { // ch == '1'
                val total = (goodStart1 + 1) % MOD          // include empty subsequence
                var newTotal = ((2 * total % MOD - prevTotalOne + MOD) % MOD)
                prevTotalOne = total
                goodStart1 = (newTotal - 1 + MOD) % MOD     // remove empty from count
            }
        }

        val answer = (goodStart1 + (if (hasZero) 1 else 0)) % MOD
        answer.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_unique_good_subsequences(binary: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut dp: i64 = 0;
        let mut last = [0i64; 2];
        let mut has_zero = false;

        for ch in binary.bytes() {
            let idx = (ch - b'0') as usize;
            if idx == 0 {
                has_zero = true;
            }
            let add = (dp + if idx == 1 { 1 } else { 0 }) % MOD;
            dp = (dp + add - last[idx] + MOD) % MOD;
            last[idx] = add;
        }

        let mut ans = dp;
        if has_zero {
            ans = (ans + 1) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-unique-good-subsequences binary)
  (-> string? exact-integer?)
  (let* ((MOD 1000000007)
         (n (string-length binary))
         (startOne 1)               ; includes empty subsequence
         (prevStartZero 0)
         (seenZero #f)
         (prevStartOne 0)
         (seenOne #f)
         (hasZero #f))
    (for ([i n])
      (let ((ch (string-ref binary i))
            (old startOne))
        (cond
          [(char=? ch #\1)
           (define dup (if seenOne prevStartOne 0))
           (define new (modulo (- (* 2 old) dup) MOD))
           (set! prevStartOne old)
           (set! seenOne #t)
           (set! startOne new)]
          [else ; ch == #\0
           (set! hasZero #t)
           (define dup (if seenZero (- prevStartZero 1) 0))
           (define new (modulo (- (- (* 2 old) 1) dup) MOD))
           (set! prevStartZero old)
           (set! seenZero #t)
           (set! startOne new)])))
    (let* ((dp1 (modulo (- startOne 1) MOD))
           (ans (+ dp1 (if hasZero 1 0))))
      (modulo ans MOD))))
```

## Erlang

```erlang
-spec number_of_unique_good_subsequences(Binary :: unicode:unicode_binary()) -> integer().
number_of_unique_good_subsequences(Binary) ->
    Mod = 1000000007,
    %% DP accumulates count of distinct good subsequences that start with '1'
    Fun =
        fun(F, <<>>, DPAcc, _Prev0, _Prev1, HasZero) ->
                {DPAcc, HasZero};
            (F, <<C, Rest/binary>>, DPAcc, Prev0, Prev1, HasZero) ->
                NewHasZero = HasZero orelse (C == $0),
                case C of
                    $0 ->
                        NewDP = (DPAcc * 2) rem Mod,
                        AdjustedDP =
                            case Prev0 of
                                undefined -> NewDP;
                                _ -> (NewDP - Prev0 + Mod) rem Mod
                            end,
                        F(F, Rest, AdjustedDP, DPAcc, Prev1, NewHasZero);
                    $1 ->
                        NewDP0 = (DPAcc * 2) rem Mod,
                        AddOne =
                            case Prev1 of
                                undefined -> 1;
                                _ -> 0
                            end,
                        NewDP1 = (NewDP0 + AddOne) rem Mod,
                        AdjustedDP =
                            case Prev1 of
                                undefined -> NewDP1;
                                _ -> (NewDP1 - Prev1 + Mod) rem Mod
                            end,
                        F(F, Rest, AdjustedDP, Prev0, DPAcc, NewHasZero)
                end
        end,
    {DPFinal, HasZ} = Fun(Fun, Binary, 0, undefined, undefined, false),
    (DPFinal + if HasZ -> 1; true -> 0 end) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec number_of_unique_good_subsequences(binary :: String.t()) :: integer
  def number_of_unique_good_subsequences(binary) do
    mod = 1_000_000_007

    {dp0, dp1, _last0, _last1, has_zero} =
      Enum.reduce(String.to_charlist(binary), {0, 0, 0, 0, false}, fn c,
                                                                   {dp0, dp1, last0, last1, has_zero} ->
        total = rem(dp0 + dp1, mod)

        if c == ?0 do
          # new good subsequences ending with '0' (starting with '1')
          add = total - last0
          add = if add < 0, do: add + mod, else: add
          dp0_new = rem(dp0 + add, mod)
          {dp0_new, dp1, total, last1, true}
        else
          # c == ?1
          # new good subsequences ending with '1' (starting with '1')
          add = (total + 1) - last1
          add = if add < 0, do: add + mod, else: add
          dp1_new = rem(dp1 + add, mod)
          {dp0, dp1_new, last0, total + 1, has_zero}
        end
      end)

    ans = dp0 + dp1
    ans = if has_zero, do: ans + 1, else: ans
    rem(ans, mod)
  end
end
```
