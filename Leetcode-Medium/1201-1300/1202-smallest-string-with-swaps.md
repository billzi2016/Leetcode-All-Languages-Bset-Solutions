# 1202. Smallest String With Swaps

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, rank;
        DSU(int n) : parent(n), rank(n, 0) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (rank[a] < rank[b]) swap(a, b);
            parent[b] = a;
            if (rank[a] == rank[b]) ++rank[a];
        }
    };
    
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        DSU dsu(n);
        for (auto& p : pairs) {
            dsu.unite(p[0], p[1]);
        }
        vector<vector<int>> groups(n);
        for (int i = 0; i < n; ++i) {
            groups[dsu.find(i)].push_back(i);
        }
        string res = s;
        for (auto& idxs : groups) {
            if (idxs.empty()) continue;
            vector<char> chars;
            chars.reserve(idxs.size());
            for (int idx : idxs) chars.push_back(s[idx]);
            sort(idxs.begin(), idxs.end());
            sort(chars.begin(), chars.end());
            for (size_t i = 0; i < idxs.size(); ++i) {
                res[idxs[i]] = chars[i];
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class DSU {
        int[] parent;
        int[] size;
        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
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

    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n = s.length();
        DSU dsu = new DSU(n);
        for (List<Integer> p : pairs) {
            dsu.union(p.get(0), p.get(1));
        }
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            groups.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }

        char[] res = s.toCharArray();
        for (List<Integer> idxList : groups.values()) {
            if (idxList.size() <= 1) continue;
            List<Character> chars = new ArrayList<>(idxList.size());
            for (int idx : idxList) {
                chars.add(s.charAt(idx));
            }
            Collections.sort(idxList);
            Collections.sort(chars);
            for (int i = 0; i < idxList.size(); i++) {
                res[idxList.get(i)] = chars.get(i);
            }
        }
        return new String(res);
    }
}
```

## Python

```python
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
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

        for a, b in pairs:
            union(a, b)

        groups = {}
        for i in range(n):
            root = find(i)
            groups.setdefault(root, []).append(i)

        res = list(s)
        for indices in groups.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for idx, ch in zip(indices, chars):
                res[idx] = ch

        return "".join(res)
```

## Python3

```python
from typing import List
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for a, b in pairs:
            union(a, b)

        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for idx, ch in zip(indices, chars):
                res[idx] = ch

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *idx;
    int cnt;
    int cap;
} Component;

