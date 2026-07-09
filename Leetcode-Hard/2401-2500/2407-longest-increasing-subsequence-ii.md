# 2407. Longest Increasing Subsequence II

## Cpp

```cpp
class Solution {
public:
    struct SegTree {
        int n;
        std::vector<int> t;
        SegTree(int sz) {
            n = 1;
            while (n < sz) n <<= 1;
            t.assign(2 * n, 0);
        }
        void update(int pos, int val) {
            pos += n;
            if (t[pos] >= val) return;
            t[pos] = val;
            for (pos >>= 1; pos; pos >>= 1)
                t[pos] = std::max(t[pos << 1], t[(pos << 1) | 1]);
        }
        int query(int l, int r) { // inclusive
            if (l > r) return 0;
            l += n;
            r += n;
            int res = 0;
            while (l <= r) {
                if (l & 1) res = std::max(res, t[l++]);
                if (!(r & 1)) res = std::max(res, t[r--]);
                l >>= 1;
                r >>= 1;
            }
            return res;
        }
    };
    
    int lengthOfLIS(std::vector<int>& nums, int k) {
        int maxVal = *std::max_element(nums.begin(), nums.end());
        SegTree seg(maxVal + 2); // enough for index up to maxVal
        int ans = 0;
        for (int x : nums) {
            int l = std::max(1, x - k);
            int r = x - 1;
            int best = seg.query(l, r);
            int cur = best + 1;
            seg.update(x, cur);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int lengthOfLIS(int[] nums, int k) {
        int maxVal = 100000; // given constraint for nums[i]
        int size = 1;
        while (size <= maxVal) size <<= 1;
        int[] seg = new int[2 * size];

        java.util.function.BiFunction<Integer, Integer, Integer> query = (l, r) -> {
            int res = 0;
            int left = l + size;
            int right = r + size;
            while (left <= right) {
                if ((left & 1) == 1) {
                    res = Math.max(res, seg[left]);
                    left++;
                }
                if ((right & 1) == 0) {
                    res = Math.max(res, seg[right]);
                    right--;
                }
                left >>= 1;
                right >>= 1;
            }
            return res;
        };

        java.util.function.BiConsumer<Integer, Integer> update = (pos, val) -> {
            int idx = pos + size;
            if (seg[idx] >= val) return;
            seg[idx] = val;
            for (idx >>= 1; idx > 0; idx >>= 1) {
                seg[idx] = Math.max(seg[2 * idx], seg[2 * idx + 1]);
            }
        };

        int answer = 0;
        for (int v : nums) {
            int l = Math.max(1, v - k);
            int r = v - 1;
            int best = 0;
            if (l <= r) {
                best = query.apply(l, r);
            }
            int cur = best + 1;
            answer = Math.max(answer, cur);
            update.accept(v, cur);
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        max_val = max(nums)
        M = max_val + 1  # values are >=1, we use index directly
        size = 1
        while size < M:
            size <<= 1
        tree = [0] * (2 * size)

        def query(l, r):
            if l > r:
                return 0
            l += size
            r += size
            res = 0
            while l <= r:
                if l & 1:
                    if tree[l] > res:
                        res = tree[l]
                    l += 1
                if not (r & 1):
                    if tree[r] > res:
                        res = tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def update(pos, val):
            pos += size
            if val <= tree[pos]:
                return
            tree[pos] = val
            pos >>= 1
            while pos:
                new_val = tree[pos << 1]
                if tree[(pos << 1) | 1] > new_val:
                    new_val = tree[(pos << 1) | 1]
                if new_val == tree[pos]:
                    break
                tree[pos] = new_val
                pos >>= 1

        ans = 0
        for x in nums:
            l = max(0, x - k)
            r = x - 1
            best = query(l, r)
            cur = best + 1
            if cur > ans:
                ans = cur
            update(x, cur)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        size = 1
        while size <= max_val:
            size <<= 1
        seg = [0] * (2 * size)

        def query(l: int, r: int) -> int:
            if l > r:
                return 0
            l += size
            r += size
            res = 0
            while l <= r:
                if l & 1:
                    if seg[l] > res:
                        res = seg[l]
                    l += 1
                if not (r & 1):
                    if seg[r] > res:
                        res = seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def update(pos: int, val: int) -> None:
            pos += size
            if seg[pos] >= val:
                return
            seg[pos] = val
            pos >>= 1
            while pos:
                new_val = seg[pos << 1]
                if seg[(pos << 1) | 1] > new_val:
                    new_val = seg[(pos << 1) | 1]
                if seg[pos] == new_val:
                    break
                seg[pos] = new_val
                pos >>= 1

        ans = 0
        for v in nums:
            l = max(1, v - k)
            r = v - 1
            best = query(l, r)
            cur = best + 1
            if cur > ans:
                ans = cur
            update(v, cur)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MAXV 100000

static int seg[4 * (MAXV + 5)];

static void segUpdate(int node, int l, int r, int idx, int val) {
    if (l == r) {
        if (val > seg[node]) seg[node] = val;
        return;
    }
    int mid = (l + r) >> 1;
    if (idx <= mid)
        segUpdate(node << 1, l, mid, idx, val);
    else
        segUpdate(node << 1 | 1, mid + 1, r, idx, val);
    seg[node] = seg[node << 1] > seg[node << 1 | 1] ? seg[node << 1] : seg[node << 1 | 1];
}

static int segQuery(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return seg[node];
    int mid = (l + r) >> 1;
    int left = segQuery(node << 1, l, mid, ql, qr);
    int right = segQuery(node << 1 | 1, mid + 1, r, ql, qr);
    return left > right ? left : right;
}

int lengthOfLIS(int* nums, int numsSize, int k) {
    memset(seg, 0, sizeof(seg));
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int left = x - k;
        if (left < 1) left = 1;
        int right = x - 1;
        int best = 0;
        if (left <= right)
            best = segQuery(1, 1, MAXV, left, right);
        int cur = best + 1;
        segUpdate(1, 1, MAXV, x, cur);
        if (cur > ans) ans = cur;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LengthOfLIS(int[] nums, int k) {
        if (nums == null || nums.Length == 0) return 0;
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;
        var seg = new SegmentTree(maxVal);
        int answer = 0;
        foreach (int num in nums) {
            int left = Math.Max(1, num - k);
            int right = num - 1;
            int best = (left <= right) ? seg.Query(left, right) : 0;
            int cur = best + 1;
            seg.Update(num, cur);
            if (cur > answer) answer = cur;
        }
        return answer;
    }

    private class SegmentTree {
        private readonly int size;
        private readonly int[] tree;

        public SegmentTree(int n) {
            size = n;
            tree = new int[4 * n];
        }

        public void Update(int idx, int val) {
            Update(1, 1, size, idx, val);
        }

        private void Update(int node, int l, int r, int idx, int val) {
            if (l == r) {
                if (val > tree[node]) tree[node] = val;
                return;
            }
            int mid = (l + r) >> 1;
            if (idx <= mid) Update(node << 1, l, mid, idx, val);
            else Update(node << 1 | 1, mid + 1, r, idx, val);
            tree[node] = Math.Max(tree[node << 1], tree[node << 1 | 1]);
        }

        public int Query(int L, int R) {
            if (L > R) return 0;
            return Query(1, 1, size, L, R);
        }

        private int Query(int node, int l, int r, int L, int R) {
            if (R < l || r < L) return 0;
            if (L <= l && r <= R) return tree[node];
            int mid = (l + r) >> 1;
            int leftMax = Query(node << 1, l, mid, L, R);
            int rightMax = Query(node << 1 | 1, mid + 1, r, L, R);
            return Math.Max(leftMax, rightMax);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var lengthOfLIS = function(nums, k) {
    // maximum possible value in nums
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    // segment tree size (next power of two)
    let N = 1;
    while (N <= maxVal) N <<= 1;
    const seg = new Int32Array(2 * N); // all zeros

    const update = (pos, val) => {
        // pos is the value (1-indexed)
        let idx = pos + N - 1;
        if (seg[idx] >= val) return; // no need to update
        seg[idx] = val;
        for (idx >>= 1; idx > 0; idx >>= 1) {
            const left = seg[idx << 1];
            const right = seg[(idx << 1) | 1];
            seg[idx] = left > right ? left : right;
        }
    };

    const query = (l, r) => {
        if (l > r) return 0;
        let res = 0;
        let left = l + N - 1;
        let right = r + N - 1;
        while (left <= right) {
            if ((left & 1) === 1) {
                if (seg[left] > res) res = seg[left];
                left++;
            }
            if ((right & 1) === 0) {
                if (seg[right] > res) res = seg[right];
                right--;
            }
            left >>= 1;
            right >>= 1;
        }
        return res;
    };

    let answer = 0;
    for (const x of nums) {
        const l = Math.max(1, x - k);
        const r = x - 1;
        const bestPrev = query(l, r);
        const cur = bestPrev + 1;
        update(x, cur);
        if (cur > answer) answer = cur;
    }
    return answer;
};
```

