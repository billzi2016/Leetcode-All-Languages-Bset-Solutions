# 3378. Count Connected Components in LCM Graph

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct DSU {
        vector<int> parent, sz;
        DSU(int n = 0) { init(n); }
        void init(int n) {
            parent.resize(n);
            sz.assign(n, 1);
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        void unite(int a, int b) {
            a = find(a); b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) swap(a, b);
            parent[b] = a;
            sz[a] += sz[b];
        }
    };
    
    int countComponents(vector<int>& nums, int threshold) {
        int n = nums.size();
        DSU dsu(n + threshold + 1); // extra space for virtual nodes 0..threshold
        unordered_map<int,int> valToIdx;
        valToIdx.reserve(n*2);
        for (int i = 0; i < n; ++i) {
            if (nums[i] <= threshold) {
                valToIdx[nums[i]] = i;
            }
        }
        int offset = n; // virtual node id = offset + m
        for (auto &p : valToIdx) {
            int v = p.first;
            int idx = p.second;
            for (int mult = v; mult <= threshold; mult += v) {
                dsu.unite(idx, offset + mult);
            }
        }
        unordered_set<int> comps;
        comps.reserve(n*2);
        for (int i = 0; i < n; ++i) {
            if (nums[i] > threshold) {
                comps.insert(i); // isolated
            } else {
                comps.insert(dsu.find(i));
            }
        }
        return (int)comps.size();
    }
};
```

## Java

```java
class Solution {
    private static class DSU {
        int[] parent;
        int[] size;
        DSU(int n) {
            parent = new int[n + 1];
            size = new int[n + 1];
            for (int i = 0; i <= n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra;
                ra = rb;
                rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }

    public int countComponents(int[] nums, int threshold) {
        DSU dsu = new DSU(threshold);
        int largeCount = 0;

        for (int v : nums) {
            if (v > threshold) {
                largeCount++;
            } else {
                for (int m = v * 2; m <= threshold; m += v) {
                    dsu.union(v, m);
                }
            }
        }

        java.util.HashSet<Integer> roots = new java.util.HashSet<>();
        for (int v : nums) {
            if (v <= threshold) {
                roots.add(dsu.find(v));
            }
        }

        return roots.size() + largeCount;
    }
}
```

## Python

```python
class Solution(object):
    def countComponents(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        first = [-1] * (threshold + 1)

        for i, v in enumerate(nums):
            if v > threshold:
                continue
            m = v
            while m <= threshold:
                if first[m] == -1:
                    first[m] = i
                else:
                    union(i, first[m])
                m += v

        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)
```

## Python3

```python
class Solution:
    def countComponents(self, nums, threshold):
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # indices of numbers <= threshold (potentially connectable)
        small_idxs = [i for i, v in enumerate(nums) if v <= threshold]

        first_of_multiple = [-1] * (threshold + 1)

        for idx in small_idxs:
            val = nums[idx]
            step = val
            for m in range(step, threshold + 1, step):
                f = first_of_multiple[m]
                if f == -1:
                    first_of_multiple[m] = idx
                else:
                    union(idx, f)

