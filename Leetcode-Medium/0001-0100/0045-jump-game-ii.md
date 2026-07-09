# 0045. Jump Game II

## Cpp

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int jumps = 0, curEnd = 0, farthest = 0;
        for (int i = 0; i < n - 1; ++i) {
            farthest = max(farthest, i + nums[i]);
            if (i == curEnd) {
                ++jumps;
                curEnd = farthest;
            }
        }
        return jumps;
    }
};
```

## Java

```java
class Solution {
    public int jump(int[] nums) {
        if (nums.length <= 1) return 0;
        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }
        return jumps;
    }
}
```

## Python

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        return jumps
```

## Python3

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
```

## C

```c
int jump(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    int jumps = 0;
    int curEnd = 0;
    int farthest = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        if (i + nums[i] > farthest) farthest = i + nums[i];
        if (i == curEnd) {
            ++jumps;
            curEnd = farthest;
        }
    }
    return jumps;
}
```

## Csharp

```csharp
public class Solution
{
    public int Jump(int[] nums)
    {
        int n = nums.Length;
        if (n <= 1) return 0;

        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;

        for (int i = 0; i < n - 1; i++)
        {
            farthest = Math.Max(farthest, i + nums[i]);
            if (i == currentEnd)
            {
                jumps++;
                currentEnd = farthest;
            }
        }

        return jumps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    const n = nums.length;
    if (n <= 1) return 0;
    let jumps = 0;
    let curEnd = 0;
    let farthest = 0;
    for (let i = 0; i < n - 1; i++) {
        farthest = Math.max(farthest, i + nums[i]);
        if (i === curEnd) {
            jumps++;
            curEnd = farthest;
        }
    }
    return jumps;
};
```

## Typescript

```typescript
function jump(nums: number[]): number {
    const n = nums.length;
    if (n <= 1) return 0;

    let jumps = 0;
    let currentEnd = 0;
    let farthest = 0;

    for (let i = 0; i < n - 1; i++) {
        farthest = Math.max(farthest, i + nums[i]);
        if (i === currentEnd) {
            jumps++;
            currentEnd = farthest;
        }
    }

    return jumps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function jump($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return 0;
        }
        $jumps = 0;
        $currentEnd = 0;
        $farthest = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $farthest = max($farthest, $i + $nums[$i]);
            if ($i == $currentEnd) {
                $jumps++;
                $currentEnd = $farthest;
                if ($currentEnd >= $n - 1) {
                    break;
                }
            }
        }
        return $jumps;
    }
}
```

## Swift

```swift
class Solution {
    func jump(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return 0 }
        var jumps = 0
        var currentEnd = 0
        var farthest = 0
        
        for i in 0..<(n - 1) {
            farthest = max(farthest, i + nums[i])
            if i == currentEnd {
                jumps += 1
                currentEnd = farthest
                if currentEnd >= n - 1 { break }
            }
        }
        return jumps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun jump(nums: IntArray): Int {
        val n = nums.size
        if (n <= 1) return 0
        var jumps = 0
        var currentEnd = 0
        var farthest = 0
        for (i in 0 until n - 1) {
            farthest = maxOf(farthest, i + nums[i])
            if (i == currentEnd) {
                jumps++
                currentEnd = farthest
                if (currentEnd >= n - 1) break
            }
        }
        return jumps
    }
}
```

## Dart

```dart
class Solution {
  int jump(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return 0;
    int jumps = 0;
    int currentEnd = 0;
    int farthest = 0;
    for (int i = 0; i < n - 1; i++) {
      farthest = farthest > i + nums[i] ? farthest : i + nums[i];
      if (i == currentEnd) {
        jumps++;
        currentEnd = farthest;
      }
    }
    return jumps;
  }
}
```

## Golang

```go
func jump(nums []int) int {
    n := len(nums)
    if n <= 1 {
        return 0
    }
    steps, currentEnd, farthest := 0, 0, 0
    for i := 0; i < n-1; i++ {
        if i+nums[i] > farthest {
            farthest = i + nums[i]
        }
        if i == currentEnd {
            steps++
            currentEnd = farthest
        }
    }
    return steps
}
```

## Ruby

```ruby
def jump(nums)
  n = nums.length
  return 0 if n <= 1
  jumps = 0
  current_end = 0
  farthest = 0
  (0...n-1).each do |i|
    farthest = [farthest, i + nums[i]].max
    if i == current_end
      jumps += 1
      current_end = farthest
    end
  end
  jumps
end
```

## Scala

```scala
object Solution {
    def jump(nums: Array[Int]): Int = {
        val n = nums.length
        if (n <= 1) return 0
        var jumps = 0
        var currentEnd = 0
        var farthest = 0
        for (i <- 0 until n - 1) {
            farthest = math.max(farthest, i + nums(i))
            if (i == currentEnd) {
                jumps += 1
                currentEnd = farthest
            }
        }
        jumps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        let mut jumps = 0;
        let mut current_end = 0usize;
        let mut farthest = 0usize;

        for i in 0..n - 1 {
            farthest = farthest.max(i + nums[i] as usize);
            if i == current_end {
                jumps += 1;
                current_end = farthest;
                if current_end >= n - 1 {
                    break;
                }
            }
        }

        jumps as i32
    }
}
```

## Racket

```racket
(define/contract (jump nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums)))
    (if (= n 1)
        0
        (let ((jumps 0)
              (current-end 0)
              (farthest 0))
          (for ([i (in-range (- n 1))])
            (set! farthest (max farthest (+ i (vector-ref v i))))
            (when (= i current-end)
              (set! jumps (+ jumps 1))
              (set! current-end farthest)))
          jumps))))
```

## Erlang

```erlang
-spec jump(Nums :: [integer()]) -> integer().
jump(Nums) ->
    case Nums of
        [_] -> 0;
        _ ->
            Len = length(Nums),
            loop(Nums, 0, 0, 0, 0, Len)
    end.

loop(_List, Index, _CurrentEnd, _Farthest, Jumps, Len) when Index >= Len - 1 ->
    Jumps;
loop([V|Rest], Index, CurrentEnd, Farthest, Jumps, Len) ->
    NewFarthest = erlang:max(Farthest, Index + V),
    if
        Index == CurrentEnd ->
            loop(Rest, Index + 1, NewFarthest, NewFarthest, Jumps + 1, Len);
        true ->
            loop(Rest, Index + 1, CurrentEnd, NewFarthest, Jumps, Len)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec jump(nums :: [integer]) :: integer
  def jump(nums) do
    n = length(nums)

    if n <= 1 do
      0
    else
      tup = List.to_tuple(nums)
      helper(tup, 0, n, 0, 0, 0)
    end
  end

  defp helper(_tup, idx, n, jumps, _cur_end, _far) when idx >= n - 1 do
    jumps
  end

  defp helper(tup, idx, n, jumps, cur_end, farthest) do
    val = elem(tup, idx)
    new_farthest = max(farthest, idx + val)

    if idx == cur_end do
      helper(tup, idx + 1, n, jumps + 1, new_farthest, new_farthest)
    else
      helper(tup, idx + 1, n, jumps, cur_end, new_farthest)
    end
  end
end
```
