# 2370. Longest Ideal Subsequence

## Cpp

```cpp
class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(26, 0);
        int ans = 0;
        for (char ch : s) {
            int cur = ch - 'a';
            int lo = max(0, cur - k);
            int hi = min(25, cur + k);
            int best = 0;
            for (int p = lo; p <= hi; ++p) {
                if (dp[p] > best) best = dp[p];
            }
            dp[cur] = max(dp[cur], best + 1);
            if (dp[cur] > ans) ans = dp[cur];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestIdealString(String s, int k) {
        int[] dp = new int[26];
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            int cur = s.charAt(i) - 'a';
            int best = 0;
            int start = Math.max(0, cur - k);
            int end = Math.min(25, cur + k);
            for (int p = start; p <= end; p++) {
                if (dp[p] > best) {
                    best = dp[p];
                }
            }
            int newLen = best + 1;
            if (newLen > dp[cur]) {
                dp[cur] = newLen;
            }
            if (dp[cur] > result) {
                result = dp[cur];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0] * 26
        res = 0
        for ch in s:
            idx = ord(ch) - 97
            lo = max(0, idx - k)
            hi = min(25, idx + k)
            best = 0
            for p in range(lo, hi + 1):
                if dp[p] > best:
                    best = dp[p]
            # extend the best subsequence ending with a compatible letter
            if best + 1 > dp[idx]:
                dp[idx] = best + 1
            if dp[idx] > res:
                res = dp[idx]
        return res
```

## Python3

```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        ans = 0
        for ch in s:
            cur = ord(ch) - 97
            lo = max(0, cur - k)
            hi = min(25, cur + k)
            best = 0
            for p in range(lo, hi + 1):
                if dp[p] > best:
                    best = dp[p]
            new_len = best + 1
            if new_len > dp[cur]:
                dp[cur] = new_len
            if dp[cur] > ans:
                ans = dp[cur]
        return ans
```

## C

```c
#include <stddef.h>

int longestIdealString(char* s, int k) {
    int dp[26] = {0};
    int ans = 0;
    for (char *p = s; *p != '\0'; ++p) {
        int cur = *p - 'a';
        int lo = cur - k;
        if (lo < 0) lo = 0;
        int hi = cur + k;
        if (hi > 25) hi = 25;
        int best = 0;
        for (int j = lo; j <= hi; ++j) {
            if (dp[j] > best) best = dp[j];
        }
        int newLen = best + 1;
        if (newLen > dp[cur]) dp[cur] = newLen;
        if (newLen > ans) ans = newLen;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestIdealString(string s, int k) {
        int[] dp = new int[26];
        int result = 0;
        foreach (char ch in s) {
            int cur = ch - 'a';
            int left = Math.Max(0, cur - k);
            int right = Math.Min(25, cur + k);
            int best = 0;
            for (int p = left; p <= right; ++p) {
                if (dp[p] > best) best = dp[p];
            }
            int newLen = best + 1;
            if (newLen > dp[cur]) dp[cur] = newLen;
            if (newLen > result) result = newLen;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestIdealString = function(s, k) {
    const dp = new Array(26).fill(0);
    let result = 0;
    for (let i = 0; i < s.length; ++i) {
        const cur = s.charCodeAt(i) - 97;
        let best = 0;
        const start = Math.max(0, cur - k);
        const end = Math.min(25, cur + k);
        for (let p = start; p <= end; ++p) {
            if (dp[p] > best) best = dp[p];
        }
        const newLen = best + 1;
        if (newLen > dp[cur]) dp[cur] = newLen;
        if (newLen > result) result = newLen;
    }
    return result;
};
```

## Typescript

```typescript
function longestIdealString(s: string, k: number): number {
    const dp = new Array(26).fill(0);
    let result = 0;
    for (const ch of s) {
        const c = ch.charCodeAt(0) - 97; // 'a' -> 0
        let best = 0;
        const left = Math.max(0, c - k);
        const right = Math.min(25, c + k);
        for (let p = left; p <= right; ++p) {
            if (dp[p] > best) best = dp[p];
        }
        const cand = best + 1;
        if (cand > dp[c]) dp[c] = cand;
        if (dp[c] > result) result = dp[c];
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function longestIdealString($s, $k) {
        $dp = array_fill(0, 26, 0);
        $n = strlen($s);
        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = ord($s[$i]) - 97; // ord('a') == 97
            $start = $cur - $k;
            if ($start < 0) $start = 0;
            $end = $cur + $k;
            if ($end > 25) $end = 25;

            $best = 0;
            for ($p = $start; $p <= $end; $p++) {
                if ($dp[$p] > $best) {
                    $best = $dp[$p];
                }
            }

            $newLen = $best + 1;
            if ($newLen > $dp[$cur]) {
                $dp[$cur] = $newLen;
            }
            if ($newLen > $res) {
                $res = $newLen;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func longestIdealString(_ s: String, _ k: Int) -> Int {
        var dp = Array(repeating: 0, count: 26)
        var result = 0
        for byte in s.utf8 {
            let cur = Int(byte) - 97   // 'a' ascii is 97
            var best = 0
            let low = max(0, cur - k)
            let high = min(25, cur + k)
            if low <= high {
                for p in low...high {
                    if dp[p] > best { best = dp[p] }
                }
            }
            let newLen = best + 1
            if newLen > dp[cur] {
                dp[cur] = newLen
            }
            if dp[cur] > result {
                result = dp[cur]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestIdealString(s: String, k: Int): Int {
        val dp = IntArray(26)
        var result = 0
        for (ch in s) {
            val cur = ch - 'a'
            var best = 0
            val left = if (cur - k < 0) 0 else cur - k
            val right = if (cur + k > 25) 25 else cur + k
            for (p in left..right) {
                if (dp[p] > best) best = dp[p]
            }
            val newLen = best + 1
            if (newLen > dp[cur]) dp[cur] = newLen
            if (newLen > result) result = newLen
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int longestIdealString(String s, int k) {
    List<int> dp = List.filled(26, 0);
    int res = 0;
    for (int i = 0; i < s.length; ++i) {
      int cur = s.codeUnitAt(i) - 97;
      int start = (cur - k).clamp(0, 25);
      int end = (cur + k).clamp(0, 25);
      int best = 0;
      for (int p = start; p <= end; ++p) {
        if (dp[p] > best) best = dp[p];
      }
      int newLen = best + 1;
      if (newLen > dp[cur]) dp[cur] = newLen;
      if (newLen > res) res = newLen;
    }
    return res;
  }
}
```

