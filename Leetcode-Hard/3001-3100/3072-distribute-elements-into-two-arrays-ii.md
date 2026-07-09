# 3072. Distribute Elements Into Two Arrays II

## Cpp

```cpp
class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n=0): n(n), bit(n+1, 0) {}
        void add(int idx, int val){
            for(; idx<=n; idx+=idx&-idx) bit[idx] += val;
        }
        int sum(int idx) const{
            int res = 0;
            for(; idx>0; idx-=idx&-idx) res += bit[idx];
            return res;
        }
    };
    
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> vals = nums;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int m = vals.size();
        
        BIT bit1(m), bit2(m);
        vector<int> arr1, arr2;
        arr1.reserve(n);
        arr2.reserve(n);
        int sz1 = 0, sz2 = 0;
        
        for (int i = 0; i < n; ++i) {
            int idx = lower_bound(vals.begin(), vals.end(), nums[i]) - vals.begin() + 1;
            if (i == 0) {
                arr1.push_back(nums[i]);
                bit1.add(idx, 1);
                ++sz1;
            } else if (i == 1) {
                arr2.push_back(nums[i]);
                bit2.add(idx, 1);
                ++sz2;
            } else {
                int cnt1 = sz1 - bit1.sum(idx); // greater than nums[i] in arr1
                int cnt2 = sz2 - bit2.sum(idx); // greater than nums[i] in arr2
                if (cnt1 > cnt2) {
                    arr1.push_back(nums[i]);
                    bit1.add(idx, 1);
                    ++sz1;
                } else if (cnt2 > cnt1) {
                    arr2.push_back(nums[i]);
                    bit2.add(idx, 1);
                    ++sz2;
                } else { // equal counts
                    if (sz1 < sz2) {
                        arr1.push_back(nums[i]);
                        bit1.add(idx, 1);
                        ++sz1;
                    } else if (sz2 < sz1) {
                        arr2.push_back(nums[i]);
                        bit2.add(idx, 1);
                        ++sz2;
                    } else { // same size
                        arr1.push_back(nums[i]);
                        bit1.add(idx, 1);
                        ++sz1;
                    }
                }
            }
        }
        vector<int> result;
        result.reserve(n);
        result.insert(result.end(), arr1.begin(), arr1.end());
        result.insert(result.end(), arr2.begin(), arr2.end());
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;
        // Coordinate compression
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        int m = 0;
        int[] uniq = new int[n];
        for (int v : sorted) {
            if (m == 0 || v != uniq[m - 1]) {
                uniq[m++] = v;
            }
        }
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>(m * 2);
        for (int i = 0; i < m; i++) {
            map.put(uniq[i], i + 1); // 1‑based index
        }

        Fenwick bit1 = new Fenwick(m);
        Fenwick bit2 = new Fenwick(m);
        java.util.ArrayList<Integer> arr1 = new java.util.ArrayList<>();
        java.util.ArrayList<Integer> arr2 = new java.util.ArrayList<>();

        int len1 = 0, len2 = 0;
        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int idx = map.get(val);
            if (i == 0) {                     // first operation
                arr1.add(val);
                bit1.add(idx, 1);
                len1++;
            } else if (i == 1) {              // second operation
                arr2.add(val);
                bit2.add(idx, 1);
                len2++;
            } else {
                int cnt1 = len1 - bit1.sum(idx); // elements > val in arr1
                int cnt2 = len2 - bit2.sum(idx); // elements > val in arr2

                if (cnt1 != cnt2) {
                    if (cnt1 > cnt2) {          // larger greaterCount -> append to that array
                        arr1.add(val);
                        bit1.add(idx, 1);
                        len1++;
                    } else {
                        arr2.add(val);
                        bit2.add(idx, 1);
                        len2++;
                    }
                } else { // equal greaterCount
                    if (len1 != len2) {
                        if (len1 < len2) {
                            arr1.add(val);
                            bit1.add(idx, 1);
                            len1++;
                        } else {
                            arr2.add(val);
                            bit2.add(idx, 1);
                            len2++;
                        }
                    } else { // equal lengths as well
                        arr1.add(val);
                        bit1.add(idx, 1);
                        len1++;
                    }
                }
            }
        }

        int[] result = new int[n];
        int pos = 0;
        for (int v : arr1) result[pos++] = v;
        for (int v : arr2) result[pos++] = v;
        return result;
    }

    private static class Fenwick {
        final int n;
        final int[] bit;

        Fenwick(int n) {
            this.n = n;
            this.bit = new int[n + 2];
        }

        void add(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }

        int sum(int idx) {
            int res = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        # coordinate compression
        vals = sorted(set(nums))
        comp = {v:i+1 for i,v in enumerate(vals)}  # 1-indexed for BIT
        m = len(vals)

        class BIT:
            __slots__ = ('size','tree')
            def __init__(self, size):
                self.size = size
                self.tree = [0]*(size+1)
            def add(self, idx, delta):
                while idx <= self.size:
                    self.tree[idx] += delta
                    idx += idx & -idx
            def query(self, idx):
                s = 0
                while idx > 0:
                    s += self.tree[idx]
                    idx -= idx & -idx
                return s

        bit1 = BIT(m)
        bit2 = BIT(m)

        arr1 = [nums[0]]
        arr2 = [nums[1]] if n > 1 else []
        idx0 = comp[nums[0]]
        bit1.add(idx0, 1)
        total1 = 1
        total2 = 0
        if n > 1:
            idx1 = comp[nums[1]]
            bit2.add(idx1, 1)
            total2 = 1

        for i in range(2, n):
            val = nums[i]
            idx = comp[val]

            cnt1 = total1 - bit1.query(idx)   # greater than val in arr1
            cnt2 = total2 - bit2.query(idx)   # greater than val in arr2

            if cnt1 > cnt2:
                choose = 1
            elif cnt2 > cnt1:
                choose = 2
            else:
                # tie, pick the shorter array (or arr1 if equal)
                if len(arr1) <= len(arr2):
                    choose = 1
                else:
                    choose = 2

            if choose == 1:
                arr1.append(val)
                bit1.add(idx, 1)
                total1 += 1
            else:
                arr2.append(val)
                bit2.add(idx, 1)
                total2 += 1

        return arr1 + arr2
```

