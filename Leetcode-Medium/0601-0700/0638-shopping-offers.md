# 0638. Shopping Offers

## Cpp

```cpp
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        // Filter out specials that are not cheaper than buying items individually
        vector<vector<int>> filtered;
        for (const auto& offer : special) {
            int total = 0;
            for (int i = 0; i < price.size(); ++i) {
                total += offer[i] * price[i];
            }
            if (total > offer.back()) { // only keep beneficial offers
                filtered.push_back(offer);
            }
        }
        this->price = &price;
        this->special = move(filtered);
        return dfs(needs);
    }

private:
    vector<int>* price;
    vector<vector<int>> special;
    unordered_map<string, int> memo;

    string encode(const vector<int>& v) {
        string s;
        for (int x : v) {
            s.push_back(char('0' + x)); // since needs[i] <= 10, single char is enough
        }
        return s;
    }

    int dfs(vector<int> needs) {
        string key = encode(needs);
        if (memo.count(key)) return memo[key];

        // cost without any special offers
        int minCost = 0;
        for (int i = 0; i < needs.size(); ++i) {
            minCost += (*price)[i] * needs[i];
        }

        // try each special offer
        for (const auto& off : special) {
            bool ok = true;
            vector<int> nxt(needs);
            for (int i = 0; i < needs.size(); ++i) {
                if (nxt[i] < off[i]) { ok = false; break; }
                nxt[i] -= off[i];
            }
            if (!ok) continue;
            int costWithOffer = dfs(nxt) + off.back();
            minCost = min(minCost, costWithOffer);
        }

        memo[key] = minCost;
        return minCost;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        return dfs(price, special, needs, new HashMap<>());
    }

    private int dfs(List<Integer> price, List<List<Integer>> special, List<Integer> needs,
                    Map<List<Integer>, Integer> memo) {
        if (memo.containsKey(needs)) {
            return memo.get(needs);
        }
        int n = price.size();
        // Cost without using any special offer
        int minCost = 0;
        for (int i = 0; i < n; i++) {
            minCost += price.get(i) * needs.get(i);
        }

        // Try each special offer
        for (List<Integer> offer : special) {
            List<Integer> nextNeeds = new ArrayList<>(n);
            boolean valid = true;
            for (int i = 0; i < n; i++) {
                int remain = needs.get(i) - offer.get(i);
                if (remain < 0) {
                    valid = false;
                    break;
                }
                nextNeeds.add(remain);
            }
            if (!valid) continue;
            int offerPrice = offer.get(n); // last element is the price of the offer
            int costWithOffer = dfs(price, special, nextNeeds, memo) + offerPrice;
            minCost = Math.min(minCost, costWithOffer);
        }

        memo.put(needs, minCost);
        return minCost;
    }
}
```

## Python

