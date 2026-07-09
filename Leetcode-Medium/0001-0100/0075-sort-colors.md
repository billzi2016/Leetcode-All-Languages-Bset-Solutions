# 0075. Sort Colors

## Cpp

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0;
        int high = (int)nums.size() - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                ++low;
                ++mid;
            } else if (nums[mid] == 1) {
                ++mid;
            } else { // nums[mid] == 2
                swap(nums[mid], nums[high]);
                --high;
            }
        }
    }
};
```

## Java

```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

## Python3

```python
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

## C

```c
void sortColors(int* nums, int numsSize) {
    int low = 0, mid = 0, high = numsSize - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            int tmp = nums[low];
            nums[low] = nums[mid];
            nums[mid] = tmp;
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else { // nums[mid] == 2
            int tmp = nums[mid];
            nums[mid] = nums[high];
            nums[high] = tmp;
            high--;
        }
    }
}
```

## Csharp

```csharp
public class Solution {
    public void SortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.Length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
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
var sortColors = function(nums) {
    let low = 0;
    let mid = 0;
    let high = nums.length - 1;

    while (mid <= high) {
        if (nums[mid] === 0) {
            // swap nums[low] and nums[mid]
            [nums[low], nums[mid]] = [nums[mid], nums[low]];
            low++;
            mid++;
        } else if (nums[mid] === 1) {
            mid++;
        } else { // nums[mid] === 2
            // swap nums[mid] and nums[high]
            [nums[mid], nums[high]] = [nums[high], nums[mid]];
            high--;
        }
    }
};
```

## Typescript

```typescript
function sortColors(nums: number[]): void {
    let low = 0;
    let mid = 0;
    let high = nums.length - 1;

    while (mid <= high) {
        if (nums[mid] === 0) {
            [nums[low], nums[mid]] = [nums[mid], nums[low]];
            low++;
            mid++;
        } else if (nums[mid] === 1) {
            mid++;
        } else { // nums[mid] === 2
            [nums[mid], nums[high]] = [nums[high], nums[mid]];
            high--;
        }
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
    function sortColors(&$nums) {
        $low = 0;
        $mid = 0;
        $high = count($nums) - 1;

        while ($mid <= $high) {
            if ($nums[$mid] === 0) {
                $tmp = $nums[$low];
                $nums[$low] = $nums[$mid];
                $nums[$mid] = $tmp;
                $low++;
                $mid++;
            } elseif ($nums[$mid] === 1) {
                $mid++;
            } else { // $nums[$mid] == 2
                $tmp = $nums[$mid];
                $nums[$mid] = $nums[$high];
                $nums[$high] = $tmp;
                $high--;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func sortColors(_ nums: inout [Int]) {
        var low = 0
        var mid = 0
        var high = nums.count - 1
        
        while mid <= high {
            switch nums[mid] {
            case 0:
                nums.swapAt(low, mid)
                low += 1
                mid += 1
            case 1:
                mid += 1
            default: // 2
                nums.swapAt(mid, high)
                high -= 1
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortColors(nums: IntArray) {
        var low = 0
        var mid = 0
        var high = nums.lastIndex

        while (mid <= high) {
            when (nums[mid]) {
                0 -> {
                    val temp = nums[low]
                    nums[low] = nums[mid]
                    nums[mid] = temp
                    low++
                    mid++
                }
                1 -> {
                    mid++
                }
                else -> { // nums[mid] == 2
                    val temp = nums[mid]
                    nums[mid] = nums[high]
                    nums[high] = temp
                    high--
                }
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void sortColors(List<int> nums) {
    int low = 0;
    int mid = 0;
    int high = nums.length - 1;

    while (mid <= high) {
      if (nums[mid] == 0) {
        int temp = nums[low];
        nums[low] = nums[mid];
        nums[mid] = temp;
        low++;
        mid++;
      } else if (nums[mid] == 1) {
        mid++;
      } else { // nums[mid] == 2
        int temp = nums[mid];
        nums[mid] = nums[high];
        nums[high] = temp;
        high--;
      }
    }
  }
}
```

## Golang

```go
func sortColors(nums []int) {
    low, mid, high := 0, 0, len(nums)-1
    for mid <= high {
        switch nums[mid] {
        case 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low++
            mid++
        case 1:
            mid++
        case 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high--
        }
    }
}
```

## Ruby

```ruby
def sort_colors(nums)
  low = 0
  mid = 0
  high = nums.length - 1

  while mid <= high
    case nums[mid]
    when 0
      nums[low], nums[mid] = nums[mid], nums[low]
      low += 1
      mid += 1
    when 1
      mid += 1
    else # nums[mid] == 2
      nums[mid], nums[high] = nums[high], nums[mid]
      high -= 1
    end
  end
end
```

## Scala

```scala
object Solution {
    def sortColors(nums: Array[Int]): Unit = {
        var low = 0
        var mid = 0
        var high = nums.length - 1

        while (mid <= high) {
            nums(mid) match {
                case 0 =>
                    val tmp = nums(low)
                    nums(low) = nums(mid)
                    nums(mid) = tmp
                    low += 1
                    mid += 1
                case 1 =>
                    mid += 1
                case 2 =>
                    val tmp = nums(mid)
                    nums(mid) = nums(high)
                    nums(high) = tmp
                    high -= 1
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut low: usize = 0;
        let mut mid: usize = 0;
        if nums.is_empty() {
            return;
        }
        let mut high: isize = (nums.len() as isize) - 1;

        while (mid as isize) <= high {
            match nums[mid] {
                0 => {
                    nums.swap(low, mid);
                    low += 1;
                    mid += 1;
                }
                1 => {
                    mid += 1;
                }
                2 => {
                    let h = high as usize;
                    nums.swap(mid, h);
                    high -= 1;
                }
                _ => unreachable!(),
            }
        }
    }
}
```
