# 3026. Maximum Good Subarray Sum

## Cpp

```cpp
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_map<long long, long long> minPref;
        long long pref = 0;
        long long ans = LLONG_MIN;
        bool found = false;
        for (int i = 0; i < (int)nums.size(); ++i) {
            pref += nums[i]; // prefix sum up to index i (inclusive)
            long long target1 = (long long)nums[i] - k;
            auto it1 = minPref.find(target1);
            if (it1 != minPref.end()) {
                ans = max(ans, pref - it1->second);
                found = true;
            }
            long long target2 = (long long)nums[i] + k;
            auto it2 = minPref.find(target2);
            if (it2 != minPref.end()) {
                ans = max(ans, pref - it2->second);
                found = true;
            }
            // store current element as potential start for future subarrays
            long long startPref = pref - nums[i]; // prefix sum before index i
            auto it = minPref.find(nums[i]);
            if (it == minPref.end() || startPref < it->second) {
                minPref[nums[i]] = startPref;
            }
        }
        return found ? ans : 0LL;
    }
};
```

## Java

```java
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        java.util.HashMap<Integer, Long> minPrefix = new java.util.HashMap<>();
        long prefix = 0L;
        long best = Long.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            long curPref = prefix + nums[i]; // P[i+1]

            int needMinus = nums[i] - k;
            Long minValMinus = minPrefix.get(needMinus);
            if (minValMinus != null) {
                best = Math.max(best, curPref - minValMinus);
            }

            int needPlus = nums[i] + k;
            Long minValPlus = minPrefix.get(needPlus);
            if (minValPlus != null) {
                best = Math.max(best, curPref - minValPlus);
            }

            // store current value as potential start with prefix sum before this index
            int curVal = nums[i];
            minPrefix.compute(curVal, (key, val) -> val == null ? prefix : Math.min(val, prefix));

            prefix = curPref;
        }

        return best == Long.MIN_VALUE ? 0L : best;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_prefix = {}
        pref = 0
        best = None

        for v in nums:
            cur_pref = pref + v  # prefix sum up to current index inclusive

            t1 = v - k
            if t1 in min_prefix:
                cand = cur_pref - min_prefix[t1]
                if best is None or cand > best:
                    best = cand

            t2 = v + k
            if t2 in min_prefix:
                cand = cur_pref - min_prefix[t2]
                if best is None or cand > best:
                    best = cand

            # store minimal prefix sum before this index for value v
            if v not in min_prefix or pref < min_prefix[v]:
                min_prefix[v] = pref

            pref = cur_pref

        return 0 if best is None else best
```

## Python3

```python
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        min_pref = {}
        pref = 0
        ans = None
        for val in nums:
            pref += val
            # possible starting values that make a good subarray ending here
            for target in (val - k, val + k):
                if target in min_pref:
                    cand = pref - min_pref[target]
                    if ans is None or cand > ans:
                        ans = cand
            start_pref = pref - val  # prefix sum before current index
            if val not in min_pref or start_pref < min_pref[val]:
                min_pref[val] = start_pref
        return 0 if ans is None else ans
```

## C

