# 1722. Minimize Hamming Distance After Swap Operations

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        DSU(int n): p(n), sz(n,1) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(sz[a]<sz[b]) swap(a,b);
            p[b]=a; sz[a]+=sz[b];
        }
    };
    
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        DSU dsu(n);
        for (auto &e : allowedSwaps) dsu.unite(e[0], e[1]);
        
        unordered_map<int, vector<int>> groups;
        groups.reserve(n*2);
        for (int i = 0; i < n; ++i) {
            int r = dsu.find(i);
            groups[r].push_back(i);
        }
        
        int ans = 0;
        for (auto &kv : groups) {
            const vector<int> &idxs = kv.second;
            unordered_map<int,int> cnt;
            cnt.reserve(idxs.size()*2);
            for (int idx : idxs) ++cnt[source[idx]];
            
            int matched = 0;
            for (int idx : idxs) {
                auto it = cnt.find(target[idx]);
                if (it != cnt.end() && it->second > 0) {
                    --(it->second);
                    ++matched;
                }
            }
            ans += (int)idxs.size() - matched;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class UnionFind {
        int[] parent;
        int[] rank;
        UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
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

    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;
        UnionFind uf = new UnionFind(n);
        for (int[] swap : allowedSwaps) {
            uf.union(swap[0], swap[1]);
        }

        // Map from root to frequency difference map
        java.util.Map<Integer, java.util.HashMap<Integer, Integer>> compDiff = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            int root = uf.find(i);
            java.util.HashMap<Integer, Integer> diffMap = compDiff.computeIfAbsent(root, k -> new java.util.HashMap<>());
            diffMap.put(source[i], diffMap.getOrDefault(source[i], 0) + 1);
            diffMap.put(target[i], diffMap.getOrDefault(target[i], 0) - 1);
        }

        int mismatches = 0;
        for (java.util.HashMap<Integer, Integer> map : compDiff.values()) {
            for (int cnt : map.values()) {
                if (cnt > 0) mismatches += cnt; // positive surplus in source cannot be matched
            }
        }
        return mismatches;
    }
}
```

## Python

```python
class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
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

        for a, b in allowedSwaps:
            union(a, b)

        from collections import defaultdict, Counter

        comps = defaultdict(list)
        for i in range(n):
            comps[find(i)].append(i)

        ans = 0
        for indices in comps.values():
            src_cnt = Counter()
            tgt_cnt = Counter()
            for idx in indices:
                src_cnt[source[idx]] += 1
                tgt_cnt[target[idx]] += 1
            matches = sum(min(src_cnt[val], tgt_cnt.get(val, 0)) for val in src_cnt)
            ans += len(indices) - matches

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict, Counter

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = DSU(n)
        for a, b in allowedSwaps:
            dsu.union(a, b)

        src_cnt = defaultdict(Counter)   # root -> Counter of source values
        tgt_cnt = defaultdict(Counter)   # root -> Counter of target values

        for i in range(n):
            r = dsu.find(i)
            src_cnt[r][source[i]] += 1
            tgt_cnt[r][target[i]] += 1

        mismatches = 0
        for r, sc in src_cnt.items():
            tc = tgt_cnt[r]
            matched = 0
            for val, cnt in sc.items():
                matched += min(cnt, tc.get(val, 0))
            component_size = sum(sc.values())
            mismatches += component_size - matched

        return mismatches
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} Vec;

static int find(int *parent, int x) {
    if (parent[x] != x) parent[x] = find(parent, parent[x]);
    return parent[x];
}

