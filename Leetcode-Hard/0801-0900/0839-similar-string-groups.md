# 0839. Similar String Groups

## Cpp

```cpp
class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        struct DSU {
            vector<int> p, sz;
            DSU(int n): p(n), sz(n,1) { iota(p.begin(), p.end(), 0); }
            int find(int x){
                if(p[x]==x) return x;
                return p[x]=find(p[x]);
            }
            void unite(int a,int b){
                a=find(a); b=find(b);
                if(a==b) return;
                if(sz[a]<sz[b]) swap(a,b);
                p[b]=a;
                sz[a]+=sz[b];
            }
        };
        DSU dsu(n);
        auto similar = [&](const string& a, const string& b)->bool{
            int diff=0;
            for(int i=0;i<(int)a.size();++i){
                if(a[i]!=b[i]){
                    ++diff;
                    if(diff>2) return false;
                }
            }
            return diff==0 || diff==2;
        };
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                if(similar(strs[i], strs[j]))
                    dsu.unite(i,j);
            }
        }
        unordered_set<int> groups;
        for(int i=0;i<n;++i) groups.insert(dsu.find(i));
        return groups.size();
    }
};
```

## Java

```java
class Solution {
    public int numSimilarGroups(String[] strs) {
        int n = strs.length;
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (areSimilar(strs[i], strs[j])) {
                    uf.union(i, j);
                }
            }
        }
        int groups = 0;
        for (int i = 0; i < n; i++) {
            if (uf.find(i) == i) groups++;
        }
        return groups;
    }

    private boolean areSimilar(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
                if (diff > 2) return false;
            }
        }
        return diff == 0 || diff == 2;
    }

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

        void union(int x, int y) {
            int rx = find(x);
            int ry = find(y);
            if (rx == ry) return;
            if (rank[rx] < rank[ry]) {
                parent[rx] = ry;
            } else if (rank[rx] > rank[ry]) {
                parent[ry] = rx;
            } else {
                parent[ry] = rx;
                rank[rx]++;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
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

        def similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2

        for i in range(n):
            si = strs[i]
            for j in range(i + 1, n):
                if similar(si, strs[j]):
                    union(i, j)

        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)
```

## Python3

```python
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
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

        def similar(s1: str, s2: str) -> bool:
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    union(i, j)

        return sum(1 for i in range(n) if find(i) == i)
```

## C

```c
#include <stddef.h>

static int find(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int *parent, int *rank, int x, int y) {
    int rx = find(parent, x);
    int ry = find(parent, y);
    if (rx == ry) return;
    if (rank[rx] < rank[ry]) {
        parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
        parent[ry] = rx;
    } else {
        parent[ry] = rx;
        rank[rx]++;
    }
}

static int isSimilar(const char *a, const char *b) {
    int diff = 0;
    for (int i = 0; a[i]; ++i) {
        if (a[i] != b[i]) {
            if (++diff > 2) return 0;
        }
    }
    return diff == 0 || diff == 2;
}

int numSimilarGroups(char** strs, int strsSize) {
    if (strsSize <= 1) return strsSize;

    int *parent = (int *)malloc(strsSize * sizeof(int));
    int *rank   = (int *)calloc(strsSize, sizeof(int));

    for (int i = 0; i < strsSize; ++i) parent[i] = i;

    for (int i = 0; i < strsSize; ++i) {
        for (int j = i + 1; j < strsSize; ++j) {
            if (isSimilar(strs[i], strs[j])) {
                unite(parent, rank, i, j);
            }
        }
    }

    int groups = 0;
    for (int i = 0; i < strsSize; ++i) {
        if (find(parent, i) == i) groups++;
    }

    free(parent);
    free(rank);
    return groups;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NumSimilarGroups(string[] strs) {
        int n = strs.Length;
        var dsu = new DSU(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (AreSimilar(strs[i], strs[j])) {
                    dsu.Union(i, j);
                }
            }
        }
        var groups = new HashSet<int>();
        for (int i = 0; i < n; i++) {
            groups.Add(dsu.Find(i));
        }
        return groups.Count;
    }

    private bool AreSimilar(string a, string b) {
        int diffCount = 0;
        int first = -1, second = -1;
        for (int i = 0; i < a.Length; i++) {
            if (a[i] != b[i]) {
                if (diffCount == 0) first = i;
                else if (diffCount == 1) second = i;
                diffCount++;
                if (diffCount > 2) return false;
            }
        }
        if (diffCount == 0) return true;
        if (diffCount != 2) return false;
        return a[first] == b[second] && a[second] == b[first];
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
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int a, int b) {
            int rootA = Find(a);
            int rootB = Find(b);
            if (rootA == rootB) return;
            if (rank[rootA] < rank[rootB]) {
                parent[rootA] = rootB;
            } else if (rank[rootA] > rank[rootB]) {
                parent[rootB] = rootA;
            } else {
                parent[rootB] = rootA;
                rank[rootA]++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var numSimilarGroups = function(strs) {
    const n = strs.length;
    const parent = new Array(n);
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; i++) parent[i] = i;

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
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
    };

    const isSimilar = (s1, s2) => {
        let diff = 0;
        for (let i = 0; i < s1.length && diff <= 2; i++) {
            if (s1[i] !== s2[i]) diff++;
        }
        return diff === 0 || diff === 2;
    };

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isSimilar(strs[i], strs[j])) union(i, j);
        }
    }

    const groups = new Set();
    for (let i = 0; i < n; i++) groups.add(find(i));
    return groups.size;
};
```

