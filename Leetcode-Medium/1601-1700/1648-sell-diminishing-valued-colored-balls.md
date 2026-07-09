# 1648. Sell Diminishing-Valued Colored Balls

## Cpp

```cpp
class Solution {
public:
    int maxProfit(std::vector<int>& inventory, int orders) {
        const long long MOD = 1000000007LL;
        long long nOrders = orders;
        long long maxInv = 0;
        for (int v : inventory) if (v > maxInv) maxInv = v;
        
        // binary search for threshold k
        long long low = 0, high = maxInv;
        while (low < high) {
            long long mid = (low + high + 1) / 2; // try higher threshold
            __int128 cnt = 0;
            for (int v : inventory) {
                if (v > mid) cnt += (long long)v - mid;
                if (cnt > nOrders) break;
            }
            if (cnt <= nOrders) low = mid;
            else high = mid - 1;
        }
        long long k = low;
        
        // compute profit
        long long totalSold = 0;
        long long ans = 0;
        for (int v : inventory) {
            if (v > k) {
                long long cnt = (long long)v - k;          // number of balls sold from this color
                long long highVal = v;
                long long lowVal = k + 1;
                long long sum = (highVal + lowVal) * cnt / 2; // arithmetic series sum
                ans = (ans + sum % MOD) % MOD;
                totalSold += cnt;
            }
        }
        long long remaining = nOrders - totalSold; // balls to take at price k
        if (remaining > 0) {
            ans = (ans + (remaining % MOD) * (k % MOD)) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private static final long INV2 = 500000004L; // modular inverse of 2 modulo MOD

    public int maxProfit(int[] inventory, int orders) {
        int n = inventory.length;
        long[] inv = new long[n];
        long maxInv = 0;
        for (int i = 0; i < n; i++) {
            inv[i] = inventory[i];
            if (inv[i] > maxInv) maxInv = inv[i];
        }

        long low = 0, high = maxInv;
        while (low < high) {
            long mid = (low + high) / 2;
            long cnt = 0;
            for (long v : inv) {
                if (v > mid) {
                    cnt += v - mid;
                    if (cnt >= orders) break;
                }
            }
            if (cnt >= orders) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        long threshold = low; // price floor
        long profit = 0;
        long remaining = orders;

        for (long v : inv) {
            if (v > threshold) {
                long num = v - threshold; // balls sold completely from this color
                long sum = ((v % MOD + (threshold + 1) % MOD) % MOD) * (num % MOD) % MOD;
                sum = sum * INV2 % MOD; // divide by 2 modulo MOD
                profit = (profit + sum) % MOD;
                remaining -= num;
            }
        }

        if (remaining > 0) {
            profit = (profit + (remaining % MOD) * (threshold % MOD)) % MOD;
        }

        return (int) profit;
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10**9 + 7
        lo, hi = 0, max(inventory)
        # binary search for the highest price k such that we can sell at least 'orders' balls with value > k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            cnt = 0
            for inv in inventory:
                if inv > mid:
                    cnt += inv - mid
                if cnt >= orders:   # early stop to avoid overflow
                    break
            if cnt >= orders:
                lo = mid
            else:
                hi = mid - 1
        k = lo

        total_sold = 0
        profit = 0
        for inv in inventory:
            if inv > k:
                cnt = inv - k
                total_sold += cnt
                # sum of arithmetic series from (k+1) to inv inclusive
                profit += (inv + (k + 1)) * cnt // 2

        excess = total_sold - orders
        if excess > 0:
            profit -= excess * (k + 1)

        return profit % MOD
```

## Python3

