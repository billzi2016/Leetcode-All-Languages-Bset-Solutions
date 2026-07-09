# 0747. Largest Number At Least Twice of Others

## Cpp

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int n = nums.size();
        int maxIdx = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }
        for (int i = 0; i < n; ++i) {
            if (i == maxIdx) continue;
            if (nums[maxIdx] < 2 * nums[i]) return -1;
        }
        return maxIdx;
    }
};
```

## Java

```java
class Solution {
    public int dominantIndex(int[] nums) {
        int max = Integer.MIN_VALUE;
        int maxIdx = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
                maxIdx = i;
            }
        }
        for (int num : nums) {
            if (num != max && max < 2L * num) {
                return -1;
            }
        }
        return maxIdx;
    }
}
```

## Python

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = -1
        max_idx = -1
        for i, v in enumerate(nums):
            if v > max_val:
                max_val = v
                max_idx = i
        # find second maximum
        second_max = 0
        for v in nums:
            if v != max_val and v > second_max:
                second_max = v
        return max_idx if max_val >= 2 * second_max else -1
```

## Python3

```python
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = -1
        max_idx = -1
        for i, v in enumerate(nums):
            if v > max_val:
                max_val = v
                max_idx = i
        for v in nums:
            if v != max_val and max_val < 2 * v:
                return -1
        return max_idx
```

## C

```c
int dominantIndex(int* nums, int numsSize) {
    if (numsSize == 0) return -1;
    int max = nums[0];
    int idx = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > max) {
            max = nums[i];
            idx = i;
        }
    }
    for (int i = 0; i < numsSize; ++i) {
        if (i == idx) continue;
        if (max < 2 * nums[i]) return -1;
    }
    return idx;
}
```

## Csharp

```csharp
public class Solution {
    public int DominantIndex(int[] nums) {
        if (nums == null || nums.Length == 0) return -1;
        int maxVal = nums[0];
        int maxIdx = 0;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] > maxVal) {
                maxVal = nums[i];
                maxIdx = i;
            }
        }
        for (int i = 0; i < nums.Length; i++) {
            if (i == maxIdx) continue;
            if (maxVal < 2L * nums[i]) return -1;
        }
        return maxIdx;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let max = -Infinity, maxIdx = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > max) {
            max = nums[i];
            maxIdx = i;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (i !== maxIdx && max < 2 * nums[i]) {
            return -1;
        }
    }
    return maxIdx;
};
```

## Typescript

```typescript
function dominantIndex(nums: number[]): number {
    let max = -1, idx = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > max) {
            max = nums[i];
            idx = i;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (i !== idx && max < 2 * nums[i]) {
            return -1;
        }
    }
    return idx;
};
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function dominantIndex($nums) {
        $max = -1;
        $maxIdx = -1;
        foreach ($nums as $i => $val) {
            if ($val > $max) {
                $max = $val;
                $maxIdx = $i;
            }
        }
        foreach ($nums as $i => $val) {
            if ($i !== $maxIdx && $max < 2 * $val) {
                return -1;
            }
        }
        return $maxIdx;
    }
}
```

## Swift

```swift
class Solution {
    func dominantIndex(_ nums: [Int]) -> Int {
        var maxVal = Int.min
        var maxIdx = -1
        for (i, v) in nums.enumerated() {
            if v > maxVal {
                maxVal = v
                maxIdx = i
            }
        }
        for v in nums {
            if v != maxVal && maxVal < 2 * v {
                return -1
            }
        }
        return maxIdx
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dominantIndex(nums: IntArray): Int {
        var max = Int.MIN_VALUE
        var index = -1
        for (i in nums.indices) {
            if (nums[i] > max) {
                max = nums[i]
                index = i
            }
        }
        for (i in nums.indices) {
            if (i != index && max < 2 * nums[i]) return -1
        }
        return index
    }
}
```

## Dart

```dart
class Solution {
  int dominantIndex(List<int> nums) {
    int maxVal = -1;
    int maxIdx = -1;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > maxVal) {
        maxVal = nums[i];
        maxIdx = i;
      }
    }
    for (int num in nums) {
      if (num != maxVal && maxVal < 2 * num) {
        return -1;
      }
    }
    return maxIdx;
  }
}
```

## Golang

```go
func dominantIndex(nums []int) int {
    maxVal, maxIdx := nums[0], 0
    for i, v := range nums {
        if v > maxVal {
            maxVal = v
            maxIdx = i
        }
    }
    for _, v := range nums {
        if v != maxVal && maxVal < 2*v {
            return -1
        }
    }
    return maxIdx
}
```

## Ruby

```ruby
def dominant_index(nums)
  max = nums.max
  max_idx = nums.index(max)
  nums.each do |x|
    next if x == max
    return -1 if max < 2 * x
  end
  max_idx
end
```

## Scala

```scala
object Solution {
    def dominantIndex(nums: Array[Int]): Int = {
        var maxVal = Int.MinValue
        var maxIdx = -1
        for (i <- nums.indices) {
            if (nums(i) > maxVal) {
                maxVal = nums(i)
                maxIdx = i
            }
        }
        for (i <- nums.indices) {
            if (i != maxIdx && maxVal < 2 * nums(i)) return -1
        }
        maxIdx
    }
}
```

## Rust

```rust
impl Solution {
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        let mut max_val = nums[0];
        let mut max_idx = 0;
        for (i, &v) in nums.iter().enumerate() {
            if v > max_val {
                max_val = v;
                max_idx = i;
            }
        }
        for &v in nums.iter() {
            if v != max_val && max_val < 2 * v {
                return -1;
            }
        }
        max_idx as i32
    }
}
```

## Racket

```racket
(define/contract (dominant-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((max -1)
        (idx -1))
    ;; Find maximum value and its index
    (for ([x nums] [i (in-naturals)])
      (when (> x max)
        (set! max x)
        (set! idx i)))
    ;; Check if any other element violates the condition
    (define violates?
      (for/or ([x nums] [i (in-naturals)])
        (and (not (= i idx)) (< max (* 2 x)))))
    (if violates? -1 idx)))
```

## Erlang

```erlang
-module(solution).
-export([dominant_index/1]).

-spec dominant_index(Nums :: [integer()]) -> integer().
dominant_index(Nums) ->
    {Max, MaxIdx} = find_max(Nums, 0, -1, -1),
    case check(Max, Nums, MaxIdx) of
        true -> MaxIdx;
        false -> -1
    end.

find_max([], _, Max, Idx) -> {Max, Idx};
find_max([H|T], I, CurMax, CurIdx) ->
    if H > CurMax ->
            find_max(T, I+1, H, I);
       true ->
            find_max(T, I+1, CurMax, CurIdx)
    end.

check(Max, List, MaxIdx) -> check(List, 0, Max, MaxIdx).

check([], _, _, _) -> true;
check([H|T], I, Max, MaxIdx) ->
    if I =/= MaxIdx andalso Max < 2*H ->
            false;
       true ->
            check(T, I+1, Max, MaxIdx)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec dominant_index(nums :: [integer]) :: integer
  def dominant_index(nums) do
    {max_val, max_idx} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({-1, -1}, fn {val, idx}, {cur_max, cur_i} ->
        if val > cur_max, do: {val, idx}, else: {cur_max, cur_i}
      end)

    if Enum.all?(nums, fn x -> max_val >= 2 * x or x == max_val end) do
      max_idx
    else
      -1
    end
  end
end
```
