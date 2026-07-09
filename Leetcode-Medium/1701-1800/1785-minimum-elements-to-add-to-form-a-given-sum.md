# 1785. Minimum Elements to Add to Form a Given Sum

## Cpp

```cpp
class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        long long sum = 0;
        for (int v : nums) sum += v;
        long long diff = static_cast<long long>(goal) - sum;
        long long need = llabs(diff);
        long long ans = (need + limit - 1) / limit;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int minElements(int[] nums, int limit, int goal) {
        long sum = 0L;
        for (int v : nums) {
            sum += v;
        }
        long diff = Math.abs((long) goal - sum);
        long ans = (diff + limit - 1L) / limit;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        total = sum(nums)
        diff = goal - total
        if diff == 0:
            return 0
        return (abs(diff) + limit - 1) // limit
```

## Python3

```python
from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        diff = abs(goal - current_sum)
        if diff == 0:
            return 0
        return (diff + limit - 1) // limit
```

## C

```c
#include <stdlib.h>

int minElements(int* nums, int numsSize, int limit, int goal) {
    long long sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
    }
    long long diff = (long long)goal - sum;
    long long absDiff = llabs(diff);
    if (absDiff == 0) return 0;
    long long ans = (absDiff + limit - 1) / limit;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinElements(int[] nums, int limit, int goal) {
        long sum = 0;
        foreach (int x in nums) {
            sum += x;
        }
        long diff = Math.Abs((long)goal - sum);
        long ans = (diff + limit - 1L) / limit;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @param {number} goal
 * @return {number}
 */
var minElements = function(nums, limit, goal) {
    let sum = 0;
    for (const v of nums) sum += v;
    const diff = Math.abs(goal - sum);
    return Math.floor((diff + limit - 1) / limit);
};
```

## Typescript

```typescript
function minElements(nums: number[], limit: number, goal: number): number {
    let sum = 0;
    for (const num of nums) {
        sum += num;
    }
    const diff = Math.abs(goal - sum);
    if (diff === 0) return 0;
    return Math.floor((diff + limit - 1) / limit);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @param Integer $goal
     * @return Integer
     */
    function minElements($nums, $limit, $goal) {
        $sum = array_sum($nums);
        $diff = $goal - $sum;
        $absDiff = abs($diff);
        if ($absDiff == 0) {
            return 0;
        }
        return intdiv($absDiff + $limit - 1, $limit);
    }
}
```

## Swift

```swift
class Solution {
    func minElements(_ nums: [Int], _ limit: Int, _ goal: Int) -> Int {
        var sum = 0
        for v in nums {
            sum += v
        }
        let diff = goal - sum
        let absDiff = diff >= 0 ? diff : -diff
        return (absDiff + limit - 1) / limit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minElements(nums: IntArray, limit: Int, goal: Int): Int {
        var sum = 0L
        for (v in nums) sum += v.toLong()
        val diff = goal.toLong() - sum
        val absDiff = kotlin.math.abs(diff)
        val ans = (absDiff + limit - 1) / limit
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minElements(List<int> nums, int limit, int goal) {
    int sum = 0;
    for (var v in nums) {
      sum += v;
    }
    int diff = goal - sum;
    int need = diff.abs();
    return (need + limit - 1) ~/ limit;
  }
}
```

## Golang

```go
func minElements(nums []int, limit int, goal int) int {
	var sum int64
	for _, v := range nums {
		sum += int64(v)
	}
	diff := int64(goal) - sum
	if diff < 0 {
		diff = -diff
	}
	l := int64(limit)
	return int((diff + l - 1) / l)
}
```

## Ruby

```ruby
def min_elements(nums, limit, goal)
  diff = goal - nums.sum
  (diff.abs + limit - 1) / limit
end
```

## Scala

```scala
object Solution {
    def minElements(nums: Array[Int], limit: Int, goal: Int): Int = {
        var sum: Long = 0L
        for (v <- nums) sum += v.toLong
        val diff = goal.toLong - sum
        val absDiff = if (diff < 0) -diff else diff
        ((absDiff + limit - 1) / limit).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_elements(nums: Vec<i32>, limit: i32, goal: i32) -> i32 {
        let sum: i64 = nums.iter().map(|&x| x as i64).sum();
        let diff = goal as i64 - sum;
        if diff == 0 {
            return 0;
        }
        let l = limit as i64;
        ((diff.abs() + l - 1) / l) as i32
    }
}
```

## Racket

```racket
(define/contract (min-elements nums limit goal)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((s (foldl + 0 nums))
         (diff (- goal s))
         (abs-diff (if (< diff 0) (- diff) diff)))
    (quotient (+ abs-diff (- limit 1)) limit)))
```

## Erlang

```erlang
-spec min_elements(Nums :: [integer()], Limit :: integer(), Goal :: integer()) -> integer().
min_elements(Nums, Limit, Goal) ->
    Sum = lists:sum(Nums),
    Diff = Goal - Sum,
    AbsDiff = abs(Diff),
    (AbsDiff + Limit - 1) div Limit.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_elements(nums :: [integer], limit :: integer, goal :: integer) :: integer
  def min_elements(nums, limit, goal) do
    diff = goal - Enum.sum(nums)
    abs_diff = Kernel.abs(diff)
    (abs_diff + limit - 1) |> div(limit)
  end
end
```
