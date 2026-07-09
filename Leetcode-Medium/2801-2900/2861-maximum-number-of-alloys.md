# 2861. Maximum Number of Alloys

## Cpp

```cpp
class Solution {
public:
    int maxNumberOfAlloys(int n, int k, int budget, vector<vector<int>>& composition,
                          vector<int>& stock, vector<int>& cost) {
        using ll = long long;
        auto can = [&](ll x) -> bool {
            for (int i = 0; i < k; ++i) {
                ll total = 0;
                for (int j = 0; j < n; ++j) {
                    ll need = (ll)composition[i][j] * x - stock[j];
                    if (need > 0) {
                        total += need * cost[j];
                        if (total > budget) break;
                    }
                }
                if (total <= budget) return true;
            }
            return false;
        };
        
        ll lo = 0, hi = 1;
        while (can(hi)) {
            lo = hi;
            hi <<= 1; // double
            if (hi > 2000000000LL) { // safe upper bound
                hi = 2000000005LL;
                break;
            }
        }
        while (lo < hi) {
            ll mid = lo + (hi - lo + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
class Solution {
    public int maxNumberOfAlloys(int n, int k, int budget, java.util.List<java.util.List<Integer>> composition,
                                 java.util.List<Integer> stock, java.util.List<Integer> cost) {
        long[] stockArr = new long[n];
        long[] costArr = new long[n];
        for (int i = 0; i < n; i++) {
            stockArr[i] = stock.get(i);
            costArr[i] = cost.get(i);
        }
        int[][] comp = new int[k][n];
        for (int i = 0; i < k; i++) {
            java.util.List<Integer> row = composition.get(i);
            for (int j = 0; j < n; j++) {
                comp[i][j] = row.get(j);
            }
        }

        long maxAlloys = 0;
        for (int i = 0; i < k; i++) {
            long high = Long.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                long possibleUnits = stockArr[j] + budget / costArr[j];
                long limit = possibleUnits / comp[i][j];
                if (limit < high) {
                    high = limit;
                }
            }

            long low = 0;
            while (low < high) {
                long mid = (low + high + 1) >>> 1;
                if (canMake(comp[i], stockArr, costArr, budget, mid)) {
                    low = mid;
                } else {
                    high = mid - 1;
                }
            }
            if (low > maxAlloys) {
                maxAlloys = low;
            }
        }
        return (int) maxAlloys;
    }

    private boolean canMake(int[] compRow, long[] stockArr, long[] costArr, int budget, long x) {
        long total = 0;
        for (int j = 0; j < compRow.length; j++) {
            long need = compRow[j] * x;
            if (need > stockArr[j]) {
                long buy = need - stockArr[j];
                total += buy * costArr[j];
                if (total > budget) {
                    return false;
                }
            }
        }
        return total <= budget;
    }
}
```

## Python

```python
class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Precompute minimal cost per alloy when buying everything (no stock)
        min_buy_cost = float('inf')
        for i in range(k):
            cur = 0
            comp = composition[i]
            for j in range(n):
                cur += comp[j] * cost[j]
            if cur < min_buy_cost:
                min_buy_cost = cur

        # Upper bound: total resources (budget + value of existing stock) divided by minimal per-alloy cost
        total_stock_value = 0
        for j in range(n):
            total_stock_value += stock[j] * cost[j]
        hi = (budget + total_stock_value) // min_buy_cost + 1  # exclusive upper bound

        def can_make(x):
            for i in range(k):
                need = 0
                comp = composition[i]
                for j in range(n):
                    required = comp[j] * x
                    if required > stock[j]:
                        need += (required - stock[j]) * cost[j]
                        if need > budget:   # early stop
                            break
                if need <= budget:
                    return True
            return False

        lo, hi = 0, hi
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_make(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition, stock, cost):
        # compute an upper bound for binary search
        ub = 0
        for i in range(k):
            cur = float('inf')
            for j in range(n):
                # maximum units of metal j we could have (stock + buying with whole budget)
                max_units = stock[j] + budget // cost[j]
                possible = max_units // composition[i][j]
                if possible < cur:
                    cur = possible
            if cur > ub:
                ub = cur

        low, high = 0, ub + 1  # high is exclusive
        while low < high:
            mid = (low + high) // 2
            feasible = False
            for i in range(k):
                total_cost = 0
                for j in range(n):
                    need = composition[i][j] * mid - stock[j]
                    if need > 0:
                        total_cost += need * cost[j]
                        if total_cost > budget:
                            break
                if total_cost <= budget:
                    feasible = True
                    break
            if feasible:
                low = mid + 1
            else:
                high = mid
        return low - 1
```

