# 0080. Remove Duplicates from Sorted Array II

## Cpp

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;
        int i = 2;
        for (int j = 2; j < n; ++j) {
            if (nums[j] != nums[i - 2]) {
                nums[i++] = nums[j];
            }
        }
        return i;
    }
};
```

## Java

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;
        int i = 2; // position to place next allowed element
        for (int j = 2; j < n; ++j) {
            if (nums[j] != nums[i - 2]) {
                nums[i++] = nums[j];
            }
        }
        return i;
    }
}
```

## Python

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        write = 2
        for read in range(2, n):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write
```

## Python3

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i = 2
        for j in range(2, n):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i
```

## C

```c
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize <= 2) return numsSize;
    int i = 2;
    for (int j = 2; j < numsSize; ++j) {
        if (nums[j] != nums[i - 2]) {
            nums[i++] = nums[j];
        }
    }
    return i;
}
```

## Csharp

```csharp
public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        int n = nums.Length;
        if (n <= 2) return n;

        int i = 2;
        for (int j = 2; j < n; ++j)
        {
            if (nums[j] != nums[i - 2])
            {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const n = nums.length;
    if (n <= 2) return n;
    let write = 2;
    for (let i = 2; i < n; ++i) {
        if (nums[i] !== nums[write - 2]) {
            nums[write] = nums[i];
            write++;
        }
    }
    return write;
};
```

## Typescript

```typescript
function removeDuplicates(nums: number[]): number {
    let i = 0;
    for (const num of nums) {
        if (i < 2 || num > nums[i - 2]) {
            nums[i] = num;
            i++;
        }
    }
    return i;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $i = 0;
        foreach ($nums as $num) {
            if ($i < 2 || $nums[$i - 2] !== $num) {
                $nums[$i++] = $num;
            }
        }
        return $i;
    }
}
```

## Swift

```swift
class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var writeIndex = 0
        for num in nums {
            if writeIndex < 2 || num != nums[writeIndex - 2] {
                nums[writeIndex] = num
                writeIndex += 1
            }
        }
        return writeIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var i = 0
        for (num in nums) {
            if (i < 2 || num != nums[i - 2]) {
                nums[i] = num
                i++
            }
        }
        return i
    }
}
```

## Dart

```dart
class Solution {
  int removeDuplicates(List<int> nums) {
    int n = nums.length;
    if (n <= 2) return n;
    int write = 0;
    for (int i = 0; i < n; ++i) {
      int num = nums[i];
      if (write < 2 || nums[write - 2] != num) {
        nums[write] = num;
        write++;
      }
    }
    return write;
  }
}
```

## Golang

```go
func removeDuplicates(nums []int) int {
	if len(nums) <= 2 {
		return len(nums)
	}
	i := 2
	for j := 2; j < len(nums); j++ {
		if nums[j] != nums[i-2] {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  write = 0
  nums.each do |num|
    if write < 2 || num != nums[write - 2]
      nums[write] = num
      write += 1
    end
  end
  write
end
```

## Scala

```scala
object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        val n = nums.length
        if (n <= 2) return n
        var write = 2
        var i = 2
        while (i < n) {
            if (nums(i) != nums(write - 2)) {
                nums(write) = nums(i)
                write += 1
            }
            i += 1
        }
        write
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 2 {
            return n as i32;
        }
        let mut write = 2usize;
        for read in 2..n {
            if nums[read] != nums[write - 2] {
                nums[write] = nums[read];
                write += 1;
            }
        }
        write as i32
    }
}
```
