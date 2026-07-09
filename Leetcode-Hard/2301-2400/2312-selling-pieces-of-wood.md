# 2312. Selling Pieces of Wood

## Cpp

```cpp
class Solution {
public:
    long long sellingWood(int m, int n, vector<vector<int>>& prices) {
        vector<vector<long long>> price(m + 1, vector<long long>(n + 1, 0));
        for (auto &p : prices) {
            int h = p[0], w = p[1];
            long long pr = p[2];
            if (h <= m && w <= n)
                price[h][w] = max(price[h][w], pr);
        }
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                long long best = price[i][j];
                // vertical cuts
                for (int cut = 1; cut < j; ++cut) {
                    best = max(best, dp[i][cut] + dp[i][j - cut]);
                }
                // horizontal cuts
                for (int cut = 1; cut < i; ++cut) {
                    best = max(best, dp[cut][j] + dp[i - cut][j]);
                }
                dp[i][j] = best;
            }
        }
        return dp[m][n];
    }
};
```

## Java

```java
class Solution {
    public long sellingWood(int m, int n, int[][] prices) {
        int[][] priceMap = new int[m + 1][n + 1];
        for (int[] p : prices) {
            int h = p[0], w = p[1], val = p[2];
            if (h <= m && w <= n) {
                priceMap[h][w] = val;
            }
        }

        long[][] dp = new long[m + 1][n + 1];

        for (int h = 1; h <= m; ++h) {
            for (int w = 1; w <= n; ++w) {
                long best = priceMap[h][w];
                // horizontal cuts
                for (int cut = 1; cut < h; ++cut) {
                    long cand = dp[cut][w] + dp[h - cut][w];
                    if (cand > best) best = cand;
                }
                // vertical cuts
                for (int cut = 1; cut < w; ++cut) {
                    long cand = dp[h][cut] + dp[h][w - cut];
                    if (cand > best) best = cand;
                }
                dp[h][w] = best;
            }
        }

        return dp[m][n];
    }
}
```

## Python

```python
class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # set direct selling prices
        for h, w, p in prices:
            if p > dp[h][w]:
                dp[h][w] = p

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                # horizontal cuts
                best = dp[h][w]
                for cut in range(1, h // 2 + 1):
                    val = dp[cut][w] + dp[h - cut][w]
                    if val > best:
                        best = val
                # vertical cuts
                for cut in range(1, w // 2 + 1):
                    val = dp[h][cut] + dp[h][w - cut]
                    if val > best:
                        best = val
                dp[h][w] = best

        return dp[m][n]
```

## Python3

```python
from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        price_map = {(h, w): p for h, w, p in prices}
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = price_map.get((h, w), 0)

                # horizontal cuts
                for cut_h in range(1, h // 2 + 1):
                    val = dp[cut_h][w] + dp[h - cut_h][w]
                    if val > best:
                        best = val

                # vertical cuts
                for cut_w in range(1, w // 2 + 1):
                    val = dp[h][cut_w] + dp[h][w - cut_w]
                    if val > best:
                        best = val

                dp[h][w] = best

        return dp[m][n]
```

## C

```c
#include <stddef.h>

long long sellingWood(int m, int n, int** prices, int pricesSize, int* pricesColSize) {
    static long long dp[201][201];
    for (int i = 0; i <= m; ++i)
        for (int j = 0; j <= n; ++j)
            dp[i][j] = 0;

    for (int idx = 0; idx < pricesSize; ++idx) {
        int h = prices[idx][0];
        int w = prices[idx][1];
        int p = prices[idx][2];
        if (h <= m && w <= n && p > dp[h][w])
            dp[h][w] = p;
    }

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            for (int k = 1; k < j; ++k) {
                long long val = dp[i][k] + dp[i][j - k];
                if (val > dp[i][j]) dp[i][j] = val;
            }
            for (int k = 1; k < i; ++k) {
                long long val = dp[k][j] + dp[i - k][j];
                if (val > dp[i][j]) dp[i][j] = val;
            }
        }
    }

    return dp[m][n];
}
```

## Csharp

