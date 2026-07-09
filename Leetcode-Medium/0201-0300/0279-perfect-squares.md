# 0279. Perfect Squares

## Cpp

```cpp
class Solution {
public:
    int numSquares(int n) {
        // Check if n is a perfect square
        int sq = (int)sqrt(n);
        if (sq * sq == n) return 1;
        
        // Check if the sum of two squares equals n
        for (int i = 1; i * i <= n; ++i) {
            int remainder = n - i * i;
            int r = (int)sqrt(remainder);
            if (r * r == remainder) return 2;
        }
        
        // Apply Legendre's three-square theorem
        int m = n;
        while (m % 4 == 0) m /= 4;
        if (m % 8 == 7) return 4;
        
        // If not 1, 2, or 4, then answer is 3
        return 3;
    }
};
```

## Java

```java
class Solution {
    public int numSquares(int n) {
        if (isSquare(n)) return 1;
        // Reduce n by removing factors of 4
        int m = n;
        while ((m & 3) == 0) { // m % 4 == 0
            m >>= 2; // divide by 4
        }
        if (m % 8 == 7) return 4;
        for (int i = 1; i * i <= n; i++) {
            if (isSquare(n - i * i)) return 2;
        }
        return 3;
    }

    private boolean isSquare(int x) {
        int r = (int) Math.sqrt(x);
        return r * r == x;
    }
}
```

## Python

```python
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math

        # Check if n is a perfect square
        if int(math.isqrt(n)) ** 2 == n:
            return 1

        # Reduce n by removing factors of 4 (Legendre's three-square theorem)
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # Check if the answer is 2
        limit = int(math.isqrt(n))
        for i in range(1, limit + 1):
            remainder = n - i * i
            if int(math.isqrt(remainder)) ** 2 == remainder:
                return 2

        # Otherwise, the answer is 3
        return 3
```

## Python3

```python
class Solution:
    def numSquares(self, n: int) -> int:
        # Precompute all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [float('inf')] * n
        for x in range(1, n + 1):
            for sq in squares:
                if sq > x:
                    break
                if dp[x - sq] + 1 < dp[x]:
                    dp[x] = dp[x - sq] + 1
        return dp[n]
```

## C

```c
int numSquares(int n) {
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    if (!dp) return 0;
    dp[0] = 0;
    for (int i = 1; i <= n; ++i) {
        dp[i] = i; // worst case: all 1's
        for (int j = 1; j * j <= i; ++j) {
            int sq = j * j;
            if (dp[i - sq] + 1 < dp[i])
                dp[i] = dp[i - sq] + 1;
        }
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = i; // worst case: all 1's

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                int square = j * j;
                if (dp[i] > dp[i - square] + 1) {
                    dp[i] = dp[i - square] + 1;
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function numSquares(n: number): number {
    const isSquare = (x: number): boolean => {
        const r = Math.floor(Math.sqrt(x));
        return r * r === x;
    };
    
    if (isSquare(n)) return 1;

    // Reduce n by removing factors of 4
    let m = n;
    while (m % 4 === 0) {
        m /= 4;
    }
    // Check Legendre's condition for four squares
    if (m % 8 === 7) return 4;

    // Check if the answer is 2
    for (let i = 1; i * i <= n; ++i) {
        if (isSquare(n - i * i)) return 2;
    }

    // Otherwise, answer is 3
    return 3;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numSquares($n) {
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;

        $squares = [];
        for ($i = 1; $i * $i <= $n; $i++) {
            $squares[] = $i * $i;
        }

        for ($i = 1; $i <= $n; $i++) {
            foreach ($squares as $sq) {
                if ($sq > $i) {
                    break;
                }
                $candidate = $dp[$i - $sq] + 1;
                if ($candidate < $dp[$i]) {
                    $dp[$i] = $candidate;
                }
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func numSquares(_ n: Int) -> Int {
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = 0
        for i in 1...n {
            var j = 1
            while j * j <= i {
                let square = j * j
                if dp[i - square] != Int.max && dp[i - square] + 1 < dp[i] {
                    dp[i] = dp[i - square] + 1
                }
                j += 1
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSquares(n: Int): Int {
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        dp[0] = 0
        for (i in 1..n) {
            var j = 1
            while (j * j <= i) {
                val prev = dp[i - j * j]
                if (prev != Int.MAX_VALUE && prev + 1 < dp[i]) {
                    dp[i] = prev + 1
                }
                j++
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int numSquares(int n) {
    List<int> dp = List.filled(n + 1, n);
    dp[0] = 0;
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j * j <= i; ++j) {
        int sq = j * j;
        if (dp[i - sq] + 1 < dp[i]) {
          dp[i] = dp[i - sq] + 1;
        }
      }
    }
    return dp[n];
  }
}
```