## Typescript

```typescript
function numSimilarGroups(strs: string[]): number {
    const n = strs.length;

    class UnionFind {
        parent: number[];
        rank: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x: number): number {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            if (this.rank[ra] === this.rank[rb]) {
                this.rank[ra]++;
            }
        }
    }

    const uf = new UnionFind(n);

    function isSimilar(a: string, b: string): boolean {
        let diff = 0;
        for (let i = 0; i < a.length && diff <= 2; i++) {
            if (a[i] !== b[i]) diff++;
        }
        return diff === 0 || diff === 2;
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isSimilar(strs[i], strs[j])) {
                uf.union(i, j);
            }
        }
    }

    const groups = new Set<number>();
    for (let i = 0; i < n; i++) {
        groups.add(uf.find(i));
    }
    return groups.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function numSimilarGroups($strs) {
        $n = count($strs);
        if ($n == 0) return 0;

        // Union-Find initialization
        $parent = range(0, $n - 1);
        $rank   = array_fill(0, $n, 0);

        // Find with path compression
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // Union by rank
        $union = function($x, $y) use (&$parent, &$rank, $find) {
            $rootX = $find($x);
            $rootY = $find($y);
            if ($rootX == $rootY) return;
            if ($rank[$rootX] < $rank[$rootY]) {
                $parent[$rootX] = $rootY;
            } elseif ($rank[$rootX] > $rank[$rootY]) {
                $parent[$rootY] = $rootX;
            } else {
                $parent[$rootY] = $rootX;
                $rank[$rootX]++;
            }
        };

        // Helper to check similarity
        $isSimilar = function($a, $b) {
            $len = strlen($a);
            $diff = 0;
            for ($i = 0; $i < $len; $i++) {
                if ($a[$i] !== $b[$i]) {
                    $diff++;
                    if ($diff > 2) return false;
                }
            }
            // diff == 0 (identical) or diff == 2 (swap two chars)
            return $diff == 0 || $diff == 2;
        };

        // Compare each pair
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($isSimilar($strs[$i], $strs[$j])) {
                    $union($i, $j);
                }
            }
        }

        // Count distinct roots
        $groups = [];
        for ($i = 0; $i < $n; $i++) {
            $root = $find($i);
            $groups[$root] = true;
        }

        return count($groups);
    }
}
```

## Swift