## Typescript

```typescript
function lengthOfLIS(nums: number[], k: number): number {
    const MAX_VAL = 100000;
    let size = 1;
    while (size <= MAX_VAL) size <<= 1;
    const seg = new Array(size * 2).fill(0);

    const update = (pos: number, val: number): void => {
        pos += size;
        if (seg[pos] >= val) return;
        seg[pos] = val;
        for (pos >>= 1; pos > 0; pos >>= 1) {
            const newVal = Math.max(seg[pos << 1], seg[(pos << 1) | 1]);
            if (seg[pos] === newVal) break;
            seg[pos] = newVal;
        }
    };

    const query = (l: number, r: number): number => {
        let res = 0;
        l += size;
        r += size;
        while (l <= r) {
            if ((l & 1) === 1) {
                res = Math.max(res, seg[l]);
                l++;
            }
            if ((r & 1) === 0) {
                res = Math.max(res, seg[r]);
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    };

    let answer = 0;
    for (const v of nums) {
        const left = Math.max(0, v - k);
        const right = v - 1;
        const bestPrev = left <= right ? query(left, right) : 0;
        const cur = bestPrev + 1;
        update(v, cur);
        if (cur > answer) answer = cur;
    }
    return answer;
}
```

## Php

```php
class SegmentTree {
    public int $size;
    public array $tree;

    public function __construct(int $n) {
        $this->size = $n;
        $this->tree = array_fill(0, 4 * $n + 5, 0);
    }

    public function queryRange(int $node, int $l, int $r, int $ql, int $qr): int {
        if ($ql > $r || $qr < $l) {
            return 0;
        }
        if ($ql <= $l && $r <= $qr) {
            return $this->tree[$node];
        }
        $mid = intdiv($l + $r, 2);
        $left = $this->queryRange($node * 2, $l, $mid, $ql, $qr);
        $right = $this->queryRange($node * 2 + 1, $mid + 1, $r, $ql, $qr);
        return max($left, $right);
    }

    public function updatePoint(int $node, int $l, int $r, int $pos, int $value): void {
        if ($l == $r) {
            if ($value > $this->tree[$node]) {
                $this->tree[$node] = $value;
            }
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($pos <= $mid) {
            $this->updatePoint($node * 2, $l, $mid, $pos, $value);
        } else {
            $this->updatePoint($node * 2 + 1, $mid + 1, $r, $pos, $value);
        }
        $this->tree[$node] = max($this->tree[$node * 2], $this->tree[$node * 2 + 1]);
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function lengthOfLIS($nums, $k) {
        if (empty($nums)) return 0;
        $maxVal = max($nums);
        $seg = new SegmentTree($maxVal);
        $ans = 0;

        foreach ($nums as $num) {
            $left = $num - $k;
            if ($left < 1) $left = 1;
            $right = $num - 1;
            $best = 0;
            if ($right >= $left) {
                $best = $seg->queryRange(1, 1, $maxVal, $left, $right);
            }
            $cur = $best + 1;
            $seg->updatePoint(1, 1, $maxVal, $num, $cur);
            if ($cur > $ans) $ans = $cur;
        }

        return $ans;
    }
}
```

