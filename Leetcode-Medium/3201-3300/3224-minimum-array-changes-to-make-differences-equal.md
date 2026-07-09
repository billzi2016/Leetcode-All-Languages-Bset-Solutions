# 3224. Minimum Array Changes to Make Differences Equal

## Cpp

```cpp
class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        int m = n / 2;
        int maxSum = 2 * k;
        vector<int> cnt(maxSum + 2, 0);
        vector<int> diff(maxSum + 3, 0); // extra space for hi+1
        
        for (int i = 0; i < m; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int sum = a + b;
            cnt[sum]++;
            
            int lo = min(a, b) + 1;
            int hi = max(a, b) + k;
            diff[lo] += 1;
            diff[hi + 1] -= 1;
        }
        
        int cur = 0;
        int ans = INT_MAX;
        for (int x = 2; x <= maxSum; ++x) { // possible sums are at least 0, but start from 2 to avoid unused low indices
            cur += diff[x];
            int oneOrZero = cur;          // pairs that need at most one change for sum x
            int zero = cnt[x];            // pairs already have sum x (need 0 changes)
            int one = oneOrZero - zero;   // exactly one change needed
            int two = m - oneOrZero;      // need two changes
            int changes = one + 2 * two;
            ans = min(ans, changes);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minChanges(int[] nums, int k) {
        int n = nums.length;
        int pairs = n / 2;
        int[] oneChangeDiff = new int[k + 2];
        int[] exactFreq = new int[k + 1];

        for (int i = 0; i < pairs; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int diff = Math.abs(a - b);
            exactFreq[diff]++;

            int min = Math.min(a, b);
            int max = Math.max(a, b);
            int limit = Math.max(k - min, max); // maximum X achievable with at most one change

            oneChangeDiff[0] += 1;
            if (limit + 1 <= k) {
                oneChangeDiff[limit + 1] -= 1;
            } else {
                // limit == k, decrement at position k+1 which exists
                oneChangeDiff[k + 1] -= 1;
            }
        }

        int curOneChange = 0;
        int minChanges = Integer.MAX_VALUE;
        for (int x = 0; x <= k; x++) {
            curOneChange += oneChangeDiff[x];
            int changes = 2 * pairs - curOneChange - exactFreq[x];
            if (changes < minChanges) {
                minChanges = changes;
            }
        }
        return minChanges;
    }
}
```

## Python

```python
class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        m = n // 2
        max_sum = 2 * k
        diff = [0] * (max_sum + 2)          # for prefix sums, need index up to max_sum+1
        exact = [0] * (max_sum + 1)         # count of pairs already having sum X

        for i in range(m):
            a = nums[i]
            b = nums[n - 1 - i]
            if a > b:
                a, b = b, a
            s = a + b
            exact[s] += 1

            lo = a + 1               # minimum X that can be achieved with one change
            hi = b + k               # maximum X that can be achieved with one change
            diff[lo] += 1
            diff[hi + 1] -= 1

        ans = float('inf')
        cur_one_change = 0
        for x in range(max_sum + 1):
            cur_one_change += diff[x]
            # total changes = 2*m - (pairs needing at most one change) - (pairs already correct)
            changes = 2 * m - cur_one_change - exact[x]
            if changes < ans:
                ans = changes
        return ans
```

## Python3