static int find(int *parent, int x) {
    if (parent[x] != x)
        parent[x] = find(parent, parent[x]);
    return parent[x];
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

static int cmpChar(const void *a, const void *b) {
    return *(const char *)a - *(const char *)b;
}

char* smallestStringWithSwaps(char* s, int** pairs, int pairsSize, int* pairsColSize) {
    int n = (int)strlen(s);
    if (n == 0) return s;

    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    for (int i = 0; i < pairsSize; ++i) {
        int a = pairs[i][0];
        int b = pairs[i][1];
        unite(parent, rank, a, b);
    }

    Component *comps = (Component *)calloc(n, sizeof(Component));

    for (int i = 0; i < n; ++i) {
        int r = find(parent, i);
        Component *c = &comps[r];
        if (c->cnt == c->cap) {
            int newCap = c->cap ? c->cap * 2 : 4;
            c->idx = (int *)realloc(c->idx, newCap * sizeof(int));
            c->cap = newCap;
        }
        c->idx[c->cnt++] = i;
    }

    for (int r = 0; r < n; ++r) {
        Component *c = &comps[r];
        if (c->cnt == 0) continue;

        int cnt = c->cnt;
        char *chars = (char *)malloc(cnt * sizeof(char));
        for (int i = 0; i < cnt; ++i)
            chars[i] = s[c->idx[i]];

        qsort(chars, cnt, sizeof(char), cmpChar);

        for (int i = 0; i < cnt; ++i)
            s[c->idx[i]] = chars[i];

        free(chars);
        free(c->idx);
    }

    free(comps);
    free(parent);
    free(rank);
    return s;
}
```

## Csharp

```csharp
public class Solution
{
    public string SmallestStringWithSwaps(string s, IList<IList<int>> pairs)
    {
        int n = s.Length;
        var dsu = new DSU(n);
        foreach (var p in pairs)
        {
            dsu.Union(p[0], p[1]);
        }

        var groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++)
        {
            int root = dsu.Find(i);
            if (!groups.ContainsKey(root))
                groups[root] = new List<int>();
            groups[root].Add(i);
        }

        char[] result = s.ToCharArray();
        foreach (var kv in groups)
        {
            var indices = kv.Value;
            var chars = new List<char>(indices.Count);
            foreach (int idx in indices)
                chars.Add(s[idx]);

            indices.Sort();   // smallest positions first
            chars.Sort();     // smallest characters first

            for (int i = 0; i < indices.Count; i++)
                result[indices[i]] = chars[i];
        }

        return new string(result);
    }

    private class DSU
    {
        private readonly int[] parent;
        private readonly int[] rank;

        public DSU(int size)
        {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }

        public int Find(int x)
        {
            if (parent[x] != x)
                parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);
            if (rootX == rootY) return;

            if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else
            {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function(s, pairs) {
    const n = s.length;
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
            [ra, rb] = [rb, ra];
        }
        parent[rb] = ra;
        if (rank[ra] === rank[rb]) rank[ra]++;
    };

    for (const [a, b] of pairs) {
        union(a, b);
    }

    const groups = new Map();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r).push(i);
    }

    const chars = s.split('');
    for (const idxs of groups.values()) {
        const letters = idxs.map(i => chars[i]);
        idxs.sort((a, b) => a - b);
        letters.sort();
        for (let i = 0; i < idxs.length; i++) {
            chars[idxs[i]] = letters[i];
        }
    }

    return chars.join('');
};
```

## Typescript

```typescript
function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    const n = s.length;
    if (pairs.length === 0) return s;

    class DSU {
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
        union(x: number, y: number): void {
            let rx = this.find(x);
            let ry = this.find(y);
            if (rx === ry) return;
            if (this.rank[rx] < this.rank[ry]) {
                this.parent[rx] = ry;
            } else if (this.rank[rx] > this.rank[ry]) {
                this.parent[ry] = rx;
            } else {
                this.parent[ry] = rx;
                this.rank[rx]++;
            }
        }
    }

    const dsu = new DSU(n);
    for (const [a, b] of pairs) {
        dsu.union(a, b);
    }

    const groups = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const root = dsu.find(i);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root)!.push(i);
    }

    const result: string[] = new Array(n);
    for (const indices of groups.values()) {
        const chars = indices.map(idx => s.charAt(idx));
        indices.sort((a, b) => a - b);
        chars.sort(); // default lexicographic sort works for single characters
        for (let i = 0; i < indices.length; i++) {
            result[indices[i]] = chars[i];
        }
    }

    return result.join('');
}
```

## Php

```php
class DSU {
    public array $parent;
    public array $rank;

    public function __construct(int $n) {
        $this->parent = range(0, $n - 1);
        $this->rank   = array_fill(0, $n, 0);
    }

    public function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    public function union(int $a, int $b): void {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra === $rb) {
            return;
        }
        if ($this->rank[$ra] < $this->rank[$rb]) {
            $this->parent[$ra] = $rb;
        } elseif ($this->rank[$ra] > $this->rank[$rb]) {
            $this->parent[$rb] = $ra;
        } else {
            $this->parent[$rb] = $ra;
            $this->rank[$ra]++;
        }
    }
}

class Solution {

