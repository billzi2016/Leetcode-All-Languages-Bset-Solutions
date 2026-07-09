# 1498. Number of Subsequences That Satisfy the Given Sum Condition

## Cpp

```cpp
class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        const int MOD = 1'000'000'007;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<long long> pow2(n);
        pow2[0] = 1;
        for (int i = 1; i < n; ++i) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long long ans = 0;
        int left = 0, right = n - 1;
        while (left <= right) {
            if ((long long)nums[left] + nums[right] <= target) {
                ans = (ans + pow2[right - left]) % MOD;
                ++left;
            } else {
                --right;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] pow2 = new long[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] << 1) % MOD;
        }
        
        int left = 0, right = n - 1;
        long ans = 0;
        while (left <= right) {
            if ((long) nums[left] + nums[right] <= target) {
                ans += pow2[right - left];
                if (ans >= MOD) ans -= MOD;
                left++;
            } else {
                right--;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        # precompute powers of 2 modulo MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] << 1) % MOD

        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        return ans
```

## Python3

```python
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] << 1) % MOD

        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int numSubseq(int* nums, int numsSize, int target) {
    const int MOD = 1000000007;
    if (numsSize == 0) return 0;

    qsort(nums, numsSize, sizeof(int), cmp_int);

    long long *pow2 = (long long *)malloc((numsSize + 1) * sizeof(long long));
    pow2[0] = 1;
    for (int i = 1; i <= numsSize; ++i) {
        pow2[i] = (pow2[i - 1] << 1) % MOD;
    }

    int left = 0, right = numsSize - 1;
    long long ans = 0;

    while (left <= right) {
        if ((long long)nums[left] + nums[right] <= target) {
            ans += pow2[right - left];
            if (ans >= MOD) ans -= MOD;
            ++left;
        } else {
            --right;
        }
    }

    free(pow2);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSubseq(int[] nums, int target) {
        const int MOD = 1000000007;
        Array.Sort(nums);
        int n = nums.Length;
        long[] pow2 = new long[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long ans = 0;
        int left = 0, right = n - 1;
        while (left <= right) {
            if ((long)nums[left] + nums[right] <= target) {
                ans = (ans + pow2[right - left]) % MOD;
                left++;
            } else {
                right--;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {
    const MOD = 1000000007;
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pow2 = new Array(n);
    pow2[0] = 1;
    for (let i = 1; i < n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    let left = 0, right = n - 1;
    let ans = 0;
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            ans = (ans + pow2[right - left]) % MOD;
            left++;
        } else {
            right--;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numSubseq(nums: number[], target: number): number {
    const MOD = 1_000_000_007;
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pow2 = new Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    let left = 0, right = n - 1;
    let ans = 0;
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            ans = (ans + pow2[right - left]) % MOD;
            left++;
        } else {
            right--;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function numSubseq($nums, $target) {
        $mod = 1000000007;
        sort($nums);
        $n = count($nums);
        $pow2 = array_fill(0, $n, 1);
        for ($i = 1; $i < $n; $i++) {
            $pow2[$i] = ($pow2[$i - 1] * 2) % $mod;
        }
        $left = 0;
        $right = $n - 1;
        $ans = 0;
        while ($left <= $right) {
            if ($nums[$left] + $nums[$right] <= $target) {
                $ans = ($ans + $pow2[$right - $left]) % $mod;
                $left++;
            } else {
                $right--;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numSubseq(_ nums: [Int], _ target: Int) -> Int {
        let MOD = 1_000_000_007
        let sorted = nums.sorted()
        let n = sorted.count
        var pow2 = [Int](repeating: 0, count: n)
        if n > 0 { pow2[0] = 1 }
        if n > 1 {
            for i in 1..<n {
                pow2[i] = Int((Int64(pow2[i - 1]) * 2) % Int64(MOD))
            }
        }
        var left = 0
        var right = n - 1
        var ans = 0
        while left <= right {
            if sorted[left] + sorted[right] <= target {
                let add = pow2[right - left]
                ans += add
                if ans >= MOD { ans -= MOD }
                left += 1
            } else {
                right -= 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSubseq(nums: IntArray, target: Int): Int {
        val MOD = 1_000_000_007L
        nums.sort()
        val n = nums.size
        val pow = LongArray(n)
        pow[0] = 1L
        for (i in 1 until n) {
            pow[i] = (pow[i - 1] * 2) % MOD
        }
        var left = 0
        var right = n - 1
        var ans = 0L
        while (left <= right) {
            if (nums[left].toLong() + nums[right] <= target.toLong()) {
                ans += pow[right - left]
                if (ans >= MOD) ans -= MOD
                left++
            } else {
                right--
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numSubseq(List<int> nums, int target) {
    nums.sort();
    final n = nums.length;
    final pow2 = List<int>.filled(n + 1, 0);
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % _mod;
    }

    int left = 0, right = n - 1;
    int ans = 0;

    while (left <= right) {
      if (nums[left] + nums[right] <= target) {
        ans = (ans + pow2[right - left]) % _mod;
        ++left;
      } else {
        --right;
      }
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

func numSubseq(nums []int, target int) int {
	const mod int64 = 1000000007
	sort.Ints(nums)
	n := len(nums)

	pow := make([]int64, n)
	if n > 0 {
		pow[0] = 1
	}
	for i := 1; i < n; i++ {
		pow[i] = (pow[i-1] * 2) % mod
	}

	left, right := 0, n-1
	var ans int64 = 0
	for left <= right {
		if nums[left]+nums[right] <= target {
			ans = (ans + pow[right-left]) % mod
			left++
		} else {
			right--
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def num_subseq(nums, target)
  mod = 1_000_000_007
  nums.sort!
  n = nums.length
  pow2 = Array.new(n, 1)
  (1...n).each { |i| pow2[i] = (pow2[i - 1] * 2) % mod }

  left = 0
  right = n - 1
  ans = 0

  while left <= right
    if nums[left] + nums[right] <= target
      ans = (ans + pow2[right - left]) % mod
      left += 1
    else
      right -= 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numSubseq(nums: Array[Int], target: Int): Int = {
        val mod = 1000000007L
        java.util.Arrays.sort(nums)
        val n = nums.length
        val pow2 = new Array[Long](n + 1)
        pow2(0) = 1L
        var i = 1
        while (i <= n) {
            pow2(i) = (pow2(i - 1) * 2) % mod
            i += 1
        }
        var left = 0
        var right = n - 1
        var ans = 0L
        while (left <= right) {
            if (nums(left).toLong + nums(right).toLong <= target) {
                ans = (ans + pow2(right - left)) % mod
                left += 1
            } else {
                right -= 1
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_subseq(nums: Vec<i32>, target: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut nums = nums;
        nums.sort_unstable();
        let n = nums.len();

        // precompute powers of two modulo MOD
        let mut pow2 = vec![0i64; n];
        if n > 0 {
            pow2[0] = 1;
            for i in 1..n {
                pow2[i] = (pow2[i - 1] * 2) % MOD;
            }
        }

        let mut left: usize = 0;
        let mut right: isize = n as isize - 1;
        let mut ans: i64 = 0;

        while (left as isize) <= right {
            let sum = nums[left] as i64 + nums[right as usize] as i64;
            if sum <= target as i64 {
                let idx = (right as usize - left) as usize;
                ans += pow2[idx];
                if ans >= MOD {
                    ans -= MOD;
                }
                left += 1;
            } else {
                right -= 1;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (num-subseq nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (define MOD 1000000007)
  (if (null? nums)
      0
      (let* ((sorted (list->vector (sort nums <)))
             (n (vector-length sorted))
             (pow2 (let ([v (make-vector (+ n 1) 0)])
                     (vector-set! v 0 1)
                     (for ([k (in-range 1 (+ n 1))])
                       (vector-set! v k (modulo (* (vector-ref v (- k 1)) 2) MOD)))
                     v))
             (ans
              (let loop ((i 0) (j (- n 1)) (acc 0))
                (if (> i j)
                    acc
                    (let ([sum (+ (vector-ref sorted i) (vector-ref sorted j))])
                      (if (<= sum target)
                          (let* ([add (vector-ref pow2 (- j i))]
                                 [new-acc (modulo (+ acc add) MOD)])
                            (loop (+ i 1) j new-acc))
                          (loop i (- j 1) acc)))))))
        ans)))
```