```python
class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        n = len(nums)
        m = n // 2
        freqDiff = [0] * (k + 1)
        diffArr = [0] * (k + 2)   # for prefix sums up to index k+1

        for i in range(m):
            a = nums[i]
            b = nums[n - 1 - i]
            low, high = (a, b) if a <= b else (b, a)
            d = high - low
            freqDiff[d] += 1

            limit = max(high, k - low)
            if limit < k:
                diffArr[limit + 1] += 1
                diffArr[k + 1] -= 1

        ans = float('inf')
        two_cnt = 0
        for x in range(k + 1):
            two_cnt += diffArr[x]
            changes = m + two_cnt - freqDiff[x]
            if changes < ans:
                ans = changes
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minChanges(int* nums, int numsSize, int k) {
    int m = numsSize / 2;
    int *exact = (int*)calloc(k + 1, sizeof(int));
    int *pref = (int*)calloc(k + 2, sizeof(int));

    for (int i = 0; i < m; ++i) {
        int a = nums[i];
        int b = nums[numsSize - 1 - i];
        int d = a > b ? a - b : b - a;
        exact[d]++;

        int tA = a > k - a ? a : k - a;
        int tB = b > k - b ? b : k - b;
        int T = tA > tB ? tA : tB;

        pref[0] += 1;
        if (T + 1 <= k) pref[T + 1] -= 1;
    }

    int best = INT_MAX;
    int cur = 0;
    for (int x = 0; x <= k; ++x) {
        cur += pref[x];
        int changes = 2 * m - cur - exact[x];
        if (changes < best) best = changes;
    }

    free(exact);
    free(pref);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinChanges(int[] nums, int k) {
        int n = nums.Length;
        int m = n / 2;
        int[] diffCount = new int[k + 1];
        int[] pref = new int[k + 2]; // for range updates

        for (int i = 0; i < m; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int d = Math.Abs(a - b);
            diffCount[d]++;

            int limitA = Math.Max(a, k - a);
            int limitB = Math.Max(b, k - b);
            int limit = Math.Max(limitA, limitB); // max X achievable with one change

            pref[0] += 1;
            if (limit + 1 <= k) {
                pref[limit + 1] -= 1;
            }
        }

        int[] oneChangePossible = new int[k + 1];
        int cur = 0;
        for (int x = 0; x <= k; x++) {
            cur += pref[x];
            oneChangePossible[x] = cur;
        }

        int baseCost = 2 * m;
        int answer = int.MaxValue;
        for (int x = 0; x <= k; x++) {
            int changes = baseCost - diffCount[x] - oneChangePossible[x];
            if (changes < answer) answer = changes;
        }
        return answer;
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
var minChanges = function(nums, k) {
    const n = nums.length;
    const pairs = n >> 1; // n is even
    const diffCount = new Array(k + 2).fill(0);
    const greaterDiff = new Array(k + 2).fill(0); // difference array for cntGreater
    
    for (let i = 0; i < pairs; ++i) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const d = Math.abs(a - b);
        diffCount[d]++;

        const limitA = Math.max(a, k - a);
        const limitB = Math.max(b, k - b);
        const L = Math.max(limitA, limitB); // max X that can be achieved with at most one change

        if (L + 1 <= k) {
            greaterDiff[L + 1] += 1; // for all X > L we need two changes
        }
    }

    // prefix sum to get cntGreater for each X
    const cntGreater = new Array(k + 1).fill(0);
    let cur = 0;
    for (let x = 0; x <= k; ++x) {
        cur += greaterDiff[x];
        cntGreater[x] = cur;
    }

    let answer = Number.MAX_SAFE_INTEGER;
    const totalPairs = pairs;

    for (let x = 0; x <= k; ++x) {
        const changes = totalPairs + cntGreater[x] - diffCount[x];
        if (changes < answer) answer = changes;
    }
    return answer;
};
```

## Typescript

