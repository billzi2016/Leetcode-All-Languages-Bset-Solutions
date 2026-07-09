# 2382. Maximum Segment Sum After Removals

## Cpp

```cpp
class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        int n = nums.size();
        vector<int> parent(n, -1), sz(n, 0);
        vector<long long> segSum(n, 0);
        vector<bool> active(n, false);
        function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (sz[ra] < sz[rb]) swap(ra, rb);
            parent[rb] = ra;
            segSum[ra] += segSum[rb];
            sz[ra] += sz[rb];
        };
        
        vector<long long> ans(n);
        long long curMax = 0;
        for (int i = n - 1; i >= 0; --i) {
            ans[i] = curMax;
            int idx = removeQueries[i];
            active[idx] = true;
            parent[idx] = idx;
            sz[idx] = 1;
            segSum[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) unite(idx, idx - 1);
            if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1);
            curMax = max(curMax, segSum[find(idx)]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] maximumSegmentSum(int[] nums, int[] removeQueries) {
        int n = nums.length;
        long[] answer = new long[n];
        boolean[] active = new boolean[n];
        int[] parent = new int[n];
        int[] size = new int[n];
        long[] compSum = new long[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        long curMax = 0L;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] = curMax;
            int idx = removeQueries[i];
            active[idx] = true;
            compSum[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) {
                union(idx, idx - 1, parent, size, compSum);
            }
            if (idx + 1 < n && active[idx + 1]) {
                union(idx, idx + 1, parent, size, compSum);
            }
            int root = find(idx, parent);
            curMax = Math.max(curMax, compSum[root]);
        }
        return answer;
    }

    private int find(int x, int[] parent) {
        if (parent[x] != x) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    private void union(int a, int b, int[] parent, int[] size, long[] compSum) {
        int ra = find(a, parent);
        int rb = find(b, parent);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            int tmp = ra; ra = rb; rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
        compSum[ra] += compSum[rb];
    }
}
```

## Python

```python
class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        parent = [-1] * n          # DSU parent
        seg_sum = [0] * n          # sum of segment for root
        active = [False] * n       # whether index is currently present

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            # attach rb under ra
            parent[rb] = ra
            seg_sum[ra] += seg_sum[rb]
            return ra

        ans = [0] * n
        cur_max = 0

        for i in range(n - 1, -1, -1):
            ans[i] = cur_max
            idx = removeQueries[i]

            active[idx] = True
            parent[idx] = idx
            seg_sum[idx] = nums[idx]

            if idx > 0 and active[idx - 1]:
                union(idx, idx - 1)
            if idx + 1 < n and active[idx + 1]:
                union(idx, idx + 1)

            root = find(idx)
            cur_max = max(cur_max, seg_sum[root])

        return ans
```

## Python3

```python
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [-1] * n
        comp_sum = [0] * n
        active = [False] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            parent[rb] = ra
            comp_sum[ra] += comp_sum[rb]

        ans = [0] * n
        cur_max = 0

        for i in range(n - 1, -1, -1):
            ans[i] = cur_max
            idx = removeQueries[i]
            active[idx] = True
            parent[idx] = idx
            comp_sum[idx] = nums[idx]

            if idx - 1 >= 0 and active[idx - 1]:
                union(idx, idx - 1)
            if idx + 1 < n and active[idx + 1]:
                union(idx, idx + 1)

            root = find(idx)
            cur_max = max(cur_max, comp_sum[root])

        return ans
```

## C

