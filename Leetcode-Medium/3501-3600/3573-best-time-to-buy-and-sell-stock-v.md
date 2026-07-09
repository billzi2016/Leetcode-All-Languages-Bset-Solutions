# 3573. Best Time to Buy and Sell Stock V

## Cpp

```cpp
class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        const long long NEG_INF = -(1LL<<60);
        vector<long long> neutral(k+1, NEG_INF), holdLong(k+1, NEG_INF), holdShort(k+1, NEG_INF);
        neutral[0] = 0;
        for (int price : prices) {
            vector<long long> nNeutral = neutral;
            vector<long long> nHoldLong = holdLong;
            vector<long long> nHoldShort = holdShort;
            for (int t = 0; t <= k; ++t) {
                if (neutral[t] != NEG_INF) {
                    // start a long transaction (buy)
                    nHoldLong[t] = max(nHoldLong[t], neutral[t] - price);
                    // start a short transaction (sell)
                    nHoldShort[t] = max(nHoldShort[t], neutral[t] + price);
                }
                if (holdLong[t] != NEG_INF && t + 1 <= k) {
                    // close long transaction (sell)
                    nNeutral[t+1] = max(nNeutral[t+1], holdLong[t] + price);
                }
                if (holdShort[t] != NEG_INF && t + 1 <= k) {
                    // close short transaction (buy back)
                    nNeutral[t+1] = max(nNeutral[t+1], holdShort[t] - price);
                }
            }
            neutral.swap(nNeutral);
            holdLong.swap(nHoldLong);
            holdShort.swap(nHoldShort);
        }
        long long ans = 0;
        for (int t = 0; t <= k; ++t) {
            ans = max(ans, neutral[t]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumProfit(int[] prices, int k) {
        int n = prices.length;
        // dp[t][state]: 0 - no open transaction, 1 - holding long (bought), 2 - holding short (sold)
        long NEG = Long.MIN_VALUE / 4;
        long[][] dp = new long[k + 1][3];
        for (int t = 0; t <= k; t++) {
            dp[t][0] = NEG;
            dp[t][1] = NEG;
            dp[t][2] = NEG;
        }
        dp[0][0] = 0L;

        for (int priceInt : prices) {
            long price = priceInt;
            long[][] ndp = new long[k + 1][3];
            for (int t = 0; t <= k; t++) {
                ndp[t][0] = dp[t][0];
                ndp[t][1] = dp[t][1];
                ndp[t][2] = dp[t][2];
            }

            for (int t = 0; t <= k; t++) {
                long noTrans = dp[t][0];
                if (noTrans != NEG) {
                    // start a long position (buy)
                    ndp[t][1] = Math.max(ndp[t][1], noTrans - price);
                    // start a short position (sell)
                    ndp[t][2] = Math.max(ndp[t][2], noTrans + price);
                }

                long holdLong = dp[t][1];
                if (holdLong != NEG && t + 1 <= k) {
                    // close long by selling
                    ndp[t + 1][0] = Math.max(ndp[t + 1][0], holdLong + price);
                }

                long holdShort = dp[t][2];
                if (holdShort != NEG && t + 1 <= k) {
                    // close short by buying back
                    ndp[t + 1][0] = Math.max(ndp[t + 1][0], holdShort - price);
                }
            }

            dp = ndp;
        }

        long ans = 0L;
        for (int t = 0; t <= k; t++) {
            ans = Math.max(ans, dp[t][0]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        INF_NEG = -10**18

        # dp[c] = max profit with exactly c completed transactions and no open position
        dp = [INF_NEG] * (k + 1)
        dp[0] = 0

        # hold_long[c] = max profit with exactly c completed transactions and holding a long position
        # hold_short[c] = max profit with exactly c completed transactions and holding a short position
        hold_long = [INF_NEG] * (k + 1)
        hold_short = [INF_NEG] * (k + 1)

        for price in prices:
            old_dp = dp[:]
            old_hold_long = hold_long[:]
            old_hold_short = hold_short[:]

            # start new long or short positions (cannot close and open on same day)
            for c in range(k + 1):
                if old_dp[c] != INF_NEG:
                    # buy to open a long position
                    if old_dp[c] - price > hold_long[c]:
                        hold_long[c] = old_dp[c] - price
                    # sell to open a short position
                    if old_dp[c] + price > hold_short[c]:
                        hold_short[c] = old_dp[c] + price

            # close positions, completing a transaction
            for c in range(k):
                # close long -> sell
                if old_hold_long[c] != INF_NEG:
                    profit = old_hold_long[c] + price
                    if profit > dp[c + 1]:
                        dp[c + 1] = profit
                # close short -> buy back
                if old_hold_short[c] != INF_NEG:
                    profit = old_hold_short[c] - price
                    if profit > dp[c + 1]:
                        dp[c + 1] = profit

            # also keep previous states (already in dp, hold_long, hold_short)

        return max(dp)
```

