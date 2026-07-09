# 1247. Minimum Swaps to Make Strings Equal

## Cpp

```cpp
class Solution {
public:
    int minimumSwap(string s1, string s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < (int)s1.size(); ++i) {
            if (s1[i] == 'x' && s2[i] == 'y') ++xy;
            else if (s1[i] == 'y' && s2[i] == 'x') ++yx;
        }
        if ((xy + yx) % 2) return -1;
        return xy / 2 + yx / 2 + 2 * (xy % 2);
    }
};
```

## Java

```java
class Solution {
    public int minimumSwap(String s1, String s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < s1.length(); i++) {
            char a = s1.charAt(i);
            char b = s2.charAt(i);
            if (a == b) continue;
            if (a == 'x' && b == 'y') xy++;
            else if (a == 'y' && b == 'x') yx++;
        }
        int total = xy + yx;
        if ((total & 1) == 1) return -1;
        int swaps = xy / 2 + yx / 2;
        if ((xy & 1) == 1) swaps += 2; // both xy and yx are odd
        return swaps;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == 'x' and b == 'y':
                xy += 1
            else:  # a == 'y' and b == 'x'
                yx += 1
        total = xy + yx
        if total % 2:
            return -1
        swaps = xy // 2 + yx // 2
        if xy % 2:  # one xy and one yx remain
            swaps += 2
        return swaps
```

## Python3

```python
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == 'x' and b == 'y':
                xy += 1
            else:  # a == 'y' and b == 'x'
                yx += 1
        # If total mismatches is odd, impossible
        if (xy + yx) % 2:
            return -1
        swaps = xy // 2 + yx // 2
        # If both have a leftover (i.e., both are odd), need two extra swaps
        if xy % 2:
            swaps += 2
        return swaps
```

## C

```c
#include <string.h>

int minimumSwap(char* s1, char* s2) {
    int cnt_xy = 0, cnt_yx = 0;
    for (int i = 0; s1[i] && s2[i]; ++i) {
        if (s1[i] != s2[i]) {
            if (s1[i] == 'x')
                cnt_xy++;
            else
                cnt_yx++;
        }
    }
    int total = cnt_xy + cnt_yx;
    if (total % 2 == 1)
        return -1;
    int swaps = cnt_xy / 2 + cnt_yx / 2;
    if ((cnt_xy & 1) && (cnt_yx & 1))
        swaps += 2;
    return swaps;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSwap(string s1, string s2) {
        int cntXY = 0, cntYX = 0;
        for (int i = 0; i < s1.Length; i++) {
            if (s1[i] == s2[i]) continue;
            if (s1[i] == 'x' && s2[i] == 'y') cntXY++;
            else cntYX++; // s1[i]=='y' && s2[i]=='x'
        }
        int total = cntXY + cntYX;
        if ((total & 1) == 1) return -1; // odd number of mismatches cannot be resolved
        int swaps = (cntXY / 2) + (cntYX / 2);
        if ((cntXY % 2) == 1) swaps += 2; // one remaining xy and yx need two swaps
        return swaps;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumSwap = function(s1, s2) {
    let cntXY = 0; // s1 has 'x', s2 has 'y'
    let cntYX = 0; // s1 has 'y', s2 has 'x'
    for (let i = 0; i < s1.length; ++i) {
        if (s1[i] === s2[i]) continue;
        if (s1[i] === 'x') cntXY++;
        else cntYX++;
    }
    const totalMismatch = cntXY + cntYX;
    if (totalMismatch % 2 !== 0) return -1; // impossible
    
    const swaps = Math.floor(cntXY / 2) + Math.floor(cntYX / 2);
    // If both counts are odd, we need two extra swaps
    const extra = (cntXY % 2) * 2;
    return swaps + extra;
};
```

## Typescript

```typescript
function minimumSwap(s1: string, s2: string): number {
    let xy = 0, yx = 0;
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] === s2[i]) continue;
        if (s1[i] === 'x' && s2[i] === 'y') xy++;
        else yx++; // s1[i] === 'y' && s2[i] === 'x'
    }
    const total = xy + yx;
    if (total % 2 !== 0) return -1;
    return Math.floor(xy / 2) + Math.floor(yx / 2) + (xy % 2) * 2;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumSwap($s1, $s2) {
        $len = strlen($s1);
        $xy = 0;
        $yx = 0;
        for ($i = 0; $i < $len; $i++) {
            if ($s1[$i] === $s2[$i]) {
                continue;
            }
            if ($s1[$i] === 'x' && $s2[$i] === 'y') {
                $xy++;
            } else { // $s1[$i] === 'y' && $s2[$i] === 'x'
                $yx++;
            }
        }

        if ((($xy + $yx) & 1) == 1) {
            return -1;
        }

        $swaps = intdiv($xy, 2) + intdiv($yx, 2);
        if ($xy % 2 == 1) { // both xy and yx are odd
            $swaps += 2;
        }
        return $swaps;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSwap(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1)
        let b = Array(s2)
        var xy = 0
        var yx = 0
        for i in 0..<a.count {
            if a[i] == b[i] { continue }
            if a[i] == "x" && b[i] == "y" {
                xy += 1
            } else {
                yx += 1
            }
        }
        let total = xy + yx
        if total % 2 != 0 {
            return -1
        }
        return xy / 2 + yx / 2 + (xy % 2) * 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSwap(s1: String, s2: String): Int {
        var xy = 0
        var yx = 0
        for (i in s1.indices) {
            if (s1[i] == s2[i]) continue
            if (s1[i] == 'x' && s2[i] == 'y') {
                xy++
            } else { // s1[i] == 'y' && s2[i] == 'x'
                yx++
            }
        }
        val total = xy + yx
        if (total % 2 != 0) return -1
        return xy / 2 + yx / 2 + (xy % 2) * 2
    }
}
```

