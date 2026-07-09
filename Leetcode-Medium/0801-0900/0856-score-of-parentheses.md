# 0856. Score of Parentheses

## Cpp

```cpp
class Solution {
public:
    int scoreOfParentheses(string s) {
        int depth = 0, ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++depth;
            } else {
                --depth;
                if (i > 0 && s[i - 1] == '(') {
                    ans += 1 << depth;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int scoreOfParentheses(String s) {
        int ans = 0;
        int depth = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') {
                depth++;
            } else {
                depth--;
                if (i > 0 && chars[i - 1] == '(') {
                    ans += 1 << depth;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[0]
```

## Python3

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth
        return score
```

## C

```c
int scoreOfParentheses(char* s) {
    int ans = 0;
    int depth = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '(') {
            ++depth;
        } else {
            --depth;
            if (i > 0 && s[i - 1] == '(') {
                ans += 1 << depth;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int ScoreOfParentheses(string s)
    {
        int score = 0, depth = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(')
                depth++;
            else
            {
                depth--;
                if (i > 0 && s[i - 1] == '(')
                    score += 1 << depth;
            }
        }
        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfParentheses = function(s) {
    let ans = 0;
    let bal = 0; // current depth
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            bal++;
        } else {
            bal--;
            if (s[i - 1] === '(') {
                ans += 1 << bal;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function scoreOfParentheses(s: string): number {
    let ans = 0;
    let depth = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '(') {
            depth++;
        } else {
            depth--;
            if (s[i - 1] === '(') {
                ans += 1 << depth;
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
    function scoreOfParentheses($s) {
        $depth = 0;
        $score = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                $depth++;
            } else {
                $depth--;
                if ($i > 0 && $s[$i - 1] === '(') {
                    $score += 1 << $depth;
                }
            }
        }
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func scoreOfParentheses(_ s: String) -> Int {
        var depth = 0
        var ans = 0
        let chars = Array(s)
        for i in 0..<chars.count {
            if chars[i] == "(" {
                depth += 1
            } else {
                depth -= 1
                if i > 0 && chars[i - 1] == "(" {
                    ans += 1 << depth
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun scoreOfParentheses(s: String): Int {
        var ans = 0
        var depth = 0
        for (i in s.indices) {
            if (s[i] == '(') {
                depth++
            } else {
                depth--
                if (i > 0 && s[i - 1] == '(') {
                    ans += 1 shl depth
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int scoreOfParentheses(String s) {
    int score = 0;
    int depth = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        depth++;
      } else {
        depth--;
        if (i > 0 && s[i - 1] == '(') {
          score += 1 << depth;
        }
      }
    }
    return score;
  }
}
```

## Golang

```go
func scoreOfParentheses(s string) int {
    ans, depth := 0, 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            depth++
        } else {
            depth--
            if i > 0 && s[i-1] == '(' {
                ans += 1 << depth
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def score_of_parentheses(s)
  ans = 0
  depth = 0
  prev = ''
  s.each_char do |c|
    if c == '('
      depth += 1
    else
      depth -= 1
      ans += 1 << depth if prev == '('
    end
    prev = c
  end
  ans
end
```

## Scala

```scala
object Solution {
    def scoreOfParentheses(s: String): Int = {
        var depth = 0
        var score = 0
        val n = s.length
        for (i <- 0 until n) {
            if (s.charAt(i) == '(') {
                depth += 1
            } else {
                depth -= 1
                if (i > 0 && s.charAt(i - 1) == '(') {
                    score += 1 << depth
                }
            }
        }
        score
    }
}
```

## Rust

```rust
impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut ans: i32 = 0;
        let mut depth: i32 = 0;
        for i in 0..bytes.len() {
            if bytes[i] == b'(' {
                depth += 1;
            } else {
                depth -= 1;
                if i > 0 && bytes[i - 1] == b'(' {
                    ans += 1 << depth;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (score-of-parentheses s)
  (-> string? exact-integer?)
  (let ((n (string-length s)))
    (let loop ((i 0) (depth 0) (res 0) (prev #\space))
      (if (= i n)
          res
          (let ((c (string-ref s i)))
            (cond [(char=? c #\()
                   (loop (+ i 1) (+ depth 1) res c)]
                  [else
                   (let ((new-depth (- depth 1)))
                     (if (char=? prev #\()
                         (loop (+ i 1) new-depth (+ res (expt 2 new-depth)) c)
                         (loop (+ i 1) new-depth res c)))]))))))
```

## Erlang

```erlang
-module(solution).
-export([score_of_parentheses/1]).

-spec score_of_parentheses(S :: unicode:unicode_binary()) -> integer().
score_of_parentheses(S) ->
    List = binary_to_list(S),
    score(List, 0, 0, $).

score([], _Depth, Acc, _Prev) ->
    Acc;
score([Char|Rest], Depth, Acc, Prev) ->
    case Char of
        $( ->
            score(Rest, Depth + 1, Acc, Char);
        $) ->
            NewAcc = 
                if Prev == $( ->
                        Acc + (1 bsl (Depth - 1));
                   true -> Acc
                end,
            score(Rest, Depth - 1, NewAcc, Char)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec score_of_parentheses(s :: String.t()) :: integer()
  def score_of_parentheses(s) do
    chars = :binary.bin_to_list(s)

    {ans, _depth, _prev} =
      Enum.reduce(chars, {0, 0, nil}, fn ch, {ans, depth, prev} ->
        case ch do
          ?( ->
            {ans, depth + 1, ?(}

          ?) ->
            new_depth = depth - 1

            add =
              if prev == ?( do
                1 <<< new_depth
              else
                0
              end

            {ans + add, new_depth, ?)}
        end
      end)

    ans
  end
end
```
