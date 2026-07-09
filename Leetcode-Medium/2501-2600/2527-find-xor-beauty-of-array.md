# 2527. Find Xor-Beauty of Array

## Cpp

```cpp
class Solution {
public:
    int xorBeauty(vector<int>& nums) {
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int xorBeauty(int[] nums) {
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
```

## Python3

```python
from typing import List

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for v in nums:
            ans ^= v
        return ans
```

## C

```c
int xorBeauty(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        ans ^= nums[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int XorBeauty(int[] nums)
    {
        int result = 0;
        foreach (int num in nums)
            result ^= num;
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
var xorBeauty = function(nums) {
    let ans = 0;
    for (const v of nums) {
        ans ^= v;
    }
    return ans;
};
```

## Typescript

```typescript
function xorBeauty(nums: number[]): number {
    let result = 0;
    for (const num of nums) {
        result ^= num;
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
    function xorBeauty($nums) {
        $ans = 0;
        foreach ($nums as $v) {
            $ans ^= $v;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func xorBeauty(_ nums: [Int]) -> Int {
        var result = 0
        for num in nums {
            result ^= num
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun xorBeauty(nums: IntArray): Int {
        var result = 0
        for (num in nums) {
            result = result xor num
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int xorBeauty(List<int> nums) {
    int result = 0;
    for (var num in nums) {
      result ^= num;
    }
    return result;
  }
}
```

## Golang

```go
func xorBeauty(nums []int) int {
    ans := 0
    for _, v := range nums {
        ans ^= v
    }
    return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def xor_beauty(nums)
  ans = 0
  nums.each { |x| ans ^= x }
  ans
end
```

## Scala

```scala
object Solution {
    def xorBeauty(nums: Array[Int]): Int = {
        var res = 0
        for (x <- nums) {
            res ^= x
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn xor_beauty(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for v in nums {
            ans ^= v;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (xor-beauty nums)
  (-> (listof exact-integer?) exact-integer?)
  (foldl bitwise-xor 0 nums))
```

## Erlang

```erlang
-spec xor_beauty([integer()]) -> integer().
xor_beauty(Nums) ->
    lists:foldl(fun(X, Acc) -> X bxor Acc end, 0, Nums).
```

## Elixir

```elixir
defmodule Solution do
  @spec xor_beauty(nums :: [integer]) :: integer
  def xor_beauty(nums) do
    Enum.reduce(nums, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
  end
end
```
