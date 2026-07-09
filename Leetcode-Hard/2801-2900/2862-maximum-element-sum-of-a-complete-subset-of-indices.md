# 2862. Maximum Element-Sum of a Complete Subset of Indices

## Cpp

```cpp
class Solution {
public:
    long long maximumSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> spf(n + 1);
        for (int i = 2; i <= n; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= n)
                    for (int j = i * i; j <= n; j += i)
                        if (!spf[j]) spf[j] = i;
            }
        }
        unordered_map<int, long long> sumByKernel;
        long long best = 0;
        for (int idx = 1; idx <= n; ++idx) {
            int x = idx;
            int kernel = 1;
            while (x > 1) {
                int p = spf[x];
                if (!p) p = x; // prime larger than sqrt(n)
                int parity = 0;
                while (x % p == 0) {
                    x /= p;
                    parity ^= 1;
                }
                if (parity) kernel *= p;
            }
            sumByKernel[kernel] += nums[idx - 1];
            best = max(best, sumByKernel[kernel]);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public long maximumSum(java.util.List<Integer> nums) {
        java.util.Map<Long, Long> sumByKernel = new java.util.HashMap<>();
        int n = nums.size();
        for (int i = 1; i <= n; ++i) {
            long kernel = squareFreePart(i);
            long curSum = sumByKernel.getOrDefault(kernel, 0L) + nums.get(i - 1);
            sumByKernel.put(kernel, curSum);
        }
        long ans = 0;
        for (long v : sumByKernel.values()) {
            if (v > ans) ans = v;
        }
        return ans;
    }

    private long squareFreePart(int x) {
        long res = 1;
        int num = x;
        for (int p = 2; p * p <= num; ++p) {
            if (num % p == 0) {
                int cnt = 0;
                while (num % p == 0) {
                    num /= p;
                    cnt ^= 1; // keep parity only
                }
                if ((cnt & 1) == 1) {
                    res *= p;
                }
            }
        }
        if (num > 1) {
            res *= num;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # smallest prime factor sieve
        spf = [0] * (n + 1)
        for i in range(2, n + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= n:
                    step = i
                    start = i * i
                    for j in range(start, n + 1, step):
                        if spf[j] == 0:
                            spf[j] = i
        spf[1] = 1

        def squarefree(x):
            res = 1
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt ^= 1  # toggle parity
                if cnt:
                    res *= p
            return res

        group_sum = {}
        for idx, val in enumerate(nums, start=1):
            key = squarefree(idx)
            group_sum[key] = group_sum.get(key, 0) + val

        return max(group_sum.values())
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # smallest prime factor for each number up to n
        spf = list(range(n + 1))
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, n + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        group_sum = defaultdict(int)

        for idx, val in enumerate(nums, start=1):
            x = idx
            kernel = 1
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt ^= 1          # keep parity only
                if cnt:
                    kernel *= p
            group_sum[kernel] += val

        return max(group_sum.values())
```

## C

