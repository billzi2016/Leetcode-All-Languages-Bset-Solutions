# 2412. Minimum Money Required Before Transactions

## Cpp

```cpp
class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions) {
        vector<pair<long long,long long>> good;
        vector<pair<long long,long long>> bad;
        for (auto &t : transactions) {
            long long cost = t[0], cash = t[1];
            if (cash >= cost) good.emplace_back(cost, cash);
            else bad.emplace_back(cost, cash);
        }
        long long ans = 0;
        // Good transactions: need at least the maximum cost among them
        for (auto &p : good) {
            ans = max(ans, p.first);
        }
        // Bad transactions: sort by cashback ascending
        sort(bad.begin(), bad.end(), [](const auto& a, const auto& b){
            return a.second < b.second;
        });
        long long lossSum = 0; // total (cost - cash) of processed bad transactions
        for (auto &p : bad) {
            long long cost = p.first;
            long long cash = p.second;
            ans = max(ans, cost + lossSum);
            lossSum += (cost - cash);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumMoney(int[][] transactions) {
        java.util.List<int[]> loss = new java.util.ArrayList<>();
        java.util.List<int[]> gain = new java.util.ArrayList<>();
        for (int[] t : transactions) {
            if (t[1] >= t[0]) {
                gain.add(t);
            } else {
                loss.add(t);
            }
        }
        // Losses: sort by cashback ascending
        loss.sort((a, b) -> Integer.compare(a[1], b[1]));
        // Gains: sort by cost descending
        gain.sort((a, b) -> Integer.compare(b[0], a[0]));

        long ans = 0;
        long cur = 0;

        for (int[] t : loss) {
            long cost = t[0];
            long cash = t[1];
            if (cur < cost) {
                ans += cost - cur;
                cur = cost;
            }
            cur = cur - cost + cash;
        }

        for (int[] t : gain) {
            long cost = t[0];
            long cash = t[1];
            if (cur < cost) {
                ans += cost - cur;
                cur = cost;
            }
            cur = cur - cost + cash;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        groupA = []
        groupB = []
        for cost, cash in transactions:
            if cash >= cost:
                groupA.append(cost)
            else:
                groupB.append((cost, cash))

        max_cost_A = max(groupA) if groupA else 0

        # For losing transactions, process those with smaller cashback first
        groupB.sort(key=lambda x: x[1])

        need = 0
        cur_money = 0
        for cost, cash in groupB:
            need = max(need, cost - cur_money)
            cur_money += cash - cost  # net loss (negative)

        return max(need, max_cost_A)
```

## Python3

