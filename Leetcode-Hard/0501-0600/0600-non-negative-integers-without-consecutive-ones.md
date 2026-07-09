# 0600. Non-negative Integers without Consecutive Ones

## Cpp

```cpp
class Solution {
public:
    int findIntegers(int n) {
        // f[i] = count of binary strings without consecutive ones of length i
        int f[32];
        f[0] = 1;          // empty string
        f[1] = 2;          // "0", "1"
        for (int i = 2; i < 32; ++i) {
            f[i] = f[i - 1] + f[i - 2];
        }
        
        int ans = 0;
        bool prev_one = false;
        for (int i = 30; i >= 0; --i) { // since n <= 1e9 < 2^30, but safe up to 31
            if ((n >> i) & 1) {
                ans += f[i];
                if (prev_one) {
                    return ans; // consecutive ones encountered, stop counting further
                }
                prev_one = true;
            } else {
                prev_one = false;
            }
        }
        // include n itself (it has no consecutive ones)
        return ans + 1;
    }
};
```

## Java

```java
class Solution {
    public int findIntegers(int n) {
        int[] f = new int[32];
        f[0] = 1;
        f[1] = 2;
        for (int i = 2; i < 32; i++) {
            f[i] = f[i - 1] + f[i - 2];
        }
        int sum = 0;
        int prevBit = 0;
        for (int i = 30; i >= 0; i--) { // highest bit needed for n <= 10^9
            if ((n & (1 << i)) != 0) {
                sum += f[i];
                if (prevBit == 1) {
                    return sum;
                }
                prevBit = 1;
            } else {
                prevBit = 0;
            }
        }
        return sum + 1; // include n itself
    }
}
```

## Python

```python
class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f[i] = count of binary strings of length i without consecutive ones
        f = [0] * 32
        f[0], f[1] = 1, 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        prev_bit = 0
        # iterate from highest bit to lowest
        for i in range(31, -1, -1):
            if n & (1 << i):
                ans += f[i]
                if prev_bit:
                    return ans  # consecutive ones encountered
                prev_bit = 1
            else:
                prev_bit = 0
        # include n itself
        return ans + 1
```

## Python3

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        # f[i]: count of binary strings of length i without consecutive ones
        f = [0] * 32
        f[0] = 1  # empty string
        f[1] = 2  # "0", "1"
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        result = 0
        prev_bit = 0
        # find the position of the highest set bit
        for k in range(31, -1, -1):
            if (n >> k) & 1:
                result += f[k]
                if prev_bit == 1:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0

        # n itself does not contain consecutive ones
        return result + 1
