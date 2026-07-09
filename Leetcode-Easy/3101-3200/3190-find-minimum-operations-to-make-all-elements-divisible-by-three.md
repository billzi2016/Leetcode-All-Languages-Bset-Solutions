# 3190. Find Minimum Operations to Make All Elements Divisible by Three

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int ans = 0;
        for (int x : nums) {
            int r = x % 3;
            if (r != 0) ans += min(r, 3 - r);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        int ops = 0;
        for (int num : nums) {
            int r = num % 3;
            if (r != 0) {
                ops += Math.min(r, 3 - r);
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for x in nums:
            r = x % 3
            if r:
                ops += min(r, 3 - r)
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(x % 3, 3 - (x % 3)) for x in nums)
```

## C

```c
int minimumOperations(int* nums, int numsSize) {
    int ops = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % 3 != 0) {
            ops += 1;
        }
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumOperations(int[] nums)
    {
        int operations = 0;
        foreach (int num in nums)
        {
            int rem = num % 3;
            if (rem != 0)
                operations += Math.Min(rem, 3 - rem);
        }
        return operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    let ops = 0;
    for (const num of nums) {
        const r = num % 3;
        if (r !== 0) {
            ops += Math.min(r, 3 - r);
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[]): number {
    let operations = 0;
    for (const num of nums) {
        const rem = num % 3;
        if (rem !== 0) {
            operations += Math.min(rem, 3 - rem);
        }
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $operations = 0;
        foreach ($nums as $num) {
            if ($num % 3 !== 0) {
                $operations++;
            }
        }
        return $operations;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var operations = 0
        for num in nums {
            if num % 3 != 0 {
                operations += 1
            }
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var ops = 0
        for (num in nums) {
            if (num % 3 != 0) ops++
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    int operations = 0;
    for (int num in nums) {
      if (num % 3 != 0) {
        operations += 1;
      }
    }
    return operations;
  }
}
```

## Golang

```go
func minimumOperations(nums []int) int {
    ops := 0
    for _, v := range nums {
        r := v % 3
        if r != 0 {
            if r < 3-r {
                ops += r
            } else {
                ops += 3 - r
            }
        }
    }
    return ops
}
```

## Ruby

```ruby
def minimum_operations(nums)
  nums.sum do |x|
    r = x % 3
    r == 0 ? 0 : [r, 3 - r].min
  end
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        nums.count(_ % 3 != 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.iter().filter(|&&x| x % 3 != 0).count() as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (apply + 
         (map (lambda (x)
                (let ([r (modulo x 3)])
                  (if (= r 0) 
                      0
                      (min r (- 3 r)))))
              nums)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    lists:foldl(fun(N, Acc) ->
        case N rem 3 of
            0 -> Acc;
            _ -> Acc + 1
        end
    end, 0, Nums).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.reduce(nums, 0, fn x, acc ->
      r = rem(x, 3)
      acc + min(r, 3 - r)
    end)
  end
end
```
