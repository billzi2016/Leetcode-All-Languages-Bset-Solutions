# 2830. Maximize the Profit as the Salesman

## Cpp

```cpp
class Solution {
public:
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        vector<vector<pair<int,int>>> endOffers(n);
        for (auto &o : offers) {
            int s = o[0], e = o[1], g = o[2];
            endOffers[e].push_back({s, g});
        }
        vector<long long> dp(n, 0);
        for (int i = 0; i < n; ++i) {
            if (i > 0) dp[i] = dp[i-1];
            for (auto &p : endOffers[i]) {
                int s = p.first;
                long long cand = (s > 0 ? dp[s-1] : 0LL) + p.second;
                if (cand > dp[i]) dp[i] = cand;
            }
        }
        return (int)dp.back();
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximizeTheProfit(int n, List<List<Integer>> offers) {
        @SuppressWarnings("unchecked")
        ArrayList<int[]>[] byEnd = new ArrayList[n];
        for (List<Integer> o : offers) {
            int start = o.get(0);
            int end = o.get(1);
            int gold = o.get(2);
            if (byEnd[end] == null) byEnd[end] = new ArrayList<>();
            byEnd[end].add(new int[]{start, gold});
        }
        long[] dp = new long[n];
        for (int i = 0; i < n; i++) {
            long best = (i == 0) ? 0 : dp[i - 1];
            if (byEnd[i] != null) {
                for (int[] arr : byEnd[i]) {
                    int start = arr[0];
                    int gold = arr[1];
                    long prev = (start > 0) ? dp[start - 1] : 0;
                    best = Math.max(best, prev + gold);
                }
            }
            dp[i] = best;
        }
        return (int) dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maximizeTheProfit(self, n, offers):
        """
        :type n: int
        :type offers: List[List[int]]
        :rtype: int
        """
        # bucket offers by their start position
        starts = [[] for _ in range(n)]
        for s, e, g in offers:
            starts[s].append((e, g))
        
        dp = [0] * (n + 1)  # dp[i]: max gold using houses [0..i-1]
        for i in range(n):
            # carry forward the best profit up to house i
            if dp[i] > dp[i + 1]:
                dp[i + 1] = dp[i]
            cur = dp[i]
            # try all offers that start at i
            for e, g in starts[i]:
                nxt = e + 1
                val = cur + g
                if val > dp[nxt]:
                    dp[nxt] = val
        return dp[n]
```

## Python3