```c
#include <stddef.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long key;
    long long val;
    char used;
} Entry;

static size_t hash_idx(long long key, size_t mask) {
    unsigned long long x = (unsigned long long)key;
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    x *= 0xc4ceb9fe1a85ec53ULL;
    x ^= x >> 33;
    return (size_t)x & mask;
}

static Entry* find_entry(Entry *table, size_t cap_mask, long long key) {
    size_t idx = hash_idx(key, cap_mask);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) & cap_mask;
    }
    return &table[idx];
}

long long maximumSubarraySum(int* nums, int numsSize, int k) {
    if (numsSize < 2) return 0;

    /* allocate hash table with power‑of‑two size */
    size_t cap = 1;
    while (cap <= (size_t)numsSize * 4) cap <<= 1;   // enough space
    Entry *table = (Entry *)calloc(cap, sizeof(Entry));
    size_t mask = cap - 1;

    long long bestAns = LLONG_MIN;
    int found = 0;

    long long pref = 0;          // prefix sum up to previous element

    for (int i = 0; i < numsSize; ++i) {
        long long cur = (long long)nums[i];
        long long newPref = pref + cur;   // prefix sum including current

        /* check possible starts with value cur - k and cur + k */
        long long targets[2] = {cur - (long long)k, cur + (long long)k};
        for (int t = 0; t < 2; ++t) {
            Entry *e = find_entry(table, mask, targets[t]);
            if (e->used && e->key == targets[t]) {
                long long cand = newPref - e->val;
                if (!found || cand > bestAns) bestAns = cand;
                found = 1;
            }
        }

        /* store current element as potential start for future subarrays */
        Entry *ecur = find_entry(table, mask, cur);
        if (!ecur->used) {
            ecur->used = 1;
            ecur->key = cur;
            ecur->val = pref;               // prefix before this index
        } else if (pref < ecur->val) {
            ecur->val = pref;               // keep minimal prefix sum
        }

        pref = newPref;
    }

    free(table);
    return found ? bestAns : 0;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        var minPref = new Dictionary<long, long>();
        long curPref = 0;
        long best = long.MinValue;

        for (int i = 0; i < nums.Length; i++) {
            long prefBefore = curPref;
            curPref += nums[i];
            long val = nums[i];

            // Check target where first element is val - k
            long target1 = val - k;
            if (minPref.TryGetValue(target1, out long minSum1)) {
                long candidate = curPref - minSum1;
                if (candidate > best) best = candidate;
            }

            // Check target where first element is val + k
            long target2 = val + k;
            if (minPref.TryGetValue(target2, out long minSum2)) {
                long candidate = curPref - minSum2;
                if (candidate > best) best = candidate;
            }

            // Store current value as possible start for future subarrays
            if (!minPref.ContainsKey(val) || prefBefore < minPref[val]) {
                minPref[val] = prefBefore;
            }
        }

        return best == long.MinValue ? 0L : best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    const minPrefByVal = new Map(); // value -> minimal prefix sum before this index
    let pref = 0; // prefix sum up to current index inclusive
    let ans = Number.NEGATIVE_INFINITY;
    
    for (let i = 0; i < nums.length; i++) {
        pref += nums[i];
        
        const target1 = nums[i] - k;
        if (minPrefByVal.has(target1)) {
            const candidate = pref - minPrefByVal.get(target1);
            if (candidate > ans) ans = candidate;
        }
        const target2 = nums[i] + k;
        if (minPrefByVal.has(target2)) {
            const candidate = pref - minPrefByVal.get(target2);
            if (candidate > ans) ans = candidate;
        }
        
        // prefix sum before this index i (i.e., sum of elements before i)
        const startPref = pref - nums[i];
        if (!minPrefByVal.has(nums[i]) || startPref < minPrefByVal.get(nums[i])) {
            minPrefByVal.set(nums[i], startPref);
        }
    }
    
    return ans === Number.NEGATIVE_INFINITY ? 0 : ans;
};
```

## Typescript

```typescript
function maximumSubarraySum(nums: number[], k: number): number {
    const minPref = new Map<number, number>();
    let pref = 0;
    let best = Number.NEGATIVE_INFINITY;

    for (let i = 0; i < nums.length; ++i) {
        const val = nums[i];
        const curPref = pref + val;

        const t1 = val - k;
        if (minPref.has(t1)) {
            const cand = curPref - minPref.get(t1)!;
            if (cand > best) best = cand;
        }

        const t2 = val + k;
        if (minPref.has(t2)) {
            const cand = curPref - minPref.get(t2)!;
            if (cand > best) best = cand;
        }

        if (!minPref.has(val) || pref < minPref.get(val)!) {
            minPref.set(val, pref);
        }

        pref = curPref;
    }

    return best === Number.NEGATIVE_INFINITY ? 0 : best;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumSubarraySum($nums, $k) {
        $pref = 0;
        $ans = PHP_INT_MIN;
        $map = [];
        foreach ($nums as $val) {
            $pref += $val; // prefix sum up to current index inclusive

            $t1 = $val - $k;
            if (array_key_exists($t1, $map)) {
                $candidate = $pref - $map[$t1];
                if ($candidate > $ans) {
                    $ans = $candidate;
                }
            }

            $t2 = $val + $k;
            if (array_key_exists($t2, $map)) {
                $candidate = $pref - $map[$t2];
                if ($candidate > $ans) {
                    $ans = $candidate;
                }
            }

            // store the prefix sum before this element for future subarrays
            $prefBefore = $pref - $val;
            if (!array_key_exists($val, $map) || $prefBefore < $map[$val]) {
                $map[$val] = $prefBefore;
            }
        }
        return $ans === PHP_INT_MIN ? 0 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        var minPrefixByValue = [Int: Int]()
        var prefix = 0
        var best = Int.min
        var found = false
        
        for num in nums {
            let target1 = num + k
            if let minPref = minPrefixByValue[target1] {
                let candidate = prefix + num - minPref
                if !found || candidate > best {
                    best = candidate
                    found = true
                }
            }
            let target2 = num - k
            if let minPref = minPrefixByValue[target2] {
                let candidate = prefix + num - minPref
                if !found || candidate > best {
                    best = candidate
                    found = true
                }
            }
            
            if let existing = minPrefixByValue[num] {
                if prefix < existing {
                    minPrefixByValue[num] = prefix
                }
            } else {
                minPrefixByValue[num] = prefix
            }
            
            prefix += num
        }
        
        return found ? best : 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSubarraySum(nums: IntArray, k: Int): Long {
        val minPrefixByValue = HashMap<Int, Long>()
        var prefix = 0L
        var best = Long.MIN_VALUE

        for (value in nums) {
            // Check subarrays ending at current index with first element value - k or value + k
            val target1 = value - k
            minPrefixByValue[target1]?.let { startPref ->
                val sum = prefix + value.toLong() - startPref
                if (sum > best) best = sum
            }
            val target2 = value + k
            minPrefixByValue[target2]?.let { startPref ->
                val sum = prefix + value.toLong() - startPref
                if (sum > best) best = sum
            }

            // Record current index as a possible start for future subarrays
            val existing = minPrefixByValue[value]
            if (existing == null || prefix < existing) {
                minPrefixByValue[value] = prefix
            }

            prefix += value.toLong()
        }
        return if (best == Long.MIN_VALUE) 0L else best
    }
}
```

