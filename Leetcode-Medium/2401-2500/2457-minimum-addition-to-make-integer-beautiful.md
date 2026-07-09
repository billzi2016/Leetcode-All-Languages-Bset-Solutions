# 2457. Minimum Addition to Make Integer Beautiful

## Cpp

```cpp
class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        auto digitSum = [&](long long x) -> int {
            int sum = 0;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            return sum;
        };
        
        if (digitSum(n) <= target) return 0LL;
        long long added = 0;
        long long cur = n;
        long long power = 1;
        while (digitSum(cur) > target) {
            // find the first non-zero digit from right
            while ((cur / power) % 10 == 0) {
                power *= 10;
            }
            int d = (int)((cur / power) % 10);
            long long inc = (10 - d) * power;
            added += inc;
            cur += inc;
            // after addition, lower digits become zero, continue with same power
        }
        return added;
    }
};
```

## Java

```java
class Solution {
    public long makeIntegerBeautiful(long n, int target) {
        long added = 0;
        while (digitSum(n) > target) {
            long power = 1;
            // find the first position from right where digit is non‑zero
            while ((n / power) % 10 == 0) {
                power *= 10;
            }
            long mod = n % (power * 10);
            long inc = (power * 10) - mod; // make lower digits zero and carry one
            added += inc;
            n += inc;
        }
        return added;
    }

    private long digitSum(long x) {
        long sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        added = 0
        pow10 = 1
        while digit_sum(n) > target:
            digit = (n // pow10) % 10
            if digit == 0:
                pow10 *= 10
                continue
            inc = (10 - digit) * pow10
            added += inc
            n += inc
            pow10 *= 10
        return added
```

## Python3

```python
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        ans = 0
        p = 1
        while digit_sum(n) > target:
            d = (n // p) % 10
            add = ((10 - d) % 10) * p
            if add == 0:
                p *= 10
                continue
            n += add
            ans += add
            p *= 10
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static long long digitSum(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

long long makeIntegerBeautiful(long long n, int target) {
    if (digitSum(n) <= target) return 0LL;
    long long add = 0;
    long long pow10 = 1;
    for (int i = 0; i < 18; ++i) { // enough for n up to 1e12
        int digit = (n / pow10) % 10;
        long long inc = ((10 - digit) % 10) * pow10;
        if (inc != 0) {
            add += inc;
            n += inc; // lower digits become zero
        }
        if (digitSum(n) <= target) return add;
        pow10 *= 10;
    }
    return add;
}
```

## Csharp

```csharp
public class Solution {
    public long MakeIntegerBeautiful(long n, int target) {
        long added = 0;
        long pow = 1;
        while (DigitSum(n + added) > target) {
            long cur = ((n + added) / pow) % 10;
            if (cur == 0) {
                pow *= 10;
                continue;
            }
            long inc = (10 - cur) * pow;
            added += inc;
            pow *= 10;
        }
        return added;
    }

    private long DigitSum(long x) {
        long sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var makeIntegerBeautiful = function(n, target) {
    const digitSum = (x) => {
        let sum = 0;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        return sum;
    };
    
    if (digitSum(n) <= target) return 0;
    
    let add = 0;
    let power = 1;
    while (true) {
        const cur = n + add;
        if (digitSum(cur) <= target) break;
        const digit = Math.floor((cur / power) % 10);
        const inc = (10 - digit) % 10;
        if (inc === 0) {
            power *= 10;
            continue;
        }
        add += inc * power;
        power *= 10;
    }
    return add;
};
```

## Typescript

```typescript
function makeIntegerBeautiful(n: number, target: number): number {
    const digitSum = (x: number): number => {
        let sum = 0;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        return sum;
    };

    let added = 0;
    while (digitSum(n) > target) {
        let pow = 1;
        while (true) {
            const digit = Math.floor((n / pow)) % 10;
            if (digit !== 0) {
                const inc = (10 - digit) * pow;
                added += inc;
                n += inc;
                break;
            }
            pow *= 10;
        }
    }
    return added;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function makeIntegerBeautiful($n, $target) {
        $addTotal = 0;
        $mult = 1; // will become 10, 100, ...

        while (true) {
            // compute digit sum of current n
            $sum = 0;
            $temp = $n;
            while ($temp > 0) {
                $sum += $temp % 10;
                $temp = intdiv($temp, 10);
            }
            if ($sum <= $target) {
                break;
            }

            // increase multiplier to next power of ten
            $mult *= 10;
            // amount needed to make lower digits zero
            $add = $mult - ($n % $mult);
            $n += $add;
            $addTotal += $add;
        }

        return $addTotal;
    }
}
```

## Swift

```swift
class Solution {
    func makeIntegerBeautiful(_ n: Int, _ target: Int) -> Int {
        var num = n
        if digitSum(num) <= target { return 0 }
        var ans = 0
        var power = 1
        while true {
            let digit = (num / power) % 10
            let add = ((10 - digit) % 10) * power
            ans += add
            num += add
            if digitSum(num) <= target { break }
            power *= 10
        }
        return ans
    }
    
    private func digitSum(_ x: Int) -> Int {
        var v = x
        var sum = 0
        while v > 0 {
            sum += v % 10
            v /= 10
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeIntegerBeautiful(n: Long, target: Int): Long {
        fun digitSum(x: Long): Int {
            var v = x
            var sum = 0
            while (v > 0) {
                sum += (v % 10).toInt()
                v /= 10
            }
            return sum
        }

        if (digitSum(n) <= target) return 0L

        var add = 0L
        var power = 1L
        while (true) {
            val cur = n + add
            if (digitSum(cur) <= target) return add
            val digit = ((cur / power) % 10).toInt()
            val inc = (10 - digit) * power
            add += inc
            power *= 10
        }
    }
}
```