static void unite(int *parent, int *rank, int a, int b) {
    int ra = find(parent, a);
    int rb = find(parent, b);
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

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int minimumHammingDistance(int* source, int sourceSize, int* target, int targetSize,
                           int** allowedSwaps, int allowedSwapsSize, int* allowedSwapsColSize) {
    int n = sourceSize;
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    for (int i = 0; i < allowedSwapsSize; ++i) {
        int a = allowedSwaps[i][0];
        int b = allowedSwaps[i][1];
        unite(parent, rank, a, b);
    }

    Vec *comps = (Vec *)calloc(n, sizeof(Vec));
    for (int i = 0; i < n; ++i) {
        int r = find(parent, i);
        Vec *v = &comps[r];
        if (v->capacity == 0) {
            v->capacity = 4;
            v->data = (int *)malloc(v->capacity * sizeof(int));
        } else if (v->size == v->capacity) {
            v->capacity <<= 1;
            v->data = (int *)realloc(v->data, v->capacity * sizeof(int));
        }
        v->data[v->size++] = i;
    }

    int mismatches = 0;
    for (int i = 0; i < n; ++i) {
        if (comps[i].size == 0) continue;
        int sz = comps[i].size;
        int *srcVals = (int *)malloc(sz * sizeof(int));
        int *tgtVals = (int *)malloc(sz * sizeof(int));
        for (int j = 0; j < sz; ++j) {
            int idx = comps[i].data[j];
            srcVals[j] = source[idx];
            tgtVals[j] = target[idx];
        }
        qsort(srcVals, sz, sizeof(int), cmp_int);
        qsort(tgtVals, sz, sizeof(int), cmp_int);

        int p = 0, q = 0;
        while (p < sz && q < sz) {
            if (srcVals[p] == tgtVals[q]) {
                ++p; ++q;
            } else if (srcVals[p] < tgtVals[q]) {
                ++mismatches;
                ++p;
            } else {
                ++mismatches;
                ++q;
            }
        }
        mismatches += (sz - p) + (sz - q);
        free(srcVals);
        free(tgtVals);
    }

    for (int i = 0; i < n; ++i) {
        free(comps[i].data);
    }
    free(comps);
    free(parent);
    free(rank);
    return mismatches;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.Length;
        DSU dsu = new DSU(n);
        foreach (var swap in allowedSwaps) {
            dsu.Union(swap[0], swap[1]);
        }

        var groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int root = dsu.Find(i);
            if (!groups.ContainsKey(root)) groups[root] = new List<int>();
            groups[root].Add(i);
        }

        int mismatches = 0;
        foreach (var kv in groups) {
            var indices = kv.Value;
            var freq = new Dictionary<int, int>();
            foreach (int idx in indices) {
                int val = source[idx];
                if (!freq.ContainsKey(val)) freq[val] = 0;
                freq[val]++;
            }
            foreach (int idx in indices) {
                int tval = target[idx];
                if (freq.TryGetValue(tval, out int cnt) && cnt > 0) {
                    freq[tval] = cnt - 1;
                } else {
                    mismatches++;
                }
            }
        }

        return mismatches;
    }

    private class DSU {
        private readonly int[] parent;
        private readonly int[] size;

        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public void Union(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                parent[ra] = rb;
                size[rb] += size[ra];
            } else {
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
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
var minimumHammingDistance = function(source, target, allowedSwaps) {
    const n = source.length;
    const parent = new Array(n);
    const size = new Array(n).fill(1);
    for (let i = 0; i < n; ++i) parent[i] = i;

    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const union = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (size[ra] < size[rb]) {
            [ra, rb] = [rb, ra];
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    };

    for (const [a, b] of allowedSwaps) {
        union(a, b);
    }

    const compMap = new Map(); // root -> Map(value -> count in source)
    for (let i = 0; i < n; ++i) {
        const r = find(i);
        let m = compMap.get(r);
        if (!m) {
            m = new Map();
            compMap.set(r, m);
        }
        const val = source[i];
        m.set(val, (m.get(val) || 0) + 1);
    }

    let mismatches = 0;
    for (let i = 0; i < n; ++i) {
        const r = find(i);
        const m = compMap.get(r);
        const tval = target[i];
        if (m.has(tval) && m.get(tval) > 0) {
            m.set(tval, m.get(tval) - 1);
        } else {
            mismatches++;
        }
    }

    return mismatches;
};
```

## Typescript

```typescript
function minimumHammingDistance(source: number[], target: number[], allowedSwaps: number[][]): number {
    const n = source.length;
    class DSU {
        parent: number[];
        rank: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x: number): number {
            if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
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
    for (const [a, b] of allowedSwaps) {
        dsu.union(a, b);
    }

    const compMap = new Map<number, Map<number, number>>();
    for (let i = 0; i < n; i++) {
        const root = dsu.find(i);
        let map = compMap.get(root);
        if (!map) {
            map = new Map<number, number>();
            compMap.set(root, map);
        }
        const sVal = source[i];
        const tVal = target[i];
        map.set(sVal, (map.get(sVal) ?? 0) + 1);
        map.set(tVal, (map.get(tVal) ?? 0) - 1);
    }

    let mismatches = 0;
    for (const freqMap of compMap.values()) {
        for (const diff of freqMap.values()) {
            if (diff > 0) mismatches += diff;
        }
    }
    return mismatches;
}
```

## Php

```php
class Solution {
    private array $parent = [];
    private array $rank = [];

    private function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    private function union(int $x, int $y): void {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx === $ry) {
            return;
        }
        if ($this->rank[$rx] < $this->rank[$ry]) {
            $this->parent[$rx] = $ry;
        } elseif ($this->rank[$rx] > $this->rank[$ry]) {
            $this->parent[$ry] = $rx;
        } else {
            $this->parent[$ry] = $rx;
            $this->rank[$rx]++;
        }
    }

    /**
     * @param Integer[] $source
     * @param Integer[] $target
     * @param Integer[][] $allowedSwaps
     * @return Integer
     */
    function minimumHammingDistance($source, $target, $allowedSwaps) {
        $n = count($source);
        $this->parent = range(0, $n - 1);
        $this->rank   = array_fill(0, $n, 0);

        foreach ($allowedSwaps as $swap) {
            $this->union($swap[0], $swap[1]);
        }

        $compSource = [];
        $compTarget = [];

        for ($i = 0; $i < $n; $i++) {
            $root = $this->find($i);
            $valS = $source[$i];
            $valT = $target[$i];

            if (!isset($compSource[$root])) {
                $compSource[$root] = [];
                $compTarget[$root] = [];
            }

            $compSource[$root][$valS] = ($compSource[$root][$valS] ?? 0) + 1;
            $compTarget[$root][$valT] = ($compTarget[$root][$valT] ?? 0) + 1;
        }

        $ans = 0;
        foreach ($compSource as $root => $srcMap) {
            $tgtMap = $compTarget[$root];
            $total   = array_sum($srcMap);
            $matched = 0;
            foreach ($srcMap as $val => $cntS) {
                if (isset($tgtMap[$val])) {
                    $matched += min($cntS, $tgtMap[$val]);
                }
            }
            $ans += $total - $matched;
        }

        return $ans;
    }
}
```

## Swift

```swift
class DSU {
    private var parent: [Int]
    private var size: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) {
        var rootX = find(x)
        var rootY = find(y)
        if rootX == rootY { return }
        if size[rootX] < size[rootY] {
            swap(&rootX, &rootY)
        }
        parent[rootY] = rootX
        size[rootX] += size[rootY]
    }
}

class Solution {
    func minimumHammingDistance(_ source: [Int], _ target: [Int], _ allowedSwaps: [[Int]]) -> Int {
        let n = source.count
        let dsu = DSU(n)
        for swap in allowedSwaps {
            dsu.union(swap[0], swap[1])
        }

        var componentMap = [Int: [Int: Int]]()
        for i in 0..<n {
            let root = dsu.find(i)
            var dict = componentMap[root] ?? [:]
            dict[source[i], default: 0] += 1
            dict[target[i], default: 0] -= 1
            componentMap[root] = dict
        }

        var result = 0
        for (_, freq) in componentMap {
            for (_, count) in freq where count > 0 {
                result += count
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumHammingDistance(source: IntArray, target: IntArray, allowedSwaps: Array<IntArray>): Int {
        val n = source.size
        val dsu = DSU(n)
        for (swap in allowedSwaps) {
            dsu.union(swap[0], swap[1])
        }
        val groups = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            val root = dsu.find(i)
            groups.getOrPut(root) { mutableListOf() }.add(i)
        }
        var result = 0
        for (indices in groups.values) {
            val countMap = HashMap<Int, Int>()
            for (idx in indices) {
                val v = source[idx]
                countMap[v] = countMap.getOrDefault(v, 0) + 1
            }
            for (idx in indices) {
                val v = target[idx]
                val cnt = countMap.getOrDefault(v, 0)
                if (cnt > 0) {
                    if (cnt == 1) {
                        countMap.remove(v)
                    } else {
                        countMap[v] = cnt - 1
                    }
                } else {
                    result++
                }
            }
        }
        return result
    }

    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val size = IntArray(n) { 1 }

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (size[ra] < size[rb]) {
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent[rb] = ra
            size[ra] += size[rb]
        }
    }
}
```

## Dart

```dart
class Solution {
  int minimumHammingDistance(List<int> source, List<int> target,
      List<List<int>> allowedSwaps) {
    int n = source.length;
    var dsu = _DSU(n);
    for (var pair in allowedSwaps) {
      dsu.union(pair[0], pair[1]);
    }

    // Group indices by their component root
    Map<int, List<int>> groups = {};
    for (int i = 0; i < n; i++) {
      int root = dsu.find(i);
      groups.putIfAbsent(root, () => []).add(i);
    }

    int mismatches = 0;
    for (var indices in groups.values) {
      if (indices.length == 1) {
        int idx = indices[0];
        if (source[idx] != target[idx]) mismatches++;
        continue;
      }
      // Count frequencies of source values within this component
      Map<int, int> freq = {};
      for (int idx in indices) {
        int val = source[idx];
        freq[val] = (freq[val] ?? 0) + 1;
      }
      // Try to match each target value with the multiset from source
      for (int idx in indices) {
        int val = target[idx];
        if (freq.containsKey(val) && freq[val]! > 0) {
          freq[val] = freq[val]! - 1;
        } else {
          mismatches++;
        }
      }
    }

    return mismatches;
  }
}

class _DSU {
  late List<int> parent;
  late List<int> rank;

  _DSU(int size) {
    parent = List.generate(size, (i) => i);
    rank = List.filled(size, 0);
  }

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void union(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);
    if (rootX == rootY) return;
    if (rank[rootX] < rank[rootY]) {
      parent[rootX] = rootY;
    } else if (rank[rootX] > rank[rootY]) {
      parent[rootY] = rootX;
    } else {
      parent[rootY] = rootX;
      rank[rootX]++;
    }
  }
}
```

## Golang

```go
func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    n := len(source)
    parent := make([]int, n)
    rank := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = i
    }
    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra == rb {
            return
        }
        if rank[ra] < rank[rb] {
            parent[ra] = rb
        } else if rank[ra] > rank[rb] {
            parent[rb] = ra
        } else {
            parent[rb] = ra
            rank[ra]++
        }
    }

    for _, sw := range allowedSwaps {
        union(sw[0], sw[1])
    }

    // map from component root to frequency map of source values
    compFreq := make(map[int]map[int]int)
    for i, val := range source {
        r := find(i)
        if _, ok := compFreq[r]; !ok {
            compFreq[r] = make(map[int]int)
        }
        compFreq[r][val]++
    }

    mismatches := 0
    for i, val := range target {
        r := find(i)
        freqMap := compFreq[r]
        if cnt, ok := freqMap[val]; ok && cnt > 0 {
            freqMap[val]--
        } else {
            mismatches++
        }
    }

    return mismatches
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(x, y)
    rx = find(x)
    ry = find(y)
    return if rx == ry
    if @rank[rx] < @rank[ry]
      @parent[rx] = ry
    elsif @rank[rx] > @rank[ry]
      @parent[ry] = rx
    else
      @parent[ry] = rx
      @rank[rx] += 1
    end
  end