    /**
     * @param String $s
     * @param Integer[][] $pairs
     * @return String
     */
    function smallestStringWithSwaps($s, $pairs) {
        $n = strlen($s);
        if ($n === 0) return $s;

        $dsu = new DSU($n);
        foreach ($pairs as $pair) {
            $dsu->union($pair[0], $pair[1]);
        }

        // Group indices by their root
        $components = [];
        for ($i = 0; $i < $n; $i++) {
            $root = $dsu->find($i);
            if (!isset($components[$root])) {
                $components[$root] = [];
            }
            $components[$root][] = $i;
        }

        $chars = str_split($s);

        foreach ($components as $indices) {
            // Extract characters for this component
            $compChars = [];
            foreach ($indices as $idx) {
                $compChars[] = $chars[$idx];
            }
            sort($compChars);          // smallest chars first
            sort($indices);            // assign to smallest positions

            $len = count($indices);
            for ($k = 0; $k < $len; $k++) {
                $chars[$indices[$k]] = $compChars[$k];
            }
        }

        return implode('', $chars);
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
    func smallestStringWithSwaps(_ s: String, _ pairs: [[Int]]) -> String {
        let n = s.count
        var chars = Array(s)
        if pairs.isEmpty { return s }

        let uf = UnionFind(n)
        for p in pairs {
            uf.union(p[0], p[1])
        }

        var groups = [Int: [Int]]()
        for i in 0..<n {
            let root = uf.find(i)
            groups[root, default: []].append(i)
        }

        var result = chars
        for (_, indices) in groups {
            let sortedIndices = indices.sorted()
            var componentChars = sortedIndices.map { chars[$0] }
            componentChars.sort()
            for (pos, idx) in sortedIndices.enumerated() {
                result[idx] = componentChars[pos]
            }
        }

        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestStringWithSwaps(s: String, pairs: List<List<Int>>): String {
        val n = s.length
        val parent = IntArray(n) { it }
        val rank = IntArray(n)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra]++
            }
        }

        for (pair in pairs) {
            union(pair[0], pair[1])
        }

        val groups = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            val root = find(i)
            groups.getOrPut(root) { mutableListOf() }.add(i)
        }

        val result = CharArray(n)
        val chars = s.toCharArray()
        for (idxList in groups.values) {
            idxList.sort()
            val sortedChars = idxList.map { chars[it] }.sorted()
            for (i in idxList.indices) {
                result[idxList[i]] = sortedChars[i]
            }
        }

        return String(result)
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
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
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

class Solution {
  String smallestStringWithSwaps(String s, List<List<int>> pairs) {
    int n = s.length;
    DSU dsu = DSU(n);
    for (var p in pairs) {
      dsu.union(p[0], p[1]);
    }

    Map<int, List<int>> groups = {};
    for (int i = 0; i < n; i++) {
      int root = dsu.find(i);
      groups.putIfAbsent(root, () => []).add(i);
    }

    List<String> chars = s.split('');
    for (var entry in groups.entries) {
      List<int> idxs = entry.value;
      if (idxs.length <= 1) continue;

      // collect characters of this component
      List<String> compChars = idxs.map((i) => chars[i]).toList();

      idxs.sort();        // sort indices ascending
      compChars.sort();   // sort characters lexicographically

      for (int j = 0; j < idxs.length; j++) {
        chars[idxs[j]] = compChars[j];
      }
    }

    return chars.join('');
  }
}
```

## Golang

```go
func smallestStringWithSwaps(s string, pairs [][]int) string {
    n := len(s)
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

    for _, p := range pairs {
        union(p[0], p[1])
    }

    comp := make(map[int][]int)
    for i := 0; i < n; i++ {
        root := find(i)
        comp[root] = append(comp[root], i)
    }

    res := []byte(s)

    for _, indices := range comp {
        if len(indices) <= 1 {
            continue
        }
        sort.Ints(indices)
        chars := make([]byte, len(indices))
        for i, idx := range indices {
            chars[i] = s[idx]
        }
        sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
        for i, idx := range indices {
            res[idx] = chars[i]
        }
    }

    return string(res)
}
```

## Ruby

```ruby
def smallest_string_with_swaps(s, pairs)
  n = s.length
  parent = Array.new(n) { |i| i }
  size = Array.new(n, 1)

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
    if size[ra] < size[rb]
      ra, rb = rb, ra
    end
    parent[rb] = ra
    size[ra] += size[rb]
  end

  pairs.each { |a, b| union.call(a, b) }

  groups = Hash.new { |h, k| h[k] = [] }
  (0...n).each do |i|
    root = find.call(i)
    groups[root] << i
  end

  result = Array.new(n)
  chars = s.chars
  groups.each_value do |indices|
    sorted_indices = indices.sort
    sorted_chars = sorted_indices.map { |idx| chars[idx] }.sort
    sorted_indices.each_with_index { |idx, j| result[idx] = sorted_chars[j] }
  end

  result.join