```typescript
function minChanges(nums: number[], k: number): number {
    const n = nums.length;
    const m = n >> 1; // number of pairs
    const base = 2 * m; // assume each pair needs two changes
    const reduce = new Array(k + 2).fill(0); // prefix sum for one‑change reductions
    const zeroCount = new Array(k + 1).fill(0); // exact diff counts

    for (let i = 0; i < m; ++i) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const low = Math.min(a, b);
        const high = Math.max(a, b);
        const d = high - low;
        zeroCount[d]++;

        const limit = Math.max(high, k - low); // max X that can be achieved with one change
        reduce[0] += 1;
        if (limit + 1 <= k) {
            reduce[limit + 1] -= 1;
        }
    }

    let minOps = Number.MAX_SAFE_INTEGER;
    let curReduction = 0;
    for (let x = 0; x <= k; ++x) {
        curReduction += reduce[x];
        const ops = base - curReduction - zeroCount[x];
        if (ops < minOps) minOps = ops;
    }
    return minOps;
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
    function minChanges($nums, $k) {
        $n = count($nums);
        $m = intdiv($n, 2); // number of pairs
        $maxSum = $k * 2;
        $size = $maxSum + 3; // extra space for diff end index

        $diff = array_fill(0, $size, 0);
        $exact = array_fill(0, $size, 0);

        for ($i = 0; $i < $m; ++$i) {
            $a = $nums[$i];
            $b = $nums[$i + $m];

            $sum = $a + $b;
            $exact[$sum]++;

            $low = min($a, $b);
            $high = max($a, $b) + $k;

            $diff[$low] += 1;
            if ($high + 1 < $size) {
                $diff[$high + 1] -= 1;
            }
        }

        // prefix sum to get count of pairs that can be fixed with at most one change
        $cntOneOrZero = array_fill(0, $maxSum + 1, 0);
        $cur = 0;
        for ($s = 0; $s <= $maxSum; ++$s) {
            $cur += $diff[$s];
            $cntOneOrZero[$s] = $cur;
        }

        $ans = PHP_INT_MAX;
        $totalPairs = $m;
        for ($x = 0; $x <= $maxSum; ++$x) {
            // changes = 2 * totalPairs - cntOneOrZero[x] - exact[x]
            $changes = 2 * $totalPairs - $cntOneOrZero[$x] - $exact[$x];
            if ($changes < $ans) {
                $ans = $changes;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minChanges(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let pairs = n / 2
        let maxX = 2 * k
        var diff = [Int](repeating: 0, count: maxX + 2)
        var zeroCount = [Int](repeating: 0, count: maxX + 1)
        
        for i in 0..<pairs {
            let a = nums[i]
            let b = nums[i + pairs]
            let low = min(a, b) + 1
            let high = max(a, b) + k
            if low <= high {
                diff[low] += 1
                if high + 1 < diff.count {
                    diff[high + 1] -= 1
                }
            }
            zeroCount[a + b] += 1
        }
        
        var oneChange = [Int](repeating: 0, count: maxX + 1)
        var cur = 0
        for x in 0...maxX {
            cur += diff[x]
            oneChange[x] = cur
        }
        
        var ans = Int.max
        let base = pairs * 2
        for X in 0...maxX {
            let changes = base - oneChange[X] - zeroCount[X]
            if changes < ans {
                ans = changes
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minChanges(nums: IntArray, k: Int): Int {
        val n = nums.size
        val m = n / 2
        val cntDiff = IntArray(k + 1)
        val diff = IntArray(k + 2) // difference array for prefix sums

        for (i in 0 until m) {
            val a = nums[i]
            val b = nums[i + m]
            val d = kotlin.math.abs(a - b)
            cntDiff[d]++

            val minVal = kotlin.math.min(a, b)
            val maxVal = kotlin.math.max(a, b)
            val t = kotlin.math.max(maxVal, k - minVal) // max X achievable with ≤1 change

            diff[0] += 1
            if (t + 1 <= k) {
                diff[t + 1] -= 1
            }
        }

        var cur = 0
        val totalPairs = m
        var answer = Int.MAX_VALUE
        for (x in 0..k) {
            cur += diff[x]
            // pairs needing at most one change for this X is cur
            val changes = 2 * totalPairs - cur - cntDiff[x]
            if (changes < answer) answer = changes
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minChanges(List<int> nums, int k) {
    int n = nums.length;
    int pairs = n ~/ 2;
    int maxSum = 2 * k;
    List<int> diff = List.filled(maxSum + 2, 0);
    Map<int, int> sumCount = {};

    for (int i = 0; i < pairs; ++i) {
      int a = nums[i];
      int b = nums[n - 1 - i];
      int lo = (a < b ? a : b) + 1;
      int hi = (a > b ? a : b) + k;

      diff[lo] += 1;
      if (hi + 1 < diff.length) {
        diff[hi + 1] -= 1;
      }

      int s = a + b;
      sumCount[s] = (sumCount[s] ?? 0) + 1;
    }

    int cur = 0;
    int ans = n; // maximum possible changes
    for (int x = 0; x <= maxSum; ++x) {
      cur += diff[x];
      int oneChangePossible = cur;
      int zeroChangePossible = sumCount[x] ?? 0;
      int changes = pairs * 2 - oneChangePossible - zeroChangePossible;
      if (changes < ans) ans = changes;
    }
    return ans;
  }
}
```