## Swift

```swift
class SegmentTree {
    private var n: Int
    private var tree: [Int]

    init(_ size: Int) {
        n = 1
        while n < size { n <<= 1 }
        tree = Array(repeating: 0, count: 2 * n)
    }

    func update(_ index: Int, _ value: Int) {
        var i = index + n
        if value <= tree[i] { return }
        tree[i] = value
        i >>= 1
        while i >= 1 {
            let newVal = max(tree[2 * i], tree[2 * i + 1])
            if newVal == tree[i] { break }
            tree[i] = newVal
            i >>= 1
        }
    }

    func query(_ l: Int, _ r: Int) -> Int {
        var left = l + n
        var right = r + n
        var res = 0
        while left <= right {
            if (left & 1) == 1 {
                res = max(res, tree[left])
                left += 1
            }
            if (right & 1) == 0 {
                res = max(res, tree[right])
                right -= 1
            }
            left >>= 1
            right >>= 1
        }
        return res
    }
}

class Solution {
    func lengthOfLIS(_ nums: [Int], _ k: Int) -> Int {
        guard let maxVal = nums.max() else { return 0 }
        let seg = SegmentTree(maxVal + 2)
        var answer = 0

        for v in nums {
            let left = max(1, v - k)
            let right = v - 1
            var best = 0
            if left <= right {
                best = seg.query(left, right)
            }
            let cur = best + 1
            seg.update(v, cur)
            answer = max(answer, cur)
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthOfLIS(nums: IntArray, k: Int): Int {
        if (nums.isEmpty()) return 0
        val maxVal = nums.maxOrNull() ?: 0
        val seg = SegmentTree(maxVal + 1)
        var answer = 0
        for (num in nums) {
            val left = if (num - k < 0) 0 else num - k
            val right = num - 1
            var best = 0
            if (left <= right) {
                best = seg.query(left, right)
            }
            val cur = best + 1
            val existing = seg.query(num, num)
            if (cur > existing) {
                seg.update(num, cur)
            }
            if (cur > answer) answer = cur
        }
        return answer
    }

    private class SegmentTree(size: Int) {
        private val n = size
        private val tree = IntArray(4 * n)

        fun update(idx: Int, value: Int) {
            update(1, 0, n - 1, idx, value)
        }

        private fun update(node: Int, l: Int, r: Int, idx: Int, value: Int) {
            if (l == r) {
                if (value > tree[node]) tree[node] = value
                return
            }
            val mid = (l + r) ushr 1
            if (idx <= mid) update(node shl 1, l, mid, idx, value)
            else update(node shl 1 or 1, mid + 1, r, idx, value)
            tree[node] = kotlin.math.max(tree[node shl 1], tree[node shl 1 or 1])
        }

        fun query(qL: Int, qR: Int): Int {
            if (qL > qR) return 0
            return query(1, 0, n - 1, qL, qR)
        }

        private fun query(node: Int, l: Int, r: Int, qL: Int, qR: Int): Int {
            if (qL <= l && r <= qR) return tree[node]
            val mid = (l + r) ushr 1
            var res = 0
            if (qL <= mid) res = kotlin.math.max(res, query(node shl 1, l, mid, qL, qR))
            if (qR > mid) res = kotlin.math.max(res, query(node shl 1 or 1, mid + 1, r, qL, qR))
            return res
        }
    }
}
```

