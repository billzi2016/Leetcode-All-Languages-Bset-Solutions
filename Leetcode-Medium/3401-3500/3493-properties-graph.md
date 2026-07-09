# 3493. Properties Graph

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n), r(n,0) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(r[a]<r[b]) swap(a,b);
            p[b]=a;
            if(r[a]==r[b]) r[a]++;
        }
    };
    
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        const int MAXV = 100;
        vector<array<char,101>> has(n);
        for(int i=0;i<n;++i){
            has[i].fill(0);
            for(int v: properties[i]){
                if(v>=1 && v<=MAXV) has[i][v]=1;
            }
        }
        DSU dsu(n);
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                int cnt = 0;
                for(int v=1; v<=MAXV && cnt<k; ++v){
                    if(has[i][v] && has[j][v]) ++cnt;
                }
                if(cnt>=k) dsu.unite(i,j);
            }
        }
        unordered_set<int> comps;
        for(int i=0;i<n;++i) comps.insert(dsu.find(i));
        return (int)comps.size();
    }
};
```

## Java

```java
class Solution {
    public int numberOfComponents(int[][] properties, int k) {
        int n = properties.length;
        java.util.BitSet[] sets = new java.util.BitSet[n];
        for (int i = 0; i < n; i++) {
            java.util.BitSet bs = new java.util.BitSet(101);
            for (int v : properties[i]) {
                bs.set(v);
            }
            sets[i] = bs;
        }

        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                java.util.BitSet intersect = (java.util.BitSet) sets[i].clone();
                intersect.and(sets[j]);
                if (intersect.cardinality() >= k) {
                    dsu.union(i, j);
                }
            }
        }

        int components = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.find(i) == i) components++;
        }
        return components;
    }

    private static class DSU {
        int[] parent;
        int[] rank;

        DSU(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
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
}
```

## Python

```python
class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(properties)
        # Convert each list to a set for fast intersection
        sets = [set(row) for row in properties]

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        for i in range(n):
            si = sets[i]
            for j in range(i + 1, n):
                if len(si & sets[j]) >= k:
                    union(i, j)

        # Count distinct roots
        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)
```

## Python3

```python
from typing import List

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        sets = [set(row) for row in properties]
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for i in range(n):
            si = sets[i]
            for j in range(i + 1, n):
                if len(si & sets[j]) >= k:
                    union(i, j)

        return len({find(i) for i in range(n)})
```

## C

```c
#include <stdlib.h>

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

int numberOfComponents(int** properties, int propertiesSize, int* propertiesColSize, int k) {
    const int MAXV = 100;
    // presence matrix
    char (*present)[MAXV + 1] = (char (*)[MAXV + 1])calloc(propertiesSize * (MAXV + 1), sizeof(char));
    for (int i = 0; i < propertiesSize; ++i) {
        int cols = propertiesColSize[i];
        for (int j = 0; j < cols; ++j) {
            int val = properties[i][j];
            if (val >= 1 && val <= MAXV)
                present[i][val] = 1;
        }
    }

    // DSU init
    int *parent = (int *)malloc(propertiesSize * sizeof(int));
    int *rank   = (int *)calloc(propertiesSize, sizeof(int));
    for (int i = 0; i < propertiesSize; ++i) parent[i] = i;

    // build edges based on intersection size >= k
    for (int i = 0; i < propertiesSize; ++i) {
        for (int j = i + 1; j < propertiesSize; ++j) {
            int common = 0;
            for (int v = 1; v <= MAXV && common < k; ++v) {
                if (present[i][v] && present[j][v]) ++common;
            }
            if (common >= k) unite(parent, rank, i, j);
        }
    }

    // count distinct components
    char seen[101] = {0};
    int components = 0;
    for (int i = 0; i < propertiesSize; ++i) {
        int root = find(parent, i);
        if (!seen[root]) {
            seen[root] = 1;
            ++components;
        }
    }

    free(present);
    free(parent);
    free(rank);
    return components;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumberOfComponents(int[][] properties, int k) {
        int n = properties.Length;
        var sets = new List<HashSet<int>>(n);
        for (int i = 0; i < n; i++) {
            var hs = new HashSet<int>();
            foreach (var v in properties[i]) hs.Add(v);
            sets.Add(hs);
        }

        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                var setA = sets[i];
                var setB = sets[j];
                int cnt = 0;
                if (setA.Count < setB.Count) {
                    foreach (var v in setA) {
                        if (setB.Contains(v)) {
                            cnt++;
                            if (cnt >= k) break;
                        }
                    }
                } else {
                    foreach (var v in setB) {
                        if (setA.Contains(v)) {
                            cnt++;
                            if (cnt >= k) break;
                        }
                    }
                }
                if (cnt >= k) dsu.Union(i, j);
            }
        }

        return dsu.CountSets();
    }

    private class DSU {
        private int[] parent;
        private int[] rank;

        public DSU(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
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
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb;
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra;
            } else {
                parent[rb] = ra;
                rank[ra]++;
            }
        }

        public int CountSets() {
            var roots = new HashSet<int>();
            for (int i = 0; i < parent.Length; i++) {
                roots.Add(Find(i));
            }
            return roots.Count;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} properties
 * @param {number} k
 * @return {number}
 */
