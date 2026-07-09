# 2909. Minimum Sum of Mountain Triplets II

## Cpp

```cpp
class Solution {
public:
    int minimumSum(vector<int>& nums) {
        int n = nums.size();
        const long long INF = 4e18;
        vector<long long> pref(n), suff(n);
        pref[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            pref[i] = min(pref[i - 1], (long long)nums[i]);
        }
        suff[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suff[i] = min(suff[i + 1], (long long)nums[i]);
        }
        long long ans = INF;
        for (int j = 1; j <= n - 2; ++j) {
            long long left = pref[j - 1];
            long long right = suff[j + 1];
            if (left < nums[j] && right < nums[j]) {
                ans = min(ans, left + nums[j] + right);
            }
        }
        return ans == INF ? -1 : (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumSum(int[] nums) {
        int n = nums.length;
        if (n < 3) return -1;
        int[] prefMin = new int[n];
        prefMin[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefMin[i] = Math.min(prefMin[i - 1], nums[i]);
        }
        int[] suffMin = new int[n];
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
        }
        long best = Long.MAX_VALUE;
        for (int j = 1; j <= n - 2; j++) {
            int left = prefMin[j - 1];
            if (left >= nums[j]) continue;
            int right = suffMin[j + 1];
            if (right >= nums[j]) continue;
            long sum = (long) left + nums[j] + right;
            if (sum < best) best = sum;
        }
        return best == Long.MAX_VALUE ? -1 : (int) best;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return -1

        # prefix minima up to each index
        prefix_min = [0] * n
        cur = nums[0]
        for i in range(n):
            cur = min(cur, nums[i])
            prefix_min[i] = cur

        # suffix minima from each index to end
        suffix_min = [0] * n
        cur = nums[-1]
        for i in range(n - 1, -1, -1):
            cur = min(cur, nums[i])
            suffix_min[i] = cur

        INF = float('inf')
        ans = INF
        # j is the peak index, cannot be first or last
        for j in range(1, n - 1):
            left = prefix_min[j - 1]
            right = suffix_min[j + 1]
            if left < nums[j] and right < nums[j]:
                ans = min(ans, left + nums[j] + right)

        return -1 if ans == INF else ans
```

## Python3

