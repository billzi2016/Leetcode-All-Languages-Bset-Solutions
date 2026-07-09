# 1703. Minimum Adjacent Swaps for K Consecutive Ones

## Cpp

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        vector<long long> pos;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) pos.push_back(i);
        }
        int m = pos.size();
        vector<long long> adj(m);
        for (int i = 0; i < m; ++i) {
            adj[i] = pos[i] - i;
        }
        vector<long long> pref(m + 1, 0);
        for (int i = 0; i < m; ++i) {
            pref[i + 1] = pref[i] + adj[i];
        }
        long long ans = LLONG_MAX;
        for (int i = 0; i + k <= m; ++i) {
            int mid = i + k / 2;
            long long median = adj[mid];
            long long leftCount = mid - i;
            long long rightCount = i + k - 1 - mid;
            long long leftSum = median * leftCount - (pref[mid] - pref[i]);
            long long rightSum = (pref[i + k] - pref[mid + 1]) - median * rightCount;
            ans = min(ans, leftSum + rightSum);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minMoves(int[] nums, int k) {
        java.util.List<Integer> onesPos = new java.util.ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                onesPos.add(i);
            }
        }
        int m = onesPos.size();
        long[] adj = new long[m];
        for (int i = 0; i < m; i++) {
            adj[i] = (long)onesPos.get(i) - i;
        }
        long[] prefix = new long[m + 1];
        for (int i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + adj[i];
        }

        long ans = Long.MAX_VALUE;
        for (int start = 0; start <= m - k; start++) {
            int mid = start + k / 2;
            long median = adj[mid];

            long leftSum = prefix[mid] - prefix[start];
            long rightSum = prefix[start + k] - prefix[mid + 1];

            long leftCount = mid - start;
            long rightCount = (start + k - 1) - mid;

            long cost = median * leftCount - leftSum + rightSum - median * rightCount;
            ans = Math.min(ans, cost);
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        positions = [i for i, v in enumerate(nums) if v == 1]
        if k <= 1:
            return 0

        # adjusted positions subtract their order index
        adj = [p - idx for idx, p in enumerate(positions)]

        # prefix sums of adjusted positions
        pref = [0]
        for a in adj:
            pref.append(pref[-1] + a)

        ans = float('inf')
        half = k // 2
        n = len(adj)
        for i in range(n - k + 1):
            j = i + k - 1
            mid = i + half
            median = adj[mid]

            # left side cost
            left_cnt = mid - i
            left_sum = pref[mid] - pref[i]
            left_cost = median * left_cnt - left_sum

            # right side cost
            right_cnt = j - mid
            right_sum = pref[j + 1] - pref[mid + 1]
            right_cost = right_sum - median * right_cnt

            total = left_cost + right_cost
            if total < ans:
                ans = total

        return int(ans)
```

## Python3

```python
from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, v in enumerate(nums) if v == 1]
        m = len(positions)
        # Adjust positions to account for consecutive target
        adjusted = [positions[i] - i for i in range(m)]
        prefix = [0]
        for val in adjusted:
            prefix.append(prefix[-1] + val)

        ans = float('inf')
        for left in range(0, m - k + 1):
            right = left + k - 1
            mid = left + k // 2
            median = adjusted[mid]

            left_cnt = mid - left
            right_cnt = right - mid

            left_sum = median * left_cnt - (prefix[mid] - prefix[left])
            right_sum = (prefix[right + 1] - prefix[mid + 1]) - median * right_cnt

            moves = left_sum + right_sum
            if moves < ans:
                ans = moves

        return int(ans)
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int minMoves(int* nums, int numsSize, int k) {
    int *pos = (int*)malloc(numsSize * sizeof(int));
    int m = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) pos[m++] = i;
    }

    long long *pref = (long long*)malloc((m + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < m; ++i) {
        pref[i + 1] = pref[i] + pos[i];
    }

    long long ans = LLONG_MAX;

    for (int i = 0; i <= m - k; ++i) {
        int j = i + k - 1;
        int midIdx = i + k / 2;
        long long medianPos = pos[midIdx];

        int leftCount = midIdx - i;
        int rightCount = j - midIdx;

        long long sumLeft = medianPos * leftCount - (pref[midIdx] - pref[i]);
        long long sumRight = (pref[j + 1] - pref[midIdx + 1]) - medianPos * rightCount;
        long long totalDist = sumLeft + sumRight;

        long long adjust;
        if (k % 2 == 1) {
            adjust = (long long)leftCount * (leftCount + 1);
        } else {
            adjust = (long long)leftCount * leftCount;
        }

        long long moves = totalDist - adjust;
        if (moves < ans) ans = moves;
    }

    free(pos);
    free(pref);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinMoves(int[] nums, int k) {
        List<long> pos = new List<long>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) pos.Add(i);
        }
        int m = pos.Count;
        long[] a = new long[m];
        for (int i = 0; i < m; i++) {
            a[i] = pos[i] - i;
        }
        long[] pref = new long[m + 1];
        for (int i = 0; i < m; i++) {
            pref[i + 1] = pref[i] + a[i];
        }

        long ans = long.MaxValue;
        for (int l = 0; l + k - 1 < m; l++) {
            int r = l + k - 1;
            int mid = l + k / 2;
            long median = a[mid];

            long leftCost = median * (mid - l) - (pref[mid] - pref[l]);
            long rightCost = (pref[r + 1] - pref[mid + 1]) - median * (r - mid);
            long total = leftCost + rightCost;
            if (total < ans) ans = total;
        }
        return (int)ans;
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
var minMoves = function(nums, k) {
    const pos = [];
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === 1) pos.push(i);
    }
    const m = pos.length;
    if (k <= 1) return 0;

    // Adjust positions to eliminate the effect of indices within the group
    const adj = new Array(m);
    for (let i = 0; i < m; ++i) {
        adj[i] = pos[i] - i;
    }

    // Prefix sums of adjusted positions
    const pref = new Array(m + 1);
    pref[0] = 0;
    for (let i = 0; i < m; ++i) {
        pref[i + 1] = pref[i] + adj[i];
    }

    let ans = Number.MAX_SAFE_INTEGER;

    for (let start = 0; start <= m - k; ++start) {
        const mid = start + Math.floor(k / 2);
        const median = adj[mid];

        const leftCount = mid - start;
        const rightCount = start + k - 1 - mid;

        const leftSum = median * leftCount - (pref[mid] - pref[start]);
        const rightSum = (pref[start + k] - pref[mid + 1]) - median * rightCount;

        const total = leftSum + rightSum;
        if (total < ans) ans = total;
    }

    return ans;
};
```

## Typescript

```typescript
function minMoves(nums: number[], k: number): number {
    const onesPos: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) onesPos.push(i);
    }
    const m = onesPos.length;
    if (k <= 1) return 0;

    // adjusted positions
    const adj: number[] = new Array(m);
    for (let i = 0; i < m; i++) {
        adj[i] = onesPos[i] - i;
    }

    // prefix sums of adjusted positions
    const pref: number[] = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) {
        pref[i + 1] = pref[i] + adj[i];
    }

    let ans = Number.MAX_SAFE_INTEGER;
    const half = Math.floor(k / 2);

    for (let start = 0; start <= m - k; start++) {
        const mid = start + half;
        const median = adj[mid];

        const leftCount = mid - start;
        const rightCount = start + k - 1 - mid;

        const leftSum = median * leftCount - (pref[mid] - pref[start]);
        const rightSum = (pref[start + k] - pref[mid + 1]) - median * rightCount;

        const total = leftSum + rightSum;
        if (total < ans) ans = total;
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
    function minMoves($nums, $k) {
        $positions = [];
        foreach ($nums as $i => $v) {
            if ($v == 1) {
                $positions[] = $i;
            }
        }
        $m = count($positions);
        if ($k <= 1) return 0;

        // adjusted positions: pos[i] - i
        $adj = [];
        for ($i = 0; $i < $m; ++$i) {
            $adj[$i] = $positions[$i] - $i;
        }

        // prefix sums of adjusted positions
        $prefix = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; ++$i) {
            $prefix[$i + 1] = $prefix[$i] + $adj[$i];
        }

        $ans = PHP_INT_MAX;
        for ($l = 0; $l <= $m - $k; ++$l) {
            $r = $l + $k - 1;
            $mid = intdiv($l + $r, 2);
            $median = $adj[$mid];

            // left side cost
            $leftCount = $mid - $l;
            $leftSum = $median * $leftCount - ($prefix[$mid] - $prefix[$l]);

            // right side cost
            $rightCount = $r - $mid;
            $rightSum = ($prefix[$r + 1] - $prefix[$mid + 1]) - $median * $rightCount;

            $total = $leftSum + $rightSum;
            if ($total < $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ nums: [Int], _ k: Int) -> Int {
        var ones = [Int]()
        for (i, v) in nums.enumerated() where v == 1 {
            ones.append(i)
        }
        let m = ones.count
        if k <= 1 { return 0 }
        
        var adj = [Int64]()
        adj.reserveCapacity(m)
        for i in 0..<m {
            adj.append(Int64(ones[i] - i))
        }
        
        var pref = [Int64](repeating: 0, count: m + 1)
        for i in 0..<m {
            pref[i + 1] = pref[i] + adj[i]
        }
        
        var ans = Int64.max
        let evenCorrection = k % 2 == 0
        let correctionValue: Int64 = evenCorrection ? {
            let t = Int64(k / 2)
            return t * (t + 1)
        }() : 0
        
        for l in 0...(m - k) {
            let r = l + k - 1
            let mid = l + k / 2
            let median = adj[mid]
            
            let leftCount = mid - l
            let leftSum = pref[mid] - pref[l]
            let leftCost = median * Int64(leftCount) - leftSum
            
            let rightCount = r - mid
            let rightSum = pref[r + 1] - pref[mid + 1]
            let rightCost = rightSum - median * Int64(rightCount)
            
            var total = leftCost + rightCost
            if evenCorrection {
                total -= correctionValue
            }
            if total < ans { ans = total }
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(nums: IntArray, k: Int): Int {
        val positions = mutableListOf<Int>()
        for (i in nums.indices) {
            if (nums[i] == 1) positions.add(i)
        }
        val m = positions.size
        if (k <= 1) return 0

        val adj = LongArray(m)
        for (i in 0 until m) {
            adj[i] = positions[i].toLong() - i.toLong()
        }

        val pref = LongArray(m + 1)
        for (i in 0 until m) {
            pref[i + 1] = pref[i] + adj[i]
        }

        var answer = Long.MAX_VALUE
        for (start in 0..m - k) {
            val end = start + k - 1
            val mid = start + k / 2
            val median = adj[mid]

            val leftCount = (mid - start).toLong()
            val rightCount = (end - mid).toLong()

            val sumLeft = pref[mid] - pref[start]
            val sumRight = pref[end + 1] - pref[mid + 1]

            val costLeft = median * leftCount - sumLeft
            val costRight = sumRight - median * rightCount

            val total = costLeft + costRight
            if (total < answer) answer = total
        }
        return answer.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(List<int> nums, int k) {
    List<int> pos = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) pos.add(i);
    }
    int m = pos.length;
    if (k == 1) return 0;

    List<int> pref = List.filled(m + 1, 0);
    for (int i = 0; i < m; i++) {
      pref[i + 1] = pref[i] + pos[i];
    }

    int ans = 1 << 60;
    for (int i = 0; i <= m - k; i++) {
      int j = i + k - 1;
      int mid = (i + j) ~/ 2;

      int leftCost = pos[mid] * (mid - i) - (pref[mid] - pref[i]);
      int rightCost = (pref[j + 1] - pref[mid + 1]) - pos[mid] * (j - mid);
      int cost = leftCost + rightCost;

      int leftCount = mid - i;
      int rightCount = j - mid;
      int extra = (leftCount * (leftCount + 1)) ~/ 2 +
          (rightCount * (rightCount + 1)) ~/ 2;

      int total = cost - extra;
      if (total < ans) ans = total;
    }
    return ans;
  }
}
```

## Golang

```go
func minMoves(nums []int, k int) int {
    var ones []int
    for i, v := range nums {
        if v == 1 {
            ones = append(ones, i)
        }
    }
    n := len(ones)
    adj := make([]int64, n)
    for i, pos := range ones {
        adj[i] = int64(pos - i)
    }
    pref := make([]int64, n)
    for i := 0; i < n; i++ {
        if i == 0 {
            pref[i] = adj[i]
        } else {
            pref[i] = pref[i-1] + adj[i]
        }
    }

    const inf int64 = 1<<63 - 1
    ans := inf

    for l := 0; l <= n-k; l++ {
        r := l + k - 1
        mid := l + k/2
        median := adj[mid]

        var leftSum int64
        if mid > l {
            sumAdj := pref[mid-1]
            if l > 0 {
                sumAdj -= pref[l-1]
            }
            leftCount := int64(mid - l)
            leftSum = median*leftCount - sumAdj
        }

        var rightSum int64
        if r > mid {
            sumAdj := pref[r] - pref[mid]
            rightCount := int64(r - mid)
            rightSum = sumAdj - median*rightCount
        }

        total := leftSum + rightSum
        if total < ans {
            ans = total
        }
    }

    return int(ans)
}
```

## Ruby

```ruby
def min_moves(nums, k)
  ones = []
  nums.each_with_index { |v, i| ones << i if v == 1 }
  m = ones.length
  return 0 if k <= 1

  adj = Array.new(m)
  (0...m).each { |i| adj[i] = ones[i] - i }

  pref = [0]
  adj.each { |v| pref << pref[-1] + v }

  ans = Float::INFINITY
  half = k / 2

  (0..m - k).each do |s|
    e = s + k - 1
    mid = s + half
    median = adj[mid]

    left_sum = pref[mid] - pref[s]
    right_sum = pref[e + 1] - pref[mid + 1]

    left_cost = median * (mid - s) - left_sum
    right_cost = right_sum - median * (e - mid)

    total = left_cost + right_cost
    ans = total if total < ans
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minMoves(nums: Array[Int], k: Int): Int = {
        val positions = scala.collection.mutable.ArrayBuffer[Long]()
        for (i <- nums.indices) if (nums(i) == 1) positions += i.toLong
        val m = positions.length
        if (k <= 1) return 0

        val pos = positions.toArray
        val pref = new Array[Long](m + 1)
        for (i <- 0 until m) {
            pref(i + 1) = pref(i) + pos(i)
        }

        var ans: Long = Long.MaxValue
        val half = k / 2

        for (start <- 0 to m - k) {
            val mid = start + half
            val median = pos(mid)

            val leftCount = mid - start
            val rightCount = start + k - mid - 1

            val left = median * leftCount - (pref(mid) - pref(start))
            val right = (pref(start + k) - pref(mid + 1)) - median * rightCount

            var total = left + right

            if (k % 2 == 0) {
                val t = half.toLong * half
                total -= t
            } else {
                val t = half.toLong * (half + 1)
                total -= t
            }

            if (total < ans) ans = total
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves(nums: Vec<i32>, k: i32) -> i32 {
        let mut pos: Vec<i64> = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if v == 1 {
                pos.push(i as i64);
            }
        }
        let m = pos.len();
        let k_usize = k as usize;
        // adjusted positions: pos[i] - i
        let mut adj: Vec<i64> = Vec::with_capacity(m);
        for (i, &p) in pos.iter().enumerate() {
            adj.push(p - i as i64);
        }
        // prefix sums of adjusted positions
        let mut pref: Vec<i64> = vec![0; m + 1];
        for i in 0..m {
            pref[i + 1] = pref[i] + adj[i];
        }

        let mut ans: i64 = i64::MAX;
        for l in 0..=m - k_usize {
            let r = l + k_usize - 1;
            let mid = l + k_usize / 2;
            let median = adj[mid];

            let left_count = (mid - l) as i64;
            let right_count = (r - mid) as i64;

            let left_sum = pref[mid] - pref[l];
            let left_dist = median * left_count - left_sum;

            let right_sum = pref[r + 1] - pref[mid + 1];
            let right_dist = right_sum - median * right_count;

            let moves = left_dist + right_dist;
            if moves < ans {
                ans = moves;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-moves nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [ones (for/list ([i (in-range n)] [v (in-list nums)] #:when (= v 1)) i)]
         [len (length ones)])
    (if (< len k)
        0
        (let* ([adj (let ([vec (make-vector len)])
                      (for ([idx (in-range len)]
                            [pos (in-list ones)])
                        (vector-set! vec idx (- pos idx)))
                      vec)]
               [pref (let ([p (make-vector (+ len 1) 0)])
                       (for ([i (in-range len)])
                         (vector-set! p (+ i 1)
                                      (+ (vector-ref p i) (vector-ref adj i))))
                       p)])
          (let ([ans +inf.0])
            (for ([left (in-range 0 (add1 (- len k)))])
              (let* ([right (+ left k -1)]
                     [mid (+ left (quotient k 2))]
                     [median (vector-ref adj mid)]
                     [left-sum (- (* median (- mid left))
                                 (- (vector-ref pref mid) (vector-ref pref left)))]
                     [right-sum (- (- (vector-ref pref (+ right 1))
                                      (vector-ref pref (+ mid 1)))
                                   (* median (- right mid)))])
                (set! ans (min ans (+ left-sum right-sum)))))
            (exact-round ans))))))
```

## Erlang

```erlang
-spec min_moves(Nums :: [integer()], K :: integer()) -> integer().
min_moves(Nums, K) ->
    Pos = positions(Nums, 0, []),
    Adj = adjusted(Pos, 0, []),
    PrefList = prefix(Adj, 0, [0]),
    AdjT = list_to_tuple(lists:reverse(Adj)),
    PrefT = list_to_tuple(PrefList),
    N = length(Adj),
    MaxStart = N - K,
    loop(0, MaxStart, K, AdjT, PrefT, infinity).

positions([], _Idx, Acc) -> lists:reverse(Acc);
positions([H|T], Idx, Acc) ->
    NewAcc = case H of
        1 -> [Idx|Acc];
        _ -> Acc
    end,
    positions(T, Idx + 1, NewAcc).

adjusted([], _I, Acc) -> lists:reverse(Acc);
adjusted([P|Rest], I, Acc) ->
    adjusted(Rest, I + 1, [P - I | Acc]).

prefix([], _Sum, Acc) -> Acc;
prefix([H|T], Sum, Acc) ->
    NewSum = Sum + H,
    prefix(T, NewSum, [NewSum | Acc]).

loop(L, MaxStart, _K, _AdjT, _PrefT, Min) when L > MaxStart ->
    Min;
loop(L, MaxStart, K, AdjT, PrefT, Min) ->
    R = L + K - 1,
    Mid = L + K div 2,
    Median = element(Mid + 1, AdjT),
    LeftCount = Mid - L,
    RightCount = R - Mid,

    SumLeft = Median * LeftCount -
        (element(Mid, PrefT) - element(L, PrefT)),
    SumRight = (element(R + 1, PrefT) - element(Mid + 1, PrefT)) -
        Median * RightCount,
    Total = SumLeft + SumRight,

    Correction = (LeftCount * (LeftCount + 1)) div 2 +
                 (RightCount * (RightCount + 1)) div 2,
    Moves = Total - Correction,
    NewMin = case Min of
        infinity -> Moves;
        _ when Moves < Min -> Moves;
        _ -> Min
    end,
    loop(L + 1, MaxStart, K, AdjT, PrefT, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(nums :: [integer], k :: integer) :: integer
  def min_moves(nums, k) do
    positions =
      for {v, i} <- Enum.with_index(nums), v == 1, do: i

    len = length(positions)

    if k <= 1 do
      0
    else
      adjusted =
        Enum.map(Enum.with_index(positions), fn {p, idx} -> p - idx end)

      # build prefix sums of adjusted values
      {rev_pref, _} =
        Enum.reduce(adjusted, {[], 0}, fn val, {list, sum} ->
          new_sum = sum + val
          {[new_sum | list], new_sum}
        end)

      pref = [0 | Enum.reverse(rev_pref)]

      adj_arr = :array.from_list(adjusted)
      pref_arr = :array.from_list(pref)

      max_l = len - k
      min_cost(0, max_l, k, adj_arr, pref_arr, 1 <<< 60)
    end
  end

  defp min_cost(l, max_l, k, adj_arr, pref_arr, cur_min) when l > max_l do
    cur_min
  end

  defp min_cost(l, max_l, k, adj_arr, pref_arr, cur_min) do
    r = l + k - 1
    m = l + div(k, 2)

    median = :array.get(m, adj_arr)

    left_sum =
      median * (m - l) -
        (:array.get(m, pref_arr) - :array.get(l, pref_arr))

    right_sum =
      (:array.get(r + 1, pref_arr) - :array.get(m + 1, pref_arr)) -
        median * (r - m)

    total = left_sum + right_sum
    new_min = if total < cur_min, do: total, else: cur_min

    min_cost(l + 1, max_l, k, adj_arr, pref_arr, new_min)
  end
end
```
