# 1913. Maximum Product Difference Between Two Pairs

## Cpp

```cpp
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int maxProductDifference(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
    }
}
```

## Python

```python
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
```

## Python3

```python
from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
```

## C

```c
#include <limits.h>

int maxProductDifference(int* nums, int numsSize) {
    int max1 = 0, max2 = 0;
    int min1 = INT_MAX, min2 = INT_MAX;

    for (int i = 0; i < numsSize; ++i) {
        int num = nums[i];

        // Update two largest
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }

        // Update two smallest
        if (num < min1) {
            min2 = min1;
            min1 = num;
        } else if (num < min2) {
            min2 = num;
        }
    }

    return max1 * max2 - min1 * min2;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProductDifference(int[] nums) {
        System.Array.Sort(nums);
        int n = nums.Length;
        return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
};
```

## Typescript

```typescript
function maxProductDifference(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProductDifference($nums) {
        sort($nums);
        $n = count($nums);
        return $nums[$n - 1] * $nums[$n - 2] - $nums[0] * $nums[1];
    }
}
```

## Swift

```swift
class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        return sorted[n - 1] * sorted[n - 2] - sorted[0] * sorted[1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProductDifference(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        return nums[n - 1] * nums[n - 2] - nums[0] * nums[1]
    }
}
```

## Golang

```go
import "sort"

func maxProductDifference(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	return nums[n-1]*nums[n-2] - nums[0]*nums[1]
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_product_difference(nums)
  nums.sort!
  nums[-1] * nums[-2] - nums[0] * nums[1]
end
```

## Scala

```scala
object Solution {
    def maxProductDifference(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        sorted(n - 1) * sorted(n - 2) - sorted(0) * sorted(1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut v = nums;
        v.sort_unstable();
        let n = v.len();
        v[n - 1] * v[n - 2] - v[0] * v[1]
    }
}
```

## Racket

```racket
(define/contract (max-product-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (define (update-max x max1 max2)
    (cond [(> x max1) (values x max1)]
          [(> x max2) (values max1 x)]
          [else        (values max1 max2)]))
  (define (update-min x min1 min2)
    (cond [(< x min1) (values x min1)]
          [(< x min2) (values min1 x)]
          [else       (values min1 min2)]))
  (let loop ((lst nums)
             (max1 0) (max2 0)
             (min1 1000000000) (min2 1000000000))
    (if (null? lst)
        (- (* max1 max2) (* min1 min2))
        (let-values (((new-max1 new-max2) (update-max (car lst) max1 max2))
                     ((new-min1 new-min2) (update-min (car lst) min1 min2)))
          (loop (cdr lst) new-max1 new-max2 new-min1 new-min2)))))
```
