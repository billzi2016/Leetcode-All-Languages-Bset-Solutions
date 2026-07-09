# 0007. Reverse Integer

## Cpp

```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
```

## Java

```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) {
                return 0;
            }
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) {
                return 0;
            }
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

## Python

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs:
            pop = x_abs % 10
            x_abs //= 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        return sign * rev
```

## Python3

```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            pop = x % 10
            x //= 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        return sign * rev
```

## C

```c
#include <limits.h>

int reverse(int x) {
    int rev = 0;
    while (x != 0) {
        int pop = x % 10;
        x /= 10;
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7))
            return 0;
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8))
            return 0;
        rev = rev * 10 + pop;
    }
    return rev;
}
```

## Csharp

```csharp
public class Solution
{
    public int Reverse(int x)
    {
        int rev = 0;
        while (x != 0)
        {
            int pop = x % 10;
            x /= 10;

            if (rev > int.MaxValue / 10 || (rev == int.MaxValue / 10 && pop > 7))
                return 0;
            if (rev < int.MinValue / 10 || (rev == int.MinValue / 10 && pop < -8))
                return 0;

            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;
    let rev = 0;
    while (x !== 0) {
        const pop = x % 10;
        x = Math.trunc(x / 10);
        if (rev > Math.trunc(INT_MAX / 10) || (rev === Math.trunc(INT_MAX / 10) && pop > 7)) {
            return 0;
        }
        if (rev < Math.trunc(INT_MIN / 10) || (rev === Math.trunc(INT_MIN / 10) && pop < -8)) {
            return 0;
        }
        rev = rev * 10 + pop;
    }
    return rev;
};
```

## Typescript

```typescript
function reverse(x: number): number {
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;
    let rev = 0;
    while (x !== 0) {
        const pop = x % 10;
        x = Math.trunc(x / 10);
        if (rev > Math.floor(INT_MAX / 10) || (rev === Math.floor(INT_MAX / 10) && pop > 7)) {
            return 0;
        }
        if (rev < Math.ceil(INT_MIN / 10) || (rev === Math.ceil(INT_MIN / 10) && pop < -8)) {
            return 0;
        }
        rev = rev * 10 + pop;
    }
    return rev;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $INT_MAX = 2147483647;
        $INT_MIN = -2147483648;
        $rev = 0;
        while ($x != 0) {
            $pop = $x % 10;
            $x = intdiv($x, 10);
            if ($rev > intdiv($INT_MAX, 10) || ($rev == intdiv($INT_MAX, 10) && $pop > 7)) {
                return 0;
            }
            if ($rev < intdiv($INT_MIN, 10) || ($rev == intdiv($INT_MIN, 10) && $pop < -8)) {
                return 0;
            }
            $rev = $rev * 10 + $pop;
        }
        return $rev;
    }
}
```

## Swift

```swift
class Solution {
    func reverse(_ x: Int) -> Int {
        var num = x
        var rev = 0
        let INT_MAX = 2147483647
        let INT_MIN = -2147483648
        
        while num != 0 {
            let pop = num % 10
            num /= 10
            
            if rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7) {
                return 0
            }
            if rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8) {
                return 0
            }
            
            rev = rev * 10 + pop
        }
        
        return rev
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverse(x: Int): Int {
        var num = x
        var rev = 0
        while (num != 0) {
            val pop = num % 10
            num /= 10
            if (rev > Int.MAX_VALUE / 10 || (rev == Int.MAX_VALUE / 10 && pop > 7)) return 0
            if (rev < Int.MIN_VALUE / 10 || (rev == Int.MIN_VALUE / 10 && pop < -8)) return 0
            rev = rev * 10 + pop
        }
        return rev
    }
}
```

## Dart

```dart
class Solution {
  int reverse(int x) {
    const int INT_MAX = 2147483647;
    const int INT_MIN = -2147483648;
    int rev = 0;
    while (x != 0) {
      int pop = x % 10;
      if (x < 0 && pop > 0) {
        pop -= 10;
      }
      x = x ~/ 10;

      if (rev > INT_MAX ~/ 10 || (rev == INT_MAX ~/ 10 && pop > 7)) {
        return 0;
      }
      if (rev < INT_MIN ~/ 10 || (rev == INT_MIN ~/ 10 && pop < -8)) {
        return 0;
      }

      rev = rev * 10 + pop;
    }
    return rev;
  }
}
```

