# 3187. Peaks in Array

## Cpp

```cpp
class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n): n(n), bit(n+1,0) {}
        void add(int idx, int val){
            for(++idx; idx<=n; idx+=idx&-idx) bit[idx] += val;
        }
        int sumPrefix(int idx){ // sum [0, idx]
            int res=0;
            for(++idx; idx>0; idx-=idx&-idx) res += bit[idx];
            return res;
        }
        int rangeSum(int l,int r){
            if(l>r) return 0;
            return sumPrefix(r) - (l?sumPrefix(l-1):0);
        }
    };
    
    vector<int> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> p(n,0); // peak indicator
        BIT bit(n);
        auto isPeak = [&](int i)->int{
            if(i<=0 || i>=n-1) return 0;
            return (nums[i] > nums[i-1] && nums[i] > nums[i+1]) ? 1 : 0;
        };
        for(int i=1;i<=n-2;++i){
            p[i]=isPeak(i);
            if(p[i]) bit.add(i, p[i]);
        }
        vector<int> ans;
        for(const auto& q: queries){
            int type = q[0];
            if(type==2){
                int idx = q[1];
                int val = q[2];
                if(nums[idx]==val) continue; // no change
                nums[idx]=val;
                for(int i=idx-1;i<=idx+1;++i){
                    if(i>=1 && i<=n-2){
                        int newPeak = isPeak(i);
                        int delta = newPeak - p[i];
                        if(delta){
                            bit.add(i, delta);
                            p[i]=newPeak;
                        }
                    }
                }
            }else{ // type 1
                int l = q[1];
                int r = q[2];
                int left = l+1;
                int right = r-1;
                if(left>right){
                    ans.push_back(0);
                }else{
                    ans.push_back(bit.rangeSum(left, right));
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class BIT {
        int n;
        int[] tree;
        BIT(int n) {
            this.n = n;
            tree = new int[n + 1];
        }
        void add(int idx, int delta) {
            for (int i = idx + 1; i <= n; i += i & -i) {
                tree[i] += delta;
            }
        }
        int sum(int idx) {
            int res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += tree[i];
            }
            return res;
        }
    }

    public List<Integer> countOfPeaks(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] peak = new int[n]; // 1 if position i is a peak, else 0
        BIT bit = new BIT(n);
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                peak[i] = 1;
                bit.add(i, 1);
            }
        }

        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int type = q[0];
            if (type == 1) { // query count
                int l = q[1];
                int r = q[2];
                if (l + 1 > r - 1) {
                    ans.add(0);
                } else {
                    int sum = bit.sum(r - 1) - bit.sum(l);
                    ans.add(sum);
                }
            } else { // type == 2, update
                int idx = q[1];
                int val = q[2];
                if (nums[idx] == val) continue;
                nums[idx] = val;
                for (int i = idx - 1; i <= idx + 1; i++) {
                    if (i <= 0 || i >= n - 1) continue;
                    int old = peak[i];
                    int now = (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ? 1 : 0;
                    if (old != now) {
                        peak[i] = now;
                        bit.add(i, now - old);
                    }
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countOfPeaks(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # Binary Indexed Tree
        class BIT:
            __slots__ = ('n', 'tree')
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)
            def add(self, idx, delta):
                i = idx + 1
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & -i
            def sum(self, idx):
                # prefix sum [0..idx]
                if idx < 0:
                    return 0
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

        bit = BIT(n)
        p = [0] * n  # peak indicator

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                p[i] = 1
                bit.add(i, 1)

        def recompute(j):
            """recompute peak status at position j (must be 1..n-2)"""
            new_val = 1 if (nums[j] > nums[j - 1] and nums[j] > nums[j + 1]) else 0
            if new_val != p[j]:
                bit.add(j, new_val - p[j])
                p[j] = new_val

        ans = []
        for typ, a, b in queries:
            if typ == 2:  # update
                idx, val = a, b
                if nums[idx] == val:
                    continue
                nums[idx] = val
                for j in (idx - 1, idx, idx + 1):
                    if 1 <= j <= n - 2:
                        recompute(j)
            else:  # typ == 1, range query
                l, r = a, b
                if l + 1 > r - 1:
                    ans.append(0)
                else:
                    total = bit.sum(r - 1) - bit.sum(l)
                    ans.append(total)
        return ans
```

## Python3

