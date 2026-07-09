# 3512. Minimum Operations to Make Array Sum Divisible by K

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        long long sum = 0;
        for (int num : nums) sum += num;
        return sum % k;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums, int k) {
        long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return (int)(sum % k);
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(nums)
        return total % k
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
```

## C

```c
int minOperations(int* nums, int numsSize, int k) {
    long long sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
    }
    return (int)(sum % k);
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums, int k) {
        long sum = 0;
        foreach (int num in nums) {
            sum += num;
        }
        return (int)(sum % k);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    let total = 0;
    for (let num of nums) {
        total += num;
    }
    return total % k;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    let total = 0;
    for (const num of nums) {
        total += num;
    }
    return total % k;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        $sum = array_sum($nums);
        return $sum % $k;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var total = 0
        for num in nums {
            total += num
        }
        return total % k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var sum = 0
        for (num in nums) {
            sum += num
        }
        return sum % k
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    int total = 0;
    for (var num in nums) {
      total += num;
    }
    return total % k;
  }
}
```

## Golang

```go
func minOperations(nums []int, k int) int {
    sum := 0
    for _, v := range nums {
        sum += v
    }
    return sum % k
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  nums.sum % k
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        val sum = nums.foldLeft(0L)(_ + _)
        (sum % k).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let sum: i32 = nums.iter().sum();
        sum % k
    }
}
```

## Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((s (apply + nums)))
    (modulo s k)))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    Sum = lists:sum(Nums),
    Sum rem K.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    sum = Enum.sum(nums)
    rem(sum, k)
  end
end
```