```python
class Solution:
    def minimumMoney(self, transactions):
        good = []
        bad = []
        for c, r in transactions:
            if r >= c:
                good.append((c, r))
            else:
                bad.append((c, r))
        # Good: sort by cost descending
        good.sort(key=lambda x: -x[0])
        # Bad: sort by cashback ascending
        bad.sort(key=lambda x: x[1])
        cur = 0
        ans = 0
        for c, r in good + bad:
            if cur < c:
                need = c - cur
                ans += need
                cur = c
            cur = cur - c + r
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int cost;
    int cash;
} Transaction;

static int cmp_pos_desc_cost(const void *a, const void *b) {
    const Transaction *ta = (const Transaction *)a;
    const Transaction *tb = (const Transaction *)b;
    if (ta->cost < tb->cost) return 1;
    if (ta->cost > tb->cost) return -1;
    return 0;
}

static int cmp_neg_asc_cash(const void *a, const void *b) {
    const Transaction *ta = (const Transaction *)a;
    const Transaction *tb = (const Transaction *)b;
    if (ta->cash < tb->cash) return -1;
    if (ta->cash > tb->cash) return 1;
    return 0;
}

static long long compute_need(Transaction *arr, int n) {
    long long cur = 0;   // accumulated net change (cash - cost)
    long long need = 0;  // minimal initial money required so far
    for (int i = 0; i < n; ++i) {
        long long cost = arr[i].cost;
        long long cash = arr[i].cash;
        if (need < cost - cur) need = cost - cur;
        cur += cash - cost;
    }
    return need;
}

long long minimumMoney(int** transactions, int transactionsSize, int* transactionsColSize){
    int posCount = 0, negCount = 0;
    for (int i = 0; i < transactionsSize; ++i) {
        if (transactions[i][1] >= transactions[i][0]) posCount++;
        else negCount++;
    }

    Transaction *pos = (Transaction *)malloc(sizeof(Transaction) * posCount);
    Transaction *neg = (Transaction *)malloc(sizeof(Transaction) * negCount);

    int pi = 0, ni = 0;
    for (int i = 0; i < transactionsSize; ++i) {
        int c = transactions[i][0];
        int r = transactions[i][1];
        if (r >= c) {
            pos[pi].cost = c;
            pos[pi].cash = r;
            pi++;
        } else {
            neg[ni].cost = c;
            neg[ni].cash = r;
            ni++;
        }
    }

    qsort(pos, posCount, sizeof(Transaction), cmp_pos_desc_cost);
    qsort(neg, negCount, sizeof(Transaction), cmp_neg_asc_cash);

    long long needPos = compute_need(pos, posCount);
    long long needNeg = compute_need(neg, negCount);

    free(pos);
    free(neg);

    return needPos > needNeg ? needPos : needNeg;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumMoney(int[][] transactions) {
        var good = new List<(int cost, int cash)>();
        var bad = new List<(int cost, int cash)>();

        foreach (var t in transactions) {
            if (t[1] >= t[0])
                good.Add((t[0], t[1]));
            else
                bad.Add((t[0], t[1]));
        }

        // Bad: cashback < cost, sort by ascending cashback
        bad.Sort((a, b) => a.cash.CompareTo(b.cash));
        // Good: cashback >= cost, sort by descending cost
        good.Sort((a, b) => b.cost.CompareTo(a.cost));

        long cur = 0;
        long ans = 0;

        foreach (var tr in bad) {
            long need = tr.cost - cur;
            if (need > ans) ans = need;
            cur += (long)tr.cash - tr.cost;
        }

        foreach (var tr in good) {
            long need = tr.cost - cur;
            if (need > ans) ans = need;
            cur += (long)tr.cash - tr.cost;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} transactions
 * @return {number}
 */
var minimumMoney = function(transactions) {
    const goodCosts = [];
    const bad = [];
    
    for (const [c, r] of transactions) {
        if (r >= c) {
            goodCosts.push(c);
        } else {
            bad.push([c, r]);
        }
    }
    
    // Good transactions: sort by cost descending (not strictly needed for max)
    goodCosts.sort((a, b) => b - a);
    
    // Bad transactions: sort by cashback ascending
    bad.sort((a, b) => a[1] - b[1]);
    
    let need = 0;      // extra money required to survive bad transactions
    let cur = 0;       // current money during simulation (starting from 0)
    let sumLoss = 0;   // total loss from bad transactions
    
    for (const [c, r] of bad) {
        sumLoss += c - r;
        if (cur < c) {
            need += c - cur;
            cur = c;
        }
        cur = cur - c + r;
    }
    
    let maxCostGood = 0;
    for (const cost of goodCosts) {
        if (cost > maxCostGood) maxCostGood = cost;
    }
    
    return Math.max(need, sumLoss + maxCostGood);
};
```

## Typescript

