# 1877. Minimize Maximum Pair Sum in Array

## Cpp

```cpp
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int maxSum = 0;
        for (int i = 0; i < n / 2; ++i) {
            int pairSum = nums[i] + nums[n - 1 - i];
            if (pairSum > maxSum) maxSum = pairSum;
        }
        return maxSum;
    }
};
```

## Java

```java
class Solution {
    public int minPairSum(int[] nums) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int maxSum = 0;
        for (int i = 0; i < n / 2; i++) {
            int sum = nums[i] + nums[n - 1 - i];
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
        return maxSum;
    }
}
```

## Python

```python
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0
        n = len(nums)
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            if pair_sum > max_sum:
                max_sum = pair_sum
        return max_sum
```

## Python3

```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            if pair_sum > max_sum:
                max_sum = pair_sum
        return max_sum
```

## C

```c
#include <stdlib.h>

static int compare_ints(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int minPairSum(int* nums, int numsSize){
    qsort(nums, (size_t)numsSize, sizeof(int), compare_ints);
    int maxSum = 0;
    for (int i = 0; i < numsSize / 2; ++i) {
        int sum = nums[i] + nums[numsSize - 1 - i];
        if (sum > maxSum) maxSum = sum;
    }
    return maxSum;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinPairSum(int[] nums)
    {
        System.Array.Sort(nums);
        int n = nums.Length;
        int maxSum = 0;
        for (int i = 0; i < n / 2; i++)
        {
            int sum = nums[i] + nums[n - 1 - i];
            if (sum > maxSum)
                maxSum = sum;
        }
        return maxSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let maxSum = 0;
    const n = nums.length;
    for (let i = 0; i < n / 2; ++i) {
        const pairSum = nums[i] + nums[n - 1 - i];
        if (pairSum > maxSum) maxSum = pairSum;
    }
    return maxSum;
};
```

## Typescript

```typescript
function minPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let maxSum = 0;
    const n = nums.length;
    for (let i = 0; i < n / 2; i++) {
        const pairSum = nums[i] + nums[n - 1 - i];
        if (pairSum > maxSum) maxSum = pairSum;
    }
    return maxSum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minPairSum($nums) {
        sort($nums);
        $n = count($nums);
        $maxSum = 0;
        for ($i = 0; $i < $n / 2; $i++) {
            $pairSum = $nums[$i] + $nums[$n - 1 - $i];
            if ($pairSum > $maxSum) {
                $maxSum = $pairSum;
            }
        }
        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var maxSum = 0
        let n = sorted.count
        for i in 0..<(n / 2) {
            let sum = sorted[i] + sorted[n - 1 - i]
            if sum > maxSum {
                maxSum = sum
            }
        }
        return maxSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minPairSum(nums: IntArray): Int {
        nums.sort()
        var maxSum = 0
        val n = nums.size
        for (i in 0 until n / 2) {
            val sum = nums[i] + nums[n - 1 - i]
            if (sum > maxSum) maxSum = sum
        }
        return maxSum
    }
}
```

## Golang

```go
func minPairSum(nums []int) int {
    sort.Ints(nums)
    maxSum := 0
    n := len(nums)
    for i := 0; i < n/2; i++ {
        s := nums[i] + nums[n-1-i]
        if s > maxSum {
            maxSum = s
        }
    }
    return maxSum
}
```

## Ruby

```ruby
def min_pair_sum(nums)
  nums.sort!
  n = nums.length
  max_sum = 0
  (0...(n / 2)).each do |i|
    sum = nums[i] + nums[n - 1 - i]
    max_sum = sum if sum > max_sum
  end
  max_sum
end
```

## Scala

```scala
object Solution {
    def minPairSum(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        var maxSum = 0
        val n = sorted.length
        for (i <- 0 until n / 2) {
            val sum = sorted(i) + sorted(n - 1 - i)
            if (sum > maxSum) maxSum = sum
        }
        maxSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut max_sum = 0;
        for i in 0..n / 2 {
            let s = nums[i] + nums[n - 1 - i];
            if s > max_sum {
                max_sum = s;
            }
        }
        max_sum
    }
}
```

## Racket

```racket
(define/contract (min-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (half (quotient n 2)))
    (let loop ((i 0) (max-sum 0))
      (if (= i half)
          max-sum
          (let* ((pair-sum (+ (list-ref sorted i)
                              (list-ref sorted (- n 1 i))))
                 (new-max (if (> pair-sum max-sum) pair-sum max-sum)))
            (loop (+ i 1) new-max))))))
```
