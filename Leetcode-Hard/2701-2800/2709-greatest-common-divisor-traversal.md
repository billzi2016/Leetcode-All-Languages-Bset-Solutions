# 2709. Greatest Common Divisor Traversal

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
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

class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return true;
        for (int v : nums) if (v == 1) return false;

        int maxV = *max_element(nums.begin(), nums.end());
        vector<int> spf(maxV + 1);
        for (int i = 2; i <= maxV; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= maxV)
                    for (int j = i * i; j <= maxV; j += i)
                        if (!spf[j]) spf[j] = i;
            }
        }

        DSU dsu(n);
        vector<int> primeIdx(maxV + 1, -1);

        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                while (x % p == 0) x /= p;
                if (primeIdx[p] == -1)
                    primeIdx[p] = i;
                else
                    dsu.unite(i, primeIdx[p]);
            }
        }

        int root = dsu.find(0);
        for (int i = 1; i < n; ++i)
            if (dsu.find(i) != root) return false;
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canTraverseAllPairs(int[] nums) {
        int n = nums.length;
        if (n == 1) return true;
        for (int v : nums) {
            if (v == 1) return false; // cannot connect to any other number
        }

        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long) i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        DSU dsu = new DSU(n);
        int[] primeToIndex = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) primeToIndex[i] = -1;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                if (primeToIndex[p] == -1) {
                    primeToIndex[p] = i;
                } else {
                    dsu.union(i, primeToIndex[p]);
                }
                while (x % p == 0) x /= p;
            }
        }

        int root = dsu.find(0);
        for (int i = 1; i < n; i++) {
            if (dsu.find(i) != root) return false;
        }
        return true;
    }

    private static class DSU {
        int[] parent, size;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
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
}
```

## Python

```python
class Solution(object):
    def canTraverseAllPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        # any number equal to 1 cannot connect with others
        for v in nums:
            if v == 1:
                return False

        max_val = max(nums)

        # smallest prime factor sieve
        spf = [0] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= max_val:
                    step = i
                    start = i * i
                    for j in range(start, max_val + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

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

        prime_to_index = {}

        for idx, val in enumerate(nums):
            x = val
            while x > 1:
                p = spf[x]
                # remove all occurrences of p
                while x % p == 0:
                    x //= p
                if p not in prime_to_index:
                    prime_to_index[p] = idx
                else:
                    union(idx, prime_to_index[p])

        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False
        return True
```

## Python3

```python
import sys
from typing import List

class DSU:
    __slots__ = ("parent", "size")
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        # any number equal to 1 makes traversal impossible when more than one element
        for v in nums:
            if v == 1:
                return False

        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        dsu = DSU(n)
        prime_to_index = {}

        for idx, val in enumerate(nums):
            x = val
            seen_primes = set()
            while x > 1:
                p = spf[x]
                seen_primes.add(p)
                while x % p == 0:
                    x //= p
            for p in seen_primes:
                if p in prime_to_index:
                    dsu.union(idx, prime_to_index[p])
                else:
                    prime_to_index[p] = idx

        root = dsu.find(0)
        for i in range(1, n):
            if dsu.find(i) != root:
                return False
        return True
```

## C

```c
#include <stdbool.h>
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

bool canTraverseAllPairs(int* nums, int numsSize) {
    if (numsSize <= 1) return true;

    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) return false;
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    /* smallest prime factor sieve */
    int *spf = (int *)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) spf[i] = i;
    for (int i = 2; i * i <= maxVal; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= maxVal; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }

    int totalCapacity = numsSize + maxVal + 1;
    int *parent = (int *)malloc(totalCapacity * sizeof(int));
    int *rank   = (int *)malloc(totalCapacity * sizeof(int));
    for (int i = 0; i < totalCapacity; ++i) {
        parent[i] = i;
        rank[i] = 0;
    }

    int *primeNode = (int *)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) primeNode[i] = -1;

    int nextId = numsSize;   // first id for dummy prime nodes

    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        while (x > 1) {
            int p = spf[x];
            if (primeNode[p] == -1) {
                primeNode[p] = nextId++;
            }
            union_sets(parent, rank, idx, primeNode[p]);
            while (x % p == 0) x /= p;
        }
    }

    int root = find_set(parent, 0);
    for (int i = 1; i < numsSize; ++i) {
        if (find_set(parent, i) != root) {
            free(spf);
            free(parent);
            free(rank);
            free(primeNode);
            return false;
        }
    }

    free(spf);
    free(parent);
    free(rank);
    free(primeNode);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanTraverseAllPairs(int[] nums)
    {
        int n = nums.Length;
        if (n == 1) return true;

        foreach (int v in nums)
            if (v == 1) return false; // cannot connect to any other number

        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++)
        {
            if (spf[i] == 0)
            {
                for (int j = i; j <= maxVal; j += i)
                {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        DSU dsu = new DSU(n);
        var primeToIndex = new System.Collections.Generic.Dictionary<int, int>();

        for (int i = 0; i < n; i++)
        {
            int x = nums[i];
            while (x > 1)
            {
                int p = spf[x];
                while (x % p == 0) x /= p; // skip duplicate factor

                if (primeToIndex.TryGetValue(p, out int prevIdx))
                {
                    dsu.Union(i, prevIdx);
                }
                else
                {
                    primeToIndex[p] = i;
                }
            }
        }

        int root = dsu.Find(0);
        for (int i = 1; i < n; i++)
        {
            if (dsu.Find(i) != root) return false;
        }
        return true;
    }

    private class DSU
    {
        private readonly int[] parent;
        private readonly byte[] rank;

        public DSU(int size)
        {
            parent = new int[size];
            rank = new byte[size];
            for (int i = 0; i < size; i++) parent[i] = i;
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

            if (rank[ra] < rank[rb])
                parent[ra] = rb;
            else if (rank[ra] > rank[rb])
                parent[rb] = ra;
            else
            {
                parent[rb] = ra;
                rank[ra]++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canTraverseAllPairs = function(nums) {
    const n = nums.length;
    if (n <= 1) return true;
    for (const v of nums) if (v === 1) return false;

    const maxVal = Math.max(...nums);
    // smallest prime factor sieve
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    class DSU {
        constructor(size) {
            this.parent = new Int32Array(size);
            this.sz = new Int32Array(size);
            for (let i = 0; i < size; ++i) {
                this.parent[i] = i;
                this.sz[i] = 1;
            }
        }
        find(x) {
            let p = this.parent[x];
            while (p !== this.parent[p]) {
                this.parent[p] = this.parent[this.parent[p]];
                p = this.parent[p];
            }
            // compress path
            while (x !== p) {
                const nxt = this.parent[x];
                this.parent[x] = p;
                x = nxt;
            }
            return p;
        }
        union(a, b) {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.sz[ra] < this.sz[rb]) {
                const tmp = ra; ra = rb; rb = tmp;
            }
            this.parent[rb] = ra;
            this.sz[ra] += this.sz[rb];
        }
    }

    const dsu = new DSU(n);
    const primeToIdx = new Int32Array(maxVal + 1);
    primeToIdx.fill(-1);

    for (let i = 0; i < n; ++i) {
        let x = nums[i];
        while (x > 1) {
            const p = spf[x] === 0 ? x : spf[x];
            while (x % p === 0) x = Math.trunc(x / p);
            const prev = primeToIdx[p];
            if (prev === -1) {
                primeToIdx[p] = i;
            } else {
                dsu.union(i, prev);
            }
        }
    }

    const root = dsu.find(0);
    for (let i = 1; i < n; ++i) {
        if (dsu.find(i) !== root) return false;
    }
    return true;
};
```

## Typescript

```typescript
function canTraverseAllPairs(nums: number[]): boolean {
    const n = nums.length;
    if (n <= 1) return true;
    for (const v of nums) if (v === 1) return false;

    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    // smallest prime factor sieve
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    const totalSize = n + maxVal + 1;
    const parent = new Int32Array(totalSize);
    const rank = new Uint8Array(totalSize);
    for (let i = 0; i < totalSize; ++i) parent[i] = i;

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
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
    }

    const offset = n; // dummy nodes for primes start here

    for (let i = 0; i < n; ++i) {
        let x = nums[i];
        while (x > 1) {
            const p = spf[x] || x;
            union(i, offset + p);
            while (x % p === 0) x = Math.floor(x / p);
        }
    }

    const root0 = find(0);
    for (let i = 1; i < n; ++i) {
        if (find(i) !== root0) return false;
    }
    return true;
}
```

## Php

```php
class DSU {
    public array $parent = [];
    public array $rank = [];

    public function __construct(int $size) {
        for ($i = 0; $i < $size; $i++) {
            $this->parent[$i] = $i;
            $this->rank[$i] = 0;
        }
    }

    public function addNode(): int {
        $id = count($this->parent);
        $this->parent[$id] = $id;
        $this->rank[$id] = 0;
        return $id;
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
     * @param Integer[] $nums
     * @return Boolean
     */
    function canTraverseAllPairs($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return true;
        }

        foreach ($nums as $v) {
            if ($v == 1) {
                return false;
            }
        }

        // Precompute smallest prime factor up to 100000
        $MAX = 100000;
        $spf = array_fill(0, $MAX + 1, 0);
        for ($i = 2; $i * $i <= $MAX; $i++) {
            if ($spf[$i] == 0) { // i is prime
                for ($j = $i * $i; $j <= $MAX; $j += $i) {
                    if ($spf[$j] == 0) {
                        $spf[$j] = $i;
                    }
                }
            }
        }
        for ($i = 2; $i <= $MAX; $i++) {
            if ($spf[$i] == 0) {
                $spf[$i] = $i;
            }
        }

        $dsu = new DSU($n);
        $primeToId = [];

        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $primes = [];
            while ($x > 1) {
                $p = $spf[$x];
                $primes[] = $p;
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                }
            }
            foreach ($primes as $p) {
                if (!isset($primeToId[$p])) {
                    $id = $dsu->addNode();
                    $primeToId[$p] = $id;
                }
                $dsu->union($i, $primeToId[$p]);
            }
        }

        $root = $dsu->find(0);
        for ($i = 1; $i < $n; $i++) {
            if ($dsu->find($i) !== $root) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class DSU {
    private var parent: [Int]
    private var rank: [Int]

    init(_ size: Int) {
        parent = Array(0..<size)
        rank = Array(repeating: 0, count: size)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ a: Int, _ b: Int) {
        var x = find(a)
        var y = find(b)
        if x == y { return }
        if rank[x] < rank[y] {
            swap(&x, &y)
        }
        parent[y] = x
        if rank[x] == rank[y] {
            rank[x] += 1
        }
    }
}

class Solution {
    func canTraverseAllPairs(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n <= 1 { return true }

        for v in nums where v == 1 {
            return false
        }

        guard let maxVal = nums.max() else { return true }

        var spf = Array(repeating: 0, count: maxVal + 1)
        if maxVal >= 2 {
            for i in 2...maxVal {
                if spf[i] == 0 {
                    spf[i] = i
                    if i * i <= maxVal {
                        var j = i * i
                        while j <= maxVal {
                            if spf[j] == 0 { spf[j] = i }
                            j += i
                        }
                    }
                }
            }
        }

        let totalSize = n + maxVal + 1
        let dsu = DSU(totalSize)

        for (idx, var value) in nums.enumerated() {
            while value > 1 {
                let p = spf[value]
                dsu.union(idx, n + p)
                while value % p == 0 {
                    value /= p
                }
            }
        }

        let root = dsu.find(0)
        for i in 1..<n {
            if dsu.find(i) != root { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
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
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (rank[x] < rank[y]) {
                parent[x] = y
            } else if (rank[x] > rank[y]) {
                parent[y] = x
            } else {
                parent[y] = x
                rank[x]++
            }
        }
    }

    fun canTraverseAllPairs(nums: IntArray): Boolean {
        val n = nums.size
        if (n <= 1) return true

        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v

        // smallest prime factor sieve
        val spf = IntArray(maxVal + 1)
        for (i in 2..maxVal) {
            if (spf[i] == 0) {
                spf[i] = i
                if (i.toLong() * i <= maxVal) {
                    var j = i * i
                    while (j <= maxVal) {
                        if (spf[j] == 0) spf[j] = i
                        j += i
                    }
                }
            }
        }

        val dsu = DSU(n + maxVal + 1)

        for (i in 0 until n) {
            var x = nums[i]
            if (x == 1) continue
            while (x > 1) {
                val p = spf[x]
                dsu.union(i, n + p)
                while (x % p == 0) x /= p
            }
        }

        val root = dsu.find(0)
        for (i in 1 until n) {
            if (dsu.find(i) != root) return false
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class DSU {
  List<int> parent;
  List<int> size;
  DSU(int n)
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

class Solution {
  bool canTraverseAllPairs(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return true;

    // If any number is 1, it cannot connect to others.
    for (int v in nums) {
      if (v == 1) return false;
    }

    int maxVal = nums.reduce(math.max);
    List<int> spf = List.filled(maxVal + 1, 0);
    for (int i = 2; i <= maxVal; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= maxVal) {
          for (int j = i * i; j <= maxVal; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    DSU dsu = DSU(n);
    Map<int, int> primeToIndex = {};

    for (int idx = 0; idx < n; ++idx) {
      int x = nums[idx];
      while (x > 1) {
        int p = spf[x];
        if (p == 0) p = x;
        if (primeToIndex.containsKey(p)) {
          dsu.union(idx, primeToIndex[p]!);
        } else {
          primeToIndex[p] = idx;
        }
        while (x % p == 0) {
          x ~/= p;
        }
      }
    }

    int root = dsu.find(0);
    for (int i = 1; i < n; ++i) {
      if (dsu.find(i) != root) return false;
    }
    return true;
  }
}
```

## Golang

```go
func canTraverseAllPairs(nums []int) bool {
    n := len(nums)
    if n == 1 {
        return true
    }
    for _, v := range nums {
        if v == 1 {
            return false
        }
    }

    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    // smallest prime factor sieve
    spf := make([]int, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        if spf[i] == 0 {
            for j := i; j <= maxVal; j += i {
                if spf[j] == 0 {
                    spf[j] = i
                }
            }
        }
    }

    // DSU implementation
    parent := make([]int, n)
    size := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = i
        size[i] = 1
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
        if size[ra] < size[rb] {
            ra, rb = rb, ra
        }
        parent[rb] = ra
        size[ra] += size[rb]
    }

    primeFirst := make(map[int]int)

    for i, val := range nums {
        x := val
        for x > 1 {
            p := spf[x]
            if _, ok := primeFirst[p]; !ok {
                primeFirst[p] = i
            } else {
                union(i, primeFirst[p])
            }
            for x%p == 0 {
                x /= p
            }
        }
    }

    root := find(0)
    for i := 1; i < n; i++ {
        if find(i) != root {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def can_traverse_all_pairs(nums)
  n = nums.length
  return true if n <= 1

  # If any number is 1 and there are other numbers, traversal impossible
  return false if nums.any? { |v| v == 1 }

  max_val = nums.max
  spf = Array.new(max_val + 1, 0)
  (2..max_val).each do |i|
    next unless spf[i] == 0
    (i..max_val).step(i) { |j| spf[j] = i if spf[j] == 0 }
  end

  total_nodes = n + max_val + 1
  parent = Array.new(total_nodes) { |idx| idx }
  rank   = Array.new(total_nodes, 0)

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

  nums.each_with_index do |val, idx|
    x = val
    while x > 1
      p = spf[x]
      union.call(idx, n + p)
      x /= p while (x % p).zero?
    end
  end

  root0 = find.call(0)
  (1...n).each do |i|
    return false unless find.call(i) == root0
  end
  true
end
```

## Scala

```scala
object Solution {
    def canTraverseAllPairs(nums: Array[Int]): Boolean = {
        val n = nums.length
        if (n <= 1) return true
        for (v <- nums) {
            if (v == 1) return false
        }
        val maxVal = nums.max
        // smallest prime factor sieve
        val spf = new Array[Int](maxVal + 1)
        var i = 2
        while (i <= maxVal) {
            if (spf(i) == 0) {
                var j = i
                while (j <= maxVal) {
                    if (spf(j) == 0) spf(j) = i
                    j += i
                }
            }
            i += 1
        }

        val offset = n
        val totalSize = n + maxVal + 1
        val parent = new Array[Int](totalSize)
        val sizeArr = new Array[Int](totalSize)
        var idx = 0
        while (idx < totalSize) {
            parent(idx) = idx
            sizeArr(idx) = 1
            idx += 1
        }

        def find(x: Int): Int = {
            var a = x
            while (parent(a) != a) {
                parent(a) = parent(parent(a))
                a = parent(a)
            }
            a
        }

        def union(a: Int, b: Int): Unit = {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (sizeArr(ra) < sizeArr(rb)) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent(rb) = ra
            sizeArr(ra) += sizeArr(rb)
        }

        // connect indices with their prime factor dummy nodes
        var pos = 0
        while (pos < n) {
            var x = nums(pos)
            var lastPrime = 0
            while (x > 1) {
                val p = spf(x)
                if (p != lastPrime) {
                    union(pos, offset + p)
                    lastPrime = p
                }
                while (x % p == 0) x /= p
            }
            pos += 1
        }

        val root0 = find(0)
        var j = 1
        while (j < n) {
            if (find(j) != root0) return false
            j += 1
        }
        true
    }
}
```

## Rust

```rust
use std::mem;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        let size = vec![1; n];
        DSU { parent, size }
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
        if self.size[ra] < self.size[rb] {
            mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n <= 1 {
            return true;
        }
        if nums.iter().any(|&x| x == 1) {
            return false;
        }

        let max_val = *nums.iter().max().unwrap() as usize;

        // smallest prime factor for each number up to max_val
        let mut spf = vec![0usize; max_val + 1];
        for i in 2..=max_val {
            if spf[i] == 0 {
                spf[i] = i;
                if i * i <= max_val {
                    let mut j = i * i;
                    while j <= max_val {
                        if spf[j] == 0 {
                            spf[j] = i;
                        }
                        j += i;
                    }
                }
            }
        }

        let offset = n;
        let total = n + max_val + 1; // extra slot for prime nodes
        let mut dsu = DSU::new(total);

        for (idx, &val) in nums.iter().enumerate() {
            let mut x = val as usize;
            while x > 1 {
                let p = spf[x];
                dsu.union(idx, offset + p);
                while x % p == 0 {
                    x /= p;
                }
            }
        }

        let root0 = dsu.find(0);
        for i in 1..n {
            if dsu.find(i) != root0 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
#lang racket

(struct dsu (parent size) #:transparent)

(define (make-dsu n)
  (define parent (make-vector n))
  (define sz     (make-vector n 1))
  (for ([i (in-range n)])
    (vector-set! parent i i))
  (dsu parent sz))

(define (find d s)
  (let* ((parent (dsu-parent s)))
    (let loop ((v d))
      (let ((p (vector-ref parent v)))
        (if (= p v)
            v
            (let ((root (loop p)))
              (vector-set! parent v root)
              root))))))

(define (union s a b)
  (let* ((ra (find a s))
         (rb (find b s)))
    (when (not (= ra rb))
      (let* ((size   (dsu-size s))
             (sa (vector-ref size ra))
             (sb (vector-ref size rb)))
        (if (> sa sb)
            (begin
              (vector-set! (dsu-parent s) rb ra)
              (vector-set! size ra (+ sa sb)))
            (begin
              (vector-set! (dsu-parent s) ra rb)
              (vector-set! size rb (+ sa sb))))))))

(define (sieve-spf limit)
  (define spf (make-vector (+ limit 1) 0))
  (for ([i (in-range 2 (add1 limit))])
    (when (= (vector-ref spf i) 0)
      (vector-set! spf i i)
      (when (<= (* i i) limit)
        (for ([j (in-range (* i i) (add1 limit) i)])
          (when (= (vector-ref spf j) 0)
            (vector-set! spf j i))))))
  spf)

(define (prime-factors x spf)
  (let loop ((v x) (prev 0) (acc '()))
    (if (= v 1)
        (reverse acc)
        (let ((p (vector-ref spf v)))
          (if (= p prev)
              (loop (quotient v p) p acc)
              (loop (quotient v p) p (cons p acc)))))))

(define/contract (can-traverse-all-pairs nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length nums)))
    (cond [(= n 1) #t]
          [(member 1 nums) #f]
          [else
           (define max-val (apply max nums))
           (define spf (sieve-spf max-val))
           (define d (make-dsu n))
           (define prime-index (make-hash))
           (for ([i (in-range n)])
             (let* ((val (list-ref nums i))
                    (primes (prime-factors val spf)))
               (for ([p primes])
                 (if (hash-has-key? prime-index p)
                     (union d i (hash-ref prime-index p))
                     (hash-set! prime-index p i)))))
           (define root0 (find 0 d))
           (let loop ((i 1))
             (cond [(>= i n) #t]
                   [(= (find i d) root0) (loop (+ i 1))]
                   [else #f]))])))
```

## Erlang

```erlang
-spec can_traverse_all_pairs(Nums :: [integer()]) -> boolean().
can_traverse_all_pairs(Nums) ->
    case length(Nums) of
        0 -> true;
        1 -> true;
        N ->
            MaxVal = lists:max(Nums),
            Limit = trunc(math:sqrt(MaxVal)) + 1,
            Primes = gen_primes(Limit),
            {PrimeMap, IndexMap} = build_maps(Nums, Primes),
            Visited0 = maps:put(0, true, #{}),
            Queue0 = [0],
            VisitedAll = bfs(Queue0, Visited0, PrimeMap, IndexMap),
            maps:size(VisitedAll) == N
    end.

%% Generate list of primes up to Limit using simple sieve
gen_primes(Limit) when Limit < 2 -> [];
gen_primes(Limit) ->
    gen_primes(lists:seq(2, Limit), []).

gen_primes([], Acc) -> lists:reverse(Acc);
gen_primes([H|T], Acc) ->
    Filtered = [X || X <- T, X rem H =/= 0],
    gen_primes(Filtered, [H|Acc]).

%% Build maps:
%% PrimeMap : prime() => list of indices containing this prime
%% IndexMap : index() => list of distinct prime factors of nums[index]
build_maps(Nums, Primes) ->
    build_maps(lists:seq(0, length(Nums)-1), Nums, Primes, #{}, #{}).

build_maps([], [], _, PrimeMap, IndexMap) ->
    {PrimeMap, IndexMap};
build_maps([Idx|RestIdx], [Num|RestNums], Primes, PrimeMap, IndexMap) ->
    Factors = factorize(Num, Primes),
    IndexMap1 = maps:put(Idx, Factors, IndexMap),
    PrimeMap1 = lists:foldl(
        fun(F, PM) ->
            case maps:is_key(F, PM) of
                true -> maps:update(F, fun(L) -> [Idx|L] end, PM);
                false -> maps:put(F, [Idx], PM)
            end
        end,
        PrimeMap,
        Factors),
    build_maps(RestIdx, RestNums, Primes, PrimeMap1, IndexMap1).

%% Factorize number into distinct prime factors using provided primes list
factorize(Num, _) when Num =< 1 -> [];
factorize(Num, Primes) ->
    factorize(Num, Primes, []).

factorize(1, _, Acc) -> lists:reverse(lists:usort(Acc));
factorize(N, [], Acc) ->
    lists:reverse(lists:usort([N|Acc]));
factorize(N, [P|Ps], Acc) when P*P =< N ->
    case N rem P of
        0 ->
            factorize(divide_out(N, P), Ps, [P|Acc]);
        _ ->
            factorize(N, Ps, Acc)
    end;
factorize(N, [_|_]=Ps, Acc) ->
    lists:reverse(lists:usort([N|Acc])).

divide_out(N, P) when N rem P =:= 0 -> divide_out(N div P, P);
divide_out(N, _) -> N.

%% BFS traversal using prime connections
bfs([], Visited, _, _) -> Visited;
bfs([Curr|RestQueue], Visited, PrimeMap, IndexMap) ->
    Factors = maps:get(Curr, IndexMap),
    {PrimeMap1, Visited1, Queue1} =
        lists:foldl(
            fun(F, {PM, V, Q}) ->
                case maps:find(F, PM) of
                    error -> {PM, V, Q};
                    {ok, Idxs} ->
                        {V2, Q2} = lists:foldl(
                            fun(I, {VV, QQ}) ->
                                case maps:is_key(I, VV) of
                                    true -> {VV, QQ};
                                    false -> {maps:put(I, true, VV), [I|QQ]}
                                end
                            end,
                            {V, Q},
                            Idxs),
                        {maps:remove(F, PM), V2, Q2}
                end
            end,
            {PrimeMap, Visited, RestQueue},
            Factors),
    bfs(Queue1, Visited1, PrimeMap1, IndexMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_traverse_all_pairs(nums :: [integer]) :: boolean
  def can_traverse_all_pairs(nums) do
    n = length(nums)

    cond do
      n <= 1 ->
        true

      Enum.any?(nums, &(&1 == 1)) ->
        false

      true ->
        max_val = Enum.max(nums)
        limit = :math.sqrt(max_val) |> trunc()
        primes = generate_primes(limit)

        size_total = n + max_val + 1

        parent =
          0..(size_total - 1)
          |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, i) end)

        sz =
          0..(size_total - 1)
          |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, 1) end)

        {parent_final, _sz} =
          Enum.with_index(nums)
          |> Enum.reduce({parent, sz}, fn {num, idx}, {par, s} ->
            factors = distinct_prime_factors(num, primes)

            Enum.reduce(factors, {par, s}, fn p, {p_par, p_sz} ->
              prime_node = n + p
              {new_par, new_sz, _} = union(p_par, p_sz, idx, prime_node)
              {new_par, new_sz}
            end)
          end)

        root0 = get_root(parent_final, 0)

        Enum.reduce_while(1..(n - 1), true, fn i, _acc ->
          if get_root(parent_final, i) == root0 do
            {:cont, true}
          else
            {:halt, false}
          end
        end)
    end
  end

  # Generate list of primes up to limit (inclusive)
  defp generate_primes(limit) when limit < 2, do: []

  defp generate_primes(limit) do
    2..limit
    |> Enum.reduce([], fn i, acc ->
      if Enum.all?(acc, fn p -> rem(i, p) != 0 end) do
        [i | acc]
      else
        acc
      end
    end)
    |> Enum.reverse()
  end

  # Return distinct prime factors of num using the provided primes list
  defp distinct_prime_factors(num, primes) do
    do_factor(num, primes, [])
    |> Enum.reverse()
  end

  defp do_factor(n, [], acc) do
    if n > 1, do: [n | acc], else: acc
  end

  defp do_factor(n, [p | ps] = list, acc) do
    cond do
      p * p > n ->
        if n > 1, do: [n | acc], else: acc

      rem(n, p) == 0 ->
        new_n = div_out_all(n, p)
        do_factor(new_n, ps, [p | acc])

      true ->
        do_factor(n, ps, acc)
    end
  end

  defp div_out_all(n, p) do
    if rem(n, p) == 0 do
      div_out_all(div(n, p), p)
    else
      n
    end
  end

  # Union-Find find with path compression (returns updated parent map and root)
  defp find(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      {parent, x}
    else
      {parent2, root} = find(parent, p)
      parent3 = Map.put(parent2, x, root)
      {parent3, root}
    end
  end

  # Union by size
  defp union(parent, sz, a, b) do
    {parent1, ra} = find(parent, a)
    {parent2, rb} = find(parent1, b)

    if ra == rb do
      {parent2, sz, false}
    else
      sa = Map.get(sz, ra)
      sb = Map.get(sz, rb)

      cond do
        sa < sb ->
          parent3 = Map.put(parent2, ra, rb)
          sz3 = Map.update!(sz, rb, &(&1 + sa))
          {parent3, sz3, true}

        true ->
          parent3 = Map.put(parent2, rb, ra)
          sz3 = Map.update!(sz, ra, &(&1 + sb))
          {parent3, sz3, true}
      end
    end
  end

  # Get root without modifying the map (used for final checks)
  defp get_root(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      x
    else
      get_root(parent, p)
    end
  end
end
```
