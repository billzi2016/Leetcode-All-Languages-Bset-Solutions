# 0808. Soup Servings

## Cpp

```cpp
class Solution {
public:
    double dp[201][201];
    
    double solve(int a, int b) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;
        if (dp[a][b] >= 0) return dp[a][b];
        double res = 0.25 * (
            solve(a - 4, b) +
            solve(a - 3, b - 1) +
            solve(a - 2, b - 2) +
            solve(a - 1, b - 3)
        );
        dp[a][b] = res;
        return res;
    }
    
    double soupServings(int n) {
        int m = (n + 24) / 25; // ceil division
        if (m > 200) return 1.0; // sufficient precision cutoff
        for (int i = 0; i <= 200; ++i)
            for (int j = 0; j <= 200; ++j)
                dp[i][j] = -1.0;
        return solve(m, m);
    }
};
```

## Java

```java
class Solution {
    public double soupServings(int n) {
        int m = (n + 24) / 25; // ceil division by 25
        if (m == 0) return 0.5;
        if (m > 200) return 1.0; // sufficient precision cutoff
        
        double[][] memo = new double[m + 1][m + 1];
        for (int i = 0; i <= m; i++) {
            java.util.Arrays.fill(memo[i], -1.0);
        }
        
        return dfs(m, m, memo);
    }
    
    private double dfs(int a, int b, double[][] memo) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;
        if (memo[a][b] >= 0) return memo[a][b];
        
        double prob = 0.25 * (
            dfs(Math.max(0, a - 4), b, memo) +
            dfs(Math.max(0, a - 3), Math.max(0, b - 1), memo) +
            dfs(Math.max(0, a - 2), Math.max(0, b - 2), memo) +
            dfs(Math.max(0, a - 1), Math.max(0, b - 3), memo)
        );
        memo[a][b] = prob;
        return prob;
    }
}
```

## Python

```python
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # For large n the probability is effectively 1.
        if n > 4800:
            return 1.0

        m = (n + 24) // 25  # ceil division by 25

        from functools import lru_cache

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (dp(a - 4, b) +
                           dp(a - 3, b - 1) +
                           dp(a - 2, b - 2) +
                           dp(a - 1, b - 3))

        return dp(m, m)
```

## Python3

```python
class Solution:
    def soupServings(self, n: int) -> float:
        from functools import lru_cache

        # Convert milliliters to servings of 25ml each (ceil)
        m = (n + 24) // 25
        # For large m the answer is effectively 1.0 within required precision.
        if m > 200:
            return 1.0

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(m, m)
```

## C

```c
#include <stdio.h>

static double memo[201][201];

double dfs(int a, int b) {
    if (a <= 0 && b <= 0) return 0.5;
    if (a <= 0) return 1.0;
    if (b <= 0) return 0.0;
    if (memo[a][b] >= 0.0) return memo[a][b];
    double res = 0.25 * (
        dfs(a - 4, b) +
        dfs(a - 3, b - 1) +
        dfs(a - 2, b - 2) +
        dfs(a - 1, b - 3)
    );
    memo[a][b] = res;
    return res;
}

double soupServings(int n) {
    int m = (n + 24) / 25;               // ceil(n/25)
    if (m > 200) return 1.0;            // sufficient precision cutoff
    for (int i = 0; i <= 200; ++i)
        for (int j = 0; j <= 200; ++j)
            memo[i][j] = -1.0;
    return dfs(m, m);
}
```

## Csharp

