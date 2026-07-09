# 1685. Sum of Absolute Differences in a Sorted Array

## Cpp

```cpp
class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size();
        long long totalSum = 0;
        for (int v : nums) totalSum += v;
        vector<int> ans(n);
        long long leftSum = 0;
        for (int i = 0; i < n; ++i) {
            long long rightSum = totalSum - leftSum - nums[i];
            long long leftCount = i;
            long long rightCount = n - 1 - i;
            long long leftTotal = leftCount * nums[i] - leftSum;
            long long rightTotal = rightSum - rightCount * nums[i];
            ans[i] = static_cast<int>(leftTotal + rightTotal);
            leftSum += nums[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        long totalSum = 0L;
        for (int num : nums) {
            totalSum += num;
        }
        long leftSum = 0L;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            long rightSum = totalSum - leftSum - nums[i];
            long leftCount = i;
            long rightCount = n - 1 - i;

            long leftTotal = leftCount * nums[i] - leftSum;
            long rightTotal = rightSum - rightCount * nums[i];

            result[i] = (int) (leftTotal + rightTotal);
            leftSum += nums[i];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        ans = []
        for i, x in enumerate(nums):
            right_sum = total - left_sum - x
            left_cnt = i
            right_cnt = n - 1 - i
            left_total = left_cnt * x - left_sum
            right_total = right_sum - right_cnt * x
            ans.append(left_total + right_total)
            left_sum += x
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        n = len(nums)
        result = [0] * n
        for i, x in enumerate(nums):
            right_sum = total - left_sum - x
            left_cnt = i
            right_cnt = n - i - 1
            left_total = left_cnt * x - left_sum
            right_total = right_sum - right_cnt * x
            result[i] = left_total + right_total
            left_sum += x
        return result
```

## C

```c
#include <stdlib.h>

int* getSumAbsoluteDifferences(int* nums, int numsSize, int* returnSize) {
    long long totalSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        totalSum += nums[i];
    }
    
    long long leftSum = 0;
    int* result = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        long long rightSum = totalSum - leftSum - nums[i];
        long long leftCount = i;
        long long rightCount = numsSize - 1 - i;
        
        long long leftTotal = leftCount * nums[i] - leftSum;
        long long rightTotal = rightSum - rightCount * nums[i];
        result[i] = (int)(leftTotal + rightTotal);
        
        leftSum += nums[i];
    }
    
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] GetSumAbsoluteDifferences(int[] nums)
    {
        int n = nums.Length;
        long totalSum = 0;
        foreach (int v in nums) totalSum += v;

        long leftSum = 0;
        int[] result = new int[n];

        for (int i = 0; i < n; i++)
        {
            long rightSum = totalSum - leftSum - nums[i];
            long leftCount = i;
            long rightCount = n - 1 - i;

            long leftTotal = leftCount * nums[i] - leftSum;
            long rightTotal = rightSum - rightCount * nums[i];

            result[i] = (int)(leftTotal + rightTotal);
            leftSum += nums[i];
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;

    let leftSum = 0;
    const result = new Array(n);
    for (let i = 0; i < n; ++i) {
        const rightSum = total - leftSum - nums[i];
        const leftCount = i;
        const rightCount = n - 1 - i;

        const leftTotal = leftCount * nums[i] - leftSum;
        const rightTotal = rightSum - rightCount * nums[i];

        result[i] = leftTotal + rightTotal;
        leftSum += nums[i];
    }
    return result;
};
```

## Typescript