```python
class Solution:
    def maximizeTheProfit(self, n: int, offers):
        from collections import defaultdict
        offers_by_end = [[] for _ in range(n)]
        for s, e, g in offers:
            offers_by_end[e].append((s, g))
        dp = [0] * n
        for i in range(n):
            if i > 0:
                dp[i] = dp[i - 1]
            best = dp[i]
            for s, g in offers_by_end[i]:
                cand = g + (dp[s - 1] if s > 0 else 0)
                if cand > best:
                    best = cand
            dp[i] = best
        return dp[-1]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
    int gold;
} Offer;

static int cmpOffer(const void *a, const void *b) {
    const Offer *oa = (const Offer *)a;
    const Offer *ob = (const Offer *)b;
    if (oa->end != ob->end)
        return oa->end - ob->end;
    return oa->start - ob->start;
}

int maximizeTheProfit(int n, int** offers, int offersSize, int* offersColSize) {
    if (offersSize == 0) return 0;

    Offer *arr = (Offer *)malloc(sizeof(Offer) * offersSize);
    for (int i = 0; i < offersSize; ++i) {
        arr[i].start = offers[i][0];
        arr[i].end   = offers[i][1];
        arr[i].gold  = offers[i][2];
    }

    qsort(arr, offersSize, sizeof(Offer), cmpOffer);

    int *ends = (int *)malloc(sizeof(int) * offersSize);
    long long *dp = (long long *)malloc(sizeof(long long) * offersSize);

    for (int i = 0; i < offersSize; ++i)
        ends[i] = arr[i].end;

    // DP computation
    dp[0] = arr[0].gold;
    for (int i = 1; i < offersSize; ++i) {
        // binary search for last interval with end < current start
        int l = 0, r = i - 1, pos = -1;
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            if (ends[mid] < arr[i].start) {
                pos = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        long long profitWithCurrent = arr[i].gold + (pos == -1 ? 0 : dp[pos]);
        dp[i] = dp[i - 1] > profitWithCurrent ? dp[i - 1] : profitWithCurrent;
    }

    int result = (int)dp[offersSize - 1];

    free(arr);
    free(ends);
    free(dp);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MaximizeTheProfit(int n, IList<IList<int>> offers) {
        var endOffers = new List<int[]>[n];
        foreach (var o in offers) {
            int start = o[0];
            int end = o[1];
            int gold = o[2];
            if (endOffers[end] == null) endOffers[end] = new List<int[]>();
            endOffers[end].Add(new int[] { start, gold });
        }

        var dp = new int[n];
        for (int i = 0; i < n; i++) {
            int best = i > 0 ? dp[i - 1] : 0;
            if (endOffers[i] != null) {
                foreach (var arr in endOffers[i]) {
                    int s = arr[0];
                    int g = arr[1];
                    int cand = (s > 0 ? dp[s - 1] : 0) + g;
                    if (cand > best) best = cand;
                }
            }
            dp[i] = best;
        }

        return n == 0 ? 0 : dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} offers
 * @return {number}
 */
var maximizeTheProfit = function(n, offers) {
    const byStart = Array.from({ length: n }, () => []);
    for (const [s, e, g] of offers) {
        byStart[s].push([e, g]);
    }
    const dp = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        const prev = i === 0 ? 0 : dp[i - 1];
        if (dp[i] < prev) dp[i] = prev;
        const list = byStart[i];
        if (list.length) {
            for (const [e, g] of list) {
                const profit = (i === 0 ? 0 : dp[i - 1]) + g;
                if (dp[e] < profit) dp[e] = profit;
            }
        }
    }
    return dp[n - 1];
};
```

## Typescript

```typescript
function maximizeTheProfit(n: number, offers: number[][]): number {
    const byStart: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [s, e, g] of offers) {
        byStart[s].push([e, g]);
    }
    const dp = new Array<number>(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        if (dp[i + 1] < dp[i]) dp[i + 1] = dp[i];
        for (const [e, g] of byStart[i]) {
            const nxt = e + 1;
            const val = dp[i] + g;
            if (dp[nxt] < val) dp[nxt] = val;
        }
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $offers
     * @return Integer
     */
    function maximizeTheProfit($n, $offers) {
        // Group offers by their start index
        $offersByStart = array_fill(0, $n, []);
        foreach ($offers as $offer) {
            [$l, $r, $g] = $offer;
            $offersByStart[$l][] = [$r, $g];
        }

        // dp[i] = max profit for houses in range [0..i]
        $dp = array_fill(0, $n, 0);

        for ($i = 0; $i < $n; ++$i) {
            if ($i > 0 && $dp[$i] < $dp[$i - 1]) {
                $dp[$i] = $dp[$i - 1];
            }

            foreach ($offersByStart[$i] as $o) {
                [$end, $gold] = $o;
                $prev = ($i > 0) ? $dp[$i - 1] : 0;
                $candidate = $prev + $gold;
                if ($candidate > $dp[$end]) {
                    $dp[$end] = $candidate;
                }
            }
        }

        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maximizeTheProfit(_ n: Int, _ offers: [[Int]]) -> Int {
        var offersByStart = Array(repeating: [(Int, Int)](), count: n)
        for offer in offers {
            let l = offer[0]
            let r = offer[1]
            let g = offer[2]
            offersByStart[l].append((r, g))
        }
        var dp = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            if dp[i] > dp[i + 1] {
                dp[i + 1] = dp[i]
            }
            for (end, gold) in offersByStart[i] {
                let idx = end + 1
                let val = dp[i] + gold
                if val > dp[idx] {
                    dp[idx] = val
                }
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeTheProfit(n: Int, offers: List<List<Int>>): Int {
        val offersByEnd = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (offer in offers) {
            val s = offer[0]
            val e = offer[1]
            val g = offer[2]
            offersByEnd[e].add(Pair(s, g))
        }

        val dp = IntArray(n + 1)
        for (i in 0 until n) {
            if (dp[i] > dp[i + 1]) dp[i + 1] = dp[i]
            for ((s, g) in offersByEnd[i]) {
                val cand = dp[s] + g
                if (cand > dp[i + 1]) dp[i + 1] = cand
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int maximizeTheProfit(int n, List<List<int>> offers) {
    // Group offers by their start index.
    List<List<List<int>>> startOffers = List.generate(n, (_) => []);
    for (var o in offers) {
      startOffers[o[0]].add(o);
    }

    List<int> dp = List.filled(n, 0);

    for (int i = 0; i < n; ++i) {
      if (i > 0 && dp[i] < dp[i - 1]) {
        dp[i] = dp[i - 1];
      }
      for (var o in startOffers[i]) {
        int l = o[0]; // equals i
        int r = o[1];
        int gold = o[2];
        int profit = gold + (l > 0 ? dp[l - 1] : 0);
        if (profit > dp[r]) {
          dp[r] = profit;
        }
      }
    }

    return dp[n - 1];
  }
}
```

