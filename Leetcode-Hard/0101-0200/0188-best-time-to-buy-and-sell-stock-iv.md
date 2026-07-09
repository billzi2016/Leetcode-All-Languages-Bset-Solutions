# 0188. Best Time to Buy and Sell Stock IV

## Cpp

```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n == 0 || k == 0) return 0;
        // If k >= n/2, we can make unlimited transactions.
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; ++i)
                if (prices[i] > prices[i - 1])
                    profit += prices[i] - prices[i - 1];
            return profit;
        }
        vector<vector<int>> dp(k + 1, vector<int>(n, 0));
        for (int t = 1; t <= k; ++t) {
            int maxDiff = -prices[0]; // dp[t-1][0] - prices[0]
            for (int i = 1; i < n; ++i) {
                dp[t][i] = max(dp[t][i - 1], prices[i] + maxDiff);
                maxDiff = max(maxDiff, dp[t - 1][i] - prices[i]);
            }
        }
        return dp[k][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0 || k == 0) return 0;
        // If k is large enough, treat as unlimited transactions
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    profit += prices[i] - prices[i - 1];
                }
            }
            return profit;
        }

        int[][] dp = new int[k + 1][n];
        for (int t = 1; t <= k; t++) {
            int maxDiff = -prices[0]; // dp[t-1][0] - price[0]
            for (int i = 1; i < n; i++) {
                dp[t][i] = Math.max(dp[t][i - 1], prices[i] + maxDiff);
                maxDiff = Math.max(maxDiff, dp[t - 1][i] - prices[i]);
            }
        }
        return dp[k][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k is large enough, treat as unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                diff = prices[i] - prices[i - 1]
                if diff > 0:
                    profit += diff
            return profit

        # dp[t][i]: max profit up to day i with at most t transactions
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]  # max(dp[t-1][j] - prices[j]) for j < i
            for i in range(1, n):
                dp[t][i] = max(dp[t][i - 1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t - 1][i] - prices[i])

        return dp[k][n - 1]
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        # If transactions are effectively unlimited
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                diff = prices[i] - prices[i - 1]
                if diff > 0:
                    profit += diff
            return profit

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]  # max(dp[t-1][j] - prices[j]) for j < i
            for i in range(1, n):
                dp[t][i] = max(dp[t][i - 1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t - 1][i] - prices[i])

        return dp[k][n - 1]
```

## C

```c
#include <stdlib.h>

static inline int max(int a, int b) { return a > b ? a : b; }

int maxProfit(int k, int* prices, int pricesSize) {
    if (pricesSize == 0 || k == 0) return 0;

    /* Unlimited transactions case */
    if (k >= pricesSize / 2) {
        int profit = 0;
        for (int i = 1; i < pricesSize; ++i)
            if (prices[i] > prices[i - 1])
                profit += prices[i] - prices[i - 1];
        return profit;
    }

    /* DP: dp[t][i] = max profit up to day i with at most t transactions */
    int **dp = (int **)malloc((k + 1) * sizeof(int *));
    for (int t = 0; t <= k; ++t)
        dp[t] = (int *)calloc(pricesSize, sizeof(int));

    for (int t = 1; t <= k; ++t) {
        int maxDiff = -prices[0];               /* dp[t-1][0] - price[0] */
        for (int i = 1; i < pricesSize; ++i) {
            dp[t][i] = max(dp[t][i - 1], prices[i] + maxDiff);
            maxDiff = max(maxDiff, dp[t - 1][i] - prices[i]);
        }
    }

    int result = dp[k][pricesSize - 1];
    for (int t = 0; t <= k; ++t) free(dp[t]);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProfit(int k, int[] prices) {
        if (prices == null || prices.Length == 0) return 0;
        int n = prices.Length;
        // If k is large enough, treat as unlimited transactions
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1])
                    profit += prices[i] - prices[i - 1];
            }
            return profit;
        }

        int[] buy = new int[k + 1];
        int[] sell = new int[k + 1];
        const int NEG_INF = int.MinValue / 2;

        for (int i = 0; i <= k; i++) {
            buy[i] = NEG_INF;
            sell[i] = 0;
        }
        // First possible buy with zero completed transactions
        buy[0] = -prices[0];

        for (int day = 1; day < n; day++) {
            int price = prices[day];
            // Update sells: completing a transaction
            for (int t = 1; t <= k; t++) {
                sell[t] = Math.Max(sell[t], buy[t - 1] + price);
            }
            // Update buys: starting a new transaction
            for (int t = 0; t < k; t++) {
                buy[t] = Math.Max(buy[t], sell[t] - price);
            }
        }

        int maxProfit = 0;
        for (int t = 0; t <= k; t++) {
            if (sell[t] > maxProfit) maxProfit = sell[t];
        }
        return maxProfit;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    const n = prices.length;
    if (n === 0 || k === 0) return 0;

    // If transactions are effectively unlimited
    if (k >= Math.floor(n / 2)) {
        let profit = 0;
        for (let i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
        }
        return profit;
    }

    const buy = new Array(k + 1).fill(-Infinity);
    const sell = new Array(k + 1).fill(0);

    for (const price of prices) {
        for (let t = 1; t <= k; t++) {
            buy[t] = Math.max(buy[t], sell[t - 1] - price);
            sell[t] = Math.max(sell[t], buy[t] + price);
        }
    }

    return sell[k];
};
```

