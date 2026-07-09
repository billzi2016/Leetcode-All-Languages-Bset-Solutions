# 0891. Sum of Subsequence Widths

## Cpp

```cpp
class Solution {
public:
    int sumSubseqWidths(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<long long> pow2(n);
        pow2[0] = 1;
        for (int i = 1; i < n; ++i) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = (pow2[i] - pow2[n - 1 - i] + MOD) % MOD;
            ans = (ans + diff * nums[i]) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int sumSubseqWidths(int[] nums) {
        int n = nums.length;
        java.util.Arrays.sort(nums);
        long[] pow2 = new long[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] << 1) % MOD;
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long diff = pow2[i] - pow2[n - 1 - i];
            if (diff < 0) diff += MOD;
            ans = (ans + diff * nums[i]) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumSubseqWidths(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] << 1) % MOD
        ans = 0
        for i, v in enumerate(nums):
            diff = (pow2[i] - pow2[n - 1 - i]) % MOD
            ans = (ans + diff * v) % MOD
        return ans
```

## Python3

```python
class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] << 1) % MOD
        ans = 0
        for i, v in enumerate(nums):
            contrib = (pow2[i] - pow2[n - 1 - i]) % MOD
            ans = (ans + contrib * v) % MOD
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int sumSubseqWidths(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    long long *pow2 = (long long *)malloc(sizeof(long long) * numsSize);
    pow2[0] = 1;
    for (int i = 1; i < numsSize; ++i) {
        pow2[i] = (pow2[i - 1] << 1) % MOD;
    }
    
    long long ans = 0;
    int nMinusOne = numsSize - 1;
    for (int i = 0; i < numsSize; ++i) {
        long long diff = pow2[i] - pow2[nMinusOne - i];
        if (diff < 0) diff += MOD;
        ans = (ans + diff * (long long)nums[i]) % MOD;
    }
    
    free(pow2);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int SumSubseqWidths(int[] nums)
    {
        const int MOD = 1000000007;
        int n = nums.Length;
        System.Array.Sort(nums);
        long[] pow = new long[n];
        pow[0] = 1;
        for (int i = 1; i < n; i++)
        {
            pow[i] = (pow[i - 1] * 2) % MOD;
        }
        long ans = 0;
        for (int i = 0; i < n; i++)
        {
            long diff = (pow[i] - pow[n - 1 - i]) % MOD;
            if (diff < 0) diff += MOD;
            ans = (ans + diff * nums[i]) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumSubseqWidths = function(nums) {
    const MOD = 1000000007n;
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pow2 = new Array(n);
    pow2[0] = 1n;
    for (let i = 1; i < n; ++i) {
        pow2[i] = (pow2[i - 1] * 2n) % MOD;
    }
    let ans = 0n;
    for (let i = 0; i < n; ++i) {
        const val = BigInt(nums[i]);
        const diff = (pow2[i] - pow2[n - 1 - i] + MOD) % MOD;
        ans = (ans + diff * val) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function sumSubseqWidths(nums: number[]): number {
    const MOD = 1000000007;
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const pow2: number[] = new Array(n);
    pow2[0] = 1;
    for (let i = 1; i < n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const diff = (pow2[i] - pow2[n - 1 - i]) % MOD;
        const contribution = ((diff + MOD) % MOD) * nums[i] % MOD;
        ans = (ans + contribution) % MOD;
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
    function sumSubseqWidths($nums) {
        $mod = 1000000007;
        $n = count($nums);
        sort($nums, SORT_NUMERIC);

        // precompute powers of 2 modulo mod
        $pow = array_fill(0, $n, 1);
        for ($i = 1; $i < $n; $i++) {
            $pow[$i] = ($pow[$i - 1] * 2) % $mod;
        }

        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            $diff = $pow[$i] - $pow[$n - 1 - $i];
            if ($diff < 0) {
                $diff += $mod;
            }
            $res = ($res + $diff * $nums[$i]) % $mod;
        }

        return (int)$res;
    }
}
```

## Swift