```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        prefix_min = [0] * n
        cur = nums[0]
        for i in range(n):
            cur = min(cur, nums[i])
            prefix_min[i] = cur

        suffix_min = [0] * n
        cur = nums[-1]
        for i in range(n - 1, -1, -1):
            cur = min(cur, nums[i])
            suffix_min[i] = cur

        ans = float('inf')
        for j in range(1, n - 1):
            left = prefix_min[j - 1]
            right = suffix_min[j + 1]
            if left < nums[j] and right < nums[j]:
                total = left + nums[j] + right
                if total < ans:
                    ans = total

        return -1 if ans == float('inf') else ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimumSum(int* nums, int numsSize) {
    if (numsSize < 3) return -1;
    
    int *pref = (int *)malloc(numsSize * sizeof(int));
    int *suff = (int *)malloc(numsSize * sizeof(int));
    if (!pref || !suff) {
        free(pref);
        free(suff);
        return -1;
    }
    
    pref[0] = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        pref[i] = nums[i] < pref[i-1] ? nums[i] : pref[i-1];
    }
    
    suff[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        suff[i] = nums[i] < suff[i+1] ? nums[i] : suff[i+1];
    }
    
    int ans = INT_MAX;
    for (int j = 1; j <= numsSize - 2; ++j) {
        int left = pref[j-1];
        int right = suff[j+1];
        if (left < nums[j] && right < nums[j]) {
            int sum = left + nums[j] + right;
            if (sum < ans) ans = sum;
        }
    }
    
    free(pref);
    free(suff);
    
    return ans == INT_MAX ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSum(int[] nums) {
        int n = nums.Length;
        if (n < 3) return -1;
        int[] prefixMin = new int[n];
        int[] suffixMin = new int[n];
        prefixMin[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefixMin[i] = Math.Min(prefixMin[i - 1], nums[i]);
        }
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.Min(suffixMin[i + 1], nums[i]);
        }
        int ans = int.MaxValue;
        for (int j = 1; j <= n - 2; j++) {
            int left = prefixMin[j - 1];
            if (left >= nums[j]) continue;
            int right = suffixMin[j + 1];
            if (right >= nums[j]) continue;
            int sum = left + nums[j] + right;
            if (sum < ans) ans = sum;
        }
        return ans == int.MaxValue ? -1 : ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSum = function(nums) {
    const n = nums.length;
    if (n < 3) return -1;

    const pref = new Array(n);
    pref[0] = nums[0];
    for (let i = 1; i < n; ++i) {
        pref[i] = Math.min(pref[i - 1], nums[i]);
    }

    const suff = new Array(n);
    suff[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suff[i] = Math.min(suff[i + 1], nums[i]);
    }

    let ans = Infinity;
    for (let j = 1; j <= n - 2; ++j) {
        const left = pref[j - 1];
        const right = suff[j + 1];
        if (left < nums[j] && right < nums[j]) {
            const sum = left + nums[j] + right;
            if (sum < ans) ans = sum;
        }
    }

    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minimumSum(nums: number[]): number {
    const n = nums.length;
    // Coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const idxMap = new Map<number, number>();
    for (let i = 0; i < uniq.length; i++) idxMap.set(uniq[i], i + 1); // 1‑based

    class BIT {
        size: number;
        tree: number[];
        constructor(size: number) {
            this.size = size;
            this.tree = new Array(size + 2).fill(Infinity);
        }
        update(pos: number, val: number): void {
            for (let i = pos; i <= this.size; i += i & -i) {
                if (val < this.tree[i]) this.tree[i] = val;
            }
        }
        query(pos: number): number {
            let res = Infinity;
            for (let i = pos; i > 0; i -= i & -i) {
                if (this.tree[i] < res) res = this.tree[i];
            }
            return res;
        }
    }

    const m = uniq.length;
    const leftBest = new Array<number>(n).fill(Infinity);
    const bitL = new BIT(m);
    for (let j = 0; j < n; ++j) {
        const id = idxMap.get(nums[j])!;
        leftBest[j] = bitL.query(id - 1); // smallest value strictly less
        bitL.update(id, nums[j]);
    }

    const rightBest = new Array<number>(n).fill(Infinity);
    const bitR = new BIT(m);
    for (let j = n - 1; j >= 0; --j) {
        const id = idxMap.get(nums[j])!;
        rightBest[j] = bitR.query(id - 1);
        bitR.update(id, nums[j]);
    }

    let ans = Infinity;
    for (let j = 0; j < n; ++j) {
        if (leftBest[j] !== Infinity && rightBest[j] !== Infinity) {
            const sum = leftBest[j] + nums[j] + rightBest[j];
            if (sum < ans) ans = sum;
        }
    }
    return ans === Infinity ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumSum($nums) {
        $n = count($nums);
        if ($n < 3) return -1;

        // prefix minima
        $prefMin = array_fill(0, $n, 0);
        $prefMin[0] = $nums[0];
        for ($i = 1; $i < $n; ++$i) {
            $prefMin[$i] = min($prefMin[$i - 1], $nums[$i]);
        }

        // suffix minima
        $suffMin = array_fill(0, $n, 0);
        $suffMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; --$i) {
            $suffMin[$i] = min($suffMin[$i + 1], $nums[$i]);
        }

        $ans = PHP_INT_MAX;
        for ($j = 1; $j <= $n - 2; ++$j) {
            $left = $prefMin[$j - 1];
            $right = $suffMin[$j + 1];
            if ($left < $nums[$j] && $right < $nums[$j]) {
                $sum = $left + $nums[$j] + $right;
                if ($sum < $ans) {
                    $ans = $sum;
                }
            }
        }

        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return -1 }
        
        var prefixMin = Array(repeating: 0, count: n)
        var cur = nums[0]
        for i in 0..<n {
            cur = min(cur, nums[i])
            prefixMin[i] = cur
        }
        
        var suffixMin = Array(repeating: 0, count: n)
        cur = nums[n - 1]
        for i in stride(from: n - 1, through: 0, by: -1) {
            cur = min(cur, nums[i])
            suffixMin[i] = cur
        }
        
        var answer = Int.max
        for j in 1..<(n - 1) {
            let left = prefixMin[j - 1]
            if left >= nums[j] { continue }
            let right = suffixMin[j + 1]
            if right >= nums[j] { continue }
            let sum = left + nums[j] + right
            if sum < answer {
                answer = sum
            }
        }
        
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSum(nums: IntArray): Int {
        val n = nums.size
        if (n < 3) return -1

        val prefixMin = IntArray(n)
        var curMin = nums[0]
        for (i in 0 until n) {
            if (nums[i] < curMin) curMin = nums[i]
            prefixMin[i] = curMin
        }

        val suffixMin = IntArray(n)
        curMin = nums[n - 1]
        for (i in n - 1 downTo 0) {
            if (nums[i] < curMin) curMin = nums[i]
            suffixMin[i] = curMin
        }

        var ans = Long.MAX_VALUE
        for (j in 1 until n - 1) {
            val left = prefixMin[j - 1]
            val right = suffixMin[j + 1]
            if (left < nums[j] && right < nums[j]) {
                val sum = left.toLong() + nums[j].toLong() + right.toLong()
                if (sum < ans) ans = sum
            }
        }

        return if (ans == Long.MAX_VALUE) -1 else ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimumSum(List<int> nums) {
    int n = nums.length;
    if (n < 3) return -1;

    List<int> pref = List.filled(n, 0);
    pref[0] = nums[0];
    for (int i = 1; i < n; ++i) {
      pref[i] = min(pref[i - 1], nums[i]);
    }

    List<int> suff = List.filled(n, 0);
    suff[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
      suff[i] = min(suff[i + 1], nums[i]);
    }

    int best = 1 << 60;
    for (int j = 1; j <= n - 2; ++j) {
      int leftMin = pref[j - 1];
      if (leftMin >= nums[j]) continue;
      int rightMin = suff[j + 1];
      if (rightMin >= nums[j]) continue;
      int sum = leftMin + nums[j] + rightMin;
      if (sum < best) best = sum;
    }

    return best == (1 << 60) ? -1 : best;
  }
}
```

