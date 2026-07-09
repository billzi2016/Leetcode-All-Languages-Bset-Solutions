# 2561. Rearranging Fruits

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        unordered_map<long long, int> diff;
        diff.reserve(basket1.size() * 2);
        long long globalMin = LLONG_MAX;
        
        for (int v : basket1) {
            ++diff[v];
            if (v < globalMin) globalMin = v;
        }
        for (int v : basket2) {
            --diff[v];
            if (v < globalMin) globalMin = v;
        }
        
        vector<long long> excess;
        excess.reserve(basket1.size());
        for (auto &p : diff) {
            int d = p.second;
            if ((abs(d) & 1)) return -1; // odd total count -> impossible
            int need = abs(d) / 2;
            for (int i = 0; i < need; ++i) excess.push_back(p.first);
        }
        
        sort(excess.begin(), excess.end());
        long long ans = 0;
        size_t k = excess.size();
        for (size_t i = 0; i < k / 2; ++i) {
            ans += min(excess[i], 2LL * globalMin);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minCost(int[] basket1, int[] basket2) {
        java.util.HashMap<Integer, Integer> freq1 = new java.util.HashMap<>();
        java.util.HashMap<Integer, Integer> freq2 = new java.util.HashMap<>();
        int globalMin = Integer.MAX_VALUE;
        for (int v : basket1) {
            freq1.put(v, freq1.getOrDefault(v, 0) + 1);
            if (v < globalMin) globalMin = v;
        }
        for (int v : basket2) {
            freq2.put(v, freq2.getOrDefault(v, 0) + 1);
            if (v < globalMin) globalMin = v;
        }

        java.util.HashSet<Integer> allKeys = new java.util.HashSet<>(freq1.keySet());
        allKeys.addAll(freq2.keySet());

        java.util.ArrayList<Integer> extra = new java.util.ArrayList<>();
        for (int key : allKeys) {
            int c1 = freq1.getOrDefault(key, 0);
            int c2 = freq2.getOrDefault(key, 0);
            int total = c1 + c2;
            if ((total & 1) == 1) {
                return -1L;
            }
            int diff = c1 - c2;
            if (diff > 0) {
                int times = diff / 2;
                for (int i = 0; i < times; ++i) extra.add(key);
            } else if (diff < 0) {
                int times = (-diff) / 2;
                for (int i = 0; i < times; ++i) extra.add(key);
            }
        }

        java.util.Collections.sort(extra);
        long result = 0L;
        int half = extra.size() / 2;
        long viaMinCost = 2L * globalMin;
        for (int i = 0; i < half; ++i) {
            int val = extra.get(i);
            result += Math.min((long) val, viaMinCost);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        from collections import Counter

        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)

        # overall minimum element across both baskets
        min_elem = min(min(basket1), min(basket2))

        excess = []

        all_keys = set(cnt1.keys()) | set(cnt2.keys())
        for x in all_keys:
            total = cnt1.get(x, 0) + cnt2.get(x, 0)
            if total & 1:   # odd total -> impossible
                return -1
            diff = cnt1.get(x, 0) - cnt2.get(x, 0)
            if diff > 0:
                excess.extend([x] * (diff // 2))
            elif diff < 0:
                excess.extend([x] * ((-diff) // 2))

        excess.sort()
        swaps = len(excess) // 2
        cost = 0
        for i in range(swaps):
            cost += min(excess[i], 2 * min_elem)
        return cost
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)

        all_vals = set(cnt1) | set(cnt2)

        # Check feasibility
        for v in all_vals:
            if (cnt1[v] + cnt2[v]) & 1:
                return -1

        need = []
        for v in all_vals:
            diff = cnt1[v] - cnt2[v]
            if diff > 0:
                need.extend([v] * (diff // 2))
            elif diff < 0:
                need.extend([v] * ((-diff) // 2))

        if not need:
            return 0

        need.sort()
        global_min = min(min(basket1), min(basket2))
        half = len(need) // 2
        total = 0
        for i in range(half):
            total += min(need[i], 2 * global_min)
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

long long minCost(int* basket1, int basket1Size, int* basket2, int basket2Size) {
    int n = basket1Size;
    if (n == 0) return 0LL;

    /* global minimum element */
    int global_min = basket1[0];
    for (int i = 1; i < n; ++i)
        if (basket1[i] < global_min) global_min = basket1[i];
    for (int i = 0; i < n; ++i)
        if (basket2[i] < global_min) global_min = basket2[i];

    /* parity check: each value must appear even number of times in total */
    int total = 2 * n;
    int *combined = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < n; ++i) combined[i] = basket1[i];
    for (int i = 0; i < n; ++i) combined[n + i] = basket2[i];

    qsort(combined, total, sizeof(int), cmp_int);
    for (int i = 0; i < total; ) {
        int j = i + 1;
        while (j < total && combined[j] == combined[i]) ++j;
        if ((j - i) & 1) {               /* odd count */
            free(combined);
            return -1LL;
        }
        i = j;
    }

    /* sort individual baskets */
    qsort(basket1, n, sizeof(int), cmp_int);
    qsort(basket2, n, sizeof(int), cmp_int);

    /* collect surplus elements */
    int *extra = (int *)malloc(total * sizeof(int));
    int extraCnt = 0;
    int i = 0, j = 0;
    while (i < n && j < n) {
        if (basket1[i] == basket2[j]) {
            ++i; ++j;
        } else if (basket1[i] < basket2[j]) {
            extra[extraCnt++] = basket1[i++];
        } else {
            extra[extraCnt++] = basket2[j++];
        }
    }
    while (i < n) extra[extraCnt++] = basket1[i++];
    while (j < n) extra[extraCnt++] = basket2[j++];

    if (extraCnt & 1) {   /* should not happen if parity check passed */
        free(combined);
        free(extra);
        return -1LL;
    }

    qsort(extra, extraCnt, sizeof(int), cmp_int);

    long long result = 0;
    long long minAll = (long long)global_min;
    for (int k = 0; k < extraCnt / 2; ++k) {
        long long val = (long long)extra[k];
        long long cost = val < 2 * minAll ? val : 2 * minAll;
        result += cost;
    }

    free(combined);
    free(extra);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long MinCost(int[] basket1, int[] basket2) {
        var diff = new Dictionary<int, int>();
        foreach (int x in basket1) {
            if (!diff.ContainsKey(x)) diff[x] = 0;
            diff[x]++;
        }
        foreach (int x in basket2) {
            if (!diff.ContainsKey(x)) diff[x] = 0;
            diff[x]--;
        }

        int minAll = int.MaxValue;
        foreach (int v in basket1) if (v < minAll) minAll = v;
        foreach (int v in basket2) if (v < minAll) minAll = v;

        var excess = new List<int>();
        foreach (var kvp in diff) {
            int d = kvp.Value;
            if ((d & 1) != 0) return -1; // odd total count, impossible
            int times = Math.Abs(d) / 2;
            for (int i = 0; i < times; i++) {
                excess.Add(kvp.Key);
            }
        }

        excess.Sort();
        long result = 0;
        int half = excess.Count / 2;
        for (int i = 0; i < half; i++) {
            int val = excess[i];
            result += Math.Min((long)val, 2L * minAll);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} basket1
 * @param {number[]} basket2
 * @return {number}
 */
var minCost = function(basket1, basket2) {
    const cnt1 = new Map();
    for (const v of basket1) cnt1.set(v, (cnt1.get(v) || 0) + 1);
    const cnt2 = new Map();
    for (const v of basket2) cnt2.set(v, (cnt2.get(v) || 0) + 1);

    let globalMin = Infinity;
    for (const v of basket1) if (v < globalMin) globalMin = v;
    for (const v of basket2) if (v < globalMin) globalMin = v;

    const extra = [];
    const keys = new Set([...cnt1.keys(), ...cnt2.keys()]);
    for (const key of keys) {
        const c1 = cnt1.get(key) || 0;
        const c2 = cnt2.get(key) || 0;
        const total = c1 + c2;
        if (total % 2 !== 0) return -1;
        const diff = c1 - c2;
        if (diff > 0) {
            const times = diff / 2;
            for (let i = 0; i < times; ++i) extra.push(key);
        } else if (diff < 0) {
            const times = (-diff) / 2;
            for (let i = 0; i < times; ++i) extra.push(key);
        }
    }

    extra.sort((a, b) => a - b);
    let ans = 0;
    const half = extra.length >> 1;
    const twoMin = 2 * globalMin;
    for (let i = 0; i < half; ++i) {
        ans += Math.min(extra[i], twoMin);
    }
    return ans;
};
```

## Typescript

```typescript
function minCost(basket1: number[], basket2: number[]): number {
    const cnt1 = new Map<number, number>();
    const cnt2 = new Map<number, number>();
    let globalMin = Number.MAX_SAFE_INTEGER;

    for (const v of basket1) {
        globalMin = Math.min(globalMin, v);
        cnt1.set(v, (cnt1.get(v) ?? 0) + 1);
    }
    for (const v of basket2) {
        globalMin = Math.min(globalMin, v);
        cnt2.set(v, (cnt2.get(v) ?? 0) + 1);
    }

    const allKeys = new Set<number>([...cnt1.keys(), ...cnt2.keys()]);
    const excess: number[] = [];

    for (const key of allKeys) {
        const c1 = cnt1.get(key) ?? 0;
        const c2 = cnt2.get(key) ?? 0;
        const total = c1 + c2;
        if (total % 2 !== 0) return -1;

        const diff = c1 - c2; // positive => surplus in basket1
        if (diff > 0) {
            const times = diff / 2;
            for (let i = 0; i < times; ++i) excess.push(key);
        } else if (diff < 0) {
            const times = (-diff) / 2;
            for (let i = 0; i < times; ++i) excess.push(key);
        }
    }

    excess.sort((a, b) => a - b);
    const swaps = excess.length >> 1; // divide by 2
    let cost = 0;
    const doubleMin = 2 * globalMin;

    for (let i = 0; i < swaps; ++i) {
        const val = excess[i];
        cost += Math.min(val, doubleMin);
    }

    return cost;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $basket1
     * @param Integer[] $basket2
     * @return Integer
     */
    function minCost($basket1, $basket2) {
        $cnt = [];
        foreach ($basket1 as $v) {
            if (!isset($cnt[$v])) {
                $cnt[$v] = [0, 0];
            }
            $cnt[$v][0]++;
        }
        foreach ($basket2 as $v) {
            if (!isset($cnt[$v])) {
                $cnt[$v] = [0, 0];
            }
            $cnt[$v][1]++;
        }

        // global minimum element across both baskets
        $globalMin = PHP_INT_MAX;
        foreach (array_merge($basket1, $basket2) as $v) {
            if ($v < $globalMin) {
                $globalMin = $v;
            }
        }

        $excess = [];

        foreach ($cnt as $val => $pair) {
            $total = $pair[0] + $pair[1];
            if (($total & 1) == 1) { // odd total -> impossible
                return -1;
            }
            $diff = $pair[0] - $pair[1];
            if ($diff > 0) {
                $times = intdiv($diff, 2);
                for ($i = 0; $i < $times; $i++) {
                    $excess[] = (int)$val;
                }
            } elseif ($diff < 0) {
                $times = intdiv(-$diff, 2);
                for ($i = 0; $i < $times; $i++) {
                    $excess[] = (int)$val;
                }
            }
        }

        sort($excess, SORT_NUMERIC);

        $m = count($excess);
        $ans = 0;
        $half = intdiv($m, 2);
        $doubleMin = $globalMin * 2;

        for ($i = 0; $i < $half; $i++) {
            $ans += min($excess[$i], $doubleMin);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ basket1: [Int], _ basket2: [Int]) -> Int {
        var cnt1 = [Int:Int]()
        var cnt2 = [Int:Int]()
        var globalMin = Int.max
        
        for v in basket1 {
            cnt1[v, default: 0] += 1
            if v < globalMin { globalMin = v }
        }
        for v in basket2 {
            cnt2[v, default: 0] += 1
            if v < globalMin { globalMin = v }
        }
        
        var need = [Int]()
        let allKeys = Set(cnt1.keys).union(cnt2.keys)
        for key in allKeys {
            let c1 = cnt1[key] ?? 0
            let c2 = cnt2[key] ?? 0
            if (c1 + c2) % 2 != 0 { return -1 }
            if c1 > c2 {
                let diff = (c1 - c2) / 2
                need.append(contentsOf: repeatElement(key, count: diff))
            }
        }
        
        need.sort()
        let half = need.count / 2
        var totalCost: Int64 = 0
        let indirectCost = Int64(2 * globalMin)
        for i in 0..<half {
            let x = need[i]
            totalCost += min(Int64(x), indirectCost)
        }
        return Int(totalCost)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(basket1: IntArray, basket2: IntArray): Long {
        val cnt1 = HashMap<Int, Int>()
        val cnt2 = HashMap<Int, Int>()
        var globalMin = Int.MAX_VALUE

        for (v in basket1) {
            cnt1[v] = (cnt1[v] ?: 0) + 1
            if (v < globalMin) globalMin = v
        }
        for (v in basket2) {
            cnt2[v] = (cnt2[v] ?: 0) + 1
            if (v < globalMin) globalMin = v
        }

        val allKeys = HashSet<Int>()
        allKeys.addAll(cnt1.keys)
        allKeys.addAll(cnt2.keys)

        val excess = ArrayList<Int>()

        for (key in allKeys) {
            val c1 = cnt1.getOrDefault(key, 0)
            val c2 = cnt2.getOrDefault(key, 0)
            val total = c1 + c2
            if ((total and 1) == 1) return -1L

            val diff = c1 - c2
            if (diff > 0) {
                repeat(diff / 2) { excess.add(key) }
            } else if (diff < 0) {
                repeat((-diff) / 2) { excess.add(key) }
            }
        }

        excess.sort()
        var result = 0L
        val half = excess.size / 2
        for (i in 0 until half) {
            val x = excess[i]
            result += minOf(x.toLong(), 2L * globalMin)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> basket1, List<int> basket2) {
    // Global minimum element across both baskets
    int globalMin = basket1.isNotEmpty ? basket1[0] : 0;
    for (int v in basket1) {
      if (v < globalMin) globalMin = v;
    }
    for (int v in basket2) {
      if (v < globalMin) globalMin = v;
    }

    // Difference map: count in basket1 minus count in basket2
    final Map<int, int> diff = {};
    for (int v in basket1) {
      diff[v] = (diff[v] ?? 0) + 1;
    }
    for (int v in basket2) {
      diff[v] = (diff[v] ?? 0) - 1;
    }

    // Collect excess elements that need to move from basket1 to basket2
    final List<int> excess = [];
    for (var entry in diff.entries) {
      int d = entry.value;
      if ((d.abs() & 1) == 1) return -1; // odd total count -> impossible
      if (d > 0) {
        int times = d ~/ 2;
        for (int i = 0; i < times; ++i) {
          excess.add(entry.key);
        }
      }
    }

    excess.sort();
    int m = excess.length ~/ 2;
    int total = 0;
    int twoMin = 2 * globalMin;
    for (int i = 0; i < m; ++i) {
      int val = excess[i];
      total += (val < twoMin) ? val : twoMin;
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func minCost(basket1 []int, basket2 []int) int64 {
    freq := make(map[int]int)
    const maxInt = int(^uint(0) >> 1)
    minVal := maxInt

    for _, v := range basket1 {
        freq[v]++
        if v < minVal {
            minVal = v
        }
    }
    for _, v := range basket2 {
        freq[v]--
        if v < minVal {
            minVal = v
        }
    }

    need := make([]int, 0)
    for val, diff := range freq {
        if diff%2 != 0 {
            return -1
        }
        cnt := diff / 2 // positive means excess in basket1, negative excess in basket2
        if cnt > 0 {
            for i := 0; i < cnt; i++ {
                need = append(need, val)
            }
        } else if cnt < 0 {
            for i := 0; i < -cnt; i++ {
                need = append(need, val)
            }
        }
    }

    if len(need) == 0 {
        return 0
    }

    sort.Ints(need)

    total := int64(0)
    m2 := 2 * minVal
    half := len(need) / 2
    for i := 0; i < half; i++ {
        x := need[i]
        if x < m2 {
            total += int64(x)
        } else {
            total += int64(m2)
        }
    }

    return total
}
```

## Ruby

```ruby
def min_cost(basket1, basket2)
  freq1 = Hash.new(0)
  freq2 = Hash.new(0)

  basket1.each { |v| freq1[v] += 1 }
  basket2.each { |v| freq2[v] += 1 }

  global_min = (basket1 + basket2).min

  need = []

  (freq1.keys | freq2.keys).each do |val|
    total = freq1[val] + freq2[val]
    return -1 if total.odd?

    diff = freq1[val] - freq2[val]
    if diff > 0
      (diff / 2).times { need << val }
    elsif diff < 0
      (-diff / 2).times { need << val }
    end
  end

  need.sort!
  half = need.size / 2
  cost = 0
  (0...half).each do |i|
    cost += [need[i], 2 * global_min].min
  end
  cost
end
```

## Scala

```scala
object Solution {
  def minCost(basket1: Array[Int], basket2: Array[Int]): Long = {
    import scala.collection.mutable.{HashMap, ArrayBuffer}
    val map1 = HashMap[Int, Int]().withDefaultValue(0)
    val map2 = HashMap[Int, Int]().withDefaultValue(0)
    var globalMin = Int.MaxValue

    for (v <- basket1) {
      map1(v) = map1(v) + 1
      if (v < globalMin) globalMin = v
    }
    for (v <- basket2) {
      map2(v) = map2(v) + 1
      if (v < globalMin) globalMin = v
    }

    val excess = ArrayBuffer[Int]()
    val allKeys = map1.keySet ++ map2.keySet

    for (key <- allKeys) {
      val c1 = map1.getOrElse(key, 0)
      val c2 = map2.getOrElse(key, 0)
      val total = c1 + c2
      if ((total & 1) == 1) return -1L
      val diff = c1 - c2
      if (diff > 0) {
        var times = diff / 2
        while (times > 0) {
          excess += key
          times -= 1
        }
      } else if (diff < 0) {
        var times = (-diff) / 2
        while (times > 0) {
          excess += key
          times -= 1
        }
      }
    }

    if (excess.isEmpty) return 0L

    val sorted = excess.sorted
    val m = globalMin.toLong
    var cost: Long = 0L
    val half = sorted.length / 2
    for (i <- 0 until half) {
      val x = sorted(i).toLong
      cost += Math.min(x, 2 * m)
    }
    cost
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let mut diff: HashMap<i32, i64> = HashMap::new();
        let mut global_min = i32::MAX;

        for &v in &basket1 {
            *diff.entry(v).or_insert(0) += 1;
            if v < global_min {
                global_min = v;
            }
        }
        for &v in &basket2 {
            *diff.entry(v).or_insert(0) -= 1;
            if v < global_min {
                global_min = v;
            }
        }

        let mut excess: Vec<i32> = Vec::new();

        for (&val, &d) in diff.iter() {
            if d % 2 != 0 {
                return -1i64;
            }
            let times = (d.abs() / 2) as usize;
            for _ in 0..times {
                excess.push(val);
            }
        }

        excess.sort_unstable();

        let half = excess.len() / 2;
        let min_global_i64 = global_min as i64;
        let mut cost: i64 = 0;
        for i in 0..half {
            let x = excess[i] as i64;
            cost += std::cmp::min(x, 2 * min_global_i64);
        }
        cost
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (min-cost basket1 basket2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((global-min (apply min (append basket1 basket2)))
         (diff (make-hash))
         (total (make-hash)))
    ;; count occurrences
    (for-each (lambda (x)
                (hash-set! diff x (+ 1 (hash-ref diff x 0)))
                (hash-set! total x (+ 1 (hash-ref total x 0))))
              basket1)
    (for-each (lambda (x)
                (hash-set! diff x (- (hash-ref diff x 0) 1))
                (hash-set! total x (+ 1 (hash-ref total x 0))))
              basket2)
    ;; build list of elements that need to be swapped
    (let ((invalid #f)
          (v '()))
      (hash-for-each
        (lambda (key cnt)
          (when (odd? cnt) (set! invalid #t))
          (let* ((d (abs (hash-ref diff key 0)))
                 (times (/ d 2)))
            (when (> times 0)
              (do ((i 0 (+ i 1))) ((= i times))
                (set! v (cons key v))))))
        total)
      (if invalid
          -1
          (let* ((sorted-v (sort v <))
                 (vec (list->vector sorted-v))
                 (len (vector-length vec))
                 (half (/ len 2))
                 (m global-min)
                 (ans (let loop ((i 0) (acc 0))
                        (if (= i half)
                            acc
                            (loop (+ i 1)
                                  (+ acc (min (vector-ref vec i) (* 2 m))))))))
            ans)))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/2]).

-spec min_cost(Basket1 :: [integer()], Basket2 :: [integer()]) -> integer().
min_cost(Basket1, Basket2) ->
    GlobalMin = lists:min(Basket1 ++ Basket2),
    DiffMap0 = maps:new(),
    DiffMap1 = update_counts(Basket1, 1, DiffMap0),
    DiffMap = update_counts(Basket2, -1, DiffMap1),
    case has_odd(DiffMap) of
        true -> -1;
        false ->
            NeedList = collect_need(maps:to_list(DiffMap), []),
            Sorted = lists:sort(NeedList),
            Half = length(Sorted) div 2,
            FirstHalf = lists:sublist(Sorted, Half),
            lists:foldl(fun(X, Acc) -> Acc + min(X, 2 * GlobalMin) end, 0, FirstHalf)
    end.

update_counts([], _Delta, Map) ->
    Map;
update_counts([H | T], Delta, Map) ->
    NewMap = maps:update_with(
        H,
        fun(V) -> V + Delta end,
        Delta,
        Map),
    update_counts(T, Delta, NewMap).

has_odd(Map) ->
    has_odd(maps:to_list(Map)).

has_odd([]) ->
    false;
has_odd([{_, V} | Rest]) ->
    case (abs(V) rem 2) of
        1 -> true;
        _ -> has_odd(Rest)
    end.

collect_need([], Acc) ->
    Acc;
collect_need([{Val, Diff} | Rest], Acc) ->
    Copies = abs(Diff) div 2,
    NewAcc = if
        Copies > 0 -> lists:duplicate(Copies, Val) ++ Acc;
        true -> Acc
    end,
    collect_need(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(basket1 :: [integer], basket2 :: [integer]) :: integer
  def min_cost(basket1, basket2) do
    # Build combined count map: value => {count_in_b1, count_in_b2}
    cnt =
      Enum.reduce(basket1, %{}, fn v, acc ->
        Map.update(acc, v, {1, 0}, fn {c1, c2} -> {c1 + 1, c2} end)
      end)

    cnt =
      Enum.reduce(basket2, cnt, fn v, acc ->
        Map.update(acc, v, {0, 1}, fn {c1, c2} -> {c1, c2 + 1} end)
      end)

    # Global minimum element across both baskets
    min_val = Enum.min(Enum.concat([basket1, basket2]))

    # Determine excess elements that need to be swapped
    {possible, extra_list} =
      Enum.reduce(cnt, {true, []}, fn {val, {c1, c2}}, {ok, list} ->
        total = c1 + c2

        if rem(total, 2) == 1 do
          {false, []}
        else
          diff = c1 - c2
          need = div(abs(diff), 2)

          new_list =
            if need > 0 do
              List.duplicate(val, need) ++ list
            else
              list
            end

          {ok, new_list}
        end
      end)

    if not possible do
      -1
    else
      sorted = Enum.sort(extra_list)
      half = div(length(sorted), 2)

      sorted
      |> Enum.take(half)
      |> Enum.reduce(0, fn v, acc -> acc + min(v, 2 * min_val) end)
    end
  end
end
```
