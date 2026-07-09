# 1488. Avoid Flood in The City

## Cpp

```cpp
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        vector<int> ans(n);
        set<int> dryDays;
        unordered_map<int, int> lastRain;
        for (int i = 0; i < n; ++i) {
            if (rains[i] == 0) {
                dryDays.insert(i);
                ans[i] = 1; // placeholder
            } else {
                int lake = rains[i];
                ans[i] = -1;
                if (lastRain.count(lake)) {
                    int prevDay = lastRain[lake];
                    auto it = dryDays.lower_bound(prevDay + 1);
                    if (it == dryDays.end()) return {};
                    int dryIdx = *it;
                    ans[dryIdx] = lake;
                    dryDays.erase(it);
                }
                lastRain[lake] = i;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        int[] ans = new int[n];
        Arrays.fill(ans, 1); // default for dry days
        
        Map<Integer, Integer> lastRain = new HashMap<>();
        TreeSet<Integer> dryDays = new TreeSet<>();
        
        for (int i = 0; i < n; i++) {
            int lake = rains[i];
            if (lake == 0) {
                dryDays.add(i);
            } else {
                if (lastRain.containsKey(lake)) {
                    Integer day = dryDays.ceiling(lastRain.get(lake) + 1);
                    if (day == null) {
                        return new int[0];
                    }
                    ans[day] = lake;
                    dryDays.remove(day);
                }
                lastRain.put(lake, i);
                ans[i] = -1;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n
        last_rain = {}
        zeros = []  # sorted list of indices where we can dry a lake

        import bisect

        for i, r in enumerate(rains):
            if r == 0:
                zeros.append(i)          # indices increase monotonically, list stays sorted
                ans[i] = 1               # placeholder, will be overwritten if used
            else:
                if r in last_rain:
                    prev_day = last_rain[r]
                    idx = bisect.bisect_right(zeros, prev_day)
                    if idx == len(zeros):
                        return []
                    dry_day = zeros.pop(idx)
                    ans[dry_day] = r      # dry lake r on this day
                last_rain[r] = i
                ans[i] = -1               # rain day

        return ans
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last_rain = {}
        dry_days = []  # min-heap of indices where rain == 0
        
        for i, lake in enumerate(rains):
            if lake == 0:
                heapq.heappush(dry_days, i)
                # placeholder; will be set when used or later default to 1
                ans[i] = 1
            else:
                if lake in last_rain:
                    prev_day = last_rain[lake]
                    # find a dry day after prev_day
                    while dry_days and dry_days[0] <= prev_day:
                        heapq.heappop(dry_days)  # cannot use this day
                    if not dry_days:
                        return []
                    dry_idx = heapq.heappop(dry_days)
                    ans[dry_idx] = lake
                last_rain[lake] = i
                ans[i] = -1
        
        # any remaining unused dry days can dry arbitrary lake (e.g., 1)
        for idx in dry_days:
            ans[idx] = 1
        
        return ans
```

## C

