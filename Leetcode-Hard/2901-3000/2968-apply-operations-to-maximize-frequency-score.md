# 2968. Apply Operations to Maximize Frequency Score

## Cpp

```cpp
class Solution {
public:
    int maxFrequencyScore(vector<int>& nums, long long k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        
        int l = 0, ans = 1;
        for (int r = 0; r < n; ++r) {
            while (l <= r) {
                int len = r - l + 1;
                int m = l + (len - 1) / 2; // median index
                long long leftCost = (long long)nums[m] * (m - l) - (pref[m] - pref[l]);
                long long rightCost = (pref[r + 1] - pref[m + 1]) - (long long)nums[m] * (r - m);
                if (leftCost + rightCost <= k) break;
                ++l;
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequencyScore(int[] nums, long k) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        int ans = 1;
        int left = 0;
        for (int right = 0; right < n; right++) {
            while (left < right) {
                int mid = (left + right) >>> 1;
                long median = nums[mid];
                long leftCost = median * (mid - left + 1L) - (pref[mid + 1] - pref[left]);
                long rightCost = (pref[right + 1] - pref[mid + 1]) - median * (right - mid);
                if (leftCost + rightCost <= k) {
                    break;
                }
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # prefix sums, pref[i] = sum of first i elements (0-indexed exclusive)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = 1
        left = 0

        for right in range(n):
            # shrink window until cost <= k
            while True:
                m = (left + right) // 2  # median index
                # cost of moving left part to nums[m]
                left_cost = nums[m] * (m - left) - (pref[m] - pref[left])
                # cost of moving right part to nums[m]
                right_cost = (pref[right + 1] - pref[m + 1]) - nums[m] * (right - m)
                total = left_cost + right_cost
                if total <= k:
                    break
                left += 1
            ans = max(ans, right - left + 1)

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        ans = 1
        for right, val in enumerate(nums):
            total += val
            # operations needed to raise all elements in [left, right] to val
            while val * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int maxFrequencyScore(int* nums, int numsSize, long long k) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);

    // prefix sums as long long
    long long *pref = (long long *)malloc((numsSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        pref[i + 1] = pref[i] + (long long)nums[i];
    }

    int best = 1;

    for (int r = 0; r < numsSize; ++r) {
        int lo = 0, hi = r;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int m = (mid + r) / 2;               // lower median index
            long long leftCount = m - mid + 1;
            long long leftSum   = pref[m + 1] - pref[mid];
            long long rightCount = r - m;
            long long rightSum   = pref[r + 1] - pref[m + 1];
            long long medianVal = (long long)nums[m];

            long long cost = medianVal * leftCount - leftSum
                           + rightSum - medianVal * rightCount;

            if (cost <= k)
                hi = mid;
            else
                lo = mid + 1;
        }
        int windowSize = r - lo + 1;
        if (windowSize > best) best = windowSize;
    }

    free(pref);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxFrequencyScore(int[] nums, long k) {
        Array.Sort(nums);
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }

        int left = 0;
        int best = 1;

        for (int right = 0; right < n; right++) {
            while (left < right && Cost(left, right, nums, pref) > k) {
                left++;
            }
            int len = right - left + 1;
            if (len > best) best = len;
        }

        return best;
    }

    private long Cost(int l, int r, int[] a, long[] pref) {
        int m = (l + r) / 2;
        long median = a[m];

        long leftSum = pref[m + 1] - pref[l];          // sum of elements from l to m
        long rightSum = pref[r + 1] - pref[m + 1];     // sum of elements from m+1 to r

        long leftCost = median * (m - l + 1) - leftSum;
        long rightCost = rightSum - median * (r - m);

        return leftCost + rightCost;
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
var maxFrequencyScore = function(nums, k) {
    const n = nums.length;
    if (n === 0) return 0;
    nums.sort((a, b) => a - b);
    // prefix sums: pref[i] = sum of first i elements (0..i-1)
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }
    // helper to compute cost to make subarray [l, r] equal to its median
    const cost = (l, r) => {
        const m = Math.floor((l + r) >> 1);
        const median = nums[m];
        const leftCount = m - l + 1;
        const rightCount = r - m;
        const leftSum = pref[m + 1] - pref[l];
        const rightSum = pref[r + 1] - pref[m + 1];
        return median * leftCount - leftSum + (rightSum - median * rightCount);
    };
    let ans = 1;
    for (let r = 0; r < n; ++r) {
        // binary search smallest l such that cost(l, r) <= k
        let lo = 0, hi = r;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (cost(mid, r) <= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        // after loop, lo is minimal l satisfying condition (or r+1 if none)
        if (cost(lo, r) <= k) {
            const len = r - lo + 1;
            if (len > ans) ans = len;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxFrequencyScore(nums: number[], k: number): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + nums[i];
    }
    let ans = 1;
    let l = 0;
    for (let r = 0; r < n; r++) {
        while (l < r) {
            const m = Math.floor((l + r) / 2);
            const leftCost = nums[m] * (m - l) - (pref[m] - pref[l]);
            const rightCost = (pref[r + 1] - pref[m + 1]) - nums[m] * (r - m);
            const cost = leftCost + rightCost;
            if (cost <= k) break;
            l++;
        }
        const len = r - l + 1;
        if (len > ans) ans = len;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxFrequencyScore($nums, $k) {
        sort($nums);
        $n = count($nums);
        if ($n == 0) return 0;

        // prefix sums
        $prefix = array_fill(0, $n, 0);
        $prefix[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $prefix[$i] = $prefix[$i - 1] + $nums[$i];
        }

        $ans = 1;
        $l = 0;

        for ($r = 0; $r < $n; $r++) {
            while ($l < $r) {
                $m = intdiv($l + $r, 2);

                // cost on the left side of median
                if ($m > $l) {
                    $sumLeft = $prefix[$m - 1] - ($l > 0 ? $prefix[$l - 1] : 0);
                    $leftCount = $m - $l;
                    $costLeft = $nums[$m] * $leftCount - $sumLeft;
                } else {
                    $costLeft = 0;
                }

                // cost on the right side of median
                if ($r > $m) {
                    $sumRight = $prefix[$r] - $prefix[$m];
                    $rightCount = $r - $m;
                    $costRight = $sumRight - $nums[$m] * $rightCount;
                } else {
                    $costRight = 0;
                }

                $totalCost = $costLeft + $costRight;

                if ($totalCost <= $k) {
                    break;
                }
                $l++;
            }
            $ans = max($ans, $r - $l + 1);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Heap<T> {
    private var elements: [T] = []
    private let priorityFunction: (T, T) -> Bool

    init(sort: @escaping (T, T) -> Bool) {
        self.priorityFunction = sort
    }

    var count: Int { elements.count }
    var isEmpty: Bool { elements.isEmpty }

    func peek() -> T? {
        return elements.first
    }

    func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }

    func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let value = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return value
        }
    }

    private func parent(_ index: Int) -> Int { (index - 1) / 2 }
    private func leftChild(_ index: Int) -> Int { 2 * index + 1 }
    private func rightChild(_ index: Int) -> Int { 2 * index + 2 }

    private func siftUp(from index: Int) {
        var child = index
        var parentIdx = parent(child)
        while child > 0 && priorityFunction(elements[child], elements[parentIdx]) {
            elements.swapAt(child, parentIdx)
            child = parentIdx
            parentIdx = parent(child)
        }
    }

    private func siftDown(from index: Int) {
        var parentIdx = index
        while true {
            let left = leftChild(parentIdx)
            let right = rightChild(parentIdx)
            var candidate = parentIdx

            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parentIdx { return }
            elements.swapAt(parentIdx, candidate)
            parentIdx = candidate
        }
    }
}

class Solution {
    func maxFrequencyScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        let sorted = nums.sorted()
        var lower = Heap<Int>(sort: >)   // max-heap
        var upper = Heap<Int>(sort: <)   // min-heap

        var sumLow: Int64 = 0
        var sumHigh: Int64 = 0
        var delayed = [Int:Int]()

        func prune(_ heap: Heap<Int>) {
            while let top = heap.peek(), let cnt = delayed[top], cnt > 0 {
                _ = heap.pop()
                if cnt == 1 {
                    delayed.removeValue(forKey: top)
                } else {
                    delayed[top] = cnt - 1
                }
            }
        }

        func balance() {
            // ensure lower has size >= upper and difference <= 1
            while lower.count > upper.count + 1 {
                if let move = lower.pop() {
                    sumLow -= Int64(move)
                    upper.push(move)
                    sumHigh += Int64(move)
                }
                prune(lower)
                prune(upper)
            }
            while lower.count < upper.count {
                if let move = upper.pop() {
                    sumHigh -= Int64(move)
                    lower.push(move)
                    sumLow += Int64(move)
                }
                prune(lower)
                prune(upper)
            }
        }

        func add(_ num: Int) {
            if let top = lower.peek(), num <= top {
                lower.push(num)
                sumLow += Int64(num)
            } else {
                upper.push(num)
                sumHigh += Int64(num)
            }
            balance()
        }

        func remove(_ num: Int) {
            // decide which heap the number belongs to based on current median
            if let top = lower.peek(), num <= top {
                sumLow -= Int64(num)
                delayed[num, default: 0] += 1
                if let peek = lower.peek(), peek == num {
                    prune(lower)
                }
            } else {
                sumHigh -= Int64(num)
                delayed[num, default: 0] += 1
                if let peek = upper.peek(), peek == num {
                    prune(upper)
                }
            }
            prune(lower)
            prune(upper)
            balance()
        }

        var left = 0
        var answer = 0
        for right in 0..<n {
            add(sorted[right])

            while true {
                guard let median = lower.peek() else { break }
                let lowSize = lower.count
                let highSize = upper.count

                let cost = Int64(median) * Int64(lowSize) - sumLow + sumHigh - Int64(median) * Int64(highSize)
                if cost <= Int64(k) {
                    break
                }
                remove(sorted[left])
                left += 1
            }

            answer = max(answer, right - left + 1)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFrequencyScore(nums: IntArray, k: Long): Int {
        val n = nums.size
        if (n == 0) return 0
        // sort as Long to avoid overflow in calculations
        val sorted = nums.map { it.toLong() }.sorted()
        val arr = LongArray(n) { sorted[it] }
        // prefix sums, prefix[i] = sum of first i elements (arr[0]..arr[i-1])
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + arr[i]
        }

        fun can(len: Int): Boolean {
            var left = 0
            while (left + len <= n) {
                val right = left + len - 1
                val medianIdx = left + (len - 1) / 2
                val median = arr[medianIdx]

                // cost for elements on the left side of median
                val leftCount = medianIdx - left
                val leftSum = prefix[medianIdx] - prefix[left]
                val costLeft = median * leftCount - leftSum

                // cost for elements on the right side of median
                val rightCount = right - medianIdx
                val rightSum = prefix[right + 1] - prefix[medianIdx + 1]
                val costRight = rightSum - median * rightCount

                if (costLeft + costRight <= k) return true
                left++
            }
            return false
        }

        var low = 1
        var high = n
        var answer = 0
        while (low <= high) {
            val mid = (low + high) ushr 1
            if (can(mid)) {
                answer = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequencyScore(List<int> nums, int k) {
    int n = nums.length;
    nums.sort();
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + nums[i];
    }
    int ans = 1;
    int l = 0;
    for (int r = 0; r < n; ++r) {
      while (l <= r) {
        int m = (l + r) >> 1;
        int med = nums[m];
        int leftCount = m - l;
        int leftSum = pref[m] - pref[l];
        int leftCost = med * leftCount - leftSum;
        int rightCount = r - m;
        int rightSum = pref[r + 1] - pref[m + 1];
        int rightCost = rightSum - med * rightCount;
        int total = leftCost + rightCost;
        if (total <= k) break;
        l++;
      }
      int len = r - l + 1;
      if (len > ans) ans = len;
    }
    return ans;
  }
}
```

