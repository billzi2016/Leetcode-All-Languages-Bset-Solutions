# 3290. Maximum Multiplication Score

## Cpp

```cpp
class Solution {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        const long long INF_NEG = -(1LL << 60);
        long long dp[5];
        for (int i = 0; i <= 4; ++i) dp[i] = INF_NEG;
        dp[0] = 0;
        for (int x : b) {
            // update from higher to lower to avoid reuse of same element
            for (int k = 4; k >= 1; --k) {
                if (dp[k-1] != INF_NEG) {
                    long long cand = dp[k-1] + (long long)a[k-1] * x;
                    if (cand > dp[k]) dp[k] = cand;
                }
            }
        }
        return dp[4];
    }
};
```

## Java

```java
class Solution {
    public long maxScore(int[] a, int[] b) {
        int n = b.length;
        long[] dpPrev = new long[n];
        for (int i = 0; i < n; i++) {
            dpPrev[i] = (long) a[0] * b[i];
        }
        for (int k = 1; k < 4; k++) {
            long best = Long.MIN_VALUE;
            long[] dpCurr = new long[n];
            for (int j = 0; j < n; j++) {
                if (j > 0) {
                    best = Math.max(best, dpPrev[j - 1]);
                }
                if (best == Long.MIN_VALUE) {
                    dpCurr[j] = Long.MIN_VALUE;
                } else {
                    dpCurr[j] = best + (long) a[k] * b[j];
                }
            }
            dpPrev = dpCurr;
        }
        long ans = Long.MIN_VALUE;
        for (long v : dpPrev) {
            if (v > ans) ans = v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        INF_NEG = -10**18
        dp = [INF_NEG] * 5
        dp[0] = 0
        for x in b:
            for j in range(4, 0, -1):
                val = dp[j-1] + a[j-1] * x
                if val > dp[j]:
                    dp[j] = val
        return dp[4]
```

## Python3

```python
from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [float('-inf')] * 5
        dp[0] = 0
        for x in b:
            for t in range(3, -1, -1):
                if dp[t] != float('-inf'):
                    cur = dp[t] + a[t] * x
                    if cur > dp[t + 1]:
                        dp[t + 1] = cur
        return int(dp[4])
```

## C

```c
#include <limits.h>

long long maxScore(int* a, int aSize, int* b, int bSize) {
    (void)aSize; // aSize is always 4
    long long dp[4];
    for (int i = 0; i < 4; ++i) dp[i] = LLONG_MIN;
    
    for (int i = 0; i < bSize; ++i) {
        long long cur = (long long)a[0] * b[i];
        if (cur > dp[0]) dp[0] = cur;
        for (int k = 3; k >= 1; --k) {
            if (dp[k-1] != LLONG_MIN) {
                long long cand = dp[k-1] + (long long)a[k] * b[i];
                if (cand > dp[k]) dp[k] = cand;
            }
        }
    }
    return dp[3];
}
```

## Csharp

```csharp
public class Solution {
    public long MaxScore(int[] a, int[] b) {
        const long NEG = long.MinValue / 4;
        long[] dp = new long[5];
        for (int i = 0; i < 5; i++) dp[i] = NEG;
        dp[0] = 0;
        foreach (int val in b) {
            for (int t = 4; t >= 1; --t) {
                if (dp[t - 1] != NEG) {
                    long cand = dp[t - 1] + (long)a[t - 1] * val;
                    if (cand > dp[t]) dp[t] = cand;
                }
            }
        }
        return dp[4];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} a
 * @param {number[]} b
 * @return {number}
 */
var maxScore = function(a, b) {
    const dp = [0, -Infinity, -Infinity, -Infinity, -Infinity];
    for (let i = 0; i < b.length; ++i) {
        const val = b[i];
        for (let k = 4; k >= 1; --k) {
            if (dp[k - 1] !== -Infinity) {
                const cand = dp[k - 1] + a[k - 1] * val;
                if (cand > dp[k]) dp[k] = cand;
            }
        }
    }
    return dp[4];
};
```

## Typescript

```typescript
function maxScore(a: number[], b: number[]): number {
    const k = 4;
    const dp = new Array(k + 1).fill(Number.NEGATIVE_INFINITY);
    dp[0] = 0;
    for (const val of b) {
        for (let p = k; p >= 1; --p) {
            if (dp[p - 1] !== Number.NEGATIVE_INFINITY) {
                const cand = dp[p - 1] + a[p - 1] * val;
                if (cand > dp[p]) dp[p] = cand;
            }
        }
    }
    return dp[k];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $a
     * @param Integer[] $b
     * @return Integer
     */
    function maxScore($a, $b) {
        $NEG_INF = -PHP_INT_MAX;
        $dp = array_fill(0, 5, $NEG_INF);
        $dp[0] = 0;
        $n = count($b);
        for ($i = 0; $i < $n; $i++) {
            $val = $b[$i];
            for ($k = 4; $k >= 1; $k--) {
                if ($dp[$k - 1] !== $NEG_INF) {
                    $candidate = $dp[$k - 1] + $a[$k - 1] * $val;
                    if ($candidate > $dp[$k]) {
                        $dp[$k] = $candidate;
                    }
                }
            }
        }
        return $dp[4];
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ a: [Int], _ b: [Int]) -> Int {
        var dp = Array(repeating: Int.min, count: 5)
        dp[0] = 0
        for val in b {
            for t in stride(from: 4, through: 1, by: -1) {
                if dp[t - 1] != Int.min {
                    let candidate = dp[t - 1] + a[t - 1] * val
                    if candidate > dp[t] {
                        dp[t] = candidate
                    }
                }
            }
        }
        return dp[4]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(a: IntArray, b: IntArray): Long {
        val dp = LongArray(5) { Long.MIN_VALUE / 4 }
        dp[0] = 0L
        for (value in b) {
            var k = 4
            while (k >= 1) {
                if (dp[k - 1] != Long.MIN_VALUE / 4) {
                    val cand = dp[k - 1] + a[k - 1].toLong() * value.toLong()
                    if (cand > dp[k]) dp[k] = cand
                }
                k--
            }
        }
        return dp[4]
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<int> a, List<int> b) {
    const int NEG_INF = -(1 << 60);
    List<int> dp = List.filled(5, NEG_INF);
    dp[0] = 0;
    for (int val in b) {
      for (int j = 3; j >= 0; --j) {
        if (dp[j] != NEG_INF) {
          int cand = dp[j] + a[j] * val;
          if (cand > dp[j + 1]) dp[j + 1] = cand;
        }
      }
    }
    return dp[4];
  }
}
```