```python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # Filter out non‑beneficial specials
        useful = []
        n = len(price)
        for sp in special:
            total_price = sum(sp[i] * price[i] for i in range(n))
            if sp[-1] < total_price:
                useful.append(sp)

        memo = {}

        def dfs(cur):
            key = tuple(cur)
            if key in memo:
                return memo[key]

            # Cost without any special offers
            min_cost = sum(cur[i] * price[i] for i in range(n))

            # Try each useful special offer
            for sp in useful:
                nxt = []
                for i in range(n):
                    if sp[i] > cur[i]:
                        break
                    nxt.append(cur[i] - sp[i])
                else:  # all items can be covered by this offer
                    cost = sp[-1] + dfs(nxt)
                    if cost < min_cost:
                        min_cost = cost

            memo[key] = min_cost
            return min_cost

        return dfs(needs)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Keep only specials that are cheaper than buying items individually
        useful_specials = []
        n = len(price)
        for sp in special:
            total_individual = sum(sp[i] * price[i] for i in range(n))
            if sp[-1] < total_individual:
                useful_specials.append(sp)

        @lru_cache(None)
        def dfs(state: tuple) -> int:
            # Cost without using any special offers
            min_cost = sum(state[i] * price[i] for i in range(n))

            # Try each useful special offer
            for sp in useful_specials:
                new_state = []
                for i in range(n):
                    if sp[i] > state[i]:
                        break
                    new_state.append(state[i] - sp[i])
                else:  # all items in the offer are available
                    cost_with_offer = dfs(tuple(new_state)) + sp[-1]
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int n;
static int *gprice;
static int **gspecial;
static int gspecialSize;
static int *gspecialColSize;
static int *memo;
static int pow11[7];

static int encode(const int *needs) {
    int key = 0;
    for (int i = 0; i < n; ++i) {
        key += needs[i] * pow11[i];
    }
    return key;
}

static int dfs(int *needs) {
    int key = encode(needs);
    if (memo[key] != -1) return memo[key];

    int cost = 0;
    for (int i = 0; i < n; ++i) {
        cost += needs[i] * gprice[i];
    }

    for (int s = 0; s < gspecialSize; ++s) {
        const int *offer = gspecial[s];
        int ok = 1;
        for (int i = 0; i < n; ++i) {
            if (needs[i] < offer[i]) { ok = 0; break; }
        }
        if (!ok) continue;

        int newNeeds[6];
        for (int i = 0; i < n; ++i) {
            newNeeds[i] = needs[i] - offer[i];
        }
        int cand = dfs(newNeeds) + offer[n];
        if (cand < cost) cost = cand;
    }

    memo[key] = cost;
    return cost;
}

int shoppingOffers(int* price, int priceSize, int** special, int specialSize,
                   int* specialColSize, int* needs, int needsSize) {
    n = priceSize;
    gprice = price;
    gspecial = special;
    gspecialSize = specialSize;
    gspecialColSize = specialColSize;

    pow11[0] = 1;
    for (int i = 1; i <= n; ++i) pow11[i] = pow11[i - 1] * 11;

    int maxState = pow11[n];
    memo = (int *)malloc(maxState * sizeof(int));
    if (!memo) return -1;
    memset(memo, -1, maxState * sizeof(int));

    int initNeeds[6];
    for (int i = 0; i < n; ++i) initNeeds[i] = needs[i];

    int result = dfs(initNeeds);
    free(memo);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int ShoppingOffers(IList<int> price, IList<IList<int>> special, IList<int> needs) {
        int n = price.Count;
        int[] priceArr = price.ToArray();

        // Filter out non-beneficial specials
        var filteredSpecials = new List<int[]>();
        foreach (var sp in special) {
            int[] arr = sp.ToArray(); // length n+1
            int regularCost = 0;
            for (int i = 0; i < n; i++) {
                regularCost += arr[i] * priceArr[i];
            }
            if (regularCost > arr[n]) { // only keep if it saves money
                filteredSpecials.Add(arr);
            }
        }

        var memo = new Dictionary<string, int>();

        int Dfs(int[] cur) {
            string key = string.Join(",", cur);
            if (memo.TryGetValue(key, out int cached)) return cached;

            // Cost without using any special offer
            int minCost = 0;
            for (int i = 0; i < n; i++) {
                minCost += cur[i] * priceArr[i];
            }

            foreach (var sp in filteredSpecials) {
                bool canUse = true;
                int[] next = new int[n];
                for (int i = 0; i < n; i++) {
                    if (cur[i] < sp[i]) { canUse = false; break; }
                    next[i] = cur[i] - sp[i];
                }
                if (!canUse) continue;

                int costWithOffer = Dfs(next) + sp[n];
                if (costWithOffer < minCost) minCost = costWithOffer;
            }

            memo[key] = minCost;
            return minCost;
        }

        return Dfs(needs.ToArray());
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} price
 * @param {number[][]} special
 * @param {number[]} needs
 * @return {number}
 */
var shoppingOffers = function(price, special, needs) {
    const memo = new Map();
    
    const dfs = (curNeeds) => {
        const key = curNeeds.join(',');
        if (memo.has(key)) return memo.get(key);
        
        // cost without any special offers
        let minCost = 0;
        for (let i = 0; i < price.length; i++) {
            minCost += price[i] * curNeeds[i];
        }
        
        // try each special offer
        for (const offer of special) {
            const nextNeeds = [];
            let valid = true;
            for (let i = 0; i < price.length; i++) {
                if (curNeeds[i] < offer[i]) {
                    valid = false;
                    break;
                }
                nextNeeds.push(curNeeds[i] - offer[i]);
            }
            if (!valid) continue;
            const costWithOffer = offer[price.length] + dfs(nextNeeds);
            if (costWithOffer < minCost) minCost = costWithOffer;
        }
        
        memo.set(key, minCost);
        return minCost;
    };
    
    return dfs(needs);
};
```

