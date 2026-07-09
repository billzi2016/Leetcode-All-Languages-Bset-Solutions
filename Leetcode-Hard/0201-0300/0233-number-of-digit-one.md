# 0233. Number of Digit One

## Cpp

```cpp
class Solution {
public:
    int countDigitOne(int n) {
        long long count = 0;
        for (long long i = 1; i <= n; i *= 10) {
            long long high = n / (i * 10);
            long long cur = (n / i) % 10;
            long long low = n % i;
            if (cur == 0) {
                count += high * i;
            } else if (cur == 1) {
                count += high * i + low + 1;
            } else {
                count += (high + 1) * i;
            }
        }
        return static_cast<int>(count);
    }
};
```

## Java

```java
class Solution {
    public int countDigitOne(int n) {
        long count = 0;
        for (long i = 1; i <= n; i *= 10) {
            long divisor = i * 10;
            long fullCycles = n / divisor;
            count += fullCycles * i;
            long remainder = n % divisor;
            long extra = Math.min(Math.max(remainder - i + 1, 0), i);
            count += extra;
        }
        return (int) count;
    }
}
```

## Python

```python
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while i <= n:
            high = n // (i * 10)
            cur = (n // i) % 10
            low = n % i
            if cur == 0:
                count += high * i
            elif cur == 1:
                count += high * i + low + 1
            else:
                count += (high + 1) * i
            i *= 10
        return count
```