## Erlang

```erlang
-module(solution).
-export([num_subseq/2]).
-define(MOD, 1000000007).

-spec num_subseq(Nums :: [integer()], Target :: integer()) -> integer().
num_subseq(Nums, Target) ->
    Sorted = lists:sort(Nums),
    Arr = list_to_tuple(Sorted),
    N = tuple_size(Arr),
    Pow = make_pow(N),                     % Pow[i] = 2^(i-1) mod MOD, i starts from 1
    loop(0, N - 1, Arr, Target, Pow, 0).

make_pow(N) ->
    make_pow(0, N, 1, []).

make_pow(I, N, Cur, Acc) when I < N ->
    NewAcc = [Cur | Acc],
    Next = (Cur * 2) rem ?MOD,
    make_pow(I + 1, N, Next, NewAcc);
make_pow(_, _, _, Acc) ->
    list_to_tuple(lists:reverse(Acc)).

loop(I, J, _Arr, _Target, _Pow, Ans) when I > J ->
    Ans;
loop(I, J, Arr, Target, Pow, Ans) ->
    Ai = element(I + 1, Arr),
    Aj = element(J + 1, Arr),
    if
        Ai + Aj =< Target ->
            Exp = J - I,
            Add = element(Exp + 1, Pow),
            NewAns = (Ans + Add) rem ?MOD,
            loop(I + 1, J, Arr, Target, Pow, NewAns);
        true ->
            loop(I, J - 1, Arr, Target, Pow, Ans)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec num_subseq(nums :: [integer], target :: integer) :: integer
  def num_subseq(nums, target) do
    mod = 1_000_000_007

    sorted = Enum.sort(nums)
    n = length(sorted)

    # powers[i] = 2^i % mod
    powers_list =
      Stream.iterate(1, fn x -> rem(x * 2, mod) end)
      |> Enum.take(n)

    powers = List.to_tuple(powers_list)
    arr = List.to_tuple(sorted)

    count(arr, target, powers, 0, n - 1, 0, mod)
  end

  defp count(_arr, _target, _powers, left, right, acc, _mod) when left > right,
    do: acc

  defp count(arr, target, powers, left, right, acc, mod) do
    if elem(arr, left) + elem(arr, right) <= target do
      add = elem(powers, right - left)
      new_acc = rem(acc + add, mod)
      count(arr, target, powers, left + 1, right, new_acc, mod)
    else
      count(arr, target, powers, left, right - 1, acc, mod)
    end
  end
end
```