end
```

## Scala

```scala
object Solution {
    def smallestStringWithSwaps(s: String, pairs: List[List[Int]]): String = {
        val n = s.length
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

        for (pair <- pairs) {
            union(pair(0), pair(1))
        }

        import scala.collection.mutable.{ArrayBuffer, Map => MutableMap}
        val groups = MutableMap[Int, ArrayBuffer[Int]]()
        for (i <- 0 until n) {
            val root = find(i)
            groups.getOrElseUpdate(root, ArrayBuffer()) += i
        }

        val res = new Array[Char](n)
        val chars = s.toCharArray

        for ((_, indices) <- groups) {
            val sortedIdx = indices.sorted
            val sortedChars = sortedIdx.map(chars(_)).sorted
            for (i <- sortedIdx.indices) {
                res(sortedIdx(i)) = sortedChars(i)
            }
        }

        new String(res)
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

impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        let n = s.len();
        if pairs.is_empty() {
            return s;
        }

        let mut dsu = DSU::new(n);
        for p in pairs {
            let a = p[0] as usize;
            let b = p[1] as usize;
            dsu.union(a, b);
        }

        let mut groups: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            let root = dsu.find(i);
            groups.entry(root).or_default().push(i);
        }

        let mut bytes = s.into_bytes();

        for indices in groups.values_mut() {
            let mut chars: Vec<u8> = indices.iter().map(|&i| bytes[i]).collect();
            indices.sort_unstable();
            chars.sort_unstable();
            for (idx, &c) in indices.iter().zip(chars.iter()) {
                bytes[*idx] = c;
            }
        }

