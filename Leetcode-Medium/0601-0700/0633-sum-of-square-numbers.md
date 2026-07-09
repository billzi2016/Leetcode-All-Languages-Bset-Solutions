# 0633. Sum of Square Numbers

## Cpp

```cpp
#include <cmath>

class Solution {
public:
    bool judgeSquareSum(int c) {
        long long a = 0;
        long long b = static_cast<long long>(std::sqrt(c));
        while (a <= b) {
            long long sum = a * a + b * b;
            if (sum == c) return true;
            if (sum < c)
                ++a;
            else
                --b;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean judgeSquareSum(int c) {
        long left = 0;
        long right = (long) Math.sqrt(c);
        while (left <= right) {
            long sum = left * left + right * right;
            if (sum == c) {
                return true;
            } else if (sum < c) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
}
```

## Python

```python
import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = math.isqrt(c)
        while left <= right:
            cur = left * left + right * right
            if cur == c:
                return True
            elif cur < c:
                left += 1
            else:
                right -= 1
        return False
```

## Python3

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import isqrt
        left, right = 0, isqrt(c)
        while left <= right:
            cur = left * left + right * right
            if cur == c:
                return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False
```

## C

```c
#include <stdbool.h>
#include <math.h>

bool judgeSquareSum(int c) {
    long long left = 0;
    long long right = (long long)sqrt((double)c);
    while (left <= right) {
        long long sum = left * left + right * right;
        if (sum == c) return true;
        if (sum < c)
            ++left;
        else
            --right;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool JudgeSquareSum(int c)
    {
        long a = 0;
        long b = (long)Math.Sqrt(c);
        while (a <= b)
        {
            long sum = a * a + b * b;
            if (sum == c) return true;
            if (sum < c) a++;
            else b--;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    let left = 0;
    let right = Math.floor(Math.sqrt(c));
    while (left <= right) {
        const sum = left * left + right * right;
        if (sum === c) return true;
        if (sum < c) {
            left++;
        } else {
            right--;
        }
    }
    return false;
};
```

## Typescript

```typescript
function judgeSquareSum(c: number): boolean {
    let a = 0;
    let b = Math.floor(Math.sqrt(c));
    while (a <= b) {
        const sum = a * a + b * b;
        if (sum === c) return true;
        if (sum < c) {
            a++;
        } else {
            b--;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $c
     * @return Boolean
     */
    function judgeSquareSum($c) {
        $left = 0;
        $right = (int)floor(sqrt($c));
        while ($left <= $right) {
            $sum = $left * $left + $right * $right;
            if ($sum == $c) {
                return true;
            } elseif ($sum < $c) {
                $left++;
            } else {
                $right--;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func judgeSquareSum(_ c: Int) -> Bool {
        var left = 0
        var right = Int(Double(c).squareRoot())
        while left <= right {
            let sum = left * left + right * right
            if sum == c {
                return true
            } else if sum < c {
                left += 1
            } else {
                right -= 1
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt

class Solution {
    fun judgeSquareSum(c: Int): Boolean {
        var a = 0L
        var b = sqrt(c.toDouble()).toLong()
        val target = c.toLong()
        while (a <= b) {
            val sum = a * a + b * b
            if (sum == target) return true
            if (sum < target) {
                a++
            } else {
                b--
            }
        }
        return false
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  bool judgeSquareSum(int c) {
    int a = 0;
    int b = sqrt(c.toDouble()).toInt();
    while (a <= b) {
      int sum = a * a + b * b;
      if (sum == c) return true;
      if (sum < c) {
        a++;
      } else {
        b--;
      }
    }
    return false;
  }
}
```

## Golang

```go
import "math"

func judgeSquareSum(c int) bool {
    left, right := 0, int(math.Sqrt(float64(c)))
    for left <= right {
        sum := left*left + right*right
        if sum == c {
            return true
        } else if sum < c {
            left++
        } else {
            right--
        }
    }
    return false
}
```

## Ruby

```ruby
def judge_square_sum(c)
  a = 0
  b = Math.sqrt(c).to_i
  while a <= b
    sum = a * a + b * b
    return true if sum == c
    if sum < c
      a += 1
    else
      b -= 1
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  def judgeSquareSum(c: Int): Boolean = {
    var left: Long = 0L
    var right: Long = Math.sqrt(c.toLong).toLong
    while (left <= right) {
      val sum = left * left + right * right
      if (sum == c) return true
      else if (sum < c) left += 1
      else right -= 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        let target = c as i64;
        let mut left: i64 = 0;
        let mut right: i64 = (c as f64).sqrt() as i64;
        while left <= right {
            let sum = left * left + right * right;
            if sum == target {
                return true;
            } else if sum < target {
                left += 1;
            } else {
                right -= 1;
            }
        }
        false
    }
}
```

## Racket

```racket
#lang racket
(require racket/math)

(define/contract (judge-square-sum c)
  (-> exact-integer? boolean?)
  (let-values ([(right _) (integer-sqrt c)])
    (let loop ((a 0) (b right))
      (cond [(> a b) #f]
            [else
             (let ([sum (+ (* a a) (* b b))])
               (cond [(= sum c) #t]
                     [(< sum c) (loop (add1 a) b)]
                     [else (loop a (sub1 b))]))])))
```

## Erlang

```erlang
-spec judge_square_sum(C :: integer()) -> boolean().
judge_square_sum(C) when C >= 0 ->
    Max = trunc(math:sqrt(C)),
    loop(0, Max, C).

loop(A, B, C) when A =< B ->
    Sum = A*A + B*B,
    if
        Sum == C -> true;
        Sum < C -> loop(A+1, B, C);
        true -> loop(A, B-1, C)
    end;
loop(_, _, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec judge_square_sum(c :: integer) :: boolean
  def judge_square_sum(c) do
    max = :math.sqrt(c) |> trunc()
    check(0, max, c)
  end

  defp check(a, b, target) when a > b, do: false

  defp check(a, b, target) do
    sum = a * a + b * b

    cond do
      sum == target -> true
      sum < target -> check(a + 1, b, target)
      true -> check(a, b - 1, target)
    end
  end
end
```
