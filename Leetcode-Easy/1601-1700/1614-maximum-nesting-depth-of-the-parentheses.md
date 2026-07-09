# 1614. Maximum Nesting Depth of the Parentheses

## Cpp

```cpp
class Solution {
public:
    int maxDepth(string s) {
        int cur = 0, ans = 0;
        for (char c : s) {
            if (c == '(') {
                ++cur;
                ans = max(ans, cur);
            } else if (c == ')') {
                --cur;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDepth(String s) {
        int max = 0, cur = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                cur++;
                if (cur > max) max = cur;
            } else if (c == ')') {
                cur--;
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        cur = 0
        for ch in s:
            if ch == '(':
                cur += 1
                if cur > max_depth:
                    max_depth = cur
            elif ch == ')':
                cur -= 1
        return max_depth
```

## Python3

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur = 0
        for ch in s:
            if ch == '(':
                cur += 1
                if cur > max_depth:
                    max_depth = cur
            elif ch == ')':
                cur -= 1
        return max_depth
```

## C

```c
int maxDepth(char* s) {
    int cur = 0, ans = 0;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '(') {
            ++cur;
            if (cur > ans) ans = cur;
        } else if (s[i] == ')') {
            --cur;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxDepth(string s)
    {
        int maxDepth = 0;
        int current = 0;
        foreach (char c in s)
        {
            if (c == '(')
            {
                current++;
                if (current > maxDepth) maxDepth = current;
            }
            else if (c == ')')
            {
                current--;
            }
        }
        return maxDepth;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let depth = 0, max = 0;
    for (let ch of s) {
        if (ch === '(') {
            depth++;
            if (depth > max) max = depth;
        } else if (ch === ')') {
            depth--;
        }
    }
    return max;
};
```

## Typescript

```typescript
function maxDepth(s: string): number {
    let maxDepth = 0;
    let current = 0;
    for (const ch of s) {
        if (ch === '(') {
            current++;
            if (current > maxDepth) maxDepth = current;
        } else if (ch === ')') {
            current--;
        }
    }
    return maxDepth;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxDepth($s) {
        $depth = 0;
        $maxDepth = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === '(') {
                $depth++;
                if ($depth > $maxDepth) {
                    $maxDepth = $depth;
                }
            } elseif ($c === ')') {
                $depth--;
            }
        }
        return $maxDepth;
    }
}
```

## Swift

```swift
class Solution {
    func maxDepth(_ s: String) -> Int {
        var current = 0
        var maxDepth = 0
        for ch in s {
            if ch == "(" {
                current += 1
                if current > maxDepth { maxDepth = current }
            } else if ch == ")" {
                current -= 1
            }
        }
        return maxDepth
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDepth(s: String): Int {
        var maxDepth = 0
        var current = 0
        for (ch in s) {
            when (ch) {
                '(' -> {
                    current++
                    if (current > maxDepth) maxDepth = current
                }
                ')' -> current--
            }
        }
        return maxDepth
    }
}
```

## Dart

```dart
class Solution {
  int maxDepth(String s) {
    int maxDepth = 0;
    int current = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        current++;
        if (current > maxDepth) maxDepth = current;
      } else if (s[i] == ')') {
        current--;
      }
    }
    return maxDepth;
  }
}
```

## Golang

```go
func maxDepth(s string) int {
    depth, max := 0, 0
    for i := 0; i < len(s); i++ {
        switch s[i] {
        case '(':
            depth++
            if depth > max {
                max = depth
            }
        case ')':
            depth--
        }
    }
    return max
}
```

## Ruby

```ruby
def max_depth(s)
  depth = 0
  current = 0
  s.each_char do |ch|
    if ch == '('
      current += 1
      depth = [depth, current].max
    elsif ch == ')'
      current -= 1
    end
  end
  depth
end
```

## Scala

```scala
object Solution {
    def maxDepth(s: String): Int = {
        var current = 0
        var ans = 0
        for (ch <- s) {
            if (ch == '(') {
                current += 1
                if (current > ans) ans = current
            } else if (ch == ')') {
                current -= 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut current = 0;
        let mut max_depth = 0;
        for c in s.chars() {
            if c == '(' {
                current += 1;
                if current > max_depth {
                    max_depth = current;
                }
            } else if c == ')' {
                current -= 1;
            }
        }
        max_depth as i32
    }
}
```

## Racket

```racket
(define/contract (max-depth s)
  (-> string? exact-integer?)
  (let loop ((i 0) (open 0) (ans 0))
    (if (= i (string-length s))
        ans
        (let* ((c (string-ref s i))
               (new-open (cond [(char=? c #\() (+ open 1)]
                               [(char=? c #\)) (- open 1)]
                               [else open]))
               (new-ans (max ans new-open)))
          (loop (+ i 1) new-open new-ans)))))
```

## Erlang

```erlang
-spec max_depth(S :: unicode:unicode_binary()) -> integer().
max_depth(S) ->
    loop(S, 0, 0).

loop(<<>>, _Count, Max) ->
    Max;
loop(<<$(, Rest/binary>>, Count, Max) ->
    NewCount = Count + 1,
    NewMax = erlang:max(NewCount, Max),
    loop(Rest, NewCount, NewMax);
loop(<<$), Rest/binary>>, Count, Max) ->
    loop(Rest, Count - 1, Max);
loop(<<_, Rest/binary>>, Count, Max) ->
    loop(Rest, Count, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_depth(s :: String.t) :: integer
  def max_depth(s) do
    {max, _} =
      :binary.bin_to_list(s)
      |> Enum.reduce({0, 0}, fn
        ?(, {mx, cur} ->
          cur = cur + 1
          mx = if cur > mx, do: cur, else: mx
          {mx, cur}

        ?), {mx, cur} ->
          {mx, cur - 1}

        _, acc ->
          acc
      end)

    max
  end
end
```