        String::from_utf8(bytes).unwrap()
    }
}
```

## Racket

```racket
(define/contract (smallest-string-with-swaps s pairs)
  (-> string? (listof (listof exact-integer?)) string?)
  (let* ([n (string-length s)]
         [parent (make-vector n (lambda (i) i))]
         [rank   (make-vector n 0)])
    ;; find with path compression
    (define (find x)
      (let ([p (vector-ref parent x)])
        (if (= p x)
            x
            (let ([root (find p)])
              (vector-set! parent x root)
              root))))
    ;; union by rank
    (define (union a b)
      (let* ([ra (find a)]
             [rb (find b)])
        (unless (= ra rb)
          (let ([rank-a (vector-ref rank ra)]
                [rank-b (vector-ref rank rb)])
            (cond [(< rank-a rank-b) (vector-set! parent ra rb)]
                  [(> rank-a rank-b) (vector-set! parent rb ra)]
                  [else
                   (vector-set! parent rb ra)
                   (vector-set! rank ra (+ rank-a 1))])))))
    ;; process all pairs
    (for ([p pairs])
      (union (first p) (second p)))
    ;; group indices by root
    (define groups (make-hash))
    (for ([i (in-range n)])
      (let* ([r (find i)]
             [lst (hash-ref groups r '())])
        (hash-set! groups r (cons i lst))))
    ;; result character vector
    (define res (make-vector n #\space))
    ;; fill with original chars as default
    (for ([i (in-range n)])
      (vector-set! res i (string-ref s i)))
    ;; process each component
    (for ([comp (in-hash-values groups)])
      (let* ([indices (sort comp <)]
             [chars   (sort (map (lambda (idx) (string-ref s idx)) indices) char<?)])
        (for ([idx indices] [ch chars])
          (vector-set! res idx ch))))
    ;; convert vector of chars to string
    (list->string (vector->list res))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_string_with_swaps/2]).
-spec smallest_string_with_swaps(S :: unicode:unicode_binary(), Pairs :: [[integer()]]) -> unicode:unicode_binary().
smallest_string_with_swaps(S, Pairs) ->
    N = byte_size(S),
    InitParent = maps:from_list([{I, I} || I <- lists:seq(0, N - 1)]),
    InitSize   = maps:from_list([{I, 1} || I <- lists:seq(0, N - 1)]),
    {FinalParent, _} = process_pairs(Pairs, InitParent, InitSize),
    CompMap = build_components(N, S, FinalParent, #{}),
    ComponentLists = maps:fold(
        fun(_Root, {Idxs, Chars}, Acc) ->
            SortedIdxs  = lists:sort(Idxs),
            SortedChars = lists:sort(Chars),
            Zip = lists:zip(SortedIdxs, SortedChars),
            [Zip | Acc]
        end,
        [], CompMap),
    AllPairs = lists:flatten(lists:reverse(ComponentLists)),
    SortedAll = lists:keysort(1, AllPairs),
    list_to_binary([Char || {_Idx, Char} <- SortedAll]).

process_pairs([], Parent, Size) ->
    {Parent, Size};
process_pairs([[A, B] | Rest], Parent, Size) ->
    {NewParent, NewSize} = union(A, B, Parent, Size),
    process_pairs(Rest, NewParent, NewSize).

union(A, B, Parent, Size) ->
    RootA = find_root(A, Parent),
    RootB = find_root(B, Parent),
    if
        RootA == RootB -> {Parent, Size};
        true ->
            SizeA = maps:get(RootA, Size),
            SizeB = maps:get(RootB, Size),
            if
                SizeA < SizeB ->
                    NewParent = maps:put(RootA, RootB, Parent),
                    NewSize   = maps:put(RootB, SizeA + SizeB, Size);
                true ->
                    NewParent = maps:put(RootB, RootA, Parent),
                    NewSize   = maps:put(RootA, SizeA + SizeB, Size)
            end,
            {NewParent, NewSize}
    end.

find_root(I, Parent) ->
    case maps:get(I, Parent) of
        I -> I;
        P -> find_root(P, Parent)
    end.

build_components(N, S, Parent, Comp) ->
    build_components(0, N, S, Parent, Comp).

build_components(I, N, _S, _Parent, Comp) when I == N ->
    Comp;
build_components(I, N, S, Parent, Comp) ->
    Root = find_root(I, Parent),
    Char = binary:at(S, I),
    UpdatedComp =
        case maps:get(Root, Comp, undefined) of
            undefined ->
                maps:put(Root, {[I], [Char]}, Comp);
            {Idxs, Chars} ->
                maps:put(Root, {[I | Idxs], [Char | Chars]}, Comp)
        end,
    build_components(I + 1, N, S, Parent, UpdatedComp).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_string_with_swaps(s :: String.t(), pairs :: [[integer]]) :: String.t()
  def smallest_string_with_swaps(s, pairs) do
    n = String.length(s)
    chars = String.graphemes(s)

    # Build adjacency map
    adj =
      Enum.reduce(pairs, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], &[b | &1])
        |> Map.update(b, [a], &[a | &1])
      end)

    # Depth‑first search to collect component indices
    explore = fn start, visited0 ->
      stack = [start]
      {comp_rev, visited} = dfs(stack, adj, visited0, [])
      {Enum.reverse(comp_rev), visited}
    end

    # Helper DFS (iterative)
    defp dfs([], _adj, visited, comp), do: {comp, visited}

    defp dfs([node | rest], adj, visited, comp) do
      if MapSet.member?(visited, node) do
        dfs(rest, adj, visited, comp)
      else
        visited = MapSet.put(visited, node)
        neighbors = Map.get(adj, node, [])
        dfs(neighbors ++ rest, adj, visited, [node | comp])
      end
    end

    # Initialize result array and visited set
    result_arr = :array.from_list(chars)
    visited0 = MapSet.new()

    {final_arr, _} =
      Enum.reduce(0..(n - 1), {result_arr, visited0}, fn i, {arr, vis} ->
        if MapSet.member?(vis, i) do
          {arr, vis}
        else
          {comp, new_vis} = explore.(i, vis)
          sorted_idx = Enum.sort(comp)

          comp_chars =
            Enum.map(sorted_idx, fn idx -> Enum.at(chars, idx) end)

          sorted_chars = Enum.sort(comp_chars)

          new_arr =
            Enum.zip(sorted_idx, sorted_chars)
            |> Enum.reduce(arr, fn {idx, ch}, acc -> :array.set(idx, ch, acc) end)

          {new_arr, new_vis}
        end
      end)

    :array.to_list(final_arr) |> Enum.join()
  end

  # Private DFS implementation used inside the module
  defp dfs([], _adj, visited, comp), do: {comp, visited}

  defp dfs([node | rest], adj, visited, comp) do
    if MapSet.member?(visited, node) do
      dfs(rest, adj, visited, comp)
    else
      visited = MapSet.put(visited, node)
      neighbors = Map.get(adj, node, [])
      dfs(neighbors ++ rest, adj, visited, [node | comp])
    end
  end
end
```