## Typescript

```typescript
function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    const n = price.length;
    const memo = new Map<string, number>();

    // Optional pruning: remove offers that are not cheaper than buying items individually
    const filteredSpecial = special.filter(offer => {
        let total = 0;
        for (let i = 0; i < n; i++) {
            total += offer[i] * price[i];
        }
        return total > offer[n]; // keep only if it offers a discount
    });

    const dfs = (curNeeds: number[]): number => {
        const key = curNeeds.join(',');
        if (memo.has(key)) return memo.get(key)!;

        // Cost without any special offers
        let minCost = 0;
        for (let i = 0; i < n; i++) {
            minCost += curNeeds[i] * price[i];
        }

        // Try each special offer
        for (const offer of filteredSpecial) {
            const nextNeeds: number[] = [];
            let valid = true;
            for (let i = 0; i < n; i++) {
                if (offer[i] > curNeeds[i]) {
                    valid = false;
                    break;
                }
                nextNeeds.push(curNeeds[i] - offer[i]);
            }
            if (!valid) continue;

            const costWithOffer = dfs(nextNeeds) + offer[n];
            if (costWithOffer < minCost) {
                minCost = costWithOffer;
            }
        }

        memo.set(key, minCost);
        return minCost;
    };

    return dfs(needs);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $price
     * @param Integer[][] $special
     * @param Integer[] $needs
     * @return Integer
     */
    function shoppingOffers($price, $special, $needs) {
        $n = count($price);
        // Keep only specials that are cheaper than buying items individually
        $validSpecials = [];
        foreach ($special as $sp) {
            $total = 0;
            for ($i = 0; $i < $n; $i++) {
                $total += $sp[$i] * $price[$i];
            }
            if ($total > $sp[$n]) {
                $validSpecials[] = $sp;
            }
        }

        $memo = [];

        $dfs = function($currNeeds) use (&$dfs, &$memo, $price, $validSpecials, $n) {
            $key = implode(',', $currNeeds);
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            // Cost without any special offers
            $minCost = 0;
            for ($i = 0; $i < $n; $i++) {
                $minCost += $currNeeds[$i] * $price[$i];
            }

            // Try each valid special offer
            foreach ($validSpecials as $sp) {
                $newNeeds = [];
                $canUse = true;
                for ($i = 0; $i < $n; $i++) {
                    if ($currNeeds[$i] < $sp[$i]) {
                        $canUse = false;
                        break;
                    }
                    $newNeeds[$i] = $currNeeds[$i] - $sp[$i];
                }
                if ($canUse) {
                    $cost = $sp[$n] + $dfs($newNeeds);
                    if ($cost < $minCost) {
                        $minCost = $cost;
                    }
                }
            }

            $memo[$key] = $minCost;
            return $minCost;
        };

        return $dfs($needs);
    }
}
```

## Swift

```swift
class Solution {
    func shoppingOffers(_ price: [Int], _ special: [[Int]], _ needs: [Int]) -> Int {
        var filteredSpecials = [[Int]]()
        for sp in special {
            var total = 0
            for i in 0..<price.count {
                total += sp[i] * price[i]
            }
            if sp[price.count] < total {
                filteredSpecials.append(sp)
            }
        }
        
        var memo = [String: Int]()
        
        func dfs(_ curNeeds: [Int]) -> Int {
            let key = curNeeds.map { String($0) }.joined(separator: ",")
            if let cached = memo[key] {
                return cached
            }
            
            var minCost = 0
            for i in 0..<price.count {
                minCost += curNeeds[i] * price[i]
            }
            
            for sp in filteredSpecials {
                var newNeeds = [Int]()
                var canApply = true
                for i in 0..<price.count {
                    if curNeeds[i] < sp[i] {
                        canApply = false
                        break
                    }
                    newNeeds.append(curNeeds[i] - sp[i])
                }
                if canApply {
                    let cost = sp[price.count] + dfs(newNeeds)
                    if cost < minCost {
                        minCost = cost
                    }
                }
            }
            
            memo[key] = minCost
            return minCost
        }
        
        return dfs(needs)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shoppingOffers(price: List<Int>, special: List<List<Int>>, needs: List<Int>): Int {
        val n = price.size
        // Filter out specials that are not cheaper than buying items individually
        val usefulSpecials = mutableListOf<List<Int>>()
        for (sp in special) {
            var total = 0
            for (i in 0 until n) {
                total += sp[i] * price[i]
            }
            if (total > sp[n]) { // only keep if it offers a discount
                usefulSpecials.add(sp)
            }
        }

        val memo = HashMap<List<Int>, Int>()

        fun dfs(cur: List<Int>): Int {
            memo[cur]?.let { return it }

            var minCost = 0
            for (i in 0 until n) {
                minCost += cur[i] * price[i]
            }

            for (sp in usefulSpecials) {
                val next = mutableListOf<Int>()
                var ok = true
                for (i in 0 until n) {
                    if (cur[i] < sp[i]) {
                        ok = false
                        break
                    }
                    next.add(cur[i] - sp[i])
                }
                if (!ok) continue
                val cost = sp[n] + dfs(next)
                if (cost < minCost) minCost = cost
            }

            memo[cur] = minCost
            return minCost
        }

        return dfs(needs)
    }
}
```