## Dart

```dart
class Solution {
  int maximumSubarraySum(List<int> nums, int k) {
    Map<int, int> best = {};
    int pref = 0;
    int? ans;

    for (int val in nums) {
      // Check subarrays ending at current index
      int target1 = val - k;
      if (best.containsKey(target1)) {
        int cand = pref + val - best[target1]!;
        if (ans == null || cand > ans) ans = cand;
      }
      int target2 = val + k;
      if (best.containsKey(target2)) {
        int cand = pref + val - best[target2]!;
        if (ans == null || cand > ans) ans = cand;
      }

      // Store current value as potential start of future subarrays
      if (!best.containsKey(val) || pref < best[val]!) {
        best[val] = pref;
      }

      pref += val;
    }

    return ans ?? 0;
  }
}
```

## Golang

```go
package main

import "math"

func maximumSubarraySum(nums []int, k int) int64 {
    prefix := int64(0)
    best := int64(0)
    found := false
    minPref := make(map[int]int64)

    for _, v := range nums {
        newPrefix := prefix + int64(v)

        if p, ok := minPref[v+k]; ok {
            cand := newPrefix - p
            if !found || cand > best {
                best = cand
                found = true
            }
        }
        if p, ok := minPref[v-k]; ok {
            cand := newPrefix - p
            if !found || cand > best {
                best = cand
                found = true
            }
        }

        if old, ok := minPref[v]; !ok || prefix < old {
            minPref[v] = prefix
        }

        prefix = newPrefix
    }

    if !found {
        return 0
    }
    // Ensure result fits within int64 range (it always does given constraints)
    if best > math.MaxInt64 {
        return math.MaxInt64
    }
    if best < math.MinInt64 {
        return math.MinInt64
    }
    return best
}
```

## Ruby

```ruby
def maximum_subarray_sum(nums, k)
  pref_min = {}
  pre = 0
  max_sum = nil

  nums.each do |val|
    pref_end = pre + val

    t1 = val - k
    if pref_min.key?(t1)
      cur = pref_end - pref_min[t1]
      max_sum = cur if max_sum.nil? || cur > max_sum
    end

    t2 = val + k
    if pref_min.key?(t2)
      cur = pref_end - pref_min[t2]
      max_sum = cur if max_sum.nil? || cur > max_sum
    end

    if !pref_min.key?(val) || pre < pref_min[val]
      pref_min[val] = pre
    end

    pre = pref_end
  end

  max_sum ? max_sum : 0
end
```

## Scala