## Dart

```dart
class Solution {
  int lengthOfLIS(List<int> nums, int k) {
    const int MAXV = 100000;
    int size = 1;
    while (size <= MAXV) size <<= 1;
    List<int> seg = List.filled(2 * size, 0);

    void update(int pos, int val) {
      pos += size;
      if (seg[pos] >= val) return;
      seg[pos] = val;
      for (pos >>= 1; pos >= 1; pos >>= 1) {
        int left = seg[pos << 1];
        int right = seg[(pos << 1) + 1];
        seg[pos] = left > right ? left : right;
      }
    }

    int query(int l, int r) {
      if (l > r) return 0;
      l += size;
      r += size;
      int res = 0;
      while (l <= r) {
        if ((l & 1) == 1) {
          if (seg[l] > res) res = seg[l];
          l++;
        }
        if ((r & 1) == 0) {
          if (seg[r] > res) res = seg[r];
          r--;
        }
        l >>= 1;
        r >>= 1;
      }
      return res;
    }

    int ans = 0;
    for (int num in nums) {
      int left = num - k;
      if (left < 1) left = 1;
      int right = num - 1;
      int best = query(left, right);
      int cur = best + 1;
      update(num, cur);
      if (cur > ans) ans = cur;
    }
    return ans;
  }
}
```