## C

```c
#include <stddef.h>
#include <limits.h>

static int canMake(long long x, int n, int k, int budget,
                   int **composition, int *stock, int *cost) {
    for (int i = 0; i < k; ++i) {
        long long totalCost = 0;
        for (int j = 0; j < n; ++j) {
            long long need = (long long)composition[i][j] * x;
            if (need > stock[j]) {
                long long buy = need - stock[j];
                totalCost += buy * cost[j];
                if (totalCost > budget) break;
            }
        }
        if (totalCost <= budget) return 1;
    }
    return 0;
}

int maxNumberOfAlloys(int n, int k, int budget,
                      int **composition, int compositionSize, int *compositionColSize,
                      int *stock, int stockSize, int *cost, int costSize) {
    (void)compositionSize; (void)compositionColSize; (void)stockSize; (void)costSize;
    long long hi = 0;
    for (int i = 0; i < k; ++i) {
        long long cur = LLONG_MAX;
        for (int j = 0; j < n; ++j) {
            long long avail = stock[j] + budget / cost[j];
            long long possible = avail / composition[i][j];
            if (possible < cur) cur = possible;
        }
        if (cur > hi) hi = cur;
    }
    long long lo = 0, mid, ans = 0;
    while (lo <= hi) {
        mid = lo + (hi - lo) / 2;
        if (canMake(mid, n, k, budget, composition, stock, cost)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNumberOfAlloys(int n, int k, int budget, IList<IList<int>> composition, IList<int> stock, IList<int> cost) {
        long best = 0;
        for (int i = 0; i < k; i++) {
            long lo = 0, hi = 2000000000L; // sufficient upper bound
            while (lo < hi) {
                long mid = (lo + hi + 1) >> 1;
                if (CanMake(composition[i], mid, stock, cost, budget))
                    lo = mid;
                else
                    hi = mid - 1;
            }
            if (lo > best) best = lo;
        }
        return (int)best;
    }

    private bool CanMake(IList<int> comp, long x, IList<int> stock, IList<int> cost, int budget) {
        long total = 0;
        for (int j = 0; j < stock.Count; j++) {
            long need = (long)comp[j] * x - stock[j];
            if (need > 0) {
                total += need * cost[j];
                if (total > budget) return false;
            }
        }
        return total <= budget;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} budget
 * @param {number[][]} composition
 * @param {number[]} stock
 * @param {number[]} cost
 * @return {number}
 */
var maxNumberOfAlloys = function(n, k, budget, composition, stock, cost) {
    // check if we can produce `x` alloys using any machine within the budget
    const canProduce = (x) => {
        for (let i = 0; i < k; ++i) {
            let totalCost = 0;
            const comp = composition[i];
            for (let j = 0; j < n; ++j) {
                const need = comp[j] * x - stock[j];
                if (need > 0) {
                    totalCost += need * cost[j];
                    if (totalCost > budget) break; // early stop
                }
            }
            if (totalCost <= budget) return true;
        }
        return false;
    };

    // exponential search to find an upper bound
    let lo = 0, hi = 1;
    while (canProduce(hi)) {
        lo = hi;
        hi *= 2;
        // safeguard against overflow beyond safe integer range
        if (hi > Number.MAX_SAFE_INTEGER) {
            hi = Number.MAX_SAFE_INTEGER;
            break;
        }
    }

    // binary search between lo and hi (inclusive)
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canProduce(mid)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function maxNumberOfAlloys(n: number, k: number, budget: number, composition: number[][], stock: number[], cost: number[]): number {
    const canMake = (x: number): boolean => {
        let minCost = Number.MAX_SAFE_INTEGER;
        for (let i = 0; i < k; ++i) {
            let total = 0;
            const comp = composition[i];
            for (let j = 0; j < n; ++j) {
                const need = comp[j] * x;
                if (need > stock[j]) {
                    const buy = need - stock[j];
                    total += buy * cost[j];
                    if (total > budget) break; // no need to continue for this machine
                }
            }
            if (total < minCost) minCost = total;
            if (minCost <= budget) return true; // early exit, feasible machine found
        }
        return minCost <= budget;
    };

    let lo = 0;
    let hi = 1;
    while (canMake(hi)) {
        hi *= 2;
        if (hi > 2_000_000_000) break; // safe upper bound
    }

    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canMake(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $budget
     * @param Integer[][] $composition
     * @param Integer[] $stock
     * @param Integer[] $cost
     * @return Integer
     */
    function maxNumberOfAlloys($n, $k, $budget, $composition, $stock, $cost) {
        // total value of existing stock (if we had to buy it)
        $totalStockValue = 0;
        for ($j = 0; $j < $n; ++$j) {
            $totalStockValue += $stock[$j] * $cost[$j];
        }

        // minimal cost to produce one alloy using any machine (buying all metals)
        $minCostPerAlloy = PHP_INT_MAX;
        for ($i = 0; $i < $k; ++$i) {
            $c = 0;
            for ($j = 0; $j < $n; ++$j) {
                $c += $composition[$i][$j] * $cost[$j];
            }
            if ($c < $minCostPerAlloy) $minCostPerAlloy = $c;
        }

        // Upper bound for binary search
        $hi = intdiv($budget + $totalStockValue, $minCostPerAlloy);
        $lo = 0;

        // Helper to check feasibility for a given target count
        $canMake = function(int $target) use ($k, $n, $budget, $composition, $stock, $cost): bool {
            for ($i = 0; $i < $k; ++$i) {
                $needCost = 0;
                for ($j = 0; $j < $n; ++$j) {
                    $required = $target * $composition[$i][$j];
                    if ($required > $stock[$j]) {
                        $extra = $required - $stock[$j];
                        $needCost += $extra * $cost[$j];
                        if ($needCost > $budget) {
                            break; // this machine already exceeds budget
                        }
                    }
                }
                if ($needCost <= $budget) {
                    return true;
                }
            }
            return false;
        };

        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($canMake($mid)) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }

        return $lo;
    }
}
```

