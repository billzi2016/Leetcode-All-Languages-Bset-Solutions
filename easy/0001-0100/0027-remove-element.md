# 0027. Remove Element

## Cpp

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
```

## Java

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}
```

## Python

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
```

## Python3

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
```

## C

```c
int removeElement(int* nums, int numsSize, int val) {
    int k = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != val) {
            nums[k++] = nums[i];
        }
    }
    return k;
}
```

## Csharp

```csharp
public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k++] = nums[i];
        }
    }
    return k;
};
```

## Typescript

```typescript
function removeElement(nums: number[], val: number): number {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] !== val) {
            nums[i] = nums[j];
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
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        $k = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] !== $val) {
                $nums[$k++] = $nums[$i];
            }
        }
        if (count($nums) > $k) {
            array_splice($nums, $k);
        }
        return $k;
    }
}
```

## Swift

```swift
class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var index = 0
        for num in nums {
            if num != val {
                nums[index] = num
                index += 1
            }
        }
        return index
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var i = 0
        for (j in nums.indices) {
            if (nums[j] != `val`) {
                nums[i] = nums[j]
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
  int removeElement(List<int> nums, int val) {
    int k = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != val) {
        nums[k] = nums[i];
        k++;
      }
    }
    return k;
  }
}
```

## Golang

```go
func removeElement(nums []int, val int) int {
    k := 0
    for _, v := range nums {
        if v != val {
            nums[k] = v
            k++
        }
    }
    return k
}
```

## Ruby

```ruby
def remove_element(nums, val)
  k = 0
  nums.each do |num|
    if num != val
      nums[k] = num
      k += 1
    end
  end
  k
end
```

## Scala

```scala
object Solution {
    def removeElement(nums: Array[Int], `val`: Int): Int = {
        var i = 0
        val n = nums.length
        while (i < n && nums(i) == `val`) i += 1 // optional, but we will just use two-pointer approach below
        var write = 0
        var read = 0
        while (read < n) {
            if (nums(read) != `val`) {
                nums(write) = nums(read)
                write += 1
            }
            read += 1
        }
        write
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k = 0usize;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums[k] = nums[i];
                k += 1;
            }
        }
        k as i32
    }
}
```
