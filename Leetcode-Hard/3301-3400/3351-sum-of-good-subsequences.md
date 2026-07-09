# 3351. Sum of Good Subsequences

## Cpp

```cpp
class Solution {
public:
    int sumOfGoodSubsequences(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int maxV = 0;
        for (int v : nums) if (v > maxV) maxV = v;
        // allocate a bit larger to safely access x+1
        vector<long long> dpCount(maxV + 3, 0);
        vector<long long> dpSum(maxV + 3, 0);
        long long ans = 0;
        for (int x : nums) {
            long long cntMinus = dpCount[x - 1];
            long long sumMinus = dpSum[x - 1];
            long long cntPlus = dpCount[x + 1];
            long long sumPlus = dpSum[x + 1];

            long long newCnt = (1LL + cntMinus + cntPlus) % MOD;
            long long add = x % MOD;
            long long newSum = (add + sumMinus + cntMinus * (x % MOD)) % MOD;
            newSum = (newSum + sumPlus + cntPlus * (x % MOD)) % MOD;

            ans += newSum;
            if (ans >= MOD) ans -= MOD;

            dpCount[x] += newCnt;
            if (dpCount[x] >= MOD) dpCount[x] -= MOD;
            dpSum[x] += newSum;
            if (dpSum[x] >= MOD) dpSum[x] -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int sumOfGoodSubsequences(int[] nums) {
        final int MOD = 1_000_000_007;
        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;
        int size = maxVal + 3; // accommodate v+1 access
        long[] cnt = new long[size];
        long[] sum = new long[size];
        long ans = 0;
        for (int v : nums) {
            long cntPrev = 0;
            long sumPrev = 0;
            if (v - 1 >= 0) {
                cntPrev += cnt[v - 1];
                sumPrev += sum[v - 1];
            }
            if (v + 1 < size) {
                cntPrev += cnt[v + 1];
                sumPrev += sum[v + 1];
            }
            cntPrev %= MOD;
            sumPrev %= MOD;

            long newCount = (1 + cntPrev) % MOD;
            long newSum = ((long) v % MOD) * newCount % MOD;
            newSum = (newSum + sumPrev) % MOD;

            cnt[v] = (cnt[v] + newCount) % MOD;
            sum[v] = (sum[v] + newSum) % MOD;
            ans = (ans + newSum) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not nums:
            return 0
        max_val = max(nums)
        size = max_val + 3  # accommodate a+1 access
        cnt = [0] * size
        ssum = [0] * size

        ans = 0
        for a in nums:
            left = a - 1
            right = a + 1

            cnt_left = cnt[left] if left >= 0 else 0
            cnt_right = cnt[right] if right < size else 0
            sum_left = ssum[left] if left >= 0 else 0
            sum_right = ssum[right] if right < size else 0

            new_cnt = (1 + cnt_left + cnt_right) % MOD

            contrib = a % MOD
            contrib = (contrib + sum_left + a * cnt_left) % MOD
            contrib = (contrib + sum_right + a * cnt_right) % MOD
            new_sum = contrib

            ans = (ans + new_sum) % MOD

            cnt[a] = (cnt[a] + new_cnt) % MOD
            ssum[a] = (ssum[a] + new_sum) % MOD

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        if not nums:
            return 0
        max_val = max(nums)
        cnt = [0] * (max_val + 3)      # extra space for num+1 access
        ssum = [0] * (max_val + 3)

        ans = 0
        for x in nums:
            c = (cnt[x - 1] + cnt[x + 1]) % MOD
            s = (ssum[x - 1] + ssum[x + 1]) % MOD

            new_cnt = (1 + c) % MOD
            new_sum = (x + s + x * c) % MOD

            ans = (ans + new_sum) % MOD

            cnt[x] = (cnt[x] + new_cnt) % MOD
            ssum[x] = (ssum[x] + new_sum) % MOD

        return ans
```

## C