```swift
class Solution {
    func sumSubseqWidths(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let sortedNums = nums.sorted()
        let n = sortedNums.count
        if n == 0 { return 0 }
        var pow2 = [Int](repeating: 0, count: n)
        pow2[0] = 1
        if n > 1 {
            for i in 1..<n {
                pow2[i] = Int((Int64(pow2[i - 1]) * 2) % Int64(MOD))
            }
        }
        var result: Int64 = 0
        let mod64 = Int64(MOD)
        for i in 0..<n {
            let diff = pow2[i] - pow2[n - 1 - i]
            var contribution = (Int64(diff) * Int64(sortedNums[i])) % mod64
            if contribution < 0 { contribution += mod64 }
            result = (result + contribution) % mod64
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumSubseqWidths(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        val sorted = nums.clone()
        sorted.sort()
        val n = sorted.size
        if (n == 0) return 0
        val pow2 = LongArray(n)
        pow2[0] = 1L
        for (i in 1 until n) {
            pow2[i] = (pow2[i - 1] * 2L) % MOD
        }
        var ans = 0L
        for (i in 0 until n) {
            val diff = (pow2[i] - pow2[n - 1 - i] + MOD) % MOD
            ans = (ans + diff * sorted[i]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int sumSubseqWidths(List<int> nums) {
    nums.sort();
    int n = nums.length;
    List<int> pow2 = List.filled(n, 0);
    pow2[0] = 1;
    for (int i = 1; i < n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % _mod;
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int diff = pow2[i] - pow2[n - 1 - i];
      if (diff < 0) diff += _mod;
      ans = (ans + (diff * nums[i]) % _mod) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const MOD int = 1000000007

func sumSubseqWidths(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	sort.Ints(nums)

	pow2 := make([]int, n)
	pow2[0] = 1
	for i := 1; i < n; i++ {
		pow2[i] = (pow2[i-1] * 2) % MOD
	}

	var ans int64 = 0
	for i := 0; i < n; i++ {
		diff := pow2[i] - pow2[n-1-i]
		if diff < 0 {
			diff += MOD
		}
		ans = (ans + int64(diff)*int64(nums[i])) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def sum_subseq_widths(nums)
  mod = 1_000_000_007
  nums.sort!
  n = nums.length
  pow2 = Array.new(n, 0)
  pow2[0] = 1
  (1...n).each do |i|
    pow2[i] = (pow2[i - 1] * 2) % mod
  end
  ans = 0
  (0...n).each do |i|
    diff = (pow2[i] - pow2[n - 1 - i]) % mod
    ans = (ans + diff * nums[i]) % mod
  end
  ans
end
```

## Scala

```scala
object Solution {
    def sumSubseqWidths(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = nums.length
        java.util.Arrays.sort(nums)
        val pow2 = new Array[Long](n)
        if (n > 0) pow2(0) = 1L
        for (i <- 1 until n) {
            pow2(i) = (pow2(i - 1) * 2L) % MOD
        }
        var ans = 0L
        for (i <- 0 until n) {
            val diff = (pow2(i) - pow2(n - 1 - i) + MOD) % MOD
            ans = (ans + diff * nums(i).toLong) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_subseq_widths(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        a.sort_unstable();
        let n = a.len();
        if n == 0 {
            return 0;
        }
        let mut pow2: Vec<i64> = vec![1; n];
        for i in 1..n {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        let mut ans: i64 = 0;
        for i in 0..n {
            let diff = (pow2[i] - pow2[n - 1 - i] + MOD) % MOD;
            ans = (ans + diff * a[i]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

(define/contract (sum-subseq-widths nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted)))
    (if (= n 0)
        0
        (begin
          (define pow2 (make-vector n))
          (vector-set! pow2 0 1)
          (for ([i (in-range 1 n)])
            (vector-set! pow2 i (modulo (* (vector-ref pow2 (- i 1)) 2) MOD)))
          (let ((ans 0))
            (for ([i (in-range n)]
                  [val (in-list sorted)])
              (define term (modulo (- (vector-ref pow2 i)
                                      (vector-ref pow2 (- n 1 i))) MOD))
              (define add (modulo (* term (modulo val MOD)) MOD))
              (set! ans (modulo (+ ans add) MOD)))
            ans)))) )
```

## Erlang

```erlang
-module(solution).
-export([sum_subseq_widths/1]).

-spec sum_subseq_widths(Nums :: [integer()]) -> integer().
sum_subseq_widths(Nums) ->
    Mod = 1000000007,
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    Pow2 = pow_list(N, Mod),
    PowRev = lists:reverse(Pow2),
    go(Sorted, Pow2, PowRev, 0, Mod).

pow_list(N, Mod) -> pow_list(N, Mod, 1, []).

pow_list(0, _, Acc) -> lists:reverse(Acc);
pow_list(K, Mod, Cur, Acc) ->
    pow_list(K - 1, Mod, (Cur * 2) rem Mod, [Cur | Acc]).

go([], [], [], Acc, _) -> Acc;
go([X | RestNums], [P1 | RestPowFwd], [P2 | RestPowRev], Acc, Mod) ->
    Diff = (P1 - P2 + Mod) rem Mod,
    Term = (Diff * (X rem Mod)) rem Mod,
    NewAcc = (Acc + Term) rem Mod,
    go(RestNums, RestPowFwd, RestPowRev, NewAcc, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_subseq_widths(nums :: [integer]) :: integer
  def sum_subseq_widths(nums) do
    mod = 1_000_000_007
    sorted = Enum.sort(nums)
    n = length(sorted)

    pow2 = powers_of_two(n, mod)
    rev_pow2 = Enum.reverse(pow2)

    Enum.zip([sorted, pow2, rev_pow2])
    |> Enum.reduce(0, fn {v, left, right}, acc ->
      diff = left - right
      diff = if diff < 0, do: diff + mod, else: diff
      (acc + diff * v) |> rem(mod)
    end)
  end

  defp powers_of_two(n, mod) do
    Enum.reduce(0..(n - 1), [], fn _, acc ->
      val = case acc do
        [] -> 1
        [prev | _] -> rem(prev * 2, mod)
      end
      [val | acc]
    end)
    |> Enum.reverse()
  end
end
```
