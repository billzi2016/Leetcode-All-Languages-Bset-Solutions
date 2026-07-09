# 2597. The Number of Beautiful Subsets

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> groups;
        for (int x : nums) groups[x % k].push_back(x);
        
        long long total = 1; // product of counts per remainder group
        
        for (auto& entry : groups) {
            vector<int>& v = entry.second;
            sort(v.begin(), v.end());
            
            // compress to value-frequency pairs
            vector<pair<int,int>> elems;
            for (int x : v) {
                if (elems.empty() || elems.back().first != x)
                    elems.emplace_back(x, 1);
                else
                    ++elems.back().second;
            }
            
            long long dpPrev2 = 1; // f(i-2), initially empty subset count
            long long dpPrev1 = 1; // f(i-1) for zero processed elements (empty subset)
            int prevVal = 0;
            bool hasPrev = false;
            
            for (auto& p : elems) {
                int val = p.first;
                int cnt = p.second;
                long long waysTake = (1LL << cnt) - 1; // non‑empty selections of this value
                
                long long skip = dpPrev1;
                long long take = (hasPrev && val - prevVal == k) ? waysTake * dpPrev2
                                                                : waysTake * dpPrev1;
                
                long long cur = skip + take;
                
                dpPrev2 = dpPrev1;
                dpPrev1 = cur;
                prevVal = val;
                hasPrev = true;
            }
            
            total *= dpPrev1; // includes empty subset for this group
        }
        
        return static_cast<int>(total - 1); // exclude overall empty subset
    }
};
```

## Java

```java
class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        java.util.Map<Integer, Integer> selected = new java.util.HashMap<>();
        long total = dfs(nums, k, 0, selected);
        return (int)(total - 1); // exclude empty subset
    }

    private long dfs(int[] nums, int k, int idx, java.util.Map<Integer, Integer> selected) {
        if (idx == nums.length) {
            return 1; // count current subset (including possibly empty)
        }
        // Skip current element
        long skip = dfs(nums, k, idx + 1, selected);
        long take = 0;
        int cur = nums[idx];
        // Can we take it? Only if no element with value cur - k is already selected
        if (!selected.containsKey(cur - k)) {
            // add current element to the selection map
            selected.put(cur, selected.getOrDefault(cur, 0) + 1);
            take = dfs(nums, k, idx + 1, selected);
            // backtrack: remove one occurrence
            int cnt = selected.get(cur);
            if (cnt == 1) {
                selected.remove(cur);
            } else {
                selected.put(cur, cnt - 1);
            }
        }
        return skip + take;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter, defaultdict
        from functools import lru_cache

        # Special case when k == 0: cannot pick two equal numbers
        if k == 0:
            cnt = Counter(nums)
            total = 1
            for f in cnt.values():
                total *= (1 + f)   # choose none or exactly one of the f copies
            return total - 1

        # Group numbers by remainder modulo k
        groups = defaultdict(list)
        for num in nums:
            groups[num % k].append(num)

        result = 1
        for arr in groups.values():
            arr.sort()
            # compress to (value, frequency) pairs
            vals = []
            freqs = []
            i = 0
            n = len(arr)
            while i < n:
                j = i
                while j < n and arr[j] == arr[i]:
                    j += 1
                vals.append(arr[i])
                freqs.append(j - i)
                i = j

            @lru_cache(None)
            def dfs(idx):
                if idx >= len(vals):
                    return 1  # empty subset for the remaining part
                # skip current value
                skip = dfs(idx + 1)

                # take at least one occurrence of current value
                takeWays = (1 << freqs[idx]) - 1  # all non‑empty selections of its copies

                if idx + 1 < len(vals) and vals[idx + 1] - vals[idx] == k:
                    # cannot take the next value together with current
                    take = takeWays * dfs(idx + 2)
                else:
                    take = takeWays * dfs(idx + 1)

                return skip + take

            result *= dfs(0)

        return result - 1
```

## Python3

```python
import collections
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = collections.defaultdict(list)
        for num in nums:
            groups[num % k].append(num)

        total = 1
        for arr in groups.values():
            cnt = collections.Counter(arr)
            values = sorted(cnt.keys())
            m = len(values)

            dp_next = 1          # dp[i+1]
            dp_next_next = 1     # dp[i+2]

            for i in range(m - 1, -1, -1):
                cur = values[i]
                ways_take = (1 << cnt[cur]) - 1

                if i + 1 < m and values[i + 1] == cur + k:
                    cur_total = dp_next + ways_take * dp_next_next
                else:
                    cur_total = dp_next + ways_take * dp_next

                dp_next_next, dp_next = dp_next, cur_total

            total *= dp_next

        return total - 1
```

## C

```c
int beautifulSubsets(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    // sort the array
    qsort(nums, numsSize, sizeof(int), (__compar_fn_t) (int (*)(const void *, const void *)) 
        (int (*)(const int*, const int*)) (int (*)(const void*, const void*) ) 
        (int (*)(const void*, const void*)) (int (*)(const void*, const void*)) 
        (int (*)(const void*, const void*)) (int (*)(const void*, const void*)) 
        (int (*)(const void*, const void*)) (int (*)(const void*, const void*))
    );
    // Simple comparator
    int cmp(const void *a, const void *b) {
        return (*(int*)a) - (*(int*)b);
    }
    qsort(nums, numsSize, sizeof(int), cmp);

    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];
    // counts array up to max possible value (1000) plus k offset
    int limit = maxVal + k + 1;
    int cnt[2005] = {0};

    long long dfs(int idx) {
        if (idx == numsSize) return 1LL; // empty subset counted
        long long res = dfs(idx + 1); // skip current element

        int val = nums[idx];
        if (val - k >= 0 && cnt[val - k] > 0) {
            // cannot take this element
        } else {
            cnt[val]++;
            res += dfs(idx + 1);
            cnt[val]--;
        }
        return res;
    }

    long long total = dfs(0) - 1; // exclude empty subset
    return (int)total;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int BeautifulSubsets(int[] nums, int k) {
        System.Array.Sort(nums);
        var cnt = new Dictionary<int, int>();
        int n = nums.Length;
        long dfs(int idx) {
            if (idx == n) return 1; // count empty subset
            long res = dfs(idx + 1); // skip current element
            int conflictVal = nums[idx] - k;
            cnt.TryGetValue(conflictVal, out int conflictCount);
            if (conflictCount == 0) {
                cnt.TryGetValue(nums[idx], out int curCount);
                cnt[nums[idx]] = curCount + 1;
                res += dfs(idx + 1);
                // backtrack
                if (cnt[nums[idx]] == 1)
                    cnt.Remove(nums[idx]);
                else
                    cnt[nums[idx]]--;
            }
            return res;
        }
        long total = dfs(0) - 1; // exclude empty subset
        return (int)total;
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
var beautifulSubsets = function(nums, k) {
    // Group numbers by remainder modulo k
    const groups = new Map();
    for (const x of nums) {
        const r = x % k;
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r).push(x);
    }

    let total = 1; // product of counts for each group

    for (const arr of groups.values()) {
        // Count frequencies of distinct values
        const freqMap = new Map();
        for (const v of arr) {
            freqMap.set(v, (freqMap.get(v) || 0) + 1);
        }
        const values = Array.from(freqMap.keys()).sort((a, b) => a - b);
        const m = values.length;
        const dp = new Array(m + 2).fill(0);
        dp[m] = 1; // empty subset for suffix

        for (let i = m - 1; i >= 0; --i) {
            const cnt = freqMap.get(values[i]);
            const takeWays = Math.pow(2, cnt) - 1; // non‑empty selections of this value
            const skip = dp[i + 1];
            let take;
            if (i + 1 < m && values[i + 1] === values[i] + k) {
                take = takeWays * dp[i + 2];
            } else {
                take = takeWays * dp[i + 1];
            }
            dp[i] = skip + take;
        }

        total *= dp[0];
    }

    // exclude the completely empty subset
    return total - 1;
};
```

## Typescript

```typescript
function beautifulSubsets(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    const used = new Set<number>();
    const n = nums.length;

    function dfs(idx: number): number {
        if (idx === n) return 0;
        let res = 0;
        // Skip current element
        res += dfs(idx + 1);
        // Take current element if it doesn't conflict with previously taken ones
        if (!used.has(nums[idx] - k)) {
            used.add(nums[idx]);
            // Subset consisting of this element alone (plus any further extensions)
            res += 1;
            res += dfs(idx + 1);
            used.delete(nums[idx]);
        }
        return res;
    }

    return dfs(0);
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
    function beautifulSubsets($nums, $k) {
        sort($nums);
        $used = [];
        $total = $this->dfs(0, $nums, $k, $used);
        return $total - 1; // exclude empty subset
    }

    private function dfs($idx, &$nums, $k, &$used) {
        $n = count($nums);
        if ($idx == $n) {
            return 1; // only the current (possibly empty) subset
        }
        // Skip current element
        $skip = $this->dfs($idx + 1, $nums, $k, $used);

        // Try to take current element if it doesn't conflict
        $take = 0;
        $need = $nums[$idx] - $k;
        if (!isset($used[$need]) || $used[$need] == 0) {
            $val = $nums[$idx];
            if (!isset($used[$val])) {
                $used[$val] = 0;
            }
            $used[$val]++;

            $take = $this->dfs($idx + 1, $nums, $k, $used);

            $used[$val]--;
            if ($used[$val] == 0) {
                unset($used[$val]);
            }
        }

        return $skip + $take;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulSubsets(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var selected = [Int:Int]()
        let n = sorted.count
        
        func dfs(_ idx: Int) -> Int {
            if idx == n { return 1 } // count empty subset
            var total = dfs(idx + 1) // skip current element
            
            let v = sorted[idx]
            if (selected[v - k] ?? 0) == 0 {
                selected[v, default: 0] += 1
                total += dfs(idx + 1)
                // backtrack
                if let cnt = selected[v] {
                    if cnt == 1 {
                        selected.removeValue(forKey: v)
                    } else {
                        selected[v] = cnt - 1
                    }
                }
            }
            return total
        }
        
        return dfs(0) - 1 // exclude empty subset
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulSubsets(nums: IntArray, k: Int): Int {
        val groups = HashMap<Int, MutableList<Int>>()
        for (num in nums) {
            val r = num % k
            groups.getOrPut(r) { mutableListOf() }.add(num)
        }
        var total = 1L
        for (list in groups.values) {
            // frequency of each distinct value in this group
            val freqMap = HashMap<Int, Int>()
            for (v in list) {
                freqMap[v] = (freqMap[v] ?: 0) + 1
            }
            val values = freqMap.keys.sorted()
            val m = values.size
            val cnt = IntArray(m)
            for (i in 0 until m) cnt[i] = freqMap[values[i]]!!

            val memo = LongArray(m) { -1L }

            fun dfs(i: Int): Long {
                if (i >= m) return 1L
                if (memo[i] != -1L) return memo[i]
                // skip current value
                var res = dfs(i + 1)
                // take at least one occurrence of current value
                val takeWays = ((1 shl cnt[i]) - 1).toLong()
                val nextIdx = if (i + 1 < m && values[i + 1] == values[i] + k) i + 2 else i + 1
                res += takeWays * dfs(nextIdx)
                memo[i] = res
                return res
            }

            total *= dfs(0)
        }
        // exclude empty subset
        return (total - 1).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int beautifulSubsets(List<int> nums, int k) {
    nums.sort();
    final Map<int, int> cnt = {};
    final int n = nums.length;

    int dfs(int idx) {
      if (idx == n) return 0;
      int res = 0;
      // Skip current element
      res += dfs(idx + 1);
      int v = nums[idx];
      // Can we take it? No element with value v - k should be present.
      if (!cnt.containsKey(v - k)) {
        cnt[v] = (cnt[v] ?? 0) + 1;
        // Subsets that include this element: the element itself plus extensions
        int sub = 1 + dfs(idx + 1);
        res += sub;
        // Backtrack
        cnt[v] = cnt[v]! - 1;
        if (cnt[v] == 0) cnt.remove(v);
      }
      return res;
    }

    return dfs(0);
  }
}
```

## Golang

```go
import "sort"

func beautifulSubsets(nums []int, k int) int {
	sort.Ints(nums)
	cnt := make(map[int]int)

	var dfs func(int) int
	dfs = func(idx int) int {
		if idx == len(nums) {
			return 1 // count empty subset
		}
		// skip current element
		res := dfs(idx + 1)

		// take current element if it doesn't conflict with previously taken elements
		if cnt[nums[idx]-k] == 0 {
			cnt[nums[idx]]++
			res += dfs(idx + 1)
			cnt[nums[idx]]--
		}
		return res
	}

	return dfs(0) - 1 // exclude empty subset
}
```

## Ruby

```ruby
def beautiful_subsets(nums, k)
  nums.sort!
  cnt = Hash.new(0)
  n = nums.length
  dfs = nil
  dfs = lambda do |i|
    return 1 if i == n
    total = dfs.call(i + 1) # skip current element
    val = nums[i]
    if cnt[val - k] == 0
      cnt[val] += 1
      total += dfs.call(i + 1) # take current element
      cnt[val] -= 1
    end
    total
  end
  dfs.call(0) - 1
end
```

## Scala

```scala
object Solution {
    def beautifulSubsets(nums: Array[Int], k: Int): Int = {
        val arr = nums.sorted
        import scala.collection.mutable

        val selected = mutable.Set[Int]()

        def dfs(i: Int): Long = {
            if (i == arr.length) return 1L
            var cnt = dfs(i + 1) // skip current element
            val v = arr(i)
            if (!selected.contains(v - k)) {
                selected.add(v)
                cnt += dfs(i + 1) // take current element
                selected.remove(v)
            }
            cnt
        }

        (dfs(0).toInt - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beautiful_subsets(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        // Build distinct values and their counts
        let mut vals: Vec<i32> = Vec::new();
        let mut cnts: Vec<usize> = Vec::new();
        for &v in &nums {
            if let Some(last) = vals.last_mut() {
                if *last == v {
                    *cnts.last_mut().unwrap() += 1;
                    continue;
                }
            }
            vals.push(v);
            cnts.push(1);
        }

        fn dfs(
            i: usize,
            vals: &Vec<i32>,
            cnts: &Vec<usize>,
            k: i32,
            memo: &mut Vec<Option<i64>>,
        ) -> i64 {
            if i >= vals.len() {
                return 1; // empty subset
            }
            if let Some(v) = memo[i] {
                return v;
            }
            // skip current value
            let skip = dfs(i + 1, vals, cnts, k, memo);
            // take at least one occurrence of current value
            let ways_take_current = (1i64 << cnts[i]) - 1; // non‑empty selections of this value
            let next_i = if i > 0 && vals[i] == vals[i - 1] + k {
                i + 2
            } else {
                i + 1
            };
            let take = ways_take_current * dfs(next_i, vals, cnts, k, memo);
            let res = skip + take;
            memo[i] = Some(res);
            res
        }

        let mut memo: Vec<Option<i64>> = vec![None; vals.len()];
        let total = dfs(0, &vals, &cnts, k, &mut memo) - 1; // exclude empty subset
        total as i32
    }
}
```

## Racket

```racket
(define/contract (beautiful-subsets nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (define (valid-subset? mask)
      (let loop-i ((i 0))
        (if (>= i n) #t
            (if (= 0 (bitwise-and mask (arithmetic-shift 1 i)))
                (loop-i (+ i 1))
                (let loop-j ((j (+ i 1)))
                  (cond [(>= j n) (loop-i (+ i 1))]
                        [(= 0 (bitwise-and mask (arithmetic-shift 1 j))) (loop-j (+ j 1))]
                        [else
                         (if (= (abs (- (vector-ref v i) (vector-ref v j))) k)
                             #f
                             (loop-j (+ j 1)))]))))))

    (let loop-mask ((mask 1) (cnt 0))
      (if (> mask (sub1 (arithmetic-shift 1 n)))
          cnt
          (loop-mask (+ mask 1)
                     (if (valid-subset? mask) (+ cnt 1) cnt))))))
```

## Erlang

```erlang
-export([beautiful_subsets/2]).

-beautiful_subsets(Nums, K) ->
    Sorted = lists:sort(Nums),
    Total = dfs(Sorted, K, #{}),
    Total - 1.

dfs([], _K, _Used) -> 
    1;
dfs([H|T], K, Used) ->
    Skip = dfs(T, K, Used),
    Take = case maps:is_key(H - K, Used) of
        true -> 0;
        false -> dfs(T, K, maps:put(H, true, Used))
    end,
    Skip + Take.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec beautiful_subsets(nums :: [integer], k :: integer) :: integer
  def beautiful_subsets(nums, k) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    max_mask = 1 <<< n

    1..(max_mask - 1)
    |> Enum.reduce(0, fn mask, acc ->
      {ok, _} =
        0..(n - 1)
        |> Enum.reduce_while({true, MapSet.new()}, fn i, {_valid, set} = state ->
          if (mask &&& (1 <<< i)) != 0 do
            v = Enum.at(sorted, i)

            if MapSet.member?(set, v - k) do
              {:halt, {false, set}}
            else
              {:cont, {true, MapSet.put(set, v)}}
            end
          else
            {:cont, state}
          end
        end)

      if ok, do: acc + 1, else: acc
    end)
  end
end
```
