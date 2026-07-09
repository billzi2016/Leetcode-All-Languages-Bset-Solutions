# 3168. Minimum Number of Chairs in a Waiting Room

## Cpp

```cpp
class Solution {
public:
    int minimumChairs(string s) {
        int cur = 0, ans = 0;
        for (char c : s) {
            if (c == 'E') ++cur;
            else --cur; // c == 'L'
            ans = max(ans, cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumChairs(String s) {
        int current = 0;
        int maxNeeded = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'E') {
                current++;
                if (current > maxNeeded) {
                    maxNeeded = current;
                }
            } else { // 'L'
                current--;
            }
        }
        return maxNeeded;
    }
}
```

## Python

```python
class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        ans = 0
        for ch in s:
            if ch == 'E':
                cur += 1
                if cur > ans:
                    ans = cur
            else:  # 'L'
                cur -= 1
        return ans
```

## Python3

```python
class Solution:
    def minimumChairs(self, s: str) -> int:
        cur = 0
        ans = 0
        for ch in s:
            if ch == 'E':
                cur += 1
                if cur > ans:
                    ans = cur
            else:  # 'L'
                cur -= 1
        return ans
```

## C

```c
int minimumChairs(char* s) {
    int cur = 0, max = 0;
    while (*s) {
        if (*s == 'E') {
            cur++;
            if (cur > max) max = cur;
        } else if (*s == 'L') {
            cur--;
        }
        s++;
    }
    return max;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumChairs(string s)
    {
        int current = 0;
        int max = 0;
        foreach (char c in s)
        {
            if (c == 'E')
                current++;
            else // 'L'
                current--;
            if (current > max)
                max = current;
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumChairs = function(s) {
    let current = 0;
    let maxNeeded = 0;
    for (const ch of s) {
        if (ch === 'E') {
            current++;
        } else { // 'L'
            current--;
        }
        if (current > maxNeeded) {
            maxNeeded = current;
        }
    }
    return maxNeeded;
};
```

## Typescript

```typescript
function minimumChairs(s: string): number {
    let current = 0;
    let maxNeeded = 0;
    for (const ch of s) {
        if (ch === 'E') {
            current++;
        } else { // 'L'
            current--;
        }
        if (current > maxNeeded) {
            maxNeeded = current;
        }
    }
    return maxNeeded;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumChairs($s) {
        $current = 0;
        $max = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === 'E') {
                $current++;
                if ($current > $max) {
                    $max = $current;
                }
            } else { // 'L'
                $current--;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func minimumChairs(_ s: String) -> Int {
        var current = 0
        var maxCount = 0
        for ch in s {
            if ch == "E" {
                current += 1
                if current > maxCount {
                    maxCount = current
                }
            } else { // 'L'
                current -= 1
            }
        }
        return maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumChairs(s: String): Int {
        var current = 0
        var maxNeeded = 0
        for (c in s) {
            if (c == 'E') {
                current++
                if (current > maxNeeded) maxNeeded = current
            } else { // 'L'
                current--
            }
        }
        return maxNeeded
    }
}
```

## Dart

```dart
class Solution {
  int minimumChairs(String s) {
    int current = 0;
    int maxPeople = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == 'E') {
        current++;
      } else { // 'L'
        current--;
      }
      if (current > maxPeople) {
        maxPeople = current;
      }
    }
    return maxPeople;
  }
}
```

## Golang

```go
func minimumChairs(s string) int {
    cur, max := 0, 0
    for _, ch := range s {
        if ch == 'E' {
            cur++
            if cur > max {
                max = cur
            }
        } else { // 'L'
            cur--
        }
    }
    return max
}
```

## Ruby

```ruby
def minimum_chairs(s)
  current = 0
  max_needed = 0
  s.each_char do |ch|
    if ch == 'E'
      current += 1
    else # 'L'
      current -= 1
    end
    max_needed = [max_needed, current].max
  end
  max_needed
end
```

## Scala

```scala
object Solution {
    def minimumChairs(s: String): Int = {
        var current = 0
        var maxNeeded = 0
        for (c <- s) {
            if (c == 'E') current += 1 else current -= 1
            if (current > maxNeeded) maxNeeded = current
        }
        maxNeeded
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_chairs(s: String) -> i32 {
        let mut current = 0;
        let mut max_needed = 0;
        for ch in s.chars() {
            if ch == 'E' {
                current += 1;
                if current > max_needed {
                    max_needed = current;
                }
            } else { // 'L'
                current -= 1;
            }
        }
        max_needed as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-chairs s)
  (-> string? exact-integer?)
  (let loop ((i 0) (curr 0) (maxc 0))
    (if (= i (string-length s))
        maxc
        (let* ((ch (string-ref s i))
               (new-curr (if (char=? ch #\E) (+ curr 1) (- curr 1)))
               (new-max (max maxc new-curr)))
          (loop (+ i 1) new-curr new-max)))))
```

## Erlang

```erlang
-spec minimum_chairs(S :: unicode:unicode_binary()) -> integer().
minimum_chairs(S) ->
    {_, Max} = lists:foldl(
        fun
            ($E, {Curr, Max}) ->
                NewCurr = Curr + 1,
                {NewCurr, erlang:max(NewCurr, Max)};
            ($L, {Curr, Max}) ->
                {Curr - 1, Max}
        end,
        {0, 0},
        binary_to_list(S)
    ),
    Max.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_chairs(String.t()) :: integer()
  def minimum_chairs(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({0, 0}, fn
      "E", {curr, max} ->
        new = curr + 1
        {new, if(new > max, do: new, else: max)}
      "L", {curr, max} ->
        new = curr - 1
        {new, max}
    end)
    |> elem(1)
  end
end
```