```csharp
using System;

public class Solution {
    public double SoupServings(int n) {
        int m = (n + 24) / 25; // ceil division
        if (m >= 200) return 1.0;
        
        double[,] memo = new double[m + 1, m + 1];
        bool[,] visited = new bool[m + 1, m + 1];
        
        double Dfs(int a, int b) {
            if (a <= 0 && b <= 0) return 0.5;
            if (a <= 0) return 1.0;
            if (b <= 0) return 0.0;
            if (visited[a, b]) return memo[a, b];
            
            visited[a, b] = true;
            double prob = 0.25 * (
                Dfs(Math.Max(0, a - 4), b) +
                Dfs(Math.Max(0, a - 3), Math.Max(0, b - 1)) +
                Dfs(Math.Max(0, a - 2), Math.Max(0, b - 2)) +
                Dfs(Math.Max(0, a - 1), Math.Max(0, b - 3))
            );
            memo[a, b] = prob;
            return prob;
        }
        
        return Dfs(m, m);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var soupServings = function(n) {
    // Convert milliliters to servings of 25ml each (ceil)
    const m = Math.ceil(n / 25);
    // For large m the answer is effectively 1 within required precision
    if (m > 200) return 1.0;

    const memo = new Map();

    function dfs(a, b) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;
        const key = a + ',' + b;
        if (memo.has(key)) return memo.get(key);
        const prob = 0.25 * (
            dfs(a - 4, b) +
            dfs(a - 3, b - 1) +
            dfs(a - 2, b - 2) +
            dfs(a - 1, b - 3)
        );
        memo.set(key, prob);
        return prob;
    }

    return dfs(m, m);
};
```

## Typescript

```typescript
function soupServings(n: number): number {
    const m = Math.ceil(n / 25);
    if (m > 200) return 1;
    const memo = new Map<string, number>();
    function dp(a: number, b: number): number {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1;
        if (b <= 0) return 0;
        const key = `${a},${b}`;
        if (memo.has(key)) return memo.get(key)!;
        const res = 0.25 * (
            dp(a - 4, b) +
            dp(a - 3, b - 1) +
            dp(a - 2, b - 2) +
            dp(a - 1, b - 3)
        );
        memo.set(key, res);
        return res;
    }
    return dp(m, m);
}
```

## Php

```php
class Solution {
    private $memo = [];

    /**
     * @param Integer $n
     * @return Float
     */
    function soupServings($n) {
        // Convert milliliters to servings of 25ml, rounding up.
        $m = intdiv($n + 24, 25);
        // For large m the answer is effectively 1 within required precision.
        if ($m > 200) {
            return 1.0;
        }
        return $this->dfs($m, $m);
    }

    private function dfs($a, $b) {
        if ($a <= 0 && $b <= 0) {
            return 0.5;
        }
        if ($a <= 0) {
            return 1.0;
        }
        if ($b <= 0) {
            return 0.0;
        }

        $key = $a . ',' . $b;
        if (isset($this->memo[$key])) {
            return $this->memo[$key];
        }

        $res = 0.25 * (
            $this->dfs($a - 4, $b) +
            $this->dfs($a - 3, $b - 1) +
            $this->dfs($a - 2, $b - 2) +
            $this->dfs($a - 1, $b - 3)
        );

        $this->memo[$key] = $res;
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func soupServings(_ n: Int) -> Double {
        let m = (n + 24) / 25
        if m >= 200 { return 1.0 }
        var memo = Array(repeating: Array(repeating: -1.0, count: m + 1), count: m + 1)
        func dfs(_ a: Int, _ b: Int) -> Double {
            if a <= 0 && b <= 0 { return 0.5 }
            if a <= 0 { return 1.0 }
            if b <= 0 { return 0.0 }
            if memo[a][b] >= 0 { return memo[a][b] }
            let res = 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3))
            memo[a][b] = res
            return res
        }
        return dfs(m, m)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun soupServings(n: Int): Double {
        val m = (n + 24) / 25  // ceil division
        if (m > 200) return 1.0

        val memo = HashMap<Pair<Int, Int>, Double>()

        fun dfs(a: Int, b: Int): Double {
            if (a <= 0 && b <= 0) return 0.5
            if (a <= 0) return 1.0
            if (b <= 0) return 0.0

            val key = a to b
            memo[key]?.let { return it }

            val prob = 0.25 * (
                    dfs(a - 4, b) +
                    dfs(a - 3, b - 1) +
                    dfs(a - 2, b - 2) +
                    dfs(a - 1, b - 3)
                )
            memo[key] = prob
            return prob
        }

        return dfs(m, m)
    }
}
```