## Python3

```python
class Solution:
    def resultArray(self, nums):
        from bisect import bisect_left

        # Coordinate compression
        uniq = sorted(set(nums))
        comp = {v: i + 1 for i, v in enumerate(uniq)}  # 1-indexed BIT size
        m = len(uniq)

        class BIT:
            __slots__ = ("n", "tree")
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)
            def add(self, idx, delta):
                while idx <= self.n:
                    self.tree[idx] += delta
                    idx += idx & -idx
            def sum(self, idx):
                s = 0
                while idx > 0:
                    s += self.tree[idx]
                    idx -= idx & -idx
                return s

        bit1 = BIT(m)
        bit2 = BIT(m)

        arr1 = []
        arr2 = []

        for i, val in enumerate(nums):
            idx = comp[val]
            if i == 0:
                arr1.append(val)
                bit1.add(idx, 1)
            elif i == 1:
                arr2.append(val)
                bit2.add(idx, 1)
            else:
                total1 = len(arr1)
                total2 = len(arr2)

                g1 = total1 - bit1.sum(idx)   # greater than val in arr1
                g2 = total2 - bit2.sum(idx)   # greater than val in arr2

                if g1 > g2:
                    arr1.append(val)
                    bit1.add(idx, 1)
                elif g2 > g1:
                    arr2.append(val)
                    bit2.add(idx, 1)
                else:
                    if len(arr1) <= len(arr2):
                        arr1.append(val)
                        bit1.add(idx, 1)
                    else:
                        arr2.append(val)
                        bit2.add(idx, 1)

        return arr1 + arr2
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int *tree;
} BIT;

static void bit_init(BIT *b, int n) {
    b->n = n;
    b->tree = (int *)calloc(n + 2, sizeof(int));
}

static void bit_update(BIT *b, int idx, int delta) {
    for (; idx <= b->n; idx += idx & -idx)
        b->tree[idx] += delta;
}

static int bit_query(const BIT *b, int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx)
        sum += b->tree[idx];
    return sum;
}

/* qsort comparator */
static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* lower_bound: first index >= target */
static int lower_bound(int *arr, int size, int target) {
    int l = 0, r = size; // [l, r)
    while (l < r) {
        int mid = l + ((r - l) >> 1);
        if (arr[mid] < target)
            l = mid + 1;
        else
            r = mid;
    }
    return l;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultArray(int* nums, int numsSize, int* returnSize) {
    // coordinate compression
    int *tmp = (int *)malloc(numsSize * sizeof(int));
    memcpy(tmp, nums, numsSize * sizeof(int));
    qsort(tmp, numsSize, sizeof(int), cmp_int);
    int *uniq = (int *)malloc(numsSize * sizeof(int));
    int m = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || tmp[i] != tmp[i - 1])
            uniq[m++] = tmp[i];
    }
    free(tmp);
    
    BIT bit1, bit2;
    bit_init(&bit1, m);
    bit_init(&bit2, m);
    
    int *arr1 = (int *)malloc(numsSize * sizeof(int));
    int *arr2 = (int *)malloc(numsSize * sizeof(int));
    int len1 = 0, len2 = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int idx = lower_bound(uniq, m, nums[i]) + 1; // BIT is 1-indexed
        if (i == 0) {
            arr1[len1++] = nums[i];
            bit_update(&bit1, idx, 1);
        } else if (i == 1) {
            arr2[len2++] = nums[i];
            bit_update(&bit2, idx, 1);
        } else {
            int cnt1 = len1 - bit_query(&bit1, idx); // greater than current
            int cnt2 = len2 - bit_query(&bit2, idx);
            if (cnt1 != cnt2) {
                if (cnt1 > cnt2) {
                    arr1[len1++] = nums[i];
                    bit_update(&bit1, idx, 1);
                } else {
                    arr2[len2++] = nums[i];
                    bit_update(&bit2, idx, 1);
                }
            } else {
                if (len1 != len2) {
                    if (len1 < len2) {
                        arr1[len1++] = nums[i];
                        bit_update(&bit1, idx, 1);
                    } else {
                        arr2[len2++] = nums[i];
                        bit_update(&bit2, idx, 1);
                    }
                } else {
                    arr1[len1++] = nums[i];
                    bit_update(&bit1, idx, 1);
                }
            }
        }
    }
    
    int *res = (int *)malloc(numsSize * sizeof(int));
    memcpy(res, arr1, len1 * sizeof(int));
    memcpy(res + len1, arr2, len2 * sizeof(int));
    
    *returnSize = numsSize;
    
    free(arr1);
    free(arr2);
    free(uniq);
    free(bit1.tree);
    free(bit2.tree);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private class Fenwick {
        private readonly int[] tree;
        private readonly int n;
        public Fenwick(int size) {
            n = size;
            tree = new int[n + 2];
        }
        public void Add(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i)
                tree[i] += delta;
        }
        public int Sum(int idx) {
            int res = 0;
            for (int i = idx; i > 0; i -= i & -i)
                res += tree[i];
            return res;
        }
    }

    public int[] ResultArray(int[] nums) {
        int n = nums.Length;
        // Coordinate compression
        var distinctSorted = nums.Distinct().OrderBy(x => x).ToArray();
        var map = new Dictionary<int, int>(distinctSorted.Length);
        for (int i = 0; i < distinctSorted.Length; i++) {
            map[distinctSorted[i]] = i + 1; // 1-indexed
        }
        int m = distinctSorted.Length;

        var bit1 = new Fenwick(m);
        var bit2 = new Fenwick(m);
        var arr1 = new List<int>();
        var arr2 = new List<int>();
        int size1 = 0, size2 = 0;

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int idx = map[val];

            if (i == 0) {
                // first element to arr1
                arr1.Add(val);
                bit1.Add(idx, 1);
                size1++;
            } else if (i == 1) {
                // second element to arr2
                arr2.Add(val);
                bit2.Add(idx, 1);
                size2++;
            } else {
                int greater1 = size1 - bit1.Sum(idx); // strictly greater than val in arr1
                int greater2 = size2 - bit2.Sum(idx); // strictly greater than val in arr2

                if (greater1 < greater2) {
                    arr1.Add(val);
                    bit1.Add(idx, 1);
                    size1++;
                } else if (greater2 < greater1) {
                    arr2.Add(val);
                    bit2.Add(idx, 1);
                    size2++;
                } else {
                    // tie: choose smaller length, if equal choose arr1
                    if (size1 <= size2) {
                        arr1.Add(val);
                        bit1.Add(idx, 1);
                        size1++;
                    } else {
                        arr2.Add(val);
                        bit2.Add(idx, 1);
                        size2++;
                    }
                }
            }
        }

        int[] result = new int[n];
        int pos = 0;
        foreach (int v in arr1) result[pos++] = v;
        foreach (int v in arr2) result[pos++] = v;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var resultArray = function(nums) {
    const n = nums.length;
    // coordinate compression
    const sorted = Array.from(new Set(nums.slice().sort((a, b) => a - b)));
    const idxMap = new Map();
    for (let i = 0; i < sorted.length; ++i) {
        idxMap.set(sorted[i], i + 1); // 1‑based index for BIT
    }
    class Fenwick {
        constructor(size) {
            this.n = size;
            this.bit = new Array(size + 2).fill(0);
        }
        add(i, delta) {
            for (; i <= this.n; i += i & -i) this.bit[i] += delta;
        }
        sum(i) {
            let s = 0;
            for (; i > 0; i -= i & -i) s += this.bit[i];
            return s;
        }
    }
    const m = sorted.length;
    const bit1 = new Fenwick(m);
    const bit2 = new Fenwick(m);
    const arr1 = [];
    const arr2 = [];
    let size1 = 0, size2 = 0;

    for (let i = 0; i < n; ++i) {
        const val = nums[i];
        const id = idxMap.get(val);
        if (i === 0) { // first operation -> arr1
            arr1.push(val);
            size1++;
            bit1.add(id, 1);
        } else if (i === 1) { // second operation -> arr2
            arr2.push(val);
            size2++;
            bit2.add(id, 1);
        } else {
            const cnt1 = size1 - bit1.sum(id); // greater than val in arr1
            const cnt2 = size2 - bit2.sum(id); // greater than val in arr2

            if (cnt1 > cnt2) {
                arr1.push(val);
                size1++;
                bit1.add(id, 1);
            } else if (cnt2 > cnt1) {
                arr2.push(val);
                size2++;
                bit2.add(id, 1);
            } else { // equal counts
                if (size1 < size2) {
                    arr1.push(val);
                    size1++;
                    bit1.add(id, 1);
                } else if (size2 < size1) {
                    arr2.push(val);
                    size2++;
                    bit2.add(id, 1);
                } else { // same length
                    arr1.push(val);
                    size1++;
                    bit1.add(id, 1);
                }
            }
        }
    }

    return arr1.concat(arr2);
};
```