```typescript
function minimumMoney(transactions: number[][]): number {
    let maxCostGood = 0;
    const bad: [number, number][] = [];
    for (const [cost, cashback] of transactions) {
        if (cashback >= cost) {
            if (cost > maxCostGood) maxCostGood = cost;
        } else {
            bad.push([cost, cashback]);
        }
    }

    // For the worst ordering of losing transactions, sort by increasing cashback
    bad.sort((a, b) => a[1] - b[1]);

    let lossSum = 0;      // total loss accumulated so far
    let needBad = 0;      // minimal initial money needed for bad transactions
    for (const [cost, cashback] of bad) {
        const required = cost + lossSum;
        if (required > needBad) needBad = required;
        lossSum += cost - cashback;
    }

    return Math.max(maxCostGood, needBad);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $transactions
     * @return Integer
     */
    function minimumMoney($transactions) {
        $gainMaxCost = 0;
        $totalLoss = 0;
        $loss = [];

        foreach ($transactions as $t) {
            $c = $t[0];
            $b = $t[1];
            if ($b >= $c) {
                if ($c > $gainMaxCost) {
                    $gainMaxCost = $c;
                }
            } else {
                $loss[] = [$c, $b];
                $totalLoss += ($c - $b);
            }
        }

        // sort loss transactions by cashback ascending
        usort($loss, function($a, $b) {
            if ($a[1] == $b[1]) return 0;
            return ($a[1] < $b[1]) ? -1 : 1;
        });

        $prefix = 0;      // sum of (cost - cashback) for previous loss transactions
        $needLoss = 0;    // minimal money to survive loss transactions in worst order

        foreach ($loss as $t) {
            $c = $t[0];
            $b = $t[1];
            $candidate = $c + $prefix;
            if ($candidate > $needLoss) {
                $needLoss = $candidate;
            }
            $prefix += ($c - $b);
        }

        // After all loss transactions, we must still afford the most expensive gain transaction
        $answer = max($needLoss, $totalLoss + $gainMaxCost);
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumMoney(_ transactions: [[Int]]) -> Int {
        var good = [(cost: Int, cash: Int)]()
        var bad = [(cost: Int, cash: Int)]()
        
        for t in transactions {
            let c = t[0]
            let cb = t[1]
            if cb >= c {
                good.append((c, cb))
            } else {
                bad.append((c, cb))
            }
        }
        
        // Bad transactions: cashback < cost, sort by cashback ascending
        bad.sort { $0.cash < $1.cash }
        // Good transactions: cashback >= cost, sort by cost descending
        good.sort { $0.cost > $1.cost }
        
        var ans = 0
        var cur = 0   // net change after processed transactions
        
        for tr in bad {
            let need = tr.cost - cur
            if need > ans { ans = need }
            cur += tr.cash - tr.cost
        }
        
        for tr in good {
            let need = tr.cost - cur
            if need > ans { ans = need }
            cur += tr.cash - tr.cost
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumMoney(transactions: Array<IntArray>): Long {
        var totalLoss = 0L
        var maxCashbackLoss = 0L
        var maxCostGain = 0L
        for (t in transactions) {
            val cost = t[0].toLong()
            val cash = t[1].toLong()
            if (cost <= cash) {
                if (cost > maxCostGain) maxCostGain = cost
            } else {
                totalLoss += cost - cash
                if (cash > maxCashbackLoss) maxCashbackLoss = cash
            }
        }
        val extra = if (maxCashbackLoss > maxCostGain) maxCashbackLoss else maxCostGain
        return totalLoss + extra
    }
}
```

## Dart

```dart
class Solution {
  int minimumMoney(List<List<int>> transactions) {
    List<List<int>> loss = [];
    int maxGainCost = 0;
    for (var t in transactions) {
      int cost = t[0];
      int cash = t[1];
      if (cash >= cost) {
        if (cost > maxGainCost) maxGainCost = cost;
      } else {
        loss.add(t);
      }
    }

    loss.sort((a, b) => a[1].compareTo(b[1]));

    int need = 0;
    int cur = 0;
    for (var t in loss) {
      int cost = t[0];
      int cash = t[1];
      if (cur < cost) {
        need += cost - cur;
        cur = cost;
      }
      cur = cur - cost + cash;
    }

    return need > maxGainCost ? need : maxGainCost;
  }
}
```

## Golang

```go
package main

import "sort"

type trans struct {
	cost, cash int
}

func minimumMoney(transactions [][]int) int64 {
	var good []trans
	var bad []trans
	for _, p := range transactions {
		if p[1] >= p[0] {
			good = append(good, trans{cost: p[0], cash: p[1]})
		} else {
			bad = append(bad, trans{cost: p[0], cash: p[1]})
		}
	}

	sort.Slice(good, func(i, j int) bool {
		return good[i].cost > good[j].cost // descending cost
	})
	sort.Slice(bad, func(i, j int) bool {
		return bad[i].cash < bad[j].cash // ascending cashback
	})

	calc := func(arr []trans) int64 {
		var need int64 = 0
		var balance int64 = 0
		for _, t := range arr {
			cost := int64(t.cost)
			if cost-balance > need {
				need = cost - balance
			}
			balance += int64(t.cash) - cost
		}
		return need
	}

	needGood := calc(good)
	needBad := calc(bad)

	if needGood > needBad {
		return needGood
	}
	return needBad
}
```

## Ruby