```python
from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        i = idx + 1  # convert to 1‑based
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, idx: int) -> int:
        """prefix sum [0..idx], inclusive; idx can be -1 => 0"""
        if idx < 0:
            return 0
        i = idx + 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # helper to check peak at position i
        def is_peak(i: int) -> bool:
            return 0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        peaks = [0] * n
        ft = FenwickTree(n)
        for i in range(1, n - 1):
            if is_peak(i):
                peaks[i] = 1
                ft.add(i, 1)

        ans: List[int] = []
        for q in queries:
            typ = q[0]
            if typ == 1:
                l, r = q[1], q[2]
                if l + 1 <= r - 1:
                    cnt = ft.sum(r - 1) - ft.sum(l)
                else:
                    cnt = 0
                ans.append(cnt)
            else:  # typ == 2
                idx, val = q[1], q[2]
                if nums[idx] == val:
                    continue
                nums[idx] = val
                for i in (idx - 1, idx, idx + 1):
                    if 0 < i < n - 1:
                        new_val = 1 if is_peak(i) else 0
                        if new_val != peaks[i]:
                            ft.add(i, new_val - peaks[i])
                            peaks[i] = new_val
        return ans
```

## C

```c
#include <stdlib.h>

static void bitAdd(int *bit, int n, int idx, int delta) {
    for (idx++; idx <= n; idx += idx & -idx)
        bit[idx] += delta;
}

static int bitSum(int *bit, int n, int idx) {
    int res = 0;
    for (idx++; idx > 0; idx -= idx & -idx)
        res += bit[idx];
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countOfPeaks(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = numsSize;
    int *p = (int*)calloc(n, sizeof(int));          // peak flags
    int *bit = (int*)calloc(n + 1, sizeof(int));    // BIT (1-indexed)

    for (int i = 1; i <= n - 2; ++i) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
            p[i] = 1;
            bitAdd(bit, n, i, 1);
        }
    }

    int *answers = (int*)malloc(queriesSize * sizeof(int));
    int ansCnt = 0;

    for (int q = 0; q < queriesSize; ++q) {
        int type = queries[q][0];
        if (type == 1) { // count peaks in [l, r]
            int l = queries[q][1];
            int r = queries[q][2];
            if (l + 1 > r - 1) {
                answers[ansCnt++] = 0;
            } else {
                int sumR = bitSum(bit, n, r - 1);
                int sumL = bitSum(bit, n, l);
                answers[ansCnt++] = sumR - sumL;
            }
        } else { // type == 2, update nums[idx] = val
            int idx = queries[q][1];
            int val = queries[q][2];
            if (nums[idx] == val) continue; // no change, skip recomputation
            nums[idx] = val;
            for (int j = idx - 1; j <= idx + 1; ++j) {
                if (j >= 1 && j <= n - 2) {
                    int newPeak = (nums[j] > nums[j - 1] && nums[j] > nums[j + 1]) ? 1 : 0;
                    if (newPeak != p[j]) {
                        int diff = newPeak - p[j];
                        p[j] = newPeak;
                        bitAdd(bit, n, j, diff);
                    }
                }
            }
        }
    }

    *returnSize = ansCnt;
    free(p);
    free(bit);
    return answers;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> CountOfPeaks(int[] nums, int[][] queries) {
        int n = nums.Length;
        int[] p = new int[n];
        Fenwick fenwick = new Fenwick(n);
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                p[i] = 1;
                fenwick.Add(i, 1);
            }
        }

        List<int> answer = new List<int>();

        foreach (var q in queries) {
            int type = q[0];
            if (type == 2) { // update
                int idx = q[1];
                int val = q[2];
                if (nums[idx] == val) continue;
                nums[idx] = val;
                for (int i = idx - 1; i <= idx + 1; i++) {
                    if (i > 0 && i < n - 1) {
                        int newPeak = (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ? 1 : 0;
                        int diff = newPeak - p[i];
                        if (diff != 0) {
                            p[i] = newPeak;
                            fenwick.Add(i, diff);
                        }
                    }
                }
            } else { // query count
                int l = q[1];
                int r = q[2];
                if (r - l <= 1) {
                    answer.Add(0);
                } else {
                    int sum = fenwick.Sum(r - 1) - fenwick.Sum(l);
                    answer.Add(sum);
                }
            }
        }

        return answer;
    }

    private class Fenwick {
        private readonly int[] tree;
        private readonly int n;

        public Fenwick(int size) {
            n = size;
            tree = new int[n + 1];
        }

        // idx is 0‑based
        public void Add(int idx, int delta) {
            for (int i = idx + 1; i <= n; i += i & -i) {
                tree[i] += delta;
            }
        }

        // sum of [0..idx], idx is 0‑based
        public int Sum(int idx) {
            int res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += tree[i];
            }
            return res;
        }
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
var countOfPeaks = function(nums, queries) {
    const n = nums.length;
    // Fenwick Tree implementation (1-indexed internally)
    class Fenwick {
        constructor(size) {
            this.n = size;
            this.bit = new Array(size + 1).fill(0);
        }
        add(idx, delta) { // idx: 0-based
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx) { // prefix sum [0..idx], idx 0-based
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
        rangeSum(l, r) { // inclusive, 0-based
            if (l > r) return 0;
            return this.sum(r) - (l > 0 ? this.sum(l - 1) : 0);
        }
    }

    const fenwick = new Fenwick(n);
    const peak = new Array(n).fill(0);

    // initialize peaks
    for (let i = 1; i <= n - 2; ++i) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
            peak[i] = 1;
            fenwick.add(i, 1);
        }
    }

    const ans = [];

    for (const q of queries) {
        const type = q[0];
        if (type === 2) { // update
            const idx = q[1];
            const val = q[2];
            if (nums[idx] === val) continue; // no change, skip recomputation
            nums[idx] = val;
            for (let i = idx - 1; i <= idx + 1; ++i) {
                if (i >= 1 && i <= n - 2) {
                    const newPeak = (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ? 1 : 0;
                    if (newPeak !== peak[i]) {
                        fenwick.add(i, newPeak - peak[i]);
                        peak[i] = newPeak;
                    }
                }
            }
        } else { // type === 1, query range
            const l = q[1];
            const r = q[2];
            const left = l + 1;
            const right = r - 1;
            ans.push(fenwick.rangeSum(left, right));
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countOfPeaks(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    const p = new Array(n).fill(0);
    class Fenwick {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 1).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
        rangeSum(l: number, r: number): number {
            if (l > r) return 0;
            const right = this.sum(r);
            const left = l > 0 ? this.sum(l - 1) : 0;
            return right - left;
        }
    }
    const bit = new Fenwick(n);
    for (let i = 1; i <= n - 2; i++) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
            p[i] = 1;
            bit.add(i, 1);
        }
    }
    const ans: number[] = [];
    for (const q of queries) {
        const type = q[0];
        if (type === 1) {
            const l = q[1], r = q[2];
            const left = l + 1, right = r - 1;
            if (left > right) ans.push(0);
            else ans.push(bit.rangeSum(left, right));
        } else {
            const idx = q[1], val = q[2];
            if (nums[idx] === val) continue;
            nums[idx] = val;
            for (let j = idx - 1; j <= idx + 1; j++) {
                if (j >= 1 && j <= n - 2) {
                    const newPeak = (nums[j] > nums[j - 1] && nums[j] > nums[j + 1]) ? 1 : 0;
                    if (newPeak !== p[j]) {
                        bit.add(j, newPeak - p[j]);
                        p[j] = newPeak;
                    }
                }
            }
        }
    }
    return ans;
}
```

