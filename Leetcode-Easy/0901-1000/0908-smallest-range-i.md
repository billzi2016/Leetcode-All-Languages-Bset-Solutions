# 0908. Smallest Range I

## Cpp

```cpp
class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int mn = INT_MAX, mx = INT_MIN;
        for (int v : nums) {
            mn = min(mn, v);
            mx = max(mx, v);
        }
        int diff = mx - mn;
        if (diff <= 2 * k) return 0;
        return diff - 2 * k;
    }
};
```

## Java

```java
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num < min) min = num;
            if (num > max) max = num;
        }
        int adjustedMin = min + k;
        int adjustedMax = max - k;
        return Math.max(0, adjustedMax - adjustedMin);
    }
}
```

## Python

```python
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        mn = min(nums)
        return max(0, mx - mn - 2 * k)
```

## Python3

```python
class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        diff = mx - mn - 2 * k
        return diff if diff > 0 else 0
```

## C

```c
int smallestRangeI(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    int mn = nums[0];
    int mx = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    int diff = mx - mn;
    int reduced = diff - 2 * k;
    return reduced > 0 ? reduced : 0;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestRangeI(int[] nums, int k) {
        if (nums == null || nums.Length == 0) return 0;
        int min = nums[0];
        int max = nums[0];
        foreach (int num in nums) {
            if (num < min) min = num;
            if (num > max) max = num;
        }
        int diff = max - min;
        int reduced = diff - 2 * k;
        return reduced > 0 ? reduced : 0;
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
var smallestRangeI = function(nums, k) {
    let minVal = Infinity;
    let maxVal = -Infinity;
    for (const num of nums) {
        if (num < minVal) minVal = num;
        if (num > maxVal) maxVal = num;
    }
    const diff = maxVal - minVal - 2 * k;
    return diff > 0 ? diff : 0;
};
```

## Typescript

```typescript
function smallestRangeI(nums: number[], k: number): number {
    let minVal = nums[0];
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        const v = nums[i];
        if (v < minVal) minVal = v;
        else if (v > maxVal) maxVal = v;
    }
    const diff = maxVal - minVal;
    return Math.max(0, diff - 2 * k);
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
    function smallestRangeI($nums, $k) {
        $min = PHP_INT_MAX;
        $max = PHP_INT_MIN;
        foreach ($nums as $num) {
            if ($num < $min) $min = $num;
            if ($num > $max) $max = $num;
        }
        $diff = $max - $min - 2 * $k;
        return $diff > 0 ? $diff : 0;
    }
}
```

## Swift

```swift
class Solution {
    func smallestRangeI(_ nums: [Int], _ k: Int) -> Int {
        guard let first = nums.first else { return 0 }
        var minVal = first
        var maxVal = first
        for num in nums {
            if num < minVal { minVal = num }
            if num > maxVal { maxVal = num }
        }
        let diff = maxVal - minVal
        let reduced = diff - 2 * k
        return reduced > 0 ? reduced : 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestRangeI(nums: IntArray, k: Int): Int {
        var minVal = Int.MAX_VALUE
        var maxVal = Int.MIN_VALUE
        for (num in nums) {
            if (num < minVal) minVal = num
            if (num > maxVal) maxVal = num
        }
        val diff = maxVal - minVal
        return if (diff <= 2 * k) 0 else diff - 2 * k
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int smallestRangeI(List<int> nums, int k) {
    int mn = nums.reduce(min);
    int mx = nums.reduce(max);
    int diff = mx - mn;
    int result = diff - 2 * k;
    return result < 0 ? 0 : result;
  }
}
```

## Golang

```go
func smallestRangeI(nums []int, k int) int {
	minVal, maxVal := nums[0], nums[0]
	for _, v := range nums {
		if v < minVal {
			minVal = v
		}
		if v > maxVal {
			maxVal = v
		}
	}
	diff := maxVal - minVal
	ans := diff - 2*k
	if ans < 0 {
		return 0
	}
	return ans
}
```

## Ruby

```ruby
def smallest_range_i(nums, k)
  min_val = nums.min
  max_val = nums.max
  diff = max_val - min_val - 2 * k
  diff > 0 ? diff : 0
end
```

## Scala

```scala
object Solution {
    def smallestRangeI(nums: Array[Int], k: Int): Int = {
        val minVal = nums.min
        val maxVal = nums.max
        val diff = maxVal - minVal - 2 * k
        if (diff > 0) diff else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_range_i(nums: Vec<i32>, k: i32) -> i32 {
        let mut min_val = i32::MAX;
        let mut max_val = i32::MIN;
        for &v in nums.iter() {
            if v < min_val { min_val = v; }
            if v > max_val { max_val = v; }
        }
        let diff = max_val - min_val - 2 * k;
        if diff > 0 { diff } else { 0 }
    }
}
```

## Racket

```racket
(define/contract (smallest-range-i nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((minv (apply min nums))
         (maxv (apply max nums))
         (diff (- maxv minv))
         (res (- diff (* 2 k))))
    (if (> res 0) res 0)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_range_i/2]).

-spec smallest_range_i(Nums :: [integer()], K :: integer()) -> integer().
smallest_range_i(Nums, K) ->
    Min = lists:min(Nums),
    Max = lists:max(Nums),
    Diff = Max - Min,
    Res = Diff - 2 * K,
    case Res of
        R when R < 0 -> 0;
        _ -> Res
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_range_i(nums :: [integer], k :: integer) :: integer
  def smallest_range_i(nums, k) do
    min_val = Enum.min(nums)
    max_val = Enum.max(nums)

    diff = max_val - min_val
    res = diff - 2 * k

    if res < 0, do: 0, else: res
  end
end
```