```ruby
def minimum_money(transactions)
  good = []
  bad = []

  transactions.each do |cost, cash|
    if cash >= cost
      good << [cost, cash]
    else
      bad << [cost, cash]
    end
  end

  good.sort_by! { |c, _| -c }          # descending cost
  bad.sort_by! { |_, r| r }            # ascending cashback

  cur = 0
  ans = 0

  good.each do |cost, cash|
    need = cost - cur
    ans = need if need > ans
    cur += cash - cost
  end

  bad.each do |cost, cash|
    need = cost - cur
    ans = need if need > ans
    cur += cash - cost
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumMoney(transactions: Array[Array[Int]]): Long = {
        val pos = scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        val neg = scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        for (t <- transactions) {
            if (t(1) >= t(0)) pos += ((t(0), t(1))) else neg += ((t(0), t(1)))
        }
        val sortedNeg = neg.sortBy(_._2)                 // ascending cashback
        val sortedPos = pos.sortWith((a, b) => a._1 > b._1) // descending cost

        var cur: Long = 0L
        var need: Long = 0L
        for ((c, r) <- sortedNeg ++ sortedPos) {
            val required = c.toLong - cur
            if (required > need) need = required
            cur += (r - c).toLong
        }
        need
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_money(transactions: Vec<Vec<i32>>) -> i64 {
        let mut good: Vec<(i64, i64)> = Vec::new();
        let mut bad: Vec<(i64, i64)> = Vec::new();

        for t in transactions {
            let c = t[0] as i64;
            let r = t[1] as i64;
            if r >= c {
                good.push((c, r));
            } else {
                bad.push((c, r));
            }
        }

        // For transactions that do not lose money, process higher cost first.
        good.sort_by(|a, b| b.0.cmp(&a.0)); // descending cost
        // For losing transactions, process lower cashback first.
        bad.sort_by(|a, b| a.1.cmp(&b.1)); // ascending cashback

        let mut cur: i64 = 0;
        let mut ans: i64 = 0;

        for (c, r) in good.iter().chain(bad.iter()) {
            if cur < *c {
                ans += *c - cur;
                cur = *c;
            }
            cur = cur - c + r;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-money transactions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((groupA '())
         (groupB '()))
    (for ([tr transactions])
      (if (>= (cadr tr) (car tr))
          (set! groupA (cons tr groupA))
          (set! groupB (cons tr groupB))))
    (define sortedA
      (sort groupA (lambda (x y) (> (car x) (car y)))))
    (define sortedB
      (sort groupB (lambda (x y) (< (cadr x) (cadr y)))))
    (define (calc-need lst)
      (let loop ((cur 0) (need 0) (rest lst))
        (if (null? rest)
            need
            (let* ((c (car (car rest)))
                   (cb (cadr (car rest)))
                   (new-need (max need (- c cur)))
                   (new-cur (+ cur (- cb c)))) ; cb - c
              (loop new-cur new-need (cdr rest))))))
    (define needA (calc-need sortedA))
    (define needB (calc-need sortedB))
    (max needA needB)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_money/1]).

-spec minimum_money(Transactions :: [[integer()]]) -> integer().
minimum_money(Transactions) ->
    {Pos, Neg} = lists:foldl(
        fun([C, R], {P, N}) ->
            if
                R >= C -> {[{C, R} | P], N};
                true   -> {P, [{C, R} | N]}
            end
        end,
        {[], []},
        Transactions),

    MaxCostPos = case Pos of
        [] -> 0;
        _  -> lists:max([C || {C, _} <- Pos])
    end,

    SortedNeg = lists:sort(
        fun({C1, R1}, {C2, R2}) ->
            if
                R1 == R2 -> C1 =< C2;
                true     -> R1 < R2
            end
        end,
        Neg),

    {Need, _} = lists:foldl(
        fun({C, R}, {NeedAcc, Cur}) ->
            NewNeed = erlang:max(NeedAcc, C - Cur),
            NewCur  = Cur + (R - C),
            {NewNeed, NewCur}
        end,
        {0, 0},
        SortedNeg),

    erlang:max(MaxCostPos, Need).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_money(transactions :: [[integer]]) :: integer
  def minimum_money(transactions) do
    {bad, good} =
      Enum.reduce(transactions, {[], []}, fn [c, r], {b, g} ->
        if r < c, do: {[ [c, r] | b ], g}, else: {b, [[c, r] | g]}
      end)

    bad_sorted = Enum.sort_by(bad, fn [_c, r] -> r end)
    good_sorted = Enum.sort_by(good, fn [c, _r] -> -c end)

    {need, _cur} =
      Enum.reduce(bad_sorted ++ good_sorted, {0, 0}, fn [c, r], {need, cur} ->
        need = max(need, c - cur)
        cur = cur + (r - c)
        {need, cur}
      end)

    need
  end
end
```
