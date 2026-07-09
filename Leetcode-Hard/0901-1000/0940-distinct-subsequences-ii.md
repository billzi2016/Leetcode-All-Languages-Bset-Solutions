# 0940. Distinct Subsequences II

## Cpp

```cpp
class Solution {
public:
    int distinctSubseqII(string s) {
        const int MOD = 1000000007;
        vector<long long> last(26, 0);
        long long dp = 1; // counts empty subsequence
        for (char ch : s) {
            int idx = ch - 'a';
            long long ndp = (dp * 2) % MOD;
            if (last[idx] != 0) {
                ndp = (ndp - last[idx] + MOD) % MOD;
            }
            last[idx] = dp;
            dp = ndp;
        }
        return (int)((dp - 1 + MOD) % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int distinctSubseqII(String s) {
        long[] last = new long[26];
        long dp = 1; // counts empty subsequence
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            long prevDp = dp;
            dp = (dp * 2 % MOD - last[idx] + MOD) % MOD;
            last[idx] = prevDp;
        }
        dp = (dp - 1 + MOD) % MOD; // exclude empty subsequence
        return (int) dp;
    }
}
```

## Python

```python
class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = 1  # count of subsequences including empty
        last = [0] * 26  # stores dp value before previous occurrence of each character
        for ch in s:
            idx = ord(ch) - 97
            new_dp = (dp * 2) % MOD
            if last[idx]:
                new_dp = (new_dp - last[idx]) % MOD
            last[idx] = dp
            dp = new_dp
        return (dp - 1) % MOD
```

## Python3

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty subsequence
        last = [-1] * 26  # last occurrence index in dp
        
        for i in range(1, n + 1):
            ch = s[i - 1]
            idx = ord(ch) - ord('a')
            dp[i] = (dp[i - 1] * 2) % MOD
            if last[idx] != -1:
                dp[i] = (dp[i] - dp[last[idx]]) % MOD
            last[idx] = i - 1
        
        return (dp[n] - 1) % MOD
```

## C

```c
#include <stddef.h>