## Golang

```go
func minChanges(nums []int, k int) int {
    n := len(nums)
    pairs := n / 2
    totalTwo := 2 * pairs

    size := 2*k + 2
    diff := make([]int, size+2)
    zeroCnt := make([]int, size+2)

    for i := 0; i < pairs; i++ {
        a := nums[i]
        b := nums[n-1-i]
        if a > b {
            a, b = b, a
        }
        lo := a + 1
        hi := b + k
        diff[lo] -= 1
        diff[hi+1] += 1

        sum := a + b
        zeroCnt[sum]++
    }

    ans := n
    cur := 0
    for x := 2; x <= 2*k; x++ {
        cur += diff[x]
        moves := totalTwo + cur - zeroCnt[x]
        if moves < ans {
            ans = moves
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_changes(nums, k)
  n = nums.length
  pairs = n / 2
  diff_cnt = Array.new(k + 1, 0)
  pref = Array.new(k + 2, 0)

  (0...pairs).each do |i|
    a = nums[i]
    b = nums[n - 1 - i]
    low = a < b ? a : b
    high = a > b ? a : b
    diff = high - low
    max_needed = [high, k - low].max

    pref[0] += 1
    if max_needed + 1 <= k
      pref[max_needed + 1] -= 1
    end

    diff_cnt[diff] += 1
  end

  ans = n
  count_one = 0
  (0..k).each do |x|
    count_one += pref[x]
    zero = diff_cnt[x]
    changes = 2 * pairs - count_one - zero
    ans = changes if changes < ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minChanges(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val m = n / 2
        val maxSum = 2 * k
        val cnt = new Array[Int](maxSum + 1)
        val diff = new Array[Int](maxSum + 2) // extra slot for hi+1

        var i = 0
        while (i < m) {
            val a = nums(i)
            val b = nums(n - 1 - i)
            cnt(a + b) += 1
            val lo = Math.min(a, b) + 1
            val hi = Math.max(a, b) + k
            diff(lo) += 1
            if (hi + 1 <= maxSum + 1) {
                diff(hi + 1) -= 1
            }
            i += 1
        }

        var pref = 0
        var ans = Int.MaxValue
        var x = 0
        while (x <= maxSum) {
            pref += diff(x)
            val changes = 2 * m - pref - cnt(x)
            if (changes < ans) ans = changes
            x += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let m = n / 2;
        let k_usize = k as usize;
        let mut diff_cnt = vec![0i32; k_usize + 1];
        let mut thresh_cnt = vec![0i32; k_usize + 1];

        for i in 0..m {
            let mut a = nums[i];
            let mut b = nums[n - 1 - i];
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            let d = (b - a) as usize;
            diff_cnt[d] += 1;

            // maximum X achievable with at most one change for this pair
            let t_val = std::cmp::max(b, k - a);
            let t = t_val as usize;
            thresh_cnt[t] += 1;
        }

        // suffix sums of thresholds: suff[x] = number of pairs with threshold >= x
        let mut suff = vec![0i32; k_usize + 2];
        for i in (0..=k_usize).rev() {
            suff[i] = thresh_cnt[i] + suff[i + 1];
        }

        let total_pairs = m as i32;
        let mut answer = i32::MAX;
        for x in 0..=k_usize {
            let one_or_less = suff[x];
            let exact = diff_cnt[x];
            let changes = 2 * total_pairs - one_or_less - exact;
            if changes < answer {
                answer = changes;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (min-changes nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((nums-v (list->vector nums))
         (n (vector-length nums-v))
         (pairs (/ n 2))
         (max-sum (* 2 k))
         (size (+ max-sum 2)) ; extra slot for hi+1
         (diff (make-vector size 0))
         (exact (make-vector size 0)))
    ;; process each pair
    (for ([i (in-range pairs)])
      (let* ((a (vector-ref nums-v i))
             (b (vector-ref nums-v (- n 1 i)))
             (lo (+ (min a b) 1))
             (hi (+ (max a b) k))
             (sum (+ a b)))
        ;; range update for one‑change possibility
        (vector-set! diff lo (+ (vector-ref diff lo) 1))
        (when (< (+ hi 1) size)
          (vector-set! diff (+ hi 1) (- (vector-ref diff (+ hi 1)) 1)))
        ;; exact sum count
        (vector-set! exact sum (+ (vector-ref exact sum) 1))))
    ;; prefix sums to obtain counts of pairs doable with ≤1 change
    (define one-change (make-vector size 0))
    (let loop ((i 0) (cur 0))
      (when (< i size)
        (set! cur (+ cur (vector-ref diff i)))
        (vector-set! one-change i cur)
        (loop (+ i 1) cur)))
    ;; evaluate minimal moves over all possible target sums
    (define min-moves (* pairs 2)) ; worst case: change both elements of every pair
    (for ([s (in-range (add1 max-sum))]) ; s = 0 .. 2k
      (let* ((zero (vector-ref exact s))
             (one (- (vector-ref one-change s) zero))
             (moves (- (* pairs 2) (* zero 2) one)))
        (when (< moves min-moves)
          (set! min-moves moves))))
    min-moves))
```

