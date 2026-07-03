# 0136. Single Number

## Cpp

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int singleNumber(int[] nums) {
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
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
```

## Python3

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

## C

```c
int singleNumber(int* nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize; ++i) {
        res ^= nums[i];
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        int result = 0;
        foreach (int num in nums) {
            result ^= num;
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
var singleNumber = function(nums) {
    let result = 0;
    for (const num of nums) {
        result ^= num;
    }
    return result;
};
```

## Typescript

```typescript
function singleNumber(nums: number[]): number {
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
    function singleNumber($nums) {
        $result = 0;
        foreach ($nums as $num) {
            $result ^= $num;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var ans = 0
        for num in nums {
            ans ^= num
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun singleNumber(nums: IntArray): Int {
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
  int singleNumber(List<int> nums) {
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
func singleNumber(nums []int) int {
    result := 0
    for _, num := range nums {
        result ^= num
    }
    return result
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  result = 0
  nums.each { |num| result ^= num }
  result
end
```

## Scala

```scala
object Solution {
    def singleNumber(nums: Array[Int]): Int = {
        var result = 0
        for (num <- nums) {
            result ^= num
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for num in nums {
            result ^= num;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (single-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (foldl bitwise-xor 0 nums))
```

## Erlang

```erlang
-module(solution).
-export([single_number/1]).

-spec single_number(Nums :: [integer()]) -> integer().
single_number(Nums) ->
    lists:foldl(fun (X, Acc) -> X bxor Acc end, 0, Nums).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec single_number(nums :: [integer]) :: integer
  def single_number(nums) do
    Enum.reduce(nums, 0, fn x, acc -> bxor(acc, x) end)
  end
end
```