```c
#include <stdlib.h>

static int hash_int(int key, int cap) {
    int h = key % cap;
    return (h < 0) ? h + cap : h;
}

static int hashmap_get(int *keys, int *vals, int cap, int key) {
    int idx = hash_int(key, cap);
    while (keys[idx] != -1) {
        if (keys[idx] == key) return vals[idx];
        idx = (idx + 1) % cap;
    }
    return -1; // not found
}

static void hashmap_put(int *keys, int *vals, int cap, int key, int val) {
    int idx = hash_int(key, cap);
    while (keys[idx] != -1 && keys[idx] != key) {
        idx = (idx + 1) % cap;
    }
    keys[idx] = key;
    vals[idx] = val;
}

static int find_set(int *parent, int x) {
    if (parent[x] == x) return x;
    parent[x] = find_set(parent, parent[x]);
    return parent[x];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* avoidFlood(int* rains, int rainsSize, int* returnSize) {
    int n = rainsSize;
    int *ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) ans[i] = -1;

    // DSU for next available dry day
    int *parent = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (rains[i] == 0)
            parent[i] = i;
        else
            parent[i] = i + 1;
    }
    parent[n] = n; // sentinel

    // hashmap for last rain day of each lake
    int cap = 200003; // a prime > 2 * 1e5
    int *keys = (int*)malloc(cap * sizeof(int));
    int *vals = (int*)malloc(cap * sizeof(int));
    for (int i = 0; i < cap; ++i) keys[i] = -1;

    for (int day = 0; day < n; ++day) {
        int lake = rains[day];
        if (lake > 0) { // rain
            int prevDay = hashmap_get(keys, vals, cap, lake);
            if (prevDay != -1) {
                int dryDay = find_set(parent, prevDay + 1);
                if (dryDay >= day || dryDay == n) {
                    // impossible to avoid flood
                    free(ans);
                    free(parent);
                    free(keys);
                    free(vals);
                    *returnSize = 0;
                    return NULL;
                }
                ans[dryDay] = lake;               // use this dry day for the lake
                parent[dryDay] = find_set(parent, dryDay + 1); // mark used
            }
            hashmap_put(keys, vals, cap, lake, day);
            ans[day] = -1;
        } else { // dry day (no rain)
            // will assign later if needed; keep placeholder -1 for now
        }
    }

    // Fill remaining unused dry days with any valid lake number (e.g., 1)
    for (int i = 0; i < n; ++i) {
        if (rains[i] == 0 && ans[i] == -1) {
            ans[i] = 1;
        }
    }

    free(parent);
    free(keys);
    free(vals);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] AvoidFlood(int[] rains) {
        int n = rains.Length;
        int[] ans = new int[n];
        var lastRain = new Dictionary<int, int>();
        var dryDays = new SortedSet<int>();

        for (int i = 0; i < n; i++) {
            if (rains[i] == 0) {
                // initially assign any lake number, will be overwritten if needed
                ans[i] = 1;
                dryDays.Add(i);
            } else {
                int lake = rains[i];
                if (lastRain.TryGetValue(lake, out int prevDay)) {
                    // need a dry day after prevDay
                    var possible = dryDays.GetViewBetween(prevDay + 1, n - 1);
                    if (possible.Count == 0) {
                        return new int[0]; // impossible
                    }
                    int dryIdx = possible.Min;
                    ans[dryIdx] = lake;      // dry this lake on that day
                    dryDays.Remove(dryIdx);   // day is now used
                }
                ans[i] = -1; // rain day
                lastRain[lake] = i;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rains
 * @return {number[]}
 */
var avoidFlood = function(rains) {
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] <= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const root = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < h.length && h[l] < h[smallest]) smallest = l;
                    if (r < h.length && h[r] < h[smallest]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }

    const n = rains.length;
    const ans = new Array(n);
    const lastRain = new Map(); // lake -> last day index
    const dryDays = new MinHeap();

    for (let i = 0; i < n; ++i) {
        const r = rains[i];
        if (r === 0) {
            dryDays.push(i);
            ans[i] = 1; // placeholder, will stay 1 if never used
        } else {
            if (lastRain.has(r)) {
                const prev = lastRain.get(r);
                while (dryDays.size() > 0 && dryDays.peek() <= prev) {
                    // this zero day is too early, discard it
                    dryDays.pop();
                }
                if (dryDays.size() === 0) {
                    return [];
                }
                const useDay = dryDays.pop(); // earliest suitable day
                ans[useDay] = r;
            }
            lastRain.set(r, i);
            ans[i] = -1;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function avoidFlood(rains: number[]): number[] {
    const n = rains.length;
    const ans = new Array<number>(n).fill(0);
    const lastRain = new Map<number, number>();

    class Fenwick {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        add(i: number, delta: number): void {
            for (let x = i; x <= this.n; x += x & -x) {
                this.tree[x] += delta;
            }
        }
        sum(i: number): number {
            let res = 0;
            for (let x = i; x > 0; x -= x & -x) {
                res += this.tree[x];
            }
            return res;
        }
        // find smallest index such that prefix sum >= k (1‑based)
        findKth(k: number): number {
            let idx = 0;
            let bitMask = 1;
            while ((bitMask << 1) <= this.n) bitMask <<= 1;
            for (let d = bitMask; d > 0; d >>= 1) {
                const next = idx + d;
                if (next <= this.n && this.tree[next] < k) {
                    idx = next;
                    k -= this.tree[next];
                }
            }
            return idx + 1;
        }
    }

    const bit = new Fenwick(n);

    for (let i = 0; i < n; ++i) {
        const rain = rains[i];
        if (rain > 0) {
            ans[i] = -1;
            if (lastRain.has(rain)) {
                const prevDay = lastRain.get(rain)!; // index of previous rain on this lake
                // number of available dry days after prevDay
                const totalAfterPrev = bit.sum(n) - bit.sum(prevDay + 1);
                if (totalAfterPrev === 0) return [];
                // we need the first dry day > prevDay, which is the (bit.sum(prevDay+1)+1)-th available day overall
                const kth = bit.sum(prevDay + 1) + 1;
                const dryIdxOneBased = bit.findKth(kth);
                const dryIdx = dryIdxOneBased - 1; // convert to 0‑based day index
                ans[dryIdx] = rain;
                bit.add(dryIdxOneBased, -1); // mark this dry day as used
            }
            lastRain.set(rain, i);
        } else {
            // dry day, initially assign arbitrary lake (will be overwritten if needed)
            ans[i] = 1;
            bit.add(i + 1, 1); // make this day available for drying
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rains
     * @return Integer[]
     */
    function avoidFlood($rains) {
        $n = count($rains);
        $ans = array_fill(0, $n, -1);
        $lastRain = []; // lake => last day index

        $bit = new BIT($n);

        for ($i = 0; $i < $n; ++$i) {
            if ($rains[$i] == 0) {
                // dry day, initially assign dummy value 1
                $ans[$i] = 1;
                $bit->add($i, 1); // mark as available
            } else {
                $lake = $rains[$i];
                if (isset($lastRain[$lake])) {
                    $prevDay = $lastRain[$lake];
                    // need a dry day after prevDay
                    $availableAfterPrev = $bit->rangeSum($prevDay + 1, $n - 1);
                    if ($availableAfterPrev == 0) {
                        return []; // impossible
                    }
                    $k = $bit->sum($prevDay) + 1; // the (sum(prev)+1)-th available day
                    $dryIdx = $bit->findKth($k); // zero‑based index
                    $ans[$dryIdx] = $lake; // dry this lake on that day
                    $bit->add($dryIdx, -1); // mark as used
                }
                $lastRain[$lake] = $i;
                $ans[$i] = -1;
            }
        }

        // any remaining dry days keep the dummy value (any positive integer is fine)
        return $ans;
    }
}

/**
 * Binary Indexed Tree (Fenwick) supporting point updates and prefix sums.
 */
class BIT {
    public int $size;
    public array $tree;

    function __construct(int $n) {
        $this->size = $n;
        // 1‑based indexing, extra element to avoid bound checks
        $this->tree = array_fill(0, $n + 2, 0);
    }

    // add $delta at zero‑based index $idx
    function add(int $idx, int $delta): void {
        $i = $idx + 1;
        while ($i <= $this->size) {
            $this->tree[$i] += $delta;
            $i += $i & (-$i);
        }
    }

    // prefix sum from 0 to zero‑based index $idx (inclusive)
    function sum(int $idx): int {
        if ($idx < 0) return 0;
        $i = $idx + 1;
        $res = 0;
        while ($i > 0) {
            $res += $this->tree[$i];
            $i -= $i & (-$i);
        }
        return $res;
    }

    // sum on interval [$l, $r] (both zero‑based, inclusive)
    function rangeSum(int $l, int $r): int {
        if ($l > $r) return 0;
        return $this->sum($r) - $this->sum($l - 1);
    }

    // find smallest zero‑based index such that prefix sum >= $k (1‑based k)
    function findKth(int $k): int {
        $idx = 0;
        // largest power of two <= size
        $bitMask = 1;
        while (($bitMask << 1) <= $this->size) {
            $bitMask <<= 1;
        }
        for (; $bitMask != 0; $bitMask >>= 1) {
            $next = $idx + $bitMask;
            if ($next <= $this->size && $this->tree[$next] < $k) {
                $idx = $next;
                $k -= $this->tree[$next];
            }
        }
        // $idx is the largest index with prefix sum < original k (1‑based)
        // zero‑based answer is $idx
        return $idx;
    }
}
```