## Golang

```go
func minimumSum(nums []int) int {
	n := len(nums)
	if n < 3 {
		return -1
	}
	prefixMin := make([]int, n)
	cur := nums[0]
	prefixMin[0] = cur
	for i := 1; i < n; i++ {
		if nums[i] < cur {
			cur = nums[i]
		}
		prefixMin[i] = cur
	}
	suffixMin := make([]int, n)
	cur = nums[n-1]
	suffixMin[n-1] = cur
	for i := n - 2; i >= 0; i-- {
		if nums[i] < cur {
			cur = nums[i]
		}
		suffixMin[i] = cur
	}
	const INF int64 = 1 << 60
	ans := INF
	for j := 1; j <= n-2; j++ {
		left := prefixMin[j-1]
		right := suffixMin[j+1]
		if left < nums[j] && right < nums[j] {
			sum := int64(left) + int64(nums[j]) + int64(right)
			if sum < ans {
				ans = sum
			}
		}
	}
	if ans == INF {
		return -1
	}
	return int(ans)
}
```

## Ruby

```ruby
def minimum_sum(nums)
  n = nums.length
  prefix_min = Array.new(n)
  min_val = Float::INFINITY
  nums.each_with_index do |v, i|
    min_val = v if v < min_val
    prefix_min[i] = min_val
  end

  suffix_min = Array.new(n)
  min_val = Float::INFINITY
  (n - 1).downto(0) do |i|
    v = nums[i]
    min_val = v if v < min_val
    suffix_min[i] = min_val
  end

  ans = Float::INFINITY
  (1...n - 1).each do |j|
    left = prefix_min[j - 1]
    right = suffix_min[j + 1]
    if left < nums[j] && right < nums[j]
      sum = left + nums[j] + right
      ans = sum if sum < ans
    end
  end

  ans == Float::INFINITY ? -1 : ans.to_i
end
```

## Scala

```scala
object Solution {
    def minimumSum(nums: Array[Int]): Int = {
        val n = nums.length
        if (n < 3) return -1

        val prefixMin = new Array[Int](n)
        var cur = Int.MaxValue
        var i = 0
        while (i < n) {
            if (nums(i) < cur) cur = nums(i)
            prefixMin(i) = cur
            i += 1
        }

        val suffixMin = new Array[Int](n)
        cur = Int.MaxValue
        i = n - 1
        while (i >= 0) {
            if (nums(i) < cur) cur = nums(i)
            suffixMin(i) = cur
            i -= 1
        }

        var ans = Long.MaxValue
        var j = 1
        while (j <= n - 2) {
            val left = prefixMin(j - 1)
            val right = suffixMin(j + 1)
            val mid = nums(j)
            if (left < mid && right < mid) {
                val sum = left.toLong + mid + right
                if (sum < ans) ans = sum
            }
            j += 1
        }

        if (ans == Long.MaxValue) -1 else ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return -1;
        }
        // prefix minima
        let mut pref = vec![0i32; n];
        pref[0] = nums[0];
        for i in 1..n {
            pref[i] = pref[i - 1].min(nums[i]);
        }
        // suffix minima
        let mut suff = vec![0i32; n];
        suff[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suff[i] = suff[i + 1].min(nums[i]);
        }

        let mut ans: i64 = i64::MAX;
        for j in 1..n - 1 {
            let left_min = pref[j - 1];
            let right_min = suff[j + 1];
            if left_min < nums[j] && right_min < nums[j] {
                let sum = left_min as i64 + nums[j] as i64 + right_min as i64;
                if sum < ans {
                    ans = sum;
                }
            }
        }

        if ans == i64::MAX {
            -1
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define/contract (minimum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (INF 1000000000000000) ; sufficiently large sentinel
         (suffix-min (make-vector n INF)))
    ;; compute suffix minima: minimum value strictly to the right of each index
    (let loop ((i (- n 1)) (cur INF))
      (when (>= i 0)
        (vector-set! suffix-min i cur)
        (let ((val (vector-ref vec i)))
          (loop (- i 1) (if (< val cur) val cur)))))
    ;; iterate possible middle indices
    (let loop2 ((j 1)
                (prefix-min (vector-ref vec 0))
                (ans INF))
      (cond
        [(>= j (- n 1)) (if (= ans INF) -1 ans)]
        [else
         (let* ((mid (vector-ref vec j))
                (right-min (vector-ref suffix-min j)))
           (define new-ans
             (if (and (< prefix-min mid) (< right-min mid))
                 (let ((s (+ prefix-min (+ mid right-min))))
                   (if (< s ans) s ans))
                 ans))
           (loop2 (+ j 1)
                  (let ((val (vector-ref vec j)))
                    (if (< val prefix-min) val prefix-min))
                  new-ans))])))))
```

