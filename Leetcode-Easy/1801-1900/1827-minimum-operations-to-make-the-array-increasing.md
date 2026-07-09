# 1827. Minimum Operations to Make the Array Increasing

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        long long ops = 0;
        int prev = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] <= prev) {
                int needed = prev + 1;
                ops += needed - nums[i];
                prev = needed;
            } else {
                prev = nums[i];
            }
        }
        return static_cast<int>(ops);
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        long ops = 0;
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > prev) {
                prev = nums[i];
            } else {
                int needed = prev + 1;
                ops += needed - nums[i];
                prev = needed;
            }
        }
        return (int) ops;
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
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1 - nums[i]
                ops += needed
                nums[i] = nums[i - 1] + 1
        return ops
```

## Python3

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(1, len(nums)):
            required = nums[i - 1] + 1
            if nums[i] < required:
                inc = required - nums[i]
                ops += inc
                nums[i] = required
        return ops
```

## C

```c
int minOperations(int* nums, int numsSize){
    if (numsSize <= 1) return 0;
    long long ops = 0;
    long long prev = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        long long need = prev + 1 > nums[i] ? prev + 1 : nums[i];
        ops += need - nums[i];
        prev = need;
    }
    return (int)ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        long operations = 0;
        if (nums == null || nums.Length == 0) return 0;
        int prev = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            int needed = prev + 1;
            if (nums[i] >= needed) {
                prev = nums[i];
            } else {
                operations += needed - nums[i];
                prev = needed;
            }
        }
        return (int)operations;
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
    let operations = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) {
            const target = nums[i - 1] + 1;
            operations += target - nums[i];
            nums[i] = target;
        }
    }
    return operations;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    let operations = 0;
    let prev = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= prev) {
            const needed = prev + 1 - nums[i];
            operations += needed;
            prev = prev + 1;
        } else {
            prev = nums[i];
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
    function minOperations($nums) {
        $operations = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] <= $nums[$i - 1]) {
                $need = $nums[$i - 1] + 1 - $nums[$i];
                $operations += $need;
                $nums[$i] = $nums[$i - 1] + 1;
            }
        }
        return $operations;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var operations = 0
        var prev = nums[0]
        for i in 1..<nums.count {
            let current = nums[i]
            if current > prev {
                prev = current
            } else {
                let needed = prev + 1 - current
                operations += needed
                prev += 1
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
        var ops = 0L
        for (i in 1 until nums.size) {
            if (nums[i] <= nums[i - 1]) {
                val need = nums[i - 1] + 1 - nums[i]
                ops += need
                nums[i] = nums[i - 1] + 1
            }
        }
        return ops.toInt()
    }
}
```

## Golang

```go
func minOperations(nums []int) int {
    ops := 0
    if len(nums) == 0 {
        return 0
    }
    prev := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > prev {
            prev = nums[i]
        } else {
            needed := prev + 1
            ops += needed - nums[i]
            prev = needed
        }
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  ops = 0
  prev = nums[0]
  (1...nums.length).each do |i|
    if nums[i] <= prev
      needed = prev + 1 - nums[i]
      ops += needed
      prev += 1
    else
      prev = nums[i]
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var ops: Long = 0L
        var prev = nums(0)
        for (i <- 1 until nums.length) {
            val cur = nums(i)
            if (cur <= prev) {
                val needed = prev + 1
                ops += needed - cur
                prev = needed
            } else {
                prev = cur
            }
        }
        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut ops: i64 = 0;
        let mut prev = nums[0];
        for &x in nums.iter().skip(1) {
            if x > prev {
                prev = x;
            } else {
                let needed = prev + 1;
                ops += (needed - x) as i64;
                prev = needed;
            }
        }
        ops as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let loop ((rest (cdr nums))
                 (prev (car nums))
                 (ops 0))
        (if (null? rest)
            ops
            (let* ((x (car rest))
                   (desired (max (+ prev 1) x))
                   (add (- desired x)))
              (loop (cdr rest) desired (+ ops add)))))))
```