```csharp
public class Solution {
    public long SellingWood(int m, int n, int[][] prices) {
        int maxM = m;
        int maxN = n;
        long[,] priceMap = new long[maxM + 1, maxN + 1];
        foreach (var p in prices) {
            int h = p[0];
            int w = p[1];
            long pr = p[2];
            if (h <= maxM && w <= maxN) {
                priceMap[h, w] = pr;
            }
        }

        long[,] dp = new long[maxM + 1, maxN + 1];

        for (int h = 1; h <= maxM; ++h) {
            for (int w = 1; w <= maxN; ++w) {
                long best = priceMap[h, w]; // sell as whole if possible, else 0

                // vertical cuts
                for (int cut = 1; cut < w; ++cut) {
                    long val = dp[h, cut] + dp[h, w - cut];
                    if (val > best) best = val;
                }

                // horizontal cuts
                for (int cut = 1; cut < h; ++cut) {
                    long val = dp[cut, w] + dp[h - cut, w];
                    if (val > best) best = val;
                }

                dp[h, w] = best;
            }
        }

        return dp[m, n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} prices
 * @return {number}
 */
var sellingWood = function(m, n, prices) {
    const priceMap = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (const [h, w, p] of prices) {
        if (h <= m && w <= n) priceMap[h][w] = p;
    }
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

    for (let h = 1; h <= m; ++h) {
        for (let w = 1; w <= n; ++w) {
            let best = priceMap[h][w];
            // horizontal cuts
            for (let cut = 1; cut < h; ++cut) {
                const val = dp[cut][w] + dp[h - cut][w];
                if (val > best) best = val;
            }
            // vertical cuts
            for (let cut = 1; cut < w; ++cut) {
                const val = dp[h][cut] + dp[h][w - cut];
                if (val > best) best = val;
            }
            dp[h][w] = best;
        }
    }

    return dp[m][n];
};
```

## Typescript

```typescript
function sellingWood(m: number, n: number, prices: number[][]): number {
    // priceMap[h][w] = price if available, else 0
    const priceMap: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (const [h, w, p] of prices) {
        if (h <= m && w <= n) {
            priceMap[h][w] = p;
        }
    }

    const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

    for (let h = 1; h <= m; ++h) {
        for (let w = 1; w <= n; ++w) {
            let best = priceMap[h][w];

            // vertical cuts
            for (let cut = 1; cut < w; ++cut) {
                const val = dp[h][cut] + dp[h][w - cut];
                if (val > best) best = val;
            }

            // horizontal cuts
            for (let cut = 1; cut < h; ++cut) {
                const val = dp[cut][w] + dp[h - cut][w];
                if (val > best) best = val;
            }

            dp[h][w] = best;
        }
    }

    return dp[m][n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $prices
     * @return Integer
     */
    function sellingWood($m, $n, $prices) {
        // price map for direct sellable pieces
        $priceMap = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        foreach ($prices as $p) {
            $hi = $p[0];
            $wi = $p[1];
            $pr = $p[2];
            if ($hi <= $m && $wi <= $n) {
                $priceMap[$hi][$wi] = $pr;
            }
        }

        // dp[h][w] = max profit for h x w piece
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        for ($h = 1; $h <= $m; $h++) {
            for ($w = 1; $w <= $n; $w++) {
                $best = $priceMap[$h][$w]; // sell directly if possible

                // try horizontal cuts
                for ($cut = 1; $cut < $h; $cut++) {
                    $cand = $dp[$cut][$w] + $dp[$h - $cut][$w];
                    if ($cand > $best) {
                        $best = $cand;
                    }
                }

                // try vertical cuts
                for ($cut = 1; $cut < $w; $cut++) {
                    $cand = $dp[$h][$cut] + $dp[$h][$w - $cut];
                    if ($cand > $best) {
                        $best = $cand;
                    }
                }

                $dp[$h][$w] = $best;
            }
        }

        return $dp[$m][$n];
    }
}
```

## Swift

```swift
class Solution {
    func sellingWood(_ m: Int, _ n: Int, _ prices: [[Int]]) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for p in prices {
            let h = p[0]
            let w = p[1]
            let price = p[2]
            if h <= m && w <= n {
                dp[h][w] = max(dp[h][w], price)
            }
        }
        
        if m == 0 || n == 0 { return 0 }
        
        for h in 1...m {
            for w in 1...n {
                var best = dp[h][w]
                
                // horizontal cuts
                if h > 1 {
                    for cut in 1..<h {
                        let val = dp[cut][w] + dp[h - cut][w]
                        if val > best { best = val }
                    }
                }
                
                // vertical cuts
                if w > 1 {
                    for cut in 1..<w {
                        let val = dp[h][cut] + dp[h][w - cut]
                        if val > best { best = val }
                    }
                }
                
                dp[h][w] = best
            }
        }
        
        return dp[m][n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sellingWood(m: Int, n: Int, prices: Array<IntArray>): Long {
        val priceMap = Array(m + 1) { LongArray(n + 1) }
        for (p in prices) {
            val h = p[0]
            val w = p[1]
            val price = p[2].toLong()
            if (h <= m && w <= n) {
                priceMap[h][w] = price
            }
        }

        val dp = Array(m + 1) { LongArray(n + 1) }

        for (i in 1..m) {
            for (j in 1..n) {
                var best = priceMap[i][j]
                // horizontal cuts
                for (k in 1 until i) {
                    val cand = dp[k][j] + dp[i - k][j]
                    if (cand > best) best = cand
                }
                // vertical cuts
                for (k in 1 until j) {
                    val cand = dp[i][k] + dp[i][j - k]
                    if (cand > best) best = cand
                }
                dp[i][j] = best
            }
        }

        return dp[m][n]
    }
}
```

