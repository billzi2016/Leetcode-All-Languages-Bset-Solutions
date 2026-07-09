# 2239. Find Closest Number to Zero

## Cpp

```cpp
class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int best = nums[0];
        for (int x : nums) {
            int ax = std::abs(x);
            int abest = std::abs(best);
            if (ax < abest || (ax == abest && x > best)) {
                best = x;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int findClosestNumber(int[] nums) {
        int best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int cur = nums[i];
            int absCur = Math.abs(cur);
            int absBest = Math.abs(best);
            if (absCur < absBest || (absCur == absBest && cur > best)) {
                best = cur;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = None
        for x in nums:
            if best is None or abs(x) < abs(best) or (abs(x) == abs(best) and x > best):
                best = x
        return best
```

## Python3

```python
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        best = None
        for x in nums:
            if best is None or abs(x) < abs(best) or (abs(x) == abs(best) and x > best):
                best = x
        return best
```

## C

```c
int findClosestNumber(int* nums, int numsSize) {
    int best = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        int cur = nums[i];
        int absCur = cur >= 0 ? cur : -cur;
        int absBest = best >= 0 ? best : -best;
        if (absCur < absBest || (absCur == absBest && cur > best)) {
            best = cur;
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int FindClosestNumber(int[] nums) {
        int best = nums[0];
        foreach (int num in nums) {
            int absNum = Math.Abs(num);
            int absBest = Math.Abs(best);
            if (absNum < absBest || (absNum == absBest && num > best)) {
                best = num;
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let closest = nums[0];
    for (let i = 1; i < nums.length; i++) {
        const cur = nums[i];
        const absCur = Math.abs(cur);
        const absClose = Math.abs(closest);
        if (absCur < absClose || (absCur === absClose && cur > closest)) {
            closest = cur;
        }
    }
    return closest;
};
```

## Typescript

```typescript
function findClosestNumber(nums: number[]): number {
    let closest = nums[0];
    for (let i = 1; i < nums.length; i++) {
        const val = nums[i];
        const absVal = Math.abs(val);
        const absClose = Math.abs(closest);
        if (absVal < absClose || (absVal === absClose && val > closest)) {
            closest = val;
        }
    }
    return closest;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findClosestNumber($nums) {
        $best = null;
        foreach ($nums as $num) {
            if ($best === null) {
                $best = $num;
                continue;
            }
            $absNum = abs($num);
            $absBest = abs($best);
            if ($absNum < $absBest || ($absNum == $absBest && $num > $best)) {
                $best = $num;
            }
        }
        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func findClosestNumber(_ nums: [Int]) -> Int {
        var closest = nums[0]
        for num in nums {
            let absNum = abs(num)
            let absClosest = abs(closest)
            if absNum < absClosest || (absNum == absClosest && num > closest) {
                closest = num
            }
        }
        return closest
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findClosestNumber(nums: IntArray): Int {
        var answer = nums[0]
        for (i in 1 until nums.size) {
            val cur = nums[i]
            val absCur = kotlin.math.abs(cur)
            val absAns = kotlin.math.abs(answer)
            if (absCur < absAns || (absCur == absAns && cur > answer)) {
                answer = cur
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int findClosestNumber(List<int> nums) {
    int best = nums[0];
    for (int i = 1; i < nums.length; i++) {
      int cur = nums[i];
      int absCur = cur.abs();
      int absBest = best.abs();
      if (absCur < absBest || (absCur == absBest && cur > best)) {
        best = cur;
      }
    }
    return best;
  }
}
```

## Golang

```go
func findClosestNumber(nums []int) int {
    ans := nums[0]
    for _, x := range nums {
        ax := x
        if ax < 0 {
            ax = -ax
        }
        aans := ans
        if aans < 0 {
            aans = -aans
        }
        if ax < aans || (ax == aans && x > ans) {
            ans = x
        }
    }
    return ans
}
```

## Ruby

```ruby
def find_closest_number(nums)
  best = nums[0]
  nums.each do |num|
    if num.abs < best.abs || (num.abs == best.abs && num > best)
      best = num
    end
  end
  best
end
```

## Scala

```scala
object Solution {
    def findClosestNumber(nums: Array[Int]): Int = {
        var best = nums(0)
        for (num <- nums) {
            val absNum = math.abs(num)
            val absBest = math.abs(best)
            if (absNum < absBest || (absNum == absBest && num > best)) {
                best = num
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        let mut best = nums[0];
        for &x in nums.iter().skip(1) {
            let ax = x.abs();
            let abest = best.abs();
            if ax < abest || (ax == abest && x > best) {
                best = x;
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (find-closest-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (foldl
   (lambda (x best)
     (let ((ax (abs x))
           (ab (abs best)))
       (cond [(< ax ab) x]
             [(= ax ab) (max x best)]
             [else best])))
   (car nums)
   (cdr nums)))
```

## Erlang

```erlang
-spec find_closest_number(Nums :: [integer()]) -> integer().
find_closest_number([H|T]) ->
    lists:foldl(
        fun(Cand, Best) ->
            AbsCand = erlang:abs(Cand),
            AbsBest = erlang:abs(Best),
            if
                AbsCand < AbsBest -> Cand;
                AbsCand > AbsBest -> Best;
                true -> erlang:max(Cand, Best)
            end
        end,
        H,
        T
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_closest_number(nums :: [integer]) :: integer
  def find_closest_number([head | tail]) do
    Enum.reduce(tail, head, fn x, best ->
      cond do
        abs(x) < abs(best) -> x
        abs(x) == abs(best) and x > best -> x
        true -> best
      end
    end)
  end
end
```
