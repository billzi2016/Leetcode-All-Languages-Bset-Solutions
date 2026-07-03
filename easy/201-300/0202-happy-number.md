# 0202. Happy Number

## Cpp

```cpp
class Solution {
public:
    int next(int x) {
        int sum = 0;
        while (x > 0) {
            int d = x % 10;
            sum += d * d;
            x /= 10;
        }
        return sum;
    }
    
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = next(slow);
            fast = next(next(fast));
        } while (slow != fast && fast != 1);
        return fast == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNext(n);
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return fast == 1;
    }

    private int getNext(int num) {
        int sum = 0;
        while (num > 0) {
            int d = num % 10;
            sum += d * d;
            num /= 10;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_num(x):
            s = 0
            while x:
                d = x % 10
                s += d * d
                x //= 10
            return s

        slow = n
        fast = next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1
```

## Python3

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            s = 0
            while x:
                d = x % 10
                s += d * d
                x //= 10
            return s

        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1
```

## C

```c
#include <stdbool.h>

static int nextNumber(int n) {
    int sum = 0;
    while (n > 0) {
        int d = n % 10;
        sum += d * d;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow = n;
    int fast = nextNumber(n);
    while (fast != 1 && slow != fast) {
        slow = nextNumber(slow);
        fast = nextNumber(nextNumber(fast));
    }
    return fast == 1;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsHappy(int n)
    {
        int Slow(int x)
        {
            int sum = 0;
            while (x > 0)
            {
                int d = x % 10;
                sum += d * d;
                x /= 10;
            }
            return sum;
        }

        int slow = n;
        int fast = Slow(Slow(n));
        while (fast != 1 && slow != fast)
        {
            slow = Slow(slow);
            fast = Slow(Slow(fast));
        }
        return fast == 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const getNext = (num) => {
        let sum = 0;
        while (num > 0) {
            const digit = num % 10;
            sum += digit * digit;
            num = Math.floor(num / 10);
        }
        return sum;
    };
    
    let slow = n, fast = n;
    do {
        slow = getNext(slow);
        fast = getNext(getNext(fast));
        if (slow === 1 || fast === 1) return true;
    } while (slow !== fast);
    
    return false;
};
```

## Typescript

```typescript
function isHappy(n: number): boolean {
    const next = (num: number): number => {
        let sum = 0;
        while (num > 0) {
            const d = num % 10;
            sum += d * d;
            num = Math.floor(num / 10);
        }
        return sum;
    };
    
    let slow = n;
    let fast = next(n);
    while (fast !== 1 && slow !== fast) {
        slow = next(slow);
        fast = next(next(fast));
    }
    return fast === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isHappy($n) {
        // Helper to compute sum of squares of digits
        $next = function ($num) {
            $sum = 0;
            while ($num > 0) {
                $digit = $num % 10;
                $sum += $digit * $digit;
                $num = intdiv($num, 10);
            }
            return $sum;
        };

        $slow = $n;
        $fast = $next($n);

        while ($fast != 1 && $slow != $fast) {
            $slow = $next($slow);
            $fast = $next($next($fast));
        }

        return $fast == 1;
    }
}
```

## Swift

```swift
class Solution {
    func isHappy(_ n: Int) -> Bool {
        var slow = n
        var fast = next(n)
        while fast != 1 && slow != fast {
            slow = next(slow)
            fast = next(next(fast))
        }
        return fast == 1
    }
    
    private func next(_ num: Int) -> Int {
        var sum = 0
        var x = num
        while x > 0 {
            let digit = x % 10
            sum += digit * digit
            x /= 10
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isHappy(n: Int): Boolean {
        var slow = n
        var fast = getNext(n)
        while (fast != 1 && slow != fast) {
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        }
        return fast == 1
    }

    private fun getNext(num: Int): Int {
        var x = num
        var sum = 0
        while (x > 0) {
            val d = x % 10
            sum += d * d
            x /= 10
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  bool isHappy(int n) {
    int next(int num) {
      int sum = 0;
      while (num > 0) {
        int digit = num % 10;
        sum += digit * digit;
        num ~/= 10;
      }
      return sum;
    }

    int slow = n;
    int fast = next(n);
    while (fast != 1 && slow != fast) {
      slow = next(slow);
      fast = next(next(fast));
    }
    return fast == 1;
  }
}
```

## Golang

```go
func isHappy(n int) bool {
    if n == 1 {
        return true
    }
    next := func(num int) int {
        sum := 0
        for num > 0 {
            d := num % 10
            sum += d * d
            num /= 10
        }
        return sum
    }

    slow, fast := n, next(n)
    for fast != 1 && slow != fast {
        slow = next(slow)
        fast = next(next(fast))
    }
    return fast == 1
}
```

## Ruby

```ruby
def is_happy(n)
  next_num = lambda do |num|
    sum = 0
    while num > 0
      digit = num % 10
      sum += digit * digit
      num /= 10
    end
    sum
  end

  slow = n
  fast = next_num.call(n)
  while fast != 1 && slow != fast
    slow = next_num.call(slow)
    fast = next_num.call(next_num.call(fast))
  end
  fast == 1
end
```

## Scala

```scala
object Solution {
    def isHappy(n: Int): Boolean = {
        def next(num: Int): Int = {
            var x = num
            var sum = 0
            while (x > 0) {
                val d = x % 10
                sum += d * d
                x /= 10
            }
            sum
        }

        var slow = n
        var fast = n
        do {
            slow = next(slow)
            fast = next(next(fast))
        } while (slow != fast && fast != 1)

        fast == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_happy(n: i32) -> bool {
        fn next(mut num: i32) -> i32 {
            let mut sum = 0;
            while num > 0 {
                let d = num % 10;
                sum += d * d;
                num /= 10;
            }
            sum
        }

        let mut slow = n;
        let mut fast = next(n);
        while fast != 1 && slow != fast {
            slow = next(slow);
            fast = next(next(fast));
        }
        fast == 1
    }
}
```

## Racket

```racket
(define/contract (is-happy n)
  (-> exact-integer? boolean?)
  (letrec ((sum-square
            (lambda (x)
              (let loop ((y x) (s 0))
                (if (= y 0)
                    s
                    (let* ((d (remainder y 10))
                           (new-s (+ s (* d d))))
                      (loop (quotient y 10) new-s))))))
           (iterate
            (lambda (x seen)
              (cond [(= x 1) #t]
                    [(hash-has-key? seen x) #f]
                    [else (hash-set! seen x #t)
                          (iterate (sum-square x) seen)]))))
    (iterate n (make-hash))))
```

## Erlang

```erlang
-module(solution).
-export([is_happy/1]).

-spec is_happy(integer()) -> boolean().
is_happy(N) when N > 0 ->
    loop(next(N), next(next(N))).

loop(1, _) -> true;
loop(_, 1) -> true;
loop(Slow, Fast) when Slow =:= Fast -> false;
loop(Slow, Fast) ->
    loop(next(Slow), next(next(Fast))).

next(N) -> sum_sq_digits(N).

sum_sq_digits(N) -> sum_sq_digits(N, 0).
sum_sq_digits(0, Acc) -> Acc;
sum_sq_digits(N, Acc) ->
    Digit = N rem 10,
    sum_sq_digits(N div 10, Acc + Digit*Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_happy(n :: integer) :: boolean
  def is_happy(n) when n > 0 do
    happy?(n, next_num(n))
  end

  defp happy?(_slow, 1), do: true
  defp happy?(slow, fast) when slow == fast, do: false
  defp happy?(slow, fast) do
    happy?(next_num(slow), next_num(next_num(fast)))
  end

  defp next_num(num) do
    num
    |> Integer.digits()
    |> Enum.map(&(&1 * &1))
    |> Enum.sum()
  end
end
```