## Golang

```go
func longestIdealString(s string, k int) int {
    dp := make([]int, 26)
    res := 0
    for i := 0; i < len(s); i++ {
        cur := int(s[i] - 'a')
        best := 0
        start := cur - k
        if start < 0 {
            start = 0
        }
        end := cur + k
        if end > 25 {
            end = 25
        }
        for p := start; p <= end; p++ {
            if dp[p] > best {
                best = dp[p]
            }
        }
        if best+1 > dp[cur] {
            dp[cur] = best + 1
        }
        if dp[cur] > res {
            res = dp[cur]
        }
    }
    return res
}
```

## Ruby

```ruby
def longest_ideal_string(s, k)
  dp = Array.new(26, 0)
  base = 'a'.ord
  s.each_char do |ch|
    idx = ch.ord - base
    left = [0, idx - k].max
    right = [25, idx + k].min
    best = 0
    (left..right).each { |j| best = dp[j] if dp[j] > best }
    new_len = best + 1
    dp[idx] = new_len if new_len > dp[idx]
  end
  dp.max
end
```

## Scala

```scala
object Solution {
    def longestIdealString(s: String, k: Int): Int = {
        val dp = new Array[Int](26)
        var res = 0
        for (ch <- s) {
            val cur = ch - 'a'
            var best = 0
            var j = Math.max(0, cur - k)
            val limit = Math.min(25, cur + k)
            while (j <= limit) {
                if (dp(j) > best) best = dp(j)
                j += 1
            }
            val newLen = best + 1
            if (newLen > dp(cur)) dp(cur) = newLen
            if (dp(cur) > res) res = dp(cur)
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = [0i32; 26];
        let mut ans = 0i32;
        for byte in s.bytes() {
            let cur = (byte - b'a') as usize;
            let start = if cur >= k { cur - k } else { 0 };
            let end = std::cmp::min(25, cur + k);
            let mut best = 0i32;
            for p in start..=end {
                if dp[p] > best {
                    best = dp[p];
                }
            }
            let new_len = best + 1;
            if new_len > dp[cur] {
                dp[cur] = new_len;
            }
            if dp[cur] > ans {
                ans = dp[cur];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-ideal-string s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (dp (make-vector 26 0))
         (k (min k 25)))
    (let loop ((i 0) (ans 0))
      (if (= i n)
          ans
          (let* ((c (string-ref s i))
                 (idx (- (char->integer c) (char->integer #\a)))
                 (low (max 0 (- idx k)))
                 (high (min 25 (+ idx k)))
                 (best (for/fold ([b 0])
                         ([j (in-range low (add1 high))])
                       (max b (vector-ref dp j))))
                 (newlen (+ best 1))
                 (old (vector-ref dp idx)))
            (when (> newlen old)
              (vector-set! dp idx newlen))
            (loop (add1 i) (if (> newlen ans) newlen ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_ideal_string/2]).

-spec longest_ideal_string(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_ideal_string(S, K) ->
    DP0 = erlang:make_tuple(26, 0),
    process(S, K, DP0, 0).

process(<<>>, _K, _DP, Res) ->
    Res;
process(<<Char, Rest/binary>>, K, DP, Res) ->
    CurrIdx = Char - $a,
    Best = max_in_range(DP, CurrIdx, K),
    NewVal = Best + 1,
    NewDP = setelement(CurrIdx+1, DP, NewVal),
    NewRes = erlang:max(Res, NewVal),
    process(Rest, K, NewDP, NewRes).

max_in_range(DP, CurrIdx, K) ->
    Low = erlang:max(0, CurrIdx - K),
    High = erlang:min(25, CurrIdx + K),
    max_in_range_loop(DP, Low, High, 0).

max_in_range_loop(_DP, I, High, Max) when I > High ->
    Max;
max_in_range_loop(DP, I, High, Max) ->
    Val = element(I+1, DP),
    NewMax = if Val > Max -> Val; true -> Max end,
    max_in_range_loop(DP, I+1, High, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_ideal_string(s :: String.t(), k :: integer) :: integer
  def longest_ideal_string(s, k) do
    dp = Tuple.duplicate(0, 26)

    {_dp_final, result} =
      s
      |> String.to_charlist()
      |> Enum.reduce({dp, 0}, fn char, {dp_acc, ans} ->
        idx = char - ?a
        low = max(0, idx - k)
        high = min(25, idx + k)

        best =
          Enum.reduce(low..high, 0, fn p, acc ->
            val = elem(dp_acc, p)
            if val > acc, do: val, else: acc
          end)

        new_len = best + 1
        cur = elem(dp_acc, idx)
        dp_new = if new_len > cur, do: put_elem(dp_acc, idx, new_len), else: dp_acc
        ans_new = if new_len > ans, do: new_len, else: ans

        {dp_new, ans_new}
      end)

    result
  end
end
```