## Swift

```swift
class Solution {
    func maxNumberOfAlloys(_ n: Int, _ k: Int, _ budget: Int, _ composition: [[Int]], _ stock: [Int], _ cost: [Int]) -> Int {
        let totalStockValue = zip(stock, cost).reduce(Int64(0)) { $0 + Int64($1.0) * Int64($1.1) }
        var minCostPerAlloy = Int64.max
        for m in 0..<k {
            var sum: Int64 = 0
            for j in 0..<n {
                sum += Int64(composition[m][j]) * Int64(cost[j])
            }
            if sum < minCostPerAlloy { minCostPerAlloy = sum }
        }
        let hi = Int((Int64(budget) + totalStockValue) / minCostPerAlloy)
        
        func canProduce(machine: Int, alloys: Int) -> Bool {
            var neededCost: Int64 = 0
            for j in 0..<n {
                let required = Int64(composition[machine][j]) * Int64(alloys)
                if required > Int64(stock[j]) {
                    let deficit = required - Int64(stock[j])
                    neededCost += deficit * Int64(cost[j])
                    if neededCost > Int64(budget) { return false }
                }
            }
            return neededCost <= Int64(budget)
        }
        
        var answer = 0
        for m in 0..<k {
            var low = 0
            var high = hi
            while low < high {
                let mid = (low + high + 1) / 2
                if canProduce(machine: m, alloys: mid) {
                    low = mid
                } else {
                    high = mid - 1
                }
            }
            if low > answer { answer = low }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumberOfAlloys(
        n: Int,
        k: Int,
        budget: Int,
        composition: List<List<Int>>,
        stock: List<Int>,
        cost: List<Int>
    ): Int {
        val stockArr = LongArray(n) { stock[it].toLong() }
        val costArr = LongArray(n) { cost[it].toLong() }

        // convert composition to long arrays for faster access
        val comp = Array(k) { LongArray(n) }
        for (i in 0 until k) {
            val row = composition[i]
            for (j in 0 until n) {
                comp[i][j] = row[j].toLong()
            }
        }

        var totalStockValue = 0L
        for (j in 0 until n) {
            totalStockValue += stockArr[j] * costArr[j]
        }

        var minCostPerAlloy = Long.MAX_VALUE
        for (i in 0 until k) {
            var sum = 0L
            for (j in 0 until n) {
                sum += comp[i][j] * costArr[j]
            }
            if (sum < minCostPerAlloy) minCostPerAlloy = sum
        }

        val budgetL = budget.toLong()
        // safe upper bound for binary search
        var highBound = (budgetL + totalStockValue) / minCostPerAlloy + 1

        var answer = 0L
        for (i in 0 until k) {
            var low = 0L
            var high = highBound
            while (low < high) {
                val mid = (low + high + 1) / 2
                var needCost = 0L
                for (j in 0 until n) {
                    val required = comp[i][j] * mid
                    var need = required - stockArr[j]
                    if (need > 0) {
                        needCost += need * costArr[j]
                        if (needCost > budgetL) break
                    }
                }
                if (needCost <= budgetL) {
                    low = mid
                } else {
                    high = mid - 1
                }
            }
            if (low > answer) answer = low
        }

        return answer.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxNumberOfAlloys(int n, int k, int budget, List<List<int>> composition,
      List<int> stock, List<int> cost) {
    // Maximum units of each metal we could possibly have (stock + buying all budget)
    List<int> maxUnits = List.filled(n, 0);
    for (int j = 0; j < n; ++j) {
      maxUnits[j] = stock[j] + budget ~/ cost[j];
    }

    // Upper bound for answer using per‑machine limits
    int high = 0;
    for (int i = 0; i < k; ++i) {
      int cur = 1 << 60; // large number
      for (int j = 0; j < n; ++j) {
        int possible = maxUnits[j] ~/ composition[i][j];
        if (possible < cur) cur = possible;
      }
      if (cur > high) high = cur;
    }

    int low = 0;
    while (low < high) {
      int mid = ((low + high + 1) >> 1);
      bool feasible = false;

      for (int i = 0; i < k && !feasible; ++i) {
        int totalCost = 0;
        for (int j = 0; j < n; ++j) {
          int need = composition[i][j] * mid - stock[j];
          if (need > 0) {
            totalCost += need * cost[j];
            if (totalCost > budget) break;
          }
        }
        if (totalCost <= budget) feasible = true;
      }

      if (feasible) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }

    return low;
  }
}
```