## Php

```php
class BIT {
    private int $n;
    private array $tree;

    public function __construct(int $size) {
        $this->n = $size;
        $this->tree = array_fill(0, $size + 2, 0);
    }

    public function add(int $idx, int $delta): void {
        for ($i = $idx; $i <= $this->n; $i += $i & (-$i)) {
            $this->tree[$i] += $delta;
        }
    }

    public function sum(int $idx): int {
        $res = 0;
        for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
            $res += $this->tree[$i];
        }
        return $res;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countOfPeaks($nums, $queries) {
        $n = count($nums);
        $bit = new BIT($n);
        $p = array_fill(0, $n, 0);

        for ($i = 1; $i < $n - 1; ++$i) {
            if ($nums[$i] > $nums[$i - 1] && $nums[$i] > $nums[$i + 1]) {
                $p[$i] = 1;
                $bit->add($i + 1, 1); // BIT is 1-indexed
            }
        }

        $answers = [];

        foreach ($queries as $q) {
            $type = $q[0];
            if ($type == 1) { // count peaks in [l, r]
                $l = $q[1];
                $r = $q[2];
                if ($r - $l < 2) {
                    $answers[] = 0;
                    continue;
                }
                // sum over indices (l+1 .. r-1)
                $sumR = $bit->sum($r);       // up to index r-1
                $sumL = $bit->sum($l + 1);   // up to index l
                $answers[] = $sumR - $sumL;
            } else { // update nums[idx] = val
                $idx = $q[1];
                $val = $q[2];
                if ($nums[$idx] === $val) {
                    continue;
                }
                $nums[$idx] = $val;
                for ($j = $idx - 1; $j <= $idx + 1; ++$j) {
                    if ($j >= 1 && $j <= $n - 2) {
                        $newPeak = ($nums[$j] > $nums[$j - 1] && $nums[$j] > $nums[$j + 1]) ? 1 : 0;
                        if ($newPeak !== $p[$j]) {
                            $delta = $newPeak - $p[$j];
                            $p[$j] = $newPeak;
                            $bit->add($j + 1, $delta);
                        }
                    }
                }
            }
        }

        return $answers;
    }
}
```