## Typescript

```typescript
function maxProfit(k: number, prices: number[]): number {
    const n = prices.length;
    if (n === 0) return 0;

    // If k is large enough, treat as unlimited transactions
    if (k >= Math.floor(n / 2)) {
        let profit = 0;
        for (let i = 1; i < n; ++i) {
            if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
        }
        return profit;
    }

    const hold: number[] = new Array(k + 1).fill(-Infinity);
    const cash: number[] = new Array(k + 1).fill(0);

    for (const price of prices) {
        for (let t = 1; t <= k; ++t) {
            hold[t] = Math.max(hold[t], cash[t - 1] - price);
            cash[t] = Math.max(cash[t], hold[t] + price);
        }
    }

    return cash[k];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($k, $prices) {
        $n = count($prices);
        if ($n == 0 || $k == 0) return 0;

        // If k is large enough, treat as unlimited transactions
        if ($k >= intdiv($n, 2)) {
            $profit = 0;
            for ($i = 1; $i < $n; $i++) {
                if ($prices[$i] > $prices[$i - 1]) {
                    $profit += $prices[$i] - $prices[$i - 1];
                }
            }
            return $profit;
        }

        // DP arrays
        $buy = array_fill(0, $k + 1, PHP_INT_MIN);
        $sell = array_fill(0, $k + 1, 0); // sell[0] = 0

        foreach ($prices as $price) {
            for ($t = $k; $t >= 1; $t--) {
                // Max profit after t-th buy (holding a stock)
                $buy[$t] = max($buy[$t], $sell[$t - 1] - $price);
                // Max profit after t-th sell (not holding)
                $sell[$t] = max($sell[$t], $buy[$t] + $price);
            }
        }

        return $sell[$k];
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ k: Int, _ prices: [Int]) -> Int {
        let n = prices.count
        if n == 0 || k == 0 { return 0 }
        if k >= n / 2 {
            var profit = 0
            for i in 1..<n {
                if prices[i] > prices[i - 1] {
                    profit += prices[i] - prices[i - 1]
                }
            }
            return profit
        }
        var buy = Array(repeating: Int.min / 2, count: k + 1)
        var sell = Array(repeating: 0, count: k + 1)
        for price in prices {
            for t in stride(from: k, through: 1, by: -1) {
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)
            }
        }
        return sell[k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(k: Int, prices: IntArray): Int {
        val n = prices.size
        if (n == 0) return 0
        if (k >= n / 2) {
            var profit = 0
            for (i in 1 until n) {
                if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1]
            }
            return profit
        }
        val buy = IntArray(k + 1) { Int.MIN_VALUE / 2 }
        val sell = IntArray(k + 1)
        for (price in prices) {
            for (t in 1..k) {
                buy[t] = maxOf(buy[t], sell[t - 1] - price)
                sell[t] = maxOf(sell[t], buy[t] + price)
            }
        }
        return sell[k]
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(int k, List<int> prices) {
    int n = prices.length;
    if (n == 0) return 0;
    if (k >= n ~/ 2) {
      int profit = 0;
      for (int i = 1; i < n; ++i) {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
      }
      return profit;
    }

    List<int> dpPrev = List.filled(n, 0);
    List<int> dpCurr = List.filled(n, 0);

    for (int t = 1; t <= k; ++t) {
      int maxDiff = -prices[0];
      dpCurr[0] = 0;
      for (int i = 1; i < n; ++i) {
        dpCurr[i] = dpCurr[i - 1];
        int candidate = prices[i] + maxDiff;
        if (candidate > dpCurr[i]) dpCurr[i] = candidate;
        int diff = dpPrev[i] - prices[i];
        if (diff > maxDiff) maxDiff = diff;
      }
      var tmp = dpPrev;
      dpPrev = dpCurr;
      dpCurr = tmp;
    }

    return dpPrev[n - 1];
  }
}
```