## Golang

```go
func lengthOfLIS(nums []int, k int) int {
    if len(nums) == 0 {
        return 0
    }
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }
    // segment tree over [1..maxVal]
    type SegTree struct {
        n    int
        data []int
    }
    var newSegTree func(int) *SegTree
    newSegTree = func(n int) *SegTree {
        return &SegTree{
            n:    n,
            data: make([]int, 4*n+5),
        }
    }
    var update func(node, l, r, pos, val int, st *SegTree)
    update = func(node, l, r, pos, val int, st *SegTree) {
        if l == r {
            if val > st.data[node] {
                st.data[node] = val
            }
            return
        }
        mid := (l + r) >> 1
        if pos <= mid {
            update(node<<1, l, mid, pos, val, st)
        } else {
            update(node<<1|1, mid+1, r, pos, val, st)
        }
        if st.data[node<<1] > st.data[node<<1|1] {
            st.data[node] = st.data[node<<1]
        } else {
            st.data[node] = st.data[node<<1|1]
        }
    }
    var query func(node, l, r, ql, qr int, st *SegTree) int
    query = func(node, l, r, ql, qr int, st *SegTree) int {
        if ql > r || qr < l {
            return 0
        }
        if ql <= l && r <= qr {
            return st.data[node]
        }
        mid := (l + r) >> 1
        left := query(node<<1, l, mid, ql, qr, st)
        right := query(node<<1|1, mid+1, r, ql, qr, st)
        if left > right {
            return left
        }
        return right
    }

    seg := newSegTree(maxVal)

    ans := 0
    for _, v := range nums {
        l := v - k
        if l < 1 {
            l = 1
        }
        r := v - 1
        best := 0
        if l <= r {
            best = query(1, 1, seg.n, l, r, seg)
        }
        cur := best + 1
        // update position v with cur if larger
        prev := query(1, 1, seg.n, v, v, seg)
        if cur > prev {
            update(1, 1, seg.n, v, cur, seg)
        }
        if cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def length_of_lis(nums, k)
  max_val = nums.max
  size = max_val + 2
  n = 1
  n <<= 1 while n < size
  tree = Array.new(2 * n, 0)

  point_update = lambda do |idx, val|
    i = idx + n - 1
    if val > tree[i]
      tree[i] = val
      i >>= 1
      while i > 0
        new_val = [tree[i << 1], tree[(i << 1) + 1]].max
        break if new_val == tree[i]
        tree[i] = new_val
        i >>= 1
      end
    end
  end

  range_query = lambda do |l, r|
    return 0 if l > r
    res = 0
    l += n - 1
    r += n - 1
    while l <= r
      if (l & 1) == 1
        res = [res, tree[l]].max
        l += 1
      end
      if (r & 1) == 0
        res = [res, tree[r]].max
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end

  ans = 0
  nums.each do |num|
    left = num - k
    left = 1 if left < 1
    right = num - 1
    best = range_query.call(left, right)
    cur = best + 1
    point_update.call(num, cur)
    ans = cur if cur > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
  def lengthOfLIS(nums: Array[Int], k: Int): Int = {
    if (nums.isEmpty) return 0
    val maxVal = 100000                     // according to constraints
    var size = 1
    while (size <= maxVal) size <<= 1
    val seg = new Array[Int](2 * size)

    def query(l0: Int, r0: Int): Int = {
      var l = l0 + size
      var r = r0 + size
      var res = 0
      while (l <= r) {
        if ((l & 1) == 1) {
          if (seg(l) > res) res = seg(l)
          l += 1
        }
        if ((r & 1) == 0) {
          if (seg(r) > res) res = seg(r)
          r -= 1
        }
        l >>= 1
        r >>= 1
      }
      res
    }

    var answer = 0

    for (num <- nums) {
      val left = math.max(1, num - k)
      val right = num - 1
      val bestPrev = if (left <= right) query(left, right) else 0
      val cur = bestPrev + 1

      // point update at position num with max value
      var pos = num + size
      if (cur > seg(pos)) {
        seg(pos) = cur
        var p = pos >> 1
        while (p > 0) {
          val newVal = math.max(seg(p << 1), seg((p << 1) + 1))
          if (newVal == seg(p)) {
            // no change, can break early
            // but continue to ensure ancestors are correct
          }
          seg(p) = newVal
          p >>= 1
        }
      }

      if (cur > answer) answer = cur
    }

    answer
  }
}
```