## Golang

```go
func maxFrequencyScore(nums []int, k int64) int {
    n := len(nums)
    sort.Ints(nums)

    pref := make([]int64, n)
    for i, v := range nums {
        if i == 0 {
            pref[i] = int64(v)
        } else {
            pref[i] = pref[i-1] + int64(v)
        }
    }

    rangeSum := func(l, r int) int64 {
        if l > r {
            return 0
        }
        if l == 0 {
            return pref[r]
        }
        return pref[r] - pref[l-1]
    }

    computeCost := func(l, r int) int64 {
        mid := (l + r) / 2
        leftCount := mid - l
        rightCount := r - mid

        leftSum := rangeSum(l, mid-1)
        rightSum := rangeSum(mid+1, r)

        medianVal := int64(nums[mid])
        costLeft := medianVal*int64(leftCount) - leftSum
        costRight := rightSum - medianVal*int64(rightCount)
        return costLeft + costRight
    }

    ans := 0
    l := 0
    for r := 0; r < n; r++ {
        for l <= r && computeCost(l, r) > k {
            l++
        }
        if size := r - l + 1; size > ans {
            ans = size
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_frequency_score(nums, k)
  nums.sort!
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }

  feasible = lambda do |len|
    (0..n - len).each do |i|
      j = i + len - 1
      m = (i + j) / 2
      left_cnt = m - i + 1
      right_cnt = j - m
      sum_left = prefix[m + 1] - prefix[i]
      sum_right = prefix[j + 1] - prefix[m + 1]
      cost = nums[m] * left_cnt - sum_left + sum_right - nums[m] * right_cnt
      return true if cost <= k
    end
    false
  end

  low = 1
  high = n
  ans = 1
  while low <= high
    mid_len = (low + high) / 2
    if feasible.call(mid_len)
      ans = mid_len
      low = mid_len + 1
    else
      high = mid_len - 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxFrequencyScore(nums: Array[Int], k: Long): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        val pref = new Array[Long](n + 1)
        for (i <- 0 until n) pref(i + 1) = pref(i) + sorted(i).toLong

        def cost(l: Int, r: Int): Long = {
            val m = (l + r) >>> 1
            val median = sorted(m).toLong
            val leftCount = m - l + 1
            val rightCount = r - m
            val leftSum = pref(m + 1) - pref(l)
            val rightSum = pref(r + 1) - pref(m + 1)
            val costLeft = median * leftCount - leftSum
            val costRight = rightSum - median * rightCount
            costLeft + costRight
        }

        var l = 0
        var ans = 0
        for (r <- 0 until n) {
            while (l <= r && cost(l, r) > k) {
                l += 1
            }
            ans = math.max(ans, r - l + 1)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency_score(nums: Vec<i32>, k: i64) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // Convert to i64 and sort
        let mut a: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        a.sort_unstable();

        // Prefix sums
        let mut pref: Vec<i64> = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + a[i];
        }

        // Helper to compute minimal cost to make subarray [l, r] equal to its median
        let cost = |l: usize, r: usize, a: &[i64], pref: &[i64]| -> i64 {
            if l == r {
                return 0;
            }
            let m = (l + r) / 2;
            let left_len = m - l;
            let right_len = r - m;
            let sum_left = pref[m] - pref[l];
            let sum_right = pref[r + 1] - pref[m + 1];
            let median = a[m];
            let left_cost = median * left_len as i64 - sum_left;
            let right_cost = sum_right - median * right_len as i64;
            left_cost + right_cost
        };

        let mut l: usize = 0;
        let mut ans: usize = 1;

        for r in 0..n {
            while l < r && cost(l, r, &a, &pref) > k {
                l += 1;
            }
            let len = r - l + 1;
            if len > ans {
                ans = len;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-frequency-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (list->vector (sort nums <)))
         (n (vector-length sorted))
         (pref (make-vector (+ n 1) 0)))
    ;; prefix sums
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1)
                   (+ (vector-ref pref i) (vector-ref sorted i))))
    (define (window-cost l r)
      (let* ((len (- r l -1))
             (m (+ l (quotient (- len 1) 2))) ; median index
             (median (vector-ref sorted m))
             (left-count (+ 1 (- m l)))
             (right-count (- r m))
             (sum-left (- (vector-ref pref (+ m 1)) (vector-ref pref l)))
             (sum-right (- (vector-ref pref (+ r 1)) (vector-ref pref (+ m 1)))))
        (+ (- (* median left-count) sum-left)
           (- sum-right (* median right-count)))))
    ;; binary search for maximal length
    (let loop ((low 1) (high n) (ans 1))
      (if (> low high)
          ans
          (let* ((mid (quotient (+ low high) 2))
                 (possible
                  (let find ((start 0) (found? #f))
                    (cond
                      [found? #t]
                      [(> start (- n mid)) #f]
                      [else
                       (if (<= (window-cost start (+ start mid -1)) k)
                           #t
                           (find (+ start 1) #f))]))))
            (if possible
                (loop (+ mid 1) high mid)
                (loop low (- mid 1) ans)))))))
```