## Golang

```go
func maxNumberOfAlloys(n int, k int, budget int, composition [][]int, stock []int, cost []int) int {
	// total value of existing stock in terms of money
	var totalStockVal int64
	for i := 0; i < n; i++ {
		totalStockVal += int64(stock[i]) * int64(cost[i])
	}
	// minimal cost to produce one alloy (if we had to buy everything)
	const inf = int64(1 << 62)
	minCostPerAlloy := inf
	for i := 0; i < k; i++ {
		var sum int64
		for j := 0; j < n; j++ {
			sum += int64(composition[i][j]) * int64(cost[j])
		}
		if sum < minCostPerAlloy {
			minCostPerAlloy = sum
		}
	}
	// upper bound for binary search
	high := (int64(budget) + totalStockVal) / minCostPerAlloy
	high += 100000 // safety buffer

	low := int64(0)
	for low < high {
		mid := (low + high + 1) / 2
		if canProduce(mid, n, k, budget, composition, stock, cost) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return int(low)
}

func canProduce(x int64, n int, k int, budget int, composition [][]int, stock []int, cost []int) bool {
	b := int64(budget)
	for i := 0; i < k; i++ {
		var total int64
		for j := 0; j < n; j++ {
			required := int64(composition[i][j])*x - int64(stock[j])
			if required > 0 {
				total += required * int64(cost[j])
				if total > b {
					break
				}
			}
		}
		if total <= b {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def max_number_of_alloys(n, k, budget, composition, stock, cost)
  # Helper to determine if we can produce x alloys with any machine
  feasible = lambda do |x|
    k.times do |i|
      total_cost = 0
      n.times do |j|
        need = composition[i][j] * x
        if need > stock[j]
          total_cost += (need - stock[j]) * cost[j]
          break if total_cost > budget
        end
      end
      return true if total_cost <= budget
    end
    false
  end

  low = 0
  high = 2_000_000_000 # sufficiently large upper bound

  while low < high
    mid = (low + high + 1) / 2
    if feasible.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end

  low
end
```