## Dart

```dart
class Solution {
  int makeIntegerBeautiful(int n, int target) {
    int digitSum(int x) {
      int sum = 0;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      return sum;
    }

    if (digitSum(n) <= target) return 0;

    int add = 0;
    int power = 1;

    while (true) {
      int modBase = power * 10;
      int remainder = n % modBase;
      int inc = (modBase - remainder) % modBase; // amount to reach next multiple of modBase

      if (inc != 0) {
        add += inc;
        n += inc;
        if (digitSum(n) <= target) break;
      }
      power *= 10;
    }

    return add;
  }
}
```

## Golang

```go
func makeIntegerBeautiful(n int64, target int) int64 {
	var added int64
	for {
		if digitSum(n) <= target {
			return added
		}
		pow10 := int64(10)
		for {
			mod := n % pow10
			if mod != 0 {
				inc := pow10 - mod
				added += inc
				n += inc
				break
			}
			pow10 *= 10
		}
	}
}

func digitSum(x int64) int {
	sum := 0
	for x > 0 {
		sum += int(x % 10)
		x /= 10
	}
	return sum
}
```

## Ruby

```ruby
def digit_sum(x)
  s = 0
  while x > 0
    s += x % 10
    x /= 10
  end
  s
end

def make_integer_beautiful(n, target)
  ans = 0
  while digit_sum(n) > target
    pow = 1
    while (n / pow) % 10 == 0
      pow *= 10
    end
    delta = pow * 10 - n % (pow * 10)
    ans += delta
    n += delta
  end
  ans
end
```

## Scala

```scala
object Solution {
    def makeIntegerBeautiful(n: Long, target: Int): Long = {
        def digitSum(x: Long): Int = {
            var sum = 0
            var v = x
            while (v > 0) {
                sum += (v % 10).toInt
                v /= 10
            }
            sum
        }

        if (digitSum(n) <= target) return 0L

        var power = 1L
        for (_ <- 0 to 18) {
            val remainder = n % power
            val inc = if (remainder == 0) 0L else power - remainder
            val newN = n + inc
            if (digitSum(newN) <= target) return inc
            // move to next digit position
            if (power > Long.MaxValue / 10) {
                // cannot increase further, but problem guarantees a solution before overflow
                return inc
            }
            power *= 10
        }
        0L
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_integer_beautiful(n: i64, target: i32) -> i64 {
        fn digit_sum(mut x: i64) -> i32 {
            let mut s = 0i32;
            while x > 0 {
                s += (x % 10) as i32;
                x /= 10;
            }
            s
        }

        if digit_sum(n) <= target {
            return 0;
        }

        let mut ans: i64 = 0;
        let mut pw: i64 = 1;

        while digit_sum(n + ans) > target {
            let cur_digit = ((n + ans) / pw) % 10;
            let inc = (10 - cur_digit) % 10; // amount to make this digit zero
            ans += inc * pw;
            pw *= 10;
        }

        ans
    }
}
```

## Racket

```racket
(define (digit-sum x)
  (let loop ((num x) (sum 0))
    (if (= num 0)
        sum
        (loop (quotient num 10) (+ sum (remainder num 10))))))

(define/contract (make-integer-beautiful n target)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((cur n) (add 0) (pow 1))
    (if (<= (digit-sum cur) target)
        add
        (let* ((mod (* pow 10))
               (rem (remainder cur mod))
               (inc (- mod rem)))
          (loop (+ cur inc) (+ add inc) (* pow 10))))))
```

## Erlang

```erlang
-module(solution).
-export([make_integer_beautiful/2]).

-spec make_integer_beautiful(N :: integer(), Target :: integer()) -> integer().
make_integer_beautiful(N, Target) ->
    case digit_sum(N) of
        S when S =< Target -> 0;
        _ -> go(N, Target, 0, 1)
    end.

digit_sum(0) -> 0;
digit_sum(N) when N > 0 ->
    digit_sum(N div 10) + (N rem 10).

go(N, Target, AccDelta, Pow10) ->
    case digit_sum(N) of
        S when S =< Target -> AccDelta;
        _ ->
            Mod = Pow10 * 10,
            Rem = N rem Mod,
            Delta = if Rem == 0 -> Mod; true -> Mod - Rem end,
            go(N + Delta, Target, AccDelta + Delta, Mod)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_integer_beautiful(n :: integer, target :: integer) :: integer
  def make_integer_beautiful(n, target) do
    if digit_sum(n) <= target do
      0
    else
      loop(n, 0, 1, target)
    end
  end

  defp loop(cur, added, power, target) do
    if digit_sum(cur) <= target do
      added
    else
      next = (div(cur, power * 10) + 1) * (power * 10)
      inc = next - cur
      loop(next, added + inc, power * 10, target)
    end
  end

  defp digit_sum(0), do: 0
  defp digit_sum(num) when num > 0 do
    rem(num, 10) + digit_sum(div(num, 10))
  end
end
```