## Typescript

```typescript
function resultArray(nums: number[]): number[] {
    const n = nums.length;
    // Coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const idxMap = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) idxMap.set(uniq[i], i + 1);

    class BIT {
        private tree: number[];
        private size: number;
        constructor(size: number) {
            this.size = size;
            this.tree = new Array(size + 2).fill(0);
        }
        update(i: number, delta: number): void {
            for (; i <= this.size; i += i & -i) this.tree[i] += delta;
        }
        query(i: number): number {
            let sum = 0;
            for (; i > 0; i -= i & -i) sum += this.tree[i];
            return sum;
        }
    }

    const bit1 = new BIT(uniq.length);
    const bit2 = new BIT(uniq.length);

    const arr1: number[] = [];
    const arr2: number[] = [];
    let size1 = 0, size2 = 0;

    for (let i = 0; i < n; i++) {
        const val = nums[i];
        const idx = idxMap.get(val)!;
        if (i === 0) {
            arr1.push(val);
            bit1.update(idx, 1);
            size1++;
        } else if (i === 1) {
            arr2.push(val);
            bit2.update(idx, 1);
            size2++;
        } else {
            const g1 = size1 - bit1.query(idx);
            const g2 = size2 - bit2.query(idx);
            let toArr1: boolean;
            if (g1 > g2) {
                toArr1 = true;
            } else if (g1 < g2) {
                toArr1 = false;
            } else {
                if (size1 < size2) toArr1 = true;
                else if (size1 > size2) toArr1 = false;
                else toArr1 = true;
            }
            if (toArr1) {
                arr1.push(val);
                bit1.update(idx, 1);
                size1++;
            } else {
                arr2.push(val);
                bit2.update(idx, 1);
                size2++;
            }
        }
    }

    return arr1.concat(arr2);
}
```

