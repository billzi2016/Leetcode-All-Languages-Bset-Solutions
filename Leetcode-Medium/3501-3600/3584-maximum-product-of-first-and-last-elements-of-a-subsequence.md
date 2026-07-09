# 3584. Maximum Product of First and Last Elements of a Subsequence

## Cpp

```cpp
class Solution {
public:
    long long maximumProduct(vector<int>& nums, int m) {
        int n = nums.size();
        vector<long long> suffixMax(n), suffixMin(n);
        for (int i = n - 1; i >= 0; --i) {
            if (i == n - 1) {
                suffixMax[i] = suffixMin[i] = nums[i];
            } else {
                suffixMax[i] = max<long long>(nums[i], suffixMax[i + 1]);
                suffixMin[i] = min<long long>(nums[i], suffixMin[i + 1]);
            }
        }
        long long ans = LLONG_MIN;
        for (int i = 0; i <= n - m; ++i) {
            int j = i + m - 1;
            long long a = nums[i];
            long long cand1 = a * suffixMax[j];
            long long cand2 = a * suffixMin[j];
            ans = max(ans, max(cand1, cand2));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumProduct(int[] nums, int m) {
        int n = nums.length;
        if (m == 1) {
            long ans = Long.MIN_VALUE;
            for (int x : nums) {
                long prod = (long) x * x;
                if (prod > ans) ans = prod;
            }
            return ans;
        }

        long answer = Long.MIN_VALUE;
        int maxSoFar = Integer.MIN_VALUE;
        int minSoFar = Integer.MAX_VALUE;

        for (int j = m - 1; j < n; ++j) {
            int idx = j - (m - 1);
            int val = nums[idx];
            if (val > maxSoFar) maxSoFar = val;
            if (val < minSoFar) minSoFar = val;

            long candidate1 = (long) maxSoFar * nums[j];
            long candidate2 = (long) minSoFar * nums[j];
            long best = candidate1 > candidate2 ? candidate1 : candidate2;
            if (best > answer) answer = best;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maximumProduct(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if m == 1:
            return max(x * x for x in nums)

        # suffix max and min arrays
        suff_max = [0] * n
        suff_min = [0] * n
        cur_max = -10**18
        cur_min = 10**18
        for i in range(n - 1, -1, -1):
            v = nums[i]
            if v > cur_max:
                cur_max = v
            if v < cur_min:
                cur_min = v
            suff_max[i] = cur_max
            suff_min[i] = cur_min

        ans = -10**18
        limit = n - m + 1
        for i in range(limit):
            j_start = i + m - 1
            a = nums[i]
            prod1 = a * suff_max[j_start]
            prod2 = a * suff_min[j_start]
            if prod1 > ans:
                ans = prod1
            if prod2 > ans:
                ans = prod2

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if m == 1:
            return max(x * x for x in nums)

        # suffix max and min
        suff_max = [0] * n
        suff_min = [0] * n
        suff_max[-1] = nums[-1]
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            v = nums[i]
            suff_max[i] = v if v > suff_max[i + 1] else suff_max[i + 1]
            suff_min[i] = v if v < suff_min[i + 1] else suff_min[i + 1]

        ans = -10**30
        limit = n - m + 1
        for i in range(limit):
            idx = i + m - 1
            a = nums[i]
            prod1 = a * suff_max[idx]
            prod2 = a * suff_min[idx]
            if prod1 > ans:
                ans = prod1
            if prod2 > ans:
                ans = prod2

        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

long long maximumProduct(int* nums, int numsSize, int m) {
    if (numsSize == 0) return 0;
    int n = numsSize;
    int *sufMax = (int *)malloc(n * sizeof(int));
    int *sufMin = (int *)malloc(n * sizeof(int));
    sufMax[n - 1] = nums[n - 1];
    sufMin[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        sufMax[i] = nums[i] > sufMax[i + 1] ? nums[i] : sufMax[i + 1];
        sufMin[i] = nums[i] < sufMin[i + 1] ? nums[i] : sufMin[i + 1];
    }
    long long ans = LLONG_MIN;
    for (int i = 0; i <= n - m; ++i) {
        int idx = i + m - 1;
        long long a = (long long)nums[i];
        long long prod1 = a * (long long)sufMax[idx];
        long long prod2 = a * (long long)sufMin[idx];
        if (prod1 > ans) ans = prod1;
        if (prod2 > ans) ans = prod2;
    }
    free(sufMax);
    free(sufMin);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumProduct(int[] nums, int m) {
        int n = nums.Length;
        if (m == 1) {
            long best = long.MinValue;
            foreach (int v in nums) {
                long prod = (long)v * v;
                if (prod > best) best = prod;
            }
            return best;
        }

        long[] maxSuf = new long[n];
        long[] minSuf = new long[n];

        maxSuf[n - 1] = nums[n - 1];
        minSuf[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            maxSuf[i] = Math.Max(nums[i], maxSuf[i + 1]);
            minSuf[i] = Math.Min(nums[i], minSuf[i + 1]);
        }

        long answer = long.MinValue;
        for (int i = 0; i <= n - m; ++i) {
            int startIdx = i + m - 1; // earliest possible last index
            long firstVal = nums[i];
            long cand1 = firstVal * maxSuf[startIdx];
            long cand2 = firstVal * minSuf[startIdx];
            if (cand1 > answer) answer = cand1;
            if (cand2 > answer) answer = cand2;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number}
 */
var maximumProduct = function(nums, m) {
    const n = nums.length;
    if (m === 1) {
        let best = -Infinity;
        for (let x of nums) {
            const prod = x * x;
            if (prod > best) best = prod;
        }
        return best;
    }
    let curMax = -Infinity;
    let curMin = Infinity;
    let ans = -Infinity;
    // j is the index of the last element
    for (let j = m - 1; j < n; ++j) {
        const i = j - (m - 1); // new eligible first-element index
        const val = nums[i];
        if (val > curMax) curMax = val;
        if (val < curMin) curMin = val;
        const lastVal = nums[j];
        const prod1 = lastVal * curMax;
        const prod2 = lastVal * curMin;
        if (prod1 > ans) ans = prod1;
        if (prod2 > ans) ans = prod2;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumProduct(nums: number[], m: number): number {
    const n = nums.length;
    const suffMax = new Array<number>(n);
    const suffMin = new Array<number>(n);
    let curMax = -Infinity;
    let curMin = Infinity;
    for (let i = n - 1; i >= 0; --i) {
        if (nums[i] > curMax) curMax = nums[i];
        if (nums[i] < curMin) curMin = nums[i];
        suffMax[i] = curMax;
        suffMin[i] = curMin;
    }
    let ans = -Infinity;
    for (let i = 0; i <= n - m; ++i) {
        const idx = i + m - 1;
        const a = nums[i];
        const prod1 = a * suffMax[idx];
        const prod2 = a * suffMin[idx];
        if (prod1 > ans) ans = prod1;
        if (prod2 > ans) ans = prod2;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $m
     * @return Integer
     */
    function maximumProduct($nums, $m) {
        $n = count($nums);
        $suffixMax = array_fill(0, $n, 0);
        $suffixMin = array_fill(0, $n, 0);

        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i == $n - 1) {
                $suffixMax[$i] = $nums[$i];
                $suffixMin[$i] = $nums[$i];
            } else {
                $suffixMax[$i] = max($nums[$i], $suffixMax[$i + 1]);
                $suffixMin[$i] = min($nums[$i], $suffixMin[$i + 1]);
            }
        }

        $ans = PHP_INT_MIN;
        for ($i = 0; $i <= $n - $m; $i++) {
            $j = $i + $m - 1;
            $maxVal = $suffixMax[$j];
            $minVal = $suffixMin[$j];

            $prod1 = $nums[$i] * $maxVal;
            $prod2 = $nums[$i] * $minVal;

            if ($prod1 > $ans) $ans = $prod1;
            if ($prod2 > $ans) $ans = $prod2;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumProduct(_ nums: [Int], _ m: Int) -> Int {
        let n = nums.count
        if m == 1 {
            var best = Int.min
            for v in nums {
                let prod = v * v
                if prod > best { best = prod }
            }
            return best
        }
        var maxSuf = Array(repeating: 0, count: n)
        var minSuf = Array(repeating: 0, count: n)
        maxSuf[n - 1] = nums[n - 1]
        minSuf[n - 1] = nums[n - 1]
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                let val = nums[i]
                maxSuf[i] = max(val, maxSuf[i + 1])
                minSuf[i] = min(val, minSuf[i + 1])
            }
        }
        var ans = Int.min
        for i in 0...(n - m) {
            let jIdx = i + m - 1
            let a = nums[i]
            let cand1 = a * maxSuf[jIdx]
            if cand1 > ans { ans = cand1 }
            let cand2 = a * minSuf[jIdx]
            if cand2 > ans { ans = cand2 }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumProduct(nums: IntArray, m: Int): Long {
        val n = nums.size
        if (m == 1) {
            var ans = Long.MIN_VALUE
            for (v in nums) {
                val prod = v.toLong() * v.toLong()
                if (prod > ans) ans = prod
            }
            return ans
        }
        val suffixMax = IntArray(n)
        val suffixMin = IntArray(n)
        var curMax = nums[n - 1]
        var curMin = nums[n - 1]
        for (i in n - 1 downTo 0) {
            if (nums[i] > curMax) curMax = nums[i]
            if (nums[i] < curMin) curMin = nums[i]
            suffixMax[i] = curMax
            suffixMin[i] = curMin
        }
        var ans = Long.MIN_VALUE
        for (i in 0 until n) {
            val start = i + m - 1
            if (start >= n) break
            val a = nums[i].toLong()
            val cand1 = a * suffixMax[start].toLong()
            val cand2 = a * suffixMin[start].toLong()
            val best = if (cand1 > cand2) cand1 else cand2
            if (best > ans) ans = best
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumProduct(List<int> nums, int m) {
    int n = nums.length;
    if (m == 1) {
      int ans = -9223372036854775808;
      for (int v in nums) {
        int prod = v * v;
        if (prod > ans) ans = prod;
      }
      return ans;
    }

    List<int> suffixMax = List.filled(n, 0);
    List<int> suffixMin = List.filled(n, 0);
    suffixMax[n - 1] = nums[n - 1];
    suffixMin[n - 1] = nums[n - 1];

    for (int i = n - 2; i >= 0; --i) {
      suffixMax[i] = nums[i] > suffixMax[i + 1] ? nums[i] : suffixMax[i + 1];
      suffixMin[i] = nums[i] < suffixMin[i + 1] ? nums[i] : suffixMin[i + 1];
    }

    int ans = -9223372036854775808;
    for (int i = 0; i <= n - m; ++i) {
      int j = i + m - 1;
      int prod1 = nums[i] * suffixMax[j];
      if (prod1 > ans) ans = prod1;
      int prod2 = nums[i] * suffixMin[j];
      if (prod2 > ans) ans = prod2;
    }
    return ans;
  }
}
```