```c
#include <stdlib.h>

int sumOfGoodSubsequences(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int maxV = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxV) maxV = nums[i];
    }
    int sz = maxV + 3;                     // ensure indices x-1, x, x+1 are valid
    long long *cnt = (long long*)calloc(sz, sizeof(long long));
    long long *sum = (long long*)calloc(sz, sizeof(long long));

    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        long long cntPrev = 0;
        long long sumPrev = 0;

        if (x - 1 >= 0) {
            cntPrev += cnt[x - 1];
            sumPrev += sum[x - 1];
        }
        if (x + 1 < sz) {
            cntPrev += cnt[x + 1];
            sumPrev += sum[x + 1];
        }

        cntPrev %= MOD;
        sumPrev %= MOD;

        long long newCnt = (cntPrev + 1) % MOD;
        long long newSum = (sumPrev + ((long long)x % MOD) * cntPrev) % MOD;
        newSum = (newSum + x) % MOD;

        cnt[x] = (cnt[x] + newCnt) % MOD;
        sum[x] = (sum[x] + newSum) % MOD;
    }

    long long ans = 0;
    for (int i = 0; i < sz; ++i) {
        ans += sum[i];
        if (ans >= MOD) ans %= MOD;
    }
    ans %= MOD;

    free(cnt);
    free(sum);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfGoodSubsequences(int[] nums) {
        const long MOD = 1000000007L;
        int max = 0;
        foreach (int v in nums) if (v > max) max = v;
        int size = max + 3; // accommodate val+1 access
        long[] cnt = new long[size];
        long[] sum = new long[size];

        foreach (int v in nums) {
            long leftCnt = v - 1 >= 0 ? cnt[v - 1] : 0;
            long rightCnt = v + 1 < size ? cnt[v + 1] : 0;
            long leftSum = v - 1 >= 0 ? sum[v - 1] : 0;
            long rightSum = v + 1 < size ? sum[v + 1] : 0;

            long newCnt = (1L + leftCnt + rightCnt) % MOD;
            long addFromLeft = (leftSum + leftCnt * v) % MOD;
            long addFromRight = (rightSum + rightCnt * v) % MOD;
            long newSum = (v % MOD + addFromLeft + addFromRight) % MOD;

            cnt[v] = (cnt[v] + newCnt) % MOD;
            sum[v] = (sum[v] + newSum) % MOD;
        }

        long ans = 0;
        foreach (long s in sum) {
            ans += s;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfGoodSubsequences = function(nums) {
    const MOD = 1000000007;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;
    const size = maxVal + 3; // extra space for x+1 access
    const cnt = new Array(size).fill(0);
    const sum = new Array(size).fill(0);

    for (const x of nums) {
        const leftCnt = x > 0 ? cnt[x - 1] : 0;
        const rightCnt = cnt[x + 1];
        const leftSum = x > 0 ? sum[x - 1] : 0;
        const rightSum = sum[x + 1];

        let newCount = (1 + leftCnt + rightCnt) % MOD;

        // contribution from extending existing good subsequences
        let extendSum = (
            leftSum +
            (leftCnt * x) % MOD +
            rightSum +
            (rightCnt * x) % MOD
        ) % MOD;

        let newSum = (x % MOD + extendSum) % MOD;

        cnt[x] = (cnt[x] + newCount) % MOD;
        sum[x] = (sum[x] + newSum) % MOD;
    }

    let total = 0;
    for (let i = 0; i < size; ++i) {
        total += sum[i];
        if (total >= MOD) total -= MOD;
    }
    return total % MOD;
};
```

## Typescript