var numberOfComponents = function(properties, k) {
    const n = properties.length;
    // Build sets of distinct values for each property list
    const sets = properties.map(arr => new Set(arr));
    
    class DSU {
        constructor(size) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; ++i) this.parent[i] = i;
        }
        find(x) {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
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
    
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            // compute intersection size with early stop
            let cnt = 0;
            const setA = sets[i];
            const setB = sets[j];
            // iterate over smaller set
            if (setA.size > setB.size) {
                for (let val of setB) {
                    if (setA.has(val)) {
                        cnt++;
                        if (cnt >= k) break;
                    }
                }
            } else {
                for (let val of setA) {
                    if (setB.has(val)) {
                        cnt++;
                        if (cnt >= k) break;
                    }
                }
            }
            if (cnt >= k) dsu.union(i, j);
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
function numberOfComponents(properties: number[][], k: number): number {
    const n = properties.length;
    const sets: Set<number>[] = new Array(n);
    for (let i = 0; i < n; i++) {
        sets[i] = new Set(properties[i]);
    }

    const parent = new Int32Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
        const ra = find(a);
        const rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let cnt = 0;
            const setA = sets[i];
            const setB = sets[j];
            if (setA.size < setB.size) {
                for (const v of setA) {
                    if (setB.has(v)) {
                        cnt++;
                        if (cnt >= k) break;
                    }
                }
            } else {
                for (const v of setB) {
                    if (setA.has(v)) {
                        cnt++;
                        if (cnt >= k) break;
                    }
                }
            }
            if (cnt >= k) union(i, j);
        }
    }

    const roots = new Set<number>();
    for (let i = 0; i < n; i++) roots.add(find(i));
    return roots.size;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $properties
     * @param Integer $k
     * @return Integer
     */
    function numberOfComponents($properties, $k) {
        $n = count($properties);
        // Build sets for each property list
        $sets = [];
        for ($i = 0; $i < $n; $i++) {
            $set = [];
            foreach ($properties[$i] as $val) {
                $set[$val] = true;
            }
            $sets[$i] = $set;
        }

        // Initialize DSU
        $parent = range(0, $n - 1);

        // Process all pairs
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $cnt = 0;
                // iterate over smaller set for efficiency
                if (count($sets[$i]) <= count($sets[$j])) {
                    foreach ($sets[$i] as $val => $_) {
                        if (isset($sets[$j][$val])) {
                            $cnt++;
                            if ($cnt >= $k) break;
                        }
                    }
                } else {
                    foreach ($sets[$j] as $val => $_) {
                        if (isset($sets[$i][$val])) {
                            $cnt++;
                            if ($cnt >= $k) break;
                        }
                    }
                }
                if ($cnt >= $k) {
                    $this->union($parent, $i, $j);
                }
            }
        }

        // Count distinct components
        $components = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($this->find($parent, $i) == $i) {
                $components++;
            }
        }
        return $components;
    }

    private function find(&$parent, $x) {
        if ($parent[$x] != $x) {
            $parent[$x] = $this->find($parent, $parent[$x]);
        }
        return $parent[$x];
    }

    private function union(&$parent, $a, $b) {
        $ra = $this->find($parent, $a);
        $rb = $this->find($parent, $b);
        if ($ra != $rb) {
            $parent[$rb] = $ra;
        }
    }
}
```

## Swift

```swift
import Foundation