end

def minimum_hamming_distance(source, target, allowed_swaps)
  n = source.length
  dsu = DSU.new(n)
  allowed_swaps.each { |a, b| dsu.union(a, b) }

  src_counts = Hash.new { |h, k| h[k] = Hash.new(0) }
  tgt_counts = Hash.new { |h, k| h[k] = Hash.new(0) }

  (0...n).each do |i|
    root = dsu.find(i)
    src_counts[root][source[i]] += 1
    tgt_counts[root][target[i]] += 1
  end

  mismatches = 0
  src_counts.each_key do |root|
    sc = src_counts[root]
    tc = tgt_counts[root]
    matches = 0
    sc.each do |val, cnt|
      tcnt = tc[val]
      matches += [cnt, tcnt].min if tcnt && tcnt > 0
    end
    size = sc.values.sum
    mismatches += size - matches
  end

  mismatches
end
```

## Scala

```scala
object Solution {
    def minimumHammingDistance(source: Array[Int], target: Array[Int], allowedSwaps: Array[Array[Int]]): Int = {
        val n = source.length
        class DSU(val n: Int) {
            private val parent = (0 until n).toArray
            private val size   = Array.fill(n)(1)

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
        }

        val dsu = new DSU(n)
        var i = 0
        while (i < allowedSwaps.length) {
            val p = allowedSwaps(i)
            dsu.union(p(0), p(1))
            i += 1
        }

        import scala.collection.mutable

        val compMap = mutable.HashMap[Int, mutable.HashMap[Int, Int]]()

        var idx = 0
        while (idx < n) {
            val root = dsu.find(idx)
            val map = compMap.getOrElseUpdate(root, mutable.HashMap[Int, Int]())
            map(source(idx)) = map.getOrElse(source(idx), 0) + 1
            idx += 1
        }

        idx = 0
        while (idx < n) {
            val root = dsu.find(idx)
            val map = compMap(root)
            map(target(idx)) = map.getOrElse(target(idx), 0) - 1
            idx += 1
        }

        var mismatches = 0
        for ((_, m) <- compMap) {
            for ((_, cnt) <- m) {
                if (cnt > 0) mismatches += cnt
            }
        }
        mismatches
    }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        let rank = vec![0; n];
        DSU { parent, rank }
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
        if ra == rb {
            return;
        }
        if self.rank[ra] < self.rank[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        if self.rank[ra] == self.rank[rb] {
            self.rank[ra] += 1;
        }
    }
}