```c
#include <stdlib.h>

long long maximumSum(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int n = numsSize;
    int *spf = (int *)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) spf[i] = i;
    for (int i = 2; i * i <= n; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= n; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    long long *groupSum = (long long *)calloc(n + 1, sizeof(long long));
    long long best = 0;

    for (int idx = 1; idx <= n; ++idx) {
        int x = idx;
        int kernel = 1;
        while (x > 1) {
            int p = spf[x];
            int parity = 0;
            while (x % p == 0) {
                x /= p;
                parity ^= 1;          // toggle exponent parity
            }
            if (parity) kernel *= p;   // include prime with odd exponent
        }
        groupSum[kernel] += (long long)nums[idx - 1];
        if (groupSum[kernel] > best) best = groupSum[kernel];
    }

    free(spf);
    free(groupSum);
    return best;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long MaximumSum(IList<int> nums) {
        int n = nums.Count;
        int[] spf = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= n; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        var sumBySquareFree = new Dictionary<int, long>();
        long best = 0;

        for (int idx = 1; idx <= n; idx++) {
            int sf = SquareFree(idx, spf);
            long curSum = nums[idx - 1];
            if (sumBySquareFree.TryGetValue(sf, out long prev)) {
                curSum += prev;
            }
            sumBySquareFree[sf] = curSum;
            if (curSum > best) best = curSum;
        }

        return best;
    }

    private int SquareFree(int x, int[] spf) {
        int result = 1;
        while (x > 1) {
            int p = spf[x];
            int parity = 0;
            while (x % p == 0) {
                x /= p;
                parity ^= 1; // toggle parity
            }
            if (parity == 1) result *= p;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const n = nums.length;
    
    // compute squarefree part of an integer (product of primes with odd exponent)
    const squareFree = (x) => {
        let res = 1;
        let d = 2;
        while (d * d <= x) {
            if (x % d === 0) {
                let cnt = 0;
                while (x % d === 0) {
                    x /= d;
                    cnt++;
                }
                if (cnt % 2 === 1) res *= d;
            }
            d += (d === 2 ? 1 : 2); // after 2, check only odd numbers
        }
        if (x > 1) res *= x; // remaining prime factor with exponent 1 (odd)
        return res;
    };
    
    const sumMap = new Map();
    for (let i = 1; i <= n; ++i) {
        const key = squareFree(i);
        const cur = sumMap.get(key) || 0;
        sumMap.set(key, cur + nums[i - 1]);
    }
    
    let ans = 0;
    for (const val of sumMap.values()) {
        if (val > ans) ans = val;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSum(nums: number[]): number {
    const n = nums.length;
    // smallest prime factor array
    const spf = new Uint32Array(n + 1);
    for (let i = 2; i * i <= n; ++i) {
        if (spf[i] === 0) { // i is prime
            for (let j = i * i; j <= n; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }
    for (let i = 2; i <= n; ++i) {
        if (spf[i] === 0) spf[i] = i;
    }

    const getSquareFree = (x: number): number => {
        let res = 1;
        while (x > 1) {
            const p = spf[x];
            let cnt = 0;
            while (x % p === 0) {
                x = Math.floor(x / p);
                cnt ^= 1; // keep only parity
            }
            if (cnt) res *= p;
        }
        return res;
    };

    const sumMap = new Map<number, number>();
    let maxSum = 0;

    for (let i = 1; i <= n; ++i) {
        const sf = getSquareFree(i);
        const cur = (sumMap.get(sf) ?? 0) + nums[i - 1];
        sumMap.set(sf, cur);
        if (cur > maxSum) maxSum = cur;
    }

    return maxSum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumSum($nums) {
        $n = count($nums);
        if ($n == 0) return 0;

        // smallest prime factor sieve up to n
        $limit = $n;
        $spf = array_fill(0, $limit + 1, 0);
        for ($i = 2; $i * $i <= $limit; $i++) {
            if ($spf[$i] == 0) {
                for ($j = $i * $i; $j <= $limit; $j += $i) {
                    if ($spf[$j] == 0) {
                        $spf[$j] = $i;
                    }
                }
            }
        }

        $groupSum = [];
        $maxSum = 0;

        for ($idx = 1; $idx <= $n; $idx++) {
            $x = $idx;
            $kernel = 1;
            while ($x > 1) {
                $p = $spf[$x];
                if ($p == 0) { // x is prime
                    $p = $x;
                }
                $cnt = 0;
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                }
                if (($cnt & 1) == 1) {
                    $kernel *= $p;
                }
            }

            $val = $nums[$idx - 1];
            if (!isset($groupSum[$kernel])) {
                $groupSum[$kernel] = 0;
            }
            $groupSum[$kernel] += $val;
            if ($groupSum[$kernel] > $maxSum) {
                $maxSum = $groupSum[$kernel];
            }
        }

        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var spf = [Int](repeating: 0, count: n + 1)
        if n >= 2 {
            for i in 2...n {
                if spf[i] == 0 {
                    spf[i] = i
                    if i * i <= n {
                        var j = i * i
                        while j <= n {
                            if spf[j] == 0 { spf[j] = i }
                            j += i
                        }
                    }
                }
            }
        }
        func kernel(_ x: Int) -> Int {
            var v = x
            var result = 1
            while v > 1 {
                let p = spf[v]
                var parity = 0
                var temp = v
                while temp % p == 0 {
                    temp /= p
                    parity ^= 1
                }
                v = temp
                if parity == 1 {
                    result *= p
                }
            }
            return result
        }
        var sumMap = [Int: Int]()
        for i in 1...n {
            let k = kernel(i)
            sumMap[k, default: 0] += nums[i - 1]
        }
        var ans = 0
        for val in sumMap.values {
            if val > ans { ans = val }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSum(nums: List<Int>): Long {
        val n = nums.size
        // Smallest prime factor sieve
        val spf = IntArray(n + 1) { it }
        var i = 2
        while (i * i <= n) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= n) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
            i++
        }

        val sumMap = HashMap<Int, Long>()
        for (idx in 1..n) {
            var x = idx
            var kernel = 1
            while (x > 1) {
                val p = spf[x]
                var cnt = 0
                while (x % p == 0) {
                    x /= p
                    cnt++
                }
                if ((cnt and 1) == 1) {
                    kernel *= p
                }
            }
            sumMap[kernel] = (sumMap[kernel] ?: 0L) + nums[idx - 1].toLong()
        }

        var ans = 0L
        for (v in sumMap.values) {
            if (v > ans) ans = v
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumSum(List<int> nums) {
    int n = nums.length;
    // Smallest prime factor sieve
    List<int> spf = List.filled(n + 1, 0);
    for (int i = 2; i <= n; i++) {
      if (spf[i] == 0) {
        for (int j = i; j <= n; j += i) {
          if (spf[j] == 0) spf[j] = i;
        }
      }
    }

    Map<int, int> groupSum = {};
    for (int idx = 1; idx <= n; idx++) {
      int x = idx;
      int kernel = 1;
      while (x > 1) {
        int p = spf[x];
        int cnt = 0;
        while (x % p == 0) {
          x ~/= p;
          cnt++;
        }
        if ((cnt & 1) == 1) {
          kernel *= p;
        }
      }
      groupSum[kernel] = (groupSum[kernel] ?? 0) + nums[idx - 1];
    }

    int maxSum = 0;
    for (int sum in groupSum.values) {
      if (sum > maxSum) maxSum = sum;
    }
    return maxSum;
  }
}
```

