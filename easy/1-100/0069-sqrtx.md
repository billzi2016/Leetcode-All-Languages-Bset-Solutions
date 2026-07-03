# 0069. Sqrt(x)

## Cpp

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        long long left = 1, right = x / 2, ans = 0;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long sq = mid * mid;
            if (sq == x) return static_cast<int>(mid);
            if (sq < x) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        long left = 1, right = x / 2L;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long div = x / mid;
            if (mid == div) {
                return (int)mid;
            } else if (mid > div) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return (int)right;
    }
}
```

## Python

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x // 2
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
```

## Python3

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid <= x // mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
```

## C

```c
int mySqrt(int x) {
    if (x < 2) return x;
    long long left = 1, right = x / 2;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long sq = mid * mid;
        if (sq == x) return (int)mid;
        if (sq < x)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return (int)right;
}
```

## Csharp

```csharp
public class Solution {
    public int MySqrt(int x) {
        if (x < 2) return x;
        long left = 1, right = x / 2;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long div = x / mid;
            if (mid == div) {
                return (int)mid;
            } else if (mid > div) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return (int)right;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) return x;
    let left = 1, right = Math.floor(x / 2), ans = 0;
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        const sq = mid * mid;
        if (sq === x) return mid;
        if (sq < x) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function mySqrt(x: number): number {
    if (x < 2) return x;
    let left = 1, right = Math.floor(x / 2);
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        const div = Math.floor(x / mid);
        if (mid === div) return mid;
        if (mid < div) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return right;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function mySqrt($x) {
        if ($x < 2) {
            return $x;
        }
        $left = 1;
        $right = intdiv($x, 2);
        $ans = 0;
        while ($left <= $right) {
            $mid = $left + intdiv($right - $left, 2);
            $quot = intdiv($x, $mid);
            if ($mid == $quot) {
                return $mid;
            } elseif ($mid < $quot) {
                $ans = $mid;
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func mySqrt(_ x: Int) -> Int {
        if x < 2 { return x }
        var left = 1
        var right = x / 2
        var ans = 0
        while left <= right {
            let mid = left + (right - left) / 2
            if mid <= x / mid {
                ans = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mySqrt(x: Int): Int {
        if (x < 2) return x
        var left = 1L
        var right = x / 2L
        while (left <= right) {
            val mid = left + (right - left) / 2
            val sq = mid * mid
            when {
                sq == x.toLong() -> return mid.toInt()
                sq < x -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return right.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int mySqrt(int x) {
    if (x < 2) return x;
    int left = 1;
    int right = x ~/ 2;
    int ans = 0;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      int div = x ~/ mid;
      if (mid == div) {
        return mid;
      } else if (mid < div) {
        ans = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func mySqrt(x int) int {
	if x < 2 {
		return x
	}
	left, right := 1, x/2
	ans := 0
	target := int64(x)
	for left <= right {
		mid := left + (right-left)/2
		sq := int64(mid) * int64(mid)
		if sq == target {
			return mid
		}
		if sq < target {
			ans = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
  return x if x < 2

  low = 1
  high = x / 2
  ans = 0

  while low <= high
    mid = (low + high) / 2
    sq = mid * mid

    if sq == x
      return mid
    elsif sq < x
      ans = mid
      low = mid + 1
    else
      high = mid - 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def mySqrt(x: Int): Int = {
        if (x < 2) return x
        var low: Long = 1
        var high: Long = x / 2
        var ans: Long = 0
        while (low <= high) {
            val mid = low + (high - low) / 2
            val sq = mid * mid
            if (sq == x) return mid.toInt
            else if (sq < x) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x < 2 {
            return x;
        }
        let mut left: i64 = 1;
        let mut right: i64 = x as i64;
        let mut ans: i64 = 0;
        while left <= right {
            let mid = (left + right) / 2;
            let sq = mid * mid;
            if sq == x as i64 {
                return mid as i32;
            } else if sq < x as i64 {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (my-sqrt x)
  (-> exact-integer? exact-integer?)
  (if (< x 2)
      x
      (let loop ((low 1) (high (quotient x 2)) (ans 0))
        (if (> low high)
            ans
            (let* ((mid (+ low (quotient (- high low) 2)))
                   (div (quotient x mid)))
              (if (<= mid div)
                  (loop (+ mid 1) high mid)
                  (loop low (- mid 1) ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([my_sqrt/1]).

-spec my_sqrt(X :: integer()) -> integer().
my_sqrt(X) when X >= 0 ->
    my_sqrt_bin(0, X, X).

my_sqrt_bin(Low, High, X) ->
    my_sqrt_bin(Low, High, X, 0).

my_sqrt_bin(Low, High, _X, Ans) when Low > High ->
    Ans;
my_sqrt_bin(Low, High, X, Ans) ->
    Mid = (Low + High) div 2,
    Prod = Mid * Mid,
    case Prod of
        P when P == X -> Mid;
        P when P < X -> my_sqrt_bin(Mid + 1, High, X, Mid);
        _ -> my_sqrt_bin(Low, Mid - 1, X, Ans)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec my_sqrt(x :: integer) :: integer
  def my_sqrt(x) when x < 2, do: x

  def my_sqrt(x) do
    bs(0, div(x, 2) + 1, x, 0)
  end

  defp bs(low, high, _x, ans) when low > high, do: ans

  defp bs(low, high, x, _ans) do
    mid = div(low + high, 2)
    sq = mid * mid

    cond do
      sq == x ->
        mid

      sq < x ->
        bs(mid + 1, high, x, mid)

      true ->
        bs(low, mid - 1, x, _ans)
    end
  end
end
```
