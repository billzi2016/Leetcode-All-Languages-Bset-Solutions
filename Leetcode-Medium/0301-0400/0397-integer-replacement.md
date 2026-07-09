# 0397. Integer Replacement

## Cpp

```cpp
class Solution {
public:
    int integerReplacement(int n) {
        long long x = n;
        int steps = 0;
        while (x != 1) {
            if ((x & 1LL) == 0) {
                x >>= 1;
            } else {
                if (x == 3 || ((x >> 1) & 1LL) == 0) {
                    --x;
                } else {
                    ++x;
                }
            }
            ++steps;
        }
        return steps;
    }
};
```

## Java

```java
class Solution {
    public int integerReplacement(int n) {
        long num = n;
        int steps = 0;
        while (num != 1) {
            if ((num & 1L) == 0) {
                num >>= 1;
            } else {
                if (num == 3 || (num & 3L) == 1) {
                    num--;
                } else {
                    num++;
                }
            }
            steps++;
        }
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            else:
                # If n is 3 or ends with ...01 (i.e., n % 4 == 1), decrement.
                # Otherwise increment to get more trailing zeros.
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
            steps += 1
        return steps
```

## Python3

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                # For n == 3 or when n mod 4 == 1, decrement; otherwise increment.
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
            steps += 1
        return steps
```

## C

```c
int integerReplacement(int n) {
    long long x = n;
    int steps = 0;
    while (x != 1) {
        if ((x & 1LL) == 0) {
            x >>= 1;
        } else {
            if (x == 3 || ((x >> 1) & 1LL) == 0) {
                x--;
            } else {
                x++;
            }
        }
        ++steps;
    }
    return steps;
}
```

## Csharp

```csharp
public class Solution
{
    public int IntegerReplacement(int n)
    {
        long cur = n;
        int steps = 0;
        while (cur != 1)
        {
            if ((cur & 1) == 0)
            {
                cur >>= 1;
            }
            else
            {
                if (cur == 3 || ((cur >> 1) & 1) == 0)
                    cur--;
                else
                    cur++;
            }
            steps++;
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    let steps = 0;
    while (n !== 1) {
        if ((n & 1) === 0) {
            n = n / 2;
        } else {
            if (n === 3 || n % 4 === 1) {
                n--;
            } else {
                n++;
            }
        }
        steps++;
    }
    return steps;
};
```

## Typescript

```typescript
function integerReplacement(n: number): number {
    let steps = 0;
    while (n !== 1) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            // For odd n, decide to increment or decrement
            if (n === 3 || n % 4 === 1) {
                n -= 1;
            } else {
                n += 1;
            }
        }
        steps++;
    }
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
    function integerReplacement($n) {
        $steps = 0;
        while ($n != 1) {
            if (($n & 1) == 0) {
                // even, divide by 2
                $n >>= 1;
            } else {
                if ($n == 3) {
                    $n--;
                } else {
                    // choose direction that creates more trailing zeros
                    if ((($n >> 1) & 1) == 0) {
                        $n--;
                    } else {
                        $n++;
                    }
                }
            }
            $steps++;
        }
        return $steps;
    }
}
```

## Swift

```swift
class Solution {
    func integerReplacement(_ n: Int) -> Int {
        var steps = 0
        var num = Int64(n)
        while num != 1 {
            if num & 1 == 0 {
                num >>= 1
            } else {
                if num == 3 || (num & 3) == 1 {
                    num -= 1
                } else {
                    num += 1
                }
            }
            steps += 1
        }
        return steps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun integerReplacement(n: Int): Int {
        var num = n.toLong()
        var steps = 0
        while (num != 1L) {
            if ((num and 1L) == 0L) {
                num = num shr 1
            } else {
                if (num == 3L || ((num shr 1) and 1L) == 0L) {
                    num--
                } else {
                    num++
                }
            }
            steps++
        }
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int integerReplacement(int n) {
    int steps = 0;
    while (n != 1) {
      if ((n & 1) == 0) {
        n >>= 1;
      } else {
        if (n == 3 || ((n >> 1) & 1) == 0) {
          n--;
        } else {
          n++;
        }
      }
      steps++;
    }
    return steps;
  }
}
```

## Golang

```go
func integerReplacement(n int) int {
	steps := 0
	x := int64(n)
	for x != 1 {
		if x%2 == 0 {
			x /= 2
		} else {
			if x == 3 || x%4 == 1 {
				x--
			} else {
				x++
			}
		}
		steps++
	}
	return steps
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def integer_replacement(n)
  steps = 0
  while n != 1
    if n.even?
      n >>= 1
    else
      # For odd n, decide to increment or decrement.
      # Prefer decrement when n == 3 or n % 4 == 1, otherwise increment.
      if n == 3 || (n & 3) == 1
        n -= 1
      else
        n += 1
      end
    end
    steps += 1
  end
  steps
end
```

## Scala

```scala
object Solution {
    def integerReplacement(n: Int): Int = {
        var steps = 0
        var x: Long = n.toLong
        while (x != 1) {
            if ((x & 1L) == 0) {
                x >>= 1
            } else {
                if (x == 3 || (x & 3L) == 1) {
                    x -= 1
                } else {
                    x += 1
                }
            }
            steps += 1
        }
        steps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn integer_replacement(n: i32) -> i32 {
        let mut cur = n as i64;
        let mut steps = 0;
        while cur != 1 {
            if cur & 1 == 0 {
                cur >>= 1;
            } else {
                if cur == 3 || (cur & 3) == 1 {
                    cur -= 1;
                } else {
                    cur += 1;
                }
            }
            steps += 1;
        }
        steps
    }
}
```

## Racket

```racket
(define/contract (integer-replacement n)
  (-> exact-integer? exact-integer?)
  (let loop ((x n) (cnt 0))
    (cond [(= x 1) cnt]
          [(even? x) (loop (/ x 2) (+ cnt 1))]
          [else
           (if (or (= x 3) (= (bitwise-and x 3) 1))
               (loop (- x 1) (+ cnt 1))
               (loop (+ x 1) (+ cnt 1)))])))
```

## Erlang

```erlang
-module(solution).
-export([integer_replacement/1]).

-spec integer_replacement(N :: integer()) -> integer().
integer_replacement(N) ->
    integer_replacement(N, 0).

%% Tail‑recursive helper with accumulator
integer_replacement(1, Acc) ->
    Acc;
integer_replacement(N, Acc) when N rem 2 =:= 0 ->
    integer_replacement(N div 2, Acc + 1);
integer_replacement(3, Acc) ->
    Acc + 2;   % 3 -> 2 -> 1
integer_replacement(N, Acc) ->
    case (N band 3) of
        1 -> integer_replacement(N - 1, Acc + 1);   % n % 4 == 1
        _ -> integer_replacement(N + 1, Acc + 1)    % n % 4 == 3
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec integer_replacement(n :: integer) :: integer
  def integer_replacement(n) do
    int_rep(n)
  end

  defp int_rep(1), do: 0
  defp int_rep(3), do: 2
  defp int_rep(n) when rem(n, 2) == 0 do
    1 + int_rep(div(n, 2))
  end
  defp int_rep(n) do
    if rem(n, 4) == 1 do
      1 + int_rep(n - 1)
    else
      1 + int_rep(n + 1)
    end
  end
end
```