## Dart

```dart
class Solution {
  int minimumSwap(String s1, String s2) {
    int xy = 0;
    int yx = 0;
    for (int i = 0; i < s1.length; i++) {
      if (s1[i] == s2[i]) continue;
      if (s1[i] == 'x' && s2[i] == 'y') {
        xy++;
      } else if (s1[i] == 'y' && s2[i] == 'x') {
        yx++;
      }
    }
    int total = xy + yx;
    if (total % 2 == 1) return -1;
    int swaps = xy ~/ 2 + yx ~/ 2;
    if ((xy & 1) == 1) swaps += 2; // both xy and yx are odd
    return swaps;
  }
}
```

## Golang

```go
func minimumSwap(s1 string, s2 string) int {
	xy, yx := 0, 0
	for i := 0; i < len(s1); i++ {
		if s1[i] == s2[i] {
			continue
		}
		if s1[i] == 'x' && s2[i] == 'y' {
			xy++
		} else { // s1[i]=='y' && s2[i]=='x'
			yx++
		}
	}
	if (xy+yx)%2 == 1 {
		return -1
	}
	swaps := xy/2 + yx/2
	if xy%2 == 1 && yx%2 == 1 {
		swaps += 2
	}
	return swaps
}
```

## Ruby

```ruby
def minimum_swap(s1, s2)
  xy = yx = 0
  s1.length.times do |i|
    next if s1[i] == s2[i]
    if s1[i] == 'x'
      xy += 1
    else
      yx += 1
    end
  end
  return -1 if (xy + yx).odd?
  swaps = xy / 2 + yx / 2
  swaps += 2 if xy.odd? # both are odd here
  swaps
end
```

## Scala

```scala
object Solution {
    def minimumSwap(s1: String, s2: String): Int = {
        var xy = 0
        var yx = 0
        val n = s1.length
        var i = 0
        while (i < n) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (s1.charAt(i) == 'x') xy += 1 else yx += 1
            }
            i += 1
        }
        val total = xy + yx
        if ((total & 1) == 1) -1
        else xy / 2 + yx / 2 + (xy % 2) * 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_swap(s1: String, s2: String) -> i32 {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let mut xy = 0;
        let mut yx = 0;
        for i in 0..b1.len() {
            if b1[i] != b2[i] {
                if b1[i] == b'x' && b2[i] == b'y' {
                    xy += 1;
                } else {
                    yx += 1;
                }
            }
        }
        if (xy + yx) % 2 == 1 {
            return -1;
        }
        let swaps = xy / 2 + yx / 2 + (xy % 2) * 2;
        swaps as i32
    }
}
```

## Racket

```racket
#lang racket
(define/contract (minimum-swap s1 s2)
  (-> string? string? exact-integer?)
  (let ((len (string-length s1)))
    (let-values ([(xy yx)
                  (for/fold ([xy 0] [yx 0]) ([i (in-range len)])
                    (let ((c1 (string-ref s1 i))
                          (c2 (string-ref s2 i)))
                      (cond [(and (char=? c1 #\x) (char=? c2 #\y)) (values (+ xy 1) yx)]
                            [(and (char=? c1 #\y) (char=? c2 #\x)) (values xy (+ yx 1))]
                            [else (values xy yx)])))])
      (if (odd? (+ xy yx))
          -1
          (+ (quotient xy 2)
             (quotient yx 2)
             (if (= (remainder xy 2) 1) 2 0))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_swap/2]).

-spec minimum_swap(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
minimum_swap(S1, S2) ->
    {A, B} = count_mismatches(S1, S2, 0, 0),
    case (A + B) rem 2 of
        1 -> -1;
        _ ->
            Base = (A div 2) + (B div 2),
            if (A rem 2) == 1 -> Base + 2; true -> Base end
    end.

count_mismatches(<<>>, <<>>, A, B) ->
    {A, B};
count_mismatches(<<C1, Rest1/binary>>, <<C2, Rest2/binary>>, A, B) when C1 =:= C2 ->
    count_mismatches(Rest1, Rest2, A, B);
count_mismatches(<<$x, Rest1/binary>>, <<$y, Rest2/binary>>, A, B) ->
    count_mismatches(Rest1, Rest2, A + 1, B);
count_mismatches(<<$y, Rest1/binary>>, <<$x, Rest2/binary>>, A, B) ->
    count_mismatches(Rest1, Rest2, A, B + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_swap(s1 :: String.t(), s2 :: String.t()) :: integer()
  def minimum_swap(s1, s2) do
    len = String.length(s1)

    {cnt_xy, cnt_yx} =
      0..(len - 1)
      |> Enum.reduce({0, 0}, fn i, {xy, yx} ->
        c1 = :binary.part(s1, i, 1)
        c2 = :binary.part(s2, i, 1)

        cond do
          c1 == c2 -> {xy, yx}
          c1 == "x" and c2 == "y" -> {xy + 1, yx}
          true -> {xy, yx + 1}
        end
      end)

    total = cnt_xy + cnt_yx

    if rem(total, 2) == 1 do
      -1
    else
      div(cnt_xy, 2) + div(cnt_yx, 2) + (rem(cnt_xy, 2) * 2)
    end
  end
end
```