```swift
class UnionFind {
    private var parent: [Int]
    private var rank: [Int]

    init(_ size: Int) {
        parent = Array(0..<size)
        rank = [Int](repeating: 0, count: size)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) {
        let rootX = find(x)
        let rootY = find(y)
        if rootX == rootY { return }

        if rank[rootX] < rank[rootY] {
            parent[rootX] = rootY
        } else if rank[rootX] > rank[rootY] {
            parent[rootY] = rootX
        } else {
            parent[rootY] = rootX
            rank[rootX] += 1
        }
    }
}

class Solution {
    func numSimilarGroups(_ strs: [String]) -> Int {
        let n = strs.count
        if n == 0 { return 0 }

        var uf = UnionFind(n)

        for i in 0..<n {
            for j in (i + 1)..<n {
                if isSimilar(strs[i], strs[j]) {
                    uf.union(i, j)
                }
            }
        }

        var groups = Set<Int>()
        for i in 0..<n {
            groups.insert(uf.find(i))
        }
        return groups.count
    }

    private func isSimilar(_ a: String, _ b: String) -> Bool {
        let arrA = Array(a)
        let arrB = Array(b)
        var diff = 0

        for k in 0..<arrA.count {
            if arrA[k] != arrB[k] {
                diff += 1
                if diff > 2 { return false }
            }
        }
        return diff == 0 || diff == 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSimilarGroups(strs: Array<String>): Int {
        val n = strs.size
        val dsu = DSU(n)
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (isSimilar(strs[i], strs[j])) {
                    dsu.union(i, j)
                }
            }
        }
        var groups = 0
        for (i in 0 until n) {
            if (dsu.find(i) == i) groups++
        }
        return groups
    }

    private fun isSimilar(a: String, b: String): Boolean {
        var first = -1
        var second = -1
        for (k in a.indices) {
            if (a[k] != b[k]) {
                when {
                    first == -1 -> first = k
                    second == -1 -> second = k
                    else -> return false
                }
            }
        }
        return when {
            first == -1 && second == -1 -> true
            second == -1 -> false
            else -> a[first] == b[second] && a[second] == b[first]
        }
    }

    private class DSU(size: Int) {
        private val parent = IntArray(size) { it }
        private val rank = IntArray(size)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var pa = find(a)
            var pb = find(b)
            if (pa == pb) return
            if (rank[pa] < rank[pb]) {
                parent[pa] = pb
            } else if (rank[pa] > rank[pb]) {
                parent[pb] = pa
            } else {
                parent[pb] = pa
                rank[pa]++
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  int numSimilarGroups(List<String> strs) {
    int n = strs.length;
    if (n == 0) return 0;

    var dsu = _DSU(n);
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (_areSimilar(strs[i], strs[j])) {
          dsu.union(i, j);
        }
      }
    }

    var groups = <int>{};
    for (int i = 0; i < n; ++i) {
      groups.add(dsu.find(i));
    }
    return groups.length;
  }

  bool _areSimilar(String a, String b) {
    int diff = 0;
    for (int i = 0; i < a.length && diff <= 2; ++i) {
      if (a[i] != b[i]) diff++;
    }
    return diff == 0 || diff == 2;
  }
}

class _DSU {
  List<int> parent;
  List<int> size;

  _DSU(int n)
      : parent = List.generate(n, (i) => i),
        size = List.filled(n, 1);

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
```

## Golang

```go
type dsu struct {
	parent []int
	rank   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	r := make([]int, n)
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

func (d *dsu) union(x, y int) {
	fx := d.find(x)
	fy := d.find(y)
	if fx == fy {
		return
	}
	if d.rank[fx] < d.rank[fy] {
		d.parent[fx] = fy
	} else if d.rank[fx] > d.rank[fy] {
		d.parent[fy] = fx
	} else {
		d.parent[fy] = fx
		d.rank[fx]++
	}
}

func isSimilar(a, b string) bool {
	diff := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			diff++
			if diff > 2 {
				return false
			}
		}
	}
	return diff == 0 || diff == 2
}

func numSimilarGroups(strs []string) int {
	n := len(strs)
	ds := newDSU(n)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if isSimilar(strs[i], strs[j]) {
				ds.union(i, j)
			}
		}
	}

	groups := 0
	seen := make(map[int]struct{})
	for i := 0; i < n; i++ {
		root := ds.find(i)
		if _, ok := seen[root]; !ok {
			seen[root] = struct{}{}
			groups++
		}
	}
	return groups
}
```

## Ruby