## Python3

```python
class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        prev = [0] * n
        for t in range(1, k + 1):
            cur = [0] * n
            best_long = float('-inf')
            best_short = float('-inf')
            for i in range(n):
                if i >= 1:
                    idx = i - 1
                    prev_profit = prev[idx - 1] if idx - 1 >= 0 else 0
                    # start a new transaction at day idx
                    cand_long = prev_profit - prices[idx]
                    cand_short = prev_profit + prices[idx]
                    if cand_long > best_long:
                        best_long = cand_long
                    if cand_short > best_short:
                        best_short = cand_short
                if i == 0:
                    cur[i] = 0
                else:
                    # end a transaction at day i (sell for long or buy back for short)
                    profit1 = prices[i] + best_long   # long sell
                    profit2 = -prices[i] + best_short  # short close
                    cur[i] = max(cur[i - 1], profit1, profit2)
            prev = cur
        return prev[-1]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

long long maximumProfit(int* prices, int pricesSize, int k) {
    if (pricesSize == 0 || k == 0) return 0;
    const long long NEG = LLONG_MIN / 4;

    long long *noHold   = (long long*)malloc((k + 1) * sizeof(long long));
    long long *longHold = (long long*)malloc((k + 1) * sizeof(long long));
    long long *shortHold= (long long*)malloc((k + 1) * sizeof(long long));

    for (int t = 0; t <= k; ++t) {
        noHold[t] = NEG;
        longHold[t] = NEG;
        shortHold[t] = NEG;
    }
    noHold[0] = 0;

    // Day 0: possible to start a transaction
    long long price0 = prices[0];
    if (k >= 0) {
        if (-price0 > longHold[0]) longHold[0] = -price0;   // buy
        if ( price0 > shortHold[0]) shortHold[0] = price0; // sell short
    }

    for (int i = 1; i < pricesSize; ++i) {
        long long p = prices[i];
        long long *newNo = (long long*)malloc((k + 1) * sizeof(long long));
        long long *newLong = (long long*)malloc((k + 1) * sizeof(long long));
        long long *newShort = (long long*)malloc((k + 1) * sizeof(long long));

        for (int t = 0; t <= k; ++t) {
            newNo[t] = NEG;
            newLong[t] = NEG;
            newShort[t] = NEG;
        }

        for (int t = 0; t <= k; ++t) {
            // stay idle
            if (noHold[t] > newNo[t]) newNo[t] = noHold[t];

            // keep holding positions
            if (longHold[t] > newLong[t]) newLong[t] = longHold[t];
            if (shortHold[t] > newShort[t]) newShort[t] = shortHold[t];

            // start a new long transaction (buy)
            if (noHold[t] - p > newLong[t]) newLong[t] = noHold[t] - p;

            // start a new short transaction (sell)
            if (noHold[t] + p > newShort[t]) newShort[t] = noHold[t] + p;

            // close long transaction -> completed
            if (t + 1 <= k && longHold[t] != NEG) {
                long long val = longHold[t] + p;
                if (val > newNo[t + 1]) newNo[t + 1] = val;
            }

            // close short transaction -> completed
            if (t + 1 <= k && shortHold[t] != NEG) {
                long long val = shortHold[t] - p;
                if (val > newNo[t + 1]) newNo[t + 1] = val;
            }
        }

        free(noHold);
        free(longHold);
        free(shortHold);
        noHold = newNo;
        longHold = newLong;
        shortHold = newShort;
    }

    long long ans = 0;
    for (int t = 0; t <= k; ++t) {
        if (noHold[t] > ans) ans = noHold[t];
    }

    free(noHold);
    free(longHold);
    free(shortHold);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumProfit(int[] prices, int k) {
        int n = prices.Length;
        if (k == 0 || n < 2) return 0L;

        const long NEG = long.MinValue / 4;

        long[] notHold = new long[k + 1];
        long[] longHold = new long[k + 1];
        long[] shortHold = new long[k + 1];

        for (int t = 0; t <= k; ++t) {
            notHold[t] = 0L;
            longHold[t] = NEG;
            shortHold[t] = NEG;
        }

        foreach (int priceInt in prices) {
            long price = priceInt;
            long[] curNot = new long[k + 1];
            long[] curLong = new long[k + 1];
            long[] curShort = new long[k + 1];

            Array.Copy(notHold, curNot, k + 1);
            Array.Copy(longHold, curLong, k + 1);
            Array.Copy(shortHold, curShort, k + 1);

            for (int t = 1; t <= k; ++t) {
                // close a long position
                if (longHold[t] != NEG) {
                    long profit = longHold[t] + price;
                    if (profit > curNot[t]) curNot[t] = profit;
                }
                // close a short position
                if (shortHold[t] != NEG) {
                    long profit = shortHold[t] - price;
                    if (profit > curNot[t]) curNot[t] = profit;
                }
                // open a new long position (start t-th transaction)
                long openLong = notHold[t - 1] - price;
                if (openLong > curLong[t]) curLong[t] = openLong;

                // open a new short position (start t-th transaction)
                long openShort = notHold[t - 1] + price;
                if (openShort > curShort[t]) curShort[t] = openShort;
            }

            notHold = curNot;
            longHold = curLong;
            shortHold = curShort;
        }

        return notHold[k];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @param {number} k
 * @return {number}
 */
var maximumProfit = function(prices, k) {
    const n = prices.length;
    // dpNo[t]: max profit after t completed transactions and not holding any position
    let dpNo = new Array(k + 1).fill(Number.NEGATIVE_INFINITY);
    dpNo[0] = 0;

    // holdLong[t]: max profit after t completed transactions while holding a long (bought) stock
    let holdLong = new Array(k + 1).fill(Number.NEGATIVE_INFINITY);
    // holdShort[t]: max profit after t completed transactions while holding a short (sold) stock
    let holdShort = new Array(k + 1).fill(Number.NEGATIVE_INFINITY);

    for (let price of prices) {
        const nextNo = dpNo.slice();
        const nextLong = holdLong.slice();
        const nextShort = holdShort.slice();

        for (let t = 0; t <= k; ++t) {
            // Close a long transaction
            if (holdLong[t] !== Number.NEGATIVE_INFINITY && t + 1 <= k) {
                const profitCloseLong = holdLong[t] + price;
                if (profitCloseLong > nextNo[t + 1]) nextNo[t + 1] = profitCloseLong;
            }
            // Close a short transaction
            if (holdShort[t] !== Number.NEGATIVE_INFINITY && t + 1 <= k) {
                const profitCloseShort = holdShort[t] - price; // bought back
                if (profitCloseShort > nextNo[t + 1]) nextNo[t + 1] = profitCloseShort;
            }
            // Open a new long transaction
            if (dpNo[t] !== Number.NEGATIVE_INFINITY) {
                const openLong = dpNo[t] - price; // spend cash to buy
                if (openLong > nextLong[t]) nextLong[t] = openLong;
            }
            // Open a new short transaction
            if (dpNo[t] !== Number.NEGATIVE_INFINITY) {
                const openShort = dpNo[t] + price; // receive cash by selling first
                if (openShort > nextShort[t]) nextShort[t] = openShort;
            }
        }

        dpNo = nextNo;
        holdLong = nextLong;
        holdShort = nextShort;
    }

    let ans = 0;
    for (let t = 0; t <= k; ++t) {
        if (dpNo[t] > ans) ans = dpNo[t];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumProfit(prices: number[], k: number): number {
    const n = prices.length;
    if (k === 0 || n === 0) return 0;

    const cash = new Array(k + 1).fill(0);               // profit with t completed transactions, no open position
    const longHold = new Array(k + 1).fill(-Infinity);   // holding a long (bought) position after starting t-th transaction
    const shortHold = new Array(k + 1).fill(-Infinity);  // holding a short (sold) position after starting t-th transaction

    for (const price of prices) {
        const prevCash = cash.slice();
        const prevLong = longHold.slice();
        const prevShort = shortHold.slice();

        for (let t = 1; t <= k; ++t) {
            // start a long transaction (buy)
            const buyVal = prevCash[t - 1] - price;
            if (buyVal > longHold[t]) longHold[t] = buyVal;

            // close a long transaction (sell)
            const sellVal = prevLong[t] + price;
            if (sellVal > cash[t]) cash[t] = sellVal;

            // start a short transaction (sell first)
            const shortStartVal = prevCash[t - 1] + price;
            if (shortStartVal > shortHold[t]) shortHold[t] = shortStartVal;

            // close a short transaction (buy back)
            const shortCloseVal = prevShort[t] - price;
            if (shortCloseVal > cash[t]) cash[t] = shortCloseVal;
        }
    }

    let ans = 0;
    for (let t = 0; t <= k; ++t) {
        if (cash[t] > ans) ans = cash[t];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $k
     * @return Integer
     */
    function maximumProfit($prices, $k) {
        $n = count($prices);
        if ($k == 0 || $n < 2) {
            return 0;
        }

        // dpPrev[i] – max profit using at most (t-1) transactions up to day i
        $dpPrev = array_fill(0, $n, 0);

        for ($t = 1; $t <= $k; $t++) {
            $dpCurr = array_fill(0, $n, 0);
            $bestA = PHP_INT_MIN; // max of dpPrev[m] - price[m]
            $bestB = PHP_INT_MIN; // max of dpPrev[m] + price[m]

            for ($i = 0; $i < $n; $i++) {
                if ($i > 0) {
                    $candidate1 = $bestA + $prices[$i];   // assume prices[i] >= prices[m]
                    $candidate2 = $bestB - $prices[$i];   // assume prices[i] <= prices[m]
                    $dpCurr[$i] = max($dpCurr[$i - 1], $candidate1, $candidate2);
                } else {
                    $dpCurr[$i] = 0;
                }

                // update best values using dpPrev at day i (for future j > i)
                $valA = $dpPrev[$i] - $prices[$i];
                if ($valA > $bestA) {
                    $bestA = $valA;
                }
                $valB = $dpPrev[$i] + $prices[$i];
                if ($valB > $bestB) {
                    $bestB = $valB;
                }
            }

            $dpPrev = $dpCurr;
        }

        return $dpPrev[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maximumProfit(_ prices: [Int], _ k: Int) -> Int {
        let n = prices.count
        if n == 0 || k == 0 { return 0 }
        let NEG_INF = Int.min / 4
        
        var noPrev = Array(repeating: NEG_INF, count: k + 1)
        var longPrev = Array(repeating: NEG_INF, count: k + 1)
        var shortPrev = Array(repeating: NEG_INF, count: k + 1)
        noPrev[0] = 0
        
        for price in prices {
            var noCur = noPrev
            var longCur = longPrev
            var shortCur = shortPrev
            
            // start new transactions from a completed state
            for t in 0...k where noPrev[t] != NEG_INF {
                let startLong = noPrev[t] - price
                if startLong > longCur[t] { longCur[t] = startLong }
                
                let startShort = noPrev[t] + price
                if startShort > shortCur[t] { shortCur[t] = startShort }
            }
            
            // close running transactions
            for t in 0...k {
                if t < k && longPrev[t] != NEG_INF {
                    let profit = longPrev[t] + price
                    if profit > noCur[t + 1] { noCur[t + 1] = profit }
                }
                if t < k && shortPrev[t] != NEG_INF {
                    let profit = shortPrev[t] - price
                    if profit > noCur[t + 1] { noCur[t + 1] = profit }
                }
            }
            
            noPrev = noCur
            longPrev = longCur
            shortPrev = shortCur
        }
        
        var answer = 0
        for t in 0...k {
            if noPrev[t] > answer { answer = noPrev[t] }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumProfit(prices: IntArray, k: Int): Long {
        val INF_NEG = Long.MIN_VALUE / 4
        var noPos = LongArray(k + 1) { INF_NEG }
        var holdLong = LongArray(k + 1) { INF_NEG }
        var holdShort = LongArray(k + 1) { INF_NEG }

        noPos[0] = 0L

        for (priceInt in prices) {
            val price = priceInt.toLong()
            val newNoPos = noPos.clone()
            val newHoldLong = holdLong.clone()
            val newHoldShort = holdShort.clone()

            for (t in 0..k) {
                // start a long transaction (buy)
                if (noPos[t] != INF_NEG) {
                    val candBuy = noPos[t] - price
                    if (candBuy > newHoldLong[t]) newHoldLong[t] = candBuy

                    // start a short transaction (sell)
                    val candShort = noPos[t] + price
                    if (candShort > newHoldShort[t]) newHoldShort[t] = candShort
                }

                // close a long transaction (sell) -> completed transaction count t+1
                if (t < k && holdLong[t] != INF_NEG) {
                    val candSell = holdLong[t] + price
                    if (candSell > newNoPos[t + 1]) newNoPos[t + 1] = candSell
                }

                // close a short transaction (buy back) -> completed transaction count t+1
                if (t < k && holdShort[t] != INF_NEG) {
                    val candBuyBack = holdShort[t] - price
                    if (candBuyBack > newNoPos[t + 1]) newNoPos[t + 1] = candBuyBack
                }
            }

            noPos = newNoPos
            holdLong = newHoldLong
            holdShort = newHoldShort
        }

        var ans = 0L
        for (t in 0..k) {
            if (noPos[t] > ans) ans = noPos[t]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumProfit(List<int> prices, int k) {
    const int NEG_INF = -1 << 60;
    List<int> notHold = List.filled(k + 1, NEG_INF);
    List<int> longHold = List.filled(k + 1, NEG_INF);
    List<int> shortHold = List.filled(k + 1, NEG_INF);
    notHold[0] = 0;

    for (int price in prices) {
      List<int> newNot = List.filled(k + 1, NEG_INF);
      List<int> newLong = List.filled(k + 1, NEG_INF);
      List<int> newShort = List.filled(k + 1, NEG_INF);

      for (int t = 0; t <= k; ++t) {
        // Not holding state
        int bestNot = notHold[t];
        if (t > 0) {
          if (longHold[t - 1] != NEG_INF) {
            bestNot = bestNot > longHold[t - 1] + price ? bestNot : longHold[t - 1] + price;
          }
          if (shortHold[t - 1] != NEG_INF) {
            bestNot = bestNot > shortHold[t - 1] - price ? bestNot : shortHold[t - 1] - price;
          }
        }
        newNot[t] = bestNot;

        // Holding long (bought)
        int bestLong = longHold[t];
        if (notHold[t] != NEG_INF) {
          bestLong = bestLong > notHold[t] - price ? bestLong : notHold[t] - price;
        }
        newLong[t] = bestLong;

        // Holding short (sold)
        int bestShort = shortHold[t];
        if (notHold[t] != NEG_INF) {
          bestShort = bestShort > notHold[t] + price ? bestShort : notHold[t] + price;
        }
        newShort[t] = bestShort;
      }

      notHold = newNot;
      longHold = newLong;
      shortHold = newShort;
    }

    int answer = NEG_INF;
    for (int val in notHold) {
      if (val > answer) answer = val;
    }
    return answer;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func maximumProfit(prices []int, k int) int64 {
	const negInf int64 = math.MinInt64 / 4
	n := len(prices)
	// dp[t][state] where state:0 none,1 long,2 short
	cur := make([][3]int64, k+1)
	for t := 0; t <= k; t++ {
		for s := 0; s < 3; s++ {
			cur[t][s] = negInf
		}
	}
	cur[0][0] = 0

	for _, price := range prices {
		p := int64(price)
		nxt := make([][3]int64, k+1)
		for t := 0; t <= k; t++ {
			for s := 0; s < 3; s++ {
				nxt[t][s] = negInf
			}
		}
		for t := 0; t <= k; t++ {
			// state 0: no open transaction
			if cur[t][0] != negInf {
				// stay idle
				if cur[t][0] > nxt[t][0] {
					nxt[t][0] = cur[t][0]
				}
				// start long (buy)
				val := cur[t][0] - p
				if val > nxt[t][1] {
					nxt[t][1] = val
				}
				// start short (sell)
				val = cur[t][0] + p
				if val > nxt[t][2] {
					nxt[t][2] = val
				}
			}
			// state 1: holding long
			if cur[t][1] != negInf {
				// continue holding
				if cur[t][1] > nxt[t][1] {
					nxt[t][1] = cur[t][1]
				}
				// close by selling
				if t+1 <= k {
					val := cur[t][1] + p
					if val > nxt[t+1][0] {
						nxt[t+1][0] = val
					}
				}
			}
			// state 2: holding short
			if cur[t][2] != negInf {
				// continue holding
				if cur[t][2] > nxt[t][2] {
					nxt[t][2] = cur[t][2]
				}
				// close by buying
				if t+1 <= k {
					val := cur[t][2] - p
					if val > nxt[t+1][0] {
						nxt[t+1][0] = val
					}
				}
			}
		}
		cur = nxt
	}

	var ans int64 = 0
	for t := 0; t <= k; t++ {
		if cur[t][0] > ans {
			ans = cur[t][0]
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_profit(prices, k)
  inf = -(1 << 60)
  not_hold = Array.new(k + 1, inf)
  hold_long = Array.new(k + 1, inf)
  hold_short = Array.new(k + 1, inf)
  not_hold[0] = 0

  prices.each do |price|
    new_not = not_hold.clone
    new_long = hold_long.clone
    new_short = hold_short.clone

    (0..k).each do |t|
      nh = not_hold[t]
      next if nh == inf
      # start a long transaction
      new_long[t] = [new_long[t], nh - price].max
      # start a short transaction
      new_short[t] = [new_short[t], nh + price].max
    end

    (0...k).each do |t|
      hl = hold_long[t]
      hs = hold_short[t]

      if hl != inf
        new_not[t + 1] = [new_not[t + 1], hl + price].max
      end
      if hs != inf
        new_not[t + 1] = [new_not[t + 1], hs - price].max
      end
    end

    not_hold = new_not
    hold_long = new_long
    hold_short = new_short
  end

  not_hold.max
end
```

