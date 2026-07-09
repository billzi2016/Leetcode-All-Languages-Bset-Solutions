# 1822. Sign of the Product of an Array

## Cpp

```cpp
class Solution {
public:
    int arraySign(vector<int>& nums) {
        int sign = 1;
        for (int num : nums) {
            if (num == 0) return 0;
            if (num < 0) sign = -sign;
        }
        return sign;
    }
};
```

## Java

```java
class Solution {
    public int arraySign(int[] nums) {
        int sign = 1;
        for (int num : nums) {
            if (num == 0) {
                return 0;
            }
            if (num < 0) {
                sign = -sign;
            }
        }
        return sign;
    }
}
```

## Python

```python
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_count ^= 1  # toggle between 0 and 1
        return -1 if neg_count else 1
```

## Python3

```python
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_count += 1
        return -1 if neg_count % 2 else 1
```

## C

```c
int arraySign(int* nums, int numsSize) {
    int sign = 1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) return 0;
        if (nums[i] < 0) sign = -sign;
    }
    return sign;
}
```

## Csharp

```csharp
public class Solution
{
    public int ArraySign(int[] nums)
    {
        int sign = 1;
        foreach (int num in nums)
        {
            if (num == 0) return 0;
            if (num < 0) sign = -sign;
        }
        return sign;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let sign = 1;
    for (const num of nums) {
        if (num === 0) return 0;
        if (num < 0) sign = -sign;
    }
    return sign;
};
```

## Typescript

```typescript
function arraySign(nums: number[]): number {
    let sign = 1;
    for (const num of nums) {
        if (num === 0) return 0;
        if (num < 0) sign = -sign;
    }
    return sign;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arraySign($nums) {
        $negCount = 0;
        foreach ($nums as $num) {
            if ($num == 0) {
                return 0;
            }
            if ($num < 0) {
                $negCount++;
            }
        }
        return ($negCount % 2 === 0) ? 1 : -1;
    }
}
```

## Swift

```swift
class Solution {
    func arraySign(_ nums: [Int]) -> Int {
        var sign = 1
        for num in nums {
            if num == 0 { return 0 }
            if num < 0 { sign = -sign }
        }
        return sign
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arraySign(nums: IntArray): Int {
        var sign = 1
        for (num in nums) {
            if (num == 0) return 0
            if (num < 0) sign = -sign
        }
        return sign
    }
}
```

## Dart

```dart
class Solution {
  int arraySign(List<int> nums) {
    int sign = 1;
    for (int num in nums) {
      if (num == 0) return 0;
      if (num < 0) sign = -sign;
    }
    return sign;
  }
}
```

## Golang

```go
func arraySign(nums []int) int {
    negCount := 0
    for _, v := range nums {
        if v == 0 {
            return 0
        }
        if v < 0 {
            negCount++
        }
    }
    if negCount%2 == 0 {
        return 1
    }
    return -1
}
```

## Ruby

```ruby
def array_sign(nums)
  sign = 1
  nums.each do |num|
    return 0 if num == 0
    sign = -sign if num < 0
  end
  sign
end
```

## Scala

```scala
object Solution {
    def arraySign(nums: Array[Int]): Int = {
        var sign = 1
        for (num <- nums) {
            if (num == 0) return 0
            else if (num < 0) sign = -sign
        }
        sign
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut neg = 0;
        for x in nums {
            if x == 0 {
                return 0;
            }
            if x < 0 {
                neg += 1;
            }
        }
        if neg % 2 == 0 { 1 } else { -1 }
    }
}
```

## Racket

```racket
(define/contract (array-sign nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (neg-count 0))
    (cond
      [(empty? lst) (if (even? neg-count) 1 -1)]
      [(zero? (first lst)) 0]
      [else (loop (rest lst)
                  (if (< (first lst) 0)
                      (+ neg-count 1)
                      neg-count))])))
```

## Erlang

```erlang
-spec array_sign(Nums :: [integer()]) -> integer().
array_sign(Nums) ->
    array_sign(Nums, 0).

array_sign([], NegCount) ->
    case NegCount rem 2 of
        0 -> 1;
        _ -> -1
    end;
array_sign([0|_], _) -> 0;
array_sign([H|T], NegCount) when H < 0 ->
    array_sign(T, NegCount + 1);
array_sign([_|T], NegCount) ->
    array_sign(T, NegCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec array_sign(nums :: [integer]) :: integer
  def array_sign(nums) do
    if Enum.any?(nums, &(&1 == 0)) do
      0
    else
      neg_count = Enum.count(nums, &(&1 < 0))
      if rem(neg_count, 2) == 0, do: 1, else: -1
    end
  end
end
```
