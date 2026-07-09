# 0952. Largest Component Size by Common Factor

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct DSU {
        vector<int> parent, sz;
        DSU(int n) : parent(n), sz(n,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x]==x) return x;
            return parent[x]=find(parent[x]);
        }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(sz[a]<sz[b]) swap(a,b);
            parent[b]=a;
            sz[a]+=sz[b];
        }
    };
    
    int largestComponentSize(vector<int>& nums) {
        int n = nums.size();
        int maxVal = *max_element(nums.begin(), nums.end());
        // smallest prime factor sieve
        vector<int> spf(maxVal+1);
        for (int i=2;i<=maxVal;++i){
            if (!spf[i]){
                for (int j=i;j<=maxVal;j+=i){
                    if(!spf[j]) spf[j]=i;
                }
            }
        }
        DSU dsu(n);
        unordered_map<int,int> primeToIdx;
        primeToIdx.reserve(n*6);
        for (int i=0;i<n;++i){
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                while (x % p == 0) x /= p;
                auto it = primeToIdx.find(p);
                if (it == primeToIdx.end()) {
                    primeToIdx[p] = i;
                } else {
                    dsu.unite(i, it->second);
                }
            }
        }
        vector<int> cnt(n,0);
        int ans=1;
        for (int i=0;i<n;++i){
            int root = dsu.find(i);
            ++cnt[root];
            ans = max(ans, cnt[root]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int largestComponentSize(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int maxVal = 0;
        for (int v : nums) {
            if (v > maxVal) maxVal = v;
        }
        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxVal; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        DSU dsu = new DSU(n);
        java.util.HashMap<Integer, Integer> primeToIndex = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                // union current index with the first occurrence of this prime
                if (!primeToIndex.containsKey(p)) {
                    primeToIndex.put(p, i);
                } else {
                    dsu.union(i, primeToIndex.get(p));
                }
                while (x % p == 0) x /= p;
            }
        }

        int ans = 1;
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            if (dsu.size[root] > ans) ans = dsu.size[root];
        }
        return ans;
    }

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
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1

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

        for idx, num in enumerate(nums):
            x = num
            primes = set()
            while x > 1:
                p = spf[x]
                if p == 0:  # x is prime larger than sqrt(max_val)
                    p = x
                primes.add(p)
                while x % p == 0:
                    x //= p
            for p in primes:
                if p in prime_to_index:
                    union(idx, prime_to_index[p])
                else:
                    prime_to_index[p] = idx

        return max(size[find(i)] for i in range(n))
```

## Python3

```python
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.sz[ra] += self.sz[rb]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        dsu = DSU(n)

        max_val = max(nums)
        # smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        prime_to_index = {}

        for idx, num in enumerate(nums):
            x = num
            seen_primes = set()
            while x > 1:
                p = spf[x]
                seen_primes.add(p)
                while x % p == 0:
                    x //= p
            for p in seen_primes:
                if p not in prime_to_index:
                    prime_to_index[p] = idx
                else:
                    dsu.union(idx, prime_to_index[p])

        # compute max component size
        max_size = 0
        for i in range(n):
            root = dsu.find(i)
            if dsu.sz[root] > max_size:
                max_size = dsu.sz[root]
        return max_size
```

## C

```c
#include <stdlib.h>