## Swift

```swift
class Fenwick {
    private var n: Int
    private var bit: [Int]
    init(_ size: Int) {
        self.n = size
        self.bit = Array(repeating: 0, count: size + 1)
    }
    func add(_ index: Int, _ delta: Int) {
        var i = index + 1
        while i <= n {
            bit[i] += delta
            i += i & -i
        }
    }
    private func prefixSum(_ index: Int) -> Int {
        if index < 0 { return 0 }
        var res = 0
        var i = index + 1
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }
    func rangeSum(_ left: Int, _ right: Int) -> Int {
        if left > right { return 0 }
        return prefixSum(right) - prefixSum(left - 1)
    }
}

class Solution {
    func countOfPeaks(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var arr = nums
        let n = arr.count
        if n < 3 { return [] } // no peaks possible, but queries may ask; handle later
        
        var peak = Array(repeating: 0, count: n)
        let fenwick = Fenwick(n)
        
        for i in 1..<(n - 1) {
            if arr[i] > arr[i - 1] && arr[i] > arr[i + 1] {
                peak[i] = 1
                fenwick.add(i, 1)
            }
        }
        
        var answer: [Int] = []
        
        for q in queries {
            let type = q[0]
            if type == 1 {
                let l = q[1]
                let r = q[2]
                let left = l + 1
                let right = r - 1
                if left <= right {
                    answer.append(fenwick.rangeSum(left, right))
                } else {
                    answer.append(0)
                }
            } else { // type == 2, update
                let idx = q[1]
                let val = q[2]
                if arr[idx] == val { continue }
                arr[idx] = val
                let start = max(1, idx - 1)
                let end = min(n - 2, idx + 1)
                if start <= end {
                    for i in start...end {
                        let newPeak = (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) ? 1 : 0
                        if newPeak != peak[i] {
                            fenwick.add(i, newPeak - peak[i])
                            peak[i] = newPeak
                        }
                    }
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Fenwick(private val n: Int) {
        private val bit = IntArray(n + 1)
        fun add(idx: Int, delta: Int) {
            var i = idx + 1
            while (i <= n) {
                bit[i] += delta
                i += i and -i
            }
        }
        fun sum(idx: Int): Int {
            var res = 0
            var i = idx + 1
            while (i > 0) {
                res += bit[i]
                i -= i and -i
            }
            return res
        }
    }

    fun countOfPeaks(nums: IntArray, queries: Array<IntArray>): List<Int> {
        val n = nums.size
        val peaks = IntArray(n)
        for (i in 1 until n - 1) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks[i] = 1
        }
        val fenwick = Fenwick(n)
        for (i in 0 until n) {
            if (peaks[i] != 0) fenwick.add(i, peaks[i])
        }

        val ans = mutableListOf<Int>()
        for (q in queries) {
            when (q[0]) {
                2 -> { // update
                    val idx = q[1]
                    val value = q[2]
                    if (nums[idx] == value) continue
                    nums[idx] = value
                    for (i in idx - 1..idx + 1) {
                        if (i >= 1 && i <= n - 2) {
                            val newPeak = if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) 1 else 0
                            val delta = newPeak - peaks[i]
                            if (delta != 0) {
                                fenwick.add(i, delta)
                                peaks[i] = newPeak
                            }
                        }
                    }
                }
                1 -> { // query count of peaks in [l, r]
                    val l = q[1]
                    val r = q[2]
                    if (l + 1 > r - 1) {
                        ans.add(0)
                    } else {
                        val count = fenwick.sum(r - 1) - fenwick.sum(l)
                        ans.add(count)
                    }
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countOfPeaks(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    // peak indicator array
    List<int> p = List.filled(n, 0);
    for (int i = 1; i <= n - 2; ++i) {
      if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
        p[i] = 1;
      }
    }

    // Fenwick Tree for prefix sums
    final bit = _Fenwick(n);
    for (int i = 1; i <= n - 2; ++i) {
      if (p[i] == 1) bit.add(i, 1);
    }

    List<int> ans = [];
    for (var q in queries) {
      int type = q[0];
      if (type == 1) {
        int l = q[1];
        int r = q[2];
        int left = l + 1;
        int right = r - 1;
        if (left > right) {
          ans.add(0);
        } else {
          ans.add(bit.rangeSum(left, right));
        }
      } else { // type == 2
        int idx = q[1];
        int val = q[2];
        nums[idx] = val;
        for (int j = idx - 1; j <= idx + 1; ++j) {
          if (j >= 1 && j <= n - 2) {
            int newPeak = (nums[j] > nums[j - 1] && nums[j] > nums[j + 1]) ? 1 : 0;
            if (newPeak != p[j]) {
              int delta = newPeak - p[j];
              p[j] = newPeak;
              bit.add(j, delta);
            }
          }
        }
      }
    }
    return ans;
  }
}

class _Fenwick {
  final List<int> _tree;
  final int _n;

  _Fenwick(this._n) : _tree = List.filled(_n + 1, 0);

  void add(int index, int delta) {
    // internal BIT is 1‑based
    for (int i = index + 1; i <= _n; i += i & -i) {
      _tree[i] += delta;
    }
  }

  int _prefixSum(int index) {
    if (index < 0) return 0;
    int res = 0;
    for (int i = index + 1; i > 0; i -= i & -i) {
      res += _tree[i];
    }
    return res;
  }

  int rangeSum(int left, int right) {
    if (left > right) return 0;
    return _prefixSum(right) - _prefixSum(left - 1);
  }
}
```