## Golang

```go
func maximizeTheProfit(n int, offers [][]int) int {
	type offer struct{ start, gold int }
	ends := make([][]offer, n)
	for _, o := range offers {
		s, e, g := o[0], o[1], o[2]
		ends[e] = append(ends[e], offer{start: s, gold: g})
	}
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		if i > 0 {
			dp[i] = dp[i-1]
		}
		for _, of := range ends[i] {
			profit := of.gold
			if of.start > 0 {
				profit += dp[of.start-1]
			}
			if profit > dp[i] {
				dp[i] = profit
			}
		}
	}
	return dp[n-1]
}
```

## Ruby

```ruby
def maximize_the_profit(n, offers)
  offers_by_end = Array.new(n) { [] }
  offers.each do |s, e, g|
    offers_by_end[e] << [s, g]
  end

  dp = Array.new(n, 0)
  (0...n).each do |i|
    best = i > 0 ? dp[i - 1] : 0
    offers_by_end[i].each do |s, g|
      prev = s > 0 ? dp[s - 1] : 0
      cand = prev + g
      best = cand if cand > best
    end
    dp[i] = best
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def maximizeTheProfit(n: Int, offers: List[List[Int]]): Int = {
        val endOffers = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Int)]())
        for (o <- offers) {
            val s = o(0)
            val e = o(1)
            val g = o(2)
            endOffers(e).append((s, g))
        }
        val dp = new Array[Int](n + 1)
        for (i <- 0 until n) {
            if (dp(i + 1) < dp(i)) dp(i + 1) = dp(i)
            for ((s, g) <- endOffers(i)) {
                val cand = dp(s) + g
                if (cand > dp(i + 1)) dp(i + 1) = cand
            }
        }
        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_the_profit(n: i32, offers: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut by_end: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n_usize];
        for offer in offers.iter() {
            let s = offer[0] as usize;
            let e = offer[1] as usize;
            let g = offer[2];
            by_end[e].push((s, g));
        }
        let mut dp: Vec<i32> = vec![0; n_usize + 1];
        for i in 1..=n_usize {
            dp[i] = dp[i - 1];
            for &(s, g) in &by_end[i - 1] {
                let cand = dp[s] + g;
                if cand > dp[i] {
                    dp[i] = cand;
                }
            }
        }
        dp[n_usize]
    }
}
```

## Racket