```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        inv = sorted(inventory, reverse=True)
        inv.append(0)
        profit = 0
        i = 0
        n = len(inv) - 1
        while orders > 0:
            cur = inv[i]
            nxt = inv[i + 1]
            cnt = i + 1          # number of colors with at least 'cur' balls
            diff = cur - nxt
            if diff == 0:
                i += 1
                continue
            total = diff * cnt   # balls we could sell by dropping from cur to nxt
            if orders >= total:
                # sell all these layers
                layer_sum = (cur + nxt + 1) * diff // 2
                profit += layer_sum * cnt
                orders -= total
            else:
                full = orders // cnt          # complete layers we can drop across all cnt colors
                rem = orders % cnt           # remaining balls at the next value
                low = cur - full
                if full > 0:
                    layer_sum = (cur + low + 1) * full // 2
                    profit += layer_sum * cnt
                profit += rem * low
                orders = 0
            i += 1
        return profit % MOD
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (vb > va) - (vb < va);
}

int maxProfit(int* inventory, int inventorySize, int orders) {
    const long long MOD = 1000000007LL;
    qsort(inventory, inventorySize, sizeof(int), cmp_desc);

    long long profit = 0;
    long long remaining = orders;

    for (int i = 0; i < inventorySize && remaining > 0; ++i) {
        long long cur = inventory[i];
        long long next = (i + 1 < inventorySize) ? inventory[i + 1] : 0;
        if (cur == next) continue;

        long long cntColors = i + 1;                 // number of colors at this level or higher
        long long diff = cur - next;                  // levels we can drop
        long long totalBalls = diff * cntColors;      // balls in the whole block

        if (remaining >= totalBalls) {
            // sell all balls down to 'next + 1'
            long long high = cur;
            long long low = next + 1;
            long long sumPerColor = (high + low) * diff / 2;   // arithmetic series sum
            profit = (profit + (sumPerColor % MOD) * (cntColors % MOD)) % MOD;
            remaining -= totalBalls;
        } else {
            // sell partially within this block
            long long fullLevels = remaining / cntColors;
            long long remainder = remaining % cntColors;

            if (fullLevels > 0) {
                long long high = cur;
                long long low = cur - fullLevels + 1;
                long long sumPerColor = (high + low) * fullLevels / 2;
                profit = (profit + (sumPerColor % MOD) * (cntColors % MOD)) % MOD;
            }

            long long val = cur - fullLevels;   // value of the remaining balls
            profit = (profit + (val % MOD) * (remainder % MOD)) % MOD;

            remaining = 0;
        }
    }

    return (int)(profit % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProfit(int[] inventory, int orders) {
        const long MOD = 1000000007L;
        Array.Sort(inventory);
        int n = inventory.Length;
        long maxInv = inventory[n - 1];
        long low = 0, high = maxInv;
        while (low < high) {
            long mid = (low + high) / 2;
            long cnt = 0;
            for (int i = n - 1; i >= 0 && cnt <= orders; i--) {
                if (inventory[i] > mid) {
                    cnt += inventory[i] - mid;
                } else {
                    break;
                }
            }
            if (cnt > orders) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        long k = low; // threshold price
        long profit = 0;
        long sold = 0;
        for (int i = n - 1; i >= 0; i--) {
            int inv = inventory[i];
            if (inv > k) {
                long cnt = inv - k;
                long sum = ((long)inv + (k + 1)) * cnt / 2;
                profit = (profit + sum) % MOD;
                sold += cnt;
            }
        }
        long remaining = orders - sold;
        if (remaining > 0) {
            profit = (profit + (remaining % MOD) * (k % MOD)) % MOD;
        }
        return (int)profit;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} inventory
 * @param {number} orders
 * @return {number}
 */
var maxProfit = function(inventory, orders) {
    const MOD = 1000000007n;
    inventory.sort((a, b) => b - a);
    let n = inventory.length;
    let remaining = BigInt(orders);
    let profit = 0n;

    for (let i = 0; i < n && remaining > 0n; i++) {
        const cur = BigInt(inventory[i]);
        const nextVal = i + 1 < n ? BigInt(inventory[i + 1]) : 0n;
        const cnt = BigInt(i + 1);
        const diff = cur - nextVal; // levels we can drop
        const totalBalls = cnt * diff;

        if (remaining >= totalBalls) {
            // sell all balls down to nextVal
            const sumPerColor = (cur + nextVal + 1n) * diff / 2n;
            profit += cnt * sumPerColor;
            remaining -= totalBalls;
        } else {
            // partial sale within this range
            const fullLayers = remaining / cnt;      // complete levels we can sell
            const remainder = remaining % cnt;       // extra balls at the next level

            if (fullLayers > 0n) {
                const low = cur - fullLayers + 1n;
                const sumPerColor = (cur + low) * fullLayers / 2n;
                profit += cnt * sumPerColor;
            }

            const val = cur - fullLayers; // value for the remaining balls
            profit += remainder * val;

            remaining = 0n; // all orders fulfilled
        }
    }

    return Number(profit % MOD);
};
```