## Swift

```swift
class Solution {
    class BIT {
        private let n: Int
        private var tree: [Int]
        init(_ n: Int) {
            self.n = n
            self.tree = Array(repeating: 0, count: n + 2)
        }
        func update(_ index: Int, _ delta: Int) {
            var i = index + 1
            while i <= n {
                tree[i] += delta
                i += i & -i
            }
        }
        func query(_ index: Int) -> Int {
            if index < 0 { return 0 }
            var i = index + 1
            var res = 0
            while i > 0 {
                res += tree[i]
                i -= i & -i
            }
            return res
        }
        // returns smallest zero‑based index such that prefix sum >= k (k >= 1)
        func findByOrder(_ k: Int) -> Int {
            var idx = 0
            var bitMask = 1
            while (bitMask << 1) <= n { bitMask <<= 1 }
            var target = k
            var mask = bitMask
            while mask != 0 {
                let next = idx + mask
                if next <= n && tree[next] < target {
                    target -= tree[next]
                    idx = next
                }
                mask >>= 1
            }
            return idx   // zero‑based index
        }
    }

    func avoidFlood(_ rains: [Int]) -> [Int] {
        let n = rains.count
        var ans = Array(repeating: -1, count: n)
        let bit = BIT(n)
        var lastRainDay = [Int: Int]()   // lake -> day index

        for i in 0..<n {
            let v = rains[i]
            if v == 0 {
                ans[i] = 1          // placeholder, will be overwritten if used
                bit.update(i, 1)    // this day is available for drying
            } else {
                if let prev = lastRainDay[v] {
                    // number of unused dry days up to prev (inclusive)
                    let cntPrev = bit.query(prev)
                    // number of unused dry days before current day i
                    let total = bit.query(i - 1)
                    if total - cntPrev == 0 {
                        return []
                    }
                    // the first available dry day after prev
                    let targetK = cntPrev + 1
                    let dryIdx = bit.findByOrder(targetK)
                    ans[dryIdx] = v
                    bit.update(dryIdx, -1)   // mark this day as used
                }
                lastRainDay[v] = i
                ans[i] = -1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet

class Solution {
    fun avoidFlood(rains: IntArray): IntArray {
        val n = rains.size
        val ans = IntArray(n) { 1 } // default dry day value
        val lastRainDay = HashMap<Int, Int>()
        val dryDays = TreeSet<Int>()

        for (i in 0 until n) {
            val lake = rains[i]
            if (lake == 0) {
                dryDays.add(i)
            } else {
                ans[i] = -1
                val prev = lastRainDay[lake]
                if (prev != null) {
                    // need a dry day after previous rain of this lake
                    val day = dryDays.higher(prev)
                    if (day == null) return IntArray(0)
                    ans[day] = lake
                    dryDays.remove(day)
                }
                lastRainDay[lake] = i
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> avoidFlood(List<int> rains) {
    int n = rains.length;
    List<int> ans = List.filled(n, 0);
    Map<int, int> lastRain = {};
    SplayTreeMap<int, int> zeroDays = SplayTreeMap<int, int>();

    for (int i = 0; i < n; i++) {
      if (rains[i] == 0) {
        zeroDays[i] = i;
        ans[i] = 1; // placeholder, any positive number is acceptable
      } else {
        int lake = rains[i];
        if (!lastRain.containsKey(lake)) {
          lastRain[lake] = i;
          ans[i] = -1;
        } else {
          int prevDay = lastRain[lake]!;
          int? dryDay = zeroDays.firstKeyAfter(prevDay);
          if (dryDay == null) {
            return [];
          }
          ans[dryDay] = lake;
          zeroDays.remove(dryDay);
          lastRain[lake] = i;
          ans[i] = -1;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type treapNode struct {
	key       int
	priority  uint32
	left, right *treapNode
}

func rotateRight(y *treapNode) *treapNode {
	x := y.left
	y.left = x.right
	x.right = y
	return x
}

func rotateLeft(x *treapNode) *treapNode {
	y := x.right
	x.right = y.left
	y.left = x
	return y
}

func treapInsert(root *treapNode, key int) *treapNode {
	if root == nil {
		return &treapNode{key: key, priority: rand.Uint32()}
	}
	if key < root.key {
		root.left = treapInsert(root.left, key)
		if root.left.priority < root.priority {
			root = rotateRight(root)
		}
	} else {
		root.right = treapInsert(root.right, key)
		if root.right.priority < root.priority {
			root = rotateLeft(root)
		}
	}
	return root
}

func treapErase(root *treapNode, key int) *treapNode {
	if root == nil {
		return nil
	}
	if key < root.key {
		root.left = treapErase(root.left, key)
	} else if key > root.key {
		root.right = treapErase(root.right, key)
	} else { // found
		if root.left == nil {
			return root.right
		}
		if root.right == nil {
			return root.left
		}
		if root.left.priority < root.right.priority {
			root = rotateRight(root)
			root.right = treapErase(root.right, key)
		} else {
			root = rotateLeft(root)
			root.left = treapErase(root.left, key)
		}
	}
	return root
}

func treapLowerBound(root *treapNode, key int) *treapNode {
	var candidate *treapNode
	for root != nil {
		if root.key >= key {
			candidate = root
			root = root.left
		} else {
			root = root.right
		}
	}
	return candidate
}

func avoidFlood(rains []int) []int {
	rand.Seed(time.Now().UnixNano())
	n := len(rains)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = 1 // default lake for dry days
	}
	lastRain := make(map[int]int)
	var zeros *treapNode

	for day, r := range rains {
		if r == 0 {
			zeros = treapInsert(zeros, day)
			// ans[day] stays as 1 unless later assigned to a specific lake
		} else {
			lake := r
			if prevDay, ok := lastRain[lake]; ok {
				node := treapLowerBound(zeros, prevDay+1)
				if node == nil {
					return []int{}
				}
				dryDay := node.key
				ans[dryDay] = lake
				zeros = treapErase(zeros, dryDay)
			}
			lastRain[lake] = day
			ans[day] = -1
		}
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

def avoid_flood(rains)
  n = rains.length
  ans = Array.new(n, 1)          # default for dry days
  last_rain = {}                 # lake => last rain day index
  dry_days = SortedSet.new       # indices of days with rain == 0

  (0...n).each do |i|
    lake = rains[i]
    if lake == 0
      dry_days.add(i)
      ans[i] = 1                # placeholder, will stay if never used
    else
      if last_rain.key?(lake)
        prev_day = last_rain[lake]
        candidate = dry_days.bsearch { |d| d > prev_day }
        return [] unless candidate
        ans[candidate] = lake
        dry_days.delete(candidate)
      end
      ans[i] = -1
      last_rain[lake] = i
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def avoidFlood(rains: Array[Int]): Array[Int] = {
    import java.util.TreeSet
    val n = rains.length
    val ans = new Array[Int](n)
    val dryDays = new TreeSet[Integer]()
    val lastRain = scala.collection.mutable.Map[Int, Int]()

    for (i <- 0 until n) {
      if (rains(i) == 0) {
        dryDays.add(i) // store index of a possible drying day
        ans(i) = 1     // placeholder, will be overwritten if used
      } else {
        val lake = rains(i)
        if (lastRain.contains(lake)) {
          val prevDay = lastRain(lake)
          val cand = dryDays.ceiling(prevDay + 1) // need a drying day after previous rain
          if (cand == null) return Array.emptyIntArray
          val day = cand.intValue()
          ans(day) = lake
          dryDays.remove(cand)
        }
        ans(i) = -1
        lastRain(lake) = i
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, HashMap};

impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        let n = rains.len();
        let mut ans = vec![-1; n];
        let mut last_rain: HashMap<i32, usize> = HashMap::new();
        let mut dry_days: BTreeSet<usize> = BTreeSet::new();

        for i in 0..n {
            let r = rains[i];
            if r == 0 {
                // this day can be used to dry a lake later
                dry_days.insert(i);
                ans[i] = 1; // placeholder, will stay if never needed
            } else {
                if let Some(&prev_day) = last_rain.get(&r) {
                    // need a dry day after prev_day
                    if let Some(&dry_day) = dry_days.range(prev_day + 1..).next() {
                        ans[dry_day] = r;
                        dry_days.remove(&dry_day);
                    } else {
                        return vec![];
                    }
                }
                last_rain.insert(r, i);
                ans[i] = -1;
            }
        }

        // remaining unused dry days can keep any positive number (already set to 1)
        ans
    }
}
```