## Scala

```scala
object Solution {
    def maxNumberOfAlloys(n: Int, k: Int, budget: Int, composition: List[List[Int]], stock: List[Int], cost: List[Int]): Int = {
        val compArr: Array[Array[Long]] = composition.map(_.map(_.toLong).toArray).toArray
        val stockArr: Array[Long] = stock.map(_.toLong).toArray
        val costArr: Array[Long] = cost.map(_.toLong).toArray
        val budgetL: Long = budget.toLong

        def canMake(x: Long): Boolean = {
            var i = 0
            while (i < k) {
                var totalCost: Long = 0L
                var j = 0
                while (j < n && totalCost <= budgetL) {
                    val need = compArr(i)(j) * x
                    if (need > stockArr(j)) {
                        val buy = need - stockArr(j)
                        totalCost += buy * costArr(j)
                    }
                    j += 1
                }
                if (totalCost <= budgetL) return true
                i += 1
            }
            false
        }

        var lo: Long = 0L
        var hi: Long = 2000000000L // safe upper bound
        while (lo < hi) {
            val mid = (lo + hi + 1) >>> 1
            if (canMake(mid)) lo = mid else hi = mid - 1
        }
        lo.toInt
    }
}
```

## Rust

```rust
impl Solution {
    fn can_make(
        x: i64,
        comp: &[i32],
        stock: &[i32],
        cost: &[i32],
        budget: i64,
    ) -> bool {
        let mut total = 0i64;
        for j in 0..stock.len() {
            let need = comp[j] as i64 * x;
            let have = stock[j] as i64;
            if need > have {
                let buy = need - have;
                total += buy * cost[j] as i64;
                if total > budget {
                    return false;
                }
            }
        }
        total <= budget
    }

    pub fn max_number_of_alloys(
        n: i32,
        k: i32,
        budget: i32,
        composition: Vec<Vec<i32>>,
        stock: Vec<i32>,
        cost: Vec<i32>,
    ) -> i32 {
        let n_usize = n as usize;
        let k_usize = k as usize;
        let budget_i64 = budget as i64;
        let mut answer: i64 = 0;

        for machine_idx in 0..k_usize {
            let comp = &composition[machine_idx];
            // Upper bound based on stock + maximum purchasable units
            let mut hi: i64 = i64::MAX;
            for j in 0..n_usize {
                let max_units = stock[j] as i64 + budget_i64 / cost[j] as i64;
                let possible = max_units / comp[j] as i64;
                if possible < hi {
                    hi = possible;
                }
            }

            // Binary search for the maximum feasible x
            let mut lo: i64 = 0;
            let mut high_exclusive: i64 = hi + 1; // exclusive upper bound
            while lo < high_exclusive {
                let mid = (lo + high_exclusive) / 2;
                if Self::can_make(mid, comp, &stock, &cost, budget_i64) {
                    lo = mid + 1;
                } else {
                    high_exclusive = mid;
                }
            }
            let max_for_machine = lo - 1;
            if max_for_machine > answer {
                answer = max_for_machine;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
(define/contract (max-number-of-alloys n k budget composition stock cost)
  (-> exact-integer? exact-integer? exact-integer?
      (listof (listof exact-integer?))
      (listof exact-integer?) (listof exact-integer?)
      exact-integer?)
  (let* ((hi 2000000000) ; sufficiently large upper bound
         (feasible?
          (lambda (t)
            (let loop-mach ((m 0))
              (if (= m k)
                  #f
                  (let ((comp (list-ref composition m)))
                    (let loop-metal ((j 0) (sum 0))
                      (cond
                        [(= j n)
                         (if (<= sum budget)
                             #t                     ; this machine works
                             (loop-mach (+ m 1)))] ; try next machine
                        [else
                         (let* ((need (* (list-ref comp j) t))
                                (extra (- need (list-ref stock j)))
                                (extra (if (> extra 0) extra 0))
                                (add (* extra (list-ref cost j)))
                                (new-sum (+ sum add)))
                           (if (> new-sum budget)
                               (loop-mach (+ m 1)) ; this machine fails
                               (loop-metal (+ j 1) new-sum)))])])))))))
    (let loop ((low 0) (high hi))
      (if (= low high)
          low
          (let* ((mid (quotient (+ low high 1) 2)))
            (if (feasible? mid)
                (loop mid high)
                (loop low (- mid 1))))))))
```

