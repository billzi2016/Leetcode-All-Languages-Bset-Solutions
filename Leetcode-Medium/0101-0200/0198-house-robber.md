# 0198. House Robber

## Cpp

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        int prev2 = nums[0];
        int prev1 = max(nums[0], nums[1]);
        for (int i = 2; i < n; ++i) {
            int cur = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
};
```

## Java

```java
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int prev2 = 0; // max amount up to house i-2
        int prev1 = 0; // max amount up to house i-1
        for (int num : nums) {
            int cur = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
```

## Python

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
        for n in nums:
            prev, curr = curr, max(curr, prev + n)
        return curr
```

## Python3

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for amount in nums:
            prev, curr = curr, max(curr, prev + amount)
        return curr
```

## C

```c
int rob(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    if (numsSize == 1) return nums[0];
    
    int prev2 = nums[0];
    int prev1 = (nums[0] > nums[1]) ? nums[0] : nums[1];
    
    for (int i = 2; i < numsSize; ++i) {
        int cur = (prev2 + nums[i] > prev1) ? (prev2 + nums[i]) : prev1;
        prev2 = prev1;
        prev1 = cur;
    }
    
    return prev1;
}
```

## Csharp

```csharp
public class Solution
{
    public int Rob(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;

        int prev2 = 0; // max amount up to house i-2
        int prev1 = 0; // max amount up to house i-1

        foreach (int money in nums)
        {
            int cur = Math.Max(prev1, prev2 + money);
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let prevTwo = 0; // max amount up to house i-2
    let prevOne = 0; // max amount up to house i-1
    
    for (let n of nums) {
        const cur = Math.max(prevOne, prevTwo + n);
        prevTwo = prevOne;
        prevOne = cur;
    }
    
    return prevOne;
};
```

## Typescript

```typescript
function rob(nums: number[]): number {
    let prev = 0, curr = 0;
    for (const n of nums) {
        const next = Math.max(curr, prev + n);
        prev = curr;
        curr = next;
    }
    return curr;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function rob($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        if ($n == 1) return $nums[0];

        $prev2 = 0;          // max amount up to house i-2
        $prev1 = $nums[0];   // max amount up to house i-1

        for ($i = 1; $i < $n; $i++) {
            $curr = max($prev1, $prev2 + $nums[$i]);
            $prev2 = $prev1;
            $prev1 = $curr;
        }

        return $prev1;
    }
}
```

## Swift

```swift
class Solution {
    func rob(_ nums: [Int]) -> Int {
        var prev2 = 0
        var prev1 = 0
        for num in nums {
            let current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        }
        return prev1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rob(nums: IntArray): Int {
        var prev1 = 0
        var prev2 = 0
        for (num in nums) {
            val cur = maxOf(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur
        }
        return prev1
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int rob(List<int> nums) {
    int prev1 = 0; // max up to previous house
    int prev2 = 0; // max up to the house before previous
    for (int num in nums) {
      int cur = max(prev1, prev2 + num);
      prev2 = prev1;
      prev1 = cur;
    }
    return prev1;
  }
}
```

## Golang

```go
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	prevTwo, prevOne := 0, 0
	for _, v := range nums {
		cur := prevOne
		if prevTwo+v > cur {
			cur = prevTwo + v
		}
		prevTwo = prevOne
		prevOne = cur
	}
	return prevOne
}
```

## Ruby

```ruby
def rob(nums)
  prev = 0
  curr = 0
  nums.each do |n|
    new_curr = [curr, prev + n].max
    prev = curr
    curr = new_curr
  end
  curr
end
```

## Scala

```scala
object Solution {
    def rob(nums: Array[Int]): Int = {
        var prev2 = 0
        var prev1 = 0
        for (n <- nums) {
            val cur = Math.max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = cur
        }
        prev1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut prev1 = 0;
        let mut prev2 = 0;
        for &num in nums.iter() {
            let cur = std::cmp::max(prev1 + num, prev2);
            prev2 = prev1;
            prev1 = cur;
        }
        prev1
    }
}
```

## Racket

```racket
(define/contract (rob nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (prev1 0) (prev2 0))
    (if (null? lst)
        prev1
        (let* ((current (car lst))
               (new-prev (max (+ current prev2) prev1)))
          (loop (cdr lst) new-prev prev1)))))
```

## Erlang

```erlang
-module(solution).
-export([rob/1]).

-spec rob(Nums :: [integer()]) -> integer().
rob([]) -> 0;
rob(Nums) ->
    rob_loop(Nums, 0, 0).

rob_loop([], Prev1, _Prev2) -> Prev1;
rob_loop([X|Rest], Prev1, Prev2) ->
    Curr = erlang:max(Prev1, Prev2 + X),
    rob_loop(Rest, Curr, Prev1).
```

## Elixir

```elixir
defmodule Solution do
  @spec rob(nums :: [integer]) :: integer
  def rob(nums) do
    {max_rob, _} =
      Enum.reduce(nums, {0, 0}, fn x, {prev, prev2} ->
        cur = max(prev, prev2 + x)
        {cur, prev}
      end)

    max_rob
  end
end
```