class DSU {
    private var parent: [Int]
    
    init(_ n: Int) {
        parent = Array(0..<n)
    }
    
    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    
    func union(_ a: Int, _ b: Int) {
        let ra = find(a)
        let rb = find(b)
        if ra != rb {
            parent[ra] = rb
        }
    }
}

class Solution {
    func numberOfComponents(_ properties: [[Int]], _ k: Int) -> Int {
        let n = properties.count
        var sets = [Set<Int>]()
        sets.reserveCapacity(n)
        for arr in properties {
            sets.append(Set(arr))
        }
        
        let dsu = DSU(n)
        
        for i in 0..<n {
            for j in (i + 1)..<n {
                let setA = sets[i]
                let setB = sets[j]
                var count = 0
                if setA.count < setB.count {
                    for v in setA where setB.contains(v) {
                        count += 1
                        if count >= k { break }
                    }
                } else {
                    for v in setB where setA.contains(v) {
                        count += 1
                        if count >= k { break }
                    }
                }
                if count >= k {
                    dsu.union(i, j)
                }
            }
        }
        
        var components = Set<Int>()
        for i in 0..<n {
            components.insert(dsu.find(i))
        }
        return components.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfComponents(properties: Array<IntArray>, k: Int): Int {
        val n = properties.size
        // Preprocess each row into a boolean presence array for values 1..100
        val presence = Array(n) { BooleanArray(101) }
        for (i in 0 until n) {
            for (v in properties[i]) {
                if (v in 1..100) presence[i][v] = true
            }
        }

        // Disjoint Set Union (Union-Find)
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            var a = x
            while (parent[a] != a) {
                parent[a] = parent[parent[a]]
                a = parent[a]
            }
            return a
        }
        fun union(a: Int, b: Int) {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) parent[ra] = rb
        }

        // Build edges based on intersection size >= k
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var cnt = 0
                val pi = presence[i]
                val pj = presence[j]
                for (v in 1..100) {
                    if (pi[v] && pj[v]) {
                        cnt++
                        if (cnt >= k) break
                    }
                }
                if (cnt >= k) union(i, j)
            }
        }

        // Count distinct components
        val roots = HashSet<Int>()
        for (i in 0 until n) {
            roots.add(find(i))
        }
        return roots.size
    }
}
```

## Dart

```dart
class Solution {
  int numberOfComponents(List<List<int>> properties, int k) {
    int n = properties.length;
    List<Set<int>> sets =
        List.generate(n, (i) => properties[i].toSet());

    DSU dsu = DSU(n);
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        Set<int> a = sets[i];
        Set<int> b = sets[j];
        int cnt = 0;
        if (a.length < b.length) {
          for (int v in a) {
            if (b.contains(v)) {
              cnt++;
              if (cnt >= k) break;
            }
          }
        } else {
          for (int v in b) {
            if (a.contains(v)) {
              cnt++;
              if (cnt >= k) break;
            }
          }
        }
        if (cnt >= k) dsu.union(i, j);
      }
    }

    Set<int> comps = {};
    for (int i = 0; i < n; ++i) {
      comps.add(dsu.find(i));
    }
    return comps.length;
  }
}

class DSU {
  List<int> parent;
  List<int> rank;
  DSU(int n)
      : parent = List.generate(n, (i) => i),
        rank = List.filled(n, 0);

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
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	sz := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		sz[i] = 1
	}
	return &dsu{parent: p, size: sz}
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
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
}