## Dart

```dart
class Solution {
  late List<int> _price;
  late List<List<int>> _specials;
  final Map<String, int> _memo = {};

  int shoppingOffers(List<int> price, List<List<int>> special, List<int> needs) {
    _price = price;
    // Keep only specials that are actually cheaper than buying items individually
    _specials = [];
    for (var sp in special) {
      int total = 0;
      for (int i = 0; i < _price.length; i++) {
        total += sp[i] * _price[i];
      }
      if (total > sp[_price.length]) {
        _specials.add(sp);
      }
    }
    return _dfs(needs);
  }

  int _dfs(List<int> needs) {
    final key = needs.join(',');
    if (_memo.containsKey(key)) return _memo[key]!;

    // Cost without any special offers
    int minCost = 0;
    for (int i = 0; i < needs.length; i++) {
      minCost += needs[i] * _price[i];
    }

    // Try each special offer
    for (var sp in _specials) {
      bool canUse = true;
      final List<int> nextNeeds = List.filled(needs.length, 0);
      for (int i = 0; i < needs.length; i++) {
        if (sp[i] > needs[i]) {
          canUse = false;
          break;
        }
        nextNeeds[i] = needs[i] - sp[i];
      }
      if (!canUse) continue;

      int costWithSpecial = _dfs(nextNeeds) + sp[_price.length];
      if (costWithSpecial < minCost) {
        minCost = costWithSpecial;
      }
    }

    _memo[key] = minCost;
    return minCost;
  }
}
```

## Golang

```go
func shoppingOffers(price []int, special [][]int, needs []int) int {
	// Filter out non-beneficial specials
	filtered := make([][]int, 0, len(special))
	for _, sp := range special {
		total := 0
		for i := 0; i < len(price); i++ {
			total += sp[i] * price[i]
		}
		if total > sp[len(sp)-1] { // cheaper than buying individually
			filtered = append(filtered, sp)
		}
	}

	memo := make(map[int]int)

	// Encode needs slice into a single integer using base 11 (needs[i] <= 10)
	encode := func(arr []int) int {
		key := 0
		for _, v := range arr {
			key = key*11 + v
		}
		return key
	}

	var dfs func([]int) int
	dfs = func(cur []int) int {
		k := encode(cur)
		if val, ok := memo[k]; ok {
			return val
		}

		// Cost without using any special offer
		minCost := 0
		for i, cnt := range cur {
			minCost += cnt * price[i]
		}

		// Try each filtered special offer
		for _, sp := range filtered {
			newNeeds := make([]int, len(cur))
			valid := true
			for i := 0; i < len(cur); i++ {
				if sp[i] > cur[i] {
					valid = false
					break
				}
				newNeeds[i] = cur[i] - sp[i]
			}
			if !valid {
				continue
			}
			cost := dfs(newNeeds) + sp[len(sp)-1]
			if cost < minCost {
				minCost = cost
			}
		}

		memo[k] = minCost
		return minCost
	}

	return dfs(needs)
}
```

## Ruby