```c
#include <stdlib.h>

static int *parent;
static long long *segSum;
static char *active;

static int find_set(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_sets(int a, int b) {
    int ra = find_set(a);
    int rb = find_set(b);
    if (ra == rb) return;
    parent[rb] = ra;
    segSum[ra] += segSum[rb];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* maximumSegmentSum(int* nums, int numsSize, int* removeQueries, int removeQueriesSize, int* returnSize) {
    int n = numsSize;
    parent = (int*)malloc(n * sizeof(int));
    segSum = (long long*)malloc(n * sizeof(long long));
    active = (char*)calloc(n, sizeof(char));

    long long *ans = (long long*)malloc(n * sizeof(long long));
    long long curMax = 0;

    for (int i = n - 1; i >= 0; --i) {
        ans[i] = curMax;
        int idx = removeQueries[i];
        active[idx] = 1;
        parent[idx] = idx;
        segSum[idx] = (long long)nums[idx];

        if (idx > 0 && active[idx - 1]) {
            union_sets(idx, idx - 1);
        }
        if (idx + 1 < n && active[idx + 1]) {
            union_sets(idx, idx + 1);
        }

        int root = find_set(idx);
        if (segSum[root] > curMax) curMax = segSum[root];
    }

    *returnSize = n;
    free(parent);
    free(segSum);
    free(active);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long[] MaximumSegmentSum(int[] nums, int[] removeQueries) {
        int n = nums.Length;
        var parent = new int[n];
        var rank = new int[n];
        var segSum = new long[n];
        var active = new bool[n];
        long maxSum = 0;
        var ans = new long[n];

        for (int i = n - 1; i >= 0; i--) {
            ans[i] = maxSum;
            int idx = removeQueries[i];
            active[idx] = true;
            parent[idx] = idx;
            rank[idx] = 0;
            segSum[idx] = nums[idx];

            if (idx > 0 && active[idx - 1]) Union(idx, idx - 1, parent, rank, segSum);
            if (idx + 1 < n && active[idx + 1]) Union(idx, idx + 1, parent, rank, segSum);

            long cur = segSum[Find(idx, parent)];
            if (cur > maxSum) maxSum = cur;
        }

        return ans;
    }

    private int Find(int x, int[] parent) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void Union(int a, int b, int[] parent, int[] rank, long[] segSum) {
        int ra = Find(a, parent);
        int rb = Find(b, parent);
        if (ra == rb) return;
        if (rank[ra] < rank[rb]) {
            int tmp = ra; ra = rb; rb = tmp;
        }
        parent[rb] = ra;
        segSum[ra] += segSum[rb];
        if (rank[ra] == rank[rb]) rank[ra]++;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} removeQueries
 * @return {number[]}
 */
var maximumSegmentSum = function(nums, removeQueries) {
    const n = nums.length;
    const parent = new Array(n).fill(-1);
    const compSum = new Array(n).fill(0);
    const active = new Array(n).fill(false);
    const ans = new Array(n);
    let curMax = 0;

    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const union = (a, b) => {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        // attach rb to ra
        parent[rb] = ra;
        compSum[ra] += compSum[rb];
    };

    for (let i = n - 1; i >= 0; --i) {
        ans[i] = curMax;
        const pos = removeQueries[i];
        active[pos] = true;
        parent[pos] = pos;
        compSum[pos] = nums[pos];

        if (pos > 0 && active[pos - 1]) union(pos, pos - 1);
        if (pos + 1 < n && active[pos + 1]) union(pos, pos + 1);

        const root = find(pos);
        curMax = Math.max(curMax, compSum[root]);
    }

    return ans;
};
```

## Typescript

