# 0062. Unique Paths

## Cpp

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) return 0;
        int total = m + n - 2;
        int k = std::min(m - 1, n - 1);
        long long res = 1;
        for (int i = 1; i <= k; ++i) {
            res = res * (total - k + i) / i;
        }
        return static_cast<int>(res);
    }
};
```

## Java

```java
class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) return 0;
        int totalSteps = m + n - 2;
        int stepsDown = Math.min(m - 1, n - 1);
        long result = 1;
        for (int i = 1; i <= stepsDown; i++) {
            result = result * (totalSteps - stepsDown + i) / i;
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
```

## Python3

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(m + n - 2, m - 1)
```

## C

```c
int uniquePaths(int m, int n) {
    if (m == 1 || n == 1) return 1;
    int total = m + n - 2;
    int k = (m - 1 < n - 1) ? m - 1 : n - 1;
    long long res = 1;
    for (int i = 1; i <= k; ++i) {
        res = res * (total - k + i) / i;
    }
    return (int)res;
}
```

## Csharp

```csharp
public class Solution
{
    public int UniquePaths(int m, int n)
    {
        // Choose the smaller of (m-1) and (n-1) to minimize iterations
        int totalSteps = m + n - 2;
        int k = Math.Min(m - 1, n - 1);
        long result = 1;
        for (int i = 1; i <= k; i++)
        {
            result = result * (totalSteps - k + i) / i;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    // Ensure the DP array is the smaller dimension for less space.
    if (n > m) {
        [m, n] = [n, m];
    }
    const dp = new Array(n).fill(1);
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[j] += dp[j - 1];
        }
    }
    return dp[n - 1];
};
```

## Typescript

```typescript
function uniquePaths(m: number, n: number): number {
    if (m === 1 || n === 1) return 1;
    const total = m + n - 2;
    const k = Math.min(m - 1, n - 1);
    let result = 1;
    for (let i = 1; i <= k; i++) {
        result = result * (total - k + i) / i;
    }
    return Math.round(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function uniquePaths($m, $n) {
        $dp = array_fill(0, $n, 1);
        for ($i = 1; $i < $m; $i++) {
            for ($j = 1; $j < $n; $j++) {
                $dp[$j] += $dp[$j - 1];
            }
        }
        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        let rows = m
        let cols = n
        var dp = [Int](repeating: 1, count: min(rows, cols))
        let larger = max(rows, cols)
        if larger > 1 && dp.count > 0 {
            for _ in 1..<larger {
                for i in 1..<dp.count {
                    dp[i] += dp[i - 1]
                }
            }
        }
        return dp.last ?? 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniquePaths(m: Int, n: Int): Int {
        val totalMoves = m + n - 2
        var k = if (m - 1 < n - 1) m - 1 else n - 1
        var result = 1L
        for (i in 1..k) {
            result = result * (totalMoves - k + i).toLong() / i.toLong()
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int uniquePaths(int m, int n) {
    int total = m + n - 2;
    int k = (m < n) ? m - 1 : n - 1; // choose smaller for efficiency
    int result = 1;
    for (int i = 1; i <= k; i++) {
      result = result * (total - k + i) ~/ i;
    }
    return result;
  }
}
```

## Golang

```go
func uniquePaths(m int, n int) int {
    total := m + n - 2
    k := m - 1
    if n-1 < k {
        k = n - 1
    }
    var res int64 = 1
    for i := 1; i <= k; i++ {
        res = res * int64(total-k+i) / int64(i)
    }
    return int(res)
}
```

## Ruby

```ruby
def unique_paths(m, n)
  total = m + n - 2
  k = [m - 1, n - 1].min
  result = 1
  (1..k).each do |i|
    result = result * (total - k + i) / i
  end
  result
end
```

## Scala

```scala
object Solution {
    def uniquePaths(m: Int, n: Int): Int = {
        if (m == 0 || n == 0) return 0
        val total = m + n - 2
        val k = math.min(m - 1, n - 1)
        var res: Long = 1L
        for (i <- 1 to k) {
            res = res * (total - k + i) / i
        }
        res.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let m = m as u64;
        let n = n as u64;
        if m == 1 || n == 1 {
            return 1;
        }
        let total = m + n - 2;
        let k = std::cmp::min(m - 1, n - 1);
        let mut res: u64 = 1;
        for i in 1..=k {
            res = res * (total - k + i) / i;
        }
        res as i32
    }
}
```

## Racket

```racket
(define/contract (unique-paths m n)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((total (- (+ m n) 2))
         (k (min (- m 1) (- n 1))))
    (if (= k 0)
        1
        (let loop ((i 1) (res 1))
          (if (> i k)
              res
              (loop (+ i 1)
                    (/ (* res (+ (- total k) i)) i)))))))
```

## Erlang

```erlang
-module(solution).
-export([unique_paths/2]).

-spec unique_paths(M :: integer(), N :: integer()) -> integer().
unique_paths(M, N) ->
    Total = M + N - 2,
    K = min(M - 1, N - 1),
    calc(Total, K, 1, 1).

calc(_Total, 0, _I, Acc) ->
    Acc;
calc(Total, K, I, Acc) when I =< K ->
    Num = Total - K + I,
    NewAcc = (Acc * Num) div I,
    calc(Total, K, I + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_paths(m :: integer, n :: integer) :: integer
  def unique_paths(m, n) do
    total = m + n - 2
    k = min(m - 1, n - 1)

    Enum.reduce(1..k, 1, fn i, acc ->
      div(acc * (total - k + i), i)
    end)
  end
end
```
