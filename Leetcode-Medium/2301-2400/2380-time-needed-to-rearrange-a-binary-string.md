# 2380. Time Needed to Rearrange a Binary String

## Cpp

```cpp
class Solution {
public:
    int secondsToRemoveOccurrences(string s) {
        int ones = 0, seconds = 0;
        for (char c : s) {
            if (c == '1') {
                ++ones;
            } else if (ones > 0) {
                seconds = max(seconds + 1, ones);
            }
        }
        return seconds;
    }
};
```

## Java

```java
class Solution {
    public int secondsToRemoveOccurrences(String s) {
        int zeros = 0;
        int seconds = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '0') {
                zeros++;
            } else if (zeros > 0) {
                // this '1' will need to move left across existing zeros
                seconds = Math.max(seconds + 1, zeros);
            }
        }
        return seconds;
    }
}
```

## Python

```python
class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros = 0
        seconds = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            elif zeros > 0:
                # this '1' needs to move left across the preceding zeros
                seconds = max(seconds + 1, zeros)
        return seconds
```

## Python3

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        seconds = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            elif zeros > 0:
                # this '1' needs to move past the preceding zeros
                seconds = max(seconds + 1, zeros)
        return seconds
```

## C

```c
int secondsToRemoveOccurrences(char* s) {
    int zeros = 0;
    int seconds = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '0') {
            ++zeros;
        } else { // s[i] == '1'
            if (zeros > 0) {
                if (seconds + 1 > zeros)
                    seconds = seconds + 1;
                else
                    seconds = zeros;
            }
        }
    }
    return seconds;
}
```

## Csharp

```csharp
public class Solution {
    public int SecondsToRemoveOccurrences(string s) {
        int ones = 0;
        int seconds = 0;
        for (int i = s.Length - 1; i >= 0; --i) {
            if (s[i] == '1') {
                ones++;
            } else { // '0'
                if (ones > 0) {
                    seconds = Math.Max(seconds + 1, ones);
                }
            }
        }
        return seconds;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var secondsToRemoveOccurrences = function(s) {
    const arr = s.split('');
    const n = arr.length;
    let seconds = 0;
    while (true) {
        const swaps = [];
        for (let i = 0; i < n - 1; ) {
            if (arr[i] === '0' && arr[i + 1] === '1') {
                swaps.push(i);
                i += 2; // skip the next character because it participates in this swap
            } else {
                i++;
            }
        }
        if (swaps.length === 0) break;
        for (const idx of swaps) {
            arr[idx] = '1';
            arr[idx + 1] = '0';
        }
        seconds++;
    }
    return seconds;
};
```

## Typescript

```typescript
function secondsToRemoveOccurrences(s: string): number {
    let zeros = 0;
    let ans = 0;
    for (const ch of s) {
        if (ch === '0') {
            zeros++;
        } else {
            if (zeros > 0) {
                ans = Math.max(ans + 1, zeros);
            }
        }
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
    function secondsToRemoveOccurrences($s) {
        $cnt = 0;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                $cnt++;
            } else { // '1'
                if ($cnt > 0) {
                    $ans = max($ans + 1, $cnt);
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func secondsToRemoveOccurrences(_ s: String) -> Int {
        var ones = 0
        var seconds = 0
        for ch in s {
            if ch == "1" {
                ones += 1
            } else { // ch == '0'
                if ones > 0 {
                    seconds = max(seconds + 1, ones)
                }
            }
        }
        return seconds
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun secondsToRemoveOccurrences(s: String): Int {
        var zeros = 0
        var seconds = 0
        for (ch in s) {
            if (ch == '0') {
                zeros++
            } else { // ch == '1'
                if (zeros > 0) {
                    seconds = maxOf(seconds + 1, zeros)
                }
            }
        }
        return seconds
    }
}
```

## Dart

```dart
class Solution {
  int secondsToRemoveOccurrences(String s) {
    int ones = 0;
    int seconds = 0;
    for (int i = s.length - 1; i >= 0; --i) {
      if (s.codeUnitAt(i) == 49) { // '1'
        ones++;
      } else {
        if (ones > 0) {
          seconds = (seconds + 1 > ones) ? seconds + 1 : ones;
        }
      }
    }
    return seconds;
  }
}
```

## Golang

```go
func secondsToRemoveOccurrences(s string) int {
	zeros := 0
	seconds := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
		} else if zeros > 0 {
			if seconds+1 > zeros {
				seconds = seconds + 1
			} else {
				seconds = zeros
			}
		}
	}
	return seconds
}
```

## Ruby

```ruby
def seconds_to_remove_occurrences(s)
  seconds = 0
  ones = 0
  i = s.length - 1
  while i >= 0
    if s.getbyte(i) == 49 # '1'
      ones += 1
    else # '0'
      if ones > 0
        seconds = [seconds + 1, ones].max
      end
    end
    i -= 1
  end
  seconds
end
```

## Scala

```scala
object Solution {
    def secondsToRemoveOccurrences(s: String): Int = {
        var zeros = 0
        var ans = 0
        for (ch <- s) {
            if (ch == '0') {
                zeros += 1
            } else {
                if (zeros > 0) {
                    ans = math.max(ans + 1, zeros)
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn seconds_to_remove_occurrences(s: String) -> i32 {
        let mut zero_cnt = 0i32;
        let mut ans = 0i32;
        for ch in s.chars() {
            if ch == '0' {
                zero_cnt += 1;
            } else if zero_cnt > 0 {
                ans = std::cmp::max(ans + 1, zero_cnt);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (seconds-to-remove-occurrences s)
  (-> string? exact-integer?)
  (let loop ((i 0)
             (n (string-length s))
             (ones 0)
             (seconds 0))
    (if (= i n)
        seconds
        (let ((c (string-ref s i)))
          (cond [(char=? c #\1)
                 (loop (+ i 1) n (+ ones 1) seconds)]
                [(and (char=? c #\0) (> ones 0))
                 (define new-seconds (max (+ seconds 1) ones))
                 (loop (+ i 1) n ones new-seconds)]
                [else
                 (loop (+ i 1) n ones seconds)])))))
```

## Erlang

```erlang
-module(solution).
-export([seconds_to_remove_occurrences/1]).

-spec seconds_to_remove_occurrences(S :: unicode:unicode_binary()) -> integer().
seconds_to_remove_occurrences(S) ->
    process(S, 0, 0).

process(<<>>, _Ones, Secs) ->
    Secs;
process(<<C, Rest/binary>>, Ones, Secs) ->
    case C of
        $1 ->
            process(Rest, Ones + 1, Secs);
        $0 ->
            if Ones =:= 0 ->
                    process(Rest, Ones, Secs);
               true ->
                    NewSecs = erlang:max(Secs + 1, Ones),
                    process(Rest, Ones, NewSecs)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec seconds_to_remove_occurrences(s :: String.t()) :: integer()
  def seconds_to_remove_occurrences(s) do
    {seconds, _ones} =
      s
      |> String.to_charlist()
      |> Enum.reduce({0, 0}, fn
        ?1, {sec, ones} -> {sec, ones + 1}
        ?0, {sec, 0} = acc -> acc
        ?0, {sec, ones} ->
          new_sec = max(sec + 1, ones)
          {new_sec, ones}
      end)

    seconds
  end
end
```