## Golang

```go
type fenwick struct {
	tree []int
}

func newFenwick(n int) *fenwick {
	return &fenwick{make([]int, n+1)}
}

func (f *fenwick) add(idx, delta int) {
	for i := idx + 1; i < len(f.tree); i += i & -i {
		f.tree[i] += delta
	}
}

func (f *fenwick) sum(idx int) int {
	res := 0
	for i := idx + 1; i > 0; i -= i & -i {
		res += f.tree[i]
	}
	return res
}

func (f *fenwick) rangeSum(l, r int) int {
	if l > r {
		return 0
	}
	if l == 0 {
		return f.sum(r)
	}
	return f.sum(r) - f.sum(l-1)
}

func countOfPeaks(nums []int, queries [][]int) []int {
	n := len(nums)
	p := make([]int, n)

	bit := newFenwick(n)

	// initialize peaks
	for i := 1; i <= n-2; i++ {
		if nums[i] > nums[i-1] && nums[i] > nums[i+1] {
			p[i] = 1
			bit.add(i, 1)
		}
	}

	ans := make([]int, 0, len(queries))

	for _, q := range queries {
		if q[0] == 1 { // query count
			l, r := q[1], q[2]
			if r-l <= 1 {
				ans = append(ans, 0)
			} else {
				cnt := bit.rangeSum(l+1, r-1)
				ans = append(ans, cnt)
			}
		} else { // update
			idx, val := q[1], q[2]
			if nums[idx] == val {
				continue
			}
			nums[idx] = val
			for _, i := range []int{idx - 1, idx, idx + 1} {
				if i >= 1 && i <= n-2 {
					newPeak := 0
					if nums[i] > nums[i-1] && nums[i] > nums[i+1] {
						newPeak = 1
					}
					if newPeak != p[i] {
						delta := newPeak - p[i]
						p[i] = newPeak
						bit.add(i, delta)
					}
				}
			}
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
    res = 0
    i = idx + 1
    while i > 0
      res += @bit[i]
      i -= i & -i
    end
    res
  end

  def range_sum(l, r)
    return 0 if l > r
    sum(r) - sum(l - 1)
  end
end

def count_of_peaks(nums, queries)
  n = nums.length
  bit = Fenwick.new(n)
  p = Array.new(n, 0)

  (1...n - 1).each do |i|
    if nums[i] > nums[i - 1] && nums[i] > nums[i + 1]
      p[i] = 1
      bit.add(i, 1)
    end
  end

  ans = []
  queries.each do |q|
    type = q[0]
    if type == 1
      l = q[1]
      r = q[2]
      if l + 1 <= r - 1
        ans << bit.range_sum(l + 1, r - 1)
      else
        ans << 0
      end
    else # type == 2
      idx = q[1]
      val = q[2]
      nums[idx] = val
      (idx - 1..idx + 1).each do |j|
        next if j < 1 || j > n - 2
        new_peak = (nums[j] > nums[j - 1] && nums[j] > nums[j + 1]) ? 1 : 0
        delta = new_peak - p[j]
        if delta != 0
          bit.add(j, delta)
          p[j] = new_peak
        end
      end
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countOfPeaks(nums: Array[Int], queries: Array[Array[Int]]): List[Int] = {
        val n = nums.length
        val p = new Array[Int](n)

        class BIT(size: Int) {
            private val tree = new Array[Int](size + 2)
            def add(idx0: Int, delta: Int): Unit = {
                var idx = idx0 + 1
                while (idx < tree.length) {
                    tree(idx) += delta
                    idx += idx & -idx
                }
            }
            private def sumIdx(idx0: Int): Int = {
                var idx = idx0 + 1
                var res = 0
                while (idx > 0) {
                    res += tree(idx)
                    idx -= idx & -idx
                }
                res
            }
            def rangeSum(l: Int, r: Int): Int = {
                if (l > r) 0 else sumIdx(r) - (if (l > 0) sumIdx(l - 1) else 0)
            }
        }

        val bit = new BIT(n)

        // initialize peaks
        for (i <- 1 until n - 1) {
            if (nums(i) > nums(i - 1) && nums(i) > nums(i + 1)) {
                p(i) = 1
                bit.add(i, 1)
            }
        }

        val ans = scala.collection.mutable.ArrayBuffer[Int]()

        def isPeak(i: Int): Boolean =
            i > 0 && i < n - 1 && nums(i) > nums(i - 1) && nums(i) > nums(i + 1)

        for (q <- queries) {
            q(0) match {
                case 2 =>
                    val idx = q(1)
                    val value = q(2)
                    if (nums(idx) != value) {
                        nums(idx) = value
                        var i = idx - 1
                        while (i <= idx + 1) {
                            if (i >= 1 && i <= n - 2) {
                                val newPeak = if (isPeak(i)) 1 else 0
                                if (newPeak != p(i)) {
                                    bit.add(i, newPeak - p(i))
                                    p(i) = newPeak
                                }
                            }
                            i += 1
                        }
                    }

                case 1 =>
                    val l = q(1)
                    val r = q(2)
                    var count = 0
                    if (l + 1 <= r - 1) {
                        val L = math.max(l + 1, 1)
                        val R = math.min(r - 1, n - 2)
                        if (L <= R) count = bit.rangeSum(L, R)
                    }
                    ans += count

                case _ => // ignore
            }
        }

        ans.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_of_peaks(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        struct Fenwick {
            n: usize,
            tree: Vec<i32>,
        }
        impl Fenwick {
            fn new(n: usize) -> Self {
                Fenwick { n, tree: vec![0; n + 1] }
            }
            fn add(&mut self, idx: usize, delta: i32) {
                let mut i = idx + 1;
                while i <= self.n {
                    self.tree[i] += delta;
                    i += i & (!i + 1);
                }
            }
            fn sum(&self, idx: usize) -> i32 {
                let mut i = idx + 1;
                let mut res = 0;
                while i > 0 {
                    res += self.tree[i];
                    i &= i - 1;
                }
                res
            }
        }

        let n = nums.len();
        let mut a = nums.clone();
        let mut p = vec![0i32; n];
        let mut bit = Fenwick::new(n);

        for i in 1..n - 1 {
            if a[i] > a[i - 1] && a[i] > a[i + 1] {
                p[i] = 1;
                bit.add(i, 1);
            }
        }

        let mut ans: Vec<i32> = Vec::new();

        for q in queries.iter() {
            let typ = q[0];
            if typ == 1 {
                let l = q[1] as usize;
                let r = q[2] as usize;
                if l + 1 <= r.saturating_sub(1) && l + 1 < n && r > 0 {
                    let left = l + 1;
                    let right = r - 1;
                    if left <= right {
                        let total = bit.sum(right)
                            - if left > 0 { bit.sum(left - 1) } else { 0 };
                        ans.push(total);
                    } else {
                        ans.push(0);
                    }
                } else {
                    ans.push(0);
                }
            } else {
                // update
                let pos = q[1] as usize;
                let val = q[2];
                a[pos] = val;

                let start = if pos >= 1 { pos - 1 } else { 0 };
                let end = usize::min(pos + 1, n - 1);
                for i in start..=end {
                    if i == 0 || i + 1 >= n {
                        continue;
                    }
                    let new_peak = if a[i] > a[i - 1] && a[i] > a[i + 1] { 1 } else { 0 };
                    if new_peak != p[i] {
                        let delta = new_peak - p[i];
                        bit.add(i, delta);
                        p[i] = new_peak;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-of-peaks nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (bit (make-vector (+ n 1) 0))
         (peaks (make-vector n 0))
         (bit-add!
          (lambda (idx delta)
            (let loop ((i idx))
              (when (<= i n)
                (vector-set! bit i (+ (vector-ref bit i) delta))
                (loop (+ i (bitwise-and i (- i))))))))
         (bit-sum
          (lambda (idx)
            (let loop ((i idx) (res 0))
              (if (= i 0)
                  res
                  (loop (bitwise-and i (- i)) (+ res (vector-ref bit i)))))))
         (range-sum
          (lambda (l r) ; inclusive, 1‑based indices for BIT
            (if (> l r) 0
                (- (bit-sum r) (bit-sum (- l 1))))))
         (is-peak?
          (lambda (i)
            (and (> i 0) (< i (- n 1))
                 (> (vector-ref nums-vec i) (vector-ref nums-vec (- i 1)))
                 (> (vector-ref nums-vec i) (vector-ref nums-vec (+ i 1))))))
         )
    ;; initialize peaks and BIT
    (for ([i (in-range 1 (- n 1))])          ; i = 1 .. n‑2
      (when (is-peak? i)
        (vector-set! peaks i 1)
        (bit-add! (+ i 1) 1)))
    ;; process queries
    (let loop ((qs queries) (ans '()))
      (if (null? qs)
          (reverse ans)
          (let* ((q (car qs))
                 (type (list-ref q 0)))
            (cond
              [(= type 2)                     ; update
               (let* ((pos (list-ref q 1))
                      (val (list-ref q 2)))
                 (when (not (= (vector-ref nums-vec pos) val))
                   (vector-set! nums-vec pos val)
                   (define start (max 1 (- pos 1)))          ; affected peak indices
                   (define end   (min (- n 2) (+ pos 1)))    ; inclusive
                   (for ([i (in-range start (+ end 1))])
                     (let ((newp (if (is-peak? i) 1 0))
                           (oldp (vector-ref peaks i)))
                       (when (not (= newp oldp))
                         (vector-set! peaks i newp)
                         (bit-add! (+ i 1) (- newp oldp))))))))
               (loop (cdr qs) ans)]
              [(= type 1)                     ; query
               (let* ((l (list-ref q 1))
                      (r (list-ref q 2)))
                 (if (< (- r l) 2)
                     (loop (cdr qs) (cons 0 ans))
                     (let ((sum (range-sum (+ l 2) r))) ; BIT indices for i = l+1 .. r-1
                       (loop (cdr qs) (cons sum ans)))))]
              [else (loop (cdr qs) ans)]))))))
```

