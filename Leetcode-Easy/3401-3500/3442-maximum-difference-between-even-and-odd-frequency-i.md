# 3442. Maximum Difference Between Even and Odd Frequency I

## Cpp

```cpp
class Solution {
public:
    int maxDifference(string s) {
        int cnt[26] = {0};
        for (char c : s) cnt[c - 'a']++;
        int maxOdd = 0;
        int minEven = INT_MAX;
        for (int f : cnt) {
            if (f == 0) continue;
            if (f % 2) {
                if (f > maxOdd) maxOdd = f;
            } else {
                if (f < minEven) minEven = f;
            }
        }
        return maxOdd - minEven;
    }
};
```

## Java

```java
class Solution {
    public int maxDifference(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        int maxOdd = Integer.MIN_VALUE;
        int minEven = Integer.MAX_VALUE;
        for (int count : freq) {
            if (count == 0) continue;
            if ((count & 1) == 1) { // odd
                if (count > maxOdd) maxOdd = count;
            } else { // even
                if (count < minEven) minEven = count;
            }
        }
        return maxOdd - minEven;
    }
}
```

## Python

```python
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = -1
        min_even = float('inf')
        for f in freq:
            if f == 0:
                continue
            if f % 2 == 1:
                if f > max_odd:
                    max_odd = f
            else:
                if f < min_even:
                    min_even = f

        return max_odd - min_even
```

## Python3

```python
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = -10**9
        min_even = 10**9
        for f in freq:
            if f == 0:
                continue
            if f & 1:
                if f > max_odd:
                    max_odd = f
            else:
                if f < min_even:
                    min_even = f

        return max_odd - min_even
```

## C

```c
#include <limits.h>

int maxDifference(char* s) {
    int freq[26] = {0};
    for (char *p = s; *p != '\0'; ++p) {
        freq[*p - 'a']++;
    }
    
    int maxOdd = -1;
    int minEven = INT_MAX;
    
    for (int i = 0; i < 26; ++i) {
        if (freq[i] == 0) continue;
        if (freq[i] % 2 == 1) {
            if (freq[i] > maxOdd) maxOdd = freq[i];
        } else {
            if (freq[i] < minEven) minEven = freq[i];
        }
    }
    
    return maxOdd - minEven;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxDifference(string s)
    {
        int[] cnt = new int[26];
        foreach (char c in s)
        {
            cnt[c - 'a']++;
        }

        int maxOdd = int.MinValue;
        int minEven = int.MaxValue;

        foreach (int f in cnt)
        {
            if (f == 0) continue;
            if ((f & 1) == 1) // odd
            {
                if (f > maxOdd) maxOdd = f;
            }
            else // even
            {
                if (f < minEven) minEven = f;
            }
        }

        return maxOdd - minEven;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function(s) {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let maxOdd = -Infinity;
    let minEven = Infinity;
    for (const f of freq) {
        if (f === 0) continue;
        if (f % 2 === 1) {
            if (f > maxOdd) maxOdd = f;
        } else {
            if (f < minEven) minEven = f;
        }
    }
    return maxOdd - minEven;
};
```

## Typescript

```typescript
function maxDifference(s: string): number {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let maxOdd = -Infinity;
    let minEven = Infinity;
    for (const f of freq) {
        if (f === 0) continue;
        if (f % 2 === 1) {
            if (f > maxOdd) maxOdd = f;
        } else {
            if (f < minEven) minEven = f;
        }
    }
    return maxOdd - minEven;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxDifference($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - ord('a');
            $freq[$idx]++;
        }
        $maxOdd = PHP_INT_MIN;
        $minEven = PHP_INT_MAX;
        foreach ($freq as $cnt) {
            if ($cnt == 0) continue;
            if ($cnt % 2 == 1) {
                if ($cnt > $maxOdd) $maxOdd = $cnt;
            } else {
                if ($cnt < $minEven) $minEven = $cnt;
            }
        }
        return $maxOdd - $minEven;
    }
}
```

## Swift

```swift
class Solution {
    func maxDifference(_ s: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97) // 'a' ASCII is 97
            freq[idx] += 1
        }
        var maxOdd = Int.min
        var minEven = Int.max
        for cnt in freq where cnt > 0 {
            if cnt % 2 == 1 {
                if cnt > maxOdd { maxOdd = cnt }
            } else {
                if cnt < minEven { minEven = cnt }
            }
        }
        return maxOdd - minEven
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDifference(s: String): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var maxOdd = Int.MIN_VALUE
        var minEven = Int.MAX_VALUE
        for (cnt in freq) {
            if (cnt == 0) continue
            if (cnt % 2 == 1) {
                if (cnt > maxOdd) maxOdd = cnt
            } else {
                if (cnt < minEven) minEven = cnt
            }
        }
        return maxOdd - minEven
    }
}
```