## Typescript

```typescript
function maxProfit(inventory: number[], orders: number): number {
    const MOD = 1000000007n;
    let maxInv = 0;
    for (const v of inventory) if (v > maxInv) maxInv = v;

    const target = BigInt(orders);
    // binary search the minimum price that will be partially sold
    let lo = 1, hi = maxInv + 1; // hi is exclusive
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        let cnt = 0n;
        for (const v of inventory) {
            if (v >= mid) cnt += BigInt(v - mid + 1);
        }
        if (cnt >= target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const price = lo - 1; // smallest value among the sold balls

    let profit = 0n;
    let sold = 0n;
    for (const v of inventory) {
        if (v > price) {
            const high = BigInt(v);
            const low = BigInt(price + 1);
            const cnt = high - low + 1n; // number of balls taken from this color
            profit += (high + low) * cnt / 2n;
            sold += cnt;
        }
    }

    const remaining = target - sold;
    if (remaining > 0n) {
        profit += remaining * BigInt(price);
    }

    return Number(profit % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $inventory
     * @param Integer $orders
     * @return Integer
     */
    function maxProfit($inventory, $orders) {
        $MOD = 1000000007;
        $maxInv = 0;
        foreach ($inventory as $v) {
            if ($v > $maxInv) $maxInv = $v;
        }

        // binary search for smallest price p such that count of balls with value > p is < orders
        $low = 0;
        $high = $maxInv;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $cnt = 0;
            foreach ($inventory as $v) {
                if ($v > $mid) {
                    $cnt += $v - $mid;
                    if ($cnt >= $orders) break; // early stop to avoid overflow
                }
            }
            if ($cnt >= $orders) {
                // still have enough balls above mid, need higher price
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        $p = $low; // threshold price

        $profit = 0;
        $cntAboveP = 0;

        foreach ($inventory as $v) {
            if ($v > $p) {
                $cnt = $v - $p;               // number of balls taken from this color
                $cntAboveP += $cnt;

                // sum of arithmetic series from (p+1) to v
                $sumEndpoints = $v + $p + 1;
                if ($cnt % 2 == 0) {
                    $partial = intdiv($cnt, 2) * $sumEndpoints;
                } else {
                    $partial = $cnt * intdiv($sumEndpoints, 2);
                }
                $profit = ($profit + $partial) % $MOD;
            }
        }

        $remaining = $orders - $cntAboveP; // balls to take at price p
        if ($remaining > 0) {
            $profit = ($profit + ($remaining % $MOD) * ($p % $MOD)) % $MOD;
        }

        return (int)$profit;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ inventory: [Int], _ orders: Int) -> Int {
        let MOD: Int64 = 1_000_000_007
        let INV2: Int64 = 500000004   // modular inverse of 2 modulo MOD
        
        var inv = inventory.map { Int64($0) }
        let totalOrders = Int64(orders)
        
        func countAbove(_ threshold: Int64) -> Int64 {
            var cnt: Int64 = 0
            for v in inv {
                if v > threshold {
                    cnt += v - threshold
                }
            }
            return cnt
        }
        
        var low: Int64 = 0
        var high: Int64 = inv.max()!
        while low < high {
            let mid = (low + high) / 2
            if countAbove(mid) > totalOrders {
                low = mid + 1
            } else {
                high = mid
            }
        }
        let k = low
        
        var result: Int64 = 0
        var sold: Int64 = 0
        
        for v in inv {
            if v > k {
                let cnt = v - k                     // number of balls taken from this color
                let highVal = v
                let lowVal = k + 1
                var sum = (highVal + lowVal) % MOD
                sum = (sum * (cnt % MOD)) % MOD
                sum = (sum * INV2) % MOD            // divide by 2 modulo MOD
                result = (result + sum) % MOD
                sold += cnt
            }
        }
        
        let remaining = totalOrders - sold
        if remaining > 0 {
            let add = (remaining % MOD) * (k % MOD) % MOD
            result = (result + add) % MOD
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(inventory: IntArray, orders: Int): Int {
        val MOD = 1_000_000_007L
        var maxVal = 0L
        for (v in inventory) if (v > maxVal) maxVal = v.toLong()
        var left = 0L
        var right = maxVal
        while (left < right) {
            val mid = (left + right) / 2
            var cnt = 0L
            for (v in inventory) {
                if (v > mid) {
                    cnt += v - mid
                    if (cnt > orders) break
                }
            }
            if (cnt <= orders) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        val k = left
        var profit = 0L
        var sold = 0L
        for (v in inventory) {
            if (v > k) {
                val n = v - k // number of balls taken from this color above k
                val sum = ((v.toLong() + (k + 1)) * n / 2)
                profit = (profit + sum) % MOD
                sold += n
            }
        }
        var remaining = orders.toLong() - sold
        if (remaining > 0) {
            profit = (profit + (remaining % MOD) * (k % MOD)) % MOD
        }
        return profit.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maxProfit(List<int> inventory, int orders) {
    inventory.sort((a, b) => b - a);
    inventory.add(0); // sentinel
    int n = inventory.length;
    int i = 0;
    int profit = 0;

    while (orders > 0 && i < n - 1) {
      int high = inventory[i];
      int low = inventory[i + 1];
      int cnt = i + 1; // number of colors at this level
      int diff = high - low;
      if (diff == 0) {
        i++;
        continue;
      }

      int totalBalls = diff * cnt;
      if (orders >= totalBalls) {
        // sell all balls down to 'low'
        int sumSeries = ((high + low + 1) * diff ~/ 2);
        profit = (profit +
                ((sumSeries % _mod) * (cnt % _mod)) % _mod) %
            _mod;
        orders -= totalBalls;
      } else {
        // sell partially
        int fullLevels = orders ~/ cnt;
        int remainder = orders % cnt;

        if (fullLevels > 0) {
          int newVal = high - fullLevels;
          int sumSeries = ((high + newVal + 1) * fullLevels ~/ 2);
          profit = (profit +
                  ((sumSeries % _mod) * (cnt % _mod)) % _mod) %
              _mod;
          // sell remainder at value newVal
          profit = (profit + (remainder % _mod) * (newVal % _mod)) % _mod;
        } else {
          // no full level, only remainder balls at current high value
          profit = (profit + (remainder % _mod) * (high % _mod)) % _mod;
        }
        orders = 0; // all orders fulfilled
      }
      i++;
    }

    return profit % _mod;
  }
}
```

