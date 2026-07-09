# 1187. Make Array Strictly Increasing

## Cpp

```cpp
class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        arr2.erase(unique(arr2.begin(), arr2.end()), arr2.end());

        unordered_map<int,int> dp;
        dp[-1] = 0; // previous value -> min operations

        for (int a : arr1) {
            unordered_map<int,int> ndp;
            for (const auto& [prev, cost] : dp) {
                if (a > prev) {
                    auto it = ndp.find(a);
                    if (it == ndp.end() || cost < it->second) ndp[a] = cost;
                }
                auto itb = upper_bound(arr2.begin(), arr2.end(), prev);
                if (itb != arr2.end()) {
                    int val = *itb;
                    int ncost = cost + 1;
                    auto it = ndp.find(val);
                    if (it == ndp.end() || ncost < it->second) ndp[val] = ncost;
                }
            }
            dp.swap(ndp);
            if (dp.empty()) return -1; // impossible to continue
        }

        int ans = INT_MAX;
        for (const auto& [_, cost] : dp) ans = min(ans, cost);
        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        // Sort and deduplicate arr2
        Arrays.sort(arr2);
        int n = arr2.length;
        List<Integer> uniqList = new ArrayList<>();
        for (int v : arr2) {
            if (uniqList.isEmpty() || uniqList.get(uniqList.size() - 1) != v) {
                uniqList.add(v);
            }
        }
        int[] b = new int[uniqList.size()];
        for (int i = 0; i < b.length; i++) b[i] = uniqList.get(i);

        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(-1, 0); // previous value -> min operations

        for (int a : arr1) {
            Map<Integer, Integer> ndp = new HashMap<>();

            for (Map.Entry<Integer, Integer> entry : dp.entrySet()) {
                int prev = entry.getKey();
                int ops = entry.getValue();

                // Keep current element if possible
                if (a > prev) {
                    ndp.merge(a, ops, Math::min);
                }

                // Replace with the smallest element in b greater than prev
                int idx = firstGreater(b, prev);
                if (idx < b.length) {
                    int val = b[idx];
                    ndp.merge(val, ops + 1, Math::min);
                }
            }

            dp = ndp;
            if (dp.isEmpty()) return -1; // early exit, impossible
        }

        int ans = Integer.MAX_VALUE;
        for (int v : dp.values()) {
            ans = Math.min(ans, v);
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private int firstGreater(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo; // may be arr.length
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # sort and deduplicate arr2 for binary search
        arr2 = sorted(set(arr2))
        INF = float('inf')
        dp = {-1: 0}  # key: previous value, value: min operations
        
        for a in arr1:
            new_dp = {}
            for prev, ops in dp.items():
                # keep current element if it is strictly greater
                if a > prev:
                    cur_ops = new_dp.get(a, INF)
                    if ops < cur_ops:
                        new_dp[a] = ops
                # replace with the smallest arr2 element greater than prev
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    rep = arr2[idx]
                    cur_ops = new_dp.get(rep, INF)
                    if ops + 1 < cur_ops:
                        new_dp[rep] = ops + 1
            dp = new_dp
            if not dp:  # no possible states
                return -1
        
        ans = min(dp.values()) if dp else INF
        return ans if ans != INF else -1
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}  # prev value -> min operations
        
        for a in arr1:
            new_dp = {}
            for prev, ops in dp.items():
                # Keep current element if it keeps strictly increasing
                if a > prev:
                    cur = new_dp.get(a, float('inf'))
                    if ops < cur:
                        new_dp[a] = ops
                # Replace with the smallest arr2 element greater than prev
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    val = arr2[idx]
                    cur = new_dp.get(val, float('inf'))
                    if ops + 1 < cur:
                        new_dp[val] = ops + 1
            dp = new_dp
            if not dp:  # early exit if no states reachable
                return -1
        
        return min(dp.values()) if dp else -1
```

## C

