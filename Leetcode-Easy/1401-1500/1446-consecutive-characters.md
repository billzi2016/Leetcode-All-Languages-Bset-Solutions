# 1446. Consecutive Characters

## Cpp

```cpp
class Solution {
public:
    int maxPower(string s) {
        int maxCount = 1;
        int cur = 1;
        for (int i = 1; i < (int)s.size(); ++i) {
            if (s[i] == s[i - 1]) {
                ++cur;
            } else {
                cur = 1;
            }
            if (cur > maxCount) maxCount = cur;
        }
        return maxCount;
    }
};
```

## Java

```java
class Solution {
    public int maxPower(String s) {
        int n = s.length();
        int maxCount = 1;
        int count = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1;
            }
            if (count > maxCount) {
                maxCount = count;
            }
        }
        return maxCount;
    }
}
```

## Python

```python
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len = 1
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1
            if cur > max_len:
                max_len = cur
        return max_len
```

## Python3

```python
class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1
            if cur > max_len:
                max_len = cur
        return max_len
```

## C

```c
int maxPower(char* s) {
    if (!s || !*s) return 0;
    int maxCount = 1, count = 1;
    for (char *p = s + 1; *p; ++p) {
        if (*p == *(p - 1)) {
            ++count;
        } else {
            if (count > maxCount) maxCount = count;
            count = 1;
        }
    }
    if (count > maxCount) maxCount = count;
    return maxCount;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxPower(string s) {
        if (string.IsNullOrEmpty(s)) return 0;
        int max = 1, count = 1;
        for (int i = 1; i < s.Length; i++) {
            if (s[i] == s[i - 1]) {
                count++;
            } else {
                count = 1;
            }
            if (count > max) max = count;
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
var maxPower = function(s) {
    let maxCount = 1;
    let count = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            count++;
        } else {
            count = 1;
        }
        if (count > maxCount) {
            maxCount = count;
        }
    }
    return maxCount;
};
```

## Typescript

```typescript
function maxPower(s: string): number {
    if (s.length === 0) return 0;
    let max = 1;
    let cur = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            cur++;
        } else {
            cur = 1;
        }
        if (cur > max) max = cur;
    }
    return max;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxPower($s) {
        $n = strlen($s);
        if ($n == 0) return 0;
        $max = 1;
        $count = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) {
                $count++;
            } else {
                $count = 1;
            }
            if ($count > $max) {
                $max = $count;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxPower(_ s: String) -> Int {
        guard !s.isEmpty else { return 0 }
        let chars = Array(s)
        var maxPower = 1
        var current = 1
        for i in 1..<chars.count {
            if chars[i] == chars[i - 1] {
                current += 1
            } else {
                current = 1
            }
            if current > maxPower {
                maxPower = current
            }
        }
        return maxPower
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPower(s: String): Int {
        var maxCount = 1
        var count = 1
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1]) {
                count++
            } else {
                count = 1
            }
            if (count > maxCount) {
                maxCount = count
            }
        }
        return maxCount
    }
}
```

## Dart

```dart
class Solution {
  int maxPower(String s) {
    if (s.isEmpty) return 0;
    int maxCount = 1;
    int count = 1;
    for (int i = 1; i < s.length; i++) {
      if (s[i] == s[i - 1]) {
        count++;
      } else {
        count = 1;
      }
      if (count > maxCount) {
        maxCount = count;
      }
    }
    return maxCount;
  }
}
```

## Golang

```go
func maxPower(s string) int {
	if len(s) == 0 {
		return 0
	}
	maxCount, count := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			count++
		} else {
			count = 1
		}
		if count > maxCount {
			maxCount = count
		}
	}
	return maxCount
}
```

## Ruby

```ruby
def max_power(s)
  return 0 if s.empty?
  max_len = 1
  cur_len = 1
  (1...s.length).each do |i|
    if s[i] == s[i - 1]
      cur_len += 1
    else
      cur_len = 1
    end
    max_len = cur_len if cur_len > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def maxPower(s: String): Int = {
        if (s.isEmpty) return 0
        var maxCount = 1
        var count = 1
        var i = 1
        while (i < s.length) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count += 1
            } else {
                count = 1
            }
            if (count > maxCount) maxCount = count
            i += 1
        }
        maxCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_power(s: String) -> i32 {
        let bytes = s.as_bytes();
        if bytes.is_empty() {
            return 0;
        }
        let mut max_len = 1i32;
        let mut cur_len = 1i32;
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                cur_len += 1;
            } else {
                if cur_len > max_len {
                    max_len = cur_len;
                }
                cur_len = 1;
            }
        }
        if cur_len > max_len {
            max_len = cur_len;
        }
        max_len
    }
}
```

## Racket

```racket
(define/contract (max-power s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (prev (if (> n 0) (string-ref s 0) #\a))
         (count 1)
         (max-count 1))
    (for ([i (in-range 1 n)])
      (let ((c (string-ref s i)))
        (if (char=? c prev)
            (set! count (+ count 1))
            (begin
              (when (> count max-count) (set! max-count count))
              (set! count 1)
              (set! prev c)))))
    (max max-count count)))
```

## Erlang

```erlang
-spec max_power(S :: unicode:unicode_binary()) -> integer().
max_power(S) ->
    case S of
        <<>> -> 0;
        <<First, Rest/binary>> ->
            max_power_loop(Rest, First, 1, 1)
    end.

max_power_loop(<<>>, _Prev, _Curr, Max) -> Max;
max_power_loop(<<Next, Rest/binary>>, Prev, Curr, Max) ->
    if Next =:= Prev ->
            NewCurr = Curr + 1,
            NewMax = erlang:max(Max, NewCurr),
            max_power_loop(Rest, Prev, NewCurr, NewMax);
       true ->
            max_power_loop(Rest, Next, 1, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_power(s :: String.t()) :: integer()
  def max_power(s) do
    chars = String.graphemes(s)

    %{max: result} =
      Enum.reduce(chars, %{prev: nil, cur: 0, max: 0}, fn ch, acc ->
        if ch == acc.prev do
          cur = acc.cur + 1
          %{acc | cur: cur, max: max(cur, acc.max)}
        else
          cur = 1
          %{acc | prev: ch, cur: cur, max: max(1, acc.max)}
        end
      end)

    result
  end
end
```
