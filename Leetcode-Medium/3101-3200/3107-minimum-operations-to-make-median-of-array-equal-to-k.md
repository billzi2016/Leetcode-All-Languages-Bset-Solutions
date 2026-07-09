# 3107. Minimum Operations to Make Median of Array Equal to K

## Cpp

```cpp
class Solution {
public:
    long long minOperationsToMakeMedianK(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int mid = n / 2; // upper median index
        long long ops = 0;
        for (int i = 0; i <= mid; ++i) {
            if (nums[i] > k) ops += (long long)(nums[i] - k);
        }
        for (int i = mid; i < n; ++i) {
            if (nums[i] < k) ops += (long long)(k - nums[i]);
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public long minOperationsToMakeMedianK(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int mid = n / 2; // larger middle for even length
        long ops = Math.abs((long)nums[mid] - k);
        for (int i = 0; i < mid; i++) {
            if (nums[i] > k) {
                ops += (long)nums[i] - k;
            }
        }
        for (int i = mid + 1; i < n; i++) {
            if (nums[i] < k) {
                ops += (long)k - nums[i];
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        m = n // 2  # upper median index
        ops = abs(nums[m] - k)
        for i in range(m):
            if nums[i] > k:
                ops += nums[i] - k
        for i in range(m + 1, n):
            if nums[i] < k:
                ops += k - nums[i]
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = len(nums) // 2
        ops = 0
        for i in range(m):
            if nums[i] > k:
                ops += nums[i] - k
        for i in range(m + 1, len(nums)):
            if nums[i] < k:
                ops += k - nums[i]
        ops += abs(nums[m] - k)
        return ops
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    long av = *(const int *)a;
    long bv = *(const int *)b;
    if (av < bv) return -1;
    if (av > bv) return 1;
    return 0;
}

long long minOperationsToMakeMedianK(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int m = numsSize / 2; // index of median (larger middle for even length)
    long long ops = 0;
    for (int i = 0; i <= m; ++i) {
        if (nums[i] > k) ops += (long long)(nums[i] - k);
    }
    for (int i = m; i < numsSize; ++i) {
        if (nums[i] < k) ops += (long long)(k - nums[i]);
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public long MinOperationsToMakeMedianK(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length;
        int medianIdx = n / 2; // larger middle for even length
        long ops = Math.Abs((long)nums[medianIdx] - k);
        for (int i = 0; i < medianIdx; i++) {
            if (nums[i] > k) {
                ops += (long)nums[i] - k;
            }
        }
        for (int i = medianIdx + 1; i < n; i++) {
            if (nums[i] < k) {
                ops += (long)k - nums[i];
            }
        }
        return ops;
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
var minOperationsToMakeMedianK = function(nums, k) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const medianIdx = Math.floor(n / 2);
    let ops = 0;
    for (let i = 0; i < n; ++i) {
        if (i <= medianIdx && nums[i] > k) {
            ops += nums[i] - k;
        } else if (i >= medianIdx && nums[i] < k) {
            ops += k - nums[i];
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minOperationsToMakeMedianK(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const mid = Math.floor(n / 2);
    let ops = 0;
    for (let i = 0; i < mid; i++) {
        if (nums[i] > k) ops += nums[i] - k;
    }
    for (let i = mid + 1; i < n; i++) {
        if (nums[i] < k) ops += k - nums[i];
    }
    ops += Math.abs(nums[mid] - k);
    return ops;
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
    function minOperationsToMakeMedianK($nums, $k) {
        sort($nums, SORT_NUMERIC);
        $n = count($nums);
        $mid = intdiv($n, 2);
        $ops = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i < $mid) {
                if ($nums[$i] > $k) {
                    $ops += $nums[$i] - $k;
                }
            } elseif ($i > $mid) {
                if ($nums[$i] < $k) {
                    $ops += $k - $nums[$i];
                }
            } else { // i == $mid
                $ops += abs($nums[$i] - $k);
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperationsToMakeMedianK(_ nums: [Int], _ k: Int) -> Int {
        var arr = nums.sorted()
        let n = arr.count
        let m = n / 2
        var ops: Int64 = 0
        
        // Left side elements should not exceed k
        for i in 0..<m {
            if arr[i] > k {
                ops += Int64(arr[i] - k)
            }
        }
        
        // Right side elements should not be less than k
        if m + 1 < n {
            for i in (m + 1)..<n {
                if arr[i] < k {
                    ops += Int64(k - arr[i])
                }
            }
        }
        
        // Adjust the median itself to k
        ops += Int64(abs(arr[m] - k))
        
        return Int(ops)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperationsToMakeMedianK(nums: IntArray, k: Int): Long {
        val arr = nums.clone()
        java.util.Arrays.sort(arr)
        val m = arr.size / 2
        var ops = 0L
        for (i in 0 until m) {
            if (arr[i] > k) ops += (arr[i] - k).toLong()
        }
        for (i in m + 1 until arr.size) {
            if (arr[i] < k) ops += (k - arr[i]).toLong()
        }
        ops += kotlin.math.abs(arr[m] - k).toLong()
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperationsToMakeMedianK(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    int mid = n ~/ 2;
    int ops = 0;
    for (int i = 0; i < n; i++) {
      if (i < mid && nums[i] > k) {
        ops += nums[i] - k;
      } else if (i == mid) {
        ops += (nums[i] - k).abs();
      } else if (i > mid && nums[i] < k) {
        ops += k - nums[i];
      }
    }
    return ops;
  }
}
```

