# 2180. Count Integers With Even Digit Sum

## Cpp

```cpp
class Solution {
public:
    int countEven(int num) {
        int cnt = 0;
        for (int i = 1; i <= num; ++i) {
            int x = i, sum = 0;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            if ((sum & 1) == 0) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countEven(int num) {
        int count = 0;
        for (int i = 1; i <= num; i++) {
            int sum = 0, x = i;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            if ((sum & 1) == 0) {
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
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        for i in range(1, num + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            if s % 2 == 0:
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(1, num + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            if s % 2 == 0:
                cnt += 1
        return cnt
```

## C

```c
int countEven(int num) {
    int cnt = 0;
    for (int i = 1; i <= num; ++i) {
        int sum = 0, x = i;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if ((sum & 1) == 0) cnt++;
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountEven(int num)
    {
        int count = 0;
        for (int i = 1; i <= num; i++)
        {
            int sum = 0, x = i;
            while (x > 0)
            {
                sum += x % 10;
                x /= 10;
            }
            if ((sum & 1) == 0)
                count++;
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
var countEven = function(num) {
    let count = 0;
    for (let i = 1; i <= num; i++) {
        let sum = 0, x = i;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        if ((sum & 1) === 0) count++;
    }
    return count;
};
```

## Typescript

```typescript
function countEven(num: number): number {
    let count = 0;
    for (let i = 1; i <= num; i++) {
        let sum = 0;
        let x = i;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        if ((sum & 1) === 0) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function countEven($num) {
        $cnt = 0;
        for ($i = 1; $i <= $num; $i++) {
            $sum = 0;
            $x = $i;
            while ($x > 0) {
                $sum += $x % 10;
                $x = intdiv($x, 10);
            }
            if (($sum & 1) == 0) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
?>
```

## Swift

```swift
class Solution {
    func countEven(_ num: Int) -> Int {
        var count = 0
        for i in 1...num {
            var x = i
            var sum = 0
            while x > 0 {
                sum += x % 10
                x /= 10
            }
            if sum % 2 == 0 {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countEven(num: Int): Int {
        var count = 0
        for (i in 1..num) {
            var sum = 0
            var x = i
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            if (sum % 2 == 0) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countEven(int num) {
    int count = 0;
    for (int i = 1; i <= num; i++) {
      int sum = 0;
      int x = i;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      if (sum % 2 == 0) count++;
    }
    return count;
  }
}
```

## Golang

```go
func countEven(num int) int {
    cnt := 0
    for i := 1; i <= num; i++ {
        sum := 0
        x := i
        for x > 0 {
            sum += x % 10
            x /= 10
        }
        if sum%2 == 0 {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_even(num)
  count = 0
  (1..num).each do |i|
    sum = 0
    n = i
    while n > 0
      sum += n % 10
      n /= 10
    end
    count += 1 if sum.even?
  end
  count
end
```

## Scala

```scala
object Solution {
    def countEven(num: Int): Int = {
        var count = 0
        for (i <- 1 to num) {
            var sum = 0
            var x = i
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            if (sum % 2 == 0) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_even(num: i32) -> i32 {
        let mut count = 0;
        for mut x in 1..=num {
            let mut sum = 0;
            while x > 0 {
                sum += x % 10;
                x /= 10;
            }
            if sum % 2 == 0 {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-even num)
  (-> exact-integer? exact-integer?)
  (let loop ((i 1) (cnt 0))
    (if (> i num)
        cnt
        (let ((s (let digit-sum ((x i) (acc 0))
                   (if (= x 0)
                       acc
                       (digit-sum (quotient x 10) (+ acc (remainder x 10)))))))
          (loop (add1 i) (if (even? s) (add1 cnt) cnt))))) )
```

## Erlang

```erlang
-spec count_even(Num :: integer()) -> integer().
count_even(Num) when Num >= 0 ->
    count_even_helper(Num, 0).

-spec count_even_helper(integer(), integer()) -> integer().
count_even_helper(0, Acc) -> Acc;
count_even_helper(N, Acc) ->
    NewAcc = case sum_digits(N) rem 2 of
                0 -> Acc + 1;
                _ -> Acc
            end,
    count_even_helper(N - 1, NewAcc).

-spec sum_digits(integer()) -> integer().
sum_digits(0) -> 0;
sum_digits(N) when N > 0 ->
    (N rem 10) + sum_digits(N div 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_even(num :: integer) :: integer
  def count_even(num) when is_integer(num) and num >= 1 do
    1..num
    |> Enum.count(fn n -> even_digit_sum?(n) end)
  end

  defp even_digit_sum?(n) do
    n
    |> Integer.digits()
    |> Enum.sum()
    |> rem(2) == 0
  end
end
```