## Erlang

```erlang
max_number_of_alloys(_N,_K,Budget,Composition,Stock,Cost) ->
    Upper = compute_upper(Composition, Stock, Cost, Budget),
    binary_search(0, Upper, Budget, Composition, Stock, Cost).

compute_upper([], _Stock, _Cost, _Budget) -> 0;
compute_upper(CompList, Stock, Cost, Budget) ->
    UpperVals = [machine_upper(MachineComp, Stock, Cost, Budget) || MachineComp <- CompList],
    lists:max(UpperVals).

machine_upper(MachineComp, Stock, Cost, Budget) ->
    machine_upper_lists(MachineComp, Stock, Cost, Budget, 1 bsl 60).

machine_upper_lists([], [], [], _Budget, MinSoFar) -> MinSoFar;
machine_upper_lists([C|Cs], [S|Ss], [P|Ps], Budget, MinSoFar) ->
    MaxAlloy = (S + Budget div P) div C,
    NewMin = erlang:min(MinSoFar, MaxAlloy),
    machine_upper_lists(Cs, Ss, Ps, Budget, NewMin).

binary_search(Low, High, _Budget, _Comp, _Stock, _Cost) when Low > High ->
    Low - 1;
binary_search(Low, High, Budget, Comp, Stock, Cost) ->
    Mid = (Low + High) div 2,
    case feasible(Mid, Comp, Stock, Cost, Budget) of
        true -> binary_search(Mid+1, High, Budget, Comp, Stock, Cost);
        false -> binary_search(Low, Mid-1, Budget, Comp, Stock, Cost)
    end.

feasible(_X, [], _Stock, _Cost, _Budget) -> false;
feasible(X, [MachineComp|Rest], Stock, Cost, Budget) ->
    case total_cost(X, MachineComp, Stock, Cost) =< Budget of
        true -> true;
        false -> feasible(X, Rest, Stock, Cost, Budget)
    end.

total_cost(X, MachineComp, Stock, Cost) ->
    total_cost_lists(MachineComp, Stock, Cost, X, 0).

total_cost_lists([], [], [], _X, Acc) -> Acc;
total_cost_lists([C|Cs], [S|Ss], [P|Ps], X, Acc) ->
    Req = C * X,
    Need = erlang:max(0, Req - S),
    NewAcc = Acc + Need * P,
    total_cost_lists(Cs, Ss, Ps, X, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_number_of_alloys(n :: integer, k :: integer, budget :: integer, composition :: [[integer]], stock :: [integer], cost :: [integer]) :: integer
  def max_number_of_alloys(_n, _k, budget, composition, stock, cost) do
    composition
    |> Enum.map(&max_alloys_for_machine(&1, stock, cost, budget))
    |> Enum.max()
  end

  defp max_alloys_for_machine(comp, stock, cost, budget) do
    binary_search(comp, stock, cost, budget, 0, 2_000_000_000)
  end

  defp binary_search(_comp, _stock, _cost, _budget, low, high) when low >= high, do: low

  defp binary_search(comp, stock, cost, budget, low, high) do
    mid = div(low + high + 1, 2)

    if feasible?(mid, comp, stock, cost, budget) do
      binary_search(comp, stock, cost, budget, mid, high)
    else
      binary_search(comp, stock, cost, budget, low, mid - 1)
    end
  end

  defp feasible?(x, comp, stock, cost, budget) do
    total_cost =
      Enum.reduce(0..(length(comp) - 1), 0, fn idx, acc ->
        need = x * Enum.at(comp, idx)
        have = Enum.at(stock, idx)
        buy = if need > have, do: need - have, else: 0
        acc + buy * Enum.at(cost, idx)
      end)

    total_cost <= budget
  end
end
```
