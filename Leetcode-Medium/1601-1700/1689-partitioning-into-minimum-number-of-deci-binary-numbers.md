# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

## Cpp

```cpp
class Solution {
public:
    int minPartitions(string n) {
        int ans = 0;
        for (char c : n) {
            ans = max(ans, c - '0');
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minPartitions(String n) {
        int max = 0;
        for (int i = 0; i < n.length(); i++) {
            int digit = n.charAt(i) - '0';
            if (digit > max) {
                max = digit;
                if (max == 9) break; // early exit, cannot be higher
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        max_digit = 0
        for ch in n:
            d = ord(ch) - 48  # faster than int()
            if d > max_digit:
                max_digit = d
                if max_digit == 9:  # early exit, can't get higher
                    break
        return max_digit
```

## Python3

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for ch in n:
            d = ord(ch) - 48  # faster than int()
            if d > max_digit:
                max_digit = d
                if max_digit == 9:  # early exit, cannot be higher
                    break
        return max_digit
```

## C

```c
int minPartitions(char* n) {
    int maxDigit = 0;
    for (int i = 0; n[i]; ++i) {
        int d = n[i] - '0';
        if (d > maxDigit) {
            maxDigit = d;
            if (maxDigit == 9) break;
        }
    }
    return maxDigit;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinPartitions(string n)
    {
        int maxDigit = 0;
        foreach (char c in n)
        {
            int digit = c - '0';
            if (digit > maxDigit)
                maxDigit = digit;
            // early exit if max possible reached (9)
            if (maxDigit == 9) break;
        }
        return maxDigit;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    let maxDigit = 0;
    for (let i = 0; i < n.length; i++) {
        const d = n.charCodeAt(i) - 48; // convert char to digit
        if (d > maxDigit) {
            maxDigit = d;
            if (maxDigit === 9) break; // early exit, can't get higher
        }
    }
    return maxDigit;
};
```

## Typescript

```typescript
function minPartitions(n: string): number {
    let maxDigit = 0;
    for (let i = 0; i < n.length; i++) {
        const digit = n.charCodeAt(i) - 48; // '0' char code is 48
        if (digit > maxDigit) {
            maxDigit = digit;
            if (maxDigit === 9) break; // early exit, cannot exceed 9
        }
    }
    return maxDigit;
}
```

## Php

```php
class Solution {

    /**
     * @param String $n
     * @return Integer
     */
    function minPartitions($n) {
        $max = 0;
        $len = strlen($n);
        for ($i = 0; $i < $len; $i++) {
            $digit = ord($n[$i]) - 48; // '0' ASCII is 48
            if ($digit > $max) {
                $max = $digit;
                if ($max == 9) { // early exit, cannot be higher
                    break;
                }
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func minPartitions(_ n: String) -> Int {
        var maxDigit = 0
        for ch in n {
            if let digit = ch.wholeNumberValue, digit > maxDigit {
                maxDigit = digit
            }
        }
        return maxDigit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minPartitions(n: String): Int {
        var maxDigit = 0
        for (c in n) {
            val digit = c - '0'
            if (digit > maxDigit) {
                maxDigit = digit
                if (maxDigit == 9) break
            }
        }
        return maxDigit
    }
}
```

## Dart

```dart
class Solution {
  int minPartitions(String n) {
    int maxDigit = 0;
    for (int i = 0; i < n.length; i++) {
      int d = n.codeUnitAt(i) - 48; // '0' ascii is 48
      if (d > maxDigit) {
        maxDigit = d;
        if (maxDigit == 9) break; // early exit, cannot be larger than 9
      }
    }
    return maxDigit;
  }
}
```

## Golang

```go
func minPartitions(n string) int {
	maxDigit := 0
	for i := 0; i < len(n); i++ {
		d := int(n[i] - '0')
		if d > maxDigit {
			maxDigit = d
			if maxDigit == 9 {
				// maximum possible digit reached, can break early if desired
			}
		}
	}
	return maxDigit
}
```

## Ruby

```ruby
def min_partitions(n)
  max_digit = 0
  n.each_byte do |c|
    digit = c - 48
    max_digit = digit if digit > max_digit
  end
  max_digit
end
```

## Scala

```scala
object Solution {
    def minPartitions(n: String): Int = {
        var maxDigit = 0
        for (c <- n) {
            val d = c - '0'
            if (d > maxDigit) maxDigit = d
        }
        maxDigit
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        n.bytes()
            .map(|b| (b - b'0') as i32)
            .max()
            .unwrap_or(0)
    }
}
```

## Racket

```racket
#lang racket

(define/contract (min-partitions n)
  (-> string? exact-integer?)
  (for/fold ([m 0]) ([c (in-string n)])
    (max m (- (char->integer c) (char->integer #\0)))))
```

## Erlang

```erlang
-module(solution).
-export([min_partitions/1]).

-spec min_partitions(N :: unicode:unicode_binary()) -> integer().
min_partitions(N) ->
    min_partitions(N, 0).

min_partitions(<<>>, Max) ->
    Max;
min_partitions(<<Digit, Rest/binary>>, Max) when Digit >= $0, Digit =< $9 ->
    Val = Digit - $0,
    NewMax = if Val > Max -> Val; true -> Max end,
    min_partitions(Rest, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_partitions(n :: String.t) :: integer
  def min_partitions(n) do
    n
    |> String.to_charlist()
    |> Enum.reduce(0, fn ch, acc ->
      digit = ch - ?0
      if digit > acc, do: digit, else: acc
    end)
  end
end
```