## Php

```php
class Fenwick {
    private $tree;
    private $n;

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
     * @return Integer[]
     */
    function resultArray($nums) {
        $n = count($nums);
        // coordinate compression
        $sorted = $nums;
        sort($sorted, SORT_NUMERIC);
        $unique = array_values(array_unique($sorted));
        $m = count($unique);
        $map = [];
        for ($i = 0; $i < $m; $i++) {
            $map[$unique[$i]] = $i + 1; // 1-indexed
        }

        $bit1 = new Fenwick($m);
        $bit2 = new Fenwick($m);
        $arr1 = [];
        $arr2 = [];
        $len1 = 0;
        $len2 = 0;

        for ($i = 0; $i < $n; $i++) {
            $val = $nums[$i];
            $idx = $map[$val];

            if ($i == 0) { // first element to arr1
                $arr1[] = $val;
                $len1++;
                $bit1->add($idx, 1);
            } elseif ($i == 1) { // second element to arr2
                $arr2[] = $val;
                $len2++;
                $bit2->add($idx, 1);
            } else {
                $greater1 = $len1 - $bit1->sum($idx);
                $greater2 = $len2 - $bit2->sum($idx);

                if ($greater1 > $greater2) {
                    $arr1[] = $val;
                    $len1++;
                    $bit1->add($idx, 1);
                } elseif ($greater2 > $greater1) {
                    $arr2[] = $val;
                    $len2++;
                    $bit2->add($idx, 1);
                } else { // equal greater counts
                    if ($len1 < $len2) {
                        $arr1[] = $val;
                        $len1++;
                        $bit1->add($idx, 1);
                    } elseif ($len2 < $len1) {
                        $arr2[] = $val;
                        $len2++;
                        $bit2->add($idx, 1);
                    } else { // equal lengths
                        $arr1[] = $val;
                        $len1++;
                        $bit1->add($idx, 1);
                    }
                }
            }
        }

        return array_merge($arr1, $arr2);
    }
}
```

## Swift

```swift
class Fenwick {
    private var n: Int
    private var tree: [Int]
    
    init(_ size: Int) {
        self.n = size
        self.tree = Array(repeating: 0, count: size + 2)
    }
    
    func update(_ index: Int, _ delta: Int) {
        var i = index
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    
    func query(_ index: Int) -> Int {
        var i = index
        var res = 0
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
}

class Solution {
    func resultArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        // Coordinate compression
        var uniq = Array(Set(nums))
        uniq.sort()
        var comp = [Int:Int]()
        for (i, v) in uniq.enumerated() {
            comp[v] = i + 1   // 1‑based index for BIT
        }
        let m = uniq.count
        let bit1 = Fenwick(m)
        let bit2 = Fenwick(m)
        
        var arr1 = [Int]()
        var arr2 = [Int]()
        
        // first element to arr1
        arr1.append(nums[0])
        if let idx = comp[nums[0]] {
            bit1.update(idx, 1)
        }
        // second element to arr2
        arr2.append(nums[1])
        if let idx = comp[nums[1]] {
            bit2.update(idx, 1)
        }
        
        var size1 = 1
        var size2 = 1
        
        for i in 2..<n {
            let val = nums[i]
            guard let idx = comp[val] else { continue }
            
            // count of elements greater than val in each array
            let greater1 = size1 - bit1.query(idx)
            let greater2 = size2 - bit2.query(idx)
            
            if greater1 != greater2 {
                if greater1 > greater2 {
                    arr1.append(val)
                    bit1.update(idx, 1)
                    size1 += 1
                } else {
                    arr2.append(val)
                    bit2.update(idx, 1)
                    size2 += 1
                }
            } else {
                // counts equal, tie‑break by length then by arr1 preference
                if size1 < size2 {
                    arr1.append(val)
                    bit1.update(idx, 1)
                    size1 += 1
                } else if size2 < size1 {
                    arr2.append(val)
                    bit2.update(idx, 1)
                    size2 += 1
                } else {
                    // equal lengths -> choose arr1
                    arr1.append(val)
                    bit1.update(idx, 1)
                    size1 += 1
                }
            }
        }
        
        return arr1 + arr2
    }
}
```

## Kotlin

