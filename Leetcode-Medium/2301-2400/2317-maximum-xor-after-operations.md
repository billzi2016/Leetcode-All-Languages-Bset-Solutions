# 2317. Maximum XOR After Operations

## Cpp

```cpp
class Solution {
public:
    int maximumXOR(vector<int>& nums) {
        int ans = 0;
        for (int v : nums) ans |= v;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumXOR(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result |= num;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result |= num
        return result
```

## Python3

```python
from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res
```

## C

```c
int maximumXOR(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        ans |= nums[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumXOR(int[] nums)
    {
        int result = 0;
        foreach (int num in nums)
        {
            result |= num;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumXOR = function(nums) {
    let result = 0;
    for (const num of nums) {
        result |= num;
    }
    return result;
};
```

## Typescript

```typescript
function maximumXOR(nums: number[]): number {
    let result = 0;
    for (const num of nums) {
        result |= num;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumXOR($nums) {
        $result = 0;
        foreach ($nums as $num) {
            $result |= $num;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maximumXOR(_ nums: [Int]) -> Int {
        var result = 0
        for num in nums {
            result |= num
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumXOR(nums: IntArray): Int {
        var result = 0
        for (num in nums) {
            result = result or num
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int maximumXOR(List<int> nums) {
    int result = 0;
    for (int num in nums) {
      result |= num;
    }
    return result;
  }
}
```

## Golang

```go
func maximumXOR(nums []int) int {
    res := 0
    for _, v := range nums {
        res |= v
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_xor(nums)
  result = 0
  nums.each { |num| result |= num }
  result
end
```

## Scala

```scala
object Solution {
    def maximumXOR(nums: Array[Int]): Int = {
        var result = 0
        for (num <- nums) {
            result |= num
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        for v in nums {
            res |= v;
        }
        res
    }
}
```

## Racket

```racket
#lang racket
(require racket/bitwise)

(define/contract (maximum-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  (foldl bitwise-ior 0 nums))
```

## Erlang

```erlang
-module(solution).
-export([maximum_xor/1]).

-spec maximum_xor(Nums :: [integer()]) -> integer().
maximum_xor(Nums) ->
    lists:foldl(fun (X, Acc) -> X bor Acc end, 0, Nums).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_xor(nums :: [integer]) :: integer
  def maximum_xor(nums) do
    Enum.reduce(nums, 0, fn x, acc -> Bitwise.bor(acc, x) end)
  end
end
```