```scala
object Solution {
    def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
        import scala.collection.mutable
        val minPref = mutable.HashMap[Int, Long]()
        var pref: Long = 0L
        var ans: Long = Long.MinValue

        for (num <- nums) {
            val prefBefore = pref
            val prefAfter = prefBefore + num.toLong

            // Check subarrays ending at current index with required start values
            val need1 = num - k
            minPref.get(need1).foreach { mp =>
                val cand = prefAfter - mp
                if (cand > ans) ans = cand
            }
            if (k != 0) {
                val need2 = num + k
                minPref.get(need2).foreach { mp =>
                    val cand = prefAfter - mp
                    if (cand > ans) ans = cand
                }
            }

            // Update map with current value as potential start for future subarrays
            val curMin = minPref.getOrElse(num, Long.MaxValue)
            if (prefBefore < curMin) {
                minPref.update(num, prefBefore)
            }

            pref = prefAfter
        }

        if (ans == Long.MinValue) 0L else ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut pref: i64 = 0;
        let mut best_start: HashMap<i32, i64> = HashMap::new(); // value -> minimal prefix sum before it
        let mut ans: i64 = i64::MIN;

        for &val in nums.iter() {
            let pref_end = pref + val as i64;

            // check both possible start values
            let targets = [val.wrapping_sub(k), val.wrapping_add(k)];
            for &t in targets.iter() {
                if let Some(&min_pref) = best_start.get(&t) {
                    let candidate = pref_end - min_pref;
                    if candidate > ans {
                        ans = candidate;
                    }
                }
            }

            // store current value with prefix sum before this element
            match best_start.entry(val) {
                std::collections::hash_map::Entry::Occupied(mut e) => {
                    if pref < *e.get() {
                        e.insert(pref);
                    }
                }
                std::collections::hash_map::Entry::Vacant(e) => {
                    e.insert(pref);
                }
            }

            pref = pref_end;
        }

        if ans == i64::MIN { 0 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (maximum-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (hash (make-hash))
         (loop
          (lambda (idx pref best)
            (if (= idx n)
                (if best best 0)
                (let* ((val (list-ref nums idx))
                       (new-pref (+ pref val))
                       (cand1 (hash-ref hash (- val k) #f))
                       (cand2 (hash-ref hash (+ val k) #f))
                       (best-after
                        (let ((candidate best))
                          (for/fold ([candidate candidate]) ([c (in-list (list cand1 cand2))])
                            (if c
                                (let ((sum (- new-pref c)))
                                  (if (or (not candidate) (> sum candidate)) sum candidate))
                                candidate)))))
                  ;; update hashmap for current value with minimal prefix before it
                  (let ((existing (hash-ref hash val #f)))
                    (if existing
                        (when (< pref existing)
                          (hash-set! hash val pref))
                        (hash-set! hash val pref)))
                  (loop (+ idx 1) new-pref best-after))))))
    (loop 0 0 #f)))
```

## Erlang

```erlang
-spec maximum_subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
maximum_subarray_sum(Nums, K) ->
    case loop(Nums, K, 0, #{}, undefined) of
        undefined -> 0;
        Ans -> Ans
    end.

loop([], _K, _Pref, _Map, MaxAns) ->
    MaxAns;
loop([Num | Rest], K, Pref, Map, MaxAns) ->
    Cand1 = maps:get(Num - K, Map, undefined),
    Max1 = case Cand1 of
        undefined -> MaxAns;
        MinPrefStart ->
            Sum = Pref + Num - MinPrefStart,
            max_val(MaxAns, Sum)
    end,
    Cand2 = maps:get(Num + K, Map, undefined),
    Max2 = case Cand2 of
        undefined -> Max1;
        MinPrefStart2 ->
            Sum2 = Pref + Num - MinPrefStart2,
            max_val(Max1, Sum2)
    end,
    Existing = maps:get(Num, Map, undefined),
    NewMap = case Existing of
        undefined -> maps:put(Num, Pref, Map);
        Prev when Prev > Pref -> maps:put(Num, Pref, Map);
        _ -> Map
    end,
    loop(Rest, K, Pref + Num, NewMap, Max2).

max_val(undefined, X) -> X;
max_val(X, undefined) -> X;
max_val(A, B) when A >= B -> A;
max_val(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_subarray_sum(nums :: [integer], k :: integer) :: integer
  def maximum_subarray_sum(nums, k) do
    {best, _} =
      Enum.reduce(nums, {nil, %{pref: 0, map: %{} }}, fn x, {cur_best, state} ->
        pref_before = state.pref
        new_pref = pref_before + x

        cur_best =
          [x - k, x + k]
          |> Enum.reduce(cur_best, fn v, acc ->
            case Map.get(state.map, v) do
              nil -> acc
              start_pref ->
                sum = new_pref - start_pref
                case acc do
                  nil -> sum
                  _ when sum > acc -> sum
                  _ -> acc
                end
            end
          end)

        updated_map =
          case Map.get(state.map, x) do
            nil -> Map.put(state.map, x, pref_before)
            existing when pref_before < existing -> Map.put(state.map, x, pref_before)
            _ -> state.map
          end

        {cur_best, %{pref: new_pref, map: updated_map}}
      end)

    case best do
      nil -> 0
      _ -> best
    end
  end
end
```