```kotlin
import java.util.*
 
class Fenwick(private val n: Int) {
    private val tree = IntArray(n + 2)
    fun update(i: Int, delta: Int) {
        var idx = i
        while (idx <= n) {
            tree[idx] += delta
            idx += idx and -idx
        }
    }
    fun query(i: Int): Int {
        var idx = i
        var sum = 0
        while (idx > 0) {
            sum += tree[idx]
            idx -= idx and -idx
        }
        return sum
    }
}
 
class Solution {
    fun resultArray(nums: IntArray): IntArray {
        val n = nums.size
        // coordinate compression
        val sorted = nums.clone()
        Arrays.sort(sorted)
        val uniqList = ArrayList<Int>()
        var prev = -1L
        for (v in sorted) {
            if (v.toLong() != prev) {
                uniqList.add(v)
                prev = v.toLong()
            }
        }
        val m = uniqList.size
        val indexMap = HashMap<Int, Int>(m * 2)
        for (i in 0 until m) {
            indexMap[uniqList[i]] = i + 1 // 1‑based
        }
 
        val bit1 = Fenwick(m)
        val bit2 = Fenwick(m)
        val arr1 = ArrayList<Int>()
        val arr2 = ArrayList<Int>()
        var size1 = 0
        var size2 = 0
 
        for (i in 0 until n) {
            val v = nums[i]
            val idx = indexMap[v]!!
            when (i) {
                0 -> {
                    arr1.add(v)
                    bit1.update(idx, 1)
                    size1++
                }
                1 -> {
                    arr2.add(v)
                    bit2.update(idx, 1)
                    size2++
                }
                else -> {
                    val cnt1 = size1 - bit1.query(idx) // greater than v in arr1
                    val cnt2 = size2 - bit2.query(idx) // greater than v in arr2
                    if (cnt1 > cnt2) {
                        arr1.add(v)
                        bit1.update(idx, 1)
                        size1++
                    } else if (cnt2 > cnt1) {
                        arr2.add(v)
                        bit2.update(idx, 1)
                        size2++
                    } else {
                        if (size1 <= size2) {
                            arr1.add(v)
                            bit1.update(idx, 1)
                            size1++
                        } else {
                            arr2.add(v)
                            bit2.update(idx, 1)
                            size2++
                        }
                    }
                }
            }
        }
 
        val result = IntArray(n)
        var pos = 0
        for (v in arr1) result[pos++] = v
        for (v in arr2) result[pos++] = v
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultArray(List<int> nums) {
    int n = nums.length;
    // Coordinate compression
    List<int> sorted = List.from(nums);
    sorted.sort();
    List<int> uniq = [];
    for (int v in sorted) {
      if (uniq.isEmpty || uniq.last != v) uniq.add(v);
    }
    Map<int, int> comp = {};
    for (int i = 0; i < uniq.length; i++) {
      comp[uniq[i]] = i + 1; // 1-indexed BIT
    }

    // Binary Indexed Tree implementation
    class BIT {
      final int size;
      final List<int> tree;
      BIT(this.size) : tree = List.filled(size + 2, 0);
      void add(int idx, int delta) {
        while (idx <= size) {
          tree[idx] += delta;
          idx += idx & -idx;
        }
      }

      int sum(int idx) {
        int res = 0;
        while (idx > 0) {
          res += tree[idx];
          idx -= idx & -idx;
        }
        return res;
      }
    }

    BIT bit1 = BIT(uniq.length);
    BIT bit2 = BIT(uniq.length);

    List<int> arr1 = [];
    List<int> arr2 = [];

    int size1 = 0, size2 = 0;

    // First element to arr1
    int idx = comp[nums[0]]!;
    arr1.add(nums[0]);
    bit1.add(idx, 1);
    size1++;

    // Second element to arr2
    idx = comp[nums[1]]!;
    arr2.add(nums[1]);
    bit2.add(idx, 1);
    size2++;

    for (int i = 2; i < n; i++) {
      int val = nums[i];
      idx = comp[val]!;

      int gc1 = size1 - bit1.sum(idx); // greater count in arr1
      int gc2 = size2 - bit2.sum(idx); // greater count in arr2

      bool chooseArr1;
      if (gc1 != gc2) {
        chooseArr1 = gc1 > gc2;
      } else {
        if (size1 != size2) {
          chooseArr1 = size1 < size2; // smaller length gets the element
        } else {
          chooseArr1 = true; // tie -> arr1
        }
      }

      if (chooseArr1) {
        arr1.add(val);
        bit1.add(idx, 1);
        size1++;
      } else {
        arr2.add(val);
        bit2.add(idx, 1);
        size2++;
      }
    }

    return [...arr1, ...arr2];
  }
}
```

## Golang

