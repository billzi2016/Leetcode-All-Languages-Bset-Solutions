# 0055. Jump Game

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int farthest = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i > farthest) return false;
            farthest = max(farthest, i + nums[i]);
            if (farthest >= (int)nums.size() - 1) return true;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canJump(int[] nums) {
        int reach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) return false;
            reach = Math.max(reach, i + nums[i]);
            if (reach >= nums.length - 1) return true;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
            if farthest >= len(nums) - 1:
                return True
        return True
```

## Python3

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
            if farthest >= len(nums) - 1:
                return True
        return True
```

## C

```c
#include <stdbool.h>

bool canJump(int* nums, int numsSize) {
    int farthest = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i > farthest) return false;
        int reach = i + nums[i];
        if (reach > farthest) farthest = reach;
        if (farthest >= numsSize - 1) return true;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanJump(int[] nums)
    {
        int farthest = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (i > farthest)
                return false;
            farthest = Math.Max(farthest, i + nums[i]);
            if (farthest >= nums.Length - 1)
                return true;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let farthest = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > farthest) return false;
        farthest = Math.max(farthest, i + nums[i]);
        if (farthest >= nums.length - 1) return true;
    }
    return true;
};
```

## Typescript

```typescript
function canJump(nums: number[]): boolean {
    let farthest = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > farthest) return false;
        farthest = Math.max(farthest, i + nums[i]);
        if (farthest >= nums.length - 1) return true;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canJump($nums) {
        $maxReach = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i > $maxReach) {
                return false;
            }
            $maxReach = max($maxReach, $i + $nums[$i]);
            if ($maxReach >= $n - 1) {
                return true;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var farthest = 0
        for i in 0..<nums.count {
            if i > farthest { return false }
            farthest = max(farthest, i + nums[i])
            if farthest >= nums.count - 1 { return true }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canJump(nums: IntArray): Boolean {
        var farthest = 0
        for (i in nums.indices) {
            if (i > farthest) return false
            farthest = maxOf(farthest, i + nums[i])
            if (farthest >= nums.lastIndex) return true
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canJump(List<int> nums) {
    int farthest = 0;
    for (int i = 0; i < nums.length; i++) {
      if (i > farthest) return false;
      farthest = farthest > i + nums[i] ? farthest : i + nums[i];
      if (farthest >= nums.length - 1) return true;
    }
    return true;
  }
}
```

## Golang

```go
func canJump(nums []int) bool {
    maxReach := 0
    for i, v := range nums {
        if i > maxReach {
            return false
        }
        if i+v > maxReach {
            maxReach = i + v
        }
        if maxReach >= len(nums)-1 {
            return true
        }
    }
    return true
}
```

## Ruby

```ruby
def can_jump(nums)
  max_reach = 0
  last_index = nums.length - 1
  nums.each_with_index do |jump, i|
    return false if i > max_reach
    max_reach = [max_reach, i + jump].max
    return true if max_reach >= last_index
  end
  false
end
```

## Scala

```scala
object Solution {
    def canJump(nums: Array[Int]): Boolean = {
        var farthest = 0
        for (i <- nums.indices) {
            if (i > farthest) return false
            farthest = math.max(farthest, i + nums(i))
            if (farthest >= nums.length - 1) return true
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut farthest: usize = 0;
        for i in 0..nums.len() {
            if i > farthest {
                return false;
            }
            let jump = nums[i] as usize;
            if i + jump > farthest {
                farthest = i + jump;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-jump nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i 0) (farthest 0))
      (cond [(>= i n) #t]
            [(> i farthest) #false]
            [else
             (define new-farthest (max farthest (+ i (vector-ref v i))))
             (if (>= new-farthest (- n 1))
                 #true
                 (loop (+ i 1) new-farthest))]))))
```

## Erlang

```erlang
-module(solution).
-export([can_jump/1]).

-spec can_jump(Nums :: [integer()]) -> boolean().
can_jump(Nums) ->
    Len = length(Nums),
    can_jump_loop(Nums, 0, 0, Len).

can_jump_loop(_List, _Idx, MaxReach, Len) when MaxReach >= Len - 1 ->
    true;
can_jump_loop([], _Idx, _MaxReach, _Len) ->
    false;
can_jump_loop([H|T], Idx, MaxReach, Len) ->
    case Idx =< MaxReach of
        false -> false;
        true ->
            NewMax = erlang:max(MaxReach, Idx + H),
            can_jump_loop(T, Idx + 1, NewMax, Len)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_jump(nums :: [integer]) :: boolean
  def can_jump(nums) do
    len = length(nums)

    result =
      Enum.reduce_while(0..len - 1, 0, fn i, max_reach ->
        if i > max_reach do
          {:halt, false}
        else
          jump = Enum.at(nums, i)
          new_max = max(max_reach, i + jump)
          {:cont, new_max}
        end
      end)

    result != false
  end
end
```