## Golang

```go
func maximumSum(nums []int) int64 {
    n := len(nums)
    spf := make([]int, n+1)
    for i := 2; i <= n; i++ {
        if spf[i] == 0 {
            spf[i] = i
            if i*i <= n {
                for j := i * i; j <= n; j += i {
                    if spf[j] == 0 {
                        spf[j] = i
                    }
                }
            }
        }
    }

    sums := make(map[int]int64)
    var maxSum int64
    for idx := 1; idx <= n; idx++ {
        x := idx
        sf := 1
        for x > 1 {
            p := spf[x]
            cnt := 0
            for x%p == 0 {
                x /= p
                cnt ^= 1
            }
            if cnt == 1 {
                sf *= p
            }
        }
        sums[sf] += int64(nums[idx-1])
        if sums[sf] > maxSum {
            maxSum = sums[sf]
        }
    }
    return maxSum
}
```

## Ruby

```ruby
def maximum_sum(nums)
  n = nums.length
  max_n = n
  spf = Array.new(max_n + 1, 0)
  (2..max_n).each do |i|
    if spf[i] == 0
      (i..max_n).step(i) { |j| spf[j] = i if spf[j] == 0 }
    end
  end

  sums = Hash.new(0)

  (1..n).each do |idx|
    x = idx
    sf = 1
    while x > 1
      p = spf[x]
      cnt = 0
      while (x % p).zero?
        x /= p
        cnt ^= 1
      end
      sf *= p if cnt == 1
    end
    sums[sf] += nums[idx - 1]
  end

  sums.values.max || 0
end
```

## Scala

```scala
object Solution {
    def maximumSum(nums: List[Int]): Long = {
        val n = nums.length
        // Smallest prime factor sieve
        val spf = new Array[Int](n + 1)
        for (i <- 2 to n) {
            if (spf(i) == 0) {
                var j = i
                while (j <= n) {
                    if (spf(j) == 0) spf(j) = i
                    j += i
                }
            }
        }

        val sums = scala.collection.mutable.Map[Int, Long]()
        var maxSum: Long = 0L

        for (idx <- 1 to n) {
            var x = idx
            var sf = 1
            while (x > 1) {
                val p = spf(x)
                var cnt = 0
                var y = x
                while (y % p == 0) {
                    cnt += 1
                    y /= p
                }
                if ((cnt & 1) == 1) sf *= p
                x = y
            }

            val newSum = sums.getOrElse(sf, 0L) + nums(idx - 1).toLong
            sums.update(sf, newSum)
            if (newSum > maxSum) maxSum = newSum
        }

        maxSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        // smallest prime factor for each number up to n
        let mut spf = vec![0usize; n + 1];
        for i in 2..=n {
            if spf[i] == 0 {
                spf[i] = i;
                if i * i <= n {
                    let mut j = i * i;
                    while j <= n {
                        if spf[j] == 0 {
                            spf[j] = i;
                        }
                        j += i;
                    }
                }
            }
        }

        use std::collections::HashMap;
        let mut sum_by_kernel: HashMap<usize, i64> = HashMap::new();
        let mut max_sum: i64 = 0;

        for (idx, &val) in nums.iter().enumerate() {
            let mut x = idx + 1; // 1‑indexed position
            let mut kernel = 1usize;
            while x > 1 {
                let p = spf[x];
                let mut odd = false;
                while x % p == 0 {
                    x /= p;
                    odd ^= true; // toggle parity of exponent
                }
                if odd {
                    kernel *= p;
                }
            }

            let entry = sum_by_kernel.entry(kernel).or_insert(0);
            *entry += val as i64;
            if *entry > max_sum {
                max_sum = *entry;
            }
        }

        max_sum
    }
}
```