```c
#include <stdlib.h>
#include <limits.h>

struct State {
    int val;
    int ops;
};

struct Cand {
    int val;
    int ops;
};

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

static int cmp_cand(const void *a, const void *b) {
    const struct Cand *ca = (const struct Cand *)a;
    const struct Cand *cb = (const struct Cand *)b;
    if (ca->val != cb->val) return (ca->val > cb->val) - (ca->val < cb->val);
    return (ca->ops > cb->ops) - (ca->ops < cb->ops);
}

static int upper_bound(int *arr, int size, int target) {
    int l = 0, r = size;
    while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] <= target)
            l = m + 1;
        else
            r = m;
    }
    return l; // first index with value > target
}

int makeArrayIncreasing(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    if (arr1Size == 0) return 0;

    /* sort and deduplicate arr2 */
    qsort(arr2, arr2Size, sizeof(int), cmp_int);
    int *uniq = (int *)malloc(sizeof(int) * arr2Size);
    int uSize = 0;
    for (int i = 0; i < arr2Size; ++i) {
        if (i == 0 || arr2[i] != arr2[i - 1]) {
            uniq[uSize++] = arr2[i];
        }
    }

    struct State dp[4005];
    int dpCnt = 0;
    dp[dpCnt++] = (struct State){-1, 0};

    for (int i = 0; i < arr1Size; ++i) {
        struct Cand cand[8005];
        int candCnt = 0;

        for (int j = 0; j < dpCnt; ++j) {
            int prev = dp[j].val;
            int ops = dp[j].ops;

            if (arr1[i] > prev) {
                cand[candCnt++] = (struct Cand){arr1[i], ops};
            }

            int idx = upper_bound(uniq, uSize, prev);
            if (idx < uSize) {
                cand[candCnt++] = (struct Cand){uniq[idx], ops + 1};
            }
        }

        if (candCnt == 0) {
            free(uniq);
            return -1;
        }

        qsort(cand, candCnt, sizeof(struct Cand), cmp_cand);

        dpCnt = 0;
        for (int k = 0; k < candCnt; ++k) {
            if (dpCnt == 0 || cand[k].val != dp[dpCnt - 1].val) {
                dp[dpCnt++] = (struct State){cand[k].val, cand[k].ops};
            } else {
                if (cand[k].ops < dp[dpCnt - 1].ops)
                    dp[dpCnt - 1].ops = cand[k].ops;
            }
        }
    }

    int answer = INT_MAX;
    for (int i = 0; i < dpCnt; ++i) {
        if (dp[i].ops < answer) answer = dp[i].ops;
    }

    free(uniq);
    return (answer == INT_MAX) ? -1 : answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MakeArrayIncreasing(int[] arr1, int[] arr2) {
        Array.Sort(arr2);
        // remove duplicates
        List<int> uniq = new List<int>();
        foreach (int v in arr2) {
            if (uniq.Count == 0 || uniq[uniq.Count - 1] != v)
                uniq.Add(v);
        }
        int[] b = uniq.ToArray();

        var dp = new Dictionary<int, int>();
        dp[-1] = 0; // previous value before first element

        foreach (int a in arr1) {
            var ndp = new Dictionary<int, int>();
            foreach (var kv in dp) {
                int prev = kv.Key;
                int ops = kv.Value;

                // keep current a if possible
                if (a > prev) {
                    if (!ndp.ContainsKey(a) || ops < ndp[a])
                        ndp[a] = ops;
                }

                // replace with smallest element in b greater than prev
                int idx = UpperBound(b, prev);
                if (idx < b.Length) {
                    int val = b[idx];
                    int newOps = ops + 1;
                    if (!ndp.ContainsKey(val) || newOps < ndp[val])
                        ndp[val] = newOps;
                }
            }
            dp = ndp;
            if (dp.Count == 0) return -1; // early exit, impossible
        }

        int ans = dp.Values.Min();
        return ans == int.MaxValue ? -1 : ans;
    }

    private int UpperBound(int[] arr, int target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid] <= target)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var makeArrayIncreasing = function(arr1, arr2) {
    // sort and deduplicate arr2
    arr2.sort((a, b) => a - b);
    const uniq = [];
    for (let v of arr2) {
        if (uniq.length === 0 || uniq[uniq.length - 1] !== v) uniq.push(v);
    }
    arr2 = uniq;

    // binary search: first index with value > target
    function upperBound(arr, target) {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    // dp maps previous value -> minimal operations so far
    let dp = new Map();
    dp.set(-1, 0); // sentinel before first element

    for (let a of arr1) {
        const ndp = new Map();

        for (const [prev, ops] of dp.entries()) {
            // Keep current element if it keeps strictly increasing
            if (a > prev) {
                const cur = ndp.get(a);
                if (cur === undefined || ops < cur) ndp.set(a, ops);
            }

            // Replace with the smallest arr2 value greater than prev
            const idx = upperBound(arr2, prev);
            if (idx < arr2.length) {
                const val = arr2[idx];
                const newOps = ops + 1;
                const cur = ndp.get(val);
                if (cur === undefined || newOps < cur) ndp.set(val, newOps);
            }
        }

        dp = ndp;
        if (dp.size === 0) return -1; // impossible to proceed
    }

    let ans = Infinity;
    for (const ops of dp.values()) {
        if (ops < ans) ans = ops;
    }
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function makeArrayIncreasing(arr1: number[], arr2: number[]): number {
    const sortedArr2 = Array.from(new Set(arr2)).sort((a, b) => a - b);
    let dp = new Map<number, number>();
    dp.set(-1, 0);

    for (const val of arr1) {
        const nextDp = new Map<number, number>();
        for (const [prev, ops] of dp.entries()) {
            // Keep current element if it maintains increasing order
            if (val > prev) {
                const cur = nextDp.get(val);
                if (cur === undefined || ops < cur) {
                    nextDp.set(val, ops);
                }
            }

            // Replace with the smallest arr2 element greater than prev
            const idx = upperBound(sortedArr2, prev);
            if (idx < sortedArr2.length) {
                const newVal = sortedArr2[idx];
                const newOps = ops + 1;
                const cur = nextDp.get(newVal);
                if (cur === undefined || newOps < cur) {
                    nextDp.set(newVal, newOps);
                }
            }
        }
        dp = nextDp;
    }

    let answer = Number.MAX_SAFE_INTEGER;
    for (const ops of dp.values()) {
        if (ops < answer) answer = ops;
    }
    return answer === Number.MAX_SAFE_INTEGER ? -1 : answer;
}

function upperBound(arr: number[], target: number): number {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (arr[mid] <= target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function makeArrayIncreasing($arr1, $arr2) {
        sort($arr2);
        // remove duplicates to keep size minimal
        $unique = [];
        $prevVal = null;
        foreach ($arr2 as $v) {
            if ($v !== $prevVal) {
                $unique[] = $v;
                $prevVal = $v;
            }
        }
        $arr2 = $unique;

        // dp: key => minimal operations to reach this previous value
        $dp = [-1 => 0];

        foreach ($arr1 as $val) {
            $newDp = [];
            foreach ($dp as $prevStr => $ops) {
                $prev = (int)$prevStr;
                // Keep current element if it is strictly greater than prev
                if ($val > $prev) {
                    if (!isset($newDp[$val]) || $ops < $newDp[$val]) {
                        $newDp[$val] = $ops;
                    }
                }
                // Replace with the smallest element in arr2 that is > prev
                $idx = $this->upperBound($arr2, $prev);
                if ($idx < count($arr2)) {
                    $candidate = $arr2[$idx];
                    $newOps = $ops + 1;
                    if (!isset($newDp[$candidate]) || $newOps < $newDp[$candidate]) {
                        $newDp[$candidate] = $newOps;
                    }
                }
            }
            $dp = $newDp;
            if (empty($dp)) {
                return -1; // no possible states
            }
        }

        $answer = min($dp);
        return $answer === INF ? -1 : $answer;
    }

    private function upperBound($arr, $target) {
        $lo = 0;
        $hi = count($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] <= $target) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        return $lo; // first index with value > target
    }
}
```