## Racket

```racket
(define/contract (avoid-flood rains)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((len (length rains))
         (rains-vec (list->vector rains))
         (ans (make-vector len 0))
         (lastRain (make-hash))
         ;; Binary Indexed Tree (1‑based internal)
         (bit (make-vector (+ len 1) 0))
         (bit-add!
          (lambda (idx delta)
            (let ((i (+ idx 1)))
              (let loop ((i i))
                (when (<= i len)
                  (vector-set! bit i (+ (vector-ref bit i) delta))
                  (loop (+ i (bitwise-and i (- i)))))))))
         (bit-sum
          (lambda (idx)
            (let ((i (+ idx 1))
                  (res 0))
              (let loop ((i i) (res res))
                (if (= i 0)
                    res
                    (loop (bitwise-and i (- i)) (+ res (vector-ref bit i))))))))
         (bit-find-kth
          (lambda (k)
            ;; returns zero‑based index of the k‑th available dry day
            (let ((idx 0)
                  (mask (let loop ((m 1))
                          (if (> (* m 2) len) m (loop (* m 2))))))
              (let loop ()
                (when (> mask 0)
                  (let ((next (+ idx mask)))
                    (when (and (<= next len)
                               (< (vector-ref bit next) k))
                      (set! idx next)
                      (set! k (- k (vector-ref bit next)))))
                  (set! mask (arithmetic-shift mask -1))
                  (loop))))
            idx))) ; zero‑based
    (let/ec return
      (for ([i (in-range len)])
        (define rain (vector-ref rains-vec i))
        (if (= rain 0)
            (begin
              (vector-set! ans i 1)   ; placeholder, will stay 1 if never used
              (bit-add! i 1))
            (begin
              (vector-set! ans i -1)
              (when (hash-has-key? lastRain rain)
                (define prev (hash-ref lastRain rain))
                (define sumPrev (bit-sum prev))
                (define total   (bit-sum (- len 1)))
                (if (= (- total sumPrev) 0)
                    (return '())
                    (let ((pos (bit-find-kth (+ sumPrev 1)))) ; zero‑based
                      (vector-set! ans pos rain)
                      (bit-add! pos -1))))
              (hash-set! lastRain rain i)))
        )
      (return (vector->list ans)))))
```

