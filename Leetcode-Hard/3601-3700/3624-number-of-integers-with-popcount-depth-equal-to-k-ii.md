# 3624. Number of Integers With Popcount-Depth Equal to K II

## Cpp

```cpp
class Solution {
public:
    struct Fenwick {
        int n;
        std::vector<int> bit;
        Fenwick(int n = 0) { init(n); }
        void init(int n_) {
            n = n_;
            bit.assign(n + 1, 0);
        }
        void add(int idx, int delta) {
            ++idx; // to 1-based
            while (idx <= n) {
                bit[idx] += delta;
                idx += idx & -idx;
            }
        }
        int sumPrefix(int idx) const {
            ++idx;
            int res = 0;
            while (idx > 0) {
                res += bit[idx];
                idx -= idx & -idx;
            }
            return res;
        }
    };
    
    int depthLL(long long x) {
        int d = 0;
        while (x != 1) {
            x = __builtin_popcountll(x);
            ++d;
        }
        return d;
    }
    
    vector<int> popcountDepth(vector<long long>& nums, vector<vector<long long>>& queries) {
        int n = nums.size();
        const int MAXK = 5;
        vector<Fenwick> fenw(MAXK + 1, Fenwick(n));
        for (int d = 0; d <= MAXK; ++d) fenw[d].init(n);
        vector<int> curDepth(n);
        for (int i = 0; i < n; ++i) {
            int d = depthLL(nums[i]);
            curDepth[i] = d;
            fenw[d].add(i, 1);
        }
        vector<int> ans;
        for (auto &q : queries) {
            int type = (int)q[0];
            if (type == 1) {
                int l = (int)q[1];
                int r = (int)q[2];
                int k = (int)q[3];
                int res = fenw[k].sumPrefix(r);
                if (l > 0) res -= fenw[k].sumPrefix(l - 1);
                ans.push_back(res);
            } else { // type == 2
                int idx = (int)q[1];
                long long val = q[2];
                int nd = depthLL(val);
                int od = curDepth[idx];
                if (nd != od) {
                    fenw[od].add(idx, -1);
                    fenw[nd].add(idx, 1);
                    curDepth[idx] = nd;
                }
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
    public int[] popcountDepth(long[] nums, long[][] queries) {
        int n = nums.length;
        Fenwick[] fens = new Fenwick[6];
        for (int d = 0; d < 6; d++) {
            fens[d] = new Fenwick(n);
        }
        int[] depthArr = new int[n];
        for (int i = 0; i < n; i++) {
            int d = computeDepth(nums[i]);
            depthArr[i] = d;
            if (d <= 5) {
                fens[d].add(i, 1);
            }
        }

        List<Integer> resList = new ArrayList<>();
        for (long[] q : queries) {
            int type = (int) q[0];
            if (type == 1) { // query count
                int l = (int) q[1];
                int r = (int) q[2];
                int k = (int) q[3];
                if (k >= 0 && k <= 5) {
                    resList.add(fens[k].rangeSum(l, r));
                } else {
                    resList.add(0);
                }
            } else { // update
                int idx = (int) q[1];
                long val = q[2];
                int oldDepth = depthArr[idx];
                if (oldDepth <= 5) {
                    fens[oldDepth].add(idx, -1);
                }
                int newDepth = computeDepth(val);
                depthArr[idx] = newDepth;
                if (newDepth <= 5) {
                    fens[newDepth].add(idx, 1);
                }
            }
        }

        int[] ans = new int[resList.size()];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = resList.get(i);
        }
        return ans;
    }

    private int computeDepth(long x) {
        int d = 0;
        while (x != 1) {
            x = Long.bitCount(x);
            d++;
        }
        return d;
    }

    class Fenwick {
        int n;
        int[] bit;

        Fenwick(int n) {
            this.n = n;
            bit = new int[n + 1];
        }

        void add(int idx, int delta) { // idx is 0‑based
            for (int i = idx + 1; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }

        int sumPrefix(int idx) { // inclusive, 0‑based
            int res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }

        int rangeSum(int l, int r) {
            if (l > r) return 0;
            return sumPrefix(r) - (l == 0 ? 0 : sumPrefix(l - 1));
        }
    }
}
```

## Python

```python
class Solution(object):
    def popcountDepth(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)

        class BIT:
            __slots__ = ('n', 'bit')
            def __init__(self, size):
                self.n = size
                self.bit = [0] * (size + 1)
            def add(self, idx, delta):
                while idx <= self.n:
                    self.bit[idx] += delta
                    idx += idx & -idx
            def sum(self, idx):
                s = 0
                while idx:
                    s += self.bit[idx]
                    idx -= idx & -idx
                return s

        def depth(x):
            d = 0
            while x != 1:
                x = x.bit_count()
                d += 1
            return d

        # initialize BITs for depths 0..5
        max_k = 5
        bits = [BIT(n) for _ in range(max_k + 1)]
        cur_depth = [0] * n
        for i, val in enumerate(nums):
            d = depth(val)
            cur_depth[i] = d
            if d <= max_k:
                bits[d].add(i + 1, 1)

        ans = []
        for q in queries:
            if q[0] == 1:   # count query [1,l,r,k]
                _, l, r, k = q
                if 0 <= k <= max_k:
                    res = bits[k].sum(r + 1) - bits[k].sum(l)
                else:
                    res = 0
                ans.append(res)
            else:           # update query [2,idx,val]
                _, idx, val = q
                old_d = cur_depth[idx]
                new_d = depth(val)
                if old_d != new_d:
                    if old_d <= max_k:
                        bits[old_d].add(idx + 1, -1)
                    if new_d <= max_k:
                        bits[new_d].add(idx + 1, 1)
                    cur_depth[idx] = new_d
        return ans
```