## Swift

```swift
class Solution {
    func makeArrayIncreasing(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var sortedArr2 = arr2.sorted()
        var uniq = [Int]()
        var last: Int? = nil
        for v in sortedArr2 {
            if v != last {
                uniq.append(v)
                last = v
            }
        }
        let b = uniq
        
        var dp: [Int:Int] = [-1: 0]
        
        for a in arr1 {
            var newDP = [Int:Int]()
            for (prev, cost) in dp {
                if a > prev {
                    if let existing = newDP[a] {
                        if cost < existing { newDP[a] = cost }
                    } else {
                        newDP[a] = cost
                    }
                }
                let idx = upperBound(b, prev)
                if idx < b.count {
                    let val = b[idx]
                    let newCost = cost + 1
                    if let existing = newDP[val] {
                        if newCost < existing { newDP[val] = newCost }
                    } else {
                        newDP[val] = newCost
                    }
                }
            }
            dp = newDP
            if dp.isEmpty { return -1 }
        }
        
        var ans = Int.max
        for v in dp.values {
            if v < ans { ans = v }
        }
        return ans == Int.max ? -1 : ans
    }
    
    private func upperBound(_ nums: [Int], _ target: Int) -> Int {
        var l = 0, r = nums.count
        while l < r {
            let m = (l + r) >> 1
            if nums[m] <= target {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeArrayIncreasing(arr1: IntArray, arr2: IntArray): Int {
        val sortedList = arr2.distinct().sorted()
        val b = IntArray(sortedList.size) { sortedList[it] }
        var dp = mutableMapOf<Int, Int>()
        dp[-1] = 0
        for (a in arr1) {
            val newDp = mutableMapOf<Int, Int>()
            for ((prev, cost) in dp) {
                if (a > prev) {
                    val cur = newDp[a]
                    if (cur == null || cost < cur) newDp[a] = cost
                }
                val idx = upperBound(b, prev)
                if (idx < b.size) {
                    val v = b[idx]
                    val newCost = cost + 1
                    val cur2 = newDp[v]
                    if (cur2 == null || newCost < cur2) newDp[v] = newCost
                }
            }
            dp = newDp
            if (dp.isEmpty()) return -1
        }
        var ans = Int.MAX_VALUE
        for (v in dp.values) {
            if (v < ans) ans = v
        }
        return if (ans == Int.MAX_VALUE) -1 else ans
    }

    private fun upperBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (arr[m] <= target) {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
}
```

