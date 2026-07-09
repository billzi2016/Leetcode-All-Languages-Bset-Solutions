# 0926. Flip String to Monotone Increasing

## Cpp

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int flips = 0; // minimum flips so far to make prefix monotone increasing
        int ones = 0;  // count of '1's seen in the original string
        for (char c : s) {
            if (c == '1') {
                ++ones;
            } else { // c == '0'
                // either flip this zero to 1 (flips+1) or flip all previous ones to zeros (ones)
                flips = min(flips + 1, ones);
            }
        }
        return flips;
    }
};
```

## Java

```java
class Solution {
    public int minFlipsMonoIncr(String s) {
        int flips = 0;
        int ones = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '1') {
                ones++;
            } else { // c == '0'
                flips = Math.min(flips + 1, ones);
            }
        }
        return flips;
    }
}
```

## Python

```python
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        flips = 0
        ones = 0
        for ch in s:
            if ch == '0':
                flips = min(flips + 1, ones)
            else:
                ones += 1
        return flips
```

## Python3

```python
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0
        for ch in s:
            if ch == '0':
                flips = min(flips + 1, ones)
            else:
                ones += 1
        return flips
```

## C

```c
int minFlipsMonoIncr(char* s) {
    int flips = 0;
    int ones = 0;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '1') {
            ++ones;
        } else { // s[i] == '0'
            // either flip this zero to 1, or flip all previous ones to 0
            flips = (flips + 1 < ones) ? flips + 1 : ones;
        }
    }
    return flips;
}
```

## Csharp

```csharp
public class Solution {
    public int MinFlipsMonoIncr(string s) {
        int flips = 0;
        int ones = 0;
        foreach (char c in s) {
            if (c == '1') {
                ones++;
            } else { // c == '0'
                flips = Math.Min(flips + 1, ones);
            }
        }
        return flips;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    let flips = 0;
    let ones = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '1') {
            ones++;
        } else { // '0'
            flips = Math.min(flips + 1, ones);
        }
    }
    return flips;
};
```

## Typescript

```typescript
function minFlipsMonoIncr(s: string): number {
    let flips = 0;
    let ones = 0;
    for (const ch of s) {
        if (ch === '1') {
            ones++;
        } else { // ch === '0'
            flips = Math.min(flips + 1, ones);
        }
    }
    return flips;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minFlipsMonoIncr($s) {
        $ones = 0;
        $flips = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1') {
                $ones++;
            } else { // '0'
                $flips = min($flips + 1, $ones);
            }
        }
        return $flips;
    }
}
```

## Swift

```swift
class Solution {
    func minFlipsMonoIncr(_ s: String) -> Int {
        var flips = 0
        var ones = 0
        for ch in s {
            if ch == "0" {
                flips = min(flips + 1, ones)
            } else {
                ones += 1
            }
        }
        return flips
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlipsMonoIncr(s: String): Int {
        var flips = 0
        var ones = 0
        for (ch in s) {
            if (ch == '0') {
                flips = kotlin.math.min(flips + 1, ones)
            } else {
                ones++
            }
        }
        return flips
    }
}
```

## Dart

```dart
class Solution {
  int minFlipsMonoIncr(String s) {
    int dpZero = 0; // flips to make prefix all zeros
    int dpOne = 0;  // flips to make prefix monotone ending with ones

    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i); // '0' -> 48, '1' -> 49
      if (ch == 48) { // '0'
        int newDpZero = dpZero;
        int newDpOne = dpZero < dpOne + 1 ? dpZero : dpOne + 1;
        dpZero = newDpZero;
        dpOne = newDpOne;
      } else { // '1'
        int newDpZero = dpZero + 1; // flip this '1' to '0'
        int newDpOne = dpZero < dpOne ? dpZero : dpOne;
        dpZero = newDpZero;
        dpOne = newDpOne;
      }
    }

    return dpZero < dpOne ? dpZero : dpOne;
  }
}
```

## Golang

```go
func minFlipsMonoIncr(s string) int {
	ones, flips := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		} else { // '0'
			if flips+1 < ones {
				flips = flips + 1
			} else {
				flips = ones
			}
		}
	}
	return flips
}
```

## Ruby

```ruby
def min_flips_mono_incr(s)
  ones = 0
  flips = 0
  s.each_char do |ch|
    if ch == '1'
      ones += 1
    else
      flips = [flips + 1, ones].min
    end
  end
  flips
end
```

## Scala

```scala
object Solution {
    def minFlipsMonoIncr(s: String): Int = {
        var flips = 0
        var ones = 0
        for (ch <- s) {
            if (ch == '0') {
                flips = Math.min(flips + 1, ones)
            } else {
                ones += 1
            }
        }
        flips
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let mut flips: i32 = 0;
        let mut ones: i32 = 0;
        for ch in s.bytes() {
            if ch == b'1' {
                ones += 1;
            } else {
                flips = std::cmp::min(flips + 1, ones);
            }
        }
        flips
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (min-flips-mono-incr s)
  (-> string? exact-integer?)
  (let ((flips 0)
        (ones 0))
    (for ([i (in-range (string-length s))])
      (let ((c (string-ref s i)))
        (cond
          [(char=? c #\0)
           (set! flips (min (+ flips 1) ones))]
          [else
           (set! ones (+ ones 1))])))
    flips))
```

## Erlang

```erlang
-spec min_flips_mono_incr(S :: unicode:unicode_binary()) -> integer().
min_flips_mono_incr(S) ->
    List = binary_to_list(S),
    {_, Flips} = lists:foldl(
        fun(C, {Ones, Fl}) ->
            case C of
                $0 ->
                    NewFl = erlang:min(Fl + 1, Ones),
                    {Ones, NewFl};
                $1 ->
                    {Ones + 1, Fl}
            end
        end,
        {0, 0},
        List),
    Flips.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_flips_mono_incr(s :: String.t()) :: integer()
  def min_flips_mono_incr(s) do
    do_min(s, 0, 0)
  end

  defp do_min(<<>>, flips, _ones), do: flips

  defp do_min(<<"0", rest::binary>>, flips, ones) do
    new_flips = min(flips + 1, ones)
    do_min(rest, new_flips, ones)
  end

  defp do_min(<<"1", rest::binary>>, flips, ones) do
    do_min(rest, flips, ones + 1)
  end
end
```