```typescript
function sumOfGoodSubsequences(nums: number[]): number {
    const MOD = 1000000007;
    if (nums.length === 0) return 0;
    const maxVal = Math.max(...nums);
    const size = maxVal + 3; // extra space for val+1 access
    const cnt = new Array<number>(size).fill(0);
    const sum = new Array<number>(size).fill(0);
    let ans = 0;

    for (const v of nums) {
        const cntMinus = v > 0 ? cnt[v - 1] : 0;
        const cntPlus = v + 1 < size ? cnt[v + 1] : 0;
        const sumMinus = v > 0 ? sum[v - 1] : 0;
        const sumPlus = v + 1 < size ? sum[v + 1] : 0;

        const newCnt = (1 + cntMinus + cntPlus) % MOD;

        const contribMinus = (sumMinus + (v * cntMinus) % MOD) % MOD;
        const contribPlus = (sumPlus + (v * cntPlus) % MOD) % MOD;
        const newSum = (v + contribMinus + contribPlus) % MOD;

        ans = (ans + newSum) % MOD;

        cnt[v] = (cnt[v] + newCnt) % MOD;
        sum[v] = (sum[v] + newSum) % MOD;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfGoodSubsequences($nums) {
        $MOD = 1000000007;
        $dpCount = [];
        $dpSum = [];

        foreach ($nums as $val) {
            $cntPrev = 0;
            $sumPrev = 0;

            $left = $val - 1;
            if (isset($dpCount[$left])) {
                $cntPrev = ($cntPrev + $dpCount[$left]) % $MOD;
                $sumPrev = ($sumPrev + $dpSum[$left]) % $MOD;
            }

            $right = $val + 1;
            if (isset($dpCount[$right])) {
                $cntPrev = ($cntPrev + $dpCount[$right]) % $MOD;
                $sumPrev = ($sumPrev + $dpSum[$right]) % $MOD;
            }

            $newCount = (1 + $cntPrev) % $MOD;

            $valMod = $val % $MOD;
            $newSum = ($valMod + $sumPrev) % $MOD;
            $newSum = ($newSum + ($valMod * $cntPrev) % $MOD) % $MOD;

            if (!isset($dpCount[$val])) {
                $dpCount[$val] = 0;
                $dpSum[$val] = 0;
            }

            $dpCount[$val] = ($dpCount[$val] + $newCount) % $MOD;
            $dpSum[$val]   = ($dpSum[$val] + $newSum) % $MOD;
        }

        $ans = 0;
        foreach ($dpSum as $s) {
            $ans = ($ans + $s) % $MOD;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfGoodSubsequences(_ nums: [Int]) -> Int {
        let MOD: Int64 = 1_000_000_007
        if nums.isEmpty { return 0 }
        var maxVal = 0
        for v in nums { if v > maxVal { maxVal = v } }
        // allocate enough space to access value+1 safely
        var cnt = [Int64](repeating: 0, count: maxVal + 3)
        var sumEnd = [Int64](repeating: 0, count: maxVal + 3)

        for num in nums {
            let x = Int64(num)
            // contributions from left neighbor (num-1)
            var leftCnt: Int64 = 0
            var leftSum: Int64 = 0
            if num > 0 {
                leftCnt = cnt[num - 1]
                leftSum = (sumEnd[num - 1] + cnt[num - 1] * x) % MOD
            }
            // contributions from right neighbor (num+1)
            var rightCnt: Int64 = 0
            var rightSum: Int64 = 0
            if num + 1 < cnt.count {
                rightCnt = cnt[num + 1]
                rightSum = (sumEnd[num + 1] + cnt[num + 1] * x) % MOD
            }

            let deltaCnt = (1 + leftCnt + rightCnt) % MOD
            let deltaSum = (x + leftSum + rightSum) % MOD

            cnt[num] = (cnt[num] + deltaCnt) % MOD
            sumEnd[num] = (sumEnd[num] + deltaSum) % MOD
        }

        var answer: Int64 = 0
        for val in 0..<cnt.count {
            answer += sumEnd[val]
            if answer >= MOD * 4 { // occasional reduction to avoid overflow
                answer %= MOD
            }
        }
        answer %= MOD
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfGoodSubsequences(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v
        val size = maxVal + 3
        val cnt = LongArray(size)
        val sum = LongArray(size)
        var ans = 0L
        for (x in nums) {
            val xm1 = x - 1
            val xp1 = x + 1
            var cntMinus = 0L
            var cntPlus = 0L
            var sumMinus = 0L
            var sumPlus = 0L
            if (xm1 >= 0) {
                cntMinus = cnt[xm1]
                sumMinus = sum[xm1]
            }
            if (xp1 < size) {
                cntPlus = cnt[xp1]
                sumPlus = sum[xp1]
            }
            val newCount = (1L + cntMinus + cntPlus) % MOD
            var newSum = x.toLong()
            newSum = (newSum + sumMinus + (cntMinus * x) % MOD) % MOD
            newSum = (newSum + sumPlus + (cntPlus * x) % MOD) % MOD
            cnt[x] = (cnt[x] + newCount) % MOD
            sum[x] = (sum[x] + newSum) % MOD
            ans += newSum
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int sumOfGoodSubsequences(List<int> nums) {
    if (nums.isEmpty) return 0;
    int maxVal = nums.reduce((a, b) => a > b ? a : b);
    int size = maxVal + 3; // accommodate x+1 access
    List<int> cnt = List.filled(size, 0);
    List<int> sumArr = List.filled(size, 0);

    int ans = 0;

    for (int x in nums) {
      int left = x - 1;
      int right = x + 1;

      // count of subsequences we can extend
      int cntPrev = 0;
      if (left >= 0) cntPrev = (cntPrev + cnt[left]) % _mod;
      if (right < size) cntPrev = (cntPrev + cnt[right]) % _mod;

      int newCnt = (1 + cntPrev) % _mod; // include singleton

      // sum contributions from extensions
      int sumPrev = 0;
      if (left >= 0) {
        int part = (sumArr[left] + (cnt[left] * x) % _mod) % _mod;
        sumPrev = (sumPrev + part) % _mod;
      }
      if (right < size) {
        int part = (sumArr[right] + (cnt[right] * x) % _mod) % _mod;
        sumPrev = (sumPrev + part) % _mod;
      }

      int newSum = ((x % _mod) + sumPrev) % _mod;

      ans += newSum;
      if (ans >= _mod) ans -= _mod;

      cnt[x] += newCnt;
      if (cnt[x] >= _mod) cnt[x] -= _mod;

      sumArr[x] += newSum;
      if (sumArr[x] >= _mod) sumArr[x] -= _mod;
    }

    return ans;
  }
}
```