```ruby
def shopping_offers(price, special, needs)
  # Remove specials that are not cheaper than buying items individually
  filtered = special.select do |sp|
    total = 0
    sp[0...price.length].each_with_index { |cnt, i| total += cnt * price[i] }
    sp[-1] < total
  end

  memo = {}
  dfs = nil
  dfs = lambda do |cur_needs|
    key = cur_needs.join(',')
    return memo[key] if memo.key?(key)

    # Cost without using any special offer
    min_cost = 0
    cur_needs.each_with_index { |need, i| min_cost += need * price[i] }

    filtered.each do |sp|
      new_needs = []
      valid = true
      cur_needs.each_with_index do |need, i|
        if need < sp[i]
          valid = false
          break
        else
          new_needs << (need - sp[i])
        end
      end
      next unless valid

      cost = dfs.call(new_needs) + sp[-1]
      min_cost = [min_cost, cost].min
    end

    memo[key] = min_cost
  end

  dfs.call(needs)
end
```

## Scala

```scala
object Solution {
  def shoppingOffers(price: List[Int], special: List[List[Int]], needs: List[Int]): Int = {
    val n = price.length
    val memo = scala.collection.mutable.Map[Vector[Int], Int]()

    def dfs(cur: Vector[Int]): Int = {
      if (memo.contains(cur)) return memo(cur)
      var minCost = (price zip cur).map { case (p, cnt) => p * cnt }.sum

      for (offer <- special) {
        val counts = offer.take(n)
        val offerPrice = offer.last
        var ok = true
        val nextBuilder = Vector.newBuilder[Int]
        var i = 0
        while (i < n) {
          if (cur(i) < counts(i)) ok = false
          nextBuilder += (cur(i) - counts(i))
          i += 1
        }
        if (ok) {
          val next = nextBuilder.result()
          val cost = dfs(next) + offerPrice
          if (cost < minCost) minCost = cost
        }
      }

      memo(cur) = minCost
      minCost
    }

    dfs(needs.toVector)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn shopping_offers(price: Vec<i32>, special: Vec<Vec<i32>>, needs: Vec<i32>) -> i32 {
        // Keep only specials that are cheaper than buying items individually
        let mut filtered = Vec::new();
        for sp in &special {
            let mut total = 0;
            for i in 0..price.len() {
                total += sp[i] * price[i];
            }
            if sp[price.len()] < total {
                filtered.push(sp.clone());
            }
        }

        use std::collections::HashMap;

        fn dfs(
            price: &Vec<i32>,
            specials: &Vec<Vec<i32>>,
            needs: Vec<i32>,
            memo: &mut HashMap<Vec<i32>, i32>,
        ) -> i32 {
            if let Some(&v) = memo.get(&needs) {
                return v;
            }

            // Cost without any special offers
            let mut best = 0;
            for i in 0..price.len() {
                best += needs[i] * price[i];
            }

            'outer: for sp in specials {
                let mut next = Vec::with_capacity(needs.len());
                for i in 0..needs.len() {
                    if needs[i] < sp[i] {
                        continue 'outer; // cannot use this special
                    }
                    next.push(needs[i] - sp[i]);
                }
                let cost = dfs(price, specials, next.clone(), memo) + sp[price.len()];
                if cost < best {
                    best = cost;
                }
            }

            memo.insert(needs.clone(), best);
            best
        }

        let mut memo: HashMap<Vec<i32>, i32> = HashMap::new();
        dfs(&price, &filtered, needs, &mut memo)
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (shopping-offers price special needs)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((n (length price))
         (memo (make-hash)))
    (define (applicable? need offer)
      (let loop ((ns need) (os offer))
        (cond [(null? os) #t]
              [(< (car ns) (car os)) #f]
              [else (loop (cdr ns) (cdr os))])))
    (define (subtract need offer)
      (map - need offer))
    (define (direct-cost need)
      (let loop ((ps price) (ns need) (acc 0))
        (if (null? ps)
            acc
            (loop (cdr ps) (cdr ns) (+ acc (* (car ps) (car ns)))))))
    (define (dfs need)
      (cond [(hash-has-key? memo need) (hash-ref memo need)]
            [else
             (let ((best (direct-cost need)))
               (for ([sp special])
                 (let* ((offer-items (take sp n))
                        (offer-price (list-ref sp n)))
                   (when (applicable? need offer-items)
                     (let ((new-need (subtract need offer-items)))
                       (set! best (min best (+ offer-price (dfs new-need))))))))
               (hash-set! memo need best)
               best)]))
    (dfs needs)))
```