```typescript
function maximumSegmentSum(nums: number[], removeQueries: number[]): number[] {
    const n = nums.length;
    const parent = new Int32Array(n);
    const segSum = new Array<number>(n).fill(0);
    const active = new Uint8Array(n);

    const find = (x: number): number => {
        let root = x;
        while (parent[root] !== root) {
            root = parent[root];
        }
        // path compression
        while (parent[x] !== x) {
            const nxt = parent[x];
            parent[x] = root;
            x = nxt;
        }
        return root;
    };

    const union = (a: number, b: number): void => {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        // attach rb to ra
        parent[rb] = ra;
        segSum[ra] += segSum[rb];
    };

    const ans = new Array<number>(n);
    let curMax = 0;

    for (let k = n - 1; k >= 0; --k) {
        ans[k] = curMax;
        const idx = removeQueries[k];
        active[idx] = 1;
        parent[idx] = idx;
        segSum[idx] = nums[idx];

        if (idx > 0 && active[idx - 1]) union(idx, idx - 1);
        if (idx + 1 < n && active[idx + 1]) union(idx, idx + 1);

        const root = find(idx);
        curMax = Math.max(curMax, segSum[root]);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $removeQueries
     * @return Integer[]
     */
    function maximumSegmentSum($nums, $removeQueries) {
        $n = count($nums);
        $parent = array_fill(0, $n, -1);      // -1 means not active yet
        $compSum = array_fill(0, $n, 0);
        $active = array_fill(0, $n, false);
        $ans = array_fill(0, $n, 0);
        $currentMax = 0;

        for ($i = $n - 1; $i >= 0; --$i) {
            $ans[$i] = $currentMax;
            $idx = $removeQueries[$i];

            // activate this index
            $active[$idx] = true;
            $parent[$idx] = $idx;
            $compSum[$idx] = $nums[$idx];

            // union with left neighbor if active
            if ($idx > 0 && $active[$idx - 1]) {
                $this->union($parent, $compSum, $idx, $idx - 1);
            }
            // union with right neighbor if active
            if ($idx < $n - 1 && $active[$idx + 1]) {
                $this->union($parent, $compSum, $idx, $idx + 1);
            }

            $root = $this->find($parent, $idx);
            $currentMax = max($currentMax, $compSum[$root]);
        }

        return $ans;
    }

    private function find(&$parent, $x) {
        if ($parent[$x] != $x) {
            $parent[$x] = $this->find($parent, $parent[$x]);
        }
        return $parent[$x];
    }

    private function union(&$parent, &$compSum, $x, $y) {
        $rx = $this->find($parent, $x);
        $ry = $this->find($parent, $y);
        if ($rx == $ry) {
            return $rx;
        }
        // attach ry to rx
        $parent[$ry] = $rx;
        $compSum[$rx] += $compSum[$ry];
        return $rx;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSegmentSum(_ nums: [Int], _ removeQueries: [Int]) -> [Int] {
        let n = nums.count
        var parent = Array(repeating: -1, count: n)
        var compSum = Array(repeating: 0, count: n)
        var active = Array(repeating: false, count: n)

        func find(_ x: Int) -> Int {
            var v = x
            while parent[v] != v {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra == rb { return }
            parent[rb] = ra
            compSum[ra] += compSum[rb]
        }

        var answer = Array(repeating: 0, count: n)
        var maxSum = 0

        for i in stride(from: n - 1, through: 0, by: -1) {
            answer[i] = maxSum
            let idx = removeQueries[i]

            active[idx] = true
            parent[idx] = idx
            compSum[idx] = nums[idx]
            if compSum[idx] > maxSum { maxSum = compSum[idx] }

            if idx > 0 && active[idx - 1] {
                union(idx, idx - 1)
                let root = find(idx)
                if compSum[root] > maxSum { maxSum = compSum[root] }
            }
            if idx + 1 < n && active[idx + 1] {
                union(idx, idx + 1)
                let root = find(idx)
                if compSum[root] > maxSum { maxSum = compSum[root] }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSegmentSum(nums: IntArray, removeQueries: IntArray): LongArray {
        val n = nums.size
        val answer = LongArray(n)
        if (n == 0) return answer

        val parent = IntArray(n) { -1 }
        val segSum = LongArray(n)
        val size = IntArray(n)
        val active = BooleanArray(n)

        var currentMax = 0L
        answer[n - 1] = 0L

        fun find(x: Int): Int {
            var p = parent[x]
            if (p != x) {
                parent[x] = find(p)
            }
            return parent[x]
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
            segSum[ra] += segSum[rb]
        }

        for (k in n - 1 downTo 1) {
            val idx = removeQueries[k]
            active[idx] = true
            parent[idx] = idx
            segSum[idx] = nums[idx].toLong()
            size[idx] = 1

            if (idx > 0 && active[idx - 1]) {
                union(idx, idx - 1)
            }
            if (idx < n - 1 && active[idx + 1]) {
                union(idx, idx + 1)
            }

            val root = find(idx)
            currentMax = kotlin.math.max(currentMax, segSum[root])
            answer[k - 1] = currentMax
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximumSegmentSum(List<int> nums, List<int> removeQueries) {
    int n = nums.length;
    List<int> parent = List.filled(n, -1);
    List<int> segSum = List.filled(n, 0);
    List<bool> active = List.filled(n, false);
    List<int> answer = List.filled(n, 0);
    int currentMax = 0;

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
      parent[rb] = ra;
      segSum[ra] += segSum[rb];
    }

    for (int i = n - 1; i >= 0; --i) {
      answer[i] = currentMax;
      int idx = removeQueries[i];
      active[idx] = true;
      parent[idx] = idx;
      segSum[idx] = nums[idx];

      if (idx > 0 && active[idx - 1]) union(idx, idx - 1);
      if (idx + 1 < n && active[idx + 1]) union(idx, idx + 1);

      int root = find(idx);
      if (segSum[root] > currentMax) currentMax = segSum[root];
    }

    return answer;
  }
}
```