```typescript
function getSumAbsoluteDifferences(nums: number[]): number[] {
    const n = nums.length;
    const total = nums.reduce((sum, val) => sum + val, 0);
    const result = new Array<number>(n);
    let leftSum = 0;
    for (let i = 0; i < n; i++) {
        const rightSum = total - leftSum - nums[i];
        const leftCount = i;
        const rightCount = n - i - 1;
        const leftTotal = leftCount * nums[i] - leftSum;
        const rightTotal = rightSum - rightCount * nums[i];
        result[i] = leftTotal + rightTotal;
        leftSum += nums[i];
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSumAbsoluteDifferences($nums) {
        $n = count($nums);
        $total = array_sum($nums);
        $leftSum = 0;
        $result = [];

        for ($i = 0; $i < $n; $i++) {
            $rightSum = $total - $leftSum - $nums[$i];
            $leftCount = $i;
            $rightCount = $n - 1 - $i;

            $leftTotal = $leftCount * $nums[$i] - $leftSum;
            $rightTotal = $rightSum - $rightCount * $nums[$i];

            $result[] = $leftTotal + $rightTotal;
            $leftSum += $nums[$i];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getSumAbsoluteDifferences(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var total = 0
        for v in nums { total += v }
        var leftSum = 0
        var result = Array(repeating: 0, count: n)
        for i in 0..<n {
            let rightSum = total - leftSum - nums[i]
            let leftCount = i
            let rightCount = n - 1 - i
            let leftTotal = leftCount * nums[i] - leftSum
            let rightTotal = rightSum - rightCount * nums[i]
            result[i] = leftTotal + rightTotal
            leftSum += nums[i]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSumAbsoluteDifferences(nums: IntArray): IntArray {
        val n = nums.size
        var total = 0L
        for (v in nums) total += v.toLong()
        var leftSum = 0L
        val result = IntArray(n)
        for (i in 0 until n) {
            val rightSum = total - leftSum - nums[i].toLong()
            val leftCount = i.toLong()
            val rightCount = (n - 1 - i).toLong()
            val leftTotal = leftCount * nums[i] - leftSum
            val rightTotal = rightSum - rightCount * nums[i]
            result[i] = (leftTotal + rightTotal).toInt()
            leftSum += nums[i].toLong()
        }
        return result
    }
}
```

## Golang

```go
func getSumAbsoluteDifferences(nums []int) []int {
    n := len(nums)
    total := 0
    for _, v := range nums {
        total += v
    }
    ans := make([]int, n)
    leftSum := 0
    for i, v := range nums {
        rightSum := total - leftSum - v
        leftCount := i
        rightCount := n - 1 - i
        leftTotal := leftCount*v - leftSum
        rightTotal := rightSum - rightCount*v
        ans[i] = leftTotal + rightTotal
        leftSum += v
    }
    return ans
}
```

## Ruby

```ruby
def get_sum_absolute_differences(nums)
  total = nums.sum
  left_sum = 0
  n = nums.length
  result = Array.new(n)

  nums.each_with_index do |num, i|
    right_sum = total - left_sum - num
    left_cnt = i
    right_cnt = n - 1 - i

    left_total = left_cnt * num - left_sum
    right_total = right_sum - right_cnt * num

    result[i] = left_total + right_total
    left_sum += num
  end

  result
end
```

## Scala

```scala
object Solution {
  def getSumAbsoluteDifferences(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    var totalSum: Long = 0L
    for (v <- nums) totalSum += v

    val ans = new Array[Int](n)
    var leftSum: Long = 0L

    var i = 0
    while (i < n) {
      val cur = nums(i).toLong
      val rightSum = totalSum - leftSum - cur
      val leftCount = i.toLong
      val rightCount = (n - 1 - i).toLong

      val leftTotal = leftCount * cur - leftSum
      val rightTotal = rightSum - rightCount * cur

      ans(i) = (leftTotal + rightTotal).toInt
      leftSum += cur
      i += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut left_sum: i64 = 0;
        let mut ans = Vec::with_capacity(n);
        for (i, &val) in nums.iter().enumerate() {
            let right_sum = total - left_sum - val as i64;
            let left_cnt = i as i64;
            let right_cnt = (n - 1 - i) as i64;
            let left_total = left_cnt * val as i64 - left_sum;
            let right_total = right_sum - right_cnt * val as i64;
            ans.push((left_total + right_total) as i32);
            left_sum += val as i64;
        }
        ans
    }
}
```