## Erlang

```erlang
-module(solution).
-export([shopping_offers/3]).

-spec shopping_offers(Price :: [integer()], Special :: [[integer()]], Needs :: [integer()]) -> integer().
shopping_offers(Price, Special, Needs) ->
    {Cost, _} = dfs(Price, Special, Needs, #{}),
    Cost.

%% Depth‑first search with memoization
dfs(_Price, _Specials, Needs, Memo) ->
    Key = list_to_tuple(Needs),
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            BaseCost = base_cost(_Price, Needs),
            {MinCost, NewMemo} = try_offers(_Specials, _Specials, _Price, Needs, BaseCost, Memo),
            FinalMemo = maps:put(Key, MinCost, NewMemo),
            {MinCost, FinalMemo}
    end.

%% Try all special offers and keep the minimal cost
try_offers(_AllSpecials, [], _Price, _Needs, MinSoFar, Memo) ->
    {MinSoFar, Memo};
try_offers(AllSpecials, [Offer|Rest], Price, Needs, MinSoFar, Memo) ->
    case can_apply(Needs, Offer) of
        true ->
            NewNeeds = apply_offer(Needs, Offer),
            {CostAfter, Memo1} = dfs(Price, AllSpecials, NewNeeds, Memo),
            Total = CostAfter + lists:last(Offer),
            NewMin = min(MinSoFar, Total),
            try_offers(AllSpecials, Rest, Price, Needs, NewMin, Memo1);
        false ->
            try_offers(AllSpecials, Rest, Price, Needs, MinSoFar, Memo)
    end.

%% Check if an offer can be used given current needs
can_apply(Needs, Offer) ->
    Items = lists:sublist(Offer, length(Offer)-1),
    can_apply_items(Needs, Items).

can_apply_items([], []) -> true;
can_apply_items([N|Ns], [O|Os]) when N >= O -> can_apply_items(Ns, Os);
can_apply_items(_, _) -> false.

%% Apply an offer to the current needs (subtract quantities)
apply_offer(Needs, Offer) ->
    Items = lists:sublist(Offer, length(Offer)-1),
    apply_subtract(Needs, Items).

apply_subtract([], []) -> [];
apply_subtract([N|Ns], [O|Os]) -> [N-O | apply_subtract(Ns, Os)].

%% Cost of buying remaining items individually
base_cost(Price, Needs) ->
    lists:foldl(fun({P,N}, Acc) -> Acc + P * N end,
                0,
                lists:zip(Price, Needs)).
```

## Elixir

```elixir
defmodule Solution do
  @spec shopping_offers(price :: [integer], special :: [[integer]], needs :: [integer]) :: integer
  def shopping_offers(price, special, needs) do
    filtered =
      Enum.filter(special, fn sp ->
        regular_cost =
          sp
          |> Enum.take(length(price))
          |> Enum.zip(price)
          |> Enum.reduce(0, fn {cnt, p}, acc -> acc + cnt * p end)

        special_price = List.last(sp)
        regular_cost > special_price
      end)

    {ans, _} = dfs(needs, price, filtered, %{})
    ans
  end

  defp dfs(needs, price, specials, memo) do
    case Map.get(memo, needs) do
      nil ->
        direct =
          Enum.zip(needs, price)
          |> Enum.reduce(0, fn {need, p}, acc -> acc + need * p end)

        {best, new_memo} =
          Enum.reduce(specials, {direct, memo}, fn sp, {cur_best, cur_memo} ->
            counts = Enum.take(sp, length(price))

            if applicable?(needs, counts) do
              next_needs = subtract(needs, counts)
              {cost_sub, updated_memo} = dfs(next_needs, price, specials, cur_memo)
              total = List.last(sp) + cost_sub
              {min(cur_best, total), updated_memo}
            else
              {cur_best, cur_memo}
            end
          end)

        memo2 = Map.put(new_memo, needs, best)
        {best, memo2}

      val ->
        {val, memo}
    end
  end

  defp applicable?(needs, counts) do
    Enum.zip(needs, counts)
    |> Enum.all?(fn {n, c} -> n >= c end)
  end

  defp subtract(needs, counts) do
    Enum.zip(needs, counts)
    |> Enum.map(fn {n, c} -> n - c end)
  end
end
```