## Golang

```go
func maxScore(a []int, b []int) int64 {
	const negInf int64 = -1 << 60
	dp := [5]int64{0, negInf, negInf, negInf, negInf}
	for _, bv := range b {
		x := int64(bv)
		for k := 3; k >= 0; k-- {
			if dp[k] == negInf {
				continue
			}
			cand := dp[k] + int64(a[k])*x
			if cand > dp[k+1] {
				dp[k+1] = cand
			}
		}
	}
	return dp[4]
}
```

## Ruby

```ruby
def max_score(a, b)
  neg_inf = -(1 << 60)
  dp = Array.new(5, neg_inf)
  dp[0] = 0
  b.each do |val|
    3.downto(0) do |k|
      next if dp[k] == neg_inf
      cand = dp[k] + a[k] * val
      dp[k + 1] = cand if cand > dp[k + 1]
    end
  end
  dp[4]
end
```

## Scala

```scala
object Solution {
    def maxScore(a: Array[Int], b: Array[Int]): Long = {
        val NEG_INF: Long = Long.MinValue / 4
        var dp = Array.fill[Long](5)(NEG_INF)
        dp(0) = 0L
        for (bv <- b) {
            val v = bv.toLong
            var k = 4
            while (k >= 1) {
                if (dp(k - 1) != NEG_INF) {
                    val cand = dp(k - 1) + a(k - 1).toLong * v
                    if (cand > dp(k)) dp(k) = cand
                }
                k -= 1
            }
        }
        dp(4)
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn max_score(a: Vec<i32>, b: Vec<i32>) -> i64 {
        let mut dp = [i64::MIN / 4; 5];
        dp[0] = 0;
        for &val in b.iter() {
            let x = val as i64;
            for k in (0..4).rev() {
                let cand = dp[k] + a[k] as i64 * x;
                if cand > dp[k + 1] {
                    dp[k + 1] = cand;
                }
            }
        }
        dp[4]
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (max-score a b)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((neg-inf (- (expt 2 60))) ; sufficiently small sentinel
         (dp (make-vector 5 neg-inf)))
    (vector-set! dp 0 0)
    (for ([x b])
      (for ([k (in-range 4 0 -1)]) ; k = 4,3,2,1
        (let* ((prev (vector-ref dp (- k 1)))
               (candidate (+ prev (* (list-ref a (- k 1)) x))))
          (when (> candidate (vector-ref dp k))
            (vector-set! dp k candidate)))))
    (vector-ref dp 4)))
```

## Erlang

```erlang
-module(solution).
-export([max_score/2]).

-spec max_score(A :: [integer()], B :: [integer()]) -> integer().
max_score(A, B) ->
    case A of
        [A0, A1, A2, A3] ->
            NegInf = -(1 bsl 60),
            InitDP = {0, NegInf, NegInf, NegInf, NegInf},
            {_D0, _D1, _D2, _D3, Result} =
                lists:foldl(
                    fun (X, {D0, D1, D2, D3, D4}) ->
                        N4 = erlang:max(D4, D3 + A3 * X),
                        N3 = erlang:max(D3, D2 + A2 * X),
                        N2 = erlang:max(D2, D1 + A1 * X),
                        N1 = erlang:max(D1, D0 + A0 * X),
                        {D0, N1, N2, N3, N4}
                    end,
                    InitDP,
                    B
                ),
            Result
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(a :: [integer], b :: [integer]) :: integer
  def max_score(a, b) do
    inf = -10_000_000_000_000

    a0 = Enum.at(a, 0)
    a1 = Enum.at(a, 1)
    a2 = Enum.at(a, 2)
    a3 = Enum.at(a, 3)

    {dp4, _dp3, _dp2, _dp1} =
      Enum.reduce(b, {inf, inf, inf, inf}, fn x, {dp4, dp3, dp2, dp1} ->
        ndp4 = if dp3 == inf, do: dp4, else: max(dp4, dp3 + a3 * x)
        ndp3 = if dp2 == inf, do: dp3, else: max(dp3, dp2 + a2 * x)
        ndp2 = if dp1 == inf, do: dp2, else: max(dp2, dp1 + a1 * x)
        ndp1 = max(dp1, a0 * x)

        {ndp4, ndp3, ndp2, ndp1}
      end)

    dp4
  end
end
```