static int find_root(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_sets(int *parent, int *size, int a, int b, int *maxComp) {
    int ra = find_root(parent, a);
    int rb = find_root(parent, b);
    if (ra == rb) return;
    if (size[ra] < size[rb]) {
        parent[ra] = rb;
        size[rb] += size[ra];
        if (size[rb] > *maxComp) *maxComp = size[rb];
    } else {
        parent[rb] = ra;
        size[ra] += size[rb];
        if (size[ra] > *maxComp) *maxComp = size[ra];
    }
}

int largestComponentSize(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];

    int *spf = (int *)calloc(maxVal + 1, sizeof(int));
    for (int i = 2; i * i <= maxVal; ++i) {
        if (!spf[i]) {
            for (int j = i * i; j <= maxVal; j += i)
                if (!spf[j]) spf[j] = i;
        }
    }
    for (int i = 2; i <= maxVal; ++i)
        if (!spf[i]) spf[i] = i;

    int *parent = (int *)malloc(numsSize * sizeof(int));
    int *size   = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        parent[i] = i;
        size[i] = 1;
    }

    int *primeIdx = (int *)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) primeIdx[i] = -1;

    int maxComp = 1;

    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        while (x > 1) {
            int p = spf[x];
            while (x % p == 0) x /= p;
            if (primeIdx[p] == -1)
                primeIdx[p] = i;
            else
                union_sets(parent, size, i, primeIdx[p], &maxComp);
        }
    }

    free(spf);
    free(parent);
    free(size);
    free(primeIdx);

    return maxComp;
}
```

## Csharp

```csharp
public class Solution {
    public int LargestComponentSize(int[] nums) {
        int n = nums.Length;
        if (n == 0) return 0;
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long)i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        UnionFind uf = new UnionFind(n);
        var primeToIndex = new System.Collections.Generic.Dictionary<int, int>();

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                if (primeToIndex.TryGetValue(p, out int prevIdx)) {
                    uf.Union(i, prevIdx);
                } else {
                    primeToIndex[p] = i;
                }
                while (x % p == 0) x /= p;
            }
        }

        int[] count = new int[n];
        int maxSize = 1;
        for (int i = 0; i < n; i++) {
            int root = uf.Find(i);
            count[root]++;
            if (count[root] > maxSize) maxSize = count[root];
        }
        return maxSize;
    }

    private class UnionFind {
        private readonly int[] parent;
        private readonly int[] size;

        public UnionFind(int n) {
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
 * @param {number[]} nums
 * @return {number}
 */
var largestComponentSize = function(nums) {
    const n = nums.length;
    if (n === 1) return 1;

    // Union Find implementation
    class UF {
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
            // path compression
            while (x !== p) {
                const nxt = this.parent[x];
                this.parent[x] = p;
                x = nxt;
            }
            return p;
        }
        union(a, b) {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            // union by size
            if (this.sz[ra] < this.sz[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            this.sz[ra] += this.sz[rb];
        }
        size(x) {
            return this.sz[this.find(x)];
        }
    }

    const maxVal = Math.max(...nums);
    // smallest prime factor sieve
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) { // i is prime
            for (let j = i; j <= maxVal; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    const uf = new UF(n);
    const primeToIndex = new Map();

    for (let idx = 0; idx < n; ++idx) {
        let x = nums[idx];
        while (x > 1) {
            const p = spf[x];
            while (x % p === 0) x = Math.trunc(x / p);
            if (!primeToIndex.has(p)) {
                primeToIndex.set(p, idx);
            } else {
                uf.union(idx, primeToIndex.get(p));
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const sz = uf.size(i);
        if (sz > ans) ans = sz;
    }
    return ans;
};
```

## Typescript

```typescript
function largestComponentSize(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    // DSU structures
    const parent = new Uint32Array(n);
    const size = new Uint32Array(n);
    for (let i = 0; i < n; i++) {
        parent[i] = i;
        size[i] = 1;
    }
    let maxSize = 1;

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        if (size[ra] < size[rb]) {
            const tmp = ra;
            ra = rb;
            rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
        if (size[ra] > maxSize) maxSize = size[ra];
    }

    // Build smallest prime factor (SPF) sieve up to max number
    const limit = Math.max(...nums);
    const spf = new Uint32Array(limit + 1);
    for (let i = 2; i * i <= limit; i++) {
        if (spf[i] === 0) {
            for (let j = i * i; j <= limit; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    const primeToIndex = new Map<number, number>();

    // Process each number, factorize and union by shared primes
    for (let idx = 0; idx < n; idx++) {
        let x = nums[idx];
        while (x > 1) {
            const p = spf[x] || x;
            const prevIdx = primeToIndex.get(p);
            if (prevIdx === undefined) {
                primeToIndex.set(p, idx);
            } else {
                union(idx, prevIdx);
            }
            while (x % p === 0) {
                x = Math.floor(x / p);
            }
        }
    }

    return maxSize;
}
```

## Php

```php
class Solution {
    private $parent = [];
    private $size = [];

    private function find($x) {
        while ($this->parent[$x] != $x) {
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    private function union($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra == $rb) return;
        if ($this->size[$ra] < $this->size[$rb]) {
            $tmp = $ra; $ra = $rb; $rb = $tmp;
        }
        $this->parent[$rb] = $ra;
        $this->size[$ra] += $this->size[$rb];
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestComponentSize($nums) {
        $n = count($nums);
        $this->parent = range(0, $n - 1);
        $this->size   = array_fill(0, $n, 1);

        $maxVal = max($nums);
        // smallest prime factor sieve
        $spf = array_fill(0, $maxVal + 1, 0);
        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) { // i is prime
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($spf[$j] == 0) $spf[$j] = $i;
                }
            }
        }

        $primeToIndex = [];

        foreach ($nums as $idx => $num) {
            $x = $num;
            $prev = 0;
            while ($x > 1) {
                $p = $spf[$x] == 0 ? $x : $spf[$x];
                if ($p != $prev) {
                    if (!isset($primeToIndex[$p])) {
                        $primeToIndex[$p] = $idx;
                    } else {
                        $this->union($idx, $primeToIndex[$p]);
                    }
                    $prev = $p;
                }
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                }
            }
        }

        $maxSize = 0;
        for ($i = 0; $i < $n; $i++) {
            $root = $this->find($i);
            if ($this->size[$root] > $maxSize) $maxSize = $this->size[$root];
        }
        return $maxSize;
    }
}
```

## Swift

```swift
class Solution {
    class DSU {
        var parent: [Int]
        var size: [Int]
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
            var xr = find(x)
            var yr = find(y)
            if xr == yr { return }
            if size[xr] < size[yr] {
                swap(&xr, &yr)
            }
            parent[yr] = xr
            size[xr] += size[yr]
        }
    }

    func largestComponentSize(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        if n == 1 { return 1 }
        guard let maxVal = nums.max() else { return 0 }
        var spf = [Int](repeating: 0, count: maxVal + 1)
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

        let dsu = DSU(n)
        var factorToIndex = [Int: Int]()

        for (i, num) in nums.enumerated() {
            var x = num
            while x > 1 {
                let p = spf[x]
                if let idx = factorToIndex[p] {
                    dsu.union(i, idx)
                } else {
                    factorToIndex[p] = i
                }
                while x % p == 0 {
                    x /= p
                }
            }
        }

        var maxSize = 0
        for i in 0..<n {
            if dsu.parent[i] == i {
                maxSize = max(maxSize, dsu.size[i])
            }
        }
        return maxSize
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestComponentSize(nums: IntArray): Int {
        val n = nums.size
        if (n == 0) return 0
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v

        // smallest prime factor sieve
        val spf = IntArray(maxVal + 1)
        for (i in 2..maxVal) {
            if (spf[i] == 0) {
                var j = i
                while (j <= maxVal) {
                    if (spf[j] == 0) spf[j] = i
                    j += i
                }
            }
        }

        val dsu = DSU(n)
        val primeToIndex = HashMap<Int, Int>()
        for (i in 0 until n) {
            var x = nums[i]
            while (x > 1) {
                val p = spf[x]
                val prev = primeToIndex[p]
                if (prev != null) {
                    dsu.union(i, prev)
                } else {
                    primeToIndex[p] = i
                }
                while (x % p == 0) x /= p
            }
        }

        var ans = 1
        val cnt = IntArray(n)
        for (i in 0 until n) {
            val root = dsu.find(i)
            cnt[root]++
            if (cnt[root] > ans) ans = cnt[root]
        }
        return ans
    }

    private class DSU(val n: Int) {
        private val parent = IntArray(n) { it }
        private val size = IntArray(n) { 1 }

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
            if (size[ra] < size[rb]) {
                val tmp = ra; ra = rb; rb = tmp
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
  int largestComponentSize(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;

    // Find maximum value to build SPF array
    int maxVal = nums[0];
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }

    // Smallest prime factor sieve
    List<int> spf = List.filled(maxVal + 1, 0);
    for (int i = 2; i <= maxVal; i++) {
      if (spf[i] == 0) {
        for (int j = i; j <= maxVal; j += i) {
          if (spf[j] == 0) spf[j] = i;
        }
      }
    }

    DSU dsu = DSU(n);
    Map<int, int> primeToIndex = {};

    for (int i = 0; i < n; i++) {
      int x = nums[i];
      while (x > 1) {
        int p = spf[x];
        if (!primeToIndex.containsKey(p)) {
          primeToIndex[p] = i;
        } else {
          dsu.union(i, primeToIndex[p]!);
        }
        while (x % p == 0) {
          x ~/= p;
        }
      }
    }

    int maxSize = 1;
    for (int i = 0; i < n; i++) {
      if (dsu.parent[i] == i && dsu.size[i] > maxSize) {
        maxSize = dsu.size[i];
      }
    }
    return maxSize;
  }
}

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
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	s := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		s[i] = 1
	}
	return &dsu{parent: p, size: s}
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

func largestComponentSize(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
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
			spf[i] = i
			if i*i <= maxVal {
				for j := i * i; j <= maxVal; j += i {
					if spf[j] == 0 {
						spf[j] = i
					}
				}
			}
		}
	}

	ds := newDSU(n)
	primeOwner := make(map[int]int)

	for idx, num := range nums {
		x := num
		for x > 1 {
			p := spf[x]
			if p == 0 { // x is prime larger than sqrt(maxVal)
				p = x
			}
			// union current index with the first index that had this prime factor
			if owner, ok := primeOwner[p]; ok {
				ds.union(idx, owner)
			} else {
				primeOwner[p] = idx
			}
			for x%p == 0 {
				x /= p
			}
		}
	}

	maxSize := 1
	for i := 0; i < n; i++ {
		root := ds.find(i)
		if ds.size[root] > maxSize {
			maxSize = ds.size[root]
		}
	}
	return maxSize
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @size = Array.new(n, 1)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(a, b)
    ra = find(a)
    rb = find(b)
    return if ra == rb
    if @size[ra] < @size[rb]
      ra, rb = rb, ra
    end
    @parent[rb] = ra
    @size[ra] += @size[rb]
  end
end

def factor_primes(num)
  primes = []
  n = num
  if n % 2 == 0
    primes << 2
    n /= 2 while n % 2 == 0
  end
  p = 3
  while p * p <= n
    if n % p == 0
      primes << p
      n /= p while n % p == 0
    end
    p += 2
  end
  primes << n if n > 1
  primes
end

def largest_component_size(nums)
  n = nums.length
  dsu = DSU.new(n)
  prime_to_index = {}

  nums.each_with_index do |num, i|
    factor_primes(num).each do |p|
      if prime_to_index.key?(p)
        dsu.union(i, prime_to_index[p])
      else
        prime_to_index[p] = i
      end
    end
  end

  count = Hash.new(0)
  (0...n).each do |i|
    root = dsu.find(i)
    count[root] += 1
  end
  count.values.max || 0
end
```

## Scala

```scala
object Solution {
    def largestComponentSize(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        val maxVal = nums.max
        // smallest prime factor for each number up to maxVal
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

        val n = nums.length
        val parent = Array.tabulate(n)(i => i)
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

        import scala.collection.mutable
        val primeToIndex = mutable.HashMap[Int, Int]()

        var idx = 0
        while (idx < n) {
            var x = nums(idx)
            var lastPrime = 0
            while (x > 1) {
                val p = spf(x)
                if (p != lastPrime) {
                    primeToIndex.get(p) match {
                        case Some(prevIdx) => union(idx, prevIdx)
                        case None => primeToIndex(p) = idx
                    }
                    lastPrime = p
                }
                while (x % p == 0) x /= p
            }
            idx += 1
        }

        var maxSize = 0
        i = 0
        while (i < n) {
            if (parent(i) == i && size(i) > maxSize) maxSize = size(i)
            i += 1
        }
        maxSize
    }
}
```

## Rust

```rust
use std::collections::HashMap;

struct UnionFind {
    parent: Vec<usize>,
    size: Vec<usize>,
}
impl UnionFind {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        UnionFind { parent, size: vec![1; n] }
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
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

fn smallest_prime_factors(limit: usize) -> Vec<usize> {
    let mut spf = vec![0usize; limit + 1];
    for i in 2..=limit {
        if spf[i] == 0 {
            spf[i] = i;
            if i * i <= limit {
                let mut j = i * i;
                while j <= limit {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
        }
    }
    spf
}

fn distinct_prime_factors(mut x: usize, spf: &Vec<usize>) -> Vec<usize> {
    let mut res = Vec::new();
    while x > 1 {
        let p = spf[x];
        res.push(p);
        while x % p == 0 {
            x /= p;
        }
    }
    res
}

impl Solution {
    pub fn largest_component_size(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let max_val = *nums.iter().max().unwrap() as usize;
        let spf = smallest_prime_factors(max_val);
        let mut uf = UnionFind::new(n);
        let mut prime_to_idx: HashMap<usize, usize> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                continue;
            }
            let factors = distinct_prime_factors(num as usize, &spf);
            for p in factors {
                if let Some(&prev_idx) = prime_to_idx.get(&p) {
                    uf.union(i, prev_idx);
                } else {
                    prime_to_idx.insert(p, i);
                }
            }
        }

        let mut count = vec![0usize; n];
        let mut ans = 1usize;
        for i in 0..n {
            let root = uf.find(i);
            count[root] += 1;
            if count[root] > ans {
                ans = count[root];
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (largest-component-size nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (max-val (apply max nums))
         (spf (make-vector (+ max-val 1) 0)))
    ;; smallest prime factor sieve
    (for ([i (in-range 2 (add1 max-val))])
      (when (= (vector-ref spf i) 0)
        (for ([j (in-range i (+ max-val 1) i)])
          (when (= (vector-ref spf j) 0)
            (vector-set! spf j i)))))
    ;; union‑find structures
    (define parent (make-vector n))
    (define size   (make-vector n 1))
    (for ([i (in-range n)]) (vector-set! parent i i))
    (define (find x)
      (let loop ((y x))
        (if (= (vector-ref parent y) y)
            y
            (begin
              (vector-set! parent y (find (vector-ref parent y)))
              (vector-ref parent y)))))
    (define (union a b)
      (let* ((ra (find a)) (rb (find b)))
        (when (not (= ra rb))
          (if (> (vector-ref size ra) (vector-ref size rb))
              (begin
                (vector-set! parent rb ra)
                (vector-set! size ra (+ (vector-ref size ra) (vector-ref size rb))))
              (begin
                (vector-set! parent ra rb)
                (vector-set! size rb (+ (vector-ref size ra) (vector-ref size rb))))))))
    ;; map factor -> first index containing it
    (define factor-index (make-hash))
    (for ([idx (in-range n)])
      (let ((num (vector-ref arr idx)))
        (let loop ((x num) (prev 0))
          (when (> x 1)
            (let* ((p (vector-ref spf x))
                   (prime (if (= p 0) x p)))
              (unless (= prime prev)
                (cond
                  [(hash-has-key? factor-index prime)
                   (union idx (hash-ref factor-index prime))]
                  [else (hash-set! factor-index prime idx)]))
              (loop (quotient x prime) prime))))))
    ;; compute maximum component size
    (let ((max-size 0))
      (for ([i (in-range n)])
        (when (= (vector-ref parent i) i)
          (set! max-size (max max-size (vector-ref size i)))))
      max-size)))
```

## Erlang

```erlang
-spec largest_component_size(Nums :: [integer()]) -> integer().
largest_component_size(Nums) ->
    N = length(Nums),
    Indices = lists:seq(0, N - 1),
    Parent0 = maps:from_list([{I, I} || I <- Indices]),
    Size0   = maps:from_list([{I, 1} || I <- Indices]),
    {Parent, Size, _FactorMap} =
        lists:foldl(
            fun({Idx, Num}, {Par, Siz, Fac}) ->
                Factors = get_factors(Num),
                lists:foldl(
                    fun(F, {PAcc, SAcc, FAcc}) ->
                        case maps:get(F, FAcc, undefined) of
                            undefined ->
                                {PAcc, SAcc, maps:put(F, Idx, FAcc)};
                            PrevIdx ->
                                {NewPar, NewSiz} = union(PrevIdx, Idx, PAcc, SAcc),
                                {NewPar, NewSiz, FAcc}
                        end
                    end,
                    {Par, Siz, Fac},
                    Factors)
            end,
            {Parent0, Size0, #{}} ,
            lists:zip(Indices, Nums)),
    lists:max(maps:values(Size)).

%% ------------------------------------------------------------------
%% Union‑Find helpers
%% ------------------------------------------------------------------

find(I, Parent) ->
    case maps:get(I, Parent) of
        I -> {I, Parent};
        P ->
            {Root, UpdatedParent} = find(P, Parent),
            NewParent = maps:put(I, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(A, B, Parent, Size) ->
    {RootA, Par1} = find(A, Parent),
    {RootB, Par2} = find(B, Par1),
    if
        RootA == RootB -> {Par2, Size};
        true ->
            SizeA = maps:get(RootA, Size),
            SizeB = maps:get(RootB, Size),
            if
                SizeA < SizeB ->
                    NewParent = maps:put(RootA, RootB, Par2),
                    NewSize   = maps:put(RootB, SizeA + SizeB, Size);
                true ->
                    NewParent = maps:put(RootB, RootA, Par2),
                    NewSize   = maps:put(RootA, SizeA + SizeB, Size)
            end,
            {NewParent, NewSize}
    end.

%% ------------------------------------------------------------------
%% Prime factorisation (distinct factors only)
%% ------------------------------------------------------------------

get_factors(N) -> get_factors(N, 2, []).

get_factors(1, _, Acc) -> Acc;
get_factors(N, F, Acc) when F * F =< N ->
    case N rem F of
        0 ->
            NewAcc = [F | Acc],
            N1 = divide_out(N, F),
            get_factors(N1, F + 1, NewAcc);
        _ ->
            get_factors(N, F + 1, Acc)
    end;
get_factors(N, _, Acc) -> [N | Acc].

divide_out(N, F) when N rem F =:= 0 -> divide_out(N div F, F);
divide_out(N, _) -> N.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_component_size(nums :: [integer]) :: integer
  def largest_component_size(nums) do
    n = length(nums)

    parent =
      Enum.reduce(0..n - 1, :array.new(n, default: 0), fn i, acc ->
        :array.set(i, i, acc)
      end)

    size = :array.new(n, default: 1)

    {parent_final, size_final, _prime_map} =
      Enum.with_index(nums)
      |> Enum.reduce({parent, size, %{}}, fn {num, idx}, {par, sz, pmap} ->
        factors = prime_factors(num)

        {new_par, new_sz, new_pmap} =
          Enum.reduce(factors, {par, sz, pmap}, fn f, {p_acc, s_acc, map_acc} ->
            case Map.fetch(map_acc, f) do
              {:ok, existing_idx} ->
                {p_union, s_union} = union(idx, existing_idx, p_acc, s_acc)
                {p_union, s_union, map_acc}

              :error ->
                {p_acc, s_acc, Map.put(map_acc, f, idx)}
            end
          end)

        {new_par, new_sz, new_pmap}
      end)

    Enum.reduce(0..n - 1, 0, fn i, acc ->
      {root, _} = find(i, parent_final)
      sz = :array.get(root, size_final)
      if sz > acc, do: sz, else: acc
    end)
  end

  # Union-Find functions
  defp find(i, parent) do
    p = :array.get(i, parent)

    if p == i do
      {i, parent}
    else
      {root, parent2} = find(p, parent)
      parent3 = :array.set(i, root, parent2)
      {root, parent3}
    end
  end

  defp union(i, j, parent, size) do
    {ri, parent1} = find(i, parent)
    {rj, parent2} = find(j, parent1)

    if ri == rj do
      {parent2, size}
    else
      sz_i = :array.get(ri, size)
      sz_j = :array.get(rj, size)

      if sz_i < sz_j do
        parent3 = :array.set(ri, rj, parent2)
        size3 = :array.set(rj, sz_i + sz_j, size)
        {parent3, size3}
      else
        parent3 = :array.set(rj, ri, parent2)
        size3 = :array.set(ri, sz_i + sz_j, size)
        {parent3, size3}
      end
    end
  end

  # Prime factorization returning unique factors
  defp prime_factors(num) do
    do_prime_factors(num, 2, [])
  end

  defp do_prime_factors(1, _p, acc), do: Enum.reverse(acc)

  defp do_prime_factors(n, p, acc) when p * p > n do
    Enum.reverse([n | acc])
  end

  defp do_prime_factors(n, p, acc) do
    if rem(n, p) == 0 do
      new_n = divide_out(n, p)
      do_prime_factors(new_n, p + inc(p), [p | acc])
    else
      do_prime_factors(n, p + inc(p), acc)
    end
  end

  defp inc(2), do: 1
  defp inc(_), do: 2

  defp divide_out(n, p) do
    if rem(n, p) == 0 do
      divide_out(div(n, p), p)
    else
      n
    end
  end
end
```