## Dart

```dart
class Solution {
  double soupServings(int n) {
    int m = (n + 24) ~/ 25; // ceil division
    if (m == 0) return 0.5;
    if (m > 200) return 1.0;

    List<List<double>> memo =
        List.generate(m + 1, (_) => List.filled(m + 1, -1.0));

    double dfs(int i, int j) {
      if (i <= 0 && j <= 0) return 0.5;
      if (i <= 0) return 1.0;
      if (j <= 0) return 0.0;

      int ii = i > m ? m : i;
      int jj = j > m ? m : j;
      if (memo[ii][jj] >= 0) return memo[ii][jj];

      double res = 0.25 *
          (dfs(i - 4, j) +
              dfs(i - 3, j - 1) +
              dfs(i - 2, j - 2) +
              dfs(i - 1, j - 3));

      memo[ii][jj] = res;
      return res;
    }

    return dfs(m, m);
  }
}
```

## Golang

```go
func soupServings(n int) float64 {
	if n == 0 {
		return 0.5
	}
	m := (n + 24) / 25 // ceil division by 25
	if m > 200 { // threshold where answer is effectively 1
		return 1.0
	}
	dp := make([][]float64, m+1)
	for i := range dp {
		dp[i] = make([]float64, m+1)
		for j := range dp[i] {
			dp[i][j] = -1.0
		}
	}
	var dfs func(int, int) float64
	dfs = func(a, b int) float64 {
		if a <= 0 && b <= 0 {
			return 0.5
		}
		if a <= 0 {
			return 1.0
		}
		if b <= 0 {
			return 0.0
		}
		if dp[a][b] >= 0 {
			return dp[a][b]
		}
		res := 0.25 * (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1, b-3))
		dp[a][b] = res
		return res
	}
	return dfs(m, m)
}
```

## Ruby

```ruby
def soup_servings(n)
  m = (n + 24) / 25
  return 1.0 if m >= 200

  dp = {}
  dfs = nil
  dfs = lambda do |i, j|
    return 0.5 if i <= 0 && j <= 0
    return 1.0 if i <= 0 && j > 0
    return 0.0 if i > 0 && j <= 0

    key = [i, j]
    return dp[key] if dp.key?(key)

    prob = 0.25 * (
      dfs.call(i - 4, j) +
      dfs.call(i - 3, j - 1) +
      dfs.call(i - 2, j - 2) +
      dfs.call(i - 1, j - 3)
    )
    dp[key] = prob
    prob
  end

  dfs.call(m, m)
end
```

## Scala

