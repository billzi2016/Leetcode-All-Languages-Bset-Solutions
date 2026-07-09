# 0947. Most Stones Removed with Same Row or Column

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        const int OFFSET = 10001; // offset to differentiate rows and columns
        unordered_map<int, int> parent;
        
        function<int(int)> find = [&](int x) -> int {
            if (parent.find(x) == parent.end()) parent[x] = x;
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        
        auto unite = [&](int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra != rb) parent[ra] = rb;
        };
        
        for (const auto& stone : stones) {
            int row = stone[0];
            int col = stone[1] + OFFSET;
            unite(row, col);
        }
        
        unordered_set<int> components;
        for (const auto& kv : parent) {
            components.insert(find(kv.first));
        }
        
        return static_cast<int>(stones.size()) - static_cast<int>(components.size());
    }
};
```

## Java

```java
class Solution {
    public int removeStones(int[][] stones) {
        UnionFind uf = new UnionFind();
        for (int[] s : stones) {
            int x = s[0];
            int y = s[1] + 10001; // offset to separate rows and columns
            uf.union(x, y);
        }
        java.util.Set<Integer> roots = new java.util.HashSet<>();
        for (int node : uf.parent.keySet()) {
            roots.add(uf.find(node));
        }
        return stones.length - roots.size();
    }

    private static class UnionFind {
        java.util.Map<Integer, Integer> parent = new java.util.HashMap<>();
        java.util.Map<Integer, Integer> rank = new java.util.HashMap<>();

        void add(int x) {
            if (!parent.containsKey(x)) {
                parent.put(x, x);
                rank.put(x, 0);
            }
        }

        int find(int x) {
            int p = parent.get(x);
            if (p != x) {
                int root = find(p);
                parent.put(x, root);
                return root;
            }
            return p;
        }

