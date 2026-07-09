# 1998. GCD Sort of an Array

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
    
    vector<int> spf;
    void buildSpf(int maxV){
        spf.assign(maxV+1,0);
        for(int i=2;i<=maxV;++i){
            if(spf[i]==0){
                spf[i]=i;
                if ((long long)i*i <= maxV)
                    for(long long j=(long long)i*i;j<=maxV;j+=i)
                        if(spf[j]==0) spf[j]=i;
            }
        }
    }
    
    vector<int> getPrimes(int x){
        vector<int> primes;
        while(x>1){
            int p=spf[x];
            primes.push_back(p);
            while(x%p==0) x/=p;
        }
        return primes;
    }
    
    bool gcdSort(vector<int>& nums) {
        int n = nums.size();
        int maxV = 100000; // per constraints
        buildSpf(maxV);
        
        DSU dsu(n);
        unordered_map<int,int> primeOwner;
        primeOwner.reserve(n*6);
        
        for(int i=0;i<n;++i){
            vector<int> primes = getPrimes(nums[i]);
            for(int p:primes){
                auto it = primeOwner.find(p);
                if(it==primeOwner.end()){
                    primeOwner[p]=i;
                }else{
                    dsu.unite(i, it->second);
                }
            }
        }
        
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        
        unordered_map<int, vector<int>> compOrig, compTarget;
        compOrig.reserve(n);
        compTarget.reserve(n);
        for(int i=0;i<n;++i){
            int root = dsu.find(i);
            compOrig[root].push_back(nums[i]);
            compTarget[root].push_back(sorted[i]);
        }
        
        for(auto &kv : compOrig){
            auto &origVals = kv.second;
            auto &targetVals = compTarget[kv.first];
            sort(origVals.begin(), origVals.end());
            sort(targetVals.begin(), targetVals.end());
            if(origVals != targetVals) return false;
        }
        return true;
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
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a), rb = find(b);
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

    public boolean gcdSort(int[] nums) {
        int n = nums.length;
        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;

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
        java.util.HashMap<Integer, Integer> primeToIdx = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                if (!primeToIdx.containsKey(p)) {
                    primeToIdx.put(p, i);
                } else {
                    dsu.union(i, primeToIdx.get(p));
                }
                while (x % p == 0) x /= p;
            }
        }

        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);

        // collect values per component
        java.util.HashMap<Integer, java.util.ArrayList<Integer>> compVals = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            compVals.computeIfAbsent(root, k -> new java.util.ArrayList<>()).add(nums[i]);
        }
        // sort each component's list ascending
        for (java.util.ArrayList<Integer> list : compVals.values()) {
            java.util.Collections.sort(list);
        }

        // verify by taking smallest available from the component for each position
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            java.util.ArrayList<Integer> list = compVals.get(root);
            int val = list.remove(list.size() - 1); // take largest remaining (since we sorted ascending)
            if (val != sorted[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_val = max(nums)

        # sieve for smallest prime factor
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        def prime_factors(x):
            while x > 1:
                p = spf[x]
                yield p
                while x % p == 0:
                    x //= p

        parent = list(range(n))
        rank = [0] * n

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1

        prime_to_index = {}
        for i, val in enumerate(nums):
            seen = set()
            for p in prime_factors(val):
                if p in seen:
                    continue
                seen.add(p)
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i

        # group indices by root
        groups = {}
        for i in range(n):
            r = find(i)
            groups.setdefault(r, []).append(i)

        sorted_nums = sorted(nums)
        for idxs in groups.values():
            original_vals = [nums[i] for i in idxs]
            target_vals = [sorted_nums[i] for i in idxs]
            if sorted(original_vals) != sorted(target_vals):
                return False
        return True
```

## Python3

```python
class Solution:
    def gcdSort(self, nums):
        from collections import defaultdict
        n = len(nums)
        max_val = max(nums)

        # smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        class DSU:
            __slots__ = ("parent", "size")
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return
                if self.size[ra] < self.size[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                self.size[ra] += self.size[rb]

        dsu = DSU(n)
        prime_to_index = {}

        for i, val in enumerate(nums):
            x = val
            seen = set()
            while x > 1:
                p = spf[x]
                seen.add(p)
                while x % p == 0:
                    x //= p
            for p in seen:
                if p in prime_to_index:
                    dsu.union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i

        sorted_nums = sorted(nums)
        comp_vals = defaultdict(list)
        comp_target = defaultdict(list)

        for i in range(n):
            r = dsu.find(i)
            comp_vals[r].append(nums[i])
            comp_target[r].append(sorted_nums[i])

        for r in comp_vals:
            if sorted(comp_vals[r]) != sorted(comp_target[r]):
                return False
        return True
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int *uf_parent;
static int *uf_rank;

static int uf_find(int x) {
    if (uf_parent[x] != x)
        uf_parent[x] = uf_find(uf_parent[x]);
    return uf_parent[x];
}

static void uf_union(int a, int b) {
    a = uf_find(a);
    b = uf_find(b);
    if (a == b) return;
    if (uf_rank[a] < uf_rank[b]) {
        uf_parent[a] = b;
    } else if (uf_rank[a] > uf_rank[b]) {
        uf_parent[b] = a;
    } else {
        uf_parent[b] = a;
        uf_rank[a]++;
    }
}

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

typedef struct {
    int root;
    int val;
} Node;

static int cmp_node(const void *a, const void *b) {
    const Node *na = (const Node *)a;
    const Node *nb = (const Node *)b;
    if (na->root != nb->root)
        return na->root - nb->root;
    return na->val - nb->val;
}

bool gcdSort(int* nums, int numsSize) {
    if (numsSize <= 1) return true;

    int maxV = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxV) maxV = nums[i];

    /* smallest prime factor sieve */
    int *spf = (int *)malloc((maxV + 1) * sizeof(int));
    for (int i = 0; i <= maxV; ++i) spf[i] = i;
    for (int i = 2; i * i <= maxV; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= maxV; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }

    /* union‑find initialization */
    uf_parent = (int *)malloc(numsSize * sizeof(int));
    uf_rank   = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        uf_parent[i] = i;
        uf_rank[i] = 0;
    }

    int *prime_first = (int *)malloc((maxV + 1) * sizeof(int));
    for (int i = 0; i <= maxV; ++i) prime_first[i] = -1;

    /* connect indices sharing a prime factor */
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        while (val > 1) {
            int p = spf[val];
            while (val % p == 0) val /= p;
            if (prime_first[p] == -1)
                prime_first[p] = i;
            else
                uf_union(i, prime_first[p]);
        }
    }

    /* sorted target array */
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmp_int);

    /* build node arrays for comparison */
    Node *origNodes   = (Node *)malloc(numsSize * sizeof(Node));
    Node *targetNodes = (Node *)malloc(numsSize * sizeof(Node));

    for (int i = 0; i < numsSize; ++i) {
        int r = uf_find(i);
        origNodes[i].root   = r;
        origNodes[i].val    = nums[i];
        targetNodes[i].root = r;
        targetNodes[i].val  = sorted[i];
    }

    qsort(origNodes,   numsSize, sizeof(Node), cmp_node);
    qsort(targetNodes, numsSize, sizeof(Node), cmp_node);

    bool ok = true;
    for (int i = 0; i < numsSize; ++i) {
        if (origNodes[i].root != targetNodes[i].root ||
            origNodes[i].val  != targetNodes[i].val) {
            ok = false;
            break;
        }
    }

    free(spf);
    free(prime_first);
    free(uf_parent);
    free(uf_rank);
    free(sorted);
    free(origNodes);
    free(targetNodes);

    return ok;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool GcdSort(int[] nums) {
        int n = nums.Length;
        int maxVal = nums.Max();

        // Smallest prime factor sieve
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

        DSU dsu = new DSU(n);
        var primeToIndex = new Dictionary<int, int>();

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            var primes = new HashSet<int>();
            while (x > 1) {
                int p = spf[x];
                primes.Add(p);
                while (x % p == 0) x /= p;
            }
            foreach (int p in primes) {
                if (!primeToIndex.ContainsKey(p)) {
                    primeToIndex[p] = i;
                } else {
                    dsu.Union(i, primeToIndex[p]);
                }
            }
        }

        int[] sorted = (int[])nums.Clone();
        Array.Sort(sorted);

        var groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int root = dsu.Find(i);
            if (!groups.ContainsKey(root)) groups[root] = new List<int>();
            groups[root].Add(i);
        }

        foreach (var kvp in groups) {
            var indices = kvp.Value;
            var origVals = new List<int>(indices.Count);
            var targetVals = new List<int>(indices.Count);
            foreach (int idx in indices) {
                origVals.Add(nums[idx]);
                targetVals.Add(sorted[idx]);
            }
            origVals.Sort();
            targetVals.Sort();
            for (int i = 0; i < origVals.Count; i++) {
                if (origVals[i] != targetVals[i]) return false;
            }
        }

        return true;
    }

    private class DSU {
        private int[] parent;
        private int[] size;

        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
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
 * @return {boolean}
 */
var gcdSort = function(nums) {
    const n = nums.length;
    if (n <= 1) return true;

    // find max value for sieve limit
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

    const getPrimeFactors = (x) => {
        const res = [];
        while (x > 1) {
            const p = spf[x];
            res.push(p);
            while (x % p === 0) x = Math.trunc(x / p);
        }
        return res;
    };

    // DSU
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
            const p = this.parent;
            while (p[x] !== x) {
                p[x] = p[p[x]];
                x = p[x];
            }
            return x;
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
    const primeToIndex = new Map();

    // union indices sharing a prime factor
    for (let i = 0; i < n; ++i) {
        const primes = getPrimeFactors(nums[i]);
        for (const p of primes) {
            if (!primeToIndex.has(p)) {
                primeToIndex.set(p, i);
            } else {
                dsu.union(i, primeToIndex.get(p));
            }
        }
    }

    // component value multiset
    const compMap = new Map(); // root -> Map(value->count)
    for (let i = 0; i < n; ++i) {
        const r = dsu.find(i);
        let m = compMap.get(r);
        if (!m) {
            m = new Map();
            compMap.set(r, m);
        }
        const val = nums[i];
        m.set(val, (m.get(val) || 0) + 1);
    }

    // sorted target
    const sorted = [...nums].sort((a, b) => a - b);

    for (let i = 0; i < n; ++i) {
        const r = dsu.find(i);
        const m = compMap.get(r);
        const need = sorted[i];
        const cnt = m.get(need);
        if (!cnt) return false;
        if (cnt === 1) m.delete(need);
        else m.set(need, cnt - 1);
    }

    return true;
};
```

## Typescript

```typescript
function gcdSort(nums: number[]): boolean {
    const n = nums.length;
    const sorted = [...nums].sort((a, b) => a - b);

    class DSU {
        parent: Int32Array;
        rank: Int8Array;
        constructor(size: number) {
            this.parent = new Int32Array(size);
            this.rank = new Int8Array(size);
            for (let i = 0; i < size; i++) this.parent[i] = i;
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

    // smallest prime factor sieve
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    const primeToIndex = new Map<number, number>();
    function getPrimes(x: number): number[] {
        const res: number[] = [];
        while (x > 1) {
            const p = spf[x];
            res.push(p);
            while (x % p === 0) x /= p;
        }
        return res;
    }

    for (let i = 0; i < n; i++) {
        const primes = getPrimes(nums[i]);
        for (const p of primes) {
            if (primeToIndex.has(p)) {
                dsu.union(i, primeToIndex.get(p)!);
            } else {
                primeToIndex.set(p, i);
            }
        }
    }

    // group indices by component
    const groups = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const r = dsu.find(i);
        let arr = groups.get(r);
        if (!arr) {
            arr = [];
            groups.set(r, arr);
        }
        arr.push(i);
    }

    // compare multisets within each component
    for (const idxs of groups.values()) {
        const orig: number[] = [];
        const target: number[] = [];
        for (const idx of idxs) {
            orig.push(nums[idx]);
            target.push(sorted[idx]);
        }
        orig.sort((a, b) => a - b);
        target.sort((a, b) => a - b);
        if (orig.length !== target.length) return false;
        for (let i = 0; i < orig.length; i++) {
            if (orig[i] !== target[i]) return false;
        }
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function gcdSort($nums) {
        $n = count($nums);
        if ($n <= 1) return true;

        // Sorted version of the array
        $sorted = $nums;
        sort($sorted, SORT_NUMERIC);

        // Build smallest prime factor (SPF) sieve up to max value
        $maxVal = max($nums);
        $spf = array_fill(0, $maxVal + 1, 0);
        for ($i = 2; $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) {
                $spf[$i] = $i;
                if ((int)$i * $i <= $maxVal) {
                    for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                        if ($spf[$j] == 0) $spf[$j] = $i;
                    }
                }
            }
        }

        // Union-Find structure
        $dsu = new class($n) {
            public array $parent;
            public array $size;
            public function __construct(int $n){
                $this->parent = range(0, $n - 1);
                $this->size   = array_fill(0, $n, 1);
            }
            public function find(int $x): int{
                while ($this->parent[$x] != $x) {
                    $this->parent[$x] = $this->parent[$this->parent[$x]];
                    $x = $this->parent[$x];
                }
                return $x;
            }
            public function union(int $a, int $b): void{
                $ra = $this->find($a);
                $rb = $this->find($b);
                if ($ra === $rb) return;
                if ($this->size[$ra] < $this->size[$rb]) {
                    $tmp = $ra; $ra = $rb; $rb = $tmp;
                }
                $this->parent[$rb] = $ra;
                $this->size[$ra] += $this->size[$rb];
            }
        };

        // Map each prime factor to the first index where it appears
        $primeToIndex = [];

        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $seenPrimes = [];
            while ($x > 1) {
                $p = $spf[$x];
                if (!isset($seenPrimes[$p])) {
                    $seenPrimes[$p] = true;
                    if (isset($primeToIndex[$p])) {
                        $dsu->union($i, $primeToIndex[$p]);
                    } else {
                        $primeToIndex[$p] = $i;
                    }
                }
                while ($x % $p == 0) $x = intdiv($x, $p);
            }
        }

        // Group original and sorted values by component root
        $origGroups   = [];
        $sortedGroups = [];

        for ($i = 0; $i < $n; $i++) {
            $root = $dsu->find($i);
            $origGroups[$root][]   = $nums[$i];
            $sortedGroups[$root][] = $sorted[$i];
        }

        // Compare each component's multisets
        foreach ($origGroups as $root => $list) {
            $a = $list;
            $b = $sortedGroups[$root] ?? [];
            sort($a, SORT_NUMERIC);
            sort($b, SORT_NUMERIC);
            if (count($a) !== count($b)) return false;
            for ($k = 0; $k < count($a); $k++) {
                if ($a[$k] !== $b[$k]) return false;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func gcdSort(_ nums: [Int]) -> Bool {
        let n = nums.count
        guard n > 1 else { return true }
        let maxVal = nums.max()!
        // Smallest prime factor sieve
        var spf = Array(repeating: 0, count: maxVal + 1)
        if maxVal >= 2 {
            for i in 2...maxVal {
                if spf[i] == 0 {
                    var j = i
                    while j <= maxVal {
                        if spf[j] == 0 { spf[j] = i }
                        j += i
                    }
                }
            }
        }
        
        struct DSU {
            var parent: [Int]
            var size: [Int]
            init(_ n: Int) {
                parent = Array(0..<n)
                size = Array(repeating: 1, count: n)
            }
            mutating func find(_ x: Int) -> Int {
                var v = x
                while parent[v] != v {
                    parent[v] = parent[parent[v]]
                    v = parent[v]
                }
                return v
            }
            mutating func union(_ a: Int, _ b: Int) {
                var ra = find(a)
                var rb = find(b)
                if ra == rb { return }
                if size[ra] < size[rb] {
                    swap(&ra, &rb)
                }
                parent[rb] = ra
                size[ra] += size[rb]
            }
        }
        
        var dsu = DSU(n)
        var primeToIndex = [Int: Int]()
        
        for i in 0..<n {
            var x = nums[i]
            var primes = Set<Int>()
            while x > 1 {
                let p = spf[x]
                primes.insert(p)
                while x % p == 0 { x /= p }
            }
            for p in primes {
                if let prev = primeToIndex[p] {
                    dsu.union(i, prev)
                } else {
                    primeToIndex[p] = i
                }
            }
        }
        
        var compVals = [Int: [Int]]()
        var targetVals = [Int: [Int]]()
        for i in 0..<n {
            let root = dsu.find(i)
            compVals[root, default: []].append(nums[i])
        }
        let sortedNums = nums.sorted()
        for i in 0..<n {
            let root = dsu.find(i)
            targetVals[root, default: []].append(sortedNums[i])
        }
        
        for (root, var vals) in compVals {
            guard var tvals = targetVals[root] else { return false }
            vals.sort()
            tvals.sort()
            if vals != tvals { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.HashMap
import kotlin.math.sqrt

class Solution {
    fun gcdSort(nums: IntArray): Boolean {
        val n = nums.size
        val sorted = nums.clone()
        sorted.sort()

        // Build smallest prime factor (SPF) sieve up to max value
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v
        val spf = IntArray(maxVal + 1) { it }
        val limit = sqrt(maxVal.toDouble()).toInt()
        for (i in 2..limit) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= maxVal) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
        }

        // Union-Find structure
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
                val tmp = ra; ra = rb; rb = tmp
            }
            parent[rb] = ra
            if (rank[ra] == rank[rb]) rank[ra]++
        }

        // Map each prime to first index containing it
        val primeToIndex = IntArray(maxVal + 1) { -1 }

        for (i in 0 until n) {
            var x = nums[i]
            while (x > 1) {
                val p = spf[x]
                if (primeToIndex[p] == -1) {
                    primeToIndex[p] = i
                } else {
                    union(i, primeToIndex[p])
                }
                while (x % p == 0) x /= p
            }
        }

        // Map values to queue of original indices
        val valueIndices = HashMap<Int, ArrayDeque<Int>>()
        for (i in 0 until n) {
            val list = valueIndices.computeIfAbsent(nums[i]) { ArrayDeque() }
            list.add(i)
        }

        // Verify each position can receive correct value
        for (i in 0 until n) {
            val targetVal = sorted[i]
            val idxQueue = valueIndices[targetVal] ?: return false
            val originalIdx = idxQueue.pollFirst()
            if (find(originalIdx) != find(i)) return false
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:collection';

class UnionFind {
  late List<int> parent;
  late List<int> rank;

  UnionFind(int n) {
    parent = List<int>.generate(n, (i) => i);
    rank = List<int>.filled(n, 0);
  }

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
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

class Solution {
  bool gcdSort(List<int> nums) {
    int n = nums.length;
    int maxVal = nums[0];
    for (int v in nums) if (v > maxVal) maxVal = v;

    // smallest prime factor sieve
    List<int> spf = List<int>.filled(maxVal + 1, 0);
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

    UnionFind uf = UnionFind(n);
    Map<int, int> primeToIndex = {};

    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      // collect unique prime factors
      while (x > 1) {
        int p = spf[x];
        if (!primeToIndex.containsKey(p)) {
          primeToIndex[p] = i;
        } else {
          uf.union(i, primeToIndex[p]!);
        }
        while (x % p == 0) x ~/= p;
      }
    }

    List<int> sorted = List<int>.from(nums);
    sorted.sort();

    Map<int, List<int>> compOrig = HashMap();
    Map<int, List<int>> compTarget = HashMap();

    for (int i = 0; i < n; ++i) {
      int root = uf.find(i);
      compOrig.putIfAbsent(root, () => []).add(nums[i]);
      compTarget.putIfAbsent(root, () => []).add(sorted[i]);
    }

    for (int root in compOrig.keys) {
      List<int> a = compOrig[root]!;
      List<int> b = compTarget[root]!;
      a.sort();
      b.sort();
      if (a.length != b.length) return false;
      for (int i = 0; i < a.length; ++i) {
        if (a[i] != b[i]) return false;
      }
    }

    return true;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

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

func gcdSort(nums []int) bool {
	n := len(nums)
	if n <= 1 {
		return true
	}
	sorted := make([]int, n)
	copy(sorted, nums)
	sort.Ints(sorted)

	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}

	// smallest prime factor sieve
	spf := make([]int, maxVal+1)
	for i := 2; i <= maxVal; i++ {
		spf[i] = i
	}
	for i := 2; i*i <= maxVal; i++ {
		if spf[i] == i { // prime
			for j := i * i; j <= maxVal; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}

	getPrimes := func(x int) []int {
		primes := []int{}
		for x > 1 {
			p := spf[x]
			primes = append(primes, p)
			for x%p == 0 {
				x /= p
			}
		}
		return primes
	}

	ds := newDSU(n)
	primeIdx := make(map[int]int)

	for i, v := range nums {
		primes := getPrimes(v)
		for _, p := range primes {
			if idx, ok := primeIdx[p]; ok {
				ds.union(i, idx)
			} else {
				primeIdx[p] = i
			}
		}
	}

	origMap := make(map[int][]int)
	targetMap := make(map[int][]int)

	for i := 0; i < n; i++ {
		root := ds.find(i)
		origMap[root] = append(origMap[root], nums[i])
		targetMap[root] = append(targetMap[root], sorted[i])
	}

	for root, origVals := range origMap {
		targetVals := targetMap[root]
		if len(origVals) != len(targetVals) {
			return false
		}
		sort.Ints(origVals)
		sort.Ints(targetVals)
		for i := 0; i < len(origVals); i++ {
			if origVals[i] != targetVals[i] {
				return false
			}
		}
	}

	return true
}
```

## Ruby

```ruby
def gcd_sort(nums)
  n = nums.length
  sorted = nums.sort

  max_val = nums.max
  spf = Array.new(max_val + 1, 0)
  (2..max_val).each do |i|
    if spf[i] == 0
      spf[i] = i
      j = i * i
      while j <= max_val
        spf[j] = i if spf[j] == 0
        j += i
      end
    end
  end

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

  prime_to_index = {}

  nums.each_with_index do |val, idx|
    x = val
    while x > 1
      p = spf[x]
      # union current index with first occurrence of this prime
      if prime_to_index.key?(p)
        union.call(idx, prime_to_index[p])
      else
        prime_to_index[p] = idx
      end
      while x % p == 0
        x /= p
      end
    end
  end

  comp_original = Hash.new { |h, k| h[k] = [] }
  comp_target   = Hash.new { |h, k| h[k] = [] }

  n.times do |i|
    root = find.call(i)
    comp_original[root] << nums[i]
    comp_target[root]   << sorted[i]
  end

  comp_original.each do |root, arr|
    arr.sort!
    comp_target[root].sort!
    return false unless arr == comp_target[root]
  end
  true
end
```

## Scala

```scala
object Solution {
  def gcdSort(nums: Array[Int]): Boolean = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)

    // Smallest prime factor sieve up to max value in nums
    var maxVal = nums.max
    if (maxVal < 2) maxVal = 2
    val spf = new Array[Int](maxVal + 1)
    var i = 2
    while (i <= maxVal) {
      if (spf(i) == 0) {
        spf(i) = i
        if (i.toLong * i <= maxVal) {
          var j = i * i
          while (j <= maxVal) {
            if (spf(j) == 0) spf(j) = i
            j += i
          }
        }
      }
      i += 1
    }

    // Disjoint Set Union
    class DSU(size: Int) {
      private val parent = Array.tabulate(size)(idx => idx)
      private val rank   = new Array[Int](size)

      def find(x: Int): Int = {
        var a = x
        while (parent(a) != a) a = parent(a)
        var root = a
        var cur  = x
        while (parent(cur) != cur) {
          val nxt = parent(cur)
          parent(cur) = root
          cur = nxt
        }
        root
      }

      def union(x: Int, y: Int): Unit = {
        var xr = find(x)
        var yr = find(y)
        if (xr == yr) return
        if (rank(xr) < rank(yr)) {
          parent(xr) = yr
        } else if (rank(xr) > rank(yr)) {
          parent(yr) = xr
        } else {
          parent(yr) = xr
          rank(xr) += 1
        }
      }
    }

    val dsu = new DSU(n)
    import scala.collection.mutable.{HashMap, ArrayBuffer}

    // Map each prime factor to the first index where it appears
    val primeToIdx = HashMap[Int, Int]()

    var idx = 0
    while (idx < n) {
      var x = nums(idx)
      while (x > 1) {
        val p = spf(x)
        primeToIdx.get(p) match {
          case Some(prevIdx) => dsu.union(idx, prevIdx)
          case None          => primeToIdx(p) = idx
        }
        while (x % p == 0) x /= p
      }
      idx += 1
    }

    // Group original and target values by component root
    val compOrig   = HashMap[Int, ArrayBuffer[Int]]()
    val compSorted = HashMap[Int, ArrayBuffer[Int]]()

    var k = 0
    while (k < n) {
      val r = dsu.find(k)
      compOrig.getOrElseUpdate(r, ArrayBuffer()).append(nums(k))
      compSorted.getOrElseUpdate(r, ArrayBuffer()).append(sorted(k))
      k += 1
    }

    // For each component, the multisets must match
    for ((root, origList) <- compOrig) {
      val targetList = compSorted(root)
      val a = origList.sorted
      val b = targetList.sorted
      if (!a.sameElements(b)) return false
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn gcd_sort(nums: Vec<i32>) -> bool {
        let n = nums.len();
        // Build smallest prime factor (SPF) sieve
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut spf = vec![0usize; max_val + 1];
        for i in 2..=max_val {
            if spf[i] == 0 {
                for j in (i..=max_val).step_by(i) {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                }
            }
        }

        // Union-Find structure
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

        let mut dsu = DSU::new(n);
        // map prime -> first index where it appears
        let mut prime_first: Vec<i32> = vec![-1; max_val + 1];

        for (i, &val_i) in nums.iter().enumerate() {
            let mut x = val_i as usize;
            while x > 1 {
                let p = spf[x];
                while x % p == 0 { x /= p; }
                if prime_first[p] == -1 {
                    prime_first[p] = i as i32;
                } else {
                    dsu.union(i, prime_first[p] as usize);
                }
            }
        }

        // Sorted target array
        let mut sorted = nums.clone();
        sorted.sort();

        // Group values by component root
        let mut group_orig: Vec<Vec<i32>> = vec![Vec::new(); n];
        let mut group_target: Vec<Vec<i32>> = vec![Vec::new(); n];

        for i in 0..n {
            let r = dsu.find(i);
            group_orig[r].push(nums[i]);
            group_target[r].push(sorted[i]);
        }

        // Compare multisets within each component
        for root in 0..n {
            if !group_orig[root].is_empty() {
                let mut a = &mut group_orig[root];
                let mut b = &mut group_target[root];
                a.sort_unstable();
                b.sort_unstable();
                if a != b {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (gcd-sort nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [max-val (apply max nums)]
         [spf
          (let ([limit max-val]
                [vec (make-vector (+ limit 1) 0)])
            (for ([i (in-range 2 (add1 limit))])
              (when (= (vector-ref vec i) 0)
                (vector-set! vec i i)
                (when (<= (* i i) limit)
                  (for ([j (in-range (* i i) (add1 limit) i)])
                    (when (= (vector-ref vec j) 0)
                      (vector-set! vec j i))))))
            vec)]
         [parent (make-vector n)])
    (for ([i (in-range n)]) (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let* ([ra (find a)] [rb (find b)])
        (when (not (= ra rb))
          (vector-set! parent ra rb))))
    (define (prime-factors x)
      (let loop ((n x) (f '()))
        (if (= n 1)
            f
            (let* ([p (vector-ref spf n)]
                   [new-f (if (member p f) f (cons p f))])
              (loop (/ n p) new-f)))))
    (define factor-index (make-hash))
    (for ([i (in-range n)])
      (let ([val (vector-ref arr i)]
            [factors (prime-factors (vector-ref arr i))])
        (for ([p factors])
          (if (hash-has-key? factor-index p)
              (union i (hash-ref factor-index p))
              (hash-set! factor-index p i)))))
    (define comp-counts (make-hash))
    (for ([i (in-range n)])
      (let* ([root (find i)]
             [val (vector-ref arr i)]
             [inner (hash-ref comp-counts root #f)])
        (if inner
            (hash-set! inner val (+ 1 (hash-ref inner val 0)))
            (begin
              (define new-inner (make-hash))
              (hash-set! new-inner val 1)
              (hash-set! comp-counts root new-inner)))))
    (define sorted-nums (sort nums <))
    (let loop ((idx 0))
      (if (= idx n)
          #t
          (let* ([root (find idx)]
                 [inner (hash-ref comp-counts root)]
                 [target (list-ref sorted-nums idx)])
            (let ([cnt (hash-ref inner target 0)])
              (if (= cnt 0)
                  #f
                  (begin
                    (hash-set! inner target (- cnt 1))
                    (loop (+ idx 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([gcd_sort/1]).

-spec gcd_sort(Nums :: [integer()]) -> boolean().
gcd_sort(Nums) ->
    N = length(Nums),
    MaxPrime = 316,
    Primes = primes_upto(MaxPrime),
    Parent0 = maps:from_list([{Idx, Idx} || Idx <- lists:seq(1, N)]),
    {Parent1, _PrimeMap} = process_nums(Nums, 1, Parent0, #{}, Primes),
    Sorted = lists:sort(Nums),
    {_FinalParent, CompMap} = build_comp_maps(Nums, Sorted, 1, Parent1, #{}),
    verify_components(CompMap).

%% Build list of primes up to Max using simple sieve (Max is small)
primes_upto(Max) ->
    sieve(lists:seq(2, Max), []).

sieve([], Acc) -> lists:reverse(Acc);
sieve([H|T], Acc) ->
    Rest = [X || X <- T, X rem H =/= 0],
    sieve(Rest, [H|Acc]).

%% Process each number to union indices sharing prime factors
process_nums([], _, Parent, PrimeMap, _) -> {Parent, PrimeMap};
process_nums([V|Rest], Idx, Parent, PrimeMap, Primes) ->
    Factors = prime_factors(V, Primes),
    {NewParent, NewPrimeMap} = lists:foldl(
        fun(F, {PAcc, PMAcc}) ->
            case maps:get(F, PMAcc, undefined) of
                undefined -> {PAcc, maps:put(F, Idx, PMAcc)};
                OtherIdx ->
                    UpdatedParent = union(PAcc, Idx, OtherIdx),
                    {UpdatedParent, PMAcc}
            end
        end,
        {Parent, PrimeMap},
        Factors),
    process_nums(Rest, Idx + 1, NewParent, NewPrimeMap, Primes).

%% Unique prime factors of N using precomputed primes list
prime_factors(N, Primes) -> prime_factors(N, Primes, []).

prime_factors(1, _, Acc) -> Acc;
prime_factors(N, [P|Ps], Acc) when P * P =< N ->
    case N rem P of
        0 ->
            NewAcc = case lists:member(P, Acc) of true -> Acc; false -> [P|Acc] end,
            prime_factors(divide_out(N, P), [P|Ps], NewAcc);
        _ ->
            prime_factors(N, Ps, Acc)
    end;
prime_factors(N, _, Acc) ->
    case lists:member(N, Acc) of true -> Acc; false -> [N|Acc] end.

divide_out(N, P) ->
    case N rem P of
        0 -> divide_out(N div P, P);
        _ -> N
    end.

%% Union-Find operations with path compression (no rank)
find(Parent, X) ->
    case maps:get(X, Parent) of
        X -> {X, Parent};
        P ->
            {Root, NewParent1} = find(Parent, P),
            NewParent2 = maps:put(X, Root, NewParent1),
            {Root, NewParent2}
    end.

union(Parent, A, B) ->
    {RootA, Parent1} = find(Parent, A),
    {RootB, Parent2} = find(Parent1, B),
    if
        RootA == RootB -> Parent2;
        true -> maps:put(RootA, RootB, Parent2)
    end.

%% Build component maps of original and sorted values per root
build_comp_maps([], [], _, Parent, Comp) -> {Parent, Comp};
build_comp_maps([O|Os], [S|Ss], Idx, Parent, Comp) ->
    {Root, NewParent} = find(Parent, Idx),
    UpdatedComp =
        case maps:get(Root, Comp, undefined) of
            undefined -> maps:put(Root, {[O], [S]}, Comp);
            {OL, SL} -> maps:put(Root, {[O|OL], [S|SL]}, Comp)
        end,
    build_comp_maps(Os, Ss, Idx + 1, NewParent, UpdatedComp).

%% Verify each component has matching multisets
verify_components(CompMap) ->
    lists:all(
        fun({_Root, {OrigL, SortL}}) ->
            lists:sort(OrigL) == lists:sort(SortL)
        end,
        maps:to_list(CompMap)).
```

## Elixir

```elixir
defmodule Solution do
  @spec gcd_sort(nums :: [integer]) :: boolean
  def gcd_sort(nums) do
    n = length(nums)

    # Initialize Union-Find parent map
    parent =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, i)
      end)

    # Build connections via shared prime factors
    {parent, _prime_map} =
      Enum.with_index(nums)
      |> Enum.reduce({parent, %{}}, fn {val, idx}, {par, pmap} ->
        factors = prime_factors(val)

        Enum.reduce(factors, {par, pmap}, fn f, {pacc, pm} ->
          case Map.get(pm, f) do
            nil ->
              {pacc, Map.put(pm, f, idx)}

            other_idx ->
              new_par = union(pacc, idx, other_idx)
              {new_par, pm}
          end
        end)
      end)

    sorted = Enum.sort(nums)

    # Pair original and target values with their indices
    pairs =
      Enum.zip(Enum.with_index(nums), Enum.with_index(sorted))

    # Group values by component root
    {comp_orig, comp_target} =
      Enum.reduce(pairs, {%{}, %{}}, fn
        ({{val, idx}, {sorted_val, _}}, {om, tm}) ->
          root = find_root(parent, idx)

          om = Map.update(om, root, [val], fn lst -> [val | lst] end)
          tm = Map.update(tm, root, [sorted_val], fn lst -> [sorted_val | lst] end)

          {om, tm}
      end)

    # Verify each component can be rearranged to match sorted order
    Enum.all?(Map.keys(comp_orig), fn r ->
      orig_vals = Map.get(comp_orig, r) |> Enum.sort()
      target_vals = Map.get(comp_target, r) |> Enum.sort()
      orig_vals == target_vals
    end)
  end

  # Union-Find find with path compression (returns updated parent map and root)
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

  # Union operation
  defp union(parent, x, y) do
    {parent1, rx} = find(parent, x)
    {parent2, ry} = find(parent1, y)

    if rx != ry do
      Map.put(parent2, rx, ry)
    else
      parent2
    end
  end

  # Find root without modifying the map (used after all unions are done)
  defp find_root(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      x
    else
      find_root(parent, p)
    end
  end

  # Compute distinct prime factors of a number
  defp prime_factors(num), do: prime_factors(num, 2, [])

  defp prime_factors(1, _i, acc), do: Enum.reverse(acc)

  defp prime_factors(n, i, acc) when i * i > n do
    [n | acc] |> Enum.reverse()
  end

  defp prime_factors(n, i, acc) do
    if rem(n, i) == 0 do
      new_n = divide_out(n, i)
      prime_factors(new_n, i + 1, [i | acc])
    else
      next_i = if i == 2, do: 3, else: i + 2
      prime_factors(n, next_i, acc)
    end
  end

  defp divide_out(n, p) do
    if rem(n, p) == 0 do
      divide_out(div(n, p), p)
    else
      n
    end
  end
end
```