## Golang

```go
func maxProfit(k int, prices []int) int {
    n := len(prices)
    if k == 0 || n == 0 {
        return 0
    }
    // If transactions are effectively unlimited.
    if k >= n/2 {
        profit := 0
        for i := 1; i < n; i++ {
            if diff := prices[i] - prices[i-1]; diff > 0 {
                profit += diff
            }
        }
        return profit
    }

    dpBuy := make([]int, k+1)
    dpSell := make([]int, k+1)

    const negInf = -1 << 60
    for i := 0; i <= k; i++ {
        dpBuy[i] = negInf
        dpSell[i] = 0
    }

    for _, price := range prices {
        for t := 1; t <= k; t++ {
            if v := dpSell[t-1] - price; v > dpBuy[t] {
                dpBuy[t] = v
            }
            if v := dpBuy[t] + price; v > dpSell[t] {
                dpSell[t] = v
            }
        }
    }

    return dpSell[k]
}
```

## Ruby

```ruby
def max_profit(k, prices)
  n = prices.length
  return 0 if k == 0 || n == 0

  # Unlimited transactions case
  if k >= n / 2
    profit = 0
    (1...n).each do |i|
      diff = prices[i] - prices[i - 1]
      profit += diff if diff > 0
    end
    return profit
  end

  buy = Array.new(k + 1, -Float::INFINITY)
  sell = Array.new(k + 1, 0)

  prices.each do |price|
    (1..k).each do |j|
      # best profit after buying j-th stock
      if sell[j - 1] - price > buy[j]
        buy[j] = sell[j - 1] - price
      end
      # best profit after selling j-th stock
      if buy[j] + price > sell[j]
        sell[j] = buy[j] + price
      end
    end
  end

  sell[k]
end
```

## Scala

```scala
object Solution {
    def maxProfit(k: Int, prices: Array[Int]): Int = {
        val n = prices.length
        if (k == 0 || n == 0) return 0

        // If k is large enough, treat as unlimited transactions
        if (k >= n / 2) {
            var profit = 0
            var i = 1
            while (i < n) {
                val diff = prices(i) - prices(i - 1)
                if (diff > 0) profit += diff
                i += 1
            }
            return profit
        }

        val buy = Array.fill(k + 1)(Int.MinValue / 2) // avoid overflow
        val sell = new Array[Int](k + 1)

        var priceIdx = 0
        while (priceIdx < n) {
            val price = prices(priceIdx)
            var t = 1
            while (t <= k) {
                buy(t) = Math.max(buy(t), sell(t - 1) - price)
                sell(t) = Math.max(sell(t), buy(t) + price)
                t += 1
            }
            priceIdx += 1
        }

        sell(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        let n = prices.len();
        if n == 0 || k == 0 {
            return 0;
        }
        let k_usize = k as usize;
        // If k is large enough, treat as unlimited transactions
        if k_usize >= n / 2 {
            let mut profit = 0;
            for i in 1..n {
                if prices[i] > prices[i - 1] {
                    profit += prices[i] - prices[i - 1];
                }
            }
            return profit;
        }

        // DP arrays: cash[t] = max profit with t transactions, not holding stock
        // hold[t] = max profit with t transactions, currently holding a stock
        let mut cash = vec![0i32; k_usize + 1];
        let mut hold = vec![i32::MIN / 2; k_usize + 1]; // effectively -infinity

        for price in prices {
            for t in 1..=k_usize {
                // Sell stock: transition from holding to not holding
                cash[t] = cash[t].max(hold[t] + price);
                // Buy stock: transition from not holding (t-1 transactions) to holding
                hold[t] = hold[t].max(cash[t - 1] - price);
            }
        }

        cash[k_usize]
    }
}
```

## Racket

