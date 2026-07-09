# 1422. Maximum Score After Splitting a String

## Cpp

```cpp
class Solution {
public:
    int maxScore(string s) {
        int totalOnes = 0;
        for (char c : s) if (c == '1') ++totalOnes;
        int zeros = 0, ones = totalOnes, ans = 0;
        for (int i = 0; i < (int)s.size() - 1; ++i) {
            if (s[i] == '0')
                ++zeros;
            else
                --ones;
            ans = max(ans, zeros + ones);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxScore(String s) {
        int totalOnes = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') totalOnes++;
        }
        int zeros = 0, ones = totalOnes, ans = 0;
        // split point is after index i, so i goes up to length-2
        for (int i = 0; i < s.length() - 1; i++) {
            char c = s.charAt(i);
            if (c == '0') {
                zeros++;
            } else { // c == '1'
                ones--;
            }
            ans = Math.max(ans, zeros + ones);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = 0
        ans = 0
        # iterate up to the second last character to ensure non-empty right part
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans
```

## Python3

```python
class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        zeros = 0
        ones_right = total_ones
        max_score = 0
        # split after each position except the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones_right -= 1
            current = zeros + ones_right
            if current > max_score:
                max_score = current
        return max_score
```

## C

```c
#include <string.h>

int maxScore(char* s) {
    int totalOnes = 0;
    for (char *p = s; *p; ++p)
        if (*p == '1')
            ++totalOnes;

    int zeros = 0, ones = totalOnes, ans = 0;
    int len = strlen(s);
    for (int i = 0; i < len - 1; ++i) {
        if (s[i] == '1')
            --ones;
        else
            ++zeros;
        int cur = zeros + ones;
        if (cur > ans)
            ans = cur;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxScore(string s) {
        int totalOnes = 0;
        foreach (char c in s) {
            if (c == '1') totalOnes++;
        }
        int zeros = 0, ones = totalOnes, ans = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            if (s[i] == '0') {
                zeros++;
            } else {
                ones--;
            }
            ans = Math.Max(ans, zeros + ones);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let totalOnes = 0;
    for (let ch of s) {
        if (ch === '1') totalOnes++;
    }
    let zeros = 0;
    let onesRight = totalOnes;
    let ans = 0;
    // split point is after index i, i ranges from 0 to n-2
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === '0') {
            zeros++;
        } else {
            onesRight--;
        }
        ans = Math.max(ans, zeros + onesRight);
    }
    return ans;
};
```

## Typescript

```typescript
function maxScore(s: string): number {
    let totalOnes = 0;
    for (const ch of s) {
        if (ch === '1') totalOnes++;
    }
    let zeros = 0;
    let onesRight = totalOnes;
    let ans = 0;
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === '0') {
            zeros++;
        } else {
            onesRight--;
        }
        const score = zeros + onesRight;
        if (score > ans) ans = score;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxScore($s) {
        $totalOnes = substr_count($s, '1');
        $zerosLeft = 0;
        $maxScore = 0;
        $n = strlen($s);
        // split point is after index i, so i goes up to n-2
        for ($i = 0; $i < $n - 1; $i++) {
            if ($s[$i] === '1') {
                $totalOnes--;
            } else { // '0'
                $zerosLeft++;
            }
            $current = $zerosLeft + $totalOnes;
            if ($current > $maxScore) {
                $maxScore = $current;
            }
        }
        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ s: String) -> Int {
        let chars = Array(s)
        var totalOnes = 0
        for ch in chars {
            if ch == "1" { totalOnes += 1 }
        }
        var zeros = 0
        var ones = totalOnes
        var ans = 0
        for i in 0..<(chars.count - 1) {
            if chars[i] == "1" {
                ones -= 1
            } else {
                zeros += 1
            }
            ans = max(ans, zeros + ones)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(s: String): Int {
        var totalOnes = 0
        for (ch in s) {
            if (ch == '1') totalOnes++
        }
        var zeros = 0
        var onesRight = totalOnes
        var ans = 0
        val n = s.length
        for (i in 0 until n - 1) {
            if (s[i] == '0') {
                zeros++
            } else {
                onesRight--
            }
            val score = zeros + onesRight
            if (score > ans) ans = score
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(String s) {
    int totalOnes = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') totalOnes++;
    }

    int zeros = 0;
    int onesRight = totalOnes;
    int ans = 0;

    // split after each position except the last character
    for (int i = 0; i < s.length - 1; i++) {
      if (s[i] == '0') {
        zeros++;
      } else {
        onesRight--;
      }
      int cur = zeros + onesRight;
      if (cur > ans) ans = cur;
    }

    return ans;
  }
}
```

## Golang