impl Solution {
    pub fn minimum_hamming_distance(
        source: Vec<i32>,
        target: Vec<i32>,
        allowed_swaps: Vec<Vec<i32>>,
    ) -> i32 {
        let n = source.len();
        let mut dsu = DSU::new(n);
        for pair in allowed_swaps.iter() {
            let a = pair[0] as usize;
            let b = pair[1] as usize;
            dsu.union(a, b);
        }

        // Group indices by their component root
        let mut groups: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            let root = dsu.find(i);
            groups.entry(root).or_default().push(i);
        }

        let mut ans = 0i32;
        for indices in groups.values() {
            let mut cnt: HashMap<i32, i32> = HashMap::new();
            // Count source values in this component
            for &idx in indices.iter() {
                *cnt.entry(source[idx]).or_insert(0) += 1;
            }
            // Match with target values
            for &idx in indices.iter() {
                let entry = cnt.entry(target[idx]).or_insert(0);
                if *entry > 0 {
                    *entry -= 1;
                } else {
                    ans += 1;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (minimum-hamming-distance source target allowedSwaps)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length source)]
         [src-vec (list->vector source)]
         [tgt-vec (list->vector target)]
         [parent (make-vector n (lambda (i) i))]
         [sz (make-vector n 1)])

    ;; find with path compression
    (define (find x)
      (let loop ((x x))
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root)))))

    ;; union by size
    (define (union a b)
      (let* ([ra (find a)]
             [rb (find b)])
        (when (not (= ra rb))
          (let ([size-a (vector-ref sz ra)]
                [size-b (vector-ref sz rb)])
            (if (> size-a size-b)
                (begin
                  (vector-set! parent rb ra)
                  (vector-set! sz ra (+ size-a size-b)))
                (begin
                  (vector-set! parent ra rb)
                  (vector-set! sz rb (+ size-a size-b))))))))

    ;; process allowed swaps
    (for ([pair allowedSwaps])
      (union (first pair) (second pair)))

    ;; map from component root to frequency hashmap
    (define comp-map (make-hash))

    (for ([i (in-range n)])
      (let* ([root (find i)]
             [freq (or (hash-ref comp-map root #f)
                       (let ([new (make-hash)])
                         (hash-set! comp-map root new)
                         new))])
        (define src-val (vector-ref src-vec i))
        (define tgt-val (vector-ref tgt-vec i))
        (hash-set! freq src-val (+ (hash-ref freq src-val 0) 1))
        (hash-set! freq tgt-val (- (hash-ref freq tgt-val 0) 1))))

    ;; compute mismatches
    (let ([total 0])
      (for ([freq (in-hash-values comp-map)])
        (for ([cnt (in-hash-values freq)])
          (when (> cnt 0)
            (set! total (+ total cnt)))))
      total)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_hamming_distance/3]).