```racket
(define/contract (max-profit k prices)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((n (length prices)))
    (if (or (= n 0) (= n 1))
        0
        (let ((prices-v (list->vector prices)))
          (if (>= k (quotient n 2))
              ;; Unlimited transactions case
              (let loop ((i 1) (profit 0))
                (if (>= i n)
                    profit
                    (let* ((diff (- (vector-ref prices-v i)
                                    (vector-ref prices-v (sub1 i))))
                           (add (if (> diff 0) diff 0)))
                      (loop (add1 i) (+ profit add)))))
              ;; DP for limited transactions
              (let loop-t ((t 1) (prev (make-vector n 0)))
                (if (> t k)
                    (vector-ref prev (sub1 n))
                    (let* ((cur (make-vector n 0))
                           (init-best (- (vector-ref prices-v 0)))) ; dp[t-1][0] - price[0]
                      (let inner-loop ((i 1) (best init-best))
                        (if (>= i n)
                            (loop-t (add1 t) cur)
                            (begin
                              (define profit-with-sell (+ (vector-ref prices-v i) best))
                              (define profit-no-sell (vector-ref cur (sub1 i)))
                              (vector-set! cur i (if (> profit-with-sell profit-no-sell)
                                                    profit-with-sell
                                                    profit-no-sell))
                              (define new-best (max best (- (vector-ref prev i)
                                                            (vector-ref prices-v i))))
                              (inner-loop (add1 i) new-best))))))))))))
```

## Erlang

```erlang
-spec max_profit(K :: integer(), Prices :: [integer()]) -> integer().
max_profit(K, Prices) ->
    case Prices of
        [] -> 0;
        [_] -> 0;
        _ ->
            N = length(Prices),
            if K >= N div 2 ->
                unlimited_profit(Prices);
               true ->
                dp_profit(K, Prices)
            end
    end.

unlimited_profit(Prices) ->
    unlimited_profit(Prices, 0).

unlimited_profit([], Acc) -> Acc;
unlimited_profit([_], Acc) -> Acc;
unlimited_profit([Prev, Curr | Rest], Acc) ->
    Diff = Curr - Prev,
    NewAcc = if Diff > 0 -> Acc + Diff; true -> Acc end,
    unlimited_profit([Curr|Rest], NewAcc).

dp_profit(K, Prices) ->
    NegInf = -1000000000,
    HoldTuple = list_to_tuple(lists:duplicate(K+1, NegInf)),
    CashTuple = list_to_tuple(lists:duplicate(K+1, 0)),
    dp_loop(Prices, HoldTuple, CashTuple, K).

dp_loop([], _Hold, CashTuple, K) ->
    element(K, CashTuple);
dp_loop([Price | Rest], HoldTuple, CashTuple, K) ->
    {NewHold, NewCash} = update_transactions(1, K, Price, HoldTuple, CashTuple, HoldTuple, CashTuple),
    dp_loop(Rest, NewHold, NewCash, K).

update_transactions(T, K, _Price, _OldHold, _OldCash, CurHold, CurCash) when T > K ->
    {CurHold, CurCash};
update_transactions(T, K, Price, OldHold, OldCash, CurHold, CurCash) ->
    PrevCash = case T of
        1 -> 0;
        _ -> element(T-1, OldCash)
    end,
    HoldPrev = element(T, OldHold),
    NewHoldT = erlang:max(HoldPrev, PrevCash - Price),
    CashPrev = element(T, OldCash),
    NewCashT = erlang:max(CashPrev, NewHoldT + Price),
    UpdatedHold = setelement(T, CurHold, NewHoldT),
    UpdatedCash = setelement(T, CurCash, NewCashT),
    update_transactions(T+1, K, Price, OldHold, OldCash, UpdatedHold, UpdatedCash).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(k :: integer, prices :: [integer]) :: integer
  def max_profit(k, prices) do
    n = length(prices)

    cond do
      k == 0 or n < 2 ->
        0

      k >= div(n, 2) ->
        Enum.reduce(1..(n - 1), 0, fn i, acc ->
          diff = Enum.at(prices, i) - Enum.at(prices, i - 1)

          if diff > 0 do
            acc + diff
          else
            acc
          end
        end)

      true ->
        # DP with at most k transactions
        initial_dp = List.duplicate(0, n)

        final_dp =
          Enum.reduce(1..k, initial_dp, fn _t, prev_dp ->
            best = -Enum.at(prices, 0)

            {curr_rev, _} =
              Enum.reduce(1..(n - 1), {[], best}, fn i, {acc, best_acc} ->
                price_i = Enum.at(prices, i)
                prev_i = Enum.at(prev_dp, i)

                dp_prev_day =
                  case acc do
                    [] -> 0
                    [last | _] -> last
                  end

                cand1 = dp_prev_day
                cand2 = price_i + best_acc
                curr_i = if cand1 > cand2, do: cand1, else: cand2
                new_best = max(best_acc, prev_i - price_i)

                {[curr_i | acc], new_best}
              end)

            [0 | Enum.reverse(curr_rev)]
          end)

        List.last(final_dp)
    end
  end
end
```
