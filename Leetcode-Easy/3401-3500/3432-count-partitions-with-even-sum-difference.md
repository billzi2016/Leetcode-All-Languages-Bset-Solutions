# 3432. Count Partitions with Even Sum Difference

## Cpp

```cpp
class Solution {
public:
    int countPartitions(vector<int>& nums) {
        long long total = 0;
        for (int v : nums) total += v;
        if (total % 2 == 0) return static_cast<int>(nums.size()) - 1;
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int countPartitions(int[] nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return (total % 2 == 0) ? nums.length - 1 : 0;
    }
}
```

## Python

```python
class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        if total & 1:
            return 0
        cnt = 0
        prefix = 0
        # iterate up to second last element as partition index i (0-indexed)
        for i in range(len(nums) - 1):
            prefix += nums[i]
            if prefix & 1 == 0:
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        return len(nums) - 1 if total % 2 == 0 else 0
```

## C

```c
int countPartitions(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    if (total % 2 == 0) {
        return numsSize - 1;
    } else {
        return 0;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int CountPartitions(int[] nums) {
        int total = 0;
        foreach (int num in nums) total += num;
        return (total % 2 == 0) ? nums.Length - 1 : 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function(nums) {
    let total = 0;
    for (let v of nums) total += v;
    return total % 2 === 0 ? nums.length - 1 : 0;
};
```

## Typescript

```typescript
function countPartitions(nums: number[]): number {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total % 2 !== 0) return 0;
    let prefix = 0;
    let ans = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        prefix += nums[i];
        if (prefix % 2 === 0) ans++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countPartitions($nums) {
        $total = array_sum($nums);
        $count = 0;
        $leftSum = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            $leftSum += $nums[$i];
            $rightSum = $total - $leftSum;
            if ( ($leftSum & 1) === ($rightSum & 1) ) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        return total % 2 == 0 ? nums.count - 1 : 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPartitions(nums: IntArray): Int {
        var sum = 0
        for (num in nums) sum += num
        return if (sum % 2 == 0) nums.size - 1 else 0
    }
}
```

## Dart

```dart
class Solution {
  int countPartitions(List<int> nums) {
    int total = 0;
    for (int v in nums) {
      total += v;
    }
    return total % 2 == 0 ? nums.length - 1 : 0;
  }
}
```

## Golang

```go
func countPartitions(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    if total%2 == 0 {
        return len(nums) - 1
    }
    return 0
}
```

## Ruby

```ruby
def count_partitions(nums)
  total = nums.sum
  total.even? ? nums.length - 1 : 0
end
```

## Scala

```scala
object Solution {
    def countPartitions(nums: Array[Int]): Int = {
        if (nums.sum % 2 == 0) nums.length - 1 else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        if total % 2 == 0 {
            (nums.len() as i32) - 1
        } else {
            0
        }
    }
}
```

## Racket

```racket
(define/contract (count-partitions nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((total (apply + nums)))
    (if (even? total)
        (- (length nums) 1)
        0)))
```

## Erlang

```erlang
-spec count_partitions([integer()]) -> integer().
count_partitions(Nums) ->
    Total = lists:sum(Nums),
    if
        Total rem 2 =:= 0 -> length(Nums) - 1;
        true -> 0
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_partitions(nums :: [integer]) :: integer
  def count_partitions(nums) do
    total = Enum.sum(nums)

    if rem(total, 2) == 0 do
      length(nums) - 1
    else
      0
    end
  end
end
```