## Golang

```go
func maximumSegmentSum(nums []int, removeQueries []int) []int64 {
    n := len(nums)
    ans := make([]int64, n)

    parent := make([]int, n)
    compSum := make([]int64, n)
    active := make([]bool, n)

    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    var union func(int, int)
    union = func(a, b int) {
        ra := find(a)
        rb := find(b)
        if ra == rb {
            return
        }
        // merge rb into ra
        parent[rb] = ra
        compSum[ra] += compSum[rb]
    }

    curMax := int64(0)

    for i := n - 1; i >= 0; i-- {
        ans[i] = curMax
        idx := removeQueries[i]

        active[idx] = true
        parent[idx] = idx
        compSum[idx] = int64(nums[idx])

        if idx > 0 && active[idx-1] {
            union(idx, idx-1)
        }
        if idx+1 < n && active[idx+1] {
            union(idx, idx+1)
        }

        root := find(idx)
        if compSum[root] > curMax {
            curMax = compSum[root]
        }
    }

    return ans
}
```

## Ruby

```ruby
def maximum_segment_sum(nums, remove_queries)
  n = nums.length
  parent = Array.new(n, -1)
  seg_sum = Array.new(n, 0)
  active = Array.new(n, false)

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
    parent[rb] = ra
    seg_sum[ra] += seg_sum[rb]
  end

  ans = Array.new(n, 0)
  max_sum = 0

  (n - 1).downto(0) do |i|
    ans[i] = max_sum
    idx = remove_queries[i]

    active[idx] = true
    parent[idx] = idx
    seg_sum[idx] = nums[idx]

    if idx > 0 && active[idx - 1]
      union.call(idx, idx - 1)
    end
    if idx + 1 < n && active[idx + 1]
      union.call(idx, idx + 1)
    end

    root = find.call(idx)
    max_sum = [max_sum, seg_sum[root]].max
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumSegmentSum(nums: Array[Int], removeQueries: Array[Int]): Array[Long] = {
        val n = nums.length
        val ans = new Array[Long](n)
        val parent = new Array[Int](n)
        val segSum = new Array[Long](n)
        val active = new Array[Boolean](n)

        def find(x: Int): Int = {
            var v = x
            while (parent(v) != v) {
                parent(v) = parent(parent(v))
                v = parent(v)
            }
            v
        }

        def union(a: Int, b: Int): Unit = {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) {
                parent(rb) = ra
                segSum(ra) += segSum(rb)
            }
        }

        var maxSum: Long = 0L

        for (i <- (n - 1) to 0 by -1) {
            ans(i) = maxSum
            val idx = removeQueries(i)
            active(idx) = true
            parent(idx) = idx
            segSum(idx) = nums(idx).toLong
            if (idx > 0 && active(idx - 1)) union(idx, idx - 1)
            if (idx + 1 < n && active(idx + 1)) union(idx, idx + 1)
            val root = find(idx)
            maxSum = math.max(maxSum, segSum(root))
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_segment_sum(nums: Vec<i32>, remove_queries: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut parent = vec![0usize; n];
        let mut comp_sum = vec![0i64; n];
        let mut active = vec![false; n];
        let mut ans = vec![0i64; n];
        let mut cur_max: i64 = 0;

        // helper functions
        fn find(x: usize, parent: &mut Vec<usize>) -> usize {
            if parent[x] != x {
                let root = find(parent[x], parent);
                parent[x] = root;
            }
            parent[x]
        }

        fn union(a: usize, b: usize, parent: &mut Vec<usize>, comp_sum: &mut Vec<i64>) {
            let ra = find(a, parent);
            let rb = find(b, parent);
            if ra == rb {
                return;
            }
            // attach rb to ra
            parent[rb] = ra;
            comp_sum[ra] += comp_sum[rb];
        }

        for i in (0..n).rev() {
            ans[i] = cur_max;
            let idx = remove_queries[i] as usize;
            active[idx] = true;
            parent[idx] = idx;
            comp_sum[idx] = nums[idx] as i64;

            if idx > 0 && active[idx - 1] {
                union(idx, idx - 1, &mut parent, &mut comp_sum);
            }
            if idx + 1 < n && active[idx + 1] {
                union(idx, idx + 1, &mut parent, &mut comp_sum);
            }

            let root = find(idx, &mut parent);
            cur_max = cur_max.max(comp_sum[root]);
        }

        ans
    }
}
```