```go
package main

import "sort"

type Fenwick struct {
	tree []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{make([]int, n+2)}
}

func (f *Fenwick) Add(i, delta int) {
	for i < len(f.tree) {
		f.tree[i] += delta
		i += i & -i
	}
}

func (f *Fenwick) Sum(i int) int {
	res := 0
	for i > 0 {
		res += f.tree[i]
		i -= i & -i
	}
	return res
}

func resultArray(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return []int{}
	}
	// coordinate compression
	compVals := make([]int, n)
	copy(compVals, nums)
	sort.Ints(compVals)
	uniq := make([]int, 0, n)
	for _, v := range compVals {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	idxMap := make(map[int]int, len(uniq))
	for i, v := range uniq {
		idxMap[v] = i + 1 // 1-based
	}
	m := len(uniq)

	bit1 := NewFenwick(m)
	bit2 := NewFenwick(m)

	arr1 := make([]int, 0, n)
	arr2 := make([]int, 0, n)
	size1, size2 := 0, 0

	for i, v := range nums {
		idx := idxMap[v]
		if i == 0 {
			arr1 = append(arr1, v)
			bit1.Add(idx, 1)
			size1++
			continue
		}
		if i == 1 {
			arr2 = append(arr2, v)
			bit2.Add(idx, 1)
			size2++
			continue
		}
		c1 := size1 - bit1.Sum(idx) // greater than v in arr1
		c2 := size2 - bit2.Sum(idx) // greater than v in arr2

		if c1 > c2 {
			arr1 = append(arr1, v)
			bit1.Add(idx, 1)
			size1++
		} else if c2 > c1 {
			arr2 = append(arr2, v)
			bit2.Add(idx, 1)
			size2++
		} else { // equal counts
			if size1 < size2 {
				arr1 = append(arr1, v)
				bit1.Add(idx, 1)
				size1++
			} else if size2 < size1 {
				arr2 = append(arr2, v)
				bit2.Add(idx, 1)
				size2++
			} else { // equal sizes
				arr1 = append(arr1, v)
				bit1.Add(idx, 1)
				size1++
			}
		}
	}

	result := make([]int, 0, n)
	result = append(result, arr1...)
	result = append(result, arr2...)
	return result
}
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @tree = Array.new(n + 2, 0)
    @total = 0
  end

  def add(i, delta)
    while i <= @n
      @tree[i] += delta
      i += i & -i
    end
    @total += delta
  end

  def sum(i)
    s = 0
    while i > 0
      s += @tree[i]
      i -= i & -i
    end
    s
  end

  def total
    @total
  end
end

# @param {Integer[]} nums
# @return {Integer[]}
def result_array(nums)
  n = nums.length
  # coordinate compression
  uniq_vals = nums.uniq.sort
  idx_map = {}
  uniq_vals.each_with_index { |v, i| idx_map[v] = i + 1 }

  m = uniq_vals.size
  bit1 = BIT.new(m)
  bit2 = BIT.new(m)

  arr1 = []
  arr2 = []

  nums.each_with_index do |val, i|
    idx = idx_map[val]
    if i == 0
      arr1 << val
      bit1.add(idx, 1)
    elsif i == 1
      arr2 << val
      bit2.add(idx, 1)
    else
      c1 = bit1.total - bit1.sum(idx) # greater than val in arr1
      c2 = bit2.total - bit2.sum(idx) # greater than val in arr2

      if c1 > c2
        arr1 << val
        bit1.add(idx, 1)
      elsif c1 < c2
        arr2 << val
        bit2.add(idx, 1)
      else
        if arr1.length <= arr2.length
          arr1 << val
          bit1.add(idx, 1)
        else
          arr2 << val
          bit2.add(idx, 1)
        end
      end
    end
  end

  arr1 + arr2
end
```

## Scala

```scala
object Solution {
    def resultArray(nums: Array[Int]): Array[Int] = {
        class BIT(val n: Int) {
            private val tree = new Array[Int](n + 2)
            def add(idx0: Int, delta: Int): Unit = {
                var i = idx0
                while (i <= n) {
                    tree(i) += delta
                    i += i & -i
                }
            }
            def sum(idx0: Int): Int = {
                var res = 0
                var i = idx0
                while (i > 0) {
                    res += tree(i)
                    i -= i & -i
                }
                res
            }
            def queryRange(l: Int, r: Int): Int = {
                if (l > r) 0 else sum(r) - sum(l - 1)
            }
        }

        val n = nums.length
        val sorted = nums.distinct.sorted
        val idxMap = scala.collection.mutable.HashMap[Int, Int]()
        for ((v, i) <- sorted.zipWithIndex) {
            idxMap(v) = i + 1 // 1-based index for BIT
        }
        val m = sorted.length

        val bit1 = new BIT(m)
        val bit2 = new BIT(m)

        import scala.collection.mutable.ArrayBuffer
        val arr1Buf = new ArrayBuffer[Int]()
        val arr2Buf = new ArrayBuffer[Int]()

        var size1 = 0
        var size2 = 0

        for (i <- nums.indices) {
            val v = nums(i)
            val idx = idxMap(v)
            if (i == 0) {
                bit1.add(idx, 1)
                size1 += 1
                arr1Buf += v
            } else if (i == 1) {
                bit2.add(idx, 1)
                size2 += 1
                arr2Buf += v
            } else {
                val cnt1 = bit1.queryRange(idx + 1, m)
                val cnt2 = bit2.queryRange(idx + 1, m)

                val toArr1: Boolean =
                    if (cnt1 != cnt2) cnt1 > cnt2
                    else if (size1 != size2) size1 < size2
                    else true

                if (toArr1) {
                    bit1.add(idx, 1)
                    size1 += 1
                    arr1Buf += v
                } else {
                    bit2.add(idx, 1)
                    size2 += 1
                    arr2Buf += v
                }
            }
        }

        val result = new Array[Int](n)
        var pos = 0
        for (v <- arr1Buf) {
            result(pos) = v
            pos += 1
        }
        for (v <- arr2Buf) {
            result(pos) = v
            pos += 1
        }
        result
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct BIT {
    n: usize,
    tree: Vec<i32>,
}

impl BIT {
    fn new(size: usize) -> Self {
        BIT { n: size, tree: vec![0; size + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i32) {
        while idx <= self.n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }

        // coordinate compression
        let mut vals = nums.clone();
        vals.sort_unstable();
        vals.dedup();
        let m = vals.len();

        let mut bit1 = BIT::new(m);
        let mut bit2 = BIT::new(m);

        let mut arr1: Vec<i32> = Vec::with_capacity(n);
        let mut arr2: Vec<i32> = Vec::with_capacity(n);

        for (i, &v) in nums.iter().enumerate() {
            let idx = vals.binary_search(&v).unwrap(); // 0‑based
            if i == 0 {
                arr1.push(v);
                bit1.add(idx + 1, 1);
            } else if i == 1 {
                arr2.push(v);
                bit2.add(idx + 1, 1);
            } else {
                let total1 = arr1.len() as i32;
                let total2 = arr2.len() as i32;

                let greater1 = total1 - bit1.sum(idx + 1);
                let greater2 = total2 - bit2.sum(idx + 1);

                match greater1.cmp(&greater2) {
                    Ordering::Greater => {
                        arr1.push(v);
                        bit1.add(idx + 1, 1);
                    }
                    Ordering::Less => {
                        arr2.push(v);
                        bit2.add(idx + 1, 1);
                    }
                    Ordering::Equal => {
                        if arr1.len() < arr2.len() {
                            arr1.push(v);
                            bit1.add(idx + 1, 1);
                        } else if arr2.len() < arr1.len() {
                            arr2.push(v);
                            bit2.add(idx + 1, 1);
                        } else {
                            // equal lengths
                            arr1.push(v);
                            bit1.add(idx + 1, 1);
                        }
                    }
                }
            }
        }

        let mut result = Vec::with_capacity(n);
        result.extend(arr1);
        result.extend(arr2);
        result
    }
}
```