## Dart

```dart
class Solution {
  int makeArrayIncreasing(List<int> arr1, List<int> arr2) {
    // Sort and deduplicate arr2
    List<int> sortedArr2 = List.from(arr2);
    sortedArr2.sort();
    List<int> uniqArr2 = [];
    for (int v in sortedArr2) {
      if (uniqArr2.isEmpty || uniqArr2.last != v) {
        uniqArr2.add(v);
      }
    }

    // dp maps previous value -> minimum operations to reach this state
    Map<int, int> dp = {-1: 0};

    for (int a in arr1) {
      Map<int, int> ndp = {};
      for (var entry in dp.entries) {
        int prev = entry.key;
        int ops = entry.value;

        // Keep current element if it keeps the sequence increasing
        if (a > prev) {
          ndp.update(a, (existing) => existing < ops ? existing : ops,
              ifAbsent: () => ops);
        }

        // Replace with the smallest element in arr2 that is greater than prev
        int idx = _upperBound(uniqArr2, prev);
        if (idx < uniqArr2.length) {
          int val = uniqArr2[idx];
          int newOps = ops + 1;
          ndp.update(val, (existing) => existing < newOps ? existing : newOps,
              ifAbsent: () => newOps);
        }
      }
      dp = ndp;
      if (dp.isEmpty) {
        return -1; // no possible states forward
      }
    }

    int answer = dp.values.reduce((a, b) => a < b ? a : b);
    return answer;
  }

  int _upperBound(List<int> list, int target) {
    int lo = 0, hi = list.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (list[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}
```

## Golang