## Erlang

```erlang
-spec count_of_peaks(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
count_of_peaks(Nums, Queries) ->
    N = length(Nums),
    NumArr0 = array:from_list(Nums),

    % initial peak flags
    Indices = lists:seq(0, N - 1),
    PList0 = [if I >= 1, I =< N - 2,
                 case is_peak(I, NumArr0) of true -> 1; false -> 0 end;
              true -> 0
             end || I <- Indices],

    Bit0 = build_bit(PList0, N),

    {_, _, RevAns} =
        lists:foldl(
          fun(Q, {NumArr, Bit, Acc}) ->
                  case Q of
                      [2, Idx, Val] ->
                          {NewNumArr, NewBit} = update_index(Idx, Val, NumArr, Bit, N),
                          {NewNumArr, NewBit, Acc};
                      [1, L, R] ->
                          Ans = query_range(L, R, Bit, N),
                          {NumArr, Bit, [Ans | Acc]}
                  end
          end,
          {NumArr0, Bit0, []},
          Queries),

    lists:reverse(RevAns).

%% --------------------------------------------------------------------
%% Helpers
%% --------------------------------------------------------------------

is_peak(I, NumArr) ->
    Left = array:get(I - 1, NumArr),
    Mid = array:get(I, NumArr),
    Right = array:get(I + 1, NumArr),
    Mid > Left andalso Mid > Right.

build_bit(PList, N) ->
    Bit0 = array:new(N + 1, {default, 0}),
    lists:foldl(
      fun({Idx, Val}, BitAcc) ->
              case Val of
                  1 -> bit_add(BitAcc, Idx + 1, 1, N);
                  _ -> BitAcc
              end
      end,
      Bit0,
      lists:zip(lists:seq(0, N - 1), PList)).

bit_add(Bit, Idx, Delta, N) when Idx =< N ->
    Cur = array:get(Idx, Bit),
    NewBit = array:set(Idx, Cur + Delta, Bit),
    Next = Idx + (Idx band -Idx),
    bit_add(NewBit, Next, Delta, N);
bit_add(Bit, _Idx, _Delta, _N) -> Bit.

bit_sum(Bit, Idx) ->
    bit_sum(Bit, Idx, 0).

bit_sum(_Bit, 0, Acc) -> Acc;
bit_sum(Bit, Idx, Acc) ->
    Cur = array:get(Idx, Bit),
    Next = Idx - (Idx band -Idx),
    bit_sum(Bit, Next, Acc + Cur).

update_index(Idx, Val, NumArr, Bit, N) ->
    OldVal = array:get(Idx, NumArr),
    if
        OldVal =:= Val -> {NumArr, Bit};
        true ->
            NewNumArr = array:set(Idx, Val, NumArr),
            Affected = [Idx - 1, Idx, Idx + 1],
            {FinalArr, FinalBit} =
                lists:foldl(
                  fun(I, {AccArr, AccBit}) ->
                          if
                              I >= 1, I =< N - 2 ->
                                  OldPeak = case is_peak(I, NumArr) of true -> 1; false -> 0 end,
                                  NewPeak = case is_peak(I, NewNumArr) of true -> 1; false -> 0 end,
                                  Delta = NewPeak - OldPeak,
                                  if
                                      Delta =/= 0 ->
                                          {AccArr, bit_add(AccBit, I + 1, Delta, N)};
                                      true ->
                                          {AccArr, AccBit}
                                  end;
                              true -> {AccArr, AccBit}
                          end
                  end,
                  {NewNumArr, Bit},
                  Affected),
            {FinalArr, FinalBit}
    end.

query_range(L, R, Bit, _N) ->
    Left = L + 1,
    Right = R - 1,
    if
        Left > Right -> 0;
        true ->
            SumR = bit_sum(Bit, Right + 1),
            SumL = bit_sum(Bit, Left),
            SumR - SumL
    end.
```

