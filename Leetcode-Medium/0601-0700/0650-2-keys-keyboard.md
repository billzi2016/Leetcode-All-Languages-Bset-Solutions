# 0650. 2 Keys Keyboard

## Cpp

```cpp
class Solution {
public:
    int minSteps(int n) {
        if (n == 1) return 0;
        int ans = 0;
        for (int d = 2; d * d <= n; ++d) {
            while (n % d == 0) {
                ans += d;
                n /= d;
            }
        }
        if (n > 1) ans += n;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minSteps(int n) {
        if (n <= 1) return 0;
        int steps = 0;
        for (int d = 2; d * d <= n; d++) {
            while (n % d == 0) {
                steps += d;
                n /= d;
            }
        }
        if (n > 1) steps += n;
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        ans = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        if n > 1:
            ans += n
        return ans
```

## Python3

```python
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        steps = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                steps += d
                n //= d
            d += 1
        if n > 1:
            steps += n
        return steps
```

## C

```c
int minSteps(int n) {
    int ans = 0;
    for (int d = 2; d * d <= n; ++d) {
        while (n % d == 0) {
            ans += d;
            n /= d;
        }
    }
    if (n > 1) {
        ans += n;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSteps(int n)
    {
        if (n == 1) return 0;
        int ans = 0;
        int d = 2;
        while (n > 1)
        {
            while (n % d == 0)
            {
                ans += d;
                n /= d;
            }
            d++;
            if (d * d > n)
            {
                if (n > 1)
                {
                    ans += n;
                    break;
                }
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function(n) {
    if (n === 1) return 0;
    let steps = 0;
    for (let d = 2; d * d <= n; d++) {
        while (n % d === 0) {
            steps += d;
            n = Math.floor(n / d);
        }
    }
    if (n > 1) steps += n;
    return steps;
};
```

## Typescript

```typescript
function minSteps(n: number): number {
    if (n <= 1) return 0;
    let steps = 0;
    for (let d = 2; d * d <= n; ++d) {
        while (n % d === 0) {
            steps += d;
            n = Math.floor(n / d);
        }
    }
    if (n > 1) steps += n;
    return steps;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minSteps($n) {
        if ($n == 1) return 0;
        $ans = 0;
        $d = 2;
        while ($d * $d <= $n) {
            while ($n % $d == 0) {
                $ans += $d;
                $n = intdiv($n, $d);
            }
            $d++;
        }
        if ($n > 1) {
            $ans += $n;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSteps(_ n: Int) -> Int {
        if n == 1 { return 0 }
        var result = 0
        var num = n
        var d = 2
        while d * d <= num {
            while num % d == 0 {
                result += d
                num /= d
            }
            d += 1
        }
        if num > 1 {
            result += num
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSteps(n: Int): Int {
        if (n == 1) return 0
        var num = n
        var ans = 0
        var d = 2
        while (d * d <= num) {
            while (num % d == 0) {
                ans += d
                num /= d
            }
            d++
        }
        if (num > 1) ans += num
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minSteps(int n) {
    if (n <= 1) return 0;
    int ans = 0;
    int d = 2;
    while (d * d <= n) {
      while (n % d == 0) {
        ans += d;
        n ~/= d;
      }
      d++;
    }
    if (n > 1) ans += n;
    return ans;
  }
}
```

## Golang

```go
func minSteps(n int) int {
	if n == 1 {
		return 0
	}
	ans := 0
	for d := 2; d*d <= n; d++ {
		for n%d == 0 {
			ans += d
			n /= d
		}
	}
	if n > 1 {
		ans += n
	}
	return ans
}
```

## Ruby

```ruby
def min_steps(n)
  return 0 if n == 1
  ans = 0
  d = 2
  while d * d <= n
    while (n % d).zero?
      ans += d
      n /= d
    end
    d += 1
  end
  ans + n
end
```

## Scala

```scala
object Solution {
    def minSteps(n: Int): Int = {
        if (n == 1) return 0
        var num = n
        var d = 2
        var ans = 0
        while (d * d <= num) {
            while (num % d == 0) {
                ans += d
                num /= d
            }
            d += 1
        }
        if (num > 1) ans += num
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_steps(n: i32) -> i32 {
        if n == 1 {
            return 0;
        }
        let mut ans = 0;
        let mut m = n;
        let mut d = 2;
        while (d * d) <= m {
            while m % d == 0 {
                ans += d;
                m /= d;
            }
            d += 1;
        }
        if m > 1 {
            ans += m;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-steps n)
  (-> exact-integer? exact-integer?)
  (let loop ((n n) (d 2) (ans 0))
    (cond
      [(= n 1) ans]
      [(> (* d d) n) (+ ans n)]               ; remaining n is prime
      [(zero? (remainder n d))
       (loop (/ n d) d (+ ans d))]
      [else (loop n (+ d 1) ans)])))
```

## Erlang

```erlang
-module(solution).
-export([min_steps/1]).

-spec min_steps(N :: integer()) -> integer().
min_steps(N) when N =< 1 ->
    0;
min_steps(N) ->
    min_steps(N, 2, 0).

min_steps(Num, D, Acc) when D * D > Num ->
    case Num of
        1 -> Acc;
        _ -> Acc + Num
    end;
min_steps(Num, D, Acc) ->
    case Num rem D of
        0 ->
            min_steps(Num div D, D, Acc + D);
        _ ->
            min_steps(Num, D + 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_steps(n :: integer) :: integer
  def min_steps(n) when n <= 1, do: 0

  def min_steps(n), do: factor(n, 2, 0)

  defp factor(1, _d, acc), do: acc

  defp factor(n, d, acc) when d * d > n do
    acc + n
  end

  defp factor(n, d, acc) do
    if rem(n, d) == 0 do
      factor(div(n, d), d, acc + d)
    else
      factor(n, d + 1, acc)
    end
  end
end
```
