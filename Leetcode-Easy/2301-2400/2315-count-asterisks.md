# 2315. Count Asterisks

## Cpp

```cpp
class Solution {
public:
    int countAsterisks(string s) {
        bool inside = false;
        int cnt = 0;
        for (char c : s) {
            if (c == '|') {
                inside = !inside;
            } else if (c == '*' && !inside) {
                ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countAsterisks(String s) {
        int count = 0;
        boolean inside = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '|') {
                inside = !inside;
            } else if (c == '*' && !inside) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        inside = False
        count = 0
        for ch in s:
            if ch == '|':
                inside = not inside
            elif ch == '*' and not inside:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        inside = False
        for ch in s:
            if ch == '|':
                inside = not inside
            elif ch == '*' and not inside:
                ans += 1
        return ans
```

## C

```c
int countAsterisks(char* s) {
    int count = 0;
    int inside = 0; // 0: outside any pair, 1: inside a pair of '|'
    for (char *p = s; *p != '\0'; ++p) {
        if (*p == '|') {
            inside ^= 1; // toggle state
        } else if (*p == '*' && !inside) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountAsterisks(string s) {
        bool inside = false;
        int count = 0;
        foreach (char ch in s) {
            if (ch == '|') {
                inside = !inside;
            } else if (!inside && ch == '*') {
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countAsterisks = function(s) {
    let inPipe = false;
    let count = 0;
    for (let ch of s) {
        if (ch === '|') {
            inPipe = !inPipe;
        } else if (ch === '*' && !inPipe) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countAsterisks(s: string): number {
    let inside = false;
    let count = 0;
    for (const ch of s) {
        if (ch === '|') {
            inside = !inside;
        } else if (ch === '*' && !inside) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countAsterisks($s) {
        $count = 0;
        $inside = false;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch === '|') {
                $inside = !$inside;
            } elseif ($ch === '*') {
                if (!$inside) {
                    $count++;
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countAsterisks(_ s: String) -> Int {
        var inside = false
        var result = 0
        for ch in s {
            if ch == "|" {
                inside.toggle()
            } else if ch == "*" && !inside {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countAsterisks(s: String): Int {
        var inside = false
        var count = 0
        for (ch in s) {
            when (ch) {
                '|' -> inside = !inside
                '*' -> if (!inside) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countAsterisks(String s) {
    bool inside = false;
    int count = 0;
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (ch == '|') {
        inside = !inside;
      } else if (!inside && ch == '*') {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countAsterisks(s string) int {
	count := 0
	inside := false
	for _, ch := range s {
		if ch == '|' {
			inside = !inside
		} else if ch == '*' && !inside {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_asterisks(s)
  inside = false
  count = 0
  s.each_char do |ch|
    if ch == '|'
      inside = !inside
    elsif ch == '*'
      count += 1 unless inside
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countAsterisks(s: String): Int = {
        var count = 0
        var inside = false
        for (c <- s) {
            c match {
                case '|' => inside = !inside
                case '*' if !inside => count += 1
                case _ => // do nothing
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_asterisks(s: String) -> i32 {
        let mut inside = false;
        let mut count = 0;
        for ch in s.chars() {
            if ch == '|' {
                inside = !inside;
            } else if ch == '*' && !inside {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-asterisks s)
  (-> string? exact-integer?)
  (let-values ([(cnt _)
                (for/fold ([cnt 0] [inside #f])
                          ([i (in-range (string-length s))])
                  (define ch (string-ref s i))
                  (cond [(char=? ch #\|) (values cnt (not inside))]
                        [(and (char=? ch #\*) (not inside)) (values (+ cnt 1) inside)]
                        [else (values cnt inside)])))])
    cnt))
```

## Erlang

```erlang
-spec count_asterisks(S :: unicode:unicode_binary()) -> integer().
count_asterisks(S) ->
    count_asterisks(S, false, 0).

count_asterisks(<<>>, _InBar, Acc) ->
    Acc;
count_asterisks(<<$|, Rest/binary>>, InBar, Acc) ->
    count_asterisks(Rest, not InBar, Acc);
count_asterisks(<<$*, Rest/binary>>, false, Acc) ->
    count_asterisks(Rest, false, Acc + 1);
count_asterisks(<<_, Rest/binary>>, InBar, Acc) ->
    count_asterisks(Rest, InBar, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_asterisks(s :: String.t) :: integer
  def count_asterisks(s) do
    {count, _} =
      s
      |> String.graphemes()
      |> Enum.reduce({0, false}, fn
        "|", {cnt, inside} -> {cnt, not inside}
        "*", {cnt, false} -> {cnt + 1, false}
        _, acc -> acc
      end)

    count
  end
end
```