## Racket

```racket
(define/contract (maximum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [spf (make-vector (+ n 1) 0)])
    ;; smallest prime factor sieve
    (for ([i (in-range 2 (+ n 1))])
      (when (= (vector-ref spf i) 0)
        (vector-set! spf i i)
        (let loop ((j (* i i)))
          (when (<= j n)
            (when (= (vector-ref spf j) 0)
              (vector-set! spf j i))
            (set! j (+ j i))))))
    ;; compute squarefree part for each index
    (define sqfree (make-vector (+ n 1) 0))
    (vector-set! sqfree 1 1)
    (for ([i (in-range 2 (+ n 1))])
      (let* ([p (vector-ref spf i)]
             [j (/ i p)])
        (if (= (remainder j p) 0)
            (vector-set! sqfree i (vector-ref sqfree (/ j p)))
            (vector-set! sqfree i (* (vector-ref sqfree j) p)))))
    ;; accumulate sums per squarefree key
    (define ht (make-hash))
    (for ([i (in-range 1 (+ n 1))])
      (let* ([key (vector-ref sqfree i)]
             [prev (hash-ref ht key 0)]
             [new-sum (+ prev (vector-ref arr (- i 1)))])
        (hash-set! ht key new-sum)))
    ;; find maximum sum
    (define max-sum 0)
    (for ([v (in-hash-values ht)])
      (when (> v max-sum) (set! max-sum v)))
    max-sum))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum/1]).

-spec maximum_sum([integer()]) -> integer().
maximum_sum(Nums) ->
    Len = length(Nums),
    SumMap = lists:foldl(
        fun({Val, Idx}, Acc) ->
            Kernel = squarefree_kernel(Idx),
            Prev = maps:get(Kernel, Acc, 0),
            maps:put(Kernel, Prev + Val, Acc)
        end,
        #{},
        lists:zip(Nums, lists:seq(1, Len))
    ),
    maps:fold(fun(_K, V, Acc) -> erlang:max(V, Acc) end, 0, SumMap).

squarefree_kernel(N) when N >= 1 ->
    squarefree_kernel(N, 2, 1).

squarefree_kernel(1, _D, Res) ->
    Res;
squarefree_kernel(N, D, Res) when D * D > N ->
    Res * N; % remaining prime factor with odd exponent (1)
squarefree_kernel(N, D, Res) ->
    case N rem D of
        0 ->
            {Cnt, Rest} = count_factor(N, D, 0),
            NewRes = if (Cnt band 1) == 1 -> Res * D; true -> Res end,
            squarefree_kernel(Rest, D + 1, NewRes);
        _ ->
            squarefree_kernel(N, D + 1, Res)
    end.

count_factor(N, D, Cnt) when N rem D =:= 0 ->
    count_factor(N div D, D, Cnt + 1);
count_factor(N, _D, Cnt) ->
    {Cnt, N}.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(nums :: [integer]) :: integer
  def maximum_sum(nums) do
    nums
    |> Enum.with_index(1)
    |> Enum.reduce(%{}, fn {val, idx}, acc ->
      key = square_free(idx)
      Map.update(acc, key, val, &(&1 + val))
    end)
    |> Map.values()
    |> Enum.max(fn -> 0 end)
  end

  defp square_free(i), do: compute_sf(i, 2, 1)

  defp compute_sf(1, _p, acc), do: acc

  defp compute_sf(x, p, acc) when p * p > x do
    # remaining prime factor with exponent 1 (odd)
    acc * x
  end

  defp compute_sf(x, p, acc) do
    if rem(x, p) == 0 do
      {x2, cnt} = remove_factor(x, p, 0)

      new_acc =
        if rem(cnt, 2) == 1 do
          acc * p
        else
          acc
        end

      compute_sf(x2, p + 1, new_acc)
    else
      compute_sf(x, p + 1, acc)
    end
  end

  defp remove_factor(x, p, cnt) do
    if rem(x, p) == 0 do
      remove_factor(div(x, p), p, cnt + 1)
    else
      {x, cnt}
    end
  end
end
```