## Python3

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, idx):
        if idx < 0:
            return 0
        i = idx + 1
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


class Solution:
    def popcountDepth(self, nums, queries):
        n = len(nums)

        def depth(x):
            d = 0
            while x != 1:
                x = x.bit_count()
                d += 1
            return d

        # depths for each position
        dep = [depth(v) for v in nums]

        # fenwick trees for depths 0..5 (inclusive)
        max_k = 5
        fens = [Fenwick(n) for _ in range(max_k + 1)]
        for i, d in enumerate(dep):
            if d <= max_k:
                fens[d].add(i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:          # count query
                _, l, r, k = q
                if 0 <= k <= max_k:
                    ans.append(fens[k].range_sum(l, r))
                else:
                    ans.append(0)
            else:                  # update query
                _, idx, val = q
                old_d = dep[idx]
                new_d = depth(val)
                if old_d != new_d:
                    if old_d <= max_k:
                        fens[old_d].add(idx, -1)
                    if new_d <= max_k:
                        fens[new_d].add(idx, 1)
                    dep[idx] = new_d
        return ans
```

## C

```c
#include <stdlib.h>

static int getDepth(long long x) {
    int d = 0;
    while (x != 1) {
        x = __builtin_popcountll((unsigned long long)x);
        d++;
    }
    return d;
}

static void bitAdd(int *bit, int n, int idx, int delta) {
    for (; idx <= n; idx += idx & -idx)
        bit[idx] += delta;
}

static int bitSum(int *bit, int idx) {
    int res = 0;
    for (; idx > 0; idx -= idx & -idx)
        res += bit[idx];
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* popcountDepth(long long* nums, int numsSize, long long** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = numsSize;
    /* fenwick trees for depths 0..5 */
    int **fenw = (int **)malloc(6 * sizeof(int *));
    for (int d = 0; d <= 5; ++d) {
        fenw[d] = (int *)calloc(n + 2, sizeof(int));
    }

    int *depths = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int dep = getDepth(nums[i]);
        depths[i] = dep;
        if (dep >= 0 && dep <= 5)
            bitAdd(fenw[dep], n, i + 1, 1);
    }

    int *answer = (int *)malloc(queriesSize * sizeof(int));
    int ansCnt = 0;

    for (int qi = 0; qi < queriesSize; ++qi) {
        long long *q = queries[qi];
        int type = (int)q[0];
        if (type == 1) {   // count query
            int l = (int)q[1];
            int r = (int)q[2];
            int k = (int)q[3];
            if (k < 0 || k > 5) {
                answer[ansCnt++] = 0;
                continue;
            }
            int res = bitSum(fenw[k], r + 1) - bitSum(fenw[k], l);
            answer[ansCnt++] = res;
        } else {           // update query
            int idx = (int)q[1];
            long long val = q[2];
            int oldDep = depths[idx];
            if (oldDep >= 0 && oldDep <= 5)
                bitAdd(fenw[oldDep], n, idx + 1, -1);
            nums[idx] = val;
            int newDep = getDepth(val);
            depths[idx] = newDep;
            if (newDep >= 0 && newDep <= 5)
                bitAdd(fenw[newDep], n, idx + 1, 1);
        }
    }

    for (int d = 0; d <= 5; ++d)
        free(fenw[d]);
    free(fenw);
    free(depths);

    *returnSize = ansCnt;
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private class Fenwick {
        private readonly int[] bit;
        private readonly int n;
        public Fenwick(int size) {
            n = size;
            bit = new int[n + 1];
        }
        // idx is zero‑based
        public void Add(int idx, int delta) {
            for (int i = idx + 1; i <= n; i += i & -i)
                bit[i] += delta;
        }
        // sum of [0..idx], idx zero‑based
        private int PrefixSum(int idx) {
            int res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i)
                res += bit[i];
            return res;
        }
        public int RangeSum(int l, int r) {
            if (l > r) return 0;
            int sumR = PrefixSum(r);
            int sumL = l > 0 ? PrefixSum(l - 1) : 0;
            return sumR - sumL;
        }
    }

    private static long PopCount(long v) {
        long cnt = 0;
        while (v != 0) {
            v &= v - 1;
            cnt++;
        }
        return cnt;
    }

    private static int GetDepth(long x) {
        int d = 0;
        while (x != 1) {
            x = PopCount(x);
            d++;
        }
        return d;
    }

    public int[] PopcountDepth(long[] nums, long[][] queries) {
        const int MAX_K = 5;
        int n = nums.Length;
        Fenwick[] fens = new Fenwick[MAX_K + 1];
        for (int k = 0; k <= MAX_K; k++) fens[k] = new Fenwick(n);
        int[] depthArr = new int[n];

        for (int i = 0; i < n; i++) {
            int d = GetDepth(nums[i]);
            depthArr[i] = d;
            if (d <= MAX_K) fens[d].Add(i, 1);
        }

        List<int> answers = new List<int>();
        foreach (var q in queries) {
            int type = (int)q[0];
            if (type == 1) { // query count
                int l = (int)q[1];
                int r = (int)q[2];
                int k = (int)q[3];
                if (k < 0 || k > MAX_K) {
                    answers.Add(0);
                } else {
                    answers.Add(fens[k].RangeSum(l, r));
                }
            } else { // update
                int idx = (int)q[1];
                long val = q[2];
                int oldDepth = depthArr[idx];
                int newDepth = GetDepth(val);
                if (oldDepth != newDepth) {
                    if (oldDepth <= MAX_K) fens[oldDepth].Add(idx, -1);
                    if (newDepth <= MAX_K) fens[newDepth].Add(idx, 1);
                    depthArr[idx] = newDepth;
                }
                nums[idx] = val;
            }
        }

        return answers.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var popcountDepth = function(nums, queries) {
    const n = nums.length;
    const MAX_K = 5;

    class Fenwick {
        constructor(size) {
            this.n = size;
            this.bit = new Int32Array(size + 1);
        }
        add(idx, delta) {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx) {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
        rangeSum(l, r) {
            if (l > r) return 0;
            const left = l ? this.sum(l - 1) : 0;
            return this.sum(r) - left;
        }
    }

    function popcnt(x) {
        let cnt = 0;
        while (x > 0) {
            if ((x % 2) === 1) cnt++;
            x = Math.floor(x / 2);
        }
        return cnt;
    }

    function getDepth(x) {
        let d = 0;
        while (x !== 1) {
            x = popcnt(x);
            d++;
        }
        return d;
    }

    const depthArr = new Array(n);
    const fens = [];
    for (let k = 0; k <= MAX_K; k++) fens.push(new Fenwick(n));

    for (let i = 0; i < n; i++) {
        const d = getDepth(nums[i]);
        depthArr[i] = d;
        if (d <= MAX_K) fens[d].add(i, 1);
    }

    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) { // count query
            const l = q[1], r = q[2], k = q[3];
            if (k > MAX_K) ans.push(0);
            else ans.push(fens[k].rangeSum(l, r));
        } else { // update query
            const idx = q[1], val = q[2];
            const newD = getDepth(val);
            const oldD = depthArr[idx];
            if (newD !== oldD) {
                if (oldD <= MAX_K) fens[oldD].add(idx, -1);
                if (newD <= MAX_K) fens[newD].add(idx, 1);
                depthArr[idx] = newD;
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function popcountDepth(nums: number[], queries: number[][]): number[] {
    const n = nums.length;

    class Fenwick {
        n: number;
        bit: number[];
        constructor(n: number) {
            this.n = n;
            this.bit = new Array(n + 1).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
        range(l: number, r: number): number {
            if (r < l) return 0;
            const right = this.sum(r);
            const left = l ? this.sum(l - 1) : 0;
            return right - left;
        }
    }

    function popcount(x: number): number {
        let cnt = 0;
        while (x > 0) {
            cnt += x & 1;
            x = Math.floor(x / 2);
        }
        return cnt;
    }

    function depth(val: number): number {
        let d = 0;
        while (val !== 1) {
            val = popcount(val);
            d++;
        }
        return d;
    }

    const fenw: Fenwick[] = [];
    for (let i = 0; i <= 5; i++) fenw.push(new Fenwick(n));
    const depths: number[] = new Array(n);

    for (let i = 0; i < n; i++) {
        const d = depth(nums[i]);
        depths[i] = d;
        if (d <= 5) fenw[d].add(i, 1);
    }

    const ans: number[] = [];

    for (const q of queries) {
        if (q[0] === 1) {
            const [, l, r, k] = q;
            ans.push(fenw[k].range(l, r));
        } else {
            const [, idx, val] = q;
            const oldD = depths[idx];
            if (oldD <= 5) fenw[oldD].add(idx, -1);
            const newD = depth(val);
            depths[idx] = newD;
            if (newD <= 5) fenw[newD].add(idx, 1);
        }
    }

    return ans;
}
```

## Php

```php
class Fenwick {
    public int $n;
    public array $tree;

    public function __construct(int $size) {
        $this->n = $size;
        $this->tree = array_fill(0, $size + 1, 0);
    }

    public function add(int $idx, int $delta): void {
        // convert to 1‑based index
        $i = $idx + 1;
        while ($i <= $this->n) {
            $this->tree[$i] += $delta;
            $i += $i & (-$i);
        }
    }

    private function sumPrefix(int $idx): int {
        if ($idx < 0) return 0;
        $i = $idx + 1;
        $res = 0;
        while ($i > 0) {
            $res += $this->tree[$i];
            $i -= $i & (-$i);
        }
        return $res;
    }

    public function rangeSum(int $l, int $r): int {
        if ($l > $r) return 0;
        return $this->sumPrefix($r) - $this->sumPrefix($l - 1);
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function popcountDepth($nums, $queries) {
        $n = count($nums);
        // pre‑compute depth for each element
        $depths = [];
        for ($i = 0; $i < $n; ++$i) {
            $depths[$i] = $this->calcDepth($nums[$i]);
        }

        // six Fenwick trees for depths 0..5
        $bits = [];
        for ($d = 0; $d <= 5; ++$d) {
            $bits[$d] = new Fenwick($n);
        }
        for ($i = 0; $i < $n; ++$i) {
            $d = $depths[$i];
            if ($d <= 5) {
                $bits[$d]->add($i, 1);
            }
        }

        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] == 1) { // range query
                $l = $q[1];
                $r = $q[2];
                $k = $q[3];
                if ($k > 5) {
                    $ans[] = 0;
                } else {
                    $ans[] = $bits[$k]->rangeSum($l, $r);
                }
            } else { // update
                $idx = $q[1];
                $val = $q[2];
                $oldDepth = $depths[$idx];
                $newDepth = $this->calcDepth($val);
                if ($oldDepth != $newDepth) {
                    if ($oldDepth <= 5) $bits[$oldDepth]->add($idx, -1);
                    if ($newDepth <= 5) $bits[$newDepth]->add($idx, 1);
                    $depths[$idx] = $newDepth;
                }
            }
        }

        return $ans;
    }

    private function calcDepth(int $x): int {
        $d = 0;
        while ($x != 1) {
            $x = $this->popcount($x);
            ++$d;
        }
        return $d;
    }

    private function popcount(int $x): int {
        $cnt = 0;
        while ($x > 0) {
            $x &= $x - 1;
            ++$cnt;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Fenwick {
    private var size: Int
    private var tree: [Int]
    init(_ n: Int) {
        self.size = n
        self.tree = Array(repeating: 0, count: n + 2)
    }
    func add(_ index: Int, _ delta: Int) {
        var i = index
        while i <= size {
            tree[i] += delta
            i += i & -i
        }
    }
    func sum(_ index: Int) -> Int {
        var res = 0
        var i = index
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
    func rangeSum(_ l: Int, _ r: Int) -> Int {
        if l > r { return 0 }
        return sum(r) - sum(l - 1)
    }
}

class Solution {
    private func depth(_ x: Int) -> Int {
        var v = x
        var d = 0
        while v != 1 {
            var cnt = 0
            var t = v
            while t > 0 {
                t &= t - 1
                cnt += 1
            }
            v = cnt
            d += 1
        }
        return d
    }

    func popcountDepth(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        let maxK = 5
        var fens = (0...maxK).map { _ in Fenwick(n) }
        var depths = Array(repeating: 0, count: n)

        for i in 0..<n {
            let d = depth(nums[i])
            depths[i] = d
            if d <= maxK {
                fens[d].add(i + 1, 1)
            }
        }

        var result = [Int]()
        var currentNums = nums

        for q in queries {
            if q[0] == 1 {
                let l = q[1]
                let r = q[2]
                let k = q[3]
                if k <= maxK {
                    let ans = fens[k].rangeSum(l + 1, r + 1)
                    result.append(ans)
                } else {
                    result.append(0)
                }
            } else { // type 2
                let idx = q[1]
                let val = q[2]

                let oldDepth = depths[idx]
                if oldDepth <= maxK {
                    fens[oldDepth].add(idx + 1, -1)
                }

                let newDepth = depth(val)
                depths[idx] = newDepth
                if newDepth <= maxK {
                    fens[newDepth].add(idx + 1, 1)
                }
                currentNums[idx] = val
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Fenwick(private val n: Int) {
        private val bit = IntArray(n + 2)
        fun add(idx: Int, delta: Int) {
            var i = idx + 1
            while (i <= n) {
                bit[i] += delta
                i += i and -i
            }
        }

        private fun sum(idx: Int): Int {
            var res = 0
            var i = idx + 1
            while (i > 0) {
                res += bit[i]
                i -= i and -i
            }
            return res
        }

        fun rangeSum(l: Int, r: Int): Int {
            if (l > r) return 0
            val right = sum(r)
            val left = if (l == 0) 0 else sum(l - 1)
            return right - left
        }
    }

    private fun popcountDepthOf(x: Long): Int {
        var v = x
        var d = 0
        while (v != 1L) {
            v = java.lang.Long.bitCount(v).toLong()
            d++
        }
        return d
    }

    fun popcountDepth(nums: LongArray, queries: Array<LongArray>): IntArray {
        val n = nums.size
        val fenw = Array(6) { Fenwick(n) }
        val depthArr = IntArray(n)
        for (i in 0 until n) {
            val d = popcountDepthOf(nums[i])
            depthArr[i] = d
            fenw[d].add(i, 1)
        }

        val answers = ArrayList<Int>()
        for (q in queries) {
            when (q[0].toInt()) {
                1 -> {
                    val l = q[1].toInt()
                    val r = q[2].toInt()
                    val k = q[3].toInt()
                    answers.add(fenw[k].rangeSum(l, r))
                }
                2 -> {
                    val idx = q[1].toInt()
                    val v = q[2]
                    val oldDepth = depthArr[idx]
                    fenw[oldDepth].add(idx, -1)
                    val newDepth = popcountDepthOf(v)
                    depthArr[idx] = newDepth
                    fenw[newDepth].add(idx, 1)
                }
            }
        }

        return answers.toIntArray()
    }
}
```

## Dart

```dart
class Fenwick {
  final List<int> _bit;
  final int n;
  Fenwick(this.n) : _bit = List.filled(n + 1, 0);

  void add(int idx, int delta) {
    // idx is 0‑based
    for (int i = idx + 1; i <= n; i += i & -i) {
      _bit[i] += delta;
    }
  }

  int _sumPrefix(int idx) {
    // idx is 0‑based, inclusive
    int res = 0;
    for (int i = idx + 1; i > 0; i -= i & -i) {
      res += _bit[i];
    }
    return res;
  }

  int rangeSum(int l, int r) {
    if (l > r) return 0;
    int left = l == 0 ? 0 : _sumPrefix(l - 1);
    return _sumPrefix(r) - left;
  }
}

class Solution {
  List<int> popcountDepth(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    // depths for each index
    List<int> depthArr = List.filled(n, 0);
    // fenwick trees for depths 0..5
    const int maxK = 5;
    List<Fenwick> fens = List.generate(maxK + 1, (_) => Fenwick(n));

    for (int i = 0; i < n; ++i) {
      int d = _depth(nums[i]);
      depthArr[i] = d;
      if (d <= maxK) fens[d].add(i, 1);
    }

    List<int> ans = [];
    for (List<int> q in queries) {
      if (q[0] == 1) {
        int l = q[1];
        int r = q[2];
        int k = q[3];
        if (k > maxK) {
          ans.add(0);
        } else {
          ans.add(fens[k].rangeSum(l, r));
        }
      } else { // update
        int idx = q[1];
        int val = q[2];
        int newD = _depth(val);
        int oldD = depthArr[idx];
        if (oldD != newD) {
          if (oldD <= maxK) fens[oldD].add(idx, -1);
          if (newD <= maxK) fens[newD].add(idx, 1);
          depthArr[idx] = newD;
        }
        nums[idx] = val;
      }
    }
    return ans;
  }

  int _depth(int x) {
    int d = 0;
    while (x != 1) {
      x = _popcnt(x);
      d++;
    }
    return d;
  }

  int _popcnt(int x) {
    int cnt = 0;
    while (x > 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

type Fenwick struct {
	n    int
	tree []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{n: n, tree: make([]int, n+1)}
}

func (f *Fenwick) Add(idx int, delta int) {
	for i := idx + 1; i <= f.n; i += i & -i {
		f.tree[i] += delta
	}
}

func (f *Fenwick) Sum(idx int) int {
	if idx < 0 {
		return 0
	}
	res := 0
	for i := idx + 1; i > 0; i -= i & -i {
		res += f.tree[i]
	}
	return res
}

func popcntDepth(x int64) int {
	d := 0
	for x != 1 {
		x = int64(bits.OnesCount64(uint64(x)))
		d++
	}
	return d
}

func popcountDepth(nums []int64, queries [][]int64) []int {
	n := len(nums)
	fenw := make([]*Fenwick, 6)
	for i := 0; i < 6; i++ {
		fenw[i] = NewFenwick(n)
	}
	depths := make([]int, n)
	for i, v := range nums {
		d := popcntDepth(v)
		if d > 5 {
			d = 5 // safety, though per constraints it won't exceed 5
		}
		depths[i] = d
		fenw[d].Add(i, 1)
	}

	var ans []int
	for _, q := range queries {
		if len(q) == 0 {
			continue
		}
		switch q[0] {
		case 1:
			l := int(q[1])
			r := int(q[2])
			k := int(q[3])
			if k < 0 || k > 5 {
				ans = append(ans, 0)
				continue
			}
			res := fenw[k].Sum(r) - fenw[k].Sum(l-1)
			ans = append(ans, res)
		case 2:
			idx := int(q[1])
			val := q[2]
			oldD := depths[idx]
			newD := popcntDepth(val)
			if newD > 5 {
				newD = 5
			}
			if oldD != newD {
				fenw[oldD].Add(idx, -1)
				fenw[newD].Add(idx, 1)
				depths[idx] = newD
			}
			nums[idx] = val
		}
	}
	return ans
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @n = n
    @bit = Array.new(n + 1, 0)
  end

  def add(idx, delta)
    i = idx + 1
    while i <= @n
      @bit[i] += delta
      i += i & -i
    end
  end

  def sum(idx)
    return 0 if idx < 0
    i = idx + 1
    s = 0
    while i > 0
      s += @bit[i]
      i -= i & -i
    end
    s
  end

  def range_sum(l, r)
    sum(r) - sum(l - 1)
  end
end

def popcnt(x)
  cnt = 0
  while x > 0
    x &= x - 1
    cnt += 1
  end
  cnt
end

def compute_depth(x)
  d = 0
  while x != 1
    x = popcnt(x)
    d += 1
  end
  d
end

def popcount_depth(nums, queries)
  n = nums.length
  max_k = 5
  depths = Array.new(n)
  fenw = Array.new(max_k + 1) { Fenwick.new(n) }

  (0...n).each do |i|
    d = compute_depth(nums[i])
    depths[i] = d
    fenw[d].add(i, 1) if d <= max_k
  end

  ans = []
  queries.each do |q|
    if q[0] == 1
      l = q[1]
      r = q[2]
      k = q[3]
      if k > max_k
        ans << 0
      else
        ans << fenw[k].range_sum(l, r)
      end
    else
      idx = q[1]
      val = q[2]
      old_d = depths[idx]
      new_d = compute_depth(val)
      if old_d != new_d
        fenw[old_d].add(idx, -1) if old_d <= max_k
        fenw[new_d].add(idx, 1) if new_d <= max_k
        depths[idx] = new_d
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  class BIT(val n: Int) {
    private val tree = new Array[Int](n + 1)

    def add(idx: Int, delta: Int): Unit = {
      var i = idx + 1
      while (i <= n) {
        tree(i) += delta
        i += i & -i
      }
    }

    private def sumIdx(idx: Int): Int = {
      var res = 0
      var i = idx + 1
      while (i > 0) {
        res += tree(i)
        i -= i & -i
      }
      res
    }

    def rangeSum(l: Int, r: Int): Int = {
      if (l > r) 0
      else sumIdx(r) - (if (l > 0) sumIdx(l - 1) else 0)
    }
  }

  private def popDepth(x: Long): Int = {
    var v = x
    var d = 0
    while (v != 1L) {
      v = java.lang.Long.bitCount(v).toLong
      d += 1
    }
    d
  }

  def popcountDepth(nums: Array[Long], queries: Array[Array[Long]]): Array[Int] = {
    val n = nums.length
    val maxK = 5
    val bits = Array.fill(maxK + 1)(new BIT(n))
    val depthArr = new Array[Int](n)

    // initialize depths and BITs
    var i = 0
    while (i < n) {
      val d = popDepth(nums(i))
      depthArr(i) = d
      if (d <= maxK) bits(d).add(i, 1)
      i += 1
    }

    val answers = new scala.collection.mutable.ArrayBuffer[Int]()

    var qIdx = 0
    while (qIdx < queries.length) {
      val q = queries(qIdx)
      q(0).toInt match {
        case 1 => // range query
          val l = q(1).toInt
          val r = q(2).toInt
          val k = q(3).toInt
          if (k <= maxK) answers += bits(k).rangeSum(l, r)
          else answers += 0
        case 2 => // update
          val idx = q(1).toInt
          val v = q(2)
          val newD = popDepth(v)
          val oldD = depthArr(idx)
          if (newD != oldD) {
            if (oldD <= maxK) bits(oldD).add(idx, -1)
            if (newD <= maxK) bits(newD).add(idx, 1)
            depthArr(idx) = newD
          }
      }
      qIdx += 1
    }

    answers.toArray
  }
}
```

## Rust

```rust
use std::cmp::min;

struct Fenwick {
    n: usize,
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, bit: vec![0; n + 1] }
    }

    fn add(&mut self, idx: usize, delta: i32) {
        let mut i = idx + 1;
        while i <= self.n {
            self.bit[i] += delta;
            let lsb = i & (!i).wrapping_add(1);
            i += lsb;
        }
    }

    fn sum(&self, idx: usize) -> i32 {
        let mut res = 0;
        let mut i = idx + 1;
        while i > 0 {
            res += self.bit[i];
            let lsb = i & (!i).wrapping_add(1);
            i -= lsb;
        }
        res
    }

    fn range_sum(&self, l: usize, r: usize) -> i32 {
        if l == 0 {
            self.sum(r)
        } else {
            self.sum(r) - self.sum(l - 1)
        }
    }
}

fn compute_depth(mut x: i64) -> usize {
    let mut d = 0usize;
    while x != 1 {
        let cnt = (x as u64).count_ones() as i64;
        x = cnt;
        d += 1;
    }
    d
}

impl Solution {
    pub fn popcount_depth(nums: Vec<i64>, queries: Vec<Vec<i64>>) -> Vec<i32> {
        const MAX_K: usize = 5;
        let n = nums.len();
        let mut depths: Vec<usize> = vec![0; n];
        let mut fens: Vec<Fenwick> = (0..=MAX_K).map(|_| Fenwick::new(n)).collect();

        for (i, &val) in nums.iter().enumerate() {
            let d = compute_depth(val);
            depths[i] = d;
            if d <= MAX_K {
                fens[d].add(i, 1);
            }
        }

        let mut ans: Vec<i32> = Vec::new();

        for q in queries.iter() {
            let typ = q[0];
            if typ == 1 {
                let l = q[1] as usize;
                let r = q[2] as usize;
                let k = q[3] as usize;
                if k <= MAX_K {
                    ans.push(fens[k].range_sum(l, r));
                } else {
                    ans.push(0);
                }
            } else {
                // typ == 2
                let idx = q[1] as usize;
                let val = q[2];
                let old_d = depths[idx];
                if old_d <= MAX_K {
                    fens[old_d].add(idx, -1);
                }
                let new_d = compute_depth(val);
                depths[idx] = new_d;
                if new_d <= MAX_K {
                    fens[new_d].add(idx, 1);
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/bitwise)
(require racket/match)

(define/contract (popcount-depth nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length nums))
         (bits (make-vector 6))
         (depths (make-vector n)))
    ;; initialize BIT vectors
    (for ([d (in-range 6)])
      (vector-set! bits d (make-vector (+ n 1) 0)))
    ;; BIT update: add delta at position idx (0‑based)
    (define (bit-update! d idx delta)
      (let ((bit (vector-ref bits d))
            (i (+ idx 1))) ; convert to 1‑based
        (let loop ((i i))
          (when (<= i n)
            (vector-set! bit i (+ (vector-ref bit i) delta))
            (loop (+ i (bitwise-and i (- i))))))))
    ;; BIT prefix sum up to idx (0‑based, inclusive)
    (define (bit-sum d idx)
      (let ((bit (vector-ref bits d))
            (i (+ idx 1)))
        (let loop ((i i) (s 0))
          (if (= i 0)
              s
              (loop (bitwise-and i (sub1 i)) (+ s (vector-ref bit i)))))))
    ;; compute popcount‑depth of a number
    (define (compute-depth x)
      (let loop ((v x) (d 0))
        (if (= v 1)
            d
            (loop (bitwise-bit-count v) (+ d 1)))))
    ;; initialize depths and BITs
    (for ([i (in-range n)])
      (let* ((val (list-ref nums i))
             (dep (compute-depth val)))
        (vector-set! depths i dep)
        (when (<= dep 5)
          (bit-update! dep i 1))))
    ;; process queries
    (let loop ((qs queries) (ans '()))
      (if (null? qs)
          (reverse ans)
          (match (car qs)
            [(list 1 l r k)
             (define cnt (- (bit-sum k r)
                            (if (= l 0) 0 (bit-sum k (sub1 l)))))
             (loop (cdr qs) (cons cnt ans))]
            [(list 2 idx val)
             (let* ((old (vector-ref depths idx))
                    (new (compute-depth val)))
               (when (<= old 5) (bit-update! old idx -1))
               (when (<= new 5) (bit-update! new idx 1))
               (vector-set! depths idx new)
               (loop (cdr qs) ans))]
            [_ (loop (cdr qs) ans)]))))))
```

## Erlang

```erlang
-module(solution).
-export([popcount_depth/2]).

%% Public API
-spec popcount_depth(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
popcount_depth(Nums, Queries) ->
    N = length(Nums),
    %% Compute initial depths
    DepthsList = [depth_of(X) || X <- Nums],
    DepthArr0 = array:from_list(DepthsList),  % zero‑based indexing
    %% Initialize six empty BIT maps
    EmptyMaps = {#{}, #{}, #{}, #{}, #{}, #{}},
    Maps0 = init_bits(EmptyMaps, DepthsList, N),
    %% Process queries
    {ResultRev, _FinalMaps, _FinalDepthArr} =
        lists:foldl(fun process_query/2,
                    {[], Maps0, DepthArr0},
                    Queries),
    lists:reverse(ResultRev).

%% Initialize BITs with the initial depths
-spec init_bits(tuple(), [integer()], integer()) -> tuple().
init_bits(Maps, Depths, N) ->
    lists:foldl(
      fun({Depth, Idx}, AccMaps) ->
              update_bit(AccMaps, Depth, Idx + 1, 1, N)
      end,
      Maps,
      lists:zip(Depths, lists:seq(0, length(Depths)-1))
    ).

%% Process a single query
-spec process_query([integer()], {list(), tuple(), array:array()}) ->
          {list(), tuple(), array:array()}.
process_query([1, L, R, K], {AnsAcc, Maps, DepthArr}) ->
    % BIT is 1‑based; indices in queries are 0‑based
    SumR = bit_query(get_map(Maps, K), R + 1),
    SumL = bit_query(get_map(Maps, K), L),
    Count = SumR - SumL,
    {[Count | AnsAcc], Maps, DepthArr};
process_query([2, Idx, Val], {AnsAcc, Maps, DepthArr}) ->
    OldDepth = array:get(Idx, DepthArr),
    NewDepth = depth_of(Val),
    if
        OldDepth =:= NewDepth ->
            {AnsAcc, Maps, DepthArr};
        true ->
            N = array:size(DepthArr) - 1,
            Maps1 = update_bit(Maps, OldDepth, Idx + 1, -1, N),
            Maps2 = update_bit(Maps1, NewDepth, Idx + 1, 1, N),
            DepthArr2 = array:set(Idx, NewDepth, DepthArr),
            {AnsAcc, Maps2, DepthArr2}
    end.

%% BIT point update (add Delta at position Index)
-spec update_bit(tuple(), integer(), integer(), integer(), integer()) -> tuple().
update_bit(Maps, Depth, Index, Delta, N) ->
    OldMap = get_map(Maps, Depth),
    NewMap = bit_update(OldMap, Index, Delta, N),
    set_map(Maps, Depth, NewMap).

%% BIT internal update on a map
-spec bit_update(map(), integer(), integer(), integer()) -> map().
bit_update(Map, Idx, Delta, N) when Idx =< N ->
    Cur = maps:get(Idx, Map, 0),
    Updated = maps:put(Idx, Cur + Delta, Map),
    Next = Idx + (Idx band -Idx),
    bit_update(Updated, Next, Delta, N);
bit_update(Map, _Idx, _Delta, _N) ->
    Map.

%% BIT prefix sum query up to Index
-spec bit_query(map(), integer()) -> integer().
bit_query(_Map, 0) -> 0;
bit_query(Map, Idx) when Idx > 0 ->
    Cur = maps:get(Idx, Map, 0),
    Cur + bit_query(Map, Idx - (Idx band -Idx)).

%% Helpers to get/set map for a specific depth in the tuple
-spec get_map(tuple(), integer()) -> map().
get_map(Maps, Depth) ->
    element(Depth + 1, Maps).

-spec set_map(tuple(), integer(), map()) -> tuple().
set_map(Maps, Depth, NewMap) ->
    setelement(Depth + 1, Maps, NewMap).

%% Compute popcount‑depth of a number
-spec depth_of(integer()) -> integer().
depth_of(1) -> 0;
depth_of(X) when X > 1 ->
    depth_iter(popcnt(X), 1).

-spec depth_iter(integer(), integer()) -> integer().
depth_iter(1, D) -> D;
depth_iter(V, D) ->
    depth_iter(popcnt(V), D + 1).

%% Popcount using Kernighan's algorithm
-spec popcnt(integer()) -> integer().
popcnt(N) -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) -> popcnt(N band (N - 1), Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  defmodule Fenwick do
    @type t :: %{n: non_neg_integer, data: map()}
    @spec new(non_neg_integer) :: t()
    def new(n), do: %{n: n, data: %{}}

    @spec add(t(), pos_integer, integer) :: t()
    def add(fenw, idx, delta), do: do_add(fenw, idx, delta)

    defp do_add(%{n: n, data: d}=fenw, idx, delta) when idx <= n do
      new_data = Map.update(d, idx, delta, &(&1 + delta))
      new_data =
        case Map.get(new_data, idx) do
          0 -> Map.delete(new_data, idx)
          _ -> new_data
        end

      do_add(%{fenw | data: new_data}, idx + (idx &&& -idx), delta)
    end

    defp do_add(fenw, _idx, _delta), do: fenw

    @spec sum(t(), non_neg_integer) :: integer
    def sum(fenw, idx), do: do_sum(0, idx, fenw.data)

    defp do_sum(acc, i, data) when i > 0 do
      val = Map.get(data, i, 0)
      do_sum(acc + val, i - (i &&& -i), data)
    end

    defp do_sum(acc, _i, _data), do: acc
  end

  @spec popcount_depth(nums :: [integer], queries :: [[integer]]) :: [integer]
  def popcount_depth(nums, queries) do
    n = length(nums)

    depths =
      Enum.reduce(Enum.with_index(nums), :array.new(n, default: 0), fn {num, i}, arr ->
        d = depth(num)
        :array.set(i, d, arr)
      end)

    fenwicks = for _ <- 0..5, do: Fenwick.new(n)

    fenwicks =
      Enum.reduce(0..(n - 1), fenwicks, fn i, fws ->
        d = :array.get(i, depths)
        if d <= 5 do
          update_fenwick(fws, d, i + 1, 1)
        else
          fws
        end
      end)

    {_, _, rev_ans} =
      Enum.reduce(queries, {fenwicks, depths, []}, fn query,
                                                      {fws, dep_arr, acc} ->
        case query do
          [1, l, r, k] ->
            ans =
              if k > 5 do
                0
              else
                fen = Enum.at(fws, k)
                Fenwick.sum(fen, r + 1) - Fenwick.sum(fen, l)
              end

            {fws, dep_arr, [ans | acc]}

          [2, idx, val] ->
            old_d = :array.get(idx, dep_arr)
            new_d = depth(val)

            fws1 =
              if old_d <= 5 do
                update_fenwick(fws, old_d, idx + 1, -1)
              else
                fws
              end

            fws2 =
              if new_d <= 5 do
                update_fenwick(fws1, new_d, idx + 1, 1)
              else
                fws1
              end

            dep_arr2 = :array.set(idx, new_d, dep_arr)
            {fws2, dep_arr2, acc}
        end
      end)

    Enum.reverse(rev_ans)
  end

  defp update_fenwick(fws, d, idx, delta) do
    fen = Enum.at(fws, d)
    new_fen = Fenwick.add(fen, idx, delta)
    List.replace_at(fws, d, new_fen)
  end

  defp popcnt(0), do: 0

  defp popcnt(x) do
    popcnt_loop(x, 0)
  end

  defp popcnt_loop(0, acc), do: acc

  defp popcnt_loop(x, acc) do
    popcnt_loop(Bitwise.band(x, x - 1), acc + 1)
  end

  defp depth(x) do
    depth_loop(x, 0)
  end

  defp depth_loop(1, d), do: d

  defp depth_loop(x, d) do
    depth_loop(popcnt(x), d + 1)
  end
end
```