## Golang

```go
package main

import "sort"

func maxProfit(inventory []int, orders int) int {
	const MOD int64 = 1_000_000_007
	sort.Slice(inventory, func(i, j int) bool { return inventory[i] > inventory[j] })
	n := len(inventory)
	inventory = append(inventory, 0)

	var profit int64
	remaining := int64(orders)

	for i := 0; i < n && remaining > 0; i++ {
		cur := int64(inventory[i])
		next := int64(inventory[i+1])
		cnt := int64(i + 1)
		diff := cur - next
		totalBalls := diff * cnt

		if remaining >= totalBalls {
			sumExact := (cur + next + 1) * diff / 2
			profit = (profit + (sumExact%MOD)*(cnt%MOD)) % MOD
			remaining -= totalBalls
		} else {
			q := remaining / cnt
			r := remaining % cnt

			if q > 0 {
				low := cur - q + 1
				sumExact := (cur + low) * q / 2
				profit = (profit + (sumExact%MOD)*(cnt%MOD)) % MOD
				cur -= q
			}
			if r > 0 {
				profit = (profit + (cur%MOD)*(r%MOD)) % MOD
			}
			remaining = 0
		}
	}

	return int(profit)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def max_profit(inventory, orders)
  inv = inventory.sort.reverse
  inv << 0
  profit = 0
  i = 0
  while orders > 0
    cur = inv[i]
    nxt = inv[i + 1]
    cnt = i + 1
    if cur == nxt
      i += 1
      next
    end
    diff = cur - nxt
    total = cnt * diff
    if orders >= total
      # sell all balls down to nxt
      sum_range = (cur + nxt + 1) * diff / 2
      profit = (profit + (cnt % MOD) * (sum_range % MOD)) % MOD
      orders -= total
      i += 1
    else
      q = orders / cnt
      r = orders % cnt
      low = cur - q
      sum_full = (cur + low + 1) * q / 2
      profit = (profit + (cnt % MOD) * (sum_full % MOD)) % MOD
      profit = (profit + r * low) % MOD
      orders = 0
    end
  end
  profit % MOD
end
```