## Elixir

```elixir
defmodule Fenwick do
  use Bitwise

  def new(size) do
    :array.new(size + 1, default: 0)
  end

  def add(tree, idx, delta) when idx > 0 do
    size = :array.size(tree) - 1
    do_add(tree, idx, delta, size)
  end

  defp do_add(tree, idx, delta, size) do
    if idx <= size do
      cur = :array.get(idx, tree)
      new_tree = :array.set(idx, cur + delta, tree)
      next_idx = idx + (idx &&& -idx)
      do_add(new_tree, next_idx, delta, size)
    else
      tree
    end
  end

  def sum(tree, idx) do
    do_sum(tree, idx, 0)
  end

  defp do_sum(_tree, 0, acc), do: acc

  defp do_sum(tree, idx, acc) do
    cur = :array.get(idx, tree)
    next_idx = idx - (idx &&& -idx)
    do_sum(tree, next_idx, acc + cur)
  end

  def range_sum(tree, l, r) when l <= r do
    sum(tree, r) - sum(tree, l - 1)
  end
end

defmodule Solution do
  use Bitwise

  @spec count_of_peaks(nums :: [integer], queries :: [[integer]]) :: [integer]
  def count_of_peaks(nums, queries) do
    n = length(nums)
    nums_arr = :array.from_list(nums)
    peaks_arr = :array.new(n, default: 0)
    tree = Fenwick.new(n)

    {peaks_arr, tree} =
      Enum.reduce(1..(n - 2), {peaks_arr, tree}, fn i, {p_arr, tr} ->
        if is_peak(nums_arr, i) do
          p_arr2 = :array.set(i, 1, p_arr)
          tr2 = Fenwick.add(tr, i + 1, 1)
          {p_arr2, tr2}
        else
          {p_arr, tr}
        end
      end)

    {answers_rev, _final_nums, _final_peaks, _final_tree} =
      Enum.reduce(queries, {[], nums_arr, peaks_arr, tree}, fn q,
                                                               {ans_acc, n_arr, p_arr,
                                                                tr} ->
        case q do
          [2, idx, val] ->
            cur = :array.get(idx, n_arr)

            if cur == val do
              {ans_acc, n_arr, p_arr, tr}
            else
              n_arr2 = :array.set(idx, val, n_arr)

              positions =
                Enum.filter([idx - 1, idx, idx + 1], fn pos ->
                  pos >= 1 and pos <= n - 2
                end)

              {p_arr2, tr2} =
                Enum.reduce(positions, {p_arr, tr}, fn pos,
                                                       {pa, t} ->
                  old = :array.get(pos, pa)
                  new = if is_peak(n_arr2, pos), do: 1, else: 0
                  delta = new - old

                  if delta != 0 do
                    pa2 = :array.set(pos, new, pa)
                    t2 = Fenwick.add(t, pos + 1, delta)
                    {pa2, t2}
                  else
                    {pa, t}
                  end
                end)

              {ans_acc, n_arr2, p_arr2, tr2}
            end

          [1, l, r] ->
            if r - l <= 1 do
              {[0 | ans_acc], n_arr, p_arr, tr}
            else
              sum = Fenwick.range_sum(tr, l + 2, r)
              {[sum | ans_acc], n_arr, p_arr, tr}
            end
        end
      end)

    Enum.reverse(answers_rev)
  end

  defp is_peak(arr, i) do
    left = :array.get(i - 1, arr)
    mid = :array.get(i, arr)
    right = :array.get(i + 1, arr)
    mid > left and mid > right
  end
end
```
