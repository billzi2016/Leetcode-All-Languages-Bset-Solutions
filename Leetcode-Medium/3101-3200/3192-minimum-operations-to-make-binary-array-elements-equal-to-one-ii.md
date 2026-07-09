# 3192. Minimum Operations to Make Binary Array Elements Equal to One II

## Cpp

```cpp
class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int ops = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int cur = nums[i];
            if (ops % 2 == 1) cur ^= 1; // apply parity of previous suffix flips
            if (cur == 0) {
                ++ops; // flip suffix starting at i
            }
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        int operations = 0;
        int flipParity = 0; // 0 means even number of flips applied so far, 1 means odd
        for (int num : nums) {
            int current = num ^ flipParity;
            if (current == 0) {
                operations++;
                flipParity ^= 1; // toggle parity for the suffix
            }
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flips = 0  # parity of performed suffix flips (0 for even, 1 for odd)
        ops = 0
        for num in nums:
            current = num ^ flips
            if current == 0:
                ops += 1
                flips ^= 1  # toggle parity for future positions
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        ops = 0
        for v in nums:
            if (v ^ flips) == 0:
                ops += 1
                flips ^= 1
        return ops
```

## C

```c
int minOperations(int* nums, int numsSize) {
    int ops = 0;
    for (int i = 0; i < numsSize; ++i) {
        int cur = nums[i];
        if (ops & 1) cur ^= 1; // apply parity of previous flips
        if (cur == 0) {
            ++ops; // flip suffix starting at i
        }
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        int operations = 0;
        int flipParity = 0; // 0 means even number of flips applied so far, 1 means odd
        foreach (int num in nums) {
            if ((num ^ flipParity) == 0) { // current effective value is 0
                operations++;
                flipParity ^= 1; // toggle parity for the suffix
            }
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
var minOperations = function(nums) {
    let ops = 0;
    let flip = 0; // parity of suffix flips applied so far
    for (let i = 0; i < nums.length; i++) {
        if ((nums[i] ^ flip) === 0) { // current value is 0, need an operation here
            ops++;
            flip ^= 1; // future elements will be flipped once more
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    let ops = 0;
    for (let i = 0; i < nums.length; i++) {
        const cur = nums[i] ^ (ops & 1);
        if (cur === 0) {
            ops++;
        }
    }
    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $parity = 0; // number of suffix flips performed modulo 2
        $ops = 0;
        foreach ($nums as $v) {
            $current = $v ^ $parity;
            if ($current == 0) { // need to flip at this index
                $ops++;
                $parity ^= 1; // toggle parity for the remaining suffix
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var operations = 0
        var flipParity = 0
        for num in nums {
            let current = num ^ flipParity
            if current == 0 {
                operations += 1
                flipParity ^= 1
            }
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        var ops = 0
        for (value in nums) {
            val effective = value xor (ops and 1)
            if (effective == 0) {
                ops++
            }
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int flips = 0;
    int operations = 0;
    for (int i = 0; i < nums.length; i++) {
      int current = nums[i];
      if ((flips & 1) == 1) {
        current ^= 1;
      }
      if (current == 0) {
        operations++;
        flips++;
      }
    }
    return operations;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    ops, flip := 0, 0
    for _, v := range nums {
        if v^flip == 0 {
            ops++
            flip ^= 1
        }
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  ops = 0
  flip = 0
  nums.each do |v|
    cur = v ^ flip
    if cur == 0
      ops += 1
      flip ^= 1
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var ops = 0
        var flip = 0 // parity of performed suffix flips
        for (v <- nums) {
            val cur = v ^ flip
            if (cur == 0) {
                ops += 1
                flip ^= 1
            }
        }
        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut ops: i32 = 0;
        for &v in nums.iter() {
            // effective value after current suffix flips
            if v ^ (ops & 1) == 0 {
                ops += 1;
            }
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (ops 0) (parity 0))
    (if (null? lst)
        ops
        (let* ((x (car lst))
               (cur (bitwise-xor x parity)))
          (if (= cur 0)
              (loop (cdr lst) (+ ops 1) (bitwise-xor parity 1))
              (loop (cdr lst) ops parity))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    {_, Ans} = lists:foldl(
        fun(N, {Flip, Count}) ->
            case (N bxor Flip) of
                0 -> {1 - Flip, Count + 1};
                _ -> {Flip, Count}
            end
        end,
        {0, 0},
        Nums),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    {ans, _flip} =
      Enum.reduce(nums, {0, 0}, fn num, {cnt, flip} ->
        effective = bxor(num, flip)

        if effective == 0 do
          {cnt + 1, bxor(flip, 1)}
        else
          {cnt, flip}
        end
      end)

    ans
  end
end
```
