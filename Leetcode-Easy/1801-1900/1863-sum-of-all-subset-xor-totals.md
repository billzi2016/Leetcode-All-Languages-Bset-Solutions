# 1863. Sum of All Subset XOR Totals

## Cpp

```cpp
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        if (nums.empty()) return 0;
        int orAll = 0;
        for (int x : nums) orAll |= x;
        return orAll << (static_cast<int>(nums.size()) - 1);
    }
};
```

## Java

```java
class Solution {
    public int subsetXORSum(int[] nums) {
        int orAll = 0;
        for (int num : nums) {
            orAll |= num;
        }
        return orAll << (nums.length - 1);
    }
}
```

## Python

```python
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        or_all = 0
        for num in nums:
            or_all |= num
        return or_all << (len(nums) - 1)
```

## Python3

```python
class Solution:
    def subsetXORSum(self, nums):
        or_all = 0
        for num in nums:
            or_all |= num
        return or_all << (len(nums) - 1)
```

## C

```c
int subsetXORSum(int* nums, int numsSize) {
    int orAll = 0;
    for (int i = 0; i < numsSize; ++i) {
        orAll |= nums[i];
    }
    return orAll << (numsSize - 1);
}
```

## Csharp

```csharp
public class Solution {
    public int SubsetXORSum(int[] nums) {
        int combinedOr = 0;
        foreach (int num in nums) {
            combinedOr |= num;
        }
        return combinedOr << (nums.Length - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums) {
    let or = 0;
    for (const num of nums) {
        or |= num;
    }
    return or << (nums.length - 1);
};
```

## Typescript

```typescript
function subsetXORSum(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    let orAll = 0;
    for (const num of nums) {
        orAll |= num;
    }
    return orAll << (n - 1);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subsetXORSum($nums) {
        $n = count($nums);
        $or = 0;
        foreach ($nums as $num) {
            $or |= $num;
        }
        return $or << ($n - 1);
    }
}
```

## Swift

```swift
class Solution {
    func subsetXORSum(_ nums: [Int]) -> Int {
        var orResult = 0
        for num in nums {
            orResult |= num
        }
        let shift = nums.count - 1
        return orResult << shift
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subsetXORSum(nums: IntArray): Int {
        var orAll = 0
        for (num in nums) {
            orAll = orAll or num
        }
        return orAll shl (nums.size - 1)
    }
}
```

## Dart

```dart
class Solution {
  int subsetXORSum(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;
    int orAll = 0;
    for (int num in nums) {
      orAll |= num;
    }
    return orAll << (n - 1);
  }
}
```

## Golang

```go
func subsetXORSum(nums []int) int {
    orVal := 0
    for _, num := range nums {
        orVal |= num
    }
    return orVal << (len(nums) - 1)
}
```

## Ruby

```ruby
def subset_xor_sum(nums)
  or_val = 0
  nums.each { |num| or_val |= num }
  or_val << (nums.length - 1)
end
```

## Scala

```scala
object Solution {
    def subsetXORSum(nums: Array[Int]): Int = {
        var orVal = 0
        for (num <- nums) {
            orVal |= num
        }
        if (nums.isEmpty) 0 else orVal << (nums.length - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let mut or_val = 0;
        for &num in nums.iter() {
            or_val |= num;
        }
        let shift = (nums.len() - 1) as u32;
        or_val << shift
    }
}
```

## Racket

```racket
(define/contract (subset-xor-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (or-val (foldl bitwise-ior 0 nums))
         (shift (- n 1)))
    (if (positive? shift)
        (arithmetic-shift or-val shift)
        or-val)))
```

## Erlang

```erlang
-module(solution).
-export([subset_xor_sum/1]).

-spec subset_xor_sum(Nums :: [integer()]) -> integer().
subset_xor_sum(Nums) ->
    Len = length(Nums),
    OrVal = lists:foldl(fun(N, Acc) -> N bor Acc end, 0, Nums),
    Shift = case Len of
                0 -> 0;
                _ -> Len - 1
            end,
    OrVal bsl Shift.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec subset_xor_sum(nums :: [integer]) :: integer
  def subset_xor_sum(nums) do
    or = Enum.reduce(nums, 0, fn x, acc -> bor(acc, x) end)
    shift = length(nums) - 1
    shift_left(or, shift)
  end
end
```