func numberOfComponents(properties [][]int, k int) int {
	n := len(properties)
	if n == 0 {
		return 0
	}
	// build boolean sets for each row (values are in [1,100])
	sets := make([][]bool, n)
	for i := 0; i < n; i++ {
		s := make([]bool, 101)
		for _, v := range properties[i] {
			s[v] = true
		}
		sets[i] = s
	}

	ds := newDSU(n)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			cnt := 0
			for v := 1; v <= 100; v++ {
				if sets[i][v] && sets[j][v] {
					cnt++
					if cnt >= k {
						break
					}
				}
			}
			if cnt >= k {
				ds.union(i, j)
			}
		}
	}

	comp := 0
	for i := 0; i < n; i++ {
		if ds.find(i) == i {
			comp++
		}
	}
	return comp
}
```

## Ruby

```ruby
require 'set'

class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    if @parent[x] != x
      @parent[x] = find(@parent[x])
    end
    @parent[x]
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

  def count_unique_roots
    (0...@parent.size).map { |i| find(i) }.uniq.size
  end
end

# @param {Integer[][]} properties
# @param {Integer} k
# @return {Integer}
def number_of_components(properties, k)
  n = properties.length
  sets = properties.map { |arr| arr.to_set }

  dsu = DSU.new(n)

  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      intersect_size = (sets[i] & sets[j]).size
      dsu.union(i, j) if intersect_size >= k
    end
  end

  dsu.count_unique_roots