```racket
#lang racket
(require racket/match)

(define/contract (maximize-the-profit n offers)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([starts (make-vector n '())])
    ;; group offers by their start index
    (for-each
     (lambda (off)
       (match-define (list s e g) off)
       (vector-set! starts s (cons off (vector-ref starts s))))
     offers)
    (define dp (make-vector (+ n 1) 0))
    (let loop ((i 0))
      (when (< i n)
        ;; ensure dp[i+1] is at least dp[i]
        (when (> (vector-ref dp i) (vector-ref dp (+ i 1)))
          (vector-set! dp (+ i 1) (vector-ref dp i)))
        ;; process all offers that start at i
        (for ([off (in-list (vector-ref starts i))])
          (match-define (list s e g) off)
          (define new-val (+ (vector-ref dp i) g))
          (when (> new-val (vector-ref dp (+ e 1)))
            (vector-set! dp (+ e 1) new-val)))
        (loop (+ i 1))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([maximize_the_profit/2]).

-spec maximize_the_profit(N :: integer(), Offers :: [[integer()]]) -> integer().
maximize_the_profit(N, Offers) ->
    Sorted = lists:sort(fun(A, B) -> element(2, A) < element(2, B) end, Offers),
    DP0 = array:new(N, {default, 0}),
    process_positions(0, N - 1, Sorted, DP0).

process_positions(I, MaxIdx, OffersSorted, DP) when I > MaxIdx ->
    case MaxIdx >= 0 of
        true -> array:get(MaxIdx, DP);
        false -> 0
    end;
process_positions(I, MaxIdx, OffersSorted, DP) ->
    Prev = if I == 0 -> 0; true -> array:get(I - 1, DP) end,
    {OffersHere, Rest} = take_offers_with_end(I, OffersSorted, []),
    BestFromOffers = best_gain(OffersHere, DP),
    Cur = if Prev > BestFromOffers -> Prev; true -> BestFromOffers end,
    NewDP = array:set(I, Cur, DP),
    process_positions(I + 1, MaxIdx, Rest, NewDP).

take_offers_with_end(_End, [], Acc) ->
    {lists:reverse(Acc), []};
take_offers_with_end(End, [Offer | Rest], Acc) ->
    case element(2, Offer) of
        End -> take_offers_with_end(End, Rest, [Offer | Acc]);
        _Other -> {lists:reverse(Acc), [Offer | Rest]}
    end.

best_gain([], _DP) -> 0;
best_gain([Offer | Tail], DP) ->
    Start = element(1, Offer),
    Gold = element(3, Offer),
    PrevGain = if Start == 0 -> 0; true -> array:get(Start - 1, DP) end,
    Total = PrevGain + Gold,
    MaxRest = best_gain(Tail, DP),
    if Total > MaxRest -> Total; true -> MaxRest end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_the_profit(n :: integer, offers :: [[integer]]) :: integer
  def maximize_the_profit(_n, offers) do
    sorted = Enum.sort_by(offers, fn [_, e, _] -> e end)
    m = length(sorted)

    ends_tuple =
      sorted
      |> Enum.map(fn [_, e, _] -> e end)
      |> List.to_tuple()

    dp_arr = :array.new(m + 1, 0)

    {final_dp, _} =
      Enum.with_index(sorted, 1)
      |> Enum.reduce({dp_arr, 0}, fn {[s, _e, g], i}, {arr, _prev} ->
        idx = binary_search(ends_tuple, s)

        profit =
          if idx == -1 do
            g
          else
            prev = :array.get(idx + 1, arr)
            g + prev
          end

        prev_dp = :array.get(i - 1, arr)
        cur_dp = if profit > prev_dp, do: profit, else: prev_dp
        new_arr = :array.set(i, cur_dp, arr)
        {new_arr, cur_dp}
      end)

    :array.get(m, final_dp)
  end

  defp binary_search(ends_tuple, start) do
    size = tuple_size(ends_tuple)
    binary_search(ends_tuple, start, 0, size - 1, -1)
  end

  defp binary_search(_tuple, _start, low, high, ans) when low > high, do: ans

  defp binary_search(tuple, start, low, high, ans) do
    mid = div(low + high, 2)
    val = :erlang.element(mid + 1, tuple)

    if val < start do
      binary_search(tuple, start, mid + 1, high, mid)
    else
      binary_search(tuple, start, low, mid - 1, ans)
    end
  end
end
```