## Racket

```racket
(define (find parent x)
  (let ((p (vector-ref parent x)))
    (if (= p x)
        x
        (let ((root (find parent p)))
          (vector-set! parent x root)
          root))))

(define (union parent seg-sum a b)
  (let* ((ra (find parent a))
         (rb (find parent b)))
    (when (not (= ra rb))
      (vector-set! parent rb ra)
      (vector-set! seg-sum ra (+ (vector-ref seg-sum ra) (vector-ref seg-sum rb))))))

(define/contract (maximum-segment-sum nums removeQueries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (remove-vec (list->vector removeQueries))
         (active (make-vector n #f))
         (parent (make-vector n -1))
         (seg-sum (make-vector n 0))
         (answers (make-vector n 0))
         (max-sum 0))
    (let loop ((i (- n 1)))
      (when (>= i 0)
        (vector-set! answers i max-sum)
        (let* ((idx (vector-ref remove-vec i))
               (val (vector-ref nums-vec idx)))
          (vector-set! active idx #t)
          (vector-set! parent idx idx)
          (vector-set! seg-sum idx val)
          (when (and (> idx 0) (vector-ref active (- idx 1)))
            (union parent seg-sum idx (- idx 1)))
          (when (and (< idx (- n 1)) (vector-ref active (+ idx 1)))
            (union parent seg-sum idx (+ idx 1)))
          (let ((root (find parent idx)))
            (set! max-sum (max max-sum (vector-ref seg-sum root)))))
        (loop (- i 1))))
    (vector->list answers)))
```

## Erlang