## Golang

```go
func maximumProduct(nums []int, m int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	suffixMax := make([]int, n)
	suffixMin := make([]int, n)

	for i := n - 1; i >= 0; i-- {
		if i == n-1 {
			suffixMax[i] = nums[i]
			suffixMin[i] = nums[i]
		} else {
			if nums[i] > suffixMax[i+1] {
				suffixMax[i] = nums[i]
			} else {
				suffixMax[i] = suffixMax[i+1]
			}
			if nums[i] < suffixMin[i+1] {
				suffixMin[i] = nums[i]
			} else {
				suffixMin[i] = suffixMin[i+1]
			}
		}
	}

	ans := int64(-1 << 63)
	for i := 0; i <= n-m; i++ {
		idx := i + m - 1
		maxVal := suffixMax[idx]
		minVal := suffixMin[idx]

		prod1 := int64(nums[i]) * int64(maxVal)
		if prod1 > ans {
			ans = prod1
		}
		prod2 := int64(nums[i]) * int64(minVal)
		if prod2 > ans {
			ans = prod2
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_product(nums, m)
  n = nums.length
  if m == 1
    max_sq = nil
    nums.each do |v|
      prod = v * v
      max_sq = prod if max_sq.nil? || prod > max_sq
    end
    return max_sq
  end

  offset = m - 1
  suff_max = Array.new(n)
  suff_min = Array.new(n)

  cur_max = nil
  cur_min = nil
  (n - 1).downto(0) do |i|
    v = nums[i]
    cur_max = v if cur_max.nil? || v > cur_max
    cur_min = v if cur_min.nil? || v < cur_min
    suff_max[i] = cur_max
    suff_min[i] = cur_min
  end

  ans = nil
  (0..n - m).each do |i|
    j_start = i + offset
    max_j = suff_max[j_start]
    min_j = suff_min[j_start]

    prod1 = nums[i] * max_j
    prod2 = nums[i] * min_j

    ans = prod1 if ans.nil? || prod1 > ans
    ans = prod2 if prod2 > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumProduct(nums: Array[Int], m: Int): Long = {
        val n = nums.length
        if (m == 1) {
            var best = Long.MinValue
            var i = 0
            while (i < n) {
                val v = nums(i).toLong
                val prod = v * v
                if (prod > best) best = prod
                i += 1
            }
            return best
        }

        val suffMax = new Array[Int](n)
        val suffMin = new Array[Int](n)

        suffMax(n - 1) = nums(n - 1)
        suffMin(n - 1) = nums(n - 1)

        var i = n - 2
        while (i >= 0) {
            val v = nums(i)
            suffMax(i) = if (v > suffMax(i + 1)) v else suffMax(i + 1)
            suffMin(i) = if (v < suffMin(i + 1)) v else suffMin(i + 1)
            i -= 1
        }

        var best = Long.MinValue
        var idx = 0
        while (idx <= n - m) {
            val start = idx + m - 1
            val a = nums(idx).toLong
            val prod1 = a * suffMax(start)
            if (prod1 > best) best = prod1
            val prod2 = a * suffMin(start)
            if (prod2 > best) best = prod2
            idx += 1
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_product(nums: Vec<i32>, m: i32) -> i64 {
        let n = nums.len();
        let m_usize = m as usize;
        if m_usize == 1 {
            let mut ans = i64::MIN;
            for &x in &nums {
                let prod = (x as i64) * (x as i64);
                if prod > ans {
                    ans = prod;
                }
            }
            return ans;
        }

        // suffix max and min
        let mut suff_max = vec![0i32; n];
        let mut suff_min = vec![0i32; n];
        suff_max[n - 1] = nums[n - 1];
        suff_min[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suff_max[i] = std::cmp::max(nums[i], suff_max[i + 1]);
            suff_min[i] = std::cmp::min(nums[i], suff_min[i + 1]);
        }

        let mut ans = i64::MIN;
        for i in 0..=n - m_usize {
            let idx = i + m_usize - 1; // earliest possible last index
            let first = nums[i] as i64;
            let cand1 = first * suff_max[idx] as i64;
            if cand1 > ans {
                ans = cand1;
            }
            let cand2 = first * suff_min[idx] as i64;
            if cand2 > ans {
                ans = cand2;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-product nums m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (= n 0)
        0
        (let* ([d (- m 1)]
               [pref-max (make-vector n)]
               [pref-min (make-vector n)])
          ;; prefix max/min
          (vector-set! pref-max 0 (vector-ref v 0))
          (vector-set! pref-min 0 (vector-ref v 0))
          (let loop ((i 1) (curmax (vector-ref v 0)) (curmin (vector-ref v 0)))
            (when (< i n)
              (define val (vector-ref v i))
              (set! curmax (if (> val curmax) val curmax))
              (set! curmin (if (< val curmin) val curmin))
              (vector-set! pref-max i curmax)
              (vector-set! pref-min i curmin)
              (loop (+ i 1) curmax curmin)))
          ;; compute answer
          (let loop2 ((j d) (best #f))
            (if (>= j n)
                best
                (let* ([val (vector-ref v j)]
                       [idx (- j d)]
                       [cand1 (* val (vector-ref pref-max idx))]
                       [cand2 (* val (vector-ref pref-min idx))]
                       [local-best (max cand1 cand2)])
                  (loop2 (+ j 1)
                         (if best
                             (if (> local-best best) local-best best)
                             local-best)))))))))
```