## Erlang

```erlang
-spec minimum_sum(Nums :: [integer()]) -> integer().
minimum_sum(Nums) ->
    N = length(Nums),
    case N < 3 of
        true -> -1;
        false ->
            Arr = list_to_tuple(Nums),
            SuffixTuple = compute_suffix_min(Arr, N),
            PrefixMin0 = element(1, Arr),
            Best = loop(2, N - 1, Arr, SuffixTuple, PrefixMin0, undefined),
            case Best of
                undefined -> -1;
                _ -> Best
            end
    end.

-spec compute_suffix_min(tuple(), integer()) -> tuple().
compute_suffix_min(Arr, N) ->
    % Build suffix minima from right to left.
    {_, List} = lists:foldl(
        fun(Index, {MinSoFar, Acc}) ->
            Val = element(Index, Arr),
            NewMin = if Val < MinSoFar -> Val; true -> MinSoFar end,
            {NewMin, [NewMin | Acc]}
        end,
        {2000000001, []},
        lists:seq(N, 1, -1)
    ),
    list_to_tuple(List).

-spec loop(integer(), integer(), tuple(), tuple(), integer(), undefined | integer()) -> undefined | integer().
loop(Pos, EndPos, _Arr, _SuffixTuple, _PrefixMin, Best) when Pos > EndPos ->
    Best;
loop(Pos, EndPos, Arr, SuffixTuple, PrefixMin, Best) ->
    Curr = element(Pos, Arr),
    RightMin = element(Pos + 1, SuffixTuple),
    NewBest =
        if (PrefixMin < Curr) andalso (RightMin < Curr) ->
                Sum = PrefixMin + Curr + RightMin,
                case Best of
                    undefined -> Sum;
                    _ when Sum < Best -> Sum;
                    _ -> Best
                end;
           true -> Best
        end,
    NewPrefixMin = if Curr < PrefixMin -> Curr; true -> PrefixMin end,
    loop(Pos + 1, EndPos, Arr, SuffixTuple, NewPrefixMin, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(nums :: [integer]) :: integer
  def minimum_sum(nums) do
    n = length(nums)

    # Prefix minima
    {pref, _} =
      Enum.map_reduce(nums, nil, fn val, prev_min ->
        cur = if prev_min == nil, do: val, else: min(prev_min, val)
        {cur, cur}
      end)

    # Suffix minima
    rev_nums = Enum.reverse(nums)

    {rev_suff, _} =
      Enum.map_reduce(rev_nums, nil, fn val, prev_min ->
        cur = if prev_min == nil, do: val, else: min(prev_min, val)
        {cur, cur}
      end)

    suffix = Enum.reverse(rev_suff)

    nums_t = List.to_tuple(nums)
    pref_t = List.to_tuple(pref)
    suff_t = List.to_tuple(suffix)

    ans =
      1..(n - 2)
      |> Enum.reduce(:infinity, fn j, acc ->
        left = elem(pref_t, j - 1)
        mid = elem(nums_t, j)
        right = elem(suff_t, j + 1)

        if left < mid and right < mid do
          sum = left + mid + right
          min(acc, sum)
        else
          acc
        end
      end)

    case ans do
      :infinity -> -1
      _ -> ans
    end
  end
end
```
