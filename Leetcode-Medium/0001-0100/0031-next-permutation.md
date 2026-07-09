# 0031. Next Permutation

## Cpp

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) --i;
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) --j;
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```

## Java

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1, n - 1);
    }

    private void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private void reverse(int[] arr, int left, int right) {
        while (left < right) {
            swap(arr, left++, right--);
        }
    }
}
```

## Python

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Find the first index i such that nums[i] < nums[i+1] when scanning from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest element greater than nums[i] to its right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the suffix starting at i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## Python3

```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## C

```c
void nextPermutation(int* nums, int numsSize) {
    if (numsSize <= 1) return;
    int i = numsSize - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = numsSize - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    int left = i + 1, right = numsSize - 1;
    while (left < right) {
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
        left++;
        right--;
    }
}
```

## Csharp

```csharp
public class Solution
{
    public void NextPermutation(int[] nums)
    {
        int n = nums.Length;
        if (n <= 1) return;

        // Find the first index 'i' from the right such that nums[i] < nums[i + 1]
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1])
            i--;

        if (i >= 0)
        {
            // Find the smallest element greater than nums[i] to the right of i
            int j = n - 1;
            while (nums[j] <= nums[i])
                j--;
            Swap(nums, i, j);
        }

        // Reverse the subarray from i + 1 to the end
        Reverse(nums, i + 1, n - 1);
    }

    private void Swap(int[] arr, int a, int b)
    {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    private void Reverse(int[] arr, int left, int right)
    {
        while (left < right)
        {
            Swap(arr, left, right);
            left++;
            right--;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    const n = nums.length;
    // Find the first index i such that nums[i] < nums[i + 1] scanning from right
    let i = n - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        // Find the smallest element greater than nums[i] to its right
        let j = n - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        // Swap nums[i] and nums[j]
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }
    // Reverse the suffix starting at i + 1
    let left = i + 1;
    let right = n - 1;
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};
```

## Typescript

```typescript
function nextPermutation(nums: number[]): void {
    const n = nums.length;
    let i = n - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        let j = n - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        const temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    let left = i + 1;
    let right = n - 1;
    while (left < right) {
        const tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
        left++;
        right--;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function nextPermutation(&$nums) {
        $n = count($nums);
        if ($n <= 1) {
            return;
        }

        // Find the first index i such that nums[i] < nums[i + 1] scanning from right to left
        $i = $n - 2;
        while ($i >= 0 && $nums[$i] >= $nums[$i + 1]) {
            $i--;
        }

        if ($i >= 0) {
            // Find the smallest element greater than nums[i] to its right
            $j = $n - 1;
            while ($j > $i && $nums[$j] <= $nums[$i]) {
                $j--;
            }
            // Swap nums[i] and nums[j]
            $tmp = $nums[$i];
            $nums[$i] = $nums[$j];
            $nums[$j] = $tmp;
        }

        // Reverse the subarray from i+1 to end to get the next smallest lexicographic order
        $left = $i + 1;
        $right = $n - 1;
        while ($left < $right) {
            $tmp = $nums[$left];
            $nums[$left] = $nums[$right];
            $nums[$right] = $tmp;
            $left++;
            $right--;
        }
    }
}
```

## Swift

```swift
class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        let n = nums.count
        if n <= 1 { return }
        
        var i = n - 2
        while i >= 0 && nums[i] >= nums[i + 1] {
            i -= 1
        }
        
        if i >= 0 {
            var j = n - 1
            while nums[j] <= nums[i] {
                j -= 1
            }
            nums.swapAt(i, j)
        }
        
        var left = i + 1
        var right = n - 1
        while left < right {
            nums.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextPermutation(nums: IntArray) {
        var i = nums.size - 2
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--
        }
        if (i >= 0) {
            var j = nums.size - 1
            while (nums[j] <= nums[i]) {
                j--
            }
            val tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        }
        var left = i + 1
        var right = nums.size - 1
        while (left < right) {
            val tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left++
            right--
        }
    }
}
```

## Dart

```dart
class Solution {
  void nextPermutation(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return;

    // Find the first index i such that nums[i] < nums[i + 1] scanning from right
    int i = n - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
      i--;
    }

    if (i >= 0) {
      // Find the smallest element greater than nums[i] to the right side
      int j = n - 1;
      while (j > i && nums[j] <= nums[i]) {
        j--;
      }
      // Swap nums[i] and nums[j]
      int temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
    }

    // Reverse the subarray from i + 1 to end
    int left = i + 1, right = n - 1;
    while (left < right) {
      int temp = nums[left];
      nums[left] = nums[right];
      nums[right] = temp;
      left++;
      right--;
    }
  }
}
```

## Golang

```go
func nextPermutation(nums []int) {
    n := len(nums)
    if n <= 1 {
        return
    }
    i := n - 2
    for i >= 0 && nums[i] >= nums[i+1] {
        i--
    }
    if i >= 0 {
        j := n - 1
        for nums[j] <= nums[i] {
            j--
        }
        nums[i], nums[j] = nums[j], nums[i]
    }
    left, right := i+1, n-1
    for left < right {
        nums[left], nums[right] = nums[right], nums[left]
        left++
        right--
    }
}
```

## Ruby

```ruby
def next_permutation(nums)
  n = nums.length
  i = n - 2
  while i >= 0 && nums[i] >= nums[i + 1]
    i -= 1
  end

  if i >= 0
    j = n - 1
    while nums[j] <= nums[i]
      j -= 1
    end
    nums[i], nums[j] = nums[j], nums[i]
  end

  left = i + 1
  right = n - 1
  while left < right
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  end
end
```

## Scala

```scala
object Solution {
  def nextPermutation(nums: Array[Int]): Unit = {
    val n = nums.length
    if (n <= 1) return

    var i = n - 2
    while (i >= 0 && nums(i) >= nums(i + 1)) {
      i -= 1
    }

    if (i >= 0) {
      var j = n - 1
      while (j > i && nums(j) <= nums(i)) {
        j -= 1
      }
      val tmp = nums(i)
      nums(i) = nums(j)
      nums(j) = tmp
    }

    var left = i + 1
    var right = n - 1
    while (left < right) {
      val t = nums(left)
      nums(left) = nums(right)
      nums(right) = t
      left += 1
      right -= 1
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n < 2 {
            return;
        }

        // Find the first index i such that nums[i] < nums[i + 1] scanning from right
        let mut i: i32 = (n - 2) as i32;
        while i >= 0 && nums[i as usize] >= nums[(i + 1) as usize] {
            i -= 1;
        }

        if i < 0 {
            // Entire sequence is non-increasing, reverse to get smallest permutation
            nums.reverse();
            return;
        }

        let i_usize = i as usize;

        // Find the smallest element greater than nums[i] to the right of i
        let mut j = n - 1;
        while nums[j] <= nums[i_usize] {
            j -= 1;
        }

        // Swap them
        nums.swap(i_usize, j);

        // Reverse the suffix starting at i+1
        let mut left = i_usize + 1;
        let mut right = n - 1;
        while left < right {
            nums.swap(left, right);
            left += 1;
            if right == 0 { break; } // safety, though condition ensures right > left
            right -= 1;
        }
    }
}
```