## Erlang

```erlang
-spec min_changes(Nums :: [integer()], K :: integer()) -> integer().
min_changes(Nums, K) ->
    M = length(Nums) div 2,
    {First, Second} = lists:split(M, Nums),
    DiffMap0 = maps:new(),
    FreqMap0 = maps:new(),
    {DiffMap, FreqMap} = process_pairs(First, Second, K, DiffMap0, FreqMap0),
    MaxRed = compute_max_reduction(0, M, 0, K, DiffMap, FreqMap),
    2 * M - MaxRed.

process_pairs([], [], _K, DiffMap, FreqMap) ->
    {DiffMap, FreqMap};
process_pairs([A|As], [B|Bs], K, DiffMap, FreqMap) ->
    Low = if A < B -> A; true -> B end,
    High = if A > B -> A; true -> B end,
    D = High - Low,
    Mpair = erlang:max(K - Low, High),
    Pos = Mpair + 1,
    DiffMap1 = maps:update_with(Pos, fun(V) -> V - 1 end, -1, DiffMap),
    FreqMap1 = maps:update_with(D, fun(V) -> V + 1 end, 1, FreqMap),
    process_pairs(As, Bs, K, DiffMap1, FreqMap1).

compute_max_reduction(Index, CurOne, MaxRed, K, DiffMap, FreqMap) when Index > K ->
    MaxRed;
compute_max_reduction(Index, CurOne, MaxRed, K, DiffMap, FreqMap) ->
    Delta = maps:get(Index, DiffMap, 0),
    NewCur = CurOne + Delta,
    Zero = maps:get(Index, FreqMap, 0),
    Red = NewCur + Zero,
    NewMax = if Red > MaxRed -> Red; true -> MaxRed end,
    compute_max_reduction(Index + 1, NewCur, NewMax, K, DiffMap, FreqMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_changes(nums :: [integer], k :: integer) :: integer
  def min_changes(nums, k) do
    n = length(nums)
    half = div(n, 2)

    {freq_exact, freq_hi} =
      Enum.reduce(0..half - 1, {%{}, %{}}, fn i, {fe, fh} ->
        a = Enum.at(nums, i)
        b = Enum.at(nums, n - 1 - i)

        d = abs(a - b)
        fe = Map.update(fe, d, 1, &(&1 + 1))

        max_a = max(a, k - a)
        max_b = max(b, k - b)
        hi = max(max_a, max_b)
        fh = Map.update(fh, hi, 1, &(&1 + 1))

        {fe, fh}
      end)

    base = half * 2

    {min_total, _} =
      Enum.reduce(Enum.reverse(0..k), {base * 2, 0}, fn x, {min_val, cur} ->
        cur = cur + Map.get(freq_hi, x, 0)
        total = base - cur - Map.get(freq_exact, x, 0)
        min_val = if total < min_val, do: total, else: min_val
        {min_val, cur}
      end)

    min_total
  end
end
```