int distinctSubseqII(char* s) {
    const int MOD = 1000000007;
    long long total = 1; // counts empty subsequence
    long long last[26] = {0};
    
    for (char *p = s; *p != '\0'; ++p) {
        int idx = *p - 'a';
        long long new_total = (total * 2 % MOD - last[idx] + MOD) % MOD;
        last[idx] = total;
        total = new_total;
    }
    
    int result = (int)((total - 1 + MOD) % MOD); // exclude empty subsequence
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int DistinctSubseqII(string s) {
        const int MOD = 1000000007;
        int n = s.Length;
        long[] dp = new long[n + 1];
        dp[0] = 1; // empty subsequence
        int[] last = new int[26]; // positions are 1-indexed, 0 means not seen
        
        for (int i = 1; i <= n; i++) {
            char ch = s[i - 1];
            int idx = ch - 'a';
            
            dp[i] = (dp[i - 1] * 2) % MOD;
            if (last[idx] != 0) {
                dp[i] = (dp[i] - dp[last[idx] - 1]) % MOD;
                if (dp[i] < 0) dp[i] += MOD;
            }
            last[idx] = i;
        }
        
        int result = (int)((dp[n] - 1 + MOD) % MOD); // exclude empty subsequence
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var distinctSubseqII = function(s) {
    const MOD = 1000000007;
    const last = new Array(26).fill(0);
    let dp = 1; // counts empty subsequence
    
    for (let i = 0; i < s.length; ++i) {
        const idx = s.charCodeAt(i) - 97;
        const newDp = ((dp * 2) % MOD - last[idx] + MOD) % MOD;
        last[idx] = dp;
        dp = newDp;
    }
    
    return (dp - 1 + MOD) % MOD;
};
```

## Typescript

```typescript
function distinctSubseqII(s: string): number {
    const MOD = 1000000007;
    let dp = 1; // counts empty subsequence
    const last = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        const idx = s.charCodeAt(i) - 97;
        const prev = last[idx];
        let ndp = (dp * 2) % MOD;
        if (prev !== 0) {
            ndp = (ndp - prev + MOD) % MOD;
        }
        last[idx] = dp;
        dp = ndp;
    }
    return (dp - 1 + MOD) % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function distinctSubseqII($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1; // empty subsequence

        // last occurrence positions (1-indexed), -1 means not seen
        $last = array_fill(0, 26, -1);

        for ($i = 1; $i <= $n; ++$i) {
            $cIdx = ord($s[$i - 1]) - ord('a');
            // double the count from previous step
            $dp[$i] = ($dp[$i - 1] * 2) % $mod;

            if ($last[$cIdx] != -1) {
                // subtract duplicates counted before the previous occurrence of this character
                $dp[$i] = ($dp[$i] - $dp[$last[$cIdx] - 1]) % $mod;
                if ($dp[$i] < 0) {
                    $dp[$i] += $mod;
                }
            }

            // update last occurrence (store as 1-indexed)
            $last[$cIdx] = $i;
        }

        // exclude empty subsequence
        $result = ($dp[$n] - 1) % $mod;
        if ($result < 0) {
            $result += $mod;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func distinctSubseqII(_ s: String) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var dp = [Int](repeating: 0, count: n)
        var last = [Int](repeating: -1, count: 26)
        
        for i in 0..<n {
            let c = chars[i]
            let idx = Int(c.unicodeScalars.first!.value - UnicodeScalar("a").value)
            let prev = (i == 0) ? 1 : dp[i - 1]   // includes empty subsequence
            var cur = (prev * 2) % MOD
            if last[idx] != -1 {
                let j = last[idx]
                let subtract = (j == 0) ? 1 : dp[j - 1]
                cur = (cur - subtract + MOD) % MOD
            }
            dp[i] = cur
            last[idx] = i
        }
        
        let result = (dp[n - 1] - 1 + MOD) % MOD   // exclude empty subsequence
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctSubseqII(s: String): Int {
        val MOD = 1_000_000_007L
        var dp = 1L // count of subsequences including empty
        val last = LongArray(26)
        for (ch in s) {
            val idx = ch - 'a'
            val newDp = ((dp * 2) % MOD - last[idx] + MOD) % MOD
            last[idx] = dp
            dp = newDp
        }
        return ((dp - 1 + MOD) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  int distinctSubseqII(String s) {
    List<int> last = List.filled(26, 0);
    int dp = 1; // counts empty subsequence
    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      int newDp = (dp * 2) % _mod;
      if (last[idx] != 0) {
        newDp -= last[idx];
        if (newDp < 0) newDp += _mod;
      }
      last[idx] = dp;
      dp = newDp;
    }
    int ans = dp - 1;
    if (ans < 0) ans += _mod;
    return ans;
  }
}
```

## Golang

```go
func distinctSubseqII(s string) int {
	const MOD int = 1000000007
	total := 1 // counts empty subsequence
	prev := make([]int, 26)

	for i := 0; i < len(s); i++ {
		idx := int(s[i] - 'a')
		newTotal := (total * 2) % MOD
		if prev[idx] != 0 {
			newTotal = (newTotal - prev[idx]) % MOD
			if newTotal < 0 {
				newTotal += MOD
			}
		}
		prev[idx] = total
		total = newTotal
	}

	ans := total - 1 // exclude empty subsequence
	if ans < 0 {
		ans += MOD
	}
	return ans
}
```

## Ruby

```ruby
def distinct_subseq_ii(s)
  mod = 1_000_000_007
  dp = 1
  last = Array.new(26, 0)

  s.each_byte do |b|
    idx = b - 97
    new_dp = (dp * 2) % mod
    new_dp -= last[idx]
    new_dp += mod if new_dp < 0
    last[idx] = dp
    dp = new_dp
  end

  result = dp - 1
  result += mod if result < 0
  result % mod
end
```

## Scala

```scala
object Solution {
    def distinctSubseqII(s: String): Int = {
        val MOD = 1000000007L
        val last = Array.fill[Long](26)(0L)
        var dpPrev: Long = 1L // count of subsequences including empty

        for (ch <- s) {
            val idx = ch - 'a'
            var cur = (dpPrev * 2) % MOD
            if (last(idx) != 0) {
                cur = (cur - last(idx) + MOD) % MOD
            }
            // update the contribution of this character for future repetitions
            last(idx) = dpPrev
            dpPrev = cur
        }

        ((dpPrev - 1 + MOD) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distinct_subseq_ii(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        let mut last = vec![0usize; 26]; // stores the last position (1-indexed) of each character

        for i in 1..=n {
            let ch = (bytes[i - 1] - b'a') as usize;
            dp[i] = (dp[i - 1] * 2) % MOD;
            if last[ch] != 0 {
                let j = last[ch];
                dp[i] = (dp[i] + MOD - dp[j - 1]) % MOD;
            }
            last[ch] = i;
        }

        let ans = (dp[n] + MOD - 1) % MOD; // exclude empty subsequence
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (distinct-subseq-ii s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (dp (make-vector (+ n 1) 0))
         (last (make-vector 26 -1)))
    (vector-set! dp 0 1)
    (for ([i (in-range 1 (+ n 1))])
      (let* ((ch (char->integer (string-ref s (- i 1))))
             (idx (- ch (char->integer #\a))) ; 0..25
             (prev (vector-ref dp (- i 1)))
             (val (* 2 prev))
             (lastIdx (vector-ref last idx))
             (sub (if (= lastIdx -1) 0 (vector-ref dp (- lastIdx 1))))
             (new-val (modulo (- val sub) MOD)))
        (vector-set! dp i new-val)
        (vector-set! last idx i)))
    (modulo (- (vector-ref dp n) 1) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([distinct_subseq_ii/1]).
-define(MOD, 1000000007).

-spec distinct_subseq_ii(S :: unicode:unicode_binary()) -> integer().
distinct_subseq_ii(S) ->
    Chars = binary_to_list(S),
    {DP, _} = lists:foldl(
        fun(C, {DpAcc, LastMap}) ->
            Prev = maps:get(C, LastMap, 0),
            NewDp = ((DpAcc * 2) rem ?MOD - Prev + ?MOD) rem ?MOD,
            NewLast = maps:put(C, DpAcc, LastMap),
            {NewDp, NewLast}
        end,
        {1, #{}},
        Chars
    ),
    (DP - 1 + ?MOD) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_subseq_ii(s :: String.t()) :: integer()
  def distinct_subseq_ii(s) do
    mod = 1_000_000_007
    chars = String.graphemes(s)

    {dp, _} =
      Enum.reduce(chars, {1, %{}}, fn c, {dp, last} ->
        new_dp = rem(dp * 2, mod)

        new_dp =
          case Map.fetch(last, c) do
            {:ok, val} -> rem(new_dp - val + mod, mod)
            :error -> new_dp
          end

        last = Map.put(last, c, dp)
        {new_dp, last}
      end)

    rem(dp - 1 + mod, mod)
  end
end
```