## Racket

```racket
(define/contract (result-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         ;; coordinate compression
         (vals (vector->list nums-vec))
         (uniq (remove-duplicates (sort vals <)))
         (m (length uniq))
         (idx-hash (make-hash)))
    (for ([v uniq] [i (in-naturals 1)])
      (hash-set! idx-hash v i))
    ;; Fenwick tree definition
    (struct fenwick (tree n) #:mutable)
    (define (make-fenwick size)
      (fenwick (make-vector (+ size 1) 0) size))
    (define (fenwick-update! ft idx delta)
      (let ((tree (fenwick-tree ft))
            (size (fenwick-n ft)))
        (let loop ((i idx))
          (when (<= i size)
            (vector-set! tree i (+ (vector-ref tree i) delta))
            (loop (+ i (bitwise-and i (- i))))))))
    (define (fenwick-query ft idx)
      (let ((tree (fenwick-tree ft)))
        (let loop ((i idx) (sum 0))
          (if (= i 0)
              sum
              (loop (bitwise-and i (- i)) (+ sum (vector-ref tree i)))))))
    ;; data structures for two arrays
    (define ft1 (make-fenwick m))
    (define ft2 (make-fenwick m))
    (define arr1 (make-vector n))
    (define arr2 (make-vector n))
    (define idx1 0)
    (define idx2 0)
    ;; first element to arr1
    (when (> n 0)
      (let ((v (vector-ref nums-vec 0)))
        (vector-set! arr1 idx1 v)
        (set! idx1 (+ idx1 1))
        (fenwick-update! ft1 (hash-ref idx-hash v) 1)))
    ;; second element to arr2
    (when (> n 1)
      (let ((v (vector-ref nums-vec 1)))
        (vector-set! arr2 idx2 v)
        (set! idx2 (+ idx2 1))
        (fenwick-update! ft2 (hash-ref idx-hash v) 1)))
    ;; process remaining elements
    (for ([i (in-range 2 n)])
      (let* ((v (vector-ref nums-vec i))
             (ci (hash-ref idx-hash v))
             (cnt1 (- idx1 (fenwick-query ft1 ci))) ; > v in arr1
             (cnt2 (- idx2 (fenwick-query ft2 ci)))) ; > v in arr2
        (cond
          [(> cnt1 cnt2)
           (vector-set! arr1 idx1 v)
           (set! idx1 (+ idx1 1))
           (fenwick-update! ft1 ci 1)]
          [(< cnt1 cnt2)
           (vector-set! arr2 idx2 v)
           (set! idx2 (+ idx2 1))
           (fenwick-update! ft2 ci 1)]
          [else
           (if (<= idx1 idx2)
               (begin
                 (vector-set! arr1 idx1 v)
                 (set! idx1 (+ idx1 1))
                 (fenwick-update! ft1 ci 1))
               (begin
                 (vector-set! arr2 idx2 v)
                 (set! idx2 (+ idx2 1))
                 (fenwick-update! ft2 ci 1)))])))
    ;; helper to take first k elements of a vector as list preserving order
    (define (vec-take vec k)
      (let loop ((i (- k 1)) (acc '()))
        (if (< i 0)
            acc
            (loop (- i 1) (cons (vector-ref vec i) acc)))))
    (append (vec-take arr1 idx1) (vec-take arr2 idx2))))
```

## Erlang