        void union(int a, int b) {
            add(a);
            add(b);
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            int rankA = rank.get(ra);
            int rankB = rank.get(rb);
            if (rankA < rankB) {
                parent.put(ra, rb);
            } else if (rankA > rankB) {
                parent.put(rb, ra);
            } else {
                parent.put(rb, ra);
                rank.put(ra, rankA + 1);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        offset = 10001  # greater than max coordinate (0..10000)
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for x, y in stones:
            union(x, y + offset)

        # count distinct components among all used nodes
        roots = set()
        for node in parent.keys():
            roots.add(find(node))
        return len(stones) - len(roots)
```

## Python3

```python
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        OFFSET = 10001  # greater than max coordinate (0..10000)

        def find(x):
            # path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for x, y in stones:
            row = x
            col = y + OFFSET
            if row not in parent:
                parent[row] = row
            if col not in parent:
                parent[col] = col
            union(row, col)

        # count distinct components among all used nodes
        roots = {find(node) for node in parent}
        return len(stones) - len(roots)
```

## C

```c
#include <stddef.h>

#define MAX_COORD 10000
#define OFFSET (MAX_COORD + 1)
#define DSU_SIZE (OFFSET * 2 + 5)

static int parent[DSU_SIZE];
static int compCount;

static int find_root(int x) {
    if (parent[x] == x) return x;
    parent[x] = find_root(parent[x]);
    return parent[x];
}

static void unite(int a, int b) {
    int ra = find_root(a);
    int rb = find_root(b);
    if (ra != rb) {
        parent[ra] = rb;
        compCount--;
    }
}

/* LeetCode function */
int removeStones(int** stones, int stonesSize, int* stonesColSize) {
    for (int i = 0; i < DSU_SIZE; ++i) parent[i] = -1;
    compCount = 0;

    for (int i = 0; i < stonesSize; ++i) {
        int rowNode = stones[i][0];
        int colNode = stones[i][1] + OFFSET;

        if (parent[rowNode] == -1) {
            parent[rowNode] = rowNode;
            compCount++;
        }
        if (parent[colNode] == -1) {
            parent[colNode] = colNode;
            compCount++;
        }

        unite(rowNode, colNode);
    }

    return stonesSize - compCount;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int RemoveStones(int[][] stones) {
        var uf = new UnionFind();
        const int offset = 10001;
        foreach (var s in stones) {
            int x = s[0];
            int y = s[1] + offset;
            uf.Add(x);
            uf.Add(y);
            uf.Union(x, y);
        }
        var roots = new HashSet<int>();
        foreach (int node in uf.Nodes) {
            roots.Add(uf.Find(node));
        }
        return stones.Length - roots.Count;
    }

    private class UnionFind {
        private readonly Dictionary<int, int> parent = new Dictionary<int, int>();

        public IEnumerable<int> Nodes => parent.Keys;

        public void Add(int x) {
            if (!parent.ContainsKey(x)) {
                parent[x] = x;
            }
        }

        public int Find(int x) {
            int p = parent[x];
            if (p != x) {
                parent[x] = Find(p);
            }
            return parent[x];
        }

        public void Union(int a, int b) {
            int rootA = Find(a);
            int rootB = Find(b);
            if (rootA == rootB) return;
            parent[rootA] = rootB;
        }
    }
}
```

## Javascript

```javascript
var removeStones = function(stones) {
    const OFFSET = 10001; // greater than max coordinate
    const parent = new Map();

    const find = (x) => {
        if (!parent.has(x)) {
            parent.set(x, x);
            return x;
        }
        let p = parent.get(x);
        if (p !== x) {
            const root = find(p);
            parent.set(x, root);
            return root;
        }
        return p;
    };

    const union = (a, b) => {
        const ra = find(a);
        const rb = find(b);
        if (ra === rb) return false;
        parent.set(ra, rb);
        return true;
    };

    for (const [x, y] of stones) {
        union(x, y + OFFSET);
    }

    const roots = new Set();
    for (const node of parent.keys()) {
        roots.add(find(node));
    }
    const components = roots.size;
    return stones.length - components;
};
```

## Typescript

```typescript
function removeStones(stones: number[][]): number {
    const OFFSET = 10001; // offset to separate rows and columns
    const MAX_SIZE = 20002; // enough for all possible indices (0..10000) + offset

    class UnionFind {
        parent: Int32Array;
        count: number;

        constructor(size: number) {
            this.parent = new Int32Array(size);
            this.parent.fill(-1);
            this.count = 0;
        }

        find(x: number): number {
            if (this.parent[x] === -1) {
                this.parent[x] = x;
                this.count++;
                return x;
            }
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }

        union(a: number, b: number): void {
            const rootA = this.find(a);
            const rootB = this.find(b);
            if (rootA === rootB) return;
            this.parent[rootA] = rootB;
            this.count--;
        }
    }

    const uf = new UnionFind(MAX_SIZE);

    for (const [x, y] of stones) {
        uf.union(x, y + OFFSET);
    }

    // maximum removable stones = total stones - number of connected components
    return stones.length - uf.count;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $stones
     * @return Integer
     */
    public function removeStones($stones) {
        $offset = 10001;
        $parent = [];
        $nodes = [];

        $find = function ($x) use (&$parent, &$find) {
            if (!isset($parent[$x])) {
                $parent[$x] = $x;
                return $x;
            }
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        foreach ($stones as $stone) {
            $a = $stone[0];
            $b = $stone[1] + $offset;
            $nodes[$a] = true;
            $nodes[$b] = true;

            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) {
                $parent[$ra] = $rb;
            }
        }

        $roots = [];
        foreach (array_keys($nodes) as $node) {
            $root = $find($node);
            $roots[$root] = true;
        }

        $components = count($roots);
        return count($stones) - $components;
    }
}
```

## Swift

```swift
class UnionFind {
    private var parent: [Int: Int] = [:]
    private(set) var count = 0

    private func add(_ x: Int) {
        if parent[x] == nil {
            parent[x] = x
            count += 1
        }
    }

    private func find(_ x: Int) -> Int {
        let p = parent[x]!
        if p == x { return x }
        let root = find(p)
        parent[x] = root
        return root
    }

    func union(_ a: Int, _ b: Int) {
        add(a)
        add(b)
        let ra = find(a)
        let rb = find(b)
        if ra != rb {
            parent[ra] = rb
            count -= 1
        }
    }
}

class Solution {
    func removeStones(_ stones: [[Int]]) -> Int {
        let offset = 10001
        let uf = UnionFind()
        for stone in stones {
            let row = stone[0]
            let col = stone[1] + offset
            uf.union(row, col)
        }
        return stones.count - uf.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeStones(stones: Array<IntArray>): Int {
        val OFFSET = 10001
        val parent = HashMap<Int, Int>()
        var components = 0

        fun find(v: Int): Int {
            if (!parent.containsKey(v)) {
                parent[v] = v
                components++
            }
            var p = parent[v]!!
            if (p != v) {
                val root = find(p)
                parent[v] = root
                return root
            }
            return v
        }

        fun union(a: Int, b: Int) {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) {
                parent[ra] = rb
                components--
            }
        }

        for (stone in stones) {
            val x = stone[0]
            val y = stone[1] + OFFSET
            union(x, y)
        }

        return stones.size - components
    }
}
```

## Dart

```dart
class Solution {
  int removeStones(List<List<int>> stones) {
    const int offset = 10001;
    final uf = _UnionFind();
    for (var stone in stones) {
      int x = stone[0];
      int y = stone[1] + offset;
      uf.union(x, y);
    }
    return stones.length - uf.components;
  }
}

class _UnionFind {
  final Map<int, int> _parent = {};
  int components = 0;

  int _find(int x) {
    if (!_parent.containsKey(x)) {
      _parent[x] = x;
      components++;
    }
    if (_parent[x] != x) {
      _parent[x] = _find(_parent[x]!);
    }
    return _parent[x]!;
  }

  void union(int a, int b) {
    int rootA = _find(a);
    int rootB = _find(b);
    if (rootA == rootB) return;
    _parent[rootA] = rootB;
    components--;
  }
}
```

## Golang

```go
func removeStones(stones [][]int) int {
	const offset = 10001
	parent := make(map[int]int)
	components := 0

	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}

	union := func(a, b int) {
		if _, ok := parent[a]; !ok {
			parent[a] = a
			components++
		}
		if _, ok := parent[b]; !ok {
			parent[b] = b
			components++
		}
		ra := find(a)
		rb := find(b)
		if ra != rb {
			parent[ra] = rb
			components--
		}
	}

	for _, s := range stones {
		x := s[0]
		y := s[1] + offset
		union(x, y)
	}
	return len(stones) - components
}
```

## Ruby

```ruby
class UnionFind
  def initialize
    @parent = {}
    @count = 0
  end

  def find(x)
    unless @parent.key?(x)
      @parent[x] = x
      @count += 1
    end
    if @parent[x] != x
      @parent[x] = find(@parent[x])
    end
    @parent[x]
  end

  def union(a, b)
    ra = find(a)
    rb = find(b)
    return if ra == rb
    @parent[ra] = rb
    @count -= 1
  end

  attr_reader :count
end

# @param {Integer[][]} stones
# @return {Integer}
def remove_stones(stones)
  uf = UnionFind.new
  offset = 10_001
  stones.each do |x, y|
    uf.union(x, y + offset)
  end
  stones.length - uf.count
end
```

## Scala

```scala
object Solution {
    def removeStones(stones: Array[Array[Int]]): Int = {
        val offset = 10001
        val parent = scala.collection.mutable.Map[Int, Int]()

        def find(x: Int): Int = {
            if (!parent.contains(x)) {
                parent(x) = x
                return x
            }
            var p = parent(x)
            if (p != x) {
                p = find(p)
                parent(x) = p
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) {
                parent(ra) = rb
            }
        }

        for (stone <- stones) {
            val x = stone(0)
            val y = stone(1) + offset
            union(x, y)
        }

        val components = parent.keys.map(find).toSet.size
        stones.length - components
    }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: HashMap<i32, i32>,
    count: i32,
}

impl DSU {
    fn new() -> Self {
        DSU {
            parent: HashMap::new(),
            count: 0,
        }
    }

    fn find(&mut self, x: i32) -> i32 {
        if !self.parent.contains_key(&x) {
            self.parent.insert(x, x);
            self.count += 1;
            return x;
        }
        let p = *self.parent.get(&x).unwrap();
        if p != x {
            let root = self.find(p);
            self.parent.insert(x, root);
            root
        } else {
            x
        }
    }

    fn union(&mut self, a: i32, b: i32) {
        let ra = self.find(a);
        let rb = self.find(b);
        if ra != rb {
            self.parent.insert(ra, rb);
            self.count -= 1;
        }
    }
}

impl Solution {
    pub fn remove_stones(stones: Vec<Vec<i32>>) -> i32 {
        let mut dsu = DSU::new();
        for stone in stones.iter() {
            let x = stone[0];
            let y = stone[1] + 10001; // offset columns to avoid clash with rows
            dsu.union(x, y);
        }
        (stones.len() as i32) - dsu.count
    }
}
```

## Racket

```racket
(define OFFSET 10001)

(define/contract (remove-stones stones)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((max-index (+ OFFSET 10000))
         (size (+ max-index 1))
         (parent (make-vector size -1))
         (seen (make-hash))
         (component-count 0))

    (define (new-node n)
      (unless (hash-has-key? seen n)
        (hash-set! seen n #t)
        (set! component-count (+ component-count 1))))

    (define (find x)
      (let ((p (vector-ref parent x)))
        (if (= p -1)
            x
            (let ((root (find p)))
              (vector-set! parent x root)
              root))))

    (define (union a b)
      (new-node a)
      (new-node b)
      (let ((ra (find a))
            (rb (find b)))
        (unless (= ra rb)
          (vector-set! parent ra rb)
          (set! component-count (- component-count 1)))))

    (for-each
     (lambda (stone)
       (let* ((x (list-ref stone 0))
              (y (+ (list-ref stone 1) OFFSET)))
         (union x y)))
     stones)

    (- (length stones) component-count)))
```

## Erlang

```erlang
-module(solution).
-export([remove_stones/1]).

-define(OFFSET, 10001).

-spec remove_stones(Stones :: [[integer()]]) -> integer().
remove_stones(Stones) ->
    {_, ComponentCount} = lists:foldl(fun process_stone/2, {#{}, 0}, Stones),
    length(Stones) - ComponentCount.

process_stone([X, Y], {ParentMap, Count}) ->
    NodeRow = X,
    NodeCol = Y + ?OFFSET,
    {ParentMap1, Count1} = ensure_node(NodeRow, ParentMap, Count),
    {ParentMap2, Count2} = ensure_node(NodeCol, ParentMap1, Count1),
    union(NodeRow, NodeCol, ParentMap2, Count2).

ensure_node(Node, Map, Count) ->
    case maps:is_key(Node, Map) of
        true -> {Map, Count};
        false -> {maps:put(Node, -1, Map), Count + 1}
    end.

union(A, B, Map, Count) ->
    {RootA, Map1} = find(A, Map),
    {RootB, Map2} = find(B, Map1),
    if
        RootA == RootB -> {Map2, Count};
        true ->
            NewMap = maps:put(RootA, RootB, Map2),
            {NewMap, Count - 1}
    end.

find(Node, Map) ->
    Parent = maps:get(Node, Map),
    if
        Parent =:= -1 -> {Node, Map};
        true ->
            {Root, UpdatedMap} = find(Parent, Map),
            CompressedMap = maps:put(Node, Root, UpdatedMap),
            {Root, CompressedMap}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_stones(stones :: [[integer]]) :: integer
  def remove_stones(stones) do
    offset = 10_001

    {_, components} =
      Enum.reduce(stones, {%{}, 0}, fn [x, y], {parent, cnt} ->
        col_node = y + offset

        {parent1, cnt1} = ensure_node(parent, cnt, x)
        {parent2, cnt2} = ensure_node(parent1, cnt1, col_node)

        union(parent2, cnt2, x, col_node)
      end)

    length(stones) - components
  end

  defp ensure_node(parent, cnt, node) do
    if Map.has_key?(parent, node) do
      {parent, cnt}
    else
      {Map.put(parent, node, node), cnt + 1}
    end
  end

  defp find(parent, node) do
    case Map.get(parent, node) do
      ^node -> {node, parent}
      parent_node ->
        {root, updated_parent} = find(parent, parent_node)
        {root, Map.put(updated_parent, node, root)}
    end
  end

  defp union(parent, cnt, a, b) do
    {ra, p1} = find(parent, a)
    {rb, p2} = find(p1, b)

    if ra == rb do
      {p2, cnt}
    else
      {Map.put(p2, ra, rb), cnt - 1}
    end
  end
end
```