## Erlang

```erlang
-module(solution).
-export([avoid_flood/1]).

-spec avoid_flood(Rains :: [integer()]) -> [integer()].
avoid_flood(Rains) ->
    case process(0, Rains, #{}, gb_trees:empty(), #{}) of
        {ok, AssignMap} -> build_answer(Rains, AssignMap);
        {error} -> []
    end.

process(_Idx, [], _LastRainMap, _DryTree, AssignMap) ->
    {ok, AssignMap};
process(Idx, [Day | Rest], LastRainMap, DryTree, AssignMap) ->
    case Day of
        0 ->
            NewDryTree = gb_trees:insert(Idx, true, DryTree),
            process(Idx + 1, Rest, LastRainMap, NewDryTree, AssignMap);
        Lake when is_integer(Lake) ->
            case maps:is_key(Lake, LastRainMap) of
                false ->
                    NewLast = maps:put(Lake, Idx, LastRainMap),
                    process(Idx + 1, Rest, NewLast, DryTree, AssignMap);
                true ->
                    Prev = maps:get(Lake, LastRainMap),
                    Iter = gb_trees:iterator_from(Prev + 1, DryTree),
                    case gb_trees:next(Iter) of
                        none -> {error};
                        {DryDay, _, _} ->
                            NewAssign = maps:put(DryDay, Lake, AssignMap),
                            NewDryTree = gb_trees:delete(DryDay, DryTree),
                            NewLast = maps:put(Lake, Idx, LastRainMap),
                            process(Idx + 1, Rest, NewLast, NewDryTree, NewAssign)
                    end
            end
    end.

build_answer(Rains, AssignMap) ->
    build_answer(Rains, 0, AssignMap, []).

build_answer([], _Idx, _AssignMap, Acc) ->
    lists:reverse(Acc);
build_answer([Day | Rest], Idx, AssignMap, Acc) ->
    Val = case Day of
        0 ->
            case maps:find(Idx, AssignMap) of
                {ok, Lake} -> Lake;
                error -> 1
            end;
        _ -> -1
    end,
    build_answer(Rest, Idx + 1, AssignMap, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec avoid_flood(rains :: [integer]) :: [integer]
  def avoid_flood(rains) do
    len = length(rains)
    ans_arr = :array.new(len, default: 0)

    init_state = {%{}, :gb_trees.empty(), ans_arr}

    result =
      Enum.with_index(rains)
      |> Enum.reduce_while(init_state, fn {rain, idx}, {last_seen, zero_tree, arr} ->
        if rain == 0 do
          new_tree = :gb_trees.insert(idx, true, zero_tree)
          new_arr = :array.set(idx, 1, arr)
          {:cont, {last_seen, new_tree, new_arr}}
        else
          lake = rain

          case Map.get(last_seen, lake) do
            nil ->
              new_last = Map.put(last_seen, lake, idx)
              new_arr = :array.set(idx, -1, arr)
              {:cont, {new_last, zero_tree, new_arr}}

            prev_idx ->
              it = :gb_trees.iterator_from(prev_idx + 1, zero_tree)

              case :gb_trees.next(it) do
                :none ->
                  {:halt, :impossible}

                {dry_idx, _val, _next_it} ->
                  arr1 = :array.set(dry_idx, lake, arr)
                  new_tree = :gb_trees.delete(dry_idx, zero_tree)
                  arr2 = :array.set(idx, -1, arr1)
                  new_last = Map.put(last_seen, lake, idx)
                  {:cont, {new_last, new_tree, arr2}}
              end
          end
        end
      end)

    case result do
      :impossible ->
        []

      {_last_seen, _zero_tree, final_arr} ->
        :array.to_list(final_arr)
    end
  end
end
```
