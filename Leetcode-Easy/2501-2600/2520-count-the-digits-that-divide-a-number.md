# 2520. Count the Digits That Divide a Number

## Cpp

```cpp
class Solution {
public:
    int countDigits(int num) {
        int original = num;
        int count = 0;
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 && original % digit == 0) {
                ++count;
            }
            num /= 10;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int countDigits(int num) {
        int original = num;
        int count = 0;
        while (num > 0) {
            int digit = num % 10;
            if (digit != 0 && original % digit == 0) {
                count++;
            }
            num /= 10;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        n = num
        while n > 0:
            digit = n % 10
            if num % digit == 0:
                count += 1
            n //= 10
        return count
```

## Python3

```python
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            d = n % 10
            if d != 0 and num % d == 0:
                count += 1
            n //= 10
        return count
```

## C

```c
int countDigits(int num) {
    int count = 0;
    int temp = num;
    while (temp > 0) {
        int digit = temp % 10;
        if (digit != 0 && num % digit == 0) {
            ++count;
        }
        temp /= 10;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountDigits(int num) {
        int count = 0;
        int n = num;
        while (n > 0) {
            int digit = n % 10;
            if (num % digit == 0) {
                count++;
            }
            n /= 10;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var countDigits = function(num) {
    let count = 0;
    let n = num;
    while (n > 0) {
        const digit = n % 10;
        if (digit !== 0 && num % digit === 0) {
            count++;
        }
        n = Math.floor(n / 10);
    }
    return count;
};
```

## Typescript

```typescript
function countDigits(num: number): number {
    let count = 0;
    let n = num;
    while (n > 0) {
        const digit = n % 10;
        if (digit !== 0 && num % digit === 0) {
            count++;
        }
        n = Math.floor(n / 10);
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function countDigits($num) {
        $original = $num;
        $count = 0;
        while ($num > 0) {
            $digit = $num % 10;
            if ($digit != 0 && $original % $digit == 0) {
                $count++;
            }
            $num = intdiv($num, 10);
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countDigits(_ num: Int) -> Int {
        var count = 0
        var n = num
        while n > 0 {
            let digit = n % 10
            if digit != 0 && num % digit == 0 {
                count += 1
            }
            n /= 10
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDigits(num: Int): Int {
        var count = 0
        var n = num
        while (n > 0) {
            val d = n % 10
            if (d != 0 && num % d == 0) {
                count++
            }
            n /= 10
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countDigits(int num) {
    int count = 0;
    int n = num;
    while (n > 0) {
      int digit = n % 10;
      if (digit != 0 && num % digit == 0) {
        count++;
      }
      n ~/= 10;
    }
    return count;
  }
}
```

## Golang

```go
func countDigits(num int) int {
    count := 0
    n := num
    for n > 0 {
        digit := n % 10
        if digit != 0 && num%digit == 0 {
            count++
        }
        n /= 10
    }
    return count
}
```

## Ruby

```ruby
def count_digits(num)
  count = 0
  n = num
  while n > 0
    digit = n % 10
    count += 1 if num % digit == 0
    n /= 10
  end
  count
end
```

## Scala

```scala
object Solution {
    def countDigits(num: Int): Int = {
        var count = 0
        var n = num
        while (n > 0) {
            val digit = n % 10
            if (num % digit == 0) count += 1
            n /= 10
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        let mut count = 0;
        let mut n = num;
        while n > 0 {
            let digit = n % 10;
            if digit != 0 && num % digit == 0 {
                count += 1;
            }
            n /= 10;
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-digits num)
  (-> exact-integer? exact-integer?)
  (let loop ((n num) (cnt 0))
    (if (= n 0)
        cnt
        (let* ((digit (remainder n 10))
               (new-cnt (if (and (not (= digit 0))
                                 (= (remainder num digit) 0))
                            (+ cnt 1)
                            cnt)))
          (loop (quotient n 10) new-cnt)))))
```

## Erlang

```erlang
-module(solution).
-export([count_digits/1]).

-spec count_digits(Num :: integer()) -> integer().
count_digits(Num) ->
    count_digits_helper(Num, Num, 0).

count_digits_helper(_, 0, Acc) ->
    Acc;
count_digits_helper(Orig, N, Acc) ->
    D = N rem 10,
    NewAcc = case D of
        0 -> Acc; % zero digit not expected per constraints
        _ when Orig rem D == 0 -> Acc + 1;
        _ -> Acc
    end,
    count_digits_helper(Orig, N div 10, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_digits(num :: integer) :: integer
  def count_digits(num) do
    count_digits(num, num, 0)
  end

  defp count_digits(0, _original, acc), do: acc

  defp count_digits(n, original, acc) do
    digit = rem(n, 10)

    new_acc =
      if digit != 0 and rem(original, digit) == 0 do
        acc + 1
      else
        acc
      end

    count_digits(div(n, 10), original, new_acc)
  end
end
```
