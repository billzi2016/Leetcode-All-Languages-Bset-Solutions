# 1157. Online Majority Element In Subarray

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class MajorityChecker {
    vector<int> arr_;
    unordered_map<int, vector<int>> pos_;
    mt19937 rng_;
public:
    MajorityChecker(vector<int>& arr) : arr_(arr), rng_(chrono::steady_clock::now().time_since_epoch().count()) {
        for (int i = 0; i < (int)arr_.size(); ++i) {
            pos_[arr_[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int threshold) {
        uniform_int_distribution<int> dist(left, right);
        const int attempts = 25;
        for (int i = 0; i < attempts; ++i) {
            int idx = dist(rng_);
            int cand = arr_[idx];
            const auto& vec = pos_[cand];
            int cnt = upper_bound(vec.begin(), vec.end(), right) - lower_bound(vec.begin(), vec.end(), left);
            if (cnt >= threshold) return cand;
        }
        return -1;
    }
};

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker* obj = new MajorityChecker(arr);
 * int param_1 = obj->query(left,right,threshold);
 */
```

## Java

```java
class MajorityChecker {
    private int[] arr;
    private java.util.Map<Integer, java.util.List<Integer>> posMap;
    private java.util.Random rand;

    public MajorityChecker(int[] arr) {
        this.arr = arr;
        posMap = new java.util.HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            posMap.computeIfAbsent(arr[i], k -> new java.util.ArrayList<>()).add(i);
        }
        rand = new java.util.Random();
    }

    public int query(int left, int right, int threshold) {
        int len = right - left + 1;
        for (int attempt = 0; attempt < 20; ++attempt) {
            int idx = left + rand.nextInt(len);
            int val = arr[idx];
            java.util.List<Integer> list = posMap.get(val);
            if (list == null) continue;
            int cnt = upperBound(list, right) - lowerBound(list, left);
            if (cnt >= threshold) {
                return val;
            }
        }
        return -1;
    }

    private int lowerBound(java.util.List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private int upperBound(java.util.List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) > target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.query(left,right,threshold);
 */
```

## Python

```python
class MajorityChecker(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        from collections import defaultdict
        self.arr = arr
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)
        self._build(1, 0, self.n - 1)

    def _merge(self, left_pair, right_pair):
        # each pair is (value, count)
        if not left_pair:
            return right_pair
        if not right_pair:
            return left_pair
        lv, lc = left_pair
        rv, rc = right_pair
        if lv == rv:
            return (lv, lc + rc)
        if lc > rc:
            return (lv, lc - rc)
        else:
            return (rv, rc - lc)

    def _build(self, idx, l, r):
        if l == r:
            self.tree[idx] = (self.arr[l], 1)
            return
        mid = (l + r) // 2
        self._build(idx * 2, l, mid)
        self._build(idx * 2 + 1, mid + 1, r)
        self.tree[idx] = self._merge(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def _query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        res = None
        if ql <= mid:
            res = self._merge(res, self._query(idx * 2, l, mid, ql, qr))
        if qr > mid:
            res = self._merge(res, self._query(idx * 2 + 1, mid + 1, r, ql, qr))
        return res

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        import bisect
        cand_pair = self._query(1, 0, self.n - 1, left, right)
        if not cand_pair:
            return -1
        cand = cand_pair[0]
        lst = self.pos.get(cand, [])
        cnt = bisect.bisect_right(lst, right) - bisect.bisect_left(lst, left)
        return cand if cnt >= threshold else -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
```

## Python3

```python
import random, bisect
from typing import List

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = {}
        for i, v in enumerate(arr):
            self.pos.setdefault(v, []).append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(25):
            idx = random.randint(left, right)
            cand = self.arr[idx]
            lst = self.pos[cand]
            cnt = bisect.bisect_right(lst, right) - bisect.bisect_left(lst, left)
            if cnt >= threshold:
                return cand
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_VAL 20000
#define ATTEMPTS 20

typedef struct {
    int *pos;
    int size;
    int cap;
} PosList;

struct MajorityChecker {
    int *arr;
    int n;
    PosList **lists; // array of pointers, index by value (0..MAX_VAL)
};

static void addPos(PosList ***listsPtr, int val, int idx) {
    PosList **lists = *listsPtr;
    if (!lists[val]) {
        lists[val] = (PosList *)malloc(sizeof(PosList));
        lists[val]->size = 0;
        lists[val]->cap = 4;
        lists[val]->pos = (int *)malloc(lists[val]->cap * sizeof(int));
    }
    PosList *pl = lists[val];
    if (pl->size == pl->cap) {
        pl->cap <<= 1;
        pl->pos = (int *)realloc(pl->pos, pl->cap * sizeof(int));
    }
    pl->pos[pl->size++] = idx;
}

static int lowerBound(int *a, int n, int target) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static int upperBound(int *a, int n, int target) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (a[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static int countInRange(PosList *pl, int left, int right) {
    int l = lowerBound(pl->pos, pl->size, left);
    int r = upperBound(pl->pos, pl->size, right);
    return r - l;
}

/** Initialize your data structure here. */
MajorityChecker* majorityCheckerCreate(int* arr, int arrSize) {
    srand((unsigned)time(NULL));
    MajorityChecker *obj = (MajorityChecker *)malloc(sizeof(MajorityChecker));
    obj->n = arrSize;
    obj->arr = (int *)malloc(arrSize * sizeof(int));
    memcpy(obj->arr, arr, arrSize * sizeof(int));

    obj->lists = (PosList **)calloc(MAX_VAL + 1, sizeof(PosList *));
    for (int i = 0; i < arrSize; ++i) {
        int val = arr[i];
        addPos(&obj->lists, val, i);
    }
    return obj;
}

/** Query majority element in [left, right] with given threshold. */
int majorityCheckerQuery(MajorityChecker* obj, int left, int right, int threshold) {
    for (int t = 0; t < ATTEMPTS; ++t) {
        int idx = left + rand() % (right - left + 1);
        int cand = obj->arr[idx];
        PosList *pl = obj->lists[cand];
        if (!pl) continue;
        int cnt = countInRange(pl, left, right);
        if (cnt >= threshold) return cand;
    }
    return -1;
}

void majorityCheckerFree(MajorityChecker* obj) {
    if (!obj) return;
    for (int i = 0; i <= MAX_VAL; ++i) {
        if (obj->lists[i]) {
            free(obj->lists[i]->pos);
            free(obj->lists[i]);
        }
    }
    free(obj->lists);
    free(obj->arr);
    free(obj);
}

/**
 * Your MajorityChecker struct will be instantiated and called as such:
 * MajorityChecker* obj = majorityCheckerCreate(arr, arrSize);
 * int param_1 = majorityCheckerQuery(obj, left, right, threshold);
 * majorityCheckerFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class MajorityChecker {
    private readonly int[] _arr;
    private readonly Dictionary<int, List<int>> _pos;
    private readonly Random _rand = new Random();

    public MajorityChecker(int[] arr) {
        _arr = arr;
        _pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < arr.Length; i++) {
            int v = arr[i];
            if (!_pos.ContainsKey(v)) _pos[v] = new List<int>();
            _pos[v].Add(i);
        }
    }

    public int Query(int left, int right, int threshold) {
        for (int attempt = 0; attempt < 20; attempt++) {
            int idx = left + _rand.Next(right - left + 1);
            int cand = _arr[idx];
            var list = _pos[cand];
            int cnt = UpperBound(list, right) - LowerBound(list, left);
            if (cnt >= threshold) return cand;
        }
        return -1;
    }

    private static int LowerBound(List<int> list, int target) {
        int lo = 0, hi = list.Count;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (list[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private static int UpperBound(List<int> list, int target) {
        int lo = 0, hi = list.Count;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (list[mid] > target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.Query(left,right,threshold);
 */
```

## Javascript

```javascript
var MajorityChecker = function(arr) {
    this.arr = arr;
    this.pos = new Map();
    for (let i = 0; i < arr.length; ++i) {
        const v = arr[i];
        if (!this.pos.has(v)) this.pos.set(v, []);
        this.pos.get(v).push(i);
    }
};

function lowerBound(a, target) {
    let l = 0, r = a.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (a[m] >= target) r = m;
        else l = m + 1;
    }
    return l;
}

function upperBound(a, target) {
    let l = 0, r = a.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (a[m] > target) r = m;
        else l = m + 1;
    }
    return l;
}

MajorityChecker.prototype.query = function(left, right, threshold) {
    for (let i = 0; i < 20; ++i) {
        const idx = left + Math.floor(Math.random() * (right - left + 1));
        const val = this.arr[idx];
        const list = this.pos.get(val);
        const cnt = upperBound(list, right) - lowerBound(list, left);
        if (cnt >= threshold) return val;
    }
    return -1;
};
```

## Typescript

```typescript
class MajorityChecker {
    private arr: number[];
    private posMap: Map<number, number[]>;

    constructor(arr: number[]) {
        this.arr = arr;
        this.posMap = new Map();
        for (let i = 0; i < arr.length; i++) {
            const v = arr[i];
            if (!this.posMap.has(v)) this.posMap.set(v, []);
            this.posMap.get(v)!.push(i);
        }
    }

    private countInRange(list: number[], left: number, right: number): number {
        // lower bound >= left
        let l = 0, r = list.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (list[m] < left) l = m + 1;
            else r = m;
        }
        const start = l;

        // upper bound > right
        l = 0; r = list.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (list[m] <= right) l = m + 1;
            else r = m;
        }
        const end = l;

        return end - start;
    }

    query(left: number, right: number, threshold: number): number {
        const attempts = 20;
        for (let i = 0; i < attempts; i++) {
            const idx = left + Math.floor(Math.random() * (right - left + 1));
            const cand = this.arr[idx];
            const list = this.posMap.get(cand)!;
            if (this.countInRange(list, left, right) >= threshold) return cand;
        }
        return -1;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = new MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */
```

## Php

```php
class MajorityChecker {
    private $arr = [];
    private $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        $this->arr = $arr;
        foreach ($arr as $idx => $val) {
            if (!isset($this->pos[$val])) {
                $this->pos[$val] = [];
            }
            $this->pos[$val][] = $idx;
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $threshold
     * @return Integer
     */
    function query($left, $right, $threshold) {
        for ($i = 0; $i < 20; $i++) {
            $randIdx = mt_rand($left, $right);
            $candidate = $this->arr[$randIdx];
            if (!isset($this->pos[$candidate])) continue;
            $list = $this->pos[$candidate];
            $cnt = $this->countInRange($list, $left, $right);
            if ($cnt >= $threshold) {
                return $candidate;
            }
        }
        return -1;
    }

    private function countInRange($list, $l, $r) {
        $leftIdx = $this->lowerBound($list, $l);
        $rightIdx = $this->upperBound($list, $r);
        return $rightIdx - $leftIdx;
    }

    // first index >= target
    private function lowerBound($arr, $target) {
        $low = 0;
        $high = count($arr);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] < $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return $low;
    }

    // first index > target
    private function upperBound($arr, $target) {
        $low = 0;
        $high = count($arr);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] <= $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return $low;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * $obj = new MajorityChecker($arr);
 * $ret_1 = $obj->query($left, $right, $threshold);
 */
```

## Swift

```swift
import Foundation

class MajorityChecker {
    private var arr: [Int]
    private var indices: [Int: [Int]]
    
    init(_ arr: [Int]) {
        self.arr = arr
        self.indices = [:]
        for (i, v) in arr.enumerated() {
            indices[v, default: []].append(i)
        }
    }
    
    func query(_ left: Int, _ right: Int, _ threshold: Int) -> Int {
        let trials = 20
        for _ in 0..<trials {
            let randIdx = Int.random(in: left...right)
            let val = arr[randIdx]
            if let list = indices[val] {
                let cnt = countInRange(list, left, right)
                if cnt >= threshold {
                    return val
                }
            }
        }
        return -1
    }
    
    private func countInRange(_ list: [Int], _ left: Int, _ right: Int) -> Int {
        let l = lowerBound(list, left)
        let r = upperBound(list, right)
        return r - l
    }
    
    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var lo = 0
        var hi = arr.count
        while lo < hi {
            let mid = (lo + hi) >> 1
            if arr[mid] < target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
    
    private func upperBound(_ arr: [Int], _ target: Int) -> Int {
        var lo = 0
        var hi = arr.count
        while lo < hi {
            let mid = (lo + hi) >> 1
            if arr[mid] <= target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}
```

## Kotlin

```kotlin
import java.util.Random
import kotlin.math.max

class MajorityChecker(arr: IntArray) {
    private val nums = arr
    private val positions = HashMap<Int, MutableList<Int>>()
    private val rand = Random()

    init {
        for (i in nums.indices) {
            positions.computeIfAbsent(nums[i]) { mutableListOf() }.add(i)
        }
    }

    fun query(left: Int, right: Int, threshold: Int): Int {
        repeat(20) {
            val idx = left + rand.nextInt(right - left + 1)
            val candidate = nums[idx]
            val list = positions[candidate] ?: return@repeat
            if (countInRange(list, left, right) >= threshold) {
                return candidate
            }
        }
        return -1
    }

    private fun countInRange(list: List<Int>, l: Int, r: Int): Int {
        val lo = lowerBound(list, l)
        val hi = upperBound(list, r)
        return hi - lo
    }

    private fun lowerBound(list: List<Int>, target: Int): Int {
        var low = 0
        var high = list.size
        while (low < high) {
            val mid = (low + high) ushr 1
            if (list[mid] >= target) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun upperBound(list: List<Int>, target: Int): Int {
        var low = 0
        var high = list.size
        while (low < high) {
            val mid = (low + high) ushr 1
            if (list[mid] > target) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */
```

## Dart

```dart
class MajorityChecker {
  late List<int> _arr;
  late int _n;
  late Map<int, List<int>> _posMap;
  late List<int> _candTree;
  late List<int> _cntTree;

  MajorityChecker(List<int> arr) {
    _arr = arr;
    _n = arr.length;
    _posMap = {};
    for (int i = 0; i < _n; ++i) {
      int v = arr[i];
      (_posMap[v] ??= []).add(i);
    }
    _candTree = List.filled(_n * 4, 0);
    _cntTree = List.filled(_n * 4, 0);
    _build(1, 0, _n - 1);
  }

  int query(int left, int right, int threshold) {
    var node = _query(1, 0, _n - 1, left, right);
    int cand = node.cand;
    var positions = _posMap[cand];
    if (positions == null) return -1;
    int occ = _countInRange(positions, left, right);
    return occ >= threshold ? cand : -1;
  }

  void _build(int idx, int l, int r) {
    if (l == r) {
      _candTree[idx] = _arr[l];
      _cntTree[idx] = 1;
      return;
    }
    int mid = (l + r) >> 1;
    _build(idx << 1, l, mid);
    _build(idx << 1 | 1, mid + 1, r);
    _merge(idx);
  }

  void _merge(int idx) {
    int leftIdx = idx << 1;
    int rightIdx = idx << 1 | 1;
    int lc = _candTree[leftIdx];
    int lcnt = _cntTree[leftIdx];
    int rc = _candTree[rightIdx];
    int rcnt = _cntTree[rightIdx];
    if (lc == rc) {
      _candTree[idx] = lc;
      _cntTree[idx] = lcnt + rcnt;
    } else if (lcnt > rcnt) {
      _candTree[idx] = lc;
      _cntTree[idx] = lcnt - rcnt;
    } else {
      _candTree[idx] = rc;
      _cntTree[idx] = rcnt - lcnt;
    }
  }

  _Node _query(int idx, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return _Node(_candTree[idx], _cntTree[idx]);
    int mid = (l + r) >> 1;
    if (qr <= mid) return _query(idx << 1, l, mid, ql, qr);
    if (ql > mid) return _query(idx << 1 | 1, mid + 1, r, ql, qr);
    var leftNode = _query(idx << 1, l, mid, ql, qr);
    var rightNode = _query(idx << 1 | 1, mid + 1, r, ql, qr);
    if (leftNode.cand == rightNode.cand) {
      return _Node(leftNode.cand, leftNode.cnt + rightNode.cnt);
    } else if (leftNode.cnt > rightNode.cnt) {
      return _Node(leftNode.cand, leftNode.cnt - rightNode.cnt);
    } else {
      return _Node(rightNode.cand, rightNode.cnt - leftNode.cnt);
    }
  }

  int _countInRange(List<int> list, int left, int right) {
    int lIdx = _lowerBound(list, left);
    int rIdx = _upperBound(list, right);
    return rIdx - lIdx;
  }

  int _lowerBound(List<int> list, int target) {
    int lo = 0, hi = list.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (list[mid] < target)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo;
  }

  int _upperBound(List<int> list, int target) {
    int lo = 0, hi = list.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (list[mid] <= target)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo;
  }
}

class _Node {
  final int cand;
  final int cnt;
  _Node(this.cand, this.cnt);
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = MajorityChecker(arr);
 * int param1 = obj.query(left,right,threshold);
 */
```

## Golang

```go
type nodeInfo struct {
	cand int
	cnt  int
}

type MajorityChecker struct {
	arr []int
	seg []nodeInfo
	pos map[int][]int
}

func Constructor(arr []int) MajorityChecker {
	mc := MajorityChecker{
		arr: make([]int, len(arr)),
		seg: make([]nodeInfo, 4*len(arr)),
		pos: make(map[int][]int),
	}
	copy(mc.arr, arr)
	for i, v := range arr {
		mc.pos[v] = append(mc.pos[v], i)
	}
	if len(arr) > 0 {
		mc.build(1, 0, len(arr)-1)
	}
	return mc
}

func (this *MajorityChecker) Query(left int, right int, threshold int) int {
	candidate := this.querySeg(1, 0, len(this.arr)-1, left, right).cand
	if candidate == 0 && len(this.pos[candidate]) == 0 {
		return -1
	}
	indices := this.pos[candidate]
	cnt := upperBound(indices, right) - lowerBound(indices, left)
	if cnt >= threshold {
		return candidate
	}
	return -1
}

func (this *MajorityChecker) build(node, l, r int) {
	if l == r {
		this.seg[node] = nodeInfo{cand: this.arr[l], cnt: 1}
		return
	}
	mid := (l + r) >> 1
	this.build(node<<1, l, mid)
	this.build(node<<1|1, mid+1, r)
	this.seg[node] = merge(this.seg[node<<1], this.seg[node<<1|1])
}

func (this *MajorityChecker) querySeg(node, l, r, ql, qr int) nodeInfo {
	if ql <= l && r <= qr {
		return this.seg[node]
	}
	mid := (l + r) >> 1
	if qr <= mid {
		return this.querySeg(node<<1, l, mid, ql, qr)
	}
	if ql > mid {
		return this.querySeg(node<<1|1, mid+1, r, ql, qr)
	}
	leftRes := this.querySeg(node<<1, l, mid, ql, qr)
	rightRes := this.querySeg(node<<1|1, mid+1, r, ql, qr)
	return merge(leftRes, rightRes)
}

func merge(a, b nodeInfo) nodeInfo {
	if a.cand == b.cand {
		return nodeInfo{cand: a.cand, cnt: a.cnt + b.cnt}
	}
	if a.cnt > b.cnt {
		return nodeInfo{cand: a.cand, cnt: a.cnt - b.cnt}
	}
	return nodeInfo{cand: b.cand, cnt: b.cnt - a.cnt}
}

func lowerBound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		m := (l + r) >> 1
		if arr[m] < target {
			l = m + 1
		} else {
			r = m
		}
	}
	return l
}

func upperBound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		m := (l + r) >> 1
		if arr[m] <= target {
			l = m + 1
		} else {
			r = m
		}
	}
	return l
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,threshold);
 */
```

## Ruby

```ruby
class MajorityChecker
  # :type arr: Integer[]
  def initialize(arr)
    @arr = arr
    @n = arr.length
    @pos = Hash.new { |h, k| h[k] = [] }
    arr.each_with_index { |v, i| @pos[v] << i }

    size = @n * 4
    @tree_val = Array.new(size)
    @tree_cnt = Array.new(size)
    build(1, 0, @n - 1)
  end

  # :type left: Integer
  # :type right: Integer
  # :type threshold: Integer
  # :rtype: Integer
  def query(left, right, threshold)
    cand, _ = query_range(1, 0, @n - 1, left, right)
    list = @pos[cand] || []
    occ = count_in_range(list, left, right)
    occ >= threshold ? cand : -1
  end

  private

  def build(node, l, r)
    if l == r
      @tree_val[node] = @arr[l]
      @tree_cnt[node] = 1
    else
      mid = (l + r) / 2
      build(node * 2, l, mid)
      build(node * 2 + 1, mid + 1, r)
      v1 = @tree_val[node * 2]
      c1 = @tree_cnt[node * 2]
      v2 = @tree_val[node * 2 + 1]
      c2 = @tree_cnt[node * 2 + 1]
      merged = merge(v1, c1, v2, c2)
      @tree_val[node] = merged[0]
      @tree_cnt[node] = merged[1]
    end
  end

  def query_range(node, l, r, ql, qr)
    return [0, 0] if qr < l || r < ql
    return [@tree_val[node], @tree_cnt[node]] if ql <= l && r <= qr

    mid = (l + r) / 2
    left_res = query_range(node * 2, l, mid, ql, qr)
    right_res = query_range(node * 2 + 1, mid + 1, r, ql, qr)
    merge(left_res[0], left_res[1], right_res[0], right_res[1])
  end

  def merge(val1, cnt1, val2, cnt2)
    return [val2, cnt2] if cnt1 == 0
    return [val1, cnt1] if cnt2 == 0
    if val1 == val2
      [val1, cnt1 + cnt2]
    elsif cnt1 > cnt2
      [val1, cnt1 - cnt2]
    else
      [val2, cnt2 - cnt1]
    end
  end

  def count_in_range(arr, left, right)
    l_idx = lower_bound(arr, left)
    r_idx = upper_bound(arr, right)
    r_idx - l_idx
  end

  def lower_bound(arr, target)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  def upper_bound(arr, target)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker.new(arr)
# param_1 = obj.query(left, right, threshold)
```

## Scala

```scala
import scala.collection.mutable
import scala.util.Random
import scala.collection.Searching._

class MajorityChecker(_arr: Array[Int]) {

  private val arr = _arr
  private val tempMap = mutable.Map[Int, mutable.ArrayBuffer[Int]]()
  for (i <- arr.indices) {
    val v = arr(i)
    tempMap.getOrElseUpdate(v, mutable.ArrayBuffer[Int]()) += i
  }
  private val posMap: Map[Int, Array[Int]] = tempMap.view.mapValues(_.toArray).toMap

  private val rand = new Random()

  def query(left: Int, right: Int, threshold: Int): Int = {
    var attempts = 20
    while (attempts > 0) {
      val idx = left + rand.nextInt(right - left + 1)
      val cand = arr(idx)
      val positions = posMap(cand)

      val lo = positions.search(left) match {
        case Found(i) => i
        case InsertionPoint(i) => i
      }
      val hi = positions.search(right) match {
        case Found(i) => i + 1
        case InsertionPoint(i) => i
      }

      if (hi - lo >= threshold) return cand

      attempts -= 1
    }
    -1
  }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * val obj = new MajorityChecker(arr)
 * val param_1 = obj.query(left,right,threshold)
 */
```

## Rust

```rust
use std::collections::HashMap;

pub struct MajorityChecker {
    arr: Vec<i32>,
    pos: HashMap<i32, Vec<usize>>,
}

impl MajorityChecker {
    pub fn new(arr: Vec<i32>) -> Self {
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            map.entry(v).or_insert_with(Vec::new).push(i);
        }
        MajorityChecker { arr, pos: map }
    }

    pub fn query(&self, left: i32, right: i32, threshold: i32) -> i32 {
        let l = left as usize;
        let r = right as usize;
        let len = r - l + 1;
        let attempts = if len < 20 { len } else { 20 };
        // simple deterministic pseudo‑random generator
        let mut rng: u64 = (left as u64).wrapping_mul(1234567).wrapping_add(right as u64);
        for _ in 0..attempts {
            let offset = (rng % (len as u64)) as usize;
            let idx = l + offset;
            rng = rng.wrapping_mul(6364136223846793005).wrapping_add(1);
            let val = self.arr[idx];
            if let Some(vec) = self.pos.get(&val) {
                // count occurrences of val in [l, r] using binary search
                let left_idx = vec.partition_point(|&x| x < l);
                let right_idx = vec.partition_point(|&x| x <= r);
                let cnt = (right_idx - left_idx) as i32;
                if cnt >= threshold {
                    return val;
                }
            }
        }
        -1
    }
}

/*
Your MajorityChecker object will be instantiated and called as such:
let obj = MajorityChecker::new(arr);
let ret_1: i32 = obj.query(left, right, threshold);
*/
```

## Racket

```racket
(define majority-checker%
  (class object%
    (super-new)
    
    ; arr : (listof exact-integer?)
    (init-field arr)
    
    ;; Convert array to vector for O(1) indexing
    (define arr-vec (list->vector arr))
    
    ;; Build hash: value -> sorted vector of indices where it appears
    (define temp-hash (make-hash))
    (for ([i (in-range (vector-length arr-vec))])
      (let* ((v (vector-ref arr-vec i))
             (lst (hash-ref temp-hash v '())))
        (hash-set! temp-hash v (cons i lst))))
    
    (define positions (make-hash))
    (for ([kv (in-hash temp-hash)])
      (let* ((val (car kv))
             (idx-list (reverse (cdr kv))) ; make ascending
             (vec (list->vector idx-list)))
        (hash-set! positions val vec)))
    
    ;; binary search: first index >= target
    (define (lower-bound vec target)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (midval (vector-ref vec mid)))
              (if (< midval target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    
    ;; binary search: first index > target
    (define (upper-bound vec target)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (midval (vector-ref vec mid)))
              (if (<= midval target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    
    ; query : exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (query left right threshold)
      (let ((range-len (+ 1 (- right left))))
        (let loop ((attempt 0))
          (if (= attempt 20)
              -1
              (let* ((rand-idx (+ left (random range-len)))
                     (val (vector-ref arr-vec rand-idx))
                     (vec (hash-ref positions val #f)))
                (if (and vec
                         (>= (- (upper-bound vec right)
                                (lower-bound vec left))
                             threshold))
                    val
                    (loop (+ attempt 1)))))))))
)
```

## Erlang

```erlang
-module(majoritychecker).
-export([majority_checker_init_/1, majority_checker_query/3]).

%% Initialize with the array.
-spec majority_checker_init_(Arr :: [integer()]) -> any().
majority_checker_init_(Arr) ->
    %% Store array as tuple for O(1) access
    ArrTuple = list_to_tuple(Arr),
    put(arr_tuple, ArrTuple),

    %% Build map from value to reversed position list
    PosMapRev = build_pos_map(Arr, 0, #{}),

    %% Reverse each list and convert to tuple
    PosMap = maps:fold(
        fun(_Key, RevList, Acc) ->
            Tuple = list_to_tuple(lists:reverse(RevList)),
            maps:put(_Key, Tuple, Acc)
        end,
        #{},
        PosMapRev),

    put(pos_map, PosMap),

    %% Seed random generator
    {A1,A2,A3} = erlang:monotonic_time(),
    rand:seed(sfmt, {A1 rem 1000000, A2 rem 1000000, A3 rem 1000000}),
    ok.

%% Query for majority element in subarray [Left, Right] with given Threshold.
-spec majority_checker_query(Left :: integer(), Right :: integer(), Threshold :: integer()) -> integer().
majority_checker_query(Left, Right, Threshold) ->
    PosMap = get(pos_map),
    ArrTuple = get(arr_tuple),
    Len = Right - Left + 1,
    Trials = 20,
    query_trials(Trials, Left, Right, Threshold, PosMap, ArrTuple).

%% Helper to perform a number of random trials.
query_trials(0, _L, _R, _T, _PosMap, _Arr) ->
    -1;
query_trials(N, L, R, T, PosMap, ArrTuple) ->
    RandIdx = L + rand:uniform(R - L + 1) - 1,
    Candidate = element(RandIdx + 1, ArrTuple),
    case maps:get(Candidate, PosMap, undefined) of
        undefined ->
            query_trials(N - 1, L, R, T, PosMap, ArrTuple);
        PosTuple ->
            Count = count_in_range(PosTuple, L, R),
            if
                Count >= T -> Candidate;
                true -> query_trials(N - 1, L, R, T, PosMap, ArrTuple)
            end
    end.

%% Build map of value => reversed list of positions.
build_pos_map([], _Idx, Acc) ->
    Acc;
build_pos_map([H|T], Idx, Acc) ->
    Updated = maps:update_with(H,
                               fun(L) -> [Idx|L] end,
                               [Idx],
                               Acc),
    build_pos_map(T, Idx + 1, Updated).

%% Count occurrences of a value whose positions are stored in PosTuple within [L,R].
count_in_range(PosTuple, L, R) ->
    Size = tuple_size(PosTuple),
    Lower = lower_bound(PosTuple, 1, Size, L),
    Upper = upper_bound(PosTuple, 1, Size, R),
    Upper - Lower.

%% First index with element >= Target (1‑based). Returns Size+1 if none.
lower_bound(_Tuple, Low, High, _Target) when Low > High ->
    Low;
lower_bound(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    Val = element(Mid, Tuple),
    if
        Val >= Target -> lower_bound(Tuple, Low, Mid - 1, Target);
        true -> lower_bound(Tuple, Mid + 1, High, Target)
    end.

%% First index with element > Target (1‑based). Returns Size+1 if none.
upper_bound(_Tuple, Low, High, _Target) when Low > High ->
    Low;
upper_bound(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    Val = element(Mid, Tuple),
    if
        Val > Target -> upper_bound(Tuple, Low, Mid - 1, Target);
        true -> upper_bound(Tuple, Mid + 1, High, Target)
    end.
```

## Elixir

```elixir
defmodule MajorityChecker do
  @spec init_(arr :: [integer]) :: any
  def init_(arr) do
    pos_map =
      Enum.with_index(arr)
      |> Enum.reduce(%{}, fn {v, i}, acc ->
        Map.update(acc, v, [i], &[i | &1])
      end)
      |> Enum.map(fn {k, vlist} -> {k, Enum.reverse(vlist)} end)
      |> Enum.into(%{})

    Process.put(:mc_data, {arr, pos_map})
    :ok
  end

  @spec query(left :: integer, right :: integer, threshold :: integer) :: integer
  def query(left, right, threshold) do
    {arr, pos_map} = Process.get(:mc_data)
    len = right - left + 1
    max_trials = 20

    Enum.reduce_while(1..max_trials, -1, fn _, _acc ->
      idx = left + :rand.uniform(len) - 1
      val = Enum.at(arr, idx)

      positions = Map.get(pos_map, val, [])
      cnt = count_in_range(positions, left, right)

      if cnt >= threshold do
        {:halt, val}
      else
        {:cont, -1}
      end
    end)
  end

  defp count_in_range(list, l, r) do
    lo = lower_bound(list, l)
    hi = upper_bound(list, r)
    hi - lo
  end

  defp lower_bound(list, target), do: bound(list, target, fn v -> v < target end)

  defp upper_bound(list, target), do: bound(list, target, fn v -> v <= target end)

  defp bound(list, target, cmp) do
    do_bound(list, 0, length(list), target, cmp)
  end

  defp do_bound(_list, low, high, _target, _cmp) when low >= high, do: low

  defp do_bound(list, low, high, target, cmp) do
    mid = div(low + high, 2)

    case Enum.at(list, mid) do
      nil ->
        low

      val ->
        if cmp.(val) do
          do_bound(list, mid + 1, high, target, cmp)
        else
          do_bound(list, low, mid, target, cmp)
        end
    end
  end
end
```
