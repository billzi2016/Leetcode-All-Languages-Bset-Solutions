# 3110. Score of a String

## Cpp

```cpp
class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for (size_t i = 1; i < s.size(); ++i) {
            score += abs(s[i] - s[i - 1]);
        }
        return score;
    }
};
```

## Java

```java
class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            score += Math.abs(s.charAt(i) - s.charAt(i + 1));
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total
```

## Python3

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        prev = ord(s[0])
        for ch in s[1:]:
            cur = ord(ch)
            total += abs(cur - prev)
            prev = cur
        return total
```

## C

```c
int scoreOfString(char* s) {
    int total = 0;
    for (int i = 0; s[i + 1] != '\0'; ++i) {
        int diff = s[i] - s[i + 1];
        if (diff < 0) diff = -diff;
        total += diff;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int ScoreOfString(string s)
    {
        int score = 0;
        for (int i = 0; i < s.Length - 1; i++)
        {
            score += Math.Abs(s[i] - s[i + 1]);
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
var scoreOfString = function(s) {
    let score = 0;
    for (let i = 1; i < s.length; ++i) {
        score += Math.abs(s.charCodeAt(i) - s.charCodeAt(i - 1));
    }
    return score;
};
```

## Typescript

```typescript
function scoreOfString(s: string): number {
    let total = 0;
    for (let i = 0; i < s.length - 1; i++) {
        total += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfString($s) {
        $score = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len - 1; $i++) {
            $score += abs(ord($s[$i]) - ord($s[$i + 1]));
        }
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func scoreOfString(_ s: String) -> Int {
        let scalars = Array(s.unicodeScalars)
        var total = 0
        for i in 0..<(scalars.count - 1) {
            let diff = Int(scalars[i].value) - Int(scalars[i + 1].value)
            total += abs(diff)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun scoreOfString(s: String): Int {
        var score = 0
        for (i in 0 until s.length - 1) {
            score += kotlin.math.abs(s[i].code - s[i + 1].code)
        }
        return score
    }
}
```

## Dart

```dart
class Solution {
  int scoreOfString(String s) {
    int total = 0;
    for (int i = 0; i < s.length - 1; ++i) {
      total += (s.codeUnitAt(i) - s.codeUnitAt(i + 1)).abs();
    }
    return total;
  }
}
```

## Golang

```go
func scoreOfString(s string) int {
    total := 0
    for i := 0; i < len(s)-1; i++ {
        diff := int(s[i]) - int(s[i+1])
        if diff < 0 {
            diff = -diff
        }
        total += diff
    }
    return total
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def score_of_string(s)
  score = 0
  (0...s.length-1).each do |i|
    score += (s[i].ord - s[i+1].ord).abs
  end
  score
end
```

## Scala

```scala
object Solution {
    def scoreOfString(s: String): Int = {
        var sum = 0
        for (i <- 0 until s.length - 1) {
            sum += Math.abs(s.charAt(i) - s.charAt(i + 1))
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0i32;
        for i in 0..b.len() - 1 {
            ans += (b[i] as i32 - b[i + 1] as i32).abs();
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (score-of-string s)
  (-> string? exact-integer?)
  (let ((len (string-length s)))
    (for/sum ([i (in-range (- len 1))])
      (abs (- (char->integer (string-ref s i))
              (char->integer (string-ref s (+ i 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([score_of_string/1]).

-spec score_of_string(S :: unicode:unicode_binary()) -> integer().
score_of_string(S) ->
    case S of
        <<First, Rest/binary>> ->
            loop(First, Rest, 0);
        _ -> 
            0
    end.

loop(_Prev, <<>>, Acc) -> Acc;
loop(Prev, <<Curr, Rest/binary>>, Acc) ->
    loop(Curr, Rest, Acc + erlang:abs(Prev - Curr)).
```

## Elixir

```elixir
defmodule Solution do
  @spec score_of_string(s :: String.t()) :: integer()
  def score_of_string(s) do
    bytes = :binary.bin_to_list(s)
    calculate(bytes, 0)
  end

  defp calculate([_], acc), do: acc
  defp calculate([a, b | rest], acc) do
    calculate([b | rest], acc + abs(a - b))
  end
end
```
