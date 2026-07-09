# 1963. Minimum Number of Swaps to Make the String Balanced

## Cpp

```cpp
class Solution {
public:
    int minSwaps(string s) {
        int unmatchedOpen = 0;
        for (char c : s) {
            if (c == '[') {
                ++unmatchedOpen;
            } else { // c == ']'
                if (unmatchedOpen > 0) {
                    --unmatchedOpen;
                }
            }
        }
        return (unmatchedOpen + 1) / 2;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(String s) {
        int balance = 0;
        int minBalance = 0;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (c == '[') {
                balance++;
            } else {
                balance--;
            }
            if (balance < minBalance) {
                minBalance = balance;
            }
        }
        return (-minBalance + 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        unmatched_open = 0
        for ch in s:
            if ch == '[':
                unmatched_open += 1
            else:  # ch == ']'
                if unmatched_open > 0:
                    unmatched_open -= 1
                # else: extra closing bracket, ignore for now
        return (unmatched_open + 1) // 2
```

## Python3

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched_open = 0
        for ch in s:
            if ch == '[':
                unmatched_open += 1
            else:  # ch == ']'
                if unmatched_open > 0:
                    unmatched_open -= 1
        return (unmatched_open + 1) // 2
```

## C

```c
int minSwaps(char* s) {
    int unmatched = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '[') {
            ++unmatched;
        } else { // ']'
            if (unmatched > 0) {
                --unmatched;
            }
        }
    }
    return (unmatched + 1) / 2;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSwaps(string s)
    {
        int unmatchedOpen = 0;
        foreach (char c in s)
        {
            if (c == '[')
                unmatchedOpen++;
            else // c == ']'
            {
                if (unmatchedOpen > 0)
                    unmatchedOpen--;
            }
        }
        return (unmatchedOpen + 1) / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    let unmatchedOpen = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '[') {
            ++unmatchedOpen;
        } else { // ']'
            if (unmatchedOpen > 0) {
                --unmatchedOpen;
            }
        }
    }
    return Math.floor((unmatchedOpen + 1) / 2);
};
```

## Typescript

```typescript
function minSwaps(s: string): number {
    let imbalance = 0;      // extra closing brackets seen so far
    let maxImbalance = 0;   // maximum value of imbalance during traversal

    for (const ch of s) {
        if (ch === '[') {
            if (imbalance > 0) {
                // this opening bracket can balance a previous unmatched closing bracket
                imbalance--;
            }
        } else { // ch === ']'
            imbalance++;
            if (imbalance > maxImbalance) {
                maxImbalance = imbalance;
            }
        }
    }

    // Each swap fixes two mismatched brackets, so round up half of maxImbalance
    return Math.floor((maxImbalance + 1) / 2);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minSwaps($s) {
        $unmatched = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '[') {
                $unmatched++;
            } else { // ']'
                if ($unmatched > 0) {
                    $unmatched--;
                }
            }
        }
        return intdiv($unmatched + 1, 2);
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ s: String) -> Int {
        var balance = 0
        var swaps = 0
        for ch in s {
            if ch == "[" {
                balance += 1
            } else { // ch == "]"
                if balance > 0 {
                    balance -= 1
                } else {
                    swaps += 1
                    balance = 1
                }
            }
        }
        return swaps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(s: String): Int {
        var unmatchedOpen = 0
        for (ch in s) {
            if (ch == '[') {
                unmatchedOpen++
            } else { // ch == ']'
                if (unmatchedOpen > 0) {
                    unmatchedOpen--
                }
            }
        }
        return (unmatchedOpen + 1) / 2
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(String s) {
    int unmatchedOpen = 0;
    for (int i = 0; i < s.length; i++) {
      if (s.codeUnitAt(i) == 91) { // '['
        unmatchedOpen++;
      } else { // ']'
        if (unmatchedOpen > 0) {
          unmatchedOpen--;
        }
      }
    }
    return (unmatchedOpen + 1) ~/ 2;
  }
}
```

## Golang

```go
func minSwaps(s string) int {
    ans, balance := 0, 0
    for i := 0; i < len(s); i++ {
        if s[i] == '[' {
            balance++
        } else { // ']'
            balance--
            if balance < 0 {
                ans++
                balance = 1
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_swaps(s)
  unmatched = 0
  s.each_char do |ch|
    if ch == '['
      unmatched += 1
    else # ']'
      unmatched -= 1 if unmatched > 0
    end
  end
  (unmatched + 1) / 2
end
```

## Scala

```scala
object Solution {
    def minSwaps(s: String): Int = {
        var open = 0
        for (ch <- s) {
            if (ch == '[') {
                open += 1
            } else {
                if (open > 0) open -= 1
            }
        }
        (open + 1) / 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let mut unmatched = 0usize;
        for ch in s.chars() {
            if ch == '[' {
                unmatched += 1;
            } else { // ']'
                if unmatched > 0 {
                    unmatched -= 1;
                }
            }
        }
        ((unmatched + 1) / 2) as i32
    }
}
```

## Racket

```racket
(define/contract (min-swaps s)
  (-> string? exact-integer?)
  (let ((stack-size 0))
    (for ([i (in-range (string-length s))])
      (let ((ch (string-ref s i)))
        (cond [(char=? ch #\[) (set! stack-size (+ stack-size 1))]
              [(char=? ch #\]) (when (> stack-size 0)
                                 (set! stack-size (- stack-size 1)))])))
    (quotient (+ stack-size 1) 2)))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps/1]).

-spec min_swaps(S :: unicode:unicode_binary()) -> integer().
min_swaps(S) ->
    min_swaps_bin(S, 0, 0).

min_swaps_bin(<<>>, _Balance, Imbalance) ->
    (Imbalance + 1) div 2;
min_swaps_bin(<<Char, Rest/binary>>, Balance, Imbalance) when Char =:= $[ ->
    min_swaps_bin(Rest, Balance + 1, Imbalance);
min_swaps_bin(<<Char, Rest/binary>>, Balance, Imbalance) when Char =:= $] ->
    case Balance of
        0 -> min_swaps_bin(Rest, Balance, Imbalance + 1);
        _ -> min_swaps_bin(Rest, Balance - 1, Imbalance)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(s :: String.t()) :: integer()
  def min_swaps(s) do
    unmatched = count_unmatched(s, 0)
    div(unmatched + 1, 2)
  end

  defp count_unmatched(<<>>, acc), do: acc

  defp count_unmatched(<<"[", rest::binary>>, acc),
    do: count_unmatched(rest, acc + 1)

  defp count_unmatched(<<"]", rest::binary>>, acc) when acc > 0,
    do: count_unmatched(rest, acc - 1)

  defp count_unmatched(<<"]", rest::binary>>, acc),
    do: count_unmatched(rest, acc)
end
```