```erlang
-spec maximum_segment_sum(Nums :: [integer()], RemoveQueries :: [integer()]) -> [integer()].
maximum_segment_sum(Nums, RemoveQueries) ->
    N = length(Nums),
    Indices = lists:seq(0, N - 1),
    ValsMap = maps:from_list(lists:zip(Indices, Nums)),
    RevRemove = lists:reverse(RemoveQueries),
    go(RevRemove, 0, #{}, #{}, [], ValsMap).

go([], _CurMax, _Parent, _Sum, Acc, _ValsMap) ->
    Acc;
go([Idx | Rest], CurMax, Parent, Sum, Acc, ValsMap) ->
    NewAcc = [CurMax | Acc],
    Val = maps:get(Idx, ValsMap),
    Parent1 = maps:put(Idx, Idx, Parent),
    Sum1 = maps:put(Idx, Val, Sum),
    CurMax1 = max(CurMax, Val),

    {Parent2, Sum2, CurMax2} =
        case maps:is_key(Idx - 1, Parent1) of
            true ->
                {P, S} = union(Idx, Idx - 1, Parent1, Sum1),
                {Root, _} = find(Idx, P),
                NewSum = maps:get(Root, S),
                {P, S, max(CurMax1, NewSum)};
            false ->
                {Parent1, Sum1, CurMax1}
        end,

    {Parent3, Sum3, CurMax3} =
        case maps:is_key(Idx + 1, Parent2) of
            true ->
                {P, S} = union(Idx, Idx + 1, Parent2, Sum2),
                {Root, _} = find(Idx, P),
                NewSum = maps:get(Root, S),
                {P, S, max(CurMax2, NewSum)};
            false ->
                {Parent2, Sum2, CurMax2}
        end,

    go(Rest, CurMax3, Parent3, Sum3, NewAcc, ValsMap).

find(I, Parent) ->
    case maps:get(I, Parent) of
        I -> {I, Parent};
        P ->
            {Root, UpdatedParent} = find(P, Parent),
            NewParent = maps:put(I, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(I, J, Parent, Sum) ->
    {Ri, P1} = find(I, Parent),
    {Rj, P2} = find(J, P1),
    if
        Ri == Rj -> {P2, Sum};
        true ->
            Si = maps:get(Ri, Sum),
            Sj = maps:get(Rj, Sum),
            NewSumVal = Si + Sj,
            NewParent = maps:put(Rj, Ri, P2),
            NewSum = maps:put(Ri, NewSumVal, Sum),
            {NewParent, NewSum}
    end.

max(A, B) when A >= B -> A;
max(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_segment_sum(nums :: [integer], remove_queries :: [integer]) :: [integer]
  def maximum_segment_sum(nums, remove_queries) do
    n = length(nums)
    nums_arr = :array.from_list(nums)

    parent = :array.new(n, default: -1)
    comp_sum = :array.new(n, default: 0)
    active = :array.new(n, default: false)

    answers = List.duplicate(0, n) |> List.to_tuple()

    {answers, _parent, _comp_sum, _active, _cur_max} =
      Enum.with_index(remove_queries)
      |> Enum.reverse()
      |> Enum.reduce({answers, parent, comp_sum, active, 0}, fn {idx, i},
                                                               {ans_tup, par, sum_arr,
                                                                act, cur_max} ->
        # record answer for this removal
        ans_tup = put_elem(ans_tup, i, cur_max)

        val = :array.get(idx, nums_arr)
        par = :array.set(idx, idx, par)
        sum_arr = :array.set(idx, val, sum_arr)
        act = :array.set(idx, true, act)

        # union with left neighbor if active
        if idx > 0 do
          left_active = :array.get(idx - 1, act)

          if left_active do
            {par, sum_arr} = union(idx, idx - 1, par, sum_arr)
            :ok
          else
            :ok
          end
        end

        # union with right neighbor if active
        if idx < n - 1 do
          right_active = :array.get(idx + 1, act)

          if right_active do
            {par, sum_arr} = union(idx, idx + 1, par, sum_arr)
            :ok
          else
            :ok
          end
        end

        # find root of current segment and update max
        {root, par} = find(par, idx)
        cur_max = max(cur_max, :array.get(root, sum_arr))

        {ans_tup, par, sum_arr, act, cur_max}
      end)

    Tuple.to_list(answers)
  end

  # Find with path compression; returns {root, updated_parent_array}
  defp find(parent, x) do
    p = :array.get(x, parent)

    if p == x do
      {x, parent}
    else
      {root, parent2} = find(parent, p)
      parent3 = :array.set(x, root, parent2)
      {root, parent3}
    end
  end

  # Union two active indices; returns updated {parent_array, sum_array}
  defp union(x, y, parent, sum_arr) do
    {rx, parent1} = find(parent, x)
    {ry, parent2} = find(parent1, y)

    if rx == ry do
      {parent2, sum_arr}
    else
      sum_rx = :array.get(rx, sum_arr)
      sum_ry = :array.get(ry, sum_arr)
      new_sum = sum_rx + sum_ry

      parent3 = :array.set(ry, rx, parent2)
      sum_arr2 = :array.set(rx, new_sum, sum_arr)

      {parent3, sum_arr2}
    end
  end
end
```