```go
func makeArrayIncreasing(arr1 []int, arr2 []int) int {
	// sort and deduplicate arr2
	sort.Ints(arr2)
	uniq := make([]int, 0, len(arr2))
	for _, v := range arr2 {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	arr2 = uniq

	const INF = int(^uint(0) >> 1) // max int
	dp := map[int]int{-1: 0}

	for _, a := range arr1 {
		newDP := make(map[int]int)
		for prev, cost := range dp {
			// keep current element if possible
			if a > prev {
				if c, ok := newDP[a]; !ok || cost < c {
					newDP[a] = cost
				}
			}
			// replace with smallest arr2 element greater than prev
			idx := sort.Search(len(arr2), func(i int) bool { return arr2[i] > prev })
			if idx < len(arr2) {
				val := arr2[idx]
				newCost := cost + 1
				if c, ok := newDP[val]; !ok || newCost < c {
					newDP[val] = newCost
				}
			}
		}
		dp = newDP
		if len(dp) == 0 {
			return -1
		}
	}

	ans := INF
	for _, v := range dp {
		if v < ans {
			ans = v
		}
	}
	if ans == INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def make_array_increasing(arr1, arr2)
  arr2 = arr2.sort.uniq
  dp = { -1 => 0 }
  arr1.each do |a|
    new_dp = {}
    dp.each do |prev, ops|
      if a > prev
        cur = new_dp[a]
        new_dp[a] = ops if cur.nil? || ops < cur
      end
      idx = arr2.bsearch_index { |x| x > prev }
      if idx
        val = arr2[idx]
        new_ops = ops + 1
        cur = new_dp[val]
        new_dp[val] = new_ops if cur.nil? || new_ops < cur
      end
    end
    dp = new_dp
    return -1 if dp.empty?
  end
  dp.values.min
end
```

## Scala

```scala
object Solution {
  def makeArrayIncreasing(arr1: Array[Int], arr2: Array[Int]): Int = {
    val uniqArr2 = arr2.distinct.sorted
    import scala.collection.mutable

    var dp = mutable.Map[Int, Int](-1 -> 0)
    val INF = Int.MaxValue / 2

    def upperBound(arr: Array[Int], target: Int): Int = {
      var l = 0
      var r = arr.length
      while (l < r) {
        val m = (l + r) >>> 1
        if (arr(m) <= target) l = m + 1 else r = m
      }
      l
    }

    for (a <- arr1) {
      val newDp = mutable.Map[Int, Int]()
      for ((prev, ops) <- dp) {
        // keep current element if possible
        if (a > prev) {
          val cur = newDp.getOrElse(a, INF)
          if (ops < cur) newDp.update(a, ops)
        }
        // replace with smallest arr2 element greater than prev
        val idx = upperBound(uniqArr2, prev)
        if (idx < uniqArr2.length) {
          val v = uniqArr2(idx)
          val newOps = ops + 1
          val cur = newDp.getOrElse(v, INF)
          if (newOps < cur) newDp.update(v, newOps)
        }
      }
      dp = newDp
    }

    if (dp.isEmpty) -1
    else {
      val ans = dp.values.min
      if (ans >= INF) -1 else ans
    }
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn make_array_increasing(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        // sort and deduplicate arr2
        let mut b = arr2;
        b.sort_unstable();
        b.dedup();

        // dp maps last value -> minimal operations to reach it
        let mut dp: HashMap<i32, i32> = HashMap::new();
        dp.insert(-1, 0);

        for &a in arr1.iter() {
            let mut ndp: HashMap<i32, i32> = HashMap::new();

            for (&prev, &ops) in dp.iter() {
                // Keep a if it keeps increasing
                if a > prev {
                    ndp.entry(a)
                        .and_modify(|e| *e = (*e).min(ops))
                        .or_insert(ops);
                }

                // Replace with the smallest element in b that is greater than prev
                let idx = match b.binary_search(&prev) {
                    Ok(pos) => pos + 1,
                    Err(pos) => pos,
                };
                if idx < b.len() {
                    let val = b[idx];
                    ndp.entry(val)
                        .and_modify(|e| *e = (*e).min(ops + 1))
                        .or_insert(ops + 1);
                }
            }

            dp = ndp;
            if dp.is_empty() {
                return -1;
            }
        }

        match dp.values().min() {
            Some(&ans) => ans,
            None => -1,
        }
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define (binary-search-first-greater vec target)
  (let loop ((lo 0) (hi (vector-length vec)))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (mid-val (vector-ref vec mid)))
          (if (> mid-val target)
              (loop lo mid)
              (loop (+ mid 1) hi))))))

(define/contract (make-array-increasing arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((sorted-arr2 (sort arr2 <))
         (unique-arr2 (remove-duplicates sorted-arr2 =))
         (vec (list->vector unique-arr2)))
    (define INF 1000000000)
    (define dp (make-hash))
    (hash-set! dp -1 0)
    (for ([a arr1])
      (define newdp (make-hash))
      (hash-for-each dp
        (lambda (prev ops)
          ;; keep a unchanged if possible
          (when (> a prev)
            (let ((cur (hash-ref newdp a INF)))
              (when (< ops cur) (hash-set! newdp a ops))))
          ;; replace with element from arr2
          (let ((idx (binary-search-first-greater vec prev)))
            (when (< idx (vector-length vec))
              (let* ((val (vector-ref vec idx))
                     (newops (+ ops 1))
                     (cur (hash-ref newdp val INF)))
                (when (< newops cur) (hash-set! newdp val newops)))))))
      (set! dp newdp))
    (if (= (hash-count dp) 0)
        -1
        (let ((ans INF))
          (hash-for-each dp
            (lambda (_ ops)
              (when (< ops ans) (set! ans ops))))
          (if (= ans INF) -1 ans)))))
```