## Golang

```go
func reverse(x int) int {
	const (
		INT_MAX = 1<<31 - 1
		INT_MIN = -1 << 31
	)
	rev := 0
	for x != 0 {
		pop := x % 10
		x /= 10

		if rev > INT_MAX/10 || (rev == INT_MAX/10 && pop > 7) {
			return 0
		}
		if rev < INT_MIN/10 || (rev == INT_MIN/10 && pop < -8) {
			return 0
		}

		rev = rev*10 + pop
	}
	return rev
}
```

## Ruby

```ruby
def reverse(x)
  int_max = 2**31 - 1
  int_min = -2**31
  rev = 0
  while x != 0
    pop = x % 10
    if x < 0 && pop > 0
      pop -= 10
    end
    x = (x - pop) / 10

    return 0 if rev > int_max / 10 || (rev == int_max / 10 && pop > 7)
    return 0 if rev < int_min / 10 || (rev == int_min / 10 && pop < -8)

    rev = rev * 10 + pop
  end
  rev
end
```

## Scala

```scala
object Solution {
    def reverse(x: Int): Int = {
        var rev = 0
        var num = x
        while (num != 0) {
            val pop = num % 10
            num = num / 10
            if (rev > Int.MaxValue / 10 || (rev == Int.MaxValue / 10 && pop > 7)) return 0
            if (rev < Int.MinValue / 10 || (rev == Int.MinValue / 10 && pop < -8)) return 0
            rev = rev * 10 + pop
        }
        rev
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut x = x;
        let mut rev: i32 = 0;
        while x != 0 {
            let pop = x % 10;
            x /= 10;
            if rev > i32::MAX / 10 || (rev == i32::MAX / 10 && pop > 7) {
                return 0;
            }
            if rev < i32::MIN / 10 || (rev == i32::MIN / 10 && pop < -8) {
                return 0;
            }
            rev = rev * 10 + pop;
        }
        rev
    }
}
```

## Racket

```racket
(define/contract (reverse x)
  (-> exact-integer? exact-integer?)
  (let* ((INT_MAX 2147483647)
         (INT_MIN -2147483648)
         (MAX_DIV (quotient INT_MAX 10))
         (MIN_DIV (quotient INT_MIN 10))) ; = -214748364
    (let loop ((n x) (rev 0))
      (if (= n 0)
          rev
          (let* ((pop (remainder n 10))
                 (next (quotient n 10)))
            (cond
              [(or (> rev MAX_DIV)
                   (and (= rev MAX_DIV) (> pop 7))
                   (< rev MIN_DIV)
                   (and (= rev MIN_DIV) (< pop -8)))
               0]
              [else
               (loop next (+ (* rev 10) pop))]))))))
```

## Erlang

```erlang
-module(solution).
-export([reverse/1]).

-define(INT_MIN, -2147483648).
-define(INT_MAX, 2147483647).

-spec reverse(integer()) -> integer().
reverse(X) ->
    AbsX = if X < 0 -> -X; true -> X end,
    RevAbs = rev_loop(AbsX, 0),
    Result = if X < 0 -> -RevAbs; true -> RevAbs end,
    case Result of
        R when R >= ?INT_MIN, R =< ?INT_MAX -> R;
        _ -> 0
    end.

rev_loop(0, Rev) ->
    Rev;
rev_loop(N, Rev) ->
    Pop = N rem 10,
    N1 = N div 10,
    rev_loop(N1, Rev * 10 + Pop).
```

## Elixir

```elixir
defmodule Solution do
  @int_max 2_147_483_647
  @int_min -2_147_483_648
  @int_max_div_10 div(@int_max, 10)

  @spec reverse(x :: integer) :: integer
  def reverse(x) do
    sign = if x < 0, do: -1, else: 1
    n = abs(x)

    case rev_loop(n, 0) do
      {:ok, rev} ->
        result = rev * sign

        if result > @int_max or result < @int_min do
          0
        else
          result
        end

      :overflow ->
        0
    end
  end

  defp rev_loop(0, rev), do: {:ok, rev}

  defp rev_loop(n, rev) do
    pop = rem(n, 10)
    n2 = div(n, 10)

    if rev > @int_max_div_10 or (rev == @int_max_div_10 and pop > 7) do
      :overflow
    else
      new_rev = rev * 10 + pop
      rev_loop(n2, new_rev)
    end
  end
end
```