end
```

## Scala

```scala
object Solution {
    def numberOfComponents(properties: Array[Array[Int]], k: Int): Int = {
        val n = properties.length
        val sets = new Array[scala.collection.mutable.BitSet](n)
        for (i <- 0 until n) {
            val bs = scala.collection.mutable.BitSet.empty
            for (v <- properties(i)) bs += v
            sets(i) = bs
        }

        val parent = (0 until n).toArray

        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                parent(p) = parent(parent(p))
                p = parent(p)
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) parent(ra) = rb
        }

        for (i <- 0 until n; j <- i + 1 until n) {
            if ((sets(i) & sets(j)).size >= k) union(i, j)
        }

        val roots = scala.collection.mutable.Set[Int]()
        for (i <- 0 until n) roots += find(i)
        roots.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_components(properties: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = properties.len();
        if n == 0 {
            return 0;
        }

        // Build presence arrays for each property row
        let mut sets: Vec<[bool; 101]> = Vec::with_capacity(n);
        for row in &properties {
            let mut arr = [false; 101];
            for &v in row {
                let idx = v as usize;
                if idx <= 100 {
                    arr[idx] = true;
                }
            }
            sets.push(arr);
        }

        // Disjoint Set Union structure
        struct DSU {
            parent: Vec<usize>,
            rank: Vec<usize>,
        }
        impl DSU {
            fn new(size: usize) -> Self {
                let parent = (0..size).collect();
                let rank = vec![0; size];
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

        let mut dsu = DSU::new(n);
        let k_usize = k as usize;

        // Connect nodes whose intersection size >= k
        for i in 0..n {
            for j in (i + 1)..n {
                let mut cnt = 0usize;
                for v in 1..=100 {
                    if sets[i][v] && sets[j][v] {
                        cnt += 1;
                        if cnt >= k_usize {
                            break;
                        }
                    }
                }
                if cnt >= k_usize {
                    dsu.union(i, j);
                }
            }
        }

        // Count distinct components
        let mut seen = std::collections::HashSet::new();
        for i in 0..n {
            let root = dsu.find(i);
            seen.insert(root);
        }
        seen.len() as i32
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (number-of-components properties k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length properties))
         (sets (map list->set properties)))
    (let ((visited (make-vector n #f)))
      (define (intersect-size i j)
        (set-count (set-intersect (list-ref sets i) (list-ref sets j))))
      (define (dfs start)
        (let loop ((stack (list start)))
          (when (not (null? stack))
            (define v (car stack))
            (define rest (cdr stack))
            (unless (vector-ref visited v)
              (vector-set! visited v #t)
              (let ((neighbors
                     (for/list ([idx (in-range n)]
                                #:when (and (not (= idx v))
                                            (not (vector-ref visited idx))
                                            (>= (intersect-size v idx) k)))
                       idx)))
                (loop (append neighbors rest)))))))
      (let loop ((i 0) (components 0))
        (if (>= i n)
            components
            (if (vector-ref visited i)
                (loop (+ i 1) components)
                (begin
                  (dfs i)
                  (loop (+ i 1) (+ components 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_components/2]).

-spec number_of_components(Properties :: [[integer()]], K :: integer()) -> integer().
number_of_components(Properties, K) ->
    count_components(Properties, K, 0, #{}).

%% Count components recursively
count_components(Properties, K, CompCnt, Visited) ->
    case find_unvisited_index(Properties, Visited) of
        none -> CompCnt;
        {Idx, _} ->
            NewVisited = bfs([Idx], Properties, K, Visited),
            count_components(Properties, K, CompCnt + 1, NewVisited)
    end.

%% Find first index not visited
find_unvisited_index(Properties, Visited) ->
    N = length(Properties),
    find_unvisited_index(0, N, Properties, Visited).

find_unvisited_index(I, N, _Properties, _Visited) when I >= N -> none;
find_unvisited_index(I, N, _Properties, Visited) ->
    case maps:is_key(I, Visited) of
        true -> find_unvisited_index(I + 1, N, _Properties, Visited);
        false -> {I, ok}
    end.

%% BFS using a stack (list)
bfs([], _Properties, _K, Visited) -> Visited;
bfs([Curr|Rest], Properties, K, Visited) ->
    case maps:is_key(Curr, Visited) of
        true ->
            bfs(Rest, Properties, K, Visited);
        false ->
            PropCurr = lists:nth(Curr + 1, Properties),
            NewVisited = maps:put(Curr, true, Visited),
            Neighs = neighbors(Curr, PropCurr, Properties, K, NewVisited),
            bfs(Neighs ++ Rest, Properties, K, NewVisited)
    end.

%% Find neighboring indices satisfying intersection condition
neighbors(Index, PropI, Properties, K, Visited) ->
    N = length(Properties),
    Indices = lists:seq(0, N - 1),
    [ J || J <- Indices,
           J =/= Index,
           not maps:is_key(J, Visited),
           intersect_len(PropI, lists:nth(J + 1, Properties)) >= K ].

%% Intersection size of distinct elements
intersect_len(A, B) ->
    SetA = sets:from_list(A),
    SetB = sets:from_list(B),
    Inter = sets:intersection(SetA, SetB),
    sets:size(Inter).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_components(properties :: [[integer]], k :: integer) :: integer
  def number_of_components(properties, k) do
    n = length(properties)

    sets =
      Enum.map(properties, fn row ->
        MapSet.new(row)
      end)

    adj = List.duplicate([], n)

    adj =
      Enum.reduce(0..(n - 2), adj, fn i, acc_adj ->
        Enum.reduce((i + 1)..(n - 1), acc_adj, fn j, inner_adj ->
          inter_size =
            MapSet.intersection(Enum.at(sets, i), Enum.at(sets, j))
            |> MapSet.size()

          if inter_size >= k do
            inner_adj
            |> List.update_at(i, fn lst -> [j | lst] end)
            |> List.update_at(j, fn lst -> [i | lst] end)
          else
            inner_adj
          end
        end)
      end)

    {components, _vis} =
      Enum.reduce(0..(n - 1), {0, MapSet.new()}, fn i, {cnt, vis} ->
        if MapSet.member?(vis, i) do
          {cnt, vis}
        else
          new_vis = explore(i, adj, vis)
          {cnt + 1, new_vis}
        end
      end)

    components
  end

  defp explore(start, adj, visited) do
    do_explore([start], adj, visited)
  end

  defp do_explore([], _adj, visited), do: visited

  defp do_explore([node | rest], adj, visited) do
    if MapSet.member?(visited, node) do
      do_explore(rest, adj, visited)
    else
      new_vis = MapSet.put(visited, node)
      neighbors = Enum.at(adj, node)
      do_explore(neighbors ++ rest, adj, new_vis)
    end
  end
end
```