## Erlang

```erlang
-export([max_frequency_score/2]).

-spec max_frequency_score(Nums :: [integer()], K :: integer()) -> integer().
max_frequency_score(Nums, K) ->
    Sorted = lists:sort(Nums),
    Tuple = list_to_tuple(Sorted),
    N = tuple_size(Tuple),
    InitState = #{l => 0,
                  lower => gb_trees:empty(),
                  upper => gb_trees:empty(),
                  sumL => 0,
                  sumU => 0,
                  sizeL => 0,
                  sizeU => 0,
                  max => 1},
    loop(0, N, Tuple, K, InitState).

%% main sliding window loop
loop(R, N, _Tuple, _K, State) when R =:= N ->
    maps:get(max, State);
loop(R, N, Tuple, K, State) ->
    X = element(R + 1, Tuple),
    %% insert X
    {Lower0, Upper0, SumL0, SumU0, SizeL0, SizeU0} =
        case gb_trees:is_empty(maps:get(lower, State)) of
            true ->
                Lower1 = gb_insert(gb_trees:empty(), X),
                {Lower1,
                 maps:get(upper, State),
                 maps:get(sumL, State) + X,
                 maps:get(sumU, State),
                 maps:get(sizeL, State) + 1,
                 maps:get(sizeU, State)};
            false ->
                Median = element(1, gb_trees:largest(maps:get(lower, State))),
                if
                    X =< Median ->
                        Lower1 = gb_insert(maps:get(lower, State), X),
                        {Lower1,
                         maps:get(upper, State),
                         maps:get(sumL, State) + X,
                         maps:get(sumU, State),
                         maps:get(sizeL, State) + 1,
                         maps:get(sizeU, State)};
                    true ->
                        Upper1 = gb_insert(maps:get(upper, State), X),
                        {maps:get(lower, State),
                         Upper1,
                         maps:get(sumL, State),
                         maps:get(sumU, State) + X,
                         maps:get(sizeL, State),
                         maps:get(sizeU, State) + 1}
                end
        end,
    %% rebalance after insertion
    {Lower1, Upper1, SumL1, SumU1, SizeL1, SizeU1} =
        rebalance(Lower0, Upper0, SumL0, SumU0, SizeL0, SizeU0),
    State1 = #{l => maps:get(l, State),
               lower => Lower1,
               upper => Upper1,
               sumL => SumL1,
               sumU => SumU1,
               sizeL => SizeL1,
               sizeU => SizeU1},
    %% shrink window while cost > K
    {State2, CurrLen} = shrink(State1, Tuple, K),
    MaxSoFar = erlang:max(maps:get(max, State), CurrLen),
    loop(R + 1, N, Tuple, K, State2#{max => MaxSoFar}).

%% rebalance two multisets so that sizeL >= sizeU and diff <= 1
rebalance(Lower, Upper, SumL, SumU, SizeL, SizeU) ->
    case SizeL > SizeU + 1 of
        true ->
            {Key, _} = gb_trees:largest(Lower),
            Lower2 = gb_delete_one(Lower, Key),
            Upper2 = gb_insert(Upper, Key),
            rebalance(Lower2, Upper2,
                      SumL - Key, SumU + Key,
                      SizeL - 1, SizeU + 1);
        false ->
            case SizeU > SizeL of
                true ->
                    {Key, _} = gb_trees:smallest(Upper),
                    Upper2 = gb_delete_one(Upper, Key),
                    Lower2 = gb_insert(Lower, Key),
                    rebalance(Lower2, Upper2,
                              SumL + Key, SumU - Key,
                              SizeL + 1, SizeU - 1);
                false ->
                    {Lower, Upper, SumL, SumU, SizeL, SizeU}
            end
    end.

%% shrink left side while total cost exceeds K
shrink(State, Tuple, K) ->
    TotalSize = maps:get(sizeL, State) + maps:get(sizeU, State),
    case TotalSize of
        0 -> {State, 0};
        _ ->
            Cost = calc_cost(State),
            if
                Cost =< K ->
                    {State, TotalSize};
                true ->
                    L = maps:get(l, State),
                    X = element(L + 1, Tuple),
                    Lower0 = maps:get(lower, State),
                    %% remove X from lower (it is the smallest element)
                    Lower1 = gb_delete_one(Lower0, X),
                    SumL1 = maps:get(sumL, State) - X,
                    SizeL1 = maps:get(sizeL, State) - 1,
                    Upper0 = maps:get(upper, State),
                    SumU0 = maps:get(sumU, State),
                    SizeU0 = maps:get(sizeU, State),
                    {Lower2, Upper2, SumL2, SumU2, SizeL2, SizeU2} =
                        rebalance(Lower1, Upper0,
                                  SumL1, SumU0,
                                  SizeL1, SizeU0),
                    NewState = #{l => L + 1,
                                 lower => Lower2,
                                 upper => Upper2,
                                 sumL => SumL2,
                                 sumU => SumU2,
                                 sizeL => SizeL2,
                                 sizeU => SizeU2},
                    shrink(NewState, Tuple, K)
            end
    end.

%% calculate total cost to make all elements equal to current median
calc_cost(State) ->
    SizeL = maps:get(sizeL, State),
    case SizeL of
        0 -> 0;
        _ ->
            Median = element(1, gb_trees:largest(maps:get(lower, State))),
            SumL = maps:get(sumL, State),
            SumU = maps:get(sumU, State),
            SizeU = maps:get(sizeU, State),
            Median * SizeL - SumL + SumU - Median * SizeU
    end.

%% multiset insert (store count)
gb_insert(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, Count} -> gb_trees:update(Key, Count + 1, Tree);
        none -> gb_trees:insert(Key, 1, Tree)
    end.

%% multiset delete one occurrence
gb_delete_one(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, 1} -> gb_trees:delete(Key, Tree);
        {value, Count} -> gb_trees:update(Key, Count - 1, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency_score(nums :: [integer], k :: integer) :: integer
  def max_frequency_score(nums, k) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    a = List.to_tuple(sorted)

    pref_rev =
      Enum.reduce(sorted, [0], fn x, acc ->
        [(hd(acc) + x) | acc]
      end)

    pref_list = Enum.reverse(pref_rev)
    pref = List.to_tuple(pref_list)

    binary_search(1, n, 0, n, a, pref, k)
  end

  defp binary_search(low, high, ans, n, a, pref, k) do
    if low > high do
      ans
    else
      mid = div(low + high, 2)

      if feasible(mid, n, a, pref, k) do
        binary_search(mid + 1, high, mid, n, a, pref, k)
      else
        binary_search(low, mid - 1, ans, n, a, pref, k)
      end
    end
  end

  defp feasible(len, n, a, pref, k) do
    max_start = n - len
    check_window(0, max_start, len, a, pref, k)
  end

  defp check_window(start, max_start, _len, _a, _pref, _k) when start > max_start,
    do: false

  defp check_window(start, max_start, len, a, pref, k) do
    r = start + len - 1
    mid = start + div(len - 1, 2)
    med = elem(a, mid)

    left_count = mid - start
    right_count = r - mid

    left_sum = elem(pref, mid) - elem(pref, start)
    right_sum = elem(pref, r + 1) - elem(pref, mid + 1)

    cost =
      med * left_count - left_sum +
        right_sum - med * right_count

    if cost <= k do
      true
    else
      check_window(start + 1, max_start, len, a, pref, k)
    end
  end
end
```