        # count distinct components
        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)
```

## C

```c
#include <stdlib.h>

static int find_set(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_sets(int *parent, int *rank, int a, int b) {
    int ra = find_set(parent, a);
    int rb = find_set(parent, b);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rank[ra]++;
    }
}

int countComponents(int* nums, int numsSize, int threshold) {
    if (numsSize == 0) return 0;

    int *parent = (int *)malloc(numsSize * sizeof(int));
    int *rank   = (int *)calloc(numsSize, sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        parent[i] = i;
    }

    int *pos = (int *)malloc((threshold + 1) * sizeof(int));
    for (int i = 0; i <= threshold; ++i) pos[i] = -1;

    int largeCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] <= threshold) {
            pos[nums[i]] = i;
        } else {
            largeCount++;
        }
    }

    for (int d = 1; d <= threshold; ++d) {
        int firstIdx = -1;
        for (int m = d; m <= threshold; m += d) {
            int idx = pos[m];
            if (idx != -1) {
                if (firstIdx == -1) {
                    firstIdx = idx;
                } else {
                    union_sets(parent, rank, firstIdx, idx);
                }
            }
        }
    }

    char *seen = (char *)calloc(numsSize, sizeof(char));
    int smallComponents = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] <= threshold) {
            int root = find_set(parent, i);
            if (!seen[root]) {
                seen[root] = 1;
                smallComponents++;
            }
        }
    }

    free(parent);
    free(rank);
    free(pos);
    free(seen);

    return smallComponents + largeCount;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountComponents(int[] nums, int threshold)
    {
        int n = nums.Length;
        var dsu = new DSU(n);
        int[] firstIdx = new int[threshold + 1];
        for (int i = 0; i <= threshold; i++) firstIdx[i] = -1;

        for (int i = 0; i < n; i++)
        {
            int val = nums[i];
            if (val > threshold) continue;
            for (int m = val; m <= threshold; m += val)
            {
                if (firstIdx[m] == -1)
                    firstIdx[m] = i;
                else
                    dsu.Union(i, firstIdx[m]);
            }
        }

        var roots = new System.Collections.Generic.HashSet<int>();
        for (int i = 0; i < n; i++)
            roots.Add(dsu.Find(i));

        return roots.Count;
    }

    private class DSU
    {
        private readonly int[] parent;
        private readonly int[] size;

        public DSU(int n)
        {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++)
            {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int Find(int x)
        {
            while (parent[x] != x)
            {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public void Union(int a, int b)
        {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb])
            {
                parent[ra] = rb;
                size[rb] += size[ra];
            }
            else
            {
                parent[rb] = ra;
                size[ra] += size[rb];
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var countComponents = function(nums, threshold) {
    const n = nums.length;
    class DSU {
        constructor(size) {
            this.parent = new Int32Array(size);
            this.rank = new Int8Array(size);
            for (let i = 0; i < size; ++i) this.parent[i] = i;
        }
        find(x) {
            const p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a, b) {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
        }
    }

    const dsu = new DSU(n);
    // map value -> index for values <= threshold
    const pos = new Int32Array(threshold + 1);
    pos.fill(-1);
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (v <= threshold) pos[v] = i;
    }

    // For each possible L, union all numbers that divide L
    for (let L = 1; L <= threshold; ++L) {
        let firstIdx = -1;
        for (let m = L; m <= threshold; m += L) {
            const idx = pos[m];
            if (idx !== -1) {
                if (firstIdx === -1) {
                    firstIdx = idx;
                } else {
                    dsu.union(firstIdx, idx);
                }
            }
        }
    }

    const roots = new Set();
    for (let i = 0; i < n; ++i) {
        roots.add(dsu.find(i));
    }
    return roots.size;
};
```

## Typescript

```typescript
function countComponents(nums: number[], threshold: number): number {
    const n = nums.length;
    class DSU {
        parent: Int32Array;
        rank: Uint8Array;
        constructor(size: number) {
            this.parent = new Int32Array(size);
            for (let i = 0; i < size; i++) this.parent[i] = i;
            this.rank = new Uint8Array(size);
        }
        find(x: number): number {
            const p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
        }
    }

    const dsu = new DSU(n);
    const first = new Int32Array(threshold + 1);
    for (let i = 0; i <= threshold; i++) first[i] = -1;

    for (let idx = 0; idx < n; idx++) {
        const val = nums[idx];
        if (val > threshold) continue;
        for (let m = val; m <= threshold; m += val) {
            const f = first[m];
            if (f === -1) {
                first[m] = idx;
            } else {
                dsu.union(idx, f);
            }
        }
    }

    const seen = new Set<number>();
    for (let i = 0; i < n; i++) {
        seen.add(dsu.find(i));
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    private function find($x, &$parent) {
        while ($parent[$x] != $x) {
            $parent[$x] = $parent[$parent[$x]];
            $x = $parent[$x];
        }
        return $x;
    }

    private function union($a, $b, &$parent, &$rank) {
        $ra = $this->find($a, $parent);
        $rb = $this->find($b, $parent);
        if ($ra == $rb) return;
        if ($rank[$ra] < $rank[$rb]) {
            $parent[$ra] = $rb;
        } elseif ($rank[$ra] > $rank[$rb]) {
            $parent[$rb] = $ra;
        } else {
            $parent[$rb] = $ra;
            $rank[$ra]++;
        }
    }

    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function countComponents($nums, $threshold) {
        $n = count($nums);
        $parent = [];
        $rank = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $parent[$i] = $i;
        }

        // firstIdx[m] stores the index of the first number that divides m
        $firstIdx = array_fill(0, $threshold + 1, -1);

        foreach ($nums as $idx => $val) {
            if ($val > $threshold) continue; // cannot connect to any other node
            for ($m = $val; $m <= $threshold; $m += $val) {
                if ($firstIdx[$m] == -1) {
                    $firstIdx[$m] = $idx;
                } else {
                    $this->union($idx, $firstIdx[$m], $parent, $rank);
                }
            }
        }

        $components = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($this->find($i, $parent) == $i) $components++;
        }
        return $components;
    }
}
```

## Swift

```swift
class Solution {
    class DSU {
        var parent: [Int]
        var rank: [Int]
        init(_ n: Int) {
            parent = Array(0..<n)
            rank = Array(repeating: 0, count: n)
        }
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        func union(_ a: Int, _ b: Int) {
            var ra = find(a)
            var rb = find(b)
            if ra == rb { return }
            if rank[ra] < rank[rb] {
                parent[ra] = rb
            } else if rank[ra] > rank[rb] {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra] += 1
            }
        }
    }

    func countComponents(_ nums: [Int], _ threshold: Int) -> Int {
        let n = nums.count
        let dsu = DSU(n)
        if threshold == 0 { return n } // no edges possible

        var firstIdx = Array(repeating: -1, count: threshold + 1)

        for (i, num) in nums.enumerated() {
            if num > threshold { continue }
            var multiple = num
            while multiple <= threshold {
                let existing = firstIdx[multiple]
                if existing == -1 {
                    firstIdx[multiple] = i
                } else {
                    dsu.union(i, existing)
                }
                multiple += num
            }
        }

        var roots = Set<Int>()
        for i in 0..<n {
            roots.insert(dsu.find(i))
        }
        return roots.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countComponents(nums: IntArray, threshold: Int): Int {
        val n = nums.size
        val dsu = DSU(n)
        val firstIdx = IntArray(threshold + 1) { -1 }
        for (i in 0 until n) {
            val v = nums[i]
            if (v <= threshold) {
                var m = v
                while (m <= threshold) {
                    val prev = firstIdx[m]
                    if (prev == -1) {
                        firstIdx[m] = i
                    } else {
                        dsu.union(i, prev)
                    }
                    if (m > threshold - v) break
                    m += v
                }
            }
        }
        val roots = HashSet<Int>()
        for (i in 0 until n) {
            roots.add(dsu.find(i))
        }
        return roots.size
    }

    private class DSU(size: Int) {
        private val parent = IntArray(size) { it }
        private val rank = IntArray(size)

        fun find(x: Int): Int {
            var a = x
            while (parent[a] != a) {
                parent[a] = parent[parent[a]]
                a = parent[a]
            }
            return a
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank[ra] < rank[rb]) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent[rb] = ra
            if (rank[ra] == rank[rb]) rank[ra]++
        }
    }
}
```

## Dart

```dart
class DSU {
  List<int> parent;
  List<int> rank;
  DSU(int n)
      : parent = List.generate(n, (i) => i),
        rank = List.filled(n, 0);

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  void union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
      parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
      parent[rb] = ra;
    } else {
      parent[rb] = ra;
      rank[ra]++;
    }
  }
}

