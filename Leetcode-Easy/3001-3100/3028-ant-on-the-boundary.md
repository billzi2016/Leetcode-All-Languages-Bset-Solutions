# 3028. Ant on the Boundary

## Cpp

```cpp
class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int pos = 0;
        int cnt = 0;
        for (int x : nums) {
            pos += x;
            if (pos == 0) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int position = 0;
        int count = 0;
        for (int num : nums) {
            position += num;
            if (position == 0) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        cnt = 0
        for v in nums:
            pos += v
            if pos == 0:
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        count = 0
        for v in nums:
            pos += v
            if pos == 0:
                count += 1
        return count
```

## C

```c
int returnToBoundaryCount(int* nums, int numsSize) {
    int position = 0;
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        position += nums[i];
        if (position == 0) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int ReturnToBoundaryCount(int[] nums) {
        int count = 0;
        int sum = 0;
        foreach (int x in nums) {
            sum += x;
            if (sum == 0) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let pos = 0;
    let count = 0;
    for (let v of nums) {
        pos += v;
        if (pos === 0) count++;
    }
    return count;
};
```

## Typescript

```typescript
function returnToBoundaryCount(nums: number[]): number {
    let position = 0;
    let count = 0;
    for (const step of nums) {
        position += step;
        if (position === 0) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function returnToBoundaryCount($nums) {
        $position = 0;
        $count = 0;
        foreach ($nums as $num) {
            $position += $num;
            if ($position == 0) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func returnToBoundaryCount(_ nums: [Int]) -> Int {
        var sum = 0
        var count = 0
        for num in nums {
            sum += num
            if sum == 0 {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun returnToBoundaryCount(nums: IntArray): Int {
        var position = 0
        var count = 0
        for (value in nums) {
            position += value
            if (position == 0) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int returnToBoundaryCount(List<int> nums) {
    int pos = 0;
    int count = 0;
    for (int step in nums) {
      pos += step;
      if (pos == 0) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func returnToBoundaryCount(nums []int) int {
    count := 0
    pos := 0
    for _, v := range nums {
        pos += v
        if pos == 0 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def return_to_boundary_count(nums)
  position = 0
  count = 0
  nums.each do |v|
    position += v
    count += 1 if position == 0
  end
  count
end
```

## Scala

```scala
object Solution {
    def returnToBoundaryCount(nums: Array[Int]): Int = {
        var position = 0
        var result = 0
        for (v <- nums) {
            position += v
            if (position == 0) result += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn return_to_boundary_count(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        let mut count = 0;
        for v in nums {
            sum += v;
            if sum == 0 {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (return-to-boundary-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (sum 0) (cnt 0))
    (if (null? lst)
        cnt
        (let* ((new-sum (+ sum (car lst)))
               (new-cnt (if (= new-sum 0) (+ cnt 1) cnt)))
          (loop (cdr lst) new-sum new-cnt)))))
```

## Erlang

```erlang
-spec return_to_boundary_count(Nums :: [integer()]) -> integer().
return_to_boundary_count(Nums) ->
    {_, Count} = lists:foldl(
        fun(X, {Sum, Cnt}) ->
            NewSum = Sum + X,
            NewCnt = case NewSum of
                0 -> Cnt + 1;
                _ -> Cnt
            end,
            {NewSum, NewCnt}
        end,
        {0, 0},
        Nums),
    Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec return_to_boundary_count(nums :: [integer]) :: integer
  def return_to_boundary_count(nums) do
    {count, _} = Enum.reduce(nums, {0, 0}, fn x, {cnt, sum} ->
      new_sum = sum + x
      if new_sum == 0, do: {cnt + 1, new_sum}, else: {cnt, new_sum}
    end)
    count
  end
end
```