## Dart

```dart
class Solution {
  int sellingWood(int m, int n, List<List<int>> prices) {
    // price matrix for direct sell values
    List<List<int>> price = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (var p in prices) {
      int h = p[0];
      int w = p[1];
      int v = p[2];
      if (h <= m && w <= n) {
        price[h][w] = v;
      }
    }

    // dp[h][w] = max profit for piece h x w
    List<List<int>> dp = List.generate(m + 1, (_) => List.filled(n + 1, 0));

    for (int h = 1; h <= m; ++h) {
      for (int w = 1; w <= n; ++w) {
        int best = price[h][w];

        // vertical cuts
        for (int cut = 1; cut < w; ++cut) {
          int val = dp[h][cut] + dp[h][w - cut];
          if (val > best) best = val;
        }

        // horizontal cuts
        for (int cut = 1; cut < h; ++cut) {
          int val = dp[cut][w] + dp[h - cut][w];
          if (val > best) best = val;
        }

        dp[h][w] = best;
      }
    }

    return dp[m][n];
  }
}
```

## Golang

```go
func sellingWood(m int, n int, prices [][]int) int64 {
	price := make([][]int64, m+1)
	for i := 0; i <= m; i++ {
		price[i] = make([]int64, n+1)
	}
	for _, p := range prices {
		h, w, v := p[0], p[1], p[2]
		if h <= m && w <= n {
			price[h][w] = int64(v)
		}
	}
	dp := make([][]int64, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int64, n+1)
	}
	for h := 1; h <= m; h++ {
		for w := 1; w <= n; w++ {
			best := price[h][w]
			for cut := 1; cut < h; cut++ {
				cand := dp[cut][w] + dp[h-cut][w]
				if cand > best {
					best = cand
				}
			}
			for cut := 1; cut < w; cut++ {
				cand := dp[h][cut] + dp[h][w-cut]
				if cand > best {
					best = cand
				}
			}
			dp[h][w] = best
		}
	}
	return dp[m][n]
}
```

## Ruby

```ruby
def selling_wood(m, n, prices)
  price_map = {}
  prices.each do |h, w, p|
    price_map[[h, w]] = p
  end

  dp = Array.new(m + 1) { Array.new(n + 1, 0) }

  (1..m).each do |h|
    (1..n).each do |w|
      best = price_map[[h, w]] || 0

      (1...h).each do |cut|
        val = dp[cut][w] + dp[h - cut][w]
        best = val if val > best
      end

      (1...w).each do |cut|
        val = dp[h][cut] + dp[h][w - cut]
        best = val if val > best
      end

      dp[h][w] = best
    end
  end

  dp[m][n]
end
```

## Scala

```scala
object Solution {
    def sellingWood(m: Int, n: Int, prices: Array[Array[Int]]): Long = {
        val priceMap = Array.ofDim[Long](m + 1, n + 1)
        for (p <- prices) {
            val h = p(0)
            val w = p(1)
            val v = p(2).toLong
            if (h <= m && w <= n) priceMap(h)(w) = v
        }
        val dp = Array.ofDim[Long](m + 1, n + 1)
        for (i <- 1 to m) {
            for (j <- 1 to n) {
                var best = priceMap(i)(j)
                var a = 1
                while (a < i) {
                    val cand = dp(a)(j) + dp(i - a)(j)
                    if (cand > best) best = cand
                    a += 1
                }
                var b = 1
                while (b < j) {
                    val cand = dp(i)(b) + dp(i)(j - b)
                    if (cand > best) best = cand
                    b += 1
                }
                dp(i)(j) = best
            }
        }
        dp(m)(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn selling_wood(m: i32, n: i32, prices: Vec<Vec<i32>>) -> i64 {
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0i64; n + 1]; m + 1];
        for p in prices.iter() {
            let h = p[0] as usize;
            let w = p[1] as usize;
            let price = p[2] as i64;
            if dp[h][w] < price {
                dp[h][w] = price;
            }
        }
        for h in 1..=m {
            for w in 1..=n {
                // horizontal cuts
                for cut_h in 1..h {
                    let val = dp[cut_h][w] + dp[h - cut_h][w];
                    if val > dp[h][w] {
                        dp[h][w] = val;
                    }
                }
                // vertical cuts
                for cut_w in 1..w {
                    let val = dp[h][cut_w] + dp[h][w - cut_w];
                    if val > dp[h][w] {
                        dp[h][w] = val;
                    }
                }
            }
        }
        dp[m][n]
    }
}
```