## Scala

```scala
object Solution {
    def maxProfit(inventory: Array[Int], orders: Int): Int = {
        val MOD = 1000000007L
        val inv = inventory.map(_.toLong).sorted(Ordering.Long.reverse)
        var low = 0L
        var high = inv.head

        // count of balls with value > x
        def countAbove(x: Long): Long = {
            var sum = 0L
            var i = 0
            while (i < inv.length && inv(i) > x) {
                sum += inv(i) - x
                i += 1
            }
            sum
        }

        // binary search for largest threshold such that countAbove(threshold) <= orders
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (countAbove(mid) <= orders) low = mid else high = mid - 1
        }
        val threshold = low

        var total = 0L
        var sold = 0L
        var i = 0
        while (i < inv.length && inv(i) > threshold) {
            val v = inv(i)
            val n = v - threshold // number of balls taken from this color
            // sum of arithmetic series: v + (v-1) + ... + (threshold+1)
            val sum = ((v + (threshold + 1)) * n / 2) % MOD
            total = (total + sum) % MOD
            sold += n
            i += 1
        }

        var remaining = orders.toLong - sold
        if (remaining > 0) {
            total = (total + (remaining % MOD) * (threshold % MOD)) % MOD
        }
        ((total % MOD) + MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(inventory: Vec<i32>, orders: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut inv: Vec<i64> = inventory.iter().map(|&x| x as i64).collect();
        inv.sort_unstable_by(|a, b| b.cmp(a)); // descending

        let mut low: i64 = 0;
        let mut high: i64 = *inv.iter().max().unwrap();

        while low < high {
            let mid = (low + high + 1) / 2;
            let mut cnt: i128 = 0;
            for &v in &inv {
                if v > mid {
                    cnt += (v - mid) as i128;
                } else {
                    break;
                }
            }
            if cnt >= orders as i128 {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        let threshold = low;
        let mut total: i64 = 0;
        let mut sold: i64 = 0;

        for &v in &inv {
            if v > threshold {
                let cnt = v - threshold; // balls taken from this color
                let first = v;
                let last = threshold + 1;
                let sum_i128 = ((first + last) as i128 * cnt as i128) / 2;
                total = (total + (sum_i128 % MOD as i128) as i64) % MOD;
                sold += cnt;
            } else {
                break;
            }
        }

        let remaining = orders as i64 - sold;
        if remaining > 0 {
            total = (total + (remaining % MOD) * (threshold % MOD) % MOD) % MOD;
        }

        total as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (max-profit inventory orders)
  (let* ((sorted (sort inventory >))
         (vec (list->vector (append sorted (list 0)))))
    (let loop ((i 0) (orders orders) (profit 0))
      (if (= orders 0)
          (modulo profit MOD)
          (let* ((cur (vector-ref vec i))
                 (next (vector-ref vec (+ i 1)))
                 (diff (- cur next))
                 (cnt (* diff (+ i 1))))
            (if (<= orders cnt)
                (let* ((full-levels (quotient orders (+ i 1)))
                       (rem (remainder orders (+ i 1)))
                       (low-price (- cur full-levels))
                       (sum-per-color
                         (if (= full-levels 0)
                             0
                             (quotient (* (+ cur (+ low-price 1)) full-levels) 2)))
                       (add (+ (* sum-per-color (+ i 1))
                               (* rem low-price))))
                  (modulo (+ profit add) MOD))
                (let* ((total-terms diff)
                       (sum-per-color
                         (quotient (* (+ cur (+ next 1)) total-terms) 2))
                       (add (* sum-per-color (+ i 1))))
                  (loop (+ i 1) (- orders cnt) (+ profit add)))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_profit/2]).

-define(MOD, 1000000007).

-spec max_profit(Inventory :: [integer()], Orders :: integer()) -> integer().
max_profit(Inventory, Orders) ->
    Max = lists:max(Inventory),
    Threshold = find_threshold(Inventory, Orders, 1, Max, 0),
    {TotalSold, Sum} = compute_sum(Inventory, Threshold),
    Remaining = Orders - TotalSold,
    Result = (Sum + (Remaining * Threshold) rem ?MOD) rem ?MOD,
    Result.

find_threshold(_Inv, _Orders, Low, High, Best) when Low > High ->
    Best;
find_threshold(Inv, Orders, Low, High, Best) ->
    Mid = (Low + High) div 2,
    Cnt = count_ge(Inv, Mid),
    if
        Cnt >= Orders ->
            find_threshold(Inv, Orders, Mid + 1, High, Mid);
        true ->
            find_threshold(Inv, Orders, Low, Mid - 1, Best)
    end.

count_ge(Inv, P) ->
    lists:foldl(fun(I, Acc) ->
        if I >= P -> Acc + (I - P + 1);
           true   -> Acc
        end
    end, 0, Inv).

compute_sum(Inv, Threshold) ->
    lists:foldl(fun(I, {CntAcc, SumAcc}) ->
        if I > Threshold ->
                Num = I - Threshold,
                NewCnt = CntAcc + Num,
                SeriesSum = ((I + (Threshold + 1)) * Num) div 2,
                NewSum = (SumAcc + SeriesSum) rem ?MOD,
                {NewCnt, NewSum};
           true ->
                {CntAcc, SumAcc}
        end
    end, {0, 0}, Inv).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec max_profit(inventory :: [integer], orders :: integer) :: integer
  def max_profit(inventory, orders) do
    mod = 1_000_000_007
    sorted = Enum.sort(inventory, &>=/2)
    max_val = List.first(sorted)

    k = find_k(0, max_val, sorted, orders)

    {profit, sold} =
      Enum.reduce(sorted, {0, 0}, fn v, {prof, sld} ->
        if v > k do
          cnt = v - k
          sum = ((v + (k + 1)) * cnt) div 2
          {(prof + sum) |> rem(mod), sld + cnt}
        else
          {prof, sld}
        end
      end)

    remaining = orders - sold
    profit = (profit + rem(remaining * k, mod)) |> rem(mod)
    profit
  end

  defp find_k(low, high, inv, orders) when low < high do
    mid = div(low + high + 1, 2)

    cnt =
      Enum.reduce(inv, 0, fn v, acc ->
        if v > mid, do: acc + (v - mid), else: acc
      end)

    if cnt >= orders do
      find_k(mid, high, inv, orders)
    else
      find_k(low, mid - 1, inv, orders)
    end
  end

  defp find_k(low, _high, _inv, _orders), do: low
end
```