## Scala

```scala
object Solution {
    def maximumProfit(prices: Array[Int], k: Int): Long = {
        val K = k
        val INF_NEG: Long = Long.MinValue / 4

        var cash = Array.fill(K + 1)(INF_NEG)
        cash(0) = 0L
        var longHold = Array.fill(K + 1)(INF_NEG)
        var shortHold = Array.fill(K + 1)(INF_NEG)

        for (priceInt <- prices) {
            val price = priceInt.toLong
            val prevCash = cash.clone()
            val prevLong = longHold.clone()
            val prevShort = shortHold.clone()

            // start new transactions
            var t = 0
            while (t <= K) {
                if (prevCash(t) != INF_NEG) {
                    val candLong = prevCash(t) - price
                    if (candLong > longHold(t)) longHold(t) = candLong

                    val candShort = prevCash(t) + price
                    if (candShort > shortHold(t)) shortHold(t) = candShort
                }
                t += 1
            }

            // close existing transactions
            t = 0
            while (t < K) {
                if (prevLong(t) != INF_NEG) {
                    val cand = prevLong(t) + price
                    if (cand > cash(t + 1)) cash(t + 1) = cand
                }
                if (prevShort(t) != INF_NEG) {
                    val cand2 = prevShort(t) - price
                    if (cand2 > cash(t + 1)) cash(t + 1) = cand2
                }
                t += 1
            }
        }

        var ans: Long = 0L
        var i = 0
        while (i <= K) {
            if (cash(i) > ans) ans = cash(i)
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_profit(prices: Vec<i32>, k: i32) -> i64 {
        let n = prices.len();
        if n == 0 {
            return 0;
        }
        let k_usize = k as usize;
        const NEG_INF: i64 = i64::MIN / 4;

        // not_holding[t]: max profit with exactly t completed transactions and no open position
        let mut not_holding = vec![NEG_INF; k_usize + 1];
        not_holding[0] = 0;
        // long_hold[t]: max profit with t completed transactions and currently holding a bought stock
        let mut long_hold = vec![NEG_INF; k_usize + 1];
        // short_hold[t]: max profit with t completed transactions and currently holding a sold (short) stock
        let mut short_hold = vec![NEG_INF; k_usize + 1];

        for price_i in prices {
            let p = price_i as i64;
            let prev_not = not_holding.clone();
            let prev_long = long_hold.clone();
            let prev_short = short_hold.clone();

            // Start a new transaction (buy or sell) without increasing completed count
            for t in 0..=k_usize {
                if prev_not[t] != NEG_INF {
                    long_hold[t] = long_hold[t].max(prev_not[t] - p);   // buy -> long hold
                    short_hold[t] = short_hold[t].max(prev_not[t] + p); // sell -> short hold
                }
            }

            // Close an existing transaction, increasing completed count by 1
            for t in 0..k_usize {
                if prev_long[t] != NEG_INF {
                    not_holding[t + 1] = not_holding[t + 1].max(prev_long[t] + p); // sell to close long
                }
                if prev_short[t] != NEG_INF {
                    not_holding[t + 1] = not_holding[t + 1].max(prev_short[t] - p); // buy to close short
                }
            }
        }

        *not_holding.iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (maximum-profit prices k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length prices))
         (prices-v (list->vector prices)))
    (if (>= k (quotient n 2))
        ;; Unlimited transactions case
        (let loop ((i 1) (total 0))
          (if (>= i n)
              total
              (let ((diff (- (vector-ref prices-v i)
                            (vector-ref prices-v (- i 1)))))
                (loop (+ i 1)
                      (+ total (if (> diff 0) diff 0))))))
        ;; DP for at most k transactions
        (let loop-transactions ((t 1) (dpPrev (make-vector n 0)))
          (if (> t k)
              (vector-ref dpPrev (- n 1))
              (let* ((best-init (- (vector-ref dpPrev 0)
                                   (vector-ref prices-v 0)))
                     (dpCurr (make-vector n 0)))
                (vector-set! dpCurr 0 0)
                (let loop-days ((i 1) (best best-init))
                  (if (>= i n)
                      (loop-transactions (+ t 1) dpCurr)
                      (let* ((profitSell (+ (vector-ref prices-v i) best))
                             (prev (vector-ref dpCurr (- i 1)))
                             (newBest (max best
                                           (- (vector-ref dpPrev i)
                                              (vector-ref prices-v i)))))
                        (vector-set! dpCurr i (if (> profitSell prev) profitSell prev))
                        (loop-days (+ i 1) newBest))))))))))
```

