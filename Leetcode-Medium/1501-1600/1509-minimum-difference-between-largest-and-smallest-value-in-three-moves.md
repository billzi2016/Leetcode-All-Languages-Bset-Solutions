# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

## Cpp

```cpp
class Solution {
public:
    int minDifference(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 4) return 0;
        std::sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 0; i < 4; ++i) {
            int diff = nums[n - 4 + i] - nums[i];
            ans = std::min(ans, diff);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minDifference(int[] nums) {
        int n = nums.length;
        if (n <= 4) return 0;
        java.util.Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < 4; i++) {
            int diff = nums[n - 4 + i] - nums[i];
            if (diff < minDiff) minDiff = diff;
        }
        return minDiff;
    }
}
```

## Python

```python
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(4):
            diff = nums[n - 4 + i] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
```

## Python3

```python
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(4):
            diff = nums[n - 4 + i] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
```

## C

```c
#include <stdlib.h>

static int compare_ints(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int minDifference(int* nums, int numsSize) {
    if (numsSize <= 4) return 0;

    qsort(nums, numsSize, sizeof(int), compare_ints);

    int n = numsSize;
    int diff1 = nums[n - 1] - nums[3];     // remove three smallest
    int diff2 = nums[n - 2] - nums[2];     // remove two smallest, one largest
    int diff3 = nums[n - 3] - nums[1];     // remove one smallest, two largest
    int diff4 = nums[n - 4] - nums[0];     // remove three largest

    int minDiff = diff1;
    if (diff2 < minDiff) minDiff = diff2;
    if (diff3 < minDiff) minDiff = diff3;
    if (diff4 < minDiff) minDiff = diff4;

    return minDiff;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDifference(int[] nums)
    {
        int n = nums.Length;
        if (n <= 4) return 0;

        Array.Sort(nums);
        int minDiff = int.MaxValue;

        for (int i = 0; i < 4; i++)
        {
            int diff = nums[n - 4 + i] - nums[i];
            if (diff < minDiff) minDiff = diff;
        }

        return minDiff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    const n = nums.length;
    if (n <= 4) return 0;
    nums.sort((a, b) => a - b);
    let ans = Infinity;
    for (let i = 0; i < 4; i++) {
        const diff = nums[n - 4 + i] - nums[i];
        if (diff < ans) ans = diff;
    }
    return ans;
};
```

## Typescript

```typescript
function minDifference(nums: number[]): number {
    const n = nums.length;
    if (n <= 4) return 0;
    nums.sort((a, b) => a - b);
    let result = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < 4; ++i) {
        const diff = nums[n - 4 + i] - nums[i];
        if (diff < result) result = diff;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDifference($nums) {
        $n = count($nums);
        if ($n <= 4) {
            return 0;
        }
        sort($nums, SORT_NUMERIC);
        $minDiff = PHP_INT_MAX;
        for ($i = 0; $i < 4; $i++) {
            $diff = $nums[$n - 4 + $i] - $nums[$i];
            if ($diff < $minDiff) {
                $minDiff = $diff;
            }
        }
        return $minDiff;
    }
}
```

## Swift

```swift
class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 4 { return 0 }
        let sorted = nums.sorted()
        var result = Int.max
        for i in 0..<4 {
            let diff = sorted[n - 4 + i] - sorted[i]
            if diff < result {
                result = diff
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDifference(nums: IntArray): Int {
        val n = nums.size
        if (n <= 4) return 0
        nums.sort()
        var ans = Int.MAX_VALUE
        for (i in 0..3) {
            val diff = nums[n - 4 + i] - nums[i]
            if (diff < ans) ans = diff
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minDifference(List<int> nums) {
    int n = nums.length;
    if (n <= 4) return 0;
    nums.sort();
    int ans = nums[n - 1] - nums[0];
    for (int i = 0; i < 4; ++i) {
      int diff = nums[n - 4 + i] - nums[i];
      if (diff < ans) ans = diff;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func minDifference(nums []int) int {
	n := len(nums)
	if n <= 4 {
		return 0
	}
	sort.Ints(nums)
	ans := nums[n-4] - nums[0]
	for i := 1; i < 4; i++ {
		diff := nums[n-4+i] - nums[i]
		if diff < ans {
			ans = diff
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_difference(nums)
  n = nums.length
  return 0 if n <= 4
  nums.sort!
  min_diff = Float::INFINITY
  (0..3).each do |i|
    diff = nums[n - 4 + i] - nums[i]
    min_diff = diff if diff < min_diff
  end
  min_diff
end
```

## Scala

```scala
object Solution {
  def minDifference(nums: Array[Int]): Int = {
    val n = nums.length
    if (n <= 4) return 0
    java.util.Arrays.sort(nums)
    var ans = Int.MaxValue
    for (i <- 0 until 4) {
      val diff = nums(n - 4 + i) - nums(i)
      if (diff < ans) ans = diff
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 4 {
            return 0;
        }
        let mut v = nums.clone();
        v.sort_unstable();
        let mut ans = i32::MAX;
        for i in 0..4 {
            let diff = v[n - 4 + i] - v[i];
            if diff < ans {
                ans = diff;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length nums)))
    (if (<= n 4)
        0
        (let* ((sorted (sort nums <))
               (diffs (map (lambda (k)
                             (- (list-ref sorted (+ (- n 4) k))
                                (list-ref sorted k)))
                           '(0 1 2 3))))
          (apply min diffs)))))
```

## Erlang

```erlang
-module(solution).
-export([min_difference/1]).

-spec min_difference(Nums :: [integer()]) -> integer().
min_difference(Nums) ->
    Len = length(Nums),
    if
        Len =< 4 -> 0;
        true ->
            Sorted = lists:sort(Nums),
            compute_min(Sorted, Len, 0, 1 bsl 60)
    end.

compute_min(_Sorted, _Len, 4, Min) -> Min;
compute_min(Sorted, Len, I, Min) ->
    Left = lists:nth(I + 1, Sorted),
    RightIdx = Len - 4 + I,
    Right = lists:nth(RightIdx + 1, Sorted),
    Diff = Right - Left,
    NewMin = if Diff < Min -> Diff; true -> Min end,
    compute_min(Sorted, Len, I + 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_difference(nums :: [integer]) :: integer
  def min_difference(nums) do
    n = length(nums)

    if n <= 4 do
      0
    else
      sorted = Enum.sort(nums)

      diffs =
        for i <- 0..3 do
          left = Enum.at(sorted, i)
          right = Enum.at(sorted, n - 4 + i)
          right - left
        end

      Enum.min(diffs)
    end
  end
end
```