```ruby
class UnionFind
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
    return false if rx == ry
    if @rank[rx] < @rank[ry]
      @parent[rx] = ry
    elsif @rank[rx] > @rank[ry]
      @parent[ry] = rx
    else
      @parent[ry] = rx
      @rank[rx] += 1
    end
    true
  end

  def count_roots
    roots = {}
    @parent.each_index { |i| roots[find(i)] = true }
    roots.size
  end
end

def similar?(a, b)
  diff = 0
  a.length.times do |i|
    if a[i] != b[i]
      diff += 1
      return false if diff > 2
    end
  end
  diff == 0 || diff == 2
end

# @param {String[]} strs
# @return {Integer}
def num_similar_groups(strs)
  n = strs.size
  uf = UnionFind.new(n)
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      uf.union(i, j) if similar?(strs[i], strs[j])
    end
  end
  uf.count_roots
end
```

## Scala

```scala
object Solution {
    def numSimilarGroups(strs: Array[String]): Int = {
        val n = strs.length
        val parent = (0 until n).toArray
        var groups = n

        def find(x: Int): Int = {
            if (parent(x) != x) {
                parent(x) = find(parent(x))
            }
            parent(x)
        }

        def union(a: Int, b: Int): Unit = {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) {
                parent(ra) = rb
                groups -= 1
            }
        }

        def similar(s1: String, s2: String): Boolean = {
            var diff = 0
            var i = 0
            while (i < s1.length && diff <= 2) {
                if (s1.charAt(i) != s2.charAt(i)) diff += 1
                i += 1
            }
            diff == 0 || diff == 2
        }

        for (i <- 0 until n) {
            var j = i + 1
            while (j < n) {
                if (similar(strs(i), strs(j))) union(i, j)
                j += 1
            }
        }

        groups
    }
}
```

## Rust

```rust
use std::collections::HashSet;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<u8>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU {
            parent,
            rank: vec![0; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut xr = self.find(x);
        let mut yr = self.find(y);
        if xr == yr {
            return;
        }
        if self.rank[xr] < self.rank[yr] {
            std::mem::swap(&mut xr, &mut yr);
        }
        self.parent[yr] = xr;
        if self.rank[xr] == self.rank[yr] {
            self.rank[xr] += 1;
        }
    }
}

fn is_similar(a: &[u8], b: &[u8]) -> bool {
    let mut diff = Vec::with_capacity(2);
    for i in 0..a.len() {
        if a[i] != b[i] {
            diff.push(i);
            if diff.len() > 2 {
                return false;
            }
        }
    }
    match diff.len() {
        0 => true,
        2 => a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]],
        _ => false,
    }
}

impl Solution {
    pub fn num_similar_groups(strs: Vec<String>) -> i32 {
        let n = strs.len();
        if n <= 1 {
            return n as i32;
        }
        let words: Vec<Vec<u8>> = strs.iter().map(|s| s.as_bytes().to_vec()).collect();
        let mut dsu = DSU::new(n);
        for i in 0..n {
            for j in (i + 1)..n {
                if is_similar(&words[i], &words[j]) {
                    dsu.union(i, j);
                }
            }
        }
        let mut groups = HashSet::new();
        for i in 0..n {
            groups.insert(dsu.find(i));
        }
        groups.len() as i32
    }
}
```

## Racket

```racket
#lang racket

(define (similar? a b)
  (let loop ((i 0) (cnt 0))
    (cond
      [(= i (string-length a)) (or (= cnt 0) (= cnt 2))]
      [else (if (char=? (string-ref a i) (string-ref b i))
                (loop (+ i 1) cnt)
                (let ((newcnt (+ cnt 1)))
                  (if (> newcnt 2)
                      #f
                      (loop (+ i 1) newcnt))))])))

(define (find parent x)
  (let ((p (vector-ref parent x)))
    (if (= p x)
        x
        (let ((root (find parent p)))
          (vector-set! parent x root)
          root))))

(define (union parent rank x y)
  (let* ((rx (find parent x))
         (ry (find parent y)))
    (when (not (= rx ry))
      (let ((rankx (vector-ref rank rx))
            (ranky (vector-ref rank ry)))
        (cond
          [(< rankx ranky) (vector-set! parent rx ry)]
          [(> rankx ranky) (vector-set! parent ry rx)]
          [else (vector-set! parent ry rx)
                (vector-set! rank rx (+ rankx 1))])))))

(define/contract (num-similar-groups strs)
  (-> (listof string?) exact-integer?)
  (let* ((n (length strs))
         (parent (make-vector n))
         (rank (make-vector n 0)))
    (for ([i (in-range n)]) (vector-set! parent i i))
    (for* ([i (in-range n)]
           [j (in-range (+ i 1) n)])
      (when (similar? (list-ref strs i) (list-ref strs j))
        (union parent rank i j)))
    (let ((roots (make-hash)))
      (for ([i (in-range n)])
        (hash-set! roots (find parent i) #t))
      (hash-count roots))))
```