## Racket

```racket
(define/contract (selling-wood m n prices)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((price-hash (make-hash)))
    (for ([p prices])
      (hash-set! price-hash (cons (first p) (second p)) (third p)))
    (define dp (make-vector (+ m 1) #f))
    (do ((i 0 (+ i 1))) ((> i m))
      (vector-set! dp i (make-vector (+ n 1) 0)))
    (for ([h (in-range 1 (+ m 1))])
      (for ([w (in-range 1 (+ n 1))])
        (define best
          (let ((key (cons h w)))
            (if (hash-has-key? price-hash key)
                (hash-ref price-hash key)
                0)))
        ;; vertical cuts
        (do ((cut 1 (+ cut 1))) ((>= cut w))
          (let* ((left (vector-ref (vector-ref dp h) cut))
                 (right (vector-ref (vector-ref dp h) (- w cut))))
            (when (> (+ left right) best)
              (set! best (+ left right)))))
        ;; horizontal cuts
        (do ((cut 1 (+ cut 1))) ((>= cut h))
          (let* ((top (vector-ref (vector-ref dp cut) w))
                 (bottom (vector-ref (vector-ref dp (- h cut)) w)))
            (when (> (+ top bottom) best)
              (set! best (+ top bottom)))))
        (vector-set! (vector-ref dp h) w best)))
    (vector-ref (vector-ref dp m) n)))
```

## Erlang

```erlang
-spec selling_wood(M :: integer(), N :: integer(), Prices :: [[integer()]]) -> integer().
selling_wood(M, N, Prices) ->
    PriceMap = build_price_map(Prices, #{}),
    DP = fill_rows(1, M, N, PriceMap, #{}),
    maps:get({M, N}, DP).

build_price_map([], Map) -> Map;
build_price_map([[H, W, P] | Rest], Map) ->
    build_price_map(Rest, maps:put({H, W}, P, Map)).

fill_rows(H, M, _N, _PriceMap, DP) when H > M -> DP;
fill_rows(H, M, N, PriceMap, DP) ->
    DP1 = fill_cols(H, 1, N, PriceMap, DP),
    fill_rows(H + 1, M, N, PriceMap, DP1).

fill_cols(_H, W, N, _PriceMap, DP) when W > N -> DP;
fill_cols(H, W, N, PriceMap, DP) ->
    Base = maps:get({H, W}, PriceMap, 0),

    Hor =
        case H > 1 of
            true ->
                lists:max(
                  [maps:get({I, W}, DP, 0) + maps:get({H - I, W}, DP, 0)
                   || I <- lists:seq(1, H - 1)])
            false -> 0
        end,

    Vert =
        case W > 1 of
            true ->
                lists:max(
                  [maps:get({H, J}, DP, 0) + maps:get({H, W - J}, DP, 0)
                   || J <- lists:seq(1, W - 1)])
            false -> 0
        end,

    MaxVal = max(Base, max(Hor, Vert)),
    DP1 = maps:put({H, W}, MaxVal, DP),
    fill_cols(H, W + 1, N, PriceMap, DP1).
```

## Elixir

```elixir
defmodule Solution do
  @spec selling_wood(m :: integer, n :: integer, prices :: [[integer]]) :: integer
  def selling_wood(m, n, prices) do
    price_map =
      Enum.reduce(prices, %{}, fn [h, w, p], acc ->
        Map.update(acc, {h, w}, p, fn existing -> max(existing, p) end)
      end)

    dp = %{}

    dp_final =
      1..m
      |> Enum.reduce(dp, fn h, dp_acc ->
        Enum.reduce(1..n, dp_acc, fn w, dp_inner ->
          base = Map.get(price_map, {h, w}, 0)

          best_vert =
            if w > 1 do
              Enum.reduce(1..(w - 1), base, fn k, cur ->
                left = Map.get(dp_inner, {h, k})
                right = Map.get(dp_inner, {h, w - k})
                max(cur, left + right)
              end)
            else
              base
            end

          best =
            if h > 1 do
              Enum.reduce(1..(h - 1), best_vert, fn k, cur ->
                top = Map.get(dp_inner, {k, w})
                bottom = Map.get(dp_inner, {h - k, w})
                max(cur, top + bottom)
              end)
            else
              best_vert
            end

          Map.put(dp_inner, {h, w}, best)
        end)
      end)

    Map.get(dp_final, {m, n}, 0)
  end
end
```