## Python3

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            high = n // (i * 10)
            cur = (n // i) % 10
            low = n % i
            if cur == 0:
                count += high * i
            elif cur == 1:
                count += high * i + low + 1
            else:
                count += (high + 1) * i
            i *= 10
        return count
```

## C

```c
int countDigitOne(int n) {
    long long count = 0;
    for (long long i = 1; i <= n; i *= 10) {
        long long divider = i * 10;
        long long fullCycles = n / divider;
        count += fullCycles * i;
        long long remainder = n % divider;
        long long extra = remainder - i + 1;
        if (extra < 0) extra = 0;
        if (extra > i) extra = i;
        count += extra;
    }
    return (int)count;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountDigitOne(int n)
    {
        long count = 0;
        long i = 1;
        long N = n;
        while (i <= N)
        {
            long divider = i * 10;
            long fullCycles = N / divider;
            count += fullCycles * i;

            long remainder = N % divider;
            long extra = remainder - i + 1;
            if (extra < 0) extra = 0;
            if (extra > i) extra = i;
            count += extra;

            i *= 10;
        }
        return (int)count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countDigitOne = function(n) {
    let count = 0;
    for (let i = 1; i <= n; i *= 10) {
        const high = Math.floor(n / (i * 10));
        const cur = Math.floor((n / i) % 10);
        const low = n % i;

        count += high * i;
        if (cur === 1) {
            count += low + 1;
        } else if (cur > 1) {
            count += i;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countDigitOne(n: number): number {
    let count = 0;
    for (let i = 1; i <= n; i *= 10) {
        const divisor = i * 10;
        const fullCycles = Math.floor(n / divisor);
        count += fullCycles * i;
        const remainder = n % divisor;
        const extra = Math.min(Math.max(remainder - i + 1, 0), i);
        count += extra;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countDigitOne($n) {
        $count = 0;
        for ($i = 1; $i <= $n; $i *= 10) {
            $divider = $i * 10;
            $fullCycles = intdiv($n, $divider);
            $count += $fullCycles * $i;

            $remainder = $n % $divider;
            $extra = $remainder - $i + 1;
            if ($extra > $i) {
                $extra = $i;
            }
            if ($extra < 0) {
                $extra = 0;
            }
            $count += $extra;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countDigitOne(_ n: Int) -> Int {
        var count: Int64 = 0
        var factor: Int64 = 1
        let N = Int64(n)
        while factor <= N {
            let lower = N % factor
            let cur = (N / factor) % 10
            let higher = N / (factor * 10)
            if cur == 0 {
                count += higher * factor
            } else if cur == 1 {
                count += higher * factor + lower + 1
            } else {
                count += (higher + 1) * factor
            }
            factor *= 10
        }
        return Int(count)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDigitOne(n: Int): Int {
        var count = 0L
        var i = 1L
        val N = n.toLong()
        while (i <= N) {
            val divisor = i * 10
            val fullCycles = N / divisor
            count += fullCycles * i
            val remainder = N % divisor
            val extra = kotlin.math.min(kotlin.math.max(remainder - i + 1, 0L), i)
            count += extra
            i *= 10
        }
        return count.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countDigitOne(int n) {
    int count = 0;
    for (int i = 1; i <= n; i *= 10) {
      int high = n ~/ (i * 10);
      int cur = (n ~/ i) % 10;
      int low = n % i;
      if (cur == 0) {
        count += high * i;
      } else if (cur == 1) {
        count += high * i + low + 1;
      } else {
        count += (high + 1) * i;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countDigitOne(n int) int {
    if n <= 0 {
        return 0
    }
    var count int64
    num := int64(n)
    for i := int64(1); i <= num; i *= 10 {
        high := num / (i * 10)
        cur := (num / i) % 10
        low := num % i

        if cur == 0 {
            count += high * i
        } else if cur == 1 {
            count += high*i + low + 1
        } else {
            count += (high + 1) * i
        }
    }
    return int(count)
}
```

## Ruby

```ruby
def count_digit_one(n)
  count = 0
  i = 1
  while i <= n
    higher = n / (i * 10)
    current = (n / i) % 10
    lower = n % i

    if current == 0
      count += higher * i
    elsif current == 1
      count += higher * i + lower + 1
    else
      count += (higher + 1) * i
    end

    i *= 10
  end
  count
end
```

## Scala

```scala
object Solution {
    def countDigitOne(n: Int): Int = {
        var count: Long = 0L
        var i: Long = 1L
        val N: Long = n.toLong
        while (i <= N) {
            val divisor = i * 10L
            val fullCycles = N / divisor
            count += fullCycles * i
            val remainder = N % divisor
            val extra = math.min(math.max(remainder - i + 1, 0L), i)
            count += extra
            i *= 10L
        }
        count.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_digit_one(n: i32) -> i32 {
        let mut count: i64 = 0;
        let mut factor: i64 = 1;
        let n64 = n as i64;
        while factor <= n64 {
            let lower = n64 % factor;
            let cur = (n64 / factor) % 10;
            let higher = n64 / (factor * 10);
            count += higher * factor;
            if cur == 0 {
                // nothing
            } else if cur == 1 {
                count += lower + 1;
            } else {
                count += factor;
            }
            factor *= 10;
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-digit-one n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 1) (ans 0))
    (if (> i n)
        ans
        (let* ((high (quotient n (* i 10)))
               (cur (remainder (quotient n i) 10))
               (low (remainder n i))
               (add (cond [(= cur 0) (* high i)]
                          [(= cur 1) (+ (* high i) low 1)]
                          [else (* (+ high 1) i)])))
          (loop (* i 10) (+ ans add))))))
```

## Erlang

```erlang
-spec count_digit_one(N :: integer()) -> integer().
count_digit_one(N) when N >= 0 ->
    count_digit_one(N, 1, 0).

count_digit_one(N, I, Acc) when I =< N ->
    High = N div (I * 10),
    Cur = (N div I) rem 10,
    Low = N rem I,
    Add = High * I + case Cur of
        C when C > 1 -> I;
        1 -> Low + 1;
        _ -> 0
    end,
    count_digit_one(N, I * 10, Acc + Add);
count_digit_one(_N, _I, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_digit_one(n :: integer) :: integer
  def count_digit_one(n) when n <= 0, do: 0
  def count_digit_one(n), do: helper(n, 1, 0)

  defp helper(_n, i, acc) when i > _n, do: acc

  defp helper(n, i, acc) do
    high = div(n, i * 10)
    curr = rem(div(n, i), 10)
    low = rem(n, i)

    add =
      cond do
        curr == 0 -> high * i
        curr == 1 -> high * i + low + 1
        true -> (high + 1) * i
      end

    helper(n, i * 10, acc + add)
  end
end
```