```erlang
-spec result_array(Nums :: [integer()]) -> [integer()].
result_array(Nums) ->
    Unique = lists:usort(Nums),
    ValToIdx = maps:from_list(lists:zip(Unique, lists:seq(1, length(Unique)))),
    Size = length(Unique),
    BIT1 = {Size, #{}},
    BIT2 = {Size, #{}},
    loop(Nums, 1, ValToIdx, BIT1, BIT2, 0, 0, [], []).

loop([], _Pos, _VMap, _BIT1, _BIT2, _Len1, _Len2, Arr1, Arr2) ->
    lists:reverse(Arr1) ++ lists:reverse(Arr2);
loop([Val | Rest], Pos, VMap, BIT1, BIT2, Len1, Len2, Arr1, Arr2) ->
    Idx = maps:get(Val, VMap),
    case Pos of
        1 ->
            NewBIT1 = bit_update(BIT1, Idx),
            loop(Rest, Pos + 1, VMap, NewBIT1, BIT2, Len1 + 1, Len2, [Val | Arr1], Arr2);
        2 ->
            NewBIT2 = bit_update(BIT2, Idx),
            loop(Rest, Pos + 1, VMap, BIT1, NewBIT2, Len1, Len2 + 1, Arr1, [Val | Arr2]);
        _ ->
            C1 = Len1 - bit_query(BIT1, Idx),
            C2 = Len2 - bit_query(BIT2, Idx),
            if
                C1 > C2 ->
                    NewBIT1 = bit_update(BIT1, Idx),
                    loop(Rest, Pos + 1, VMap, NewBIT1, BIT2, Len1 + 1, Len2, [Val | Arr1], Arr2);
                C2 > C1 ->
                    NewBIT2 = bit_update(BIT2, Idx),
                    loop(Rest, Pos + 1, VMap, BIT1, NewBIT2, Len1, Len2 + 1, Arr1, [Val | Arr2]);
                true ->
                    if
                        Len1 < Len2 ->
                            NewBIT1 = bit_update(BIT1, Idx),
                            loop(Rest, Pos + 1, VMap, NewBIT1, BIT2, Len1 + 1, Len2, [Val | Arr1], Arr2);
                        Len2 < Len1 ->
                            NewBIT2 = bit_update(BIT2, Idx),
                            loop(Rest, Pos + 1, VMap, BIT1, NewBIT2, Len1, Len2 + 1, Arr1, [Val | Arr2]);
                        true ->
                            NewBIT1 = bit_update(BIT1, Idx),
                            loop(Rest, Pos + 1, VMap, NewBIT1, BIT2, Len1 + 1, Len2, [Val | Arr1], Arr2)
                    end
            end
    end.

bit_update({Size, Map}, Idx) ->
    {Size, update_loop(Idx, Size, Map)}.

update_loop(I, Size, M) when I > Size -> M;
update_loop(I, Size, M) ->
    NewM = maps:update_with(I,
        fun(V) -> V + 1 end,
        1,
        M),
    update_loop(I + (I band (-I)), Size, NewM).

bit_query({_, Map}, Idx) ->
    query_loop(Idx, Map, 0).

query_loop(0, _Map, Acc) -> Acc;
query_loop(I, Map, Acc) ->
    Val = maps:get(I, Map, 0),
    query_loop(I - (I band (-I)), Map, Acc + Val).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec result_array(nums :: [integer]) :: [integer]
  def result_array(nums) do
    uniq_sorted = nums |> Enum.uniq() |> Enum.sort()
    rank_map = Enum.with_index(uniq_sorted, 1) |> Enum.into(%{}, fn {v, i} -> {v, i} end)
    max_idx = length(uniq_sorted)

    bit1 = :array.new(max_idx + 2, default: 0)
    bit2 = :array.new(max_idx + 2, default: 0)

    {arr1_rev, arr2_rev, _b1, _b2, _c1, _c2} =
      Enum.with_index(nums, 1)
      |> Enum.reduce({[], [], bit1, bit2, 0, 0}, fn {val, idx},
            {a1, a2, b1, b2, c1, c2} ->
        rank = Map.fetch!(rank_map, val)

        cond do
          idx == 1 ->
            nb1 = bit_update(b1, rank, 1, max_idx)
            {[val | a1], a2, nb1, b2, c1 + 1, c2}

          idx == 2 ->
            nb2 = bit_update(b2, rank, 1, max_idx)
            {a1, [val | a2], b1, nb2, c1, c2 + 1}

          true ->
            gc1 = c1 - bit_query(b1, rank)
            gc2 = c2 - bit_query(b2, rank)

            cond do
              gc1 > gc2 ->
                nb1 = bit_update(b1, rank, 1, max_idx)
                {[val | a1], a2, nb1, b2, c1 + 1, c2}

              gc2 > gc1 ->
                nb2 = bit_update(b2, rank, 1, max_idx)
                {a1, [val | a2], b1, nb2, c1, c2 + 1}

              true ->
                if c1 <= c2 do
                  nb1 = bit_update(b1, rank, 1, max_idx)
                  {[val | a1], a2, nb1, b2, c1 + 1, c2}
                else
                  nb2 = bit_update(b2, rank, 1, max_idx)
                  {a1, [val | a2], b1, nb2, c1, c2 + 1}
                end
            end
        end
      end)

    Enum.reverse(arr1_rev) ++ Enum.reverse(arr2_rev)
  end

  defp bit_update(bit, idx, delta, max_idx) when idx <= max_idx do
    cur = :array.get(idx, bit)
    new_bit = :array.set(idx, cur + delta, bit)
    next = idx + (idx &&& -idx)
    bit_update(new_bit, next, delta, max_idx)
  end

  defp bit_update(bit, _idx, _delta, _max_idx), do: bit

  defp bit_query(_bit, 0), do: 0

  defp bit_query(bit, idx) do
    cur = :array.get(idx, bit)
    bit_query(bit, idx - (idx &&& -idx)) + cur
  end
end
```
