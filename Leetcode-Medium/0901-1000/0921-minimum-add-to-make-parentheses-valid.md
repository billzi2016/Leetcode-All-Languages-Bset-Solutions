# 0921. Minimum Add to Make Parentheses Valid

## Cpp

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0, add = 0;
        for (char c : s) {
            if (c == '(') {
                ++open;
            } else { // ')'
                if (open > 0) {
                    --open;
                } else {
                    ++add; // need an extra '('
                }
            }
        }
        return open + add;
    }
};
```

## Java

```java
class Solution {
    public int minAddToMakeValid(String s) {
        int open = 0, adds = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                open++;
            } else { // ')'
                if (open > 0) {
                    open--;
                } else {
                    adds++;
                }
            }
        }
        return adds + open;
    }
}
```

## Python

```python
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_brackets = 0
        additions = 0
        for ch in s:
            if ch == '(':
                open_brackets += 1
            else:  # ')'
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    additions += 1
        return additions + open_brackets
```

## Python3

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        additions = 0
        for ch in s:
            if ch == '(':
                open_brackets += 1
            else:  # ch == ')'
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    additions += 1
        return additions + open_brackets
```

## C

```c
int minAddToMakeValid(char* s) {
    int open = 0;
    int adds = 0;
    for (; *s; ++s) {
        if (*s == '(') {
            ++open;
        } else { // ')'
            if (open > 0) {
                --open;
            } else {
                ++adds;
            }
        }
    }
    return adds + open;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinAddToMakeValid(string s)
    {
        int open = 0, additions = 0;
        foreach (char c in s)
        {
            if (c == '(')
                open++;
            else // ')'
            {
                if (open > 0)
                    open--;
                else
                    additions++;
            }
        }
        return additions + open;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    let open = 0;
    let adds = 0;
    for (let ch of s) {
        if (ch === '(') {
            open++;
        } else { // ')'
            if (open > 0) {
                open--;
            } else {
                adds++;
            }
        }
    }
    return adds + open;
};
```

## Typescript

```typescript
function minAddToMakeValid(s: string): number {
    let open = 0, adds = 0;
    for (const ch of s) {
        if (ch === '(') {
            open++;
        } else {
            if (open > 0) {
                open--;
            } else {
                adds++;
            }
        }
    }
    return adds + open;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minAddToMakeValid($s) {
        $open = 0;
        $adds = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                $open++;
            } else { // ')'
                if ($open > 0) {
                    $open--;
                } else {
                    $adds++;
                }
            }
        }
        return $adds + $open;
    }
}
```

## Swift

```swift
class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var open = 0
        var adds = 0
        for ch in s {
            if ch == "(" {
                open += 1
            } else { // ')'
                if open > 0 {
                    open -= 1
                } else {
                    adds += 1
                }
            }
        }
        return adds + open
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAddToMakeValid(s: String): Int {
        var open = 0
        var adds = 0
        for (ch in s) {
            if (ch == '(') {
                open++
            } else {
                if (open > 0) {
                    open--
                } else {
                    adds++
                }
            }
        }
        return open + adds
    }
}
```

## Dart

```dart
class Solution {
  int minAddToMakeValid(String s) {
    int open = 0;
    int add = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        open++;
      } else {
        if (open > 0) {
          open--;
        } else {
          add++;
        }
      }
    }
    return add + open;
  }
}
```

## Golang

```go
func minAddToMakeValid(s string) int {
    open, adds := 0, 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            open++
        } else { // ')'
            if open > 0 {
                open--
            } else {
                adds++
            }
        }
    }
    return open + adds
}
```

## Ruby

```ruby
def min_add_to_make_valid(s)
  open = 0
  adds = 0
  s.each_char do |c|
    if c == '('
      open += 1
    else
      if open > 0
        open -= 1
      else
        adds += 1
      end
    end
  end
  adds + open
end
```

## Scala

```scala
object Solution {
    def minAddToMakeValid(s: String): Int = {
        var openBrackets = 0
        var additionsNeeded = 0
        for (ch <- s) {
            if (ch == '(') {
                openBrackets += 1
            } else { // ch == ')'
                if (openBrackets > 0) {
                    openBrackets -= 1
                } else {
                    additionsNeeded += 1
                }
            }
        }
        additionsNeeded + openBrackets
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut open = 0;
        let mut add = 0;
        for ch in s.chars() {
            if ch == '(' {
                open += 1;
            } else {
                if open > 0 {
                    open -= 1;
                } else {
                    add += 1;
                }
            }
        }
        (add + open) as i32
    }
}
```

## Racket

```racket
(define/contract (min-add-to-make-valid s)
  (-> string? exact-integer?)
  (let loop ((i 0) (open 0) (adds 0))
    (if (= i (string-length s))
        (+ open adds)
        (let ((c (string-ref s i)))
          (cond [(char=? c #\()
                 (loop (+ i 1) (+ open 1) adds)]
                [(char=? c #\))
                 (if (> open 0)
                     (loop (+ i 1) (- open 1) adds)
                     (loop (+ i 1) open (+ adds 1)))]
                [else
                 (loop (+ i 1) open adds)])))))
```

## Erlang

```erlang
-module(solution).
-export([min_add_to_make_valid/1]).

-spec min_add_to_make_valid(S :: unicode:unicode_binary()) -> integer().
min_add_to_make_valid(S) ->
    min_add_to_make_valid(binary:bin_to_list(S), 0, 0).

min_add_to_make_valid([], Open, Add) ->
    Open + Add;
min_add_to_make_valid([$( | Rest], Open, Add) ->
    min_add_to_make_valid(Rest, Open + 1, Add);
min_add_to_make_valid([$) | Rest], Open, Add) ->
    case Open > 0 of
        true -> min_add_to_make_valid(Rest, Open - 1, Add);
        false -> min_add_to_make_valid(Rest, Open, Add + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_add_to_make_valid(s :: String.t()) :: integer()
  def min_add_to_make_valid(s) do
    {open, adds} =
      String.graphemes(s)
      |> Enum.reduce({0, 0}, fn
        "(", {o, a} -> {o + 1, a}
        ")", {o, a} ->
          if o > 0 do
            {o - 1, a}
          else
            {o, a + 1}
          end
      end)

    open + adds
  end
end
```