## Golang

```go
func sumOfGoodSubsequences(nums []int) int {
	const MOD int64 = 1000000007
	if len(nums) == 0 {
		return 0
	}
	maxV := 0
	for _, v := range nums {
		if v > maxV {
			maxV = v
		}
	}
	shift := 1
	size := maxV + shift + 2 // extra space for neighbor access
	cnt := make([]int64, size)
	sumArr := make([]int64, size)

	var ans int64 = 0
	for _, v := range nums {
		idx := v + shift
		leftIdx := idx - 1
		rightIdx := idx + 1

		leftCnt := cnt[leftIdx]
		leftSum := sumArr[leftIdx]
		rightCnt := cnt[rightIdx]
		rightSum := sumArr[rightIdx]

		addCnt := (leftCnt + rightCnt + 1) % MOD

		x := int64(v)
		addSum := x % MOD
		addSum = (addSum + leftSum) % MOD
		addSum = (addSum + (leftCnt%MOD)*x) % MOD
		addSum = (addSum + rightSum) % MOD
		addSum = (addSum + (rightCnt%MOD)*x) % MOD

		cnt[idx] = (cnt[idx] + addCnt) % MOD
		sumArr[idx] = (sumArr[idx] + addSum) % MOD
		ans = (ans + addSum) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def sum_of_good_subsequences(nums)
  mod = 1_000_000_007
  max_val = nums.max || 0
  size = max_val + 3
  cnt = Array.new(size, 0)
  sm = Array.new(size, 0)

  nums.each do |x|
    c1 = x > 0 ? cnt[x - 1] : 0
    s1 = x > 0 ? sm[x - 1] : 0
    c2 = cnt[x + 1]
    s2 = sm[x + 1]

    new_cnt = (1 + c1 + c2) % mod
    part1 = (s1 + c1 * x) % mod
    part2 = (s2 + c2 * x) % mod
    new_sum = (x % mod + part1 + part2) % mod

    cnt[x] = (cnt[x] + new_cnt) % mod
    sm[x] = (sm[x] + new_sum) % mod
  end

  total = sm.reduce(0) { |acc, v| (acc + v) % mod }
  total
end
```

## Scala