```go
func maxScore(s string) int {
    totalOnes := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '1' {
            totalOnes++
        }
    }

    zeros, onesRight := 0, totalOnes
    ans := 0

    // split after each position except the last character
    for i := 0; i < len(s)-1; i++ {
        if s[i] == '0' {
            zeros++
        } else { // s[i] == '1'
            onesRight--
        }
        score := zeros + onesRight
        if score > ans {
            ans = score
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_score(s)
  total_ones = s.count('1')
  zeros = 0
  ones_right = total_ones
  best = 0
  s.each_char.with_index do |ch, i|
    break if i == s.length - 1
    if ch == '0'
      zeros += 1
    else
      ones_right -= 1
    end
    score = zeros + ones_right
    best = score if score > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def maxScore(s: String): Int = {
        var totalOnes = 0
        for (ch <- s) if (ch == '1') totalOnes += 1

        var zerosLeft = 0
        var onesRight = totalOnes
        var best = 0

        // iterate up to second last character to ensure non‑empty right part
        for (i <- 0 until s.length - 1) {
            if (s.charAt(i) == '0') zerosLeft += 1
            else onesRight -= 1
            val score = zerosLeft + onesRight
            if (score > best) best = score
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(s: String) -> i32 {
        let bytes = s.as_bytes();
        // total number of '1's in the whole string
        let mut ones_right: i32 = bytes.iter().filter(|&&c| c == b'1').count() as i32;
        let mut zeros_left: i32 = 0;
        let mut best: i32 = 0;

        // split after each position except the last character
        for i in 0..bytes.len() - 1 {
            if bytes[i] == b'0' {
                zeros_left += 1;
            } else {
                ones_right -= 1;
            }
            let score = zeros_left + ones_right;
            if score > best {
                best = score;
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (max-score s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         ;; count total number of '1's in the whole string
         (total-ones (let loop ((i 0) (cnt 0))
                       (if (= i len)
                           cnt
                           (loop (+ i 1)
                                 (if (char=? (string-ref s i) #\1)
                                     (+ cnt 1)
                                     cnt)))))
         (ans 0)
         (zeros 0)
         (ones total-ones))
    ;; iterate possible split positions; stop before the last character
    (let loop ((i 0) (best ans) (z zeros) (o ones))
      (if (= i (- len 1))
          best
          (let* ((c (string-ref s i))
                 (new-z (if (char=? c #\0) (+ z 1) z))
                 (new-o (if (char=? c #\1) (- o 1) o))
                 (score (+ new-z new-o))
                 (new-best (if (> score best) score best)))
            (loop (+ i 1) new-best new-z new-o))))))
```

## Erlang

```erlang
-module(solution).
-export([max_score/1]).

-spec max_score(S :: unicode:unicode_binary()) -> integer().
max_score(S) ->
    List = binary_to_list(S),
    TotalOnes = count_ones(List, 0),
    Len = length(List),
    PrefixLen = Len - 1,
    Prefix = lists:sublist(List, PrefixLen),
    loop(Prefix, 0, TotalOnes, 0).

count_ones([], Acc) -> Acc;
count_ones([H|T], Acc) ->
    NewAcc = if H == $1 -> Acc + 1; true -> Acc end,
    count_ones(T, NewAcc).

loop([], _Zeros, _OnesRight, MaxScore) ->
    MaxScore;
loop([Char|Rest], Zeros, OnesRight, MaxScore) ->
    NewZeros = case Char of
        $0 -> Zeros + 1;
        _ -> Zeros
    end,
    NewOnesRight = case Char of
        $1 -> OnesRight - 1;
        _ -> OnesRight
    end,
    Score = NewZeros + NewOnesRight,
    NewMax = if Score > MaxScore -> Score; true -> MaxScore end,
    loop(Rest, NewZeros, NewOnesRight, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(s :: String.t) :: integer
  def max_score(s) do
    chars = String.to_charlist(s)
    total_ones = Enum.count(chars, fn c -> c == ?1 end)
    len = length(chars)

    {_zeros, _ones, best, _} =
      Enum.reduce(Enum.with_index(chars), {0, total_ones, 0, 0}, fn
        {ch, idx}, {zeros, ones, cur_best, _prev_idx} when idx < len - 1 ->
          if ch == ?0 do
            new_zeros = zeros + 1
            new_ones = ones
            new_best = max(cur_best, new_zeros + new_ones)
            {new_zeros, new_ones, new_best, idx}
          else
            # ch == ?1
            new_zeros = zeros
            new_ones = ones - 1
            new_best = max(cur_best, new_zeros + new_ones)
            {new_zeros, new_ones, new_best, idx}
          end

        _, acc ->
          acc
      end)

    best
  end
end
```