```

## C

```c
int findIntegers(int n) {
    int f[32];
    f[0] = 1;
    f[1] = 2;
    for (int i = 2; i < 32; ++i)
        f[i] = f[i - 1] + f[i - 2];

    int sum = 0;
    int prev_bit = 0;
    for (int i = 30; i >= 0; --i) {
        if (n & (1 << i)) {
            sum += f[i];
            if (prev_bit)
                return sum;          // consecutive ones encountered
            prev_bit = 1;
        } else {
            prev_bit = 0;
        }
    }
    return sum + 1;                  // include n itself
}
```

## Csharp

```csharp
public class Solution
{
    public int FindIntegers(int n)
    {
        int[] f = new int[32];
        f[0] = 1;
        f[1] = 2;
        for (int i = 2; i < 32; i++)
            f[i] = f[i - 1] + f[i - 2];

        int ans = 0;
        int prevBit = 0;

        for (int i = 31; i >= 0; i--)
        {
            if (((n >> i) & 1) == 1)
            {
                ans += f[i];
                if (prevBit == 1)
                    return ans; // consecutive ones found, stop
                prevBit = 1;
            }
            else
            {
                prevBit = 0;
            }
        }

        return ans + 1; // include n itself
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var findIntegers = function(n) {
    // f[i] = count of binary strings of length i without consecutive ones
    const f = new Array(32).fill(0);
    f[0] = 1; // empty string
    f[1] = 2; // "0", "1"
    for (let i = 2; i < 32; ++i) {
        f[i] = f[i - 1] + f[i - 2];
    }

    let result = 0;
    let prevBit = 0;

    for (let i = 30; i >= 0; --i) { // since n <= 1e9 < 2^30
        if ((n >> i) & 1) {
            result += f[i];
            if (prevBit === 1) {
                // consecutive ones encountered, cannot include further numbers
                return result;
            }
            prevBit = 1;
        } else {
            prevBit = 0;
        }
    }

    // n itself does not contain consecutive ones
    return result + 1;
};
```

## Typescript

```typescript
function findIntegers(n: number): number {
    const fib: number[] = new Array(32).fill(0);
    fib[0] = 1;
    fib[1] = 2;
    for (let i = 2; i < 32; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    let result = 0;
    let prevBit = 0;

    for (let k = 31; k >= 0; k--) {
        if ((n & (1 << k)) !== 0) {
            result += fib[k];
            if (prevBit === 1) {
                return result;
            }
            prevBit = 1;
        } else {
            prevBit = 0;
        }
    }

    return result + 1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function findIntegers($n) {
        // Precompute Fibonacci-like counts for lengths up to 31 bits
        $fib = array_fill(0, 32, 0);
        $fib[0] = 1; // empty string or single 0
        $fib[1] = 2; // "0", "1"
        for ($i = 2; $i < 32; $i++) {
            $fib[$i] = $fib[$i - 1] + $fib[$i - 2];
        }

        $ans = 0;
        $prevBit = false;

        // Scan bits from most significant to least significant
        for ($k = 31; $k >= 0; $k--) {
            if ((($n >> $k) & 1) === 1) {
                $ans += $fib[$k];
                if ($prevBit) {
                    // Two consecutive ones found, stop early
                    return $ans;
                }
                $prevBit = true;
            } else {
                $prevBit = false;
            }
        }

        // Include n itself (it has no consecutive ones)
        return $ans + 1;
    }
}
```

## Swift

```swift
class Solution {
    func findIntegers(_ n: Int) -> Int {
        var f = [Int](repeating: 0, count: 32)
        f[0] = 1
        f[1] = 2
        for i in 2..<32 {
            f[i] = f[i - 1] + f[i - 2]
        }
        
        var result = 0
        var prevBit = false
        
        for i in stride(from: 31, through: 0, by: -1) {
            if (n & (1 << i)) != 0 {
                result += f[i]
                if prevBit {
                    return result
                }
                prevBit = true
            } else {
                prevBit = false
            }
        }
        return result + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findIntegers(n: Int): Int {
        val f = LongArray(32)
        f[0] = 1L
        f[1] = 2L
        for (i in 2 until 32) {
            f[i] = f[i - 1] + f[i - 2]
        }
        var ans = 0L
        var prevBit = 0
        for (i in 31 downTo 0) {
            if ((n shr i) and 1 == 1) {
                ans += f[i]
                if (prevBit == 1) {
                    return ans.toInt()
                }
                prevBit = 1
            } else {
                prevBit = 0
            }
        }
        return (ans + 1).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int findIntegers(int n) {
    // f[i] = count of binary strings of length i without consecutive ones
    List<int> f = List.filled(32, 0);
    f[0] = 1;
    f[1] = 2;
    for (int i = 2; i < 32; ++i) {
      f[i] = f[i - 1] + f[i - 2];
    }

    int ans = 0;
    int prevBit = 0;

    // Find most significant bit set in n
    int msb = 31;
    while (msb >= 0 && ((n >> msb) & 1) == 0) {
      msb--;
    }

    for (int i = msb; i >= 0; --i) {
      if (((n >> i) & 1) == 1) {
        ans += f[i];
        if (prevBit == 1) {
          // consecutive ones encountered, stop counting
          return ans;
        }
        prevBit = 1;
      } else {
        prevBit = 0;
      }
    }

    // n itself does not contain consecutive ones
    return ans + 1;
  }
}
```

## Golang

```go
func findIntegers(n int) int {
    // f[i] = count of binary strings of length i without consecutive ones
    const maxBits = 32
    f := make([]int, maxBits)
    f[0] = 1
    f[1] = 2
    for i := 2; i < maxBits; i++ {
        f[i] = f[i-1] + f[i-2]
    }

    ans := 0
    prevOne := false
    for i := maxBits - 1; i >= 0; i-- {
        if (n>>i)&1 == 1 {
            ans += f[i]
            if prevOne {
                // consecutive ones encountered, cannot include further numbers
                return ans
            }
            prevOne = true
        } else {
            prevOne = false
        }
    }
    // n itself does not contain consecutive ones
    return ans + 1
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def find_integers(n)
  f = Array.new(32, 0)
  f[0] = 1
  f[1] = 2
  (2...32).each do |i|
    f[i] = f[i - 1] + f[i - 2]
  end

  result = 0
  prev_bit = 0
  i = n.bit_length - 1
  while i >= 0
    if (n & (1 << i)) != 0
      result += f[i]
      return result if prev_bit == 1
      prev_bit = 1
    else
      prev_bit = 0
    end
    i -= 1
  end
  result + 1
end
```

## Scala

```scala
object Solution {
    def findIntegers(n: Int): Int = {
        val f = new Array[Int](32)
        f(0) = 1
        f(1) = 2
        for (i <- 2 until 32) {
            f(i) = f(i - 1) + f(i - 2)
        }

        var result = 0
        var prevBit = 0

        var msb = 31
        while (msb >= 0 && ((n >> msb) & 1) == 0) {
            msb -= 1
        }

        for (k <- msb to 0 by -1) {
            val currBit = (n >> k) & 1
            if (currBit == 1) {
                result += f(k)
                if (prevBit == 1) {
                    return result
                }
                prevBit = 1
            } else {
                prevBit = 0
            }
        }

        result + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_integers(n: i32) -> i32 {
        // f[i] = count of binary strings of length i without consecutive ones
        let mut f = vec![0i64; 32];
        f[0] = 1;
        f[1] = 2;
        for i in 2..32 {
            f[i] = f[i - 1] + f[i - 2];
        }

        let mut result: i64 = 0;
        let mut prev_one = false;
        let n_u = n as u32;

        for k in (0..32).rev() {
            if ((n_u >> k) & 1) == 1 {
                result += f[k];
                if prev_one {
                    return result as i32; // consecutive ones encountered
                }
                prev_one = true;
            } else {
                prev_one = false;
            }
        }

        (result + 1) as i32 // include n itself
    }
}
```

## Racket

```racket
(define/contract (find-integers n)
  (-> exact-integer? exact-integer?)
  (if (= n 0)
      1
      (let* ((max-bits 32)
             (dp (make-vector max-bits)))
        (vector-set! dp 0 1)          ; empty string
        (vector-set! dp 1 2)          ; "0", "1"
        (for ([i (in-range 2 max-bits)])
          (vector-set! dp i (+ (vector-ref dp (- i 1))
                               (vector-ref dp (- i 2)))))
        (let loop ((i (- (integer-length n) 1)) ; start from MSB index
                   (prev-zero? #t)               ; previous bit was 0
                   (ans 0))
          (if (< i 0)
              (+ ans 1)                         ; n itself has no consecutive ones
              (let ((bit (bitwise-and (arithmetic-shift n (- i)) 1)))
                (if (= bit 1)
                    (let ((new-ans (+ ans (vector-ref dp i))))
                      (if prev-zero?
                          (loop (- i 1) #f new-ans) ; continue, set previous to 1
                          new-ans))                 ; consecutive ones -> stop
                    (loop (- i 1) #t ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_integers/1]).

find_integers(N) ->
    MaxBits = 31,
    FTup = list_to_tuple(fib_vals(MaxBits)),
    Highest = highest_bit(N),
    count_bits(N, Highest - 1, FTup, 0, false).

fib_vals(Max) -> fib_vals_acc(0, Max, []).

fib_vals_acc(I, Max, Acc) when I > Max ->
    lists:reverse(Acc);
fib_vals_acc(I, Max, Acc) ->
    Val = case I of
        0 -> 1;
        1 -> 2;
        _ ->
            [Prev | [PrevPrev | _]] = Acc,
            Prev + PrevPrev
    end,
    fib_vals_acc(I + 1, Max, [Val | Acc]).

highest_bit(N) -> highest_bit(N, 0).
highest_bit(0, Acc) -> Acc;
highest_bit(N, Acc) ->
    highest_bit(N bsr 1, Acc + 1).

count_bits(_, Pos, _, Sum, _) when Pos < 0 ->
    Sum + 1;
count_bits(N, Pos, FTup, Sum, PrevOne) ->
    BitMask = 1 bsl Pos,
    case N band BitMask of
        0 ->
            count_bits(N, Pos - 1, FTup, Sum, false);
        _ ->
            NewSum = Sum + element(Pos + 1, FTup),
            if PrevOne ->
                NewSum;
               true ->
                count_bits(N, Pos - 1, FTup, NewSum, true)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec find_integers(n :: integer) :: integer
  def find_integers(n) do
    f = compute_f()
    max_bit = highest_bit(n)
    count_without_consecutive(f, n, max_bit)
  end

  # Precompute f[i] = number of binary strings of length i without consecutive ones
  defp compute_f() do
    f = List.duplicate(0, 32)
    f = put_elem(f, 0, 1)   # empty string
    f = put_elem(f, 1, 2)   # "0", "1"
    Enum.reduce(2..31, f, fn i, acc ->
      val = elem(acc, i - 1) + elem(acc, i - 2)
      put_elem(acc, i, val)
    end)
  end

  # Find position of most significant bit (0‑based). Returns -1 for n == 0.
  defp highest_bit(0), do: -1
  defp highest_bit(n) when n > 0 do
    highest_bit_helper(n, 0)
  end

  defp highest_bit_helper(0, pos), do: pos - 1
  defp highest_bit_helper(num, pos), do: highest_bit_helper(num >>> 1, pos + 1)

  # Main counting routine.
  defp count_without_consecutive(f, n, i) do
    do_count(f, n, i, 0, 0)
  end

  defp do_count(_f, _n, -1, sum, _prev), do: sum + 1

  defp do_count(f, n, i, sum, prev) do
    if ((n >>> i) &&& 1) == 1 do
      new_sum = sum + elem(f, i)
      if prev == 1 do
        new_sum
      else
        do_count(f, n, i - 1, new_sum, 1)
      end
    else
      do_count(f, n, i - 1, sum, 0)
    end
  end
end
```