## Rust

```rust
use std::cmp::max;

struct SegTree {
    n: usize,
    data: Vec<i32>,
}
impl SegTree {
    fn new(size: usize) -> Self {
        let mut n = 1usize;
        while n < size {
            n <<= 1;
        }
        SegTree { n, data: vec![0; 2 * n] }
    }
    fn update(&mut self, mut pos: usize, val: i32) {
        pos += self.n;
        if self.data[pos] >= val {
            return;
        }
        self.data[pos] = val;
        while pos > 1 {
            pos >>= 1;
            let new_val = self.data[2 * pos].max(self.data[2 * pos + 1]);
            if self.data[pos] == new_val {
                break;
            }
            self.data[pos] = new_val;
        }
    }
    fn query(&self, mut l: usize, mut r: usize) -> i32 {
        let mut res = 0i32;
        l += self.n;
        r += self.n;
        while l <= r {
            if (l & 1) == 1 {
                res = max(res, self.data[l]);
                l += 1;
            }
            if (r & 1) == 0 {
                res = max(res, self.data[r]);
                r -= 1;
            }
            l >>= 1;
            r >>= 1;
        }
        res
    }
}

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>, k: i32) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut seg = SegTree::new(max_val + 2);
        let mut ans = 0i32;
        for &num in nums.iter() {
            let v = num as usize;
            let l = if v > k as usize { v - k as usize } else { 1 };
            let r = if v == 0 { 0 } else { v - 1 };
            let best = if l <= r { seg.query(l, r) } else { 0 };
            let dp = best + 1;
            seg.update(v, dp);
            ans = max(ans, dp);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (length-of-lis nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((max-val (apply max nums))
         (size
          (let loop ((s 1))
            (if (< s (+ max-val 1)) (loop (* s 2)) s)))
         (seg (make-vector (* 2 size) 0))
         (update
          (lambda (idx val)
            (let* ((pos (+ idx size))
                   (old (vector-ref seg pos))
                   (new (if (> val old) val old)))
              (when (> new old)
                (vector-set! seg pos new)
                (let loop ((i (quotient pos 2)))
                  (when (> i 0)
                    (let ((left (vector-ref seg (* i 2)))
                          (right (vector-ref seg (+ (* i 2) 1))))
                      (vector-set! seg i (if (> left right) left right))
                      (loop (quotient i 2)))))))))
         (query
          (lambda (l r)
            (let loop ((l (+ l size)) (r (+ r size)) (res 0))
              (if (= l r)
                  res
                  (begin
                    (when (odd? l)
                      (set! res (max res (vector-ref seg l)))
                      (set! l (+ l 1)))
                    (when (odd? r)
                      (set! r (- r 1))
                      (set! res (max res (vector-ref seg r))))
                    (loop (quotient l 2) (quotient r 2) res))))))
         (process
          (let loop ((lst nums) (best 0))
            (if (null? lst)
                best
                (let* ((v (car lst))
                       (l (max 0 (- v k)))
                       (prev (if (< l v) (query l v) 0))
                       (cur (+ prev 1)))
                  (update v cur)
                  (loop (cdr lst) (if (> cur best) cur best)))))))
    (process)))
```

## Erlang

