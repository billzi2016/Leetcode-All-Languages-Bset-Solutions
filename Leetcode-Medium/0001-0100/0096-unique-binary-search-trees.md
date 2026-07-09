# 0096. Unique Binary Search Trees

## Cpp

```cpp
class Solution {
public:
    int numTrees(int n) {
        std::vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; ++i) {
            long long total = 0;
            for (int j = 1; j <= i; ++j) {
                total += static_cast<long long>(dp[j - 1]) * dp[i - j];
            }
            dp[i] = static_cast<int>(total);
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            long total = 0;
            for (int j = 1; j <= i; j++) {
                total += (long) dp[j - 1] * dp[i - j];
            }
            dp[i] = (int) total;
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            total = 0
            for left_nodes in range(i):
                right_nodes = i - 1 - left_nodes
                total += dp[left_nodes] * dp[right_nodes]
            dp[i] = total
        return dp[n]
```

## Python3

```python
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            total = 0
            for left in range(i):
                total += dp[left] * dp[i - 1 - left]
            dp[i] = total
        return dp[n]
```

## C

```c
int numTrees(int n) {
    long long dp[20] = {0};
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
        dp[i] = 0;
        for (int j = 1; j <= i; ++j) {
            dp[i] += dp[j - 1] * dp[i - j];
        }
    }
    return (int)dp[n];
}
```

## Csharp

```csharp
public class Solution
{
    public int NumTrees(int n)
    {
        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++)
        {
            long sum = 0;
            for (int j = 1; j <= i; j++)
            {
                sum += dp[j - 1] * dp[i - j];
            }
            dp[i] = sum;
        }
        return (int)dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    for (let i = 2; i <= n; i++) {
        let total = 0;
        for (let root = 1; root <= i; root++) {
            total += dp[root - 1] * dp[i - root];
        }
        dp[i] = total;
    }
    return dp[n];
};
```

## Typescript

```typescript
function numTrees(n: number): number {
    const dp = new Array<number>(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        let total = 0;
        for (let j = 1; j <= i; j++) {
            total += dp[j - 1] * dp[i - j];
        }
        dp[i] = total;
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numTrees($n) {
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $total = 0;
            for ($j = 1; $j <= $i; $j++) {
                $total += $dp[$j - 1] * $dp[$i - $j];
            }
            $dp[$i] = $total;
        }
        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func numTrees(_ n: Int) -> Int {
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        if n >= 1 { dp[1] = 1 }
        if n <= 1 { return dp[n] }
        for i in 2...n {
            var total = 0
            for j in 1...i {
                total += dp[j - 1] * dp[i - j]
            }
            dp[i] = total
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTrees(n: Int): Int {
        val dp = LongArray(n + 1)
        dp[0] = 1L
        for (i in 1..n) {
            var sum = 0L
            for (j in 1..i) {
                sum += dp[j - 1] * dp[i - j]
            }
            dp[i] = sum
        }
        return dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numTrees(int n) {
    List<int> dp = List.filled(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
      int total = 0;
      for (int j = 1; j <= i; j++) {
        total += dp[j - 1] * dp[i - j];
      }
      dp[i] = total;
    }
    return dp[n];
  }
}
```

## Golang

```go
func numTrees(n int) int {
    dp := make([]int, n+1)
    dp[0] = 1
    for i := 1; i <= n; i++ {
        total := 0
        for j := 1; j <= i; j++ {
            total += dp[j-1] * dp[i-j]
        }
        dp[i] = total
    }
    return dp[n]
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def num_trees(n)
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  dp[1] = 1 if n >= 1

  (2..n).each do |i|
    total = 0
    (1..i).each do |j|
      total += dp[j - 1] * dp[i - j]
    end
    dp[i] = total
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def numTrees(n: Int): Int = {
        val dp = new Array[Int](n + 1)
        dp(0) = 1
        for (i <- 1 to n) {
            var total = 0
            for (j <- 1 to i) {
                total += dp(j - 1) * dp(i - j)
            }
            dp(i) = total
        }
        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            let mut sum = 0i64;
            for j in 1..=i {
                sum += dp[j - 1] * dp[i - j];
            }
            dp[i] = sum;
        }
        dp[n] as i32
    }
}
```

## Racket

```racket
(define/contract (num-trees n)
  (-> exact-integer? exact-integer?)
  (let* ([dp (make-vector (+ n 1) 0)])
    (vector-set! dp 0 1)
    (for ([i (in-range 1 (+ n 1))])
      (let ([sum 0])
        (for ([j (in-range 1 (+ i 1))])
          (set! sum (+ sum (* (vector-ref dp (- j 1))
                              (vector-ref dp (- i j))))))
        (vector-set! dp i sum)))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([num_trees/1]).

-spec num_trees(integer()) -> integer().
num_trees(N) when N >= 0 ->
    C = comb(2 * N, N),
    C div (N + 1).

-spec comb(integer(), integer()) -> integer().
comb(N, K) ->
    case K > N - K of
        true -> comb(N, N - K);
        false -> comb_loop(1, K, 1, N)
    end.

-spec comb_loop(integer(), integer(), integer(), integer()) -> integer().
comb_loop(I, K, Acc, _N) when I > K ->
    Acc;
comb_loop(I, K, Acc, N) ->
    Numer = N - K + I,
    NewAcc = (Acc * Numer) div I,
    comb_loop(I + 1, K, NewAcc, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_trees(n :: integer) :: integer
  def num_trees(n) do
    arr = :array.set(0, 1, :array.new(n + 1, default: 0))

    arr =
      Enum.reduce(1..n, arr, fn i, a ->
        total =
          Enum.reduce(0..(i - 1), 0, fn left, acc ->
            right = i - 1 - left
            acc + (:array.get(left, a) * :array.get(right, a))
          end)

        :array.set(i, total, a)
      end)

    :array.get(n, arr)
  end
end
```