-spec minimum_hamming_distance(Source :: [integer()], Target :: [integer()], AllowedSwaps :: [[integer()]]) -> integer().
minimum_hamming_distance(Source, Target, AllowedSwaps) ->
    N = length(Source),
    SourceTuple = list_to_tuple(Source),
    TargetTuple = list_to_tuple(Target),
    Adj = build_adj(AllowedSwaps, #{}),
    Indices = lists:seq(0, N - 1),
    {_, Distance} = lists:foldl(
        fun(Index, {Visited, Dist}) ->
            case maps:is_key(Index, Visited) of
                true -> {Visited, Dist};
                false ->
                    {ComponentIndices, NewVisited} = dfs_collect([Index], Adj, Visited, []),
                    ComponentSize = length(ComponentIndices),
                    SourceCountMap = build_source_counts(ComponentIndices, SourceTuple, #{}),
                    Matches = count_matches(ComponentIndices, TargetTuple, SourceCountMap, 0),
                    MismatchComp = ComponentSize - Matches,
                    {NewVisited, Dist + MismatchComp}
            end
        end,
        {#{}, 0},
        Indices),
    Distance.

build_adj([], Adj) -> Adj;
build_adj([[A, B] | Rest], Adj) ->
    Adj1 = maps:update_with(
        A,
        fun(L) -> [B | L] end,
        [B],
        Adj
    ),
    Adj2 = maps:update_with(
        B,
        fun(L) -> [A | L] end,
        [A],
        Adj1
    ),
    build_adj(Rest, Adj2).

dfs_collect([], _Adj, Visited, Acc) ->
    {Acc, Visited};
dfs_collect([H | T], Adj, Visited, Acc) ->
    case maps:is_key(H, Visited) of
        true ->
            dfs_collect(T, Adj, Visited, Acc);
        false ->
            NewVisited = maps:put(H, true, Visited),
            Neigh = maps:get(H, Adj, []),
            NewStack = Neigh ++ T,
            dfs_collect(NewStack, Adj, NewVisited, [H | Acc])
    end.

build_source_counts([], _SourceTuple, CountMap) -> CountMap;
build_source_counts([Idx | Rest], SourceTuple, CountMap) ->
    Val = element(Idx + 1, SourceTuple),
    NewCountMap = maps:update_with(
        Val,
        fun(C) -> C + 1 end,
        1,
        CountMap
    ),
    build_source_counts(Rest, SourceTuple, NewCountMap).

count_matches([], _TargetTuple, _CountMap, Matches) -> Matches;
count_matches([Idx | Rest], TargetTuple, CountMap, Matches) ->
    Val = element(Idx + 1, TargetTuple),
    case maps:find(Val, CountMap) of
        {ok, C} when C > 0 ->
            NewC = C - 1,
            UpdatedCountMap =
                if
                    NewC == 0 -> maps:remove(Val, CountMap);
                    true -> maps:put(Val, NewC, CountMap)
                end,
            count_matches(Rest, TargetTuple, UpdatedCountMap, Matches + 1);
        _ ->
            count_matches(Rest, TargetTuple, CountMap, Matches)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_hamming_distance(source :: [integer], target :: [integer], allowed_swaps :: [[integer]]) :: integer
  def minimum_hamming_distance(source, target, allowed_swaps) do
    n = length(source)

    # initialize DSU parent and size maps
    parent =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, i)
      end)

    size =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, 1)
      end)

    # process all allowed swaps
    {parent_final, _size_final} =
      Enum.reduce(allowed_swaps, {parent, size}, fn [a, b], {p, s} ->
        union(p, s, a, b)
      end)

    # map index -> target value for O(1) lookup
    target_idx_map =
      Enum.with_index(target)
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, i, v) end)

    # first pass: count source values per component
    {comp_counts, _} =
      Enum.with_index(source)
      |> Enum.reduce({%{}, parent_final}, fn {src_val, idx}, {counts, pmap} ->
        {root, pmap2} = find(pmap, idx)
        comp_map = Map.get(counts, root, %{})
        new_comp_map = Map.update(comp_map, src_val, 1, &(&1 + 1))
        {Map.put(counts, root, new_comp_map), pmap2}
      end)

    # second pass: match target values against component counts
    {mismatch, _ , _} =
      Enum.reduce(0..(n - 1), {0, parent_final, comp_counts}, fn idx, {mis, pmap, counts} ->
        {root, pmap2} = find(pmap, idx)
        tgt_val = Map.get(target_idx_map, idx)
        comp_map = Map.get(counts, root, %{})
        case Map.get(comp_map, tgt_val, 0) do
          0 ->
            {mis + 1, pmap2, counts}
          cnt ->
            new_comp_map =
              if cnt == 1 do
                Map.delete(comp_map, tgt_val)
              else
                Map.put(comp_map, tgt_val, cnt - 1)
              end

            new_counts = Map.put(counts, root, new_comp_map)
            {mis, pmap2, new_counts}
        end
      end)

    mismatch
  end

  # Find with path compression
  defp find(parent, x) do
    case Map.get(parent, x) do
      ^x = root -> {root, parent}
      p ->
        {root, parent2} = find(parent, p)
        {root, Map.put(parent2, x, root)}
    end
  end

  # Union by size
  defp union(parent, size, a, b) do
    {ra, parent1} = find(parent, a)
    {rb, parent2} = find(parent1, b)

    if ra == rb do
      {parent2, size}
    else
      sz_a = Map.get(size, ra)
      sz_b = Map.get(size, rb)

      cond do
        sz_a < sz_b ->
          new_parent = Map.put(parent2, ra, rb)
          new_size = size |> Map.put(rb, sz_a + sz_b) |> Map.delete(ra)
          {new_parent, new_size}

        true ->
          new_parent = Map.put(parent2, rb, ra)
          new_size = size |> Map.put(ra, sz_a + sz_b) |> Map.delete(rb)
          {new_parent, new_size}
      end
    end
  end
end
```
