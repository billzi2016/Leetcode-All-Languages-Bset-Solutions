# 3091. Apply Operations to Make Sum of Array Greater Than or Equal to k

## Cpp

```cpp
class Solution {
public:
    int minOperations(int k) {
        int ans = INT_MAX;
        for (int inc = 0; inc <= k; ++inc) {
            long long val = inc + 1LL;
            long long needLen = (k + val - 1) / val; // minimal length after duplicates
            long long dup = needLen - 1; // number of duplicate operations
            if (dup < 0) dup = 0;
            ans = min(ans, inc + (int)dup);
            // early break: when val exceeds k and dup becomes 0, further inc only increase total
            if (val > k && dup == 0) break;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int k) {
        if (k <= 1) return 0;
        int best = Integer.MAX_VALUE;
        for (int inc = 0; inc <= k; inc++) {
            long val = 1L + inc;                     // value after increase operations
            long needElements = (k + val - 1) / val; // ceil(k / val)
            int dup = (int) (needElements - 1);      // duplicate operations needed
            int total = inc + dup;
            if (total < best) {
                best = total;
            }
            // optional early stop: if inc already exceeds current best, further inc will only increase total
            if (inc > best) break;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        ans = float('inf')
        # iterate over possible number of increase operations
        for inc in range(k + 1):  # k <= 1e5, acceptable
            val = inc + 1                     # value after increases
            need_len = (k + val - 1) // val   # minimal array length needed
            dup = need_len - 1                # duplicate operations required
            ops = inc + dup
            if ops < ans:
                ans = ops
        return ans
```

## Python3

```python
class Solution:
    def minOperations(self, k: int) -> int:
        ans = float('inf')
        for a in range(1, k + 1):
            inc_ops = a - 1
            dup_ops = (k + a - 1) // a - 1  # ceil(k / a) - 1
            if dup_ops < 0:
                dup_ops = 0
            ans = min(ans, inc_ops + dup_ops)
        return ans
```

## C

```c
#include <limits.h>

int minOperations(int k) {
    int ans = INT_MAX;
    for (int i = 0; i <= k; ++i) {
        long v = (long)i + 1;                     // value after i increase operations
        long d = (k + v - 1) / v - 1;              // required duplicate operations
        if (d < 0) d = 0;
        int total = i + (int)d;
        if (total < ans) ans = total;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int k) {
        long K = k;
        int ans = k - 1; // all increase operations
        for (int i = 1; (long)i * i <= K; ++i) {
            int x = i - 1;                         // number of increase ops
            long need = (K + i - 1) / i;           // ceil(k / i)
            int y = (int)(need - 1);               // number of duplicate ops
            ans = Math.Min(ans, x + y);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var minOperations = function(k) {
    let best = Infinity;
    for (let inc = 0; inc <= k; ++inc) {
        const val = 1 + inc;                 // value after all increase operations
        if (val > k) {                       // further increases only worsen the answer
            best = Math.min(best, inc);
            break;
        }
        const needElems = Math.ceil(k / val); // total elements needed
        const dup = needElems - 1;           // duplicate operations
        best = Math.min(best, inc + dup);
    }
    return best;
};
```

## Typescript

```typescript
function minOperations(k: number): number {
    let ans = k - 1; // all increase operations
    const limit = Math.floor(Math.sqrt(k));
    for (let a = 1; a <= limit; a++) {
        const b = Math.ceil(k / a);
        const ops = a + b - 2;
        if (ops < ans) ans = ops;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function minOperations($k) {
        $ans = $k; // upper bound
        for ($v = 1; $v <= $k; $v++) {
            // number of duplicate operations needed after increasing to value $v
            $t = intdiv($k + $v - 1, $v) - 1;
            $ops = ($v - 1) + $t;
            if ($ops < $ans) {
                $ans = $ops;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ k: Int) -> Int {
        var answer = Int.max
        let limit = Int(Double(k).squareRoot())
        for i in 1...limit {
            let n = i                     // number of elements after duplications
            let v = (k + n - 1) / n       // required value after increases (ceil)
            let ops = v + n - 2           // total operations: (v-1) increases + (n-1) duplicates
            if ops < answer {
                answer = ops
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(k: Int): Int {
        var ans = Int.MAX_VALUE
        for (v in 1..k) {
            val needElements = (k + v - 1) / v // ceil division of k by v
            val ops = (v - 1) + (needElements - 1)
            if (ops < ans) ans = ops
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minOperations(int k) {
    int ans = k - 1; // all increase operations
    for (int i = 0; i * i <= k; ++i) {
      int v = i + 1;
      int d = ((k + v - 1) ~/ v) - 1; // required duplicate ops
      if (d < 0) d = 0;
      ans = min(ans, i + d);
    }
    return ans;
  }
}
```

## Golang

```go
func minOperations(k int) int {
	if k <= 1 {
		return 0
	}
	ans := k - 1 // all increase operations, no duplicates
	for inc := 0; inc <= k; inc++ {
		val := 1 + inc
		needElems := (k + val - 1) / val // ceil(k/val)
		dup := needElems - 1
		if total := inc + dup; total < ans {
			ans = total
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_operations(k)
  ans = Float::INFINITY
  max_d = 0
  while (1 << max_d) <= k * 2
    max_d += 1
  end
  (0..max_d).each do |d|
    pow = 1 << d
    needed = (k + pow - 1) / pow  # ceil(k / pow)
    x = needed > 1 ? needed - 1 : 0
    ops = x + d
    ans = ops if ops < ans
  end
  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minOperations(k: Int): Int = {
        var ans = Int.MaxValue
        var v = 1
        while (v <= k) {
            val t = (k + v - 1) / v
            val ops = v + t - 2
            if (ops < ans) ans = ops
            v += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(k: i32) -> i32 {
        let k = k as i64;
        let mut ans = i64::MAX;
        for inc in 0..=k {
            let v = 1 + inc; // value after increase operations
            let need = (k + v - 1) / v; // minimum number of elements needed
            let dup = need - 1; // duplicate operations required
            let ops = inc + dup;
            if ops < ans {
                ans = ops;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations k)
  (-> exact-integer? exact-integer?)
  (let* ((limit (floor (sqrt k)))
         (init (+ k 10))) ; a value larger than any possible answer
    (for/fold ([ans init]) ([v (in-range 1 (add1 limit))])
      (let* ([t (ceiling (/ k v))]
             [ops (- (+ v t) 2)])
        (if (< ops ans) ops ans)))))
```

## Erlang

```erlang
-spec min_operations(K :: integer()) -> integer().
min_operations(K) ->
    Limit = trunc(math:sqrt(K)) + 1,
    min_ops_loop(1, Limit, K, K + 1).

min_ops_loop(A, MaxA, _K, Best) when A > MaxA ->
    Best;
min_ops_loop(A, MaxA, K, Best) ->
    B = (K + A - 1) div A,
    Ops = A + B - 2,
    NewBest = if Ops < Best -> Ops; true -> Best end,
    min_ops_loop(A + 1, MaxA, K, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(k :: integer) :: integer
  def min_operations(k) do
    Enum.reduce(0..k, k, fn a, best ->
      v = a + 1
      needed = div(k + v - 1, v)   # ceil(k / v)
      b = needed - 1
      total = a + b
      if total < best, do: total, else: best
    end)
  end
end
```