class Solution {
  int countComponents(List<int> nums, int threshold) {
    int n = nums.length;
    DSU dsu = DSU(n);
    int T = threshold;

    // Map value (<=T) to its index in nums
    List<int> idx = List.filled(T + 1, -1);
    for (int i = 0; i < n; ++i) {
      int v = nums[i];
      if (v <= T) idx[v] = i;
    }

    // For each multiple, keep the first index that divides it
    List<int> firstIdxForMultiple = List.filled(T + 1, -1);

    for (int val = 1; val <= T; ++val) {
      int nodeIdx = idx[val];
      if (nodeIdx == -1) continue;
      for (int mult = val; mult <= T; mult += val) {
        if (firstIdxForMultiple[mult] == -1) {
          firstIdxForMultiple[mult] = nodeIdx;
        } else {
          dsu.union(nodeIdx, firstIdxForMultiple[mult]);
        }
      }
    }

    // Count distinct components
    Set<int> roots = {};
    for (int i = 0; i < n; ++i) {
      roots.add(dsu.find(i));
    }
    return roots.length;
  }
}
```

## Golang

```go
package main

type dsu struct {
	parent []int
	rank   []byte
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	r := make([]byte, n)
	for i := 0; i < n; i++ {
		p[i] = i
	}
	return &dsu{parent: p, rank: r}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

func (d *dsu) union(a, b int) {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return
	}
	if d.rank[ra] < d.rank[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	if d.rank[ra] == d.rank[rb] {
		d.rank[ra]++
	}
}

func countComponents(nums []int, threshold int) int {
	smallIdx := make(map[int]int)
	var smallVals []int
	for _, v := range nums {
		if v <= threshold {
			smallIdx[v] = len(smallVals)
			smallVals = append(smallVals, v)
		}
	}
	m := len(smallVals)
	ds := newDSU(m)

	rep := make([]int, threshold+1)
	for i := range rep {
		rep[i] = -1
	}

	for idx, val := range smallVals {
		for mult := val; mult <= threshold; mult += val {
			if rep[mult] == -1 {
				rep[mult] = idx
			} else {
				ds.union(idx, rep[mult])
			}
		}
	}

	rootSet := make(map[int]struct{})
	for i := 0; i < m; i++ {
		r := ds.find(i)
		rootSet[r] = struct{}{}
	}
	return len(rootSet) + (len(nums) - m)
}
```

## Ruby

```ruby
def count_components(nums, threshold)
  # Map values <= threshold to indices
  idx_map = {}
  nums.each do |v|
    if v <= threshold
      idx_map[v] = idx_map.size
    end
  end

  m = idx_map.size
  # DSU for numbers <= threshold
  parent = Array.new(m) { |i| i }
  rank   = Array.new(m, 0)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
  end

  first = Array.new(threshold + 1, -1)

  idx_map.each do |value, idx|
    mult = value
    while mult <= threshold
      if first[mult] == -1
        first[mult] = idx
      else
        union.call(idx, first[mult])
      end
      mult += value
    end
  end

  # Count distinct roots among values <= threshold
  seen = {}
  idx_map.each_value do |idx|
    root = find.call(idx)
    seen[root] = true
  end
  components = seen.size

  # Add isolated nodes (values > threshold)
  isolated = nums.count { |v| v > threshold }
  components + isolated
end
```

## Scala

```scala
object Solution {
    def countComponents(nums: Array[Int], threshold: Int): Int = {
        val n = nums.length
        val parent = (0 until n).toArray
        val size = Array.fill(n)(1)

        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                parent(p) = parent(parent(p))
                p = parent(p)
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (size(ra) < size(rb)) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent(rb) = ra
            size(ra) += size(rb)
        }

        val first = Array.fill(threshold + 1)(-1)

        for (i <- 0 until n) {
            val x = nums(i)
            if (x <= threshold) {
                var m = x
                while (m <= threshold) {
                    if (first(m) == -1) first(m) = i else union(i, first(m))
                    m += x
                }
            }
        }

        val seen = scala.collection.mutable.HashSet[Int]()
        for (i <- 0 until n) {
            seen.add(find(i))
        }
        seen.size
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}
impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n { parent.push(i); }
        DSU { parent, size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }
    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb { return; }
        // union by size
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

impl Solution {
    pub fn count_components(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut dsu = DSU::new(n);
        let mut idx_map: HashMap<i32, usize> = HashMap::new();

        for (i, &v) in nums.iter().enumerate() {
            if v <= threshold {
                idx_map.insert(v, i);
            }
        }

        // For each possible divisor d, union all numbers that are multiples of d
        let t = threshold as i32;
        for d in 1..=t {
            let mut first: Option<usize> = None;
            let mut multiple = d;
            while multiple <= t {
                if let Some(&idx) = idx_map.get(&multiple) {
                    match first {
                        None => first = Some(idx),
                        Some(rep) => dsu.union(rep, idx),
                    }
                }
                multiple += d;
            }
        }

        let mut seen: HashSet<usize> = HashSet::new();
        let mut isolated_gt_thresh = 0;

        for (i, &v) in nums.iter().enumerate() {
            if v > threshold {
                isolated_gt_thresh += 1;
            } else {
                let root = dsu.find(i);
                seen.insert(root);
            }
        }

        (seen.len() + isolated_gt_thresh) as i32
    }
}
```

## Racket

```racket
(define/contract (count-components nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (parent (make-vector n))
         (size   (make-vector n 1)))
    ;; initialize DSU
    (for ([i (in-range n)])
      (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let ((ra (find a)) (rb (find b)))
        (when (not (= ra rb))
          (let ((sa (vector-ref size ra))
                (sb (vector-ref size rb)))
            (if (> sa sb)
                (begin
                  (vector-set! parent rb ra)
                  (vector-set! size ra (+ sa sb)))
                (begin
                  (vector-set! parent ra rb)
                  (vector-set! size rb (+ sb sa))))))))
    ;; map values <= threshold to their indices
    (define val->idx (make-hash))
    (for ([idx (in-range n)]
          [val  (in-list nums)])
      (when (<= val threshold)
        (hash-set! val->idx val idx)))
    ;; first index seen for each multiple
    (define firstIdx (make-vector (+ threshold 1) -1))
    ;; union numbers sharing a common multiple <= threshold
    (for ([val (in-hash-keys val->idx)])
      (let ((idx (hash-ref val->idx val)))
        (let loop ((m val))
          (when (<= m threshold)
            (let ((first (vector-ref firstIdx m)))
              (if (= first -1)
                  (vector-set! firstIdx m idx)
                  (union idx first)))
            (loop (+ m val))))))
    ;; count distinct components
    (define roots (make-hash))
    (for ([i (in-range n)])
      (hash-set! roots (find i) #t))
    (hash-count roots)))
```

## Erlang

```erlang
-module(solution).
-export([count_components/2]).

%% Public API
-spec count_components(Nums :: [integer()], Threshold :: integer()) -> integer().
count_components(Nums, Threshold) ->
    %% Initialize ETS tables for DSU
    ParentTab = ets:new(parent_tab, [named_table, public]),
    RankTab   = ets:new(rank_tab,   [named_table, public]),

    N = length(Nums),
    IdxList = lists:seq(0, N - 1),

    %% Insert each node into DSU structures
    lists:foreach(
        fun(Idx) ->
            ets:insert(parent_tab, {Idx, Idx}),
            ets:insert(rank_tab,   {Idx, 0})
        end,
        IdxList),

    %% Pair indices with values
    NumPairs = lists:zip(IdxList, Nums),

    %% Process numbers whose value <= Threshold
    FirstMap = #{},
    FinalFirstMap = process_numbers(NumPairs, Threshold, FirstMap),

    %% Count distinct roots
    RootsSet = lists:foldl(
        fun({Idx, _Val}, Acc) ->
            Root = find(Idx),
            maps:put(Root, true, Acc)
        end,
        #{},
        NumPairs),

    maps:size(RootsSet).

%% Process each number for union via multiples
-spec process_numbers([{integer(), integer()}], integer(), map()) -> map().
process_numbers([], _Threshold, FirstMap) ->
    FirstMap;
process_numbers([{Idx, Val} | Rest], Threshold, FirstMap) ->
    NewFirstMap =
        if Val =< Threshold ->
                union_multiples(Val, Idx, Threshold, FirstMap);
           true ->
                FirstMap
        end,
    process_numbers(Rest, Threshold, NewFirstMap).

%% Union current index with previous indices sharing a multiple
-spec union_multiples(integer(), integer(), integer(), map()) -> map().
union_multiples(V, Idx, Threshold, FirstMap) ->
    union_multiples_loop(V, V, Threshold, Idx, FirstMap).

-spec union_multiples_loop(integer(), integer(), integer(), integer(), map()) -> map().
union_multiples_loop(_V, M, Threshold, _Idx, FirstMap) when M > Threshold ->
    FirstMap;
union_multiples_loop(V, M, Threshold, Idx, FirstMap) ->
    case maps:get(M, FirstMap, -1) of
        -1 ->
            NewMap = maps:put(M, Idx, FirstMap),
            union_multiples_loop(V, M + V, Threshold, Idx, NewMap);
        ExistingIdx ->
            union(Idx, ExistingIdx),
            union_multiples_loop(V, M + V, Threshold, Idx, FirstMap)
    end.

%% DSU find with path compression
-spec find(integer()) -> integer().
find(I) ->
    case ets:lookup(parent_tab, I) of
        [{I, P}] when P =:= I ->
            I;
        [{I, P}] ->
            Root = find(P),
            ets:insert(parent_tab, {I, Root}),
            Root
    end.

%% DSU union by rank
-spec union(integer(), integer()) -> ok.
union(A, B) ->
    RA = find(A),
    RB = find(B),
    if RA == RB ->
            ok;
       true ->
            RankA = get_rank(RA),
            RankB = get_rank(RB),
            case RankA < RankB of
                true ->
                    ets:insert(parent_tab, {RA, RB});
                false ->
                    case RankA > RankB of
                        true ->
                            ets:insert(parent_tab, {RB, RA});
                        false -> % equal ranks
                            ets:insert(parent_tab, {RB, RA}),
                            increment_rank(RA)
                    end
            end
    end.

-spec get_rank(integer()) -> integer().
get_rank(R) ->
    [{R, Rank}] = ets:lookup(rank_tab, R),
    Rank.

-spec increment_rank(integer()) -> ok.
increment_rank(R) ->
    Rank = get_rank(R),
    ets:insert(rank_tab, {R, Rank + 1}),
    ok.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_components(nums :: [integer], threshold :: integer) :: integer
  def count_components(nums, threshold) do
    indexed = Enum.with_index(nums)

    # Separate numbers <= threshold and > threshold
    {small, big_count} =
      Enum.reduce(indexed, {[], 0}, fn {num, idx}, {s_acc, b_cnt} ->
        if num <= threshold do
          {[{num, idx} | s_acc], b_cnt}
        else
          {s_acc, b_cnt + 1}
        end
      end)

    # Initialize DSU structures for small numbers
    parent = Enum.reduce(small, %{}, fn {_num, idx}, acc -> Map.put(acc, idx, idx) end)
    rank = Enum.reduce(small, %{}, fn {_num, idx}, acc -> Map.put(acc, idx, 1) end)

    # Array to store first index seen for each multiple
    rep_arr = :array.from_list(List.duplicate(-1, threshold + 1))

    {parent_final, rank_final, _rep_arr} =
      Enum.reduce(small, {parent, rank, rep_arr}, fn {num, idx}, {par, rk, arr} ->
        process_multiples(num, idx, num, threshold, par, rk, arr)
      end)

    # Count distinct roots among small numbers
    root_set =
      Enum.reduce(small, MapSet.new(), fn {_num, idx}, set ->
        root = get_root(parent_final, idx)
        MapSet.put(set, root)
      end)

    MapSet.size(root_set) + big_count
  end

  # Recursively process multiples of a number
  defp process_multiples(_num, _idx, m, max, parent, rank, arr) when m > max do
    {parent, rank, arr}
  end

  defp process_multiples(num, idx, m, max, parent, rank, arr) do
    existing = :array.get(m, arr)

    if existing == -1 do
      arr2 = :array.set(m, idx, arr)
      process_multiples(num, idx, m + num, max, parent, rank, arr2)
    else
      {parent2, rank2} = union(parent, rank, idx, existing)
      process_multiples(num, idx, m + num, max, parent2, rank2, arr)
    end
  end

  # Find with path compression (returns updated map and root)
  defp find(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      {parent, x}
    else
      {parent1, root} = find(parent, p)
      parent2 = Map.put(parent1, x, root)
      {parent2, root}
    end
  end

  # Get root without modifying the map (used for final counting)
  defp get_root(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      x
    else
      get_root(parent, p)
    end
  end

  # Union by size
  defp union(parent, rank, a, b) do
    {parent1, ra} = find(parent, a)
    {parent2, rb} = find(parent1, b)

    if ra == rb do
      {parent2, rank}
    else
      size_a = Map.get(rank, ra)
      size_b = Map.get(rank, rb)

      cond do
        size_a < size_b ->
          parent3 = Map.put(parent2, ra, rb)
          rank3 = Map.put(rank, rb, size_a + size_b)
          {parent3, rank3}

        true ->
          parent3 = Map.put(parent2, rb, ra)
          rank3 = Map.put(rank, ra, size_a + size_b)
          {parent3, rank3}
      end
    end
  end
end
```