## Erlang

```erlang
-module(solution).
-export([num_similar_groups/1]).

-spec num_similar_groups(Strs :: [unicode:unicode_binary()]) -> integer().
num_similar_groups(Strs) ->
    N = length(Strs),
    Indices = lists:seq(0, N - 1),
    Parents0 = maps:from_list([{Idx, Idx} || Idx <- Indices]),
    StrLists = [binary_to_list(S) || S <- Strs],
    Pairs = [{I, J} || I <- lists:seq(0, N - 2), J <- lists:seq(I + 1, N - 1)],
    ParentsFinal = lists:foldl(
        fun({I, J}, AccParents) ->
            Si = lists:nth(I + 1, StrLists),
            Sj = lists:nth(J + 1, StrLists),
            case similar(Si, Sj) of
                true -> union(I, J, AccParents);
                false -> AccParents
            end
        end,
        Parents0,
        Pairs
    ),
    RootSet = lists:foldl(
        fun(I, Set) ->
            Root = find_root(I, ParentsFinal),
            sets:add_element(Root, Set)
        end,
        sets:new(),
        Indices
    ),
    sets:size(RootSet).

similar(A, B) ->
    Diff = [{X, Y} || {X, Y} <- lists:zip(A, B), X =/= Y],
    case length(Diff) of
        0 -> true;
        2 ->
            [{A1, B1}, {A2, B2}] = Diff,
            A1 =:= B2 andalso A2 =:= B1;
        _ -> false
    end.

find_root(I, Parents) ->
    Parent = maps:get(I, Parents),
    if
        Parent == I -> I;
        true -> find_root(Parent, Parents)
    end.

union(I, J, Parents) ->
    RootI = find_root(I, Parents),
    RootJ = find_root(J, Parents),
    if
        RootI == RootJ -> Parents;
        true -> maps:put(RootI, RootJ, Parents)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_similar_groups(strs :: [String.t()]) :: integer
  def num_similar_groups(strs) do
    n = length(strs)

    {group_count, _visited} =
      Enum.reduce(0..n - 1, {0, MapSet.new()}, fn i, {cnt, visited} ->
        if MapSet.member?(visited, i) do
          {cnt, visited}
        else
          {new_visited, _} = bfs(i, strs, visited)
          {cnt + 1, new_visited}
        end
      end)

    group_count
  end

  defp bfs(start_idx, strings, visited) do
    queue = :queue.new() |> :queue.in(start_idx)
    visited = MapSet.put(visited, start_idx)
    bfs_loop(queue, strings, visited)
  end

  defp bfs_loop(queue, strings, visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        {visited, nil}

      {{:value, idx}, q_rest} ->
        n = length(strings)

        {q_next, vis_next} =
          Enum.reduce(0..n - 1, {q_rest, visited}, fn j, {q_acc, v_acc} ->
            if MapSet.member?(v_acc, j) do
              {q_acc, v_acc}
            else
              s_i = Enum.at(strings, idx)
              s_j = Enum.at(strings, j)

              if similar?(s_i, s_j) do
                { :queue.in(j, q_acc), MapSet.put(v_acc, j) }
              else
                {q_acc, v_acc}
              end
            end
          end)

        bfs_loop(q_next, strings, vis_next)
    end
  end

  defp similar?(a, b) do
    len = byte_size(a)

    mismatches =
      Enum.reduce_while(0..len - 1, 0, fn i, cnt ->
        if :binary.at(a, i) != :binary.at(b, i) do
          new = cnt + 1

          if new > 2 do
            {:halt, new}
          else
            {:cont, new}
          end
        else
          {:cont, cnt}
        end
      end)

    mismatches == 0 or mismatches == 2
  end
end
```
