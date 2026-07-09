# 3627. Maximum Median Sum of Subsequences of Size 3

## Cpp

```cpp
class Solution {
public:
    long long maximumMedianSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long sum = 0;
        for (int i = n / 3; i < n; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public long maximumMedianSum(int[] nums) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        long sum = 0L;
        for (int i = n - 2; i >= n / 3; i -= 2) {
            sum += nums[i];
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        k = n // 3
        ans = 0
        # take the k largest possible medians: positions n-2, n-4, ..., n-2k
        for i in range(1, k + 1):
            ans += nums[n - 2 * i]
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        groups = n // 3
        idx = n - 2
        total = 0
        for _ in range(groups):
            total += nums[idx]
            idx -= 2
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

long long maximumMedianSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int groups = numsSize / 3;
    long long sum = 0;
    for (int i = 0; i < groups; ++i) {
        sum += (long long)nums[numsSize - 2 - 2 * i];
    }
    return sum;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaximumMedianSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int groups = n / 3;
        long sum = 0;
        for (int i = n - 2, cnt = 0; cnt < groups; i -= 2, cnt++) {
            sum += nums[i];
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumMedianSum = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const groups = n / 3;
    let sum = 0;
    for (let i = 0; i < groups; ++i) {
        // median positions are at n-2, n-4, ..., n-2*groups
        sum += nums[n - 2 - i * 2];
    }
    return sum;
};
```

## Typescript

```typescript
function maximumMedianSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const groups = n / 3;
    let sum = 0;
    for (let i = 0; i < groups; i++) {
        sum += nums[n - 2 - 2 * i];
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumMedianSum($nums) {
        sort($nums, SORT_NUMERIC);
        $n = count($nums);
        $k = intdiv($n, 3);
        $sum = 0;
        $idx = $n - 2; // start from the second largest element
        for ($i = 0; $i < $k; $i++) {
            $sum += $nums[$idx];
            $idx -= 2; // skip one element each time
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maximumMedianSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        let groups = n / 3
        var sum = 0
        for i in 0..<groups {
            sum += sorted[n - 2 - 2 * i]
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumMedianSum(nums: IntArray): Long {
        nums.sort()
        val n = nums.size
        val m = n / 3
        var sum = 0L
        var idx = n - 2
        repeat(m) {
            sum += nums[idx].toLong()
            idx -= 2
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int maximumMedianSum(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int k = n ~/ 3;
    int sum = 0;
    for (int i = n - 2, cnt = 0; cnt < k; i -= 2, cnt++) {
      sum += nums[i];
    }
    return sum;
  }
}
```

## Golang

```go
import "sort"

func maximumMedianSum(nums []int) int64 {
	sort.Ints(nums)
	n := len(nums)
	k := n / 3
	var ans int64 = 0
	for i := n - 2; i >= n-2*k; i -= 2 {
		ans += int64(nums[i])
	}
	return ans
}
```

## Ruby

```ruby
def maximum_median_sum(nums)
  nums.sort!
  n = nums.length
  groups = n / 3
  sum = 0
  idx = n - 2
  groups.times do
    sum += nums[idx]
    idx -= 2
  end
  sum
end
```

## Scala

```scala
object Solution {
  def maximumMedianSum(nums: Array[Int]): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var i = n - 2
    val limit = n / 3
    var sum: Long = 0L
    while (i >= limit) {
      sum += nums(i).toLong
      i -= 2
    }
    sum
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_median_sum(nums: Vec<i32>) -> i64 {
        let mut v = nums;
        v.sort();
        let n = v.len();
        let groups = n / 3;
        let mut sum: i64 = 0;
        for i in 0..groups {
            let idx = n - 2 - 2 * i;
            sum += v[idx] as i64;
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (maximum-median-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (vec (list->vector sorted))
         (n (vector-length vec))
         (groups (/ n 3)))
    (let loop ((i 1) (sum 0))
      (if (> i groups)
          sum
          (loop (+ i 1)
                (+ sum (vector-ref vec (- n (* 2 i)))))))))
```

## Erlang

```erlang
-spec maximum_median_sum(Nums :: [integer()]) -> integer().
maximum_median_sum(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    K2 = 2 * (N div 3),
    Threshold = N - K2,
    {_, Sum} = lists:foldl(
        fun(Elem, {Idx, Acc}) ->
            NewIdx = Idx + 1,
            case (Idx >= Threshold) andalso ((N - Idx) rem 2 == 0) of
                true -> {NewIdx, Acc + Elem};
                false -> {NewIdx, Acc}
            end
        end,
        {0, 0},
        Sorted),
    Sum.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_median_sum(nums :: [integer]) :: integer
  def maximum_median_sum(nums) do
    sorted_desc = Enum.sort(nums, &>=/2)
    groups = div(length(sorted_desc), 3)

    {sum, _} =
      Enum.with_index(sorted_desc)
      |> Enum.reduce({0, 0}, fn {val, idx}, {acc, taken} ->
        if rem(idx, 2) == 1 and taken < groups do
          {acc + val, taken + 1}
        else
          {acc, taken}
        end
      end)

    sum
  end
end
```