## Golang

```go
import "math"

func isSquare(x int) bool {
    y := int(math.Sqrt(float64(x)))
    return y*y == x
}

func numSquares(n int) int {
    if isSquare(n) {
        return 1
    }
    m := n
    for m%4 == 0 {
        m /= 4
    }
    if m%8 == 7 {
        return 4
    }
    for i := 1; i*i <= n; i++ {
        if isSquare(n - i*i) {
            return 2
        }
    }
    return 3
}
```

## Ruby

```ruby
def num_squares(n)
  squares = []
  i = 1
  while i * i <= n
    squares << i * i
    i += 1
  end

  dp = Array.new(n + 1, n) # worst case: n times 1^2
  dp[0] = 0

  (1..n).each do |i|
    squares.each do |sq|
      break if sq > i
      dp[i] = [dp[i], dp[i - sq] + 1].min
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
  def numSquares(n: Int): Int = {
    def isSquare(x: Int): Boolean = {
      val r = math.sqrt(x).toInt
      r * r == x
    }

    if (isSquare(n)) return 1

    var m = n
    while (m % 4 == 0) {
      m /= 4
    }
    if (m % 8 == 7) return 4

    val limit = math.sqrt(n).toInt
    var i = 1
    while (i <= limit) {
      if (isSquare(n - i * i)) return 2
      i += 1
    }

    3
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        if Self::is_square(n) {
            return 1;
        }
        let mut i = 1;
        while i * i <= n {
            if Self::is_square(n - i * i) {
                return 2;
            }
            i += 1;
        }
        // Apply Legendre's three-square theorem
        let mut m = n;
        while m % 4 == 0 {
            m /= 4;
        }
        if m % 8 == 7 {
            4
        } else {
            3
        }
    }

    fn is_square(x: i32) -> bool {
        let r = (x as f64).sqrt() as i32;
        r * r == x || (r + 1) * (r + 1) == x
    }
}
```

## Racket

```racket
(define/contract (num-squares n)
  (-> exact-integer? exact-integer?)
  (let* ((max-root (exact-floor (sqrt n)))
         (squares (for/list ([i (in-range 1 (+ max-root 1))]) (* i i)))
         (dp (make-vector (+ n 1) 0))) ; dp[0] = 0
    (for ([i (in-range 1 (+ n 1))])
      (let ((best (+ i 1))) ; worst case: all 1's
        (for ([sq squares])
          (when (<= sq i)
            (let ((cand (+ 1 (vector-ref dp (- i sq)))))
              (when (< cand best) (set! best cand)))))
        (vector-set! dp i best)))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([num_squares/1]).

-spec num_squares(N :: integer()) -> integer().
num_squares(N) when N >= 0 ->
    Squares = [S*S || S <- lists:seq(1, trunc(math:sqrt(N)))],
    DPMap = build_dp(N, Squares),
    maps:get(N, DPMap).

build_dp(N, Squares) ->
    lists:foldl(fun(I, Acc) ->
        Min = min_count(I, Squares, Acc),
        maps:put(I, Min, Acc)
    end, #{0 => 0}, lists:seq(1, N)).

min_count(I, Squares, DP) ->
    lists:min([maps:get(I - Sq, DP) + 1 || Sq <- Squares, Sq =< I]).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_squares(integer) :: integer
  def num_squares(n) when n <= 0, do: 0

  def num_squares(n) do
    max_root = trunc(:math.sqrt(n))
    squares = for k <- 1..max_root, do: k * k

    dp = :array.new(n + 1, default: n)
    dp = :array.set(0, 0, dp)

    dp =
      Enum.reduce(1..n, dp, fn i, acc ->
        min_val =
          Enum.reduce(squares, n, fn sq, cur_min ->
            if sq > i do
              cur_min
            else
              prev = :array.get(i - sq, acc)
              new_val = prev + 1
              if new_val < cur_min, do: new_val, else: cur_min
            end
          end)

        :array.set(i, min_val, acc)
      end)

    :array.get(n, dp)
  end
end
```
