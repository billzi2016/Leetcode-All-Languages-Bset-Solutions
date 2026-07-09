# 0189. Rotate Array

## Cpp

```cpp
class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return;
        k %= n;
        if (k == 0) return;
        auto rev = [&](int l, int r) {
            while (l < r) {
                std::swap(nums[l++], nums[r--]);
            }
        };
        rev(0, n - 1);
        rev(0, k - 1);
        rev(k, n - 1);
    }
};
```

## Java

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return;
        k %= n;
        if (k == 0) return;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }
    
    private void reverse(int[] arr, int left, int right) {
        while (left < right) {
            int tmp = arr[left];
            arr[left++] = arr[right];
            arr[right--] = tmp;
        }
    }
}
```

## Python

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return

        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)

    def _reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## Python3

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return

        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)

    def _reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## C

```c
void rotate(int* nums, int numsSize, int k) {
    if (numsSize <= 1) return;
    k %= numsSize;
    if (k == 0) return;

    // helper to reverse a segment in-place
    auto rev = [&](int left, int right) {
        while (left < right) {
            int tmp = nums[left];
            nums[left++] = nums[right];
            nums[right--] = tmp;
        }
    };

    rev(0, numsSize - 1);
    rev(0, k - 1);
    rev(k, numsSize - 1);
}
```

## Csharp

```csharp
public class Solution
{
    public void Rotate(int[] nums, int k)
    {
        int n = nums.Length;
        if (n == 0) return;
        k %= n;
        Reverse(nums, 0, n - 1);
        Reverse(nums, 0, k - 1);
        Reverse(nums, k, n - 1);
    }

    private void Reverse(int[] nums, int left, int right)
    {
        while (left < right)
        {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}
```

## Javascript

```javascript
function reverse(arr, start, end) {
    while (start < end) {
        const temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const n = nums.length;
    if (n === 0) return;
    k %= n;
    if (k === 0) return;

    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);
};
```

## Typescript

```typescript
function rotate(nums: number[], k: number): void {
    const n = nums.length;
    if (n === 0) return;
    k %= n;
    if (k === 0) return;

    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);
}

function reverse(arr: number[], left: number, right: number): void {
    while (left < right) {
        const tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
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
     * @param Integer $k
     * @return NULL
     */
    function rotate(&$nums, $k) {
        $n = count($nums);
        if ($n == 0) return;
        $k %= $n;
        if ($k == 0) return;

        $this->reverse($nums, 0, $n - 1);
        $this->reverse($nums, 0, $k - 1);
        $this->reverse($nums, $k, $n - 1);
    }

    private function reverse(&$arr, $start, $end) {
        while ($start < $end) {
            $tmp = $arr[$start];
            $arr[$start] = $arr[$end];
            $arr[$end] = $tmp;
            $start++;
            $end--;
        }
    }
}
```

## Swift

```swift
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        let n = nums.count
        guard n > 0 else { return }
        var k = k % n
        if k == 0 { return }
        
        func reverse(_ start: Int, _ end: Int) {
            var left = start
            var right = end - 1
            while left < right {
                nums.swapAt(left, right)
                left += 1
                right -= 1
            }
        }
        
        reverse(0, n)
        reverse(0, k)
        reverse(k, n)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rotate(nums: IntArray, k: Int) {
        val n = nums.size
        if (n == 0) return
        var kk = k % n
        if (kk == 0) return
        reverse(nums, 0, n - 1)
        reverse(nums, 0, kk - 1)
        reverse(nums, kk, n - 1)
    }

    private fun reverse(arr: IntArray, start: Int, end: Int) {
        var i = start
        var j = end
        while (i < j) {
            val tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i++
            j--
        }
    }
}
```

## Dart

```dart
class Solution {
  void rotate(List<int> nums, int k) {
    int n = nums.length;
    if (n == 0) return;
    k %= n;
    if (k == 0) return;

    _reverse(nums, 0, n - 1);
    _reverse(nums, 0, k - 1);
    _reverse(nums, k, n - 1);
  }

  void _reverse(List<int> nums, int left, int right) {
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
func rotate(nums []int, k int) {
	n := len(nums)
	if n == 0 {
		return
	}
	k = k % n
	if k == 0 {
		return
	}
	reverse := func(a []int, start, end int) {
		for start < end {
			a[start], a[end] = a[end], a[start]
			start++
			end--
		}
	}
	reverse(nums, 0, n-1)
	reverse(nums, 0, k-1)
	reverse(nums, k, n-1)
}
```

## Ruby

```ruby
def rotate(nums, k)
  n = nums.length
  return if n <= 1 || (k %= n) == 0

  # reverse entire array
  l, r = 0, n - 1
  while l < r
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
  end

  # reverse first k elements
  l, r = 0, k - 1
  while l < r
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
  end

  # reverse the rest
  l, r = k, n - 1
  while l < r
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
  end
end
```

## Scala

```scala
object Solution {
    def rotate(nums: Array[Int], k: Int): Unit = {
        val n = nums.length
        if (n == 0) return
        val steps = k % n
        if (steps == 0) return

        reverse(nums, 0, n - 1)
        reverse(nums, 0, steps - 1)
        reverse(nums, steps, n - 1)
    }

    private def reverse(arr: Array[Int], left: Int, right: Int): Unit = {
        var l = left
        var r = right
        while (l < r) {
            val tmp = arr(l)
            arr(l) = arr(r)
            arr(r) = tmp
            l += 1
            r -= 1
        }
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let n = nums.len();
        if n == 0 {
            return;
        }
        let k = (k as usize) % n;
        if k == 0 {
            return;
        }

        nums.reverse();
        nums[..k].reverse();
        nums[k..].reverse();
    }
}
```