## Erlang

```erlang
-spec maximum_product(Nums :: [integer()], M :: integer()) -> integer().
maximum_product(Nums, M) ->
    N = length(Nums),
    case M of
        1 ->
            %% max square of any element
            lists:max([X * X || X <- Nums]);
        _ ->
            Tuple = list_to_tuple(Nums),
            {SufMaxList, SufMinList} = build_suffix(N - 1, Tuple, [], []),
            SufMaxTuple = list_to_tuple(SufMaxList),
            SufMinTuple = list_to_tuple(SufMinList),
            MaxProd = loop(0, N - M, Tuple, SufMaxTuple, SufMinTuple, M, undefined),
            MaxProd
    end.

%% Build suffix max and min lists (from start to end)
build_suffix(-1, _Tuple, AccMax, AccMin) ->
    {lists:reverse(AccMax), lists:reverse(AccMin)};
build_suffix(Index, Tuple, AccMax, AccMin) ->
    Val = element(Tuple, Index),
    case Index of
        N when N == length(tuple_to_list(Tuple)) - 1 -> % first call (last element)
            NewMax = Val,
            NewMin = Val,
            build_suffix(Index - 1, Tuple, [NewMax | AccMax], [NewMin | AccMin]);
        _ ->
            PrevMax = hd(AccMax),
            PrevMin = hd(AccMin),
            NewMax = max(Val, PrevMax),
            NewMin = min(Val, PrevMin),
            build_suffix(Index - 1, Tuple, [NewMax | AccMax], [NewMin | AccMin])
    end.

%% Loop over possible start positions
loop(I, End, NumTuple, SufMaxTuple, SufMinTuple, M, CurrentMax) when I =< End ->
    A = element(NumTuple, I),
    J = I + M - 1,
    Bmax = element(SufMaxTuple, J),
    Bmin = element(SufMinTuple, J),
    Prod = if
        A >= 0 -> A * Bmax;
        true   -> A * Bmin
    end,
    NewMax = case CurrentMax of
        undefined -> Prod;
        _ when Prod > CurrentMax -> Prod;
        _ -> CurrentMax
    end,
    loop(I + 1, End, NumTuple, SufMaxTuple, SufMinTuple, M, NewMax);
loop(_, _, _, _, _, _, Max) ->
    Max.

%% Helper to get element from tuple with 0‑based index
element(Tuple, Index) ->
    erlang:element(Index + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_product(nums :: [integer], m :: integer) :: integer
  def maximum_product(nums, m) do
    n = length(nums)

    if m == 1 do
      Enum.max_by(nums, fn x -> x * x end)
    else
      nums_t = List.to_tuple(nums)

      rev = Enum.reverse(nums)

      {max_rev, min_rev, _} =
        Enum.reduce(rev, {[], [], nil}, fn val, {max_acc, min_acc, prev} ->
          if prev == nil do
            max_val = val
            min_val = val
          else
            {prev_max, prev_min} = prev
            max_val = if val > prev_max, do: val, else: prev_max
            min_val = if val < prev_min, do: val, else: prev_min
          end

          {[max_val | max_acc], [min_val | min_acc], {max_val, min_val}}
        end)

      suffix_max = List.to_tuple(Enum.reverse(max_rev))
      suffix_min = List.to_tuple(Enum.reverse(min_rev))

      Enum.reduce(0..(n - m), nil, fn i, acc ->
        a = elem(nums_t, i)
        j = i + m - 1
        cand1 = a * elem(suffix_max, j)
        cand2 = a * elem(suffix_min, j)

        best = if cand1 > cand2, do: cand1, else: cand2

        cond do
          acc == nil -> best
          best > acc -> best
          true -> acc
        end
      end)
    end
  end
end
```
