# 1674. Minimum Moves to Make Array Complementary

## Cpp

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        int pairs = n / 2;
        int maxSum = 2 * limit;
        vector<int> diff(maxSum + 2, 0);
        vector<int> exact(maxSum + 1, 0);
        
        for (int i = 0; i < pairs; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int lo = min(a, b) + 1;
            int hi = max(a, b) + limit;
            diff[lo] += 1;
            if (hi + 1 <= maxSum) diff[hi + 1] -= 1;
            exact[a + b]++;
        }
        
        int ans = INT_MAX;
        int cur = 0;
        for (int s = 2; s <= maxSum; ++s) {
            cur += diff[s];
            int oneMovePossible = cur;
            int zeroMove = exact[s];
            int moves = 2 * pairs - oneMovePossible - zeroMove;
            ans = min(ans, moves);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;
        int pairs = n / 2;
        int maxSum = 2 * limit;
        int[] diff = new int[maxSum + 2]; // allow index up to maxSum+1

        for (int i = 0; i < pairs; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int sum = a + b;

            int lo = Math.min(a, b) + 1;
            int hi = Math.max(a, b) + limit;

            // One move needed for sums in [lo, hi]
            diff[lo] -= 1;
            diff[hi + 1] += 1;

            // Zero moves needed for the exact current sum
            diff[sum] -= 1;
            diff[sum + 1] += 1;
        }

        int base = pairs * 2; // start assuming two moves per pair
        int cur = 0;
        int ans = Integer.MAX_VALUE;

        for (int s = 2; s <= maxSum; ++s) {
            cur += diff[s];
            int moves = base + cur;
            if (moves < ans) ans = moves;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        pairs = n // 2
        size = 2 * limit + 2
        diff = [0] * (size + 1)  # extra slot to avoid index error

        for i in range(pairs):
            a = nums[i]
            b = nums[n - 1 - i]
            lo = min(a, b) + 1
            hi = max(a, b) + limit
            diff[lo] -= 1
            diff[hi + 1] += 1

            s = a + b
            diff[s] -= 1
            diff[s + 1] += 1

        best = float('inf')
        cur = 0
        base = 2 * pairs
        for x in range(2, 2 * limit + 1):
            cur += diff[x]
            moves = base + cur
            if moves < best:
                best = moves
        return best
```

## Python3

```python
class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        pairs = n // 2
        max_sum = 2 * limit
        diff = [0] * (max_sum + 2)   # for range updates
        exact = [0] * (max_sum + 2)  # count of sums achievable with 0 moves

        for i in range(pairs):
            a = nums[i]
            b = nums[n - 1 - i]
            lo = min(a, b) + 1
            hi = max(a, b) + limit
            diff[lo] -= 1
            diff[hi + 1] += 1
            exact[a + b] += 1

        cur = 0
        best = float('inf')
        base = 2 * pairs  # cost if every pair needs two moves
        for s in range(2, max_sum + 1):
            cur += diff[s]
            total = base + cur - exact[s]
            if total < best:
                best = total
        return best
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minMoves(int* nums, int numsSize, int limit) {
    int totalPairs = numsSize / 2;
    int maxSum = 2 * limit;

    int *pref = (int *)calloc(maxSum + 2, sizeof(int));
    int *exact = (int *)calloc(maxSum + 1, sizeof(int));

    for (int i = 0; i < totalPairs; ++i) {
        int a = nums[i];
        int b = nums[numsSize - 1 - i];

        int low = (a < b ? a : b) + 1;
        int high = (a > b ? a : b) + limit;

        pref[low] += 1;
        if (high + 1 <= maxSum)
            pref[high + 1] -= 1;

        exact[a + b] += 1;
    }

    int cur = 0;
    int ans = INT_MAX;
    for (int x = 2; x <= maxSum; ++x) {
        cur += pref[x];
        int moves = 2 * totalPairs - cur - exact[x];
        if (moves < ans)
            ans = moves;
    }

    free(pref);
    free(exact);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMoves(int[] nums, int limit) {
        int n = nums.Length;
        int pairs = n / 2;
        int maxSum = 2 * limit;
        int size = maxSum + 2; // need index up to maxSum+1
        int[] diff = new int[size];
        int[] sumFreq = new int[size];

        for (int i = 0; i < pairs; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int lo = Math.Min(a, b) + 1;
            int hi = Math.Max(a, b) + limit;

            diff[lo] += 1;
            if (hi + 1 < size) {
                diff[hi + 1] -= 1;
            }

            sumFreq[a + b] ++;
        }

        int[] atMostOne = new int[size];
        int cur = 0;
        for (int s = 2; s <= maxSum; s++) {
            cur += diff[s];
            atMostOne[s] = cur;
        }

        int result = int.MaxValue;
        int totalTwoMoves = pairs * 2;
        for (int s = 2; s <= maxSum; s++) {
            int moves = totalTwoMoves - atMostOne[s] - sumFreq[s];
            if (moves < result) result = moves;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var minMoves = function(nums, limit) {
    const n = nums.length;
    const totalPairs = n >> 1; // n / 2
    const maxSum = limit << 1; // 2 * limit

    const diff = new Array(maxSum + 2).fill(0);
    const exact = new Array(maxSum + 2).fill(0);

    for (let i = 0; i < totalPairs; ++i) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const sum = a + b;
        exact[sum]++;

        const low = Math.min(a, b) + 1;
        const high = Math.max(a, b) + limit;

        diff[low] += 1;
        diff[high + 1] -= 1;
    }

    let cur = 0;
    let ans = Infinity;
    for (let s = 2; s <= maxSum; ++s) {
        cur += diff[s]; // pairs that can be fixed with at most one change for sum s
        const moves = (totalPairs - cur) * 2 + (cur - exact[s]); // 2-move pairs + 1-move pairs
        if (moves < ans) ans = moves;
    }
    return ans;
};
```

## Typescript

```typescript
function minMoves(nums: number[], limit: number): number {
    const n = nums.length;
    const pairs = n >> 1;
    const maxSum = limit * 2;
    const diff = new Array(maxSum + 2).fill(0);

    for (let i = 0; i < pairs; i++) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const low = Math.min(a, b) + 1;
        const high = Math.max(a, b) + limit;

        diff[low] -= 1;
        diff[high + 1] += 1;

        const sum = a + b;
        diff[sum] -= 1;
        diff[sum + 1] += 1;
    }

    let cur = 0;
    let ans = Number.MAX_SAFE_INTEGER;
    const base = pairs * 2;

    for (let s = 2; s <= maxSum; s++) {
        cur += diff[s];
        const moves = base + cur;
        if (moves < ans) ans = moves;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer
     */
    function minMoves($nums, $limit) {
        $n = count($nums);
        $pairCount = intdiv($n, 2);
        $maxSum = $limit * 2;

        // diff array for range updates (pairs that can be fixed with 1 move)
        $diff = array_fill(0, $maxSum + 2, 0);
        // count of pairs already having exact sum
        $cntExact = array_fill(0, $maxSum + 2, 0);

        for ($i = 0; $i < $pairCount; $i++) {
            $a = $nums[$i];
            $b = $nums[$n - 1 - $i];
            $sum = $a + $b;
            $cntExact[$sum]++;

            $low = min($a, $b) + 1;
            $high = max($a, $b) + $limit;

            $diff[$low] += 1;
            if ($high + 1 <= $maxSum) {
                $diff[$high + 1] -= 1;
            }
        }

        // prefix to get number of pairs that need at most 1 move for each possible sum
        $oneMove = array_fill(0, $maxSum + 2, 0);
        $curr = 0;
        for ($s = 2; $s <= $maxSum; $s++) {
            $curr += $diff[$s];
            $oneMove[$s] = $curr;
        }

        $base = $pairCount * 2; // if every pair needs 2 moves
        $ans = PHP_INT_MAX;

        for ($s = 2; $s <= $maxSum; $s++) {
            // total moves = base - pairs needing only 1 move - pairs already correct
            $moves = $base - $oneMove[$s] - $cntExact[$s];
            if ($moves < $ans) {
                $ans = $moves;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ nums: [Int], _ limit: Int) -> Int {
        let n = nums.count
        let pairs = n / 2
        var diff = Array(repeating: 0, count: 2 * limit + 2)
        var exact = Array(repeating: 0, count: 2 * limit + 2)
        
        for i in 0..<pairs {
            let a = nums[i]
            let b = nums[n - 1 - i]
            let low = min(a, b) + 1
            let high = max(a, b) + limit
            diff[low] += 1
            if high + 1 < diff.count {
                diff[high + 1] -= 1
            }
            exact[a + b] += 1
        }
        
        var best = Int.max
        var cur = 0
        for sum in 2...2 * limit {
            cur += diff[sum]
            let moves = pairs * 2 - cur - exact[sum]
            if moves < best {
                best = moves
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        val n = nums.size
        val m = n / 2
        val maxSum = 2 * limit
        val diff = IntArray(maxSum + 2)
        val exact = IntArray(maxSum + 1)

        var i = 0
        while (i < m) {
            val a = nums[i]
            val b = nums[n - 1 - i]
            val sum = a + b
            exact[sum]++

            val low = kotlin.math.min(a, b) + 1
            val high = kotlin.math.max(a, b) + limit

            diff[low] += 1
            if (high + 1 <= maxSum) {
                diff[high + 1] -= 1
            }
            i++
        }

        var cur = 0
        var ans = Int.MAX_VALUE
        var x = 2
        while (x <= maxSum) {
            cur += diff[x]
            val moves = 2 * m - cur - exact[x]
            if (moves < ans) ans = moves
            x++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(List<int> nums, int limit) {
    int n = nums.length;
    int pairs = n ~/ 2;
    int maxSum = 2 * limit;

    List<int> diff = List.filled(maxSum + 2, 0);
    List<int> exact = List.filled(maxSum + 2, 0);

    for (int i = 0; i < pairs; ++i) {
      int a = nums[i];
      int b = nums[n - 1 - i];

      int low = (a < b ? a : b) + 1;
      int high = (a > b ? a : b) + limit;

      diff[low] -= 1;
      diff[high + 1] += 1;

      exact[a + b] += 1;
    }

    int base = pairs * 2;
    int cur = 0;
    int ans = n; // maximum possible moves is n

    for (int sum = 2; sum <= maxSum; ++sum) {
      cur += diff[sum];
      int moves = base + cur - exact[sum];
      if (moves < ans) ans = moves;
    }

    return ans;
  }
}
```

## Golang

```go
func minMoves(nums []int, limit int) int {
    n := len(nums)
    pairs := n / 2
    base := 2 * pairs
    // diff array for prefix sum, size up to 2*limit+1 (inclusive), plus extra for safety
    diff := make([]int, 2*limit+2)

    min := func(a, b int) int {
        if a < b {
            return a
        }
        return b
    }
    max := func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }

    for i := 0; i < pairs; i++ {
        a := nums[i]
        b := nums[n-1-i]

        lo := min(a, b) + 1
        hi := max(a, b) + limit

        diff[lo] -= 1
        if hi+1 < len(diff) {
            diff[hi+1] += 1
        }

        sum := a + b
        diff[sum] -= 1
        if sum+1 < len(diff) {
            diff[sum+1] += 1
        }
    }

    ans := base
    cur := 0
    for s := 2; s <= 2*limit; s++ {
        cur += diff[s]
        moves := base + cur
        if moves < ans {
            ans = moves
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_moves(nums, limit)
  n = nums.length
  m = n / 2
  max_sum = 2 * limit
  diff = Array.new(max_sum + 2, 0)

  base = 0
  (0...m).each do |i|
    a = nums[i]
    b = nums[n - 1 - i]
    sum = a + b
    low = [a, b].min + 1
    high = [a, b].max + limit

    diff[low] -= 1
    diff[high + 1] += 1

    diff[sum] -= 1
    diff[sum + 1] += 1

    base += 2
  end

  min_moves = Float::INFINITY
  cur = 0
  (2..max_sum).each do |s|
    cur += diff[s]
    total = base + cur
    min_moves = total if total < min_moves
  end

  min_moves
end
```

## Scala

```scala
object Solution {
    def minMoves(nums: Array[Int], limit: Int): Int = {
        val n = nums.length
        val pairs = n / 2
        val maxSum = 2 * limit
        // diff array for range updates, size enough to include index maxSum+1
        val diff = new Array[Int](maxSum + 3)
        var i = 0
        while (i < pairs) {
            val a = nums(i)
            val b = nums(n - 1 - i)
            val lo = Math.min(a, b) + 1          // start of range needing only 1 move
            val hi = Math.max(a, b) + limit      // end of that range
            diff(lo) -= 1
            diff(hi + 1) += 1
            val sum = a + b                       // exact sum needs 0 moves
            diff(sum) -= 1
            diff(sum + 1) += 1
            i += 1
        }
        var cur = 0
        var ans = Int.MaxValue
        var x = 2
        while (x <= maxSum) {
            cur += diff(x)
            val totalMoves = cur + 2 * pairs     // base cost 2 per pair plus adjustments
            if (totalMoves < ans) ans = totalMoves
            x += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let lim = limit as usize;
        let max_sum = 2 * lim;
        let mut diff = vec![0i32; max_sum + 2];
        let mut exact = vec![0i32; max_sum + 1];

        for i in 0..n / 2 {
            let a = nums[i] as usize;
            let b = nums[n - 1 - i] as usize;
            let sum = a + b;
            exact[sum] += 1;

            let lo = std::cmp::min(a, b) + 1;
            let hi = std::cmp::max(a, b) + lim;
            diff[lo] += 1;
            if hi + 1 <= max_sum {
                diff[hi + 1] -= 1;
            }
        }

        let total_pairs = (n / 2) as i32;
        let base = 2 * total_pairs;

        let mut ans = i32::MAX;
        let mut cur = 0i32;
        for x in 2..=max_sum {
            cur += diff[x];
            // moves = base - rangeCount[x] - exact[x]
            let moves = base - cur - exact[x];
            if moves < ans {
                ans = moves;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-moves nums limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (pairs (/ n 2))
         (max-sum (* 2 limit))
         (diff (make-vector (+ max-sum 2) 0))
         (cnt (make-vector (+ max-sum 1) 0))
         (vec (list->vector nums)))
    ;; process each pair
    (for ([i (in-range pairs)])
      (let* ((a (vector-ref vec i))
             (b (vector-ref vec (- n 1 i)))
             (low (+ (min a b) 1))
             (high (+ (max a b) limit))
             (sum (+ a b)))
        ;; range update for at most one change
        (vector-set! diff low (+ 1 (vector-ref diff low)))
        (let ((idx (+ high 1)))
          (when (< idx (vector-length diff))
            (vector-set! diff idx (- (vector-ref diff idx) 1))))
        ;; count exact sum (zero changes)
        (vector-set! cnt sum (+ 1 (vector-ref cnt sum)))))
    ;; sweep to find minimal moves
    (let ((cur 0)
          (best most-positive-fixnum))
      (for ([s (in-range 2 (+ max-sum 1))])
        (set! cur (+ cur (vector-ref diff s)))
        (let* ((zero (vector-ref cnt s))
               (moves (- (* 2 pairs) cur zero))) ; moves = 2*pairs - cur - zero
          (when (< moves best)
            (set! best moves))))
      best)))
```

## Erlang

```erlang
-spec min_moves(Nums :: [integer()], Limit :: integer()) -> integer().
min_moves(Nums, Limit) ->
    N = length(Nums),
    Half = N div 2,
    First = lists:sublist(Nums, Half),
    SecondRev = lists:reverse(lists:nthtail(Half, Nums)),
    Diff = build_diff(First, SecondRev, Limit, #{}),
    Base = 2 * Half,
    MaxSum = 2 * Limit,
    calc_min(Diff, MaxSum, Base).

build_diff([], [], _Limit, Diff) ->
    Diff;
build_diff([A|As], [B|Bs], Limit, Diff) ->
    Lo = erlang:min(A, B) + 1,
    Hi = erlang:max(A, B) + Limit,
    S = A + B,
    D1 = update(Diff, Lo, -1),
    D2 = update(D1, Hi + 1, 1),
    D3 = update(D2, S, -1),
    D4 = update(D3, S + 1, 1),
    build_diff(As, Bs, Limit, D4).

update(Map, Key, Delta) ->
    maps:update_with(Key,
        fun(V) -> V + Delta end,
        Delta,
        Map).

calc_min(Diff, MaxSum, Base) ->
    calc_min_seq(2, MaxSum, Diff, 0, Base, Base).

calc_min_seq(Cur, Max, _Diff, _Cum, _Base, Min) when Cur > Max ->
    Min;
calc_min_seq(Cur, Max, Diff, Cum, Base, Min) ->
    Delta = maps:get(Cur, Diff, 0),
    NewCum = Cum + Delta,
    Moves = Base + NewCum,
    NewMin = if Moves < Min -> Moves; true -> Min end,
    calc_min_seq(Cur + 1, Max, Diff, NewCum, Base, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(nums :: [integer], limit :: integer) :: integer
  def min_moves(nums, limit) do
    n = length(nums)
    total_pairs = div(n, 2)
    max_sum = 2 * limit

    pref = :array.new(max_sum + 2, default: 0)
    cnt = :array.new(max_sum + 2, default: 0)

    {pref, cnt} =
      Enum.reduce(0..total_pairs - 1, {pref, cnt}, fn i, {pref_acc, cnt_acc} ->
        a = Enum.at(nums, i)
        b = Enum.at(nums, n - 1 - i)

        low = min(a, b) + 1
        high = max(a, b) + limit

        pref_acc =
          :array.set(low, (:array.get(low, pref_acc) + 1), pref_acc)
        pref_acc =
          :array.set(high + 1, (:array.get(high + 1, pref_acc) - 1), pref_acc)

        sum = a + b
        cnt_acc = :array.set(sum, (:array.get(sum, cnt_acc) + 1), cnt_acc)

        {pref_acc, cnt_acc}
      end)

    result =
      Enum.reduce(2..max_sum, %{cur: 0, best: 1_000_000_000}, fn x, acc ->
        cur = acc.cur + :array.get(x, pref)
        one_move = cur
        zero_move = :array.get(x, cnt)
        moves = 2 * total_pairs - one_move - zero_move

        best = if moves < acc.best, do: moves, else: acc.best
        %{cur: cur, best: best}
      end)

    result.best
  end
end
```