```scala
object Solution {
    def sumOfGoodSubsequences(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        var maxVal = 0
        for (v <- nums) if (v > maxVal) maxVal = v
        val size = maxVal + 2 // to safely access x+1
        val cnt = new Array[Long](size)
        val sumArr = new Array[Long](size)
        var ans = 0L

        for (xInt <- nums) {
            val x = xInt.toLong
            val leftIdx = xInt - 1
            val rightIdx = xInt + 1

            val leftCount = if (leftIdx >= 0) cnt(leftIdx) else 0L
            val rightCount = if (rightIdx < size) cnt(rightIdx) else 0L
            val leftSum = if (leftIdx >= 0) sumArr(leftIdx) else 0L
            val rightSum = if (rightIdx < size) sumArr(rightIdx) else 0L

            val addCount = (1L + leftCount + rightCount) % MOD
            val addSum = (
                x +
                ((leftSum + (leftCount * x) % MOD) % MOD) +
                ((rightSum + (rightCount * x) % MOD) % MOD)
            ) % MOD

            cnt(xInt) = (cnt(xInt) + addCount) % MOD
            sumArr(xInt) = (sumArr(xInt) + addSum) % MOD
            ans = (ans + addSum) % MOD
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_good_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut max_val = 0usize;
        for &x in &nums {
            if x as usize > max_val {
                max_val = x as usize;
            }
        }
        // allocate a bit extra to safely access v+1
        let size = max_val + 3;
        let mut cnt: Vec<i64> = vec![0; size];
        let mut sum_end: Vec<i64> = vec![0; size];
        let mut ans: i64 = 0;

        for &num in nums.iter() {
            let v = num as usize;
            let left_cnt = if v > 0 { cnt[v - 1] } else { 0 };
            let left_sum = if v > 0 { sum_end[v - 1] } else { 0 };
            let right_idx = v + 1;
            let right_cnt = if right_idx < size { cnt[right_idx] } else { 0 };
            let right_sum = if right_idx < size { sum_end[right_idx] } else { 0 };

            let new_cnt = (1 + left_cnt + right_cnt) % MOD;

            let v_i64 = num as i64;
            let mut new_sum = v_i64;
            new_sum = (new_sum
                + (left_sum + left_cnt * v_i64 % MOD) % MOD) % MOD;
            new_sum = (new_sum
                + (right_sum + right_cnt * v_i64 % MOD) % MOD) % MOD;

            ans += new_sum;
            if ans >= MOD {
                ans -= MOD;
            }

            cnt[v] += new_cnt;
            if cnt[v] >= MOD {
                cnt[v] -= MOD;
            }
            sum_end[v] += new_sum;
            if sum_end[v] >= MOD {
                sum_end[v] -= MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (sum-of-good-subsequences nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((MOD 1000000007)
         (MAXV 100000)                     ; given constraint
         (SIZE (+ MAXV 3))                 ; extra space for v+1 access
         (cnt (make-vector SIZE 0))
         (sums (make-vector SIZE 0))
         (ans 0))
    (for ([x nums])
      (define left (- x 1))
      (define right (+ x 1))
      (define cnt-left (if (and (>= left 0) (< left SIZE)) (vector-ref cnt left) 0))
      (define cnt-right (if (and (>= right 0) (< right SIZE)) (vector-ref cnt right) 0))
      (define sum-left (if (and (>= left 0) (< left SIZE)) (vector-ref sums left) 0))
      (define sum-right (if (and (>= right 0) (< right SIZE)) (vector-ref sums right) 0))

      (define add-cnt (+ 1 cnt-left cnt-right))

      (define add-sum
        (modulo
         (+ x
            (modulo (+ sum-left (* cnt-left x)) MOD)
            (modulo (+ sum-right (* cnt-right x)) MOD))
         MOD))

      (set! ans (modulo (+ ans add-sum) MOD))

      (let* ((old-cnt (vector-ref cnt x))
             (old-sum (vector-ref sums x)))
        (vector-set! cnt x (modulo (+ old-cnt add-cnt) MOD))
        (vector-set! sums x (modulo (+ old-sum add-sum) MOD))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_good_subsequences/1]).

-define(MOD, 1000000007).

sum_of_good_subsequences(Nums) ->
    {_, SumMap} = lists:foldl(fun process/2, {#{}, #{}}, Nums),
    maps:fold(fun(_Key, Val, Acc) -> (Acc + Val) rem ?MOD end, 0, SumMap).

process(Num, {CntMap, SumMap}) ->
    PrevCnt = (maps:get(Num - 1, CntMap, 0) + maps:get(Num + 1, CntMap, 0)) rem ?MOD,
    PrevSum = (maps:get(Num - 1, SumMap, 0) + maps:get(Num + 1, SumMap, 0)) rem ?MOD,
    AddCnt = (PrevCnt + 1) rem ?MOD,
    AddSum = (PrevSum + (PrevCnt * Num) rem ?MOD + Num) rem ?MOD,
    NewCntMap = maps:update_with(Num, fun(V) -> (V + AddCnt) rem ?MOD end, AddCnt, CntMap),
    NewSumMap = maps:update_with(Num, fun(V) -> (V + AddSum) rem ?MOD end, AddSum, SumMap),
    {NewCntMap, NewSumMap}.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_good_subsequences(nums :: [integer]) :: integer
  def sum_of_good_subsequences(nums) do
    mod = 1_000_000_007

    {_, _, ans} =
      Enum.reduce(nums, {%{}, %{}, 0}, fn a, {cnt, sum, acc} ->
        cnt_minus = Map.get(cnt, a - 1, 0)
        sum_minus = Map.get(sum, a - 1, 0)

        cnt_plus = Map.get(cnt, a + 1, 0)
        sum_plus = Map.get(sum, a + 1, 0)

        new_cnt = rem(1 + cnt_minus + cnt_plus, mod)

        contrib_minus = rem(sum_minus + cnt_minus * a, mod)
        contrib_plus = rem(sum_plus + cnt_plus * a, mod)

        new_sum = rem(a + contrib_minus + contrib_plus, mod)

        acc = rem(acc + new_sum, mod)

        cnt_a = Map.get(cnt, a, 0)
        sum_a = Map.get(sum, a, 0)

        cnt = Map.put(cnt, a, rem(cnt_a + new_cnt, mod))
        sum = Map.put(sum, a, rem(sum_a + new_sum, mod))

        {cnt, sum, acc}
      end)

    ans
  end
end
```