```scala
object Solution {
    def soupServings(n: Int): Double = {
        val m = (n + 24) / 25 // ceil division
        if (m == 0) return 0.5
        // For large m, probability is effectively 1
        if (m > 200) return 1.0

        val dp = Array.ofDim[Double](m + 1, m + 1)

        // base cases
        for (i <- 0 to m) {
            dp(0)(i) = 1.0          // A empty first
            dp(i)(0) = 0.0          // B empty first
        }
        dp(0)(0) = 0.5

        for (i <- 1 to m) {
            for (j <- 1 to m) {
                val a = dp(math.max(0, i - 4))(j)
                val b = dp(math.max(0, i - 3))(math.max(0, j - 1))
                val c = dp(math.max(0, i - 2))(math.max(0, j - 2))
                val d = dp(math.max(0, i - 1))(math.max(0, j - 3))
                dp(i)(j) = 0.25 * (a + b + c + d)
            }
        }

        dp(m)(m)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        // Convert milliliters to servings of 25 ml each, rounding up.
        let m = (n + 24) / 25;
        // For large enough m the answer is effectively 1.0 within required precision.
        if m >= 200 {
            return 1.0;
        }

        use std::collections::HashMap;

        fn dfs(i: i32, j: i32, memo: &mut HashMap<(i32, i32), f64>) -> f64 {
            if i <= 0 && j <= 0 {
                return 0.5;
            }
            if i <= 0 {
                return 1.0;
            }
            if j <= 0 {
                return 0.0;
            }
            if let Some(&v) = memo.get(&(i, j)) {
                return v;
            }
            let prob = 0.25
                * (dfs(i - 4, j, memo)
                    + dfs(i - 3, j - 1, memo)
                    + dfs(i - 2, j - 2, memo)
                    + dfs(i - 1, j - 3, memo));
            memo.insert((i, j), prob);
            prob
        }

        let mut memo: HashMap<(i32, i32), f64> = HashMap::new();
        dfs(m, m, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (soup-servings n)
  (-> exact-integer? flonum?)
  (let* ([m (ceiling (/ n 25.0))])
    (if (>= m 200)
        1.0
        (let ([memo (make-hash)])
          (define (dp i j)
            (cond [(and (<= i 0) (<= j 0)) 0.5]
                  [(<= i 0) 1.0]
                  [(<= j 0) 0.0]
                  [else
                   (let ([key (cons i j)])
                     (if (hash-has-key? memo key)
                         (hash-ref memo key)
                         (let* ([val (/ (+ (dp (- i 4) j)
                                           (dp (- i 3) (- j 1))
                                           (dp (- i 2) (- j 2))
                                           (dp (- i 1) (- j 3)))
                                        4.0)])
                           (hash-set! memo key val)
                           val))))]))
          (dp m m)))))
```

## Erlang

```erlang
-module(solution).
-export([soup_servings/1]).

-spec soup_servings(N :: integer()) -> float().
soup_servings(N) ->
    M = (N + 24) div 25,
    case M > 200 of
        true -> 1.0;
        false ->
            {Ans, _} = dfs(M, M, #{}),
            Ans
    end.

dfs(I, J, Memo) when I =< 0, J =< 0 ->
    {0.5, Memo};
dfs(I, _J, Memo) when I =< 0 ->
    {1.0, Memo};
dfs(_I, J, Memo) when J =< 0 ->
    {0.0, Memo};
dfs(I, J, Memo) ->
    case maps:find({I, J}, Memo) of
        {ok, V} ->
            {V, Memo};
        error ->
            {V1, M1} = dfs(I - 4, J, Memo),
            {V2, M2} = dfs(I - 3, J - 1, M1),
            {V3, M3} = dfs(I - 2, J - 2, M2),
            {V4, M4} = dfs(I - 1, J - 3, M3),
            V = (V1 + V2 + V3 + V4) / 4.0,
            NewMemo = maps:put({I, J}, V, M4),
            {V, NewMemo}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec soup_servings(n :: integer) :: float
  def soup_servings(n) do
    m = div(n + 24, 25)  # ceil division by 25

    if m > 200 do
      1.0
    else
      {ans, _} = dfs(m, m, %{})
      ans
    end
  end

  defp dfs(i, j, memo) when i <= 0 and j <= 0, do: {0.5, memo}
  defp dfs(i, _j, memo) when i <= 0, do: {1.0, memo}
  defp dfs(_i, j, memo) when j <= 0, do: {0.0, memo}

  defp dfs(i, j, memo) do
    case Map.fetch(memo, {i, j}) do
      {:ok, val} ->
        {val, memo}

      :error ->
        {v1, m1} = dfs(i - 4, j, memo)
        {v2, m2} = dfs(i - 3, j - 1, m1)
        {v3, m3} = dfs(i - 2, j - 2, m2)
        {v4, m4} = dfs(i - 1, j - 3, m3)

        val = 0.25 * (v1 + v2 + v3 + v4)
        new_memo = Map.put(m4, {i, j}, val)
        {val, new_memo}
    end
  end
end
```