## Dart

```dart
class Solution {
  int maxDifference(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }
    int maxOdd = -1;
    int minEven = 101; // length constraint upper bound + 1
    for (int c in cnt) {
      if (c == 0) continue;
      if (c % 2 == 1) {
        if (c > maxOdd) maxOdd = c;
      } else {
        if (c < minEven) minEven = c;
      }
    }
    return maxOdd - minEven;
  }
}
```

## Golang

```go
func maxDifference(s string) int {
    freq := [26]int{}
    for _, ch := range s {
        freq[ch-'a']++
    }
    maxOdd := 0
    minEven := len(s) + 1
    for _, cnt := range freq {
        if cnt == 0 {
            continue
        }
        if cnt%2 == 1 {
            if cnt > maxOdd {
                maxOdd = cnt
            }
        } else {
            if cnt < minEven {
                minEven = cnt
            }
        }
    }
    return maxOdd - minEven
}
```

## Ruby

```ruby
def max_difference(s)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  max_odd = 0
  min_even = s.length
  freq.each do |c|
    next if c == 0
    if c.odd?
      max_odd = c if c > max_odd
    else
      min_even = c if c < min_even
    end
  end
  max_odd - min_even
end
```

## Scala

```scala
object Solution {
    def maxDifference(s: String): Int = {
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        var maxOdd = Int.MinValue
        var minEven = Int.MaxValue
        for (f <- freq if f > 0) {
            if ((f & 1) == 1) { // odd
                if (f > maxOdd) maxOdd = f
            } else { // even
                if (f < minEven) minEven = f
            }
        }
        maxOdd - minEven
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut freq = [0usize; 26];
        for b in s.bytes() {
            let idx = (b - b'a') as usize;
            freq[idx] += 1;
        }
        let mut max_odd = 0usize;
        let mut min_even = usize::MAX;
        for &c in freq.iter() {
            if c == 0 {
                continue;
            }
            if c % 2 == 1 {
                if c > max_odd {
                    max_odd = c;
                }
            } else {
                if c < min_even {
                    min_even = c;
                }
            }
        }
        (max_odd as i32) - (min_even as i32)
    }
}
```

## Racket

```racket
(define/contract (max-difference s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [counts (make-vector 26 0)])
    ;; count frequencies
    (for ([i (in-range n)])
      (let* ([ch (string-ref s i)]
             [idx (- (char->integer ch) (char->integer #\a))])
        (vector-set! counts idx (+ 1 (vector-ref counts idx)))))
    ;; compute max odd and min even
    (define max-odd -1)
    (define min-even (+ n 1))
    (for ([cnt (in-vector counts)])
      (when (> cnt 0)
        (if (odd? cnt)
            (set! max-odd (max max-odd cnt))
            (set! min-even (min min-even cnt)))))
    (- max-odd min-even)))
```

## Erlang

```erlang
-module(solution).
-export([max_difference/1]).

-spec max_difference(S :: unicode:unicode_binary()) -> integer().
max_difference(S) ->
    Counts = count_chars(binary_to_list(S), #{}),
    Values = maps:values(Counts),
    OddVals = [V || V <- Values, V rem 2 =:= 1],
    EvenVals = [V || V <- Values, V rem 2 =:= 0],
    MaxOdd = lists:max(OddVals),
    MinEven = lists:min(EvenVals),
    MaxOdd - MinEven.

count_chars([], Acc) -> Acc;
count_chars([C|Rest], Acc) ->
    NewAcc = maps:update_with(C, fun(N) -> N + 1 end, 1, Acc),
    count_chars(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_difference(s :: String.t()) :: integer
  def max_difference(s) do
    freq =
      s
      |> String.to_charlist()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    {max_odd, min_even} =
      freq
      |> Map.values()
      |> Enum.reduce({0, 1_000_000}, fn cnt, {mo, me} ->
        if rem(cnt, 2) == 1 do
          {if cnt > mo, do: cnt, else: mo, me}
        else
          {mo, if cnt < me, do: cnt, else: me}
        end
      end)

    max_odd - min_even
  end
end
```