## Erlang

```erlang
-spec make_array_increasing([integer()], [integer()]) -> integer().
make_array_increasing(Arr1, Arr2) ->
    Sorted = lists:usort(Arr2),
    Len2 = length(Sorted),
    Arr2Array = array:from_list(Sorted),
    DP0 = #{-1 => 0},
    FinalDP = lists:foldl(fun(A1Elem, DPAcc) ->
        NewDP = maps:new(),
        maps:fold(fun(Prev, Cost, ND) ->
            ND1 = if A1Elem > Prev -> update_map(ND, A1Elem, Cost); true -> ND end,
            Idx = upper_bound(Arr2Array, Len2, Prev),
            case Idx < Len2 of
                true ->
                    Val = array:get(Idx, Arr2Array),
                    update_map(ND1, Val, Cost + 1);
                false -> ND1
            end
        end, NewDP, DPAcc)
    end, DP0, Arr1),

    case maps:values(FinalDP) of
        [] -> -1;
        Values -> lists:min(Values)
    end.

upper_bound(Array, Len, Target) ->
    upper_bound(Array, Target, 0, Len).

upper_bound(_Array, _Target, Lo, Hi) when Lo >= Hi -> Lo;
upper_bound(Array, Target, Lo, Hi) ->
    Mid = (Lo + Hi) div 2,
    Val = array:get(Mid, Array),
    if Val =< Target ->
            upper_bound(Array, Target, Mid + 1, Hi);
       true ->
            upper_bound(Array, Target, Lo, Mid)
    end.

update_map(Map, Key, Cost) ->
    case maps:is_key(Key, Map) of
        true ->
            Existing = maps:get(Key, Map),
            MinCost = if Cost < Existing -> Cost; true -> Existing end,
            maps:put(Key, MinCost, Map);
        false ->
            maps:put(Key, Cost, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_array_increasing(arr1 :: [integer], arr2 :: [integer]) :: integer
  def make_array_increasing(arr1, arr2) do
    # sort and deduplicate arr2
    arr2_sorted = arr2 |> Enum.sort() |> Enum.uniq()
    arr2_arr = :array.from_list(arr2_sorted)
    n = :array.size(arr2_arr)

    dp_initial = %{-1 => 0}
    final_dp = process(arr1, arr2_arr, n, dp_initial)

    case Map.values(final_dp) do
      [] -> -1
      vals -> Enum.min(vals)
    end
  end

  defp process([], _arr2_arr, _n, dp), do: dp

  defp process([a | rest], arr2_arr, n, dp) do
    new_dp =
      Enum.reduce(dp, %{}, fn {prev, cost}, acc ->
        # keep original a if possible
        acc1 =
          if a > prev do
            Map.update(acc, a, cost, &min(&1, cost))
          else
            acc
          end

        idx = upper_bound(arr2_arr, n, prev)

        if idx < n do
          val = :array.get(idx, arr2_arr)
          new_cost = cost + 1
          Map.update(acc1, val, new_cost, &min(&1, new_cost))
        else
          acc1
        end
      end)

    process(rest, arr2_arr, n, new_dp)
  end

  # binary search: first index with value > target
  defp upper_bound(arr, size, target), do: ub(0, size, arr, target)

  defp ub(low, high, _arr, _target) when low >= high, do: low

  defp ub(low, high, arr, target) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val <= target do
      ub(mid + 1, high, arr, target)
    else
      ub(low, mid, arr, target)
    end
  end
end
```