## Erlang

```erlang
-spec maximum_profit(Prices :: [integer()], K :: integer()) -> integer().
maximum_profit(Prices, K) ->
    NegInf = -1000000000000000,
    InitBuy = lists:duplicate(K + 1, NegInf),
    InitSell = [0] ++ lists:duplicate(K, NegInf),
    {_, FinalSell} = lists:foldl(
        fun(P, {Buy, Sell}) -> process_price(P, Buy, Sell) end,
        {InitBuy, InitSell},
        Prices
    ),
    lists:max(FinalSell).

process_price(Price, BuyList, SellList) ->
    [B0 | RestBuy] = BuyList,
    [S0 | RestSell] = SellList,
    {NewTailBuy, NewTailSell} = process_t(
        Price,
        RestBuy,
        RestSell,
        S0,
        [],
        []
    ),
    {[B0 | NewTailBuy], [S0 | NewTailSell]}.

process_t(_Price, [], [], _PrevSellOld, AccBuyRev, AccSellRev) ->
    {lists:reverse(AccBuyRev), lists:reverse(AccSellRev)};
process_t(Price, [BuyT | RestBuy], [SellT | RestSell], PrevSellOld, AccBuyRev, AccSellRev) ->
    NewBuy = erlang:max(BuyT, PrevSellOld - Price),
    NewSell = erlang:max(SellT, NewBuy + Price),
    process_t(
        Price,
        RestBuy,
        RestSell,
        SellT,
        [NewBuy | AccBuyRev],
        [NewSell | AccSellRev]
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_profit(prices :: [integer], k :: integer) :: integer
  def maximum_profit(prices, k) do
    neg_inf = -1_000_000_000_000_000

    dp0 = List.replace_at(List.duplicate(neg_inf, k + 1), 0, 0)
    dp1 = List.duplicate(neg_inf, k + 1)
    dp2 = List.duplicate(neg_inf, k + 1)

    {dp0_final, _dp1, _dp2} =
      Enum.reduce(prices, {dp0, dp1, dp2}, fn price, {dp0, dp1, dp2} ->
        new_dp0 =
          Enum.map(0..k, fn t ->
            base = Enum.at(dp0, t)

            cand =
              if t > 0 do
                close_long = Enum.at(dp1, t - 1) + price
                close_short = Enum.at(dp2, t - 1) - price
                max(close_long, close_short)
              else
                neg_inf
              end

            max(base, cand)
          end)

        new_dp1 =
          Enum.map(0..k, fn t ->
            base = Enum.at(dp1, t)
            open_long = Enum.at(dp0, t) - price
            max(base, open_long)
          end)

        new_dp2 =
          Enum.map(0..k, fn t ->
            base = Enum.at(dp2, t)
            open_short = Enum.at(dp0, t) + price
            max(base, open_short)
          end)

        {new_dp0, new_dp1, new_dp2}
      end)

    Enum.max(dp0_final)
  end
end
```