## Golang

```go
import "sort"

func minOperationsToMakeMedianK(nums []int, k int) int64 {
	sort.Ints(nums)
	n := len(nums)
	mid := n / 2
	var ops int64

	for i := 0; i < mid; i++ {
		if nums[i] > k {
			ops += int64(nums[i] - k)
		}
	}
	for i := mid + 1; i < n; i++ {
		if nums[i] < k {
			ops += int64(k - nums[i])
		}
	}
	diff := nums[mid] - k
	if diff < 0 {
		diff = -diff
	}
	ops += int64(diff)
	return ops
}
```

## Ruby

```ruby
def min_operations_to_make_median_k(nums, k)
  a = nums.sort
  m = a.length / 2
  ops = 0
  a.each_with_index do |val, i|
    if i < m
      ops += val - k if val > k
    elsif i > m
      ops += k - val if val < k
    else
      ops += (val - k).abs
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperationsToMakeMedianK(nums: Array[Int], k: Int): Long = {
        val sorted = nums.sorted
        val n = sorted.length
        val mid = n / 2
        var ops: Long = 0L

        var i = 0
        while (i < mid) {
            if (sorted(i) > k) ops += sorted(i).toLong - k
            i += 1
        }

        ops += math.abs(sorted(mid).toLong - k)

        i = mid + 1
        while (i < n) {
            if (sorted(i) < k) ops += k.toLong - sorted(i)
            i += 1
        }

        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations_to_make_median_k(nums: Vec<i32>, k: i32) -> i64 {
        let mut v = nums;
        v.sort_unstable();
        let n = v.len();
        let m = n / 2;
        let mut ans: i64 = 0;
        // Left side including median
        for i in 0..=m {
            if v[i] > k {
                ans += (v[i] - k) as i64;
            }
        }
        // Right side including median
        for i in m..n {
            if v[i] < k {
                ans += (k - v[i]) as i64;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations-to-make-median-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (mid (quotient n 2)))
    (for/sum ([i (in-range n)]
              [val (in-list sorted)])
      (cond
        [(= i mid) (abs (- val k))]
        [(< i mid) (if (> val k) (- val k) 0)]
        [(> i mid) (if (< val k) (- k val) 0)]))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations_to_make_median_k/2]).

-spec min_operations_to_make_median_k(Nums :: [integer()], K :: integer()) -> integer().
min_operations_to_make_median_k(Nums, K) ->
    Sorted = lists:sort(Nums),
    Len = length(Sorted),
    Idx = Len div 2,
    Median = lists:nth(Idx + 1, Sorted),
    if
        Median == K ->
            0;
        Median > K ->
            Prefix = lists:sublist(Sorted, Idx + 1),
            lists:foldl(fun(X, Acc) ->
                if X > K -> Acc + (X - K); true -> Acc end
            end, 0, Prefix);
        Median < K ->
            Suffix = lists:nthtail(Idx, Sorted),
            lists:foldl(fun(X, Acc) ->
                if X < K -> Acc + (K - X); true -> Acc end
            end, 0, Suffix)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations_to_make_median_k(nums :: [integer], k :: integer) :: integer
  def min_operations_to_make_median_k(nums, k) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    mid = div(n, 2)
    median = Enum.at(sorted, mid)

    cond do
      median == k ->
        0

      median < k ->
        Enum.reduce(Enum.slice(sorted, mid, n - mid), 0, fn x, acc ->
          if x < k, do: acc + (k - x), else: acc
        end)

      true -> # median > k
        Enum.reduce(Enum.take(sorted, mid + 1), 0, fn x, acc ->
          if x > k, do: acc + (x - k), else: acc
        end)
    end
  end
end
```