```erlang
-module(solution).
-export([length_of_lis/2]).
-spec length_of_lis(Nums :: [integer()], K :: integer()) -> integer().
length_of_lis(Nums, K) ->
    MaxVal = lists:max(Nums),
    Size = next_pow2(MaxVal + 1),
    Seg = ets:new(seg, [named_table, public]),
    process_nums(Nums, K, Size, Seg, 0).

process_nums([], _K, _Size, _Seg, Ans) -> Ans;
process_nums([Num|Rest], K, Size, Seg, CurAns) ->
    L = max(1, Num - K),
    R = Num - 1,
    MaxPrev = case L =< R of
                  true -> query(Seg, 1, 0, Size-1, L, R);
                  false -> 0
              end,
    DP = MaxPrev + 1,
    update(Seg, 1, 0, Size-1, Num, DP),
    NewAns = max(CurAns, DP),
    process_nums(Rest, K, Size, Seg, NewAns).

query(_Seg, _Node, L, R, QL, QR) when QL =< L, R =< QR ->
    case ets:lookup(seg, _Node) of
        [] -> 0;
        [{_Node, V}] -> V
    end;
query(Seg, Node, L, R, QL, QR) when QR < L; QL > R ->
    0;
query(Seg, Node, L, R, QL, QR) ->
    Mid = (L + R) div 2,
    LeftMax = query(Seg, Node*2, L, Mid, QL, QR),
    RightMax = query(Seg, Node*2+1, Mid+1, R, QL, QR),
    max(LeftMax, RightMax).

update(Seg, Node, L, R, Pos, Val) when L == R ->
    case ets:lookup(seg, Node) of
        [] -> ets:insert(seg, {Node, Val});
        [{Node, Old}] when Val > Old -> ets:insert(seg, {Node, Val});
        _ -> ok
    end;
update(Seg, Node, L, R, Pos, Val) ->
    Mid = (L + R) div 2,
    if Pos =< Mid ->
            update(Seg, Node*2, L, Mid, Pos, Val);
       true ->
            update(Seg, Node*2+1, Mid+1, R, Pos, Val)
    end,
    LeftVal = case ets:lookup(seg, Node*2) of [] -> 0; [{_,V}] -> V end,
    RightVal = case ets:lookup(seg, Node*2+1) of [] -> 0; [{_,V}] -> V end,
    MaxChild = max(LeftVal, RightVal),
    case ets:lookup(seg, Node) of
        [] -> ets:insert(seg, {Node, MaxChild});
        [{Node, Old}] when MaxChild > Old -> ets:insert(seg, {Node, MaxChild});
        _ -> ok
    end.

next_pow2(N) -> next_pow2(N, 1).
next_pow2(N, P) when P >= N -> P;
next_pow2(N, P) -> next_pow2(N, P*2).
```

## Elixir

```elixir
defmodule Solution do
  @spec length_of_lis(nums :: [integer], k :: integer) :: integer
  def length_of_lis(nums, k) do
    max_val = Enum.max(nums)
    size = max_val + 2
    tree = :array.new(4 * size, default: 0)

    {_final_tree, ans} =
      Enum.reduce(nums, {tree, 0}, fn x, {t, a} ->
        l = x - k
        l = if l < 1, do: 1, else: l
        r = x - 1

        best =
          if l <= r do
            seg_query(t, 1, 1, size, l, r)
          else
            0
          end

        cur = best + 1
        t2 = seg_update(t, 1, 1, size, x, cur)
        {t2, if cur > a, do: cur, else: a}
      end)

    ans
  end

  defp seg_query(tree, _node, _l, _r, ql, qr) when ql > qr, do: 0

  defp seg_query(tree, node, l, r, ql, qr) do
    cond do
      ql > r or qr < l ->
        0

      ql <= l and r <= qr ->
        :array.get(node, tree)

      true ->
        mid = div(l + r, 2)
        left = seg_query(tree, node * 2, l, mid, ql, qr)
        right = seg_query(tree, node * 2 + 1, mid + 1, r, ql, qr)
        if left > right, do: left, else: right
    end
  end

  defp seg_update(tree, node, l, r, pos, val) do
    if l == r do
      cur = :array.get(node, tree)
      new_val = if cur > val, do: cur, else: val
      :array.set(node, new_val, tree)
    else
      mid = div(l + r, 2)

      tree =
        if pos <= mid do
          seg_update(tree, node * 2, l, mid, pos, val)
        else
          seg_update(tree, node * 2 + 1, mid + 1, r, pos, val)
        end

      left = :array.get(node * 2, tree)
      right = :array.get(node * 2 + 1, tree)
      new_val = if left > right, do: left, else: right
      :array.set(node, new_val, tree)
    end
  end
end
```
