# 0324. Wiggle Sort II

## Cpp

```cpp
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return;
        // Find median
        vector<int> copy = nums;
        nth_element(copy.begin(), copy.begin() + n / 2, copy.end());
        int median = copy[n / 2];
        
        auto idx = [n](int i) { return (1 + 2 * i) % (n | 1); };
        
        int left = 0, i = 0, right = n - 1;
        while (i <= right) {
            int vi = nums[idx(i)];
            if (vi > median) {
                swap(nums[idx(left)], nums[idx(i)]);
                ++left;
                ++i;
            } else if (vi < median) {
                swap(nums[idx(i)], nums[idx(right)]);
                --right;
            } else {
                ++i;
            }
        }
    }
};
```

## Java

```java
class Solution {
    public void wiggleSort(int[] nums) {
        int n = nums.length;
        if (n <= 1) return;
        int median = findKthSmallest(nums.clone(), n / 2);
        int left = 0, i = 0, right = n - 1;
        while (i <= right) {
            int mappedIdx = newIndex(i, n);
            if (nums[mappedIdx] > median) {
                swap(nums, newIndex(left, n), mappedIdx);
                left++;
                i++;
            } else if (nums[mappedIdx] < median) {
                swap(nums, mappedIdx, newIndex(right, n));
                right--;
            } else {
                i++;
            }
        }
    }

    private int findKthSmallest(int[] arr, int k) {
        java.util.Random rand = new java.util.Random();
        int left = 0, right = arr.length - 1;
        while (true) {
            if (left == right) return arr[left];
            int pivotIdx = left + rand.nextInt(right - left + 1);
            pivotIdx = partition(arr, left, right, pivotIdx);
            if (k == pivotIdx) {
                return arr[k];
            } else if (k < pivotIdx) {
                right = pivotIdx - 1;
            } else {
                left = pivotIdx + 1;
            }
        }
    }

    private int partition(int[] arr, int left, int right, int pivotIdx) {
        int pivotVal = arr[pivotIdx];
        swap(arr, pivotIdx, right);
        int storeIdx = left;
        for (int i = left; i < right; i++) {
            if (arr[i] <= pivotVal) {
                swap(arr, storeIdx, i);
                storeIdx++;
            }
        }
        swap(arr, storeIdx, right);
        return storeIdx;
    }

    private int newIndex(int idx, int n) {
        return (1 + 2 * idx) % (n | 1);
    }

    private void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

## Python

```python
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # Find median
        mid = sorted(nums)[n // 2]

        # Virtual index mapping
        def idx(i):
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1
        while i <= right:
            vi = idx(i)
            if nums[vi] > mid:
                vleft = idx(left)
                nums[vi], nums[vleft] = nums[vleft], nums[vi]
                left += 1
                i += 1
            elif nums[vi] < mid:
                vright = idx(right)
                nums[vi], nums[vright] = nums[vright], nums[vi]
                right -= 1
            else:
                i += 1
```

## Python3

```python
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        median = sorted(nums)[n // 2]

        def idx(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1
        while i <= right:
            cur = nums[idx(i)]
            if cur > median:
                l_idx = idx(left)
                r_idx = idx(i)
                nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
                left += 1
                i += 1
            elif cur < median:
                r_idx = idx(right)
                nums[idx(i)], nums[r_idx] = nums[r_idx], nums[idx(i)]
                right -= 1
            else:
                i += 1
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

void wiggleSort(int* nums, int numsSize) {
    if (numsSize <= 1) return;

    /* Find median */
    int *tmp = (int *)malloc(numsSize * sizeof(int));
    memcpy(tmp, nums, numsSize * sizeof(int));
    qsort(tmp, numsSize, sizeof(int), cmp_int);
    int median = tmp[numsSize / 2];
    free(tmp);

    int n = numsSize;
    int left = 0, i = 0, right = n - 1;

    #define IDX(k) ((1 + 2 * (k)) % (n | 1))
    #define VAL(k) nums[IDX(k)]

    while (i <= right) {
        if (VAL(i) > median) {
            int t = VAL(left);
            VAL(left) = VAL(i);
            VAL(i) = t;
            left++;
            i++;
        } else if (VAL(i) < median) {
            int t = VAL(right);
            VAL(right) = VAL(i);
            VAL(i) = t;
            right--;
        } else {
            i++;
        }
    }

    #undef IDX
    #undef VAL
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly System.Random _rand = new System.Random();

    public void WiggleSort(int[] nums)
    {
        int n = nums.Length;
        // Find median using quickselect on a copy to avoid modifying original order prematurely
        int[] copy = (int[])nums.Clone();
        int median = QuickSelect(copy, 0, n - 1, n / 2);

        int left = 0, i = 0, right = n - 1;
        int mask = n | 1; // ensures odd number for mapping

        while (i <= right)
        {
            int vi = VirtualIndex(i, mask);
            if (nums[vi] > median)
            {
                int vleft = VirtualIndex(left, mask);
                Swap(nums, vi, vleft);
                left++;
                i++;
            }
            else if (nums[vi] < median)
            {
                int vright = VirtualIndex(right, mask);
                Swap(nums, vi, vright);
                right--;
            }
            else
            {
                i++;
            }
        }
    }

    private static int VirtualIndex(int index, int mask)
    {
        // (1 + 2*index) % mask gives the required mapping
        return (1 + 2 * index) % mask;
    }

    private static void Swap(int[] arr, int i, int j)
    {
        if (i == j) return;
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    // Quickselect to find the k-th smallest element (0-indexed)
    private static int QuickSelect(int[] nums, int left, int right, int k)
    {
        while (true)
        {
            if (left == right) return nums[left];

            int pivotIndex = left + _rand.Next(right - left + 1);
            pivotIndex = Partition(nums, left, right, pivotIndex);

            if (k == pivotIndex)
                return nums[k];
            else if (k < pivotIndex)
                right = pivotIndex - 1;
            else
                left = pivotIndex + 1;
        }
    }

    private static int Partition(int[] nums, int left, int right, int pivotIndex)
    {
        int pivotValue = nums[pivotIndex];
        Swap(nums, pivotIndex, right);
        int storeIndex = left;

        for (int i = left; i < right; i++)
        {
            if (nums[i] < pivotValue)
            {
                Swap(nums, storeIndex, i);
                storeIndex++;
            }
        }

        Swap(nums, storeIndex, right);
        return storeIndex;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    const n = nums.length;
    // Find median using sorting (O(n log n))
    const sorted = [...nums].sort((a, b) => a - b);
    const median = sorted[Math.floor((n - 1) / 2)];
    
    // Virtual index mapping
    const mapIdx = i => (1 + 2 * i) % (n | 1);
    
    let left = 0, i = 0, right = n - 1;
    while (i <= right) {
        const vi = mapIdx(i);
        if (nums[vi] > median) {
            const vleft = mapIdx(left);
            [nums[vi], nums[vleft]] = [nums[vleft], nums[vi]];
            left++;
            i++;
        } else if (nums[vi] < median) {
            const vright = mapIdx(right);
            [nums[vi], nums[vright]] = [nums[vright], nums[vi]];
            right--;
        } else {
            i++;
        }
    }
};
```

## Typescript

```typescript
function wiggleSort(nums: number[]): void {
    const n = nums.length;
    if (n <= 1) return;

    const median = findKthSmallest(nums, Math.floor((n - 1) / 2));

    const mapIdx = (i: number): number => (1 + 2 * i) % (n | 1);

    let left = 0,
        i = 0,
        right = n - 1;
    while (i <= right) {
        const vi = mapIdx(i);
        if (nums[vi] > median) {
            const vleft = mapIdx(left);
            swap(nums, vleft, vi);
            left++;
            i++;
        } else if (nums[vi] < median) {
            const vright = mapIdx(right);
            swap(nums, vi, vright);
            right--;
        } else {
            i++;
        }
    }

    function swap(arr: number[], a: number, b: number): void {
        const tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    function findKthSmallest(arr: number[], k: number): number {
        let left = 0,
            right = arr.length - 1;
        while (true) {
            if (left === right) return arr[left];
            const pivotIdx = randomInt(left, right);
            const newPivotIdx = partition(arr, left, right, pivotIdx);
            if (k === newPivotIdx) {
                return arr[k];
            } else if (k < newPivotIdx) {
                right = newPivotIdx - 1;
            } else {
                left = newPivotIdx + 1;
            }
        }
    }

    function partition(arr: number[], left: number, right: number, pivotIdx: number): number {
        const pivotVal = arr[pivotIdx];
        swap(arr, pivotIdx, right);
        let store = left;
        for (let i = left; i < right; i++) {
            if (arr[i] < pivotVal) {
                swap(arr, store, i);
                store++;
            }
        }
        swap(arr, store, right);
        return store;
    }

    function randomInt(min: number, max: number): number {
        return Math.floor(Math.random() * (max - min + 1)) + min;
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
    function wiggleSort(&$nums) {
        $n = count($nums);
        if ($n <= 1) return;
        $sorted = $nums;
        sort($sorted);
        $median = $sorted[intdiv($n, 2)];
        $left = 0;
        $i = 0;
        $right = $n - 1;
        $mask = $n | 1; // ensure odd for mapping
        while ($i <= $right) {
            $mappedI = (1 + 2 * $i) % $mask;
            if ($nums[$mappedI] > $median) {
                $mappedLeft = (1 + 2 * $left) % $mask;
                $tmp = $nums[$mappedI];
                $nums[$mappedI] = $nums[$mappedLeft];
                $nums[$mappedLeft] = $tmp;
                $left++;
                $i++;
            } elseif ($nums[$mappedI] < $median) {
                $mappedRight = (1 + 2 * $right) % $mask;
                $tmp = $nums[$mappedI];
                $nums[$mappedI] = $nums[$mappedRight];
                $nums[$mappedRight] = $tmp;
                $right--;
            } else {
                $i++;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func wiggleSort(_ nums: inout [Int]) {
        let n = nums.count
        if n <= 1 { return }
        var copy = nums
        let median = quickSelect(&copy, n / 2)
        
        var i = 0, j = 0, k = n - 1
        func mappedIndex(_ idx: Int) -> Int {
            return (1 + 2 * idx) % (n | 1)
        }
        
        while j <= k {
            let vi = mappedIndex(j)
            if nums[vi] > median {
                let vI = mappedIndex(i)
                nums.swapAt(vI, vi)
                i += 1
                j += 1
            } else if nums[vi] < median {
                let vk = mappedIndex(k)
                nums.swapAt(vi, vk)
                k -= 1
            } else {
                j += 1
            }
        }
    }
    
    private func quickSelect(_ nums: inout [Int], _ k: Int) -> Int {
        var left = 0
        var right = nums.count - 1
        while true {
            if left == right { return nums[left] }
            let pivotIdx = partition(&nums, left, right)
            if k == pivotIdx {
                return nums[k]
            } else if k < pivotIdx {
                right = pivotIdx - 1
            } else {
                left = pivotIdx + 1
            }
        }
    }
    
    private func partition(_ nums: inout [Int], _ left: Int, _ right: Int) -> Int {
        let randomPivot = Int.random(in: left...right)
        nums.swapAt(randomPivot, right)
        let pivot = nums[right]
        var store = left
        for i in left..<right {
            if nums[i] < pivot {
                nums.swapAt(store, i)
                store += 1
            }
        }
        nums.swapAt(store, right)
        return store
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wiggleSort(nums: IntArray) {
        val n = nums.size
        if (n <= 1) return

        // Find median using sorting (O(n log n))
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val median = sorted[n / 2]

        fun newIndex(idx: Int): Int = (1 + 2 * idx) % (n or 1)

        var left = 0
        var i = 0
        var right = n - 1

        while (i <= right) {
            val mappedIdx = newIndex(i)
            when {
                nums[mappedIdx] > median -> {
                    // swap with element at virtual left
                    val li = newIndex(left)
                    val tmp = nums[li]
                    nums[li] = nums[mappedIdx]
                    nums[mappedIdx] = tmp
                    left++
                    i++
                }
                nums[mappedIdx] < median -> {
                    // swap with element at virtual right
                    val ri = newIndex(right)
                    val tmp = nums[mappedIdx]
                    nums[mappedIdx] = nums[ri]
                    nums[ri] = tmp
                    right--
                }
                else -> {
                    i++
                }
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void wiggleSort(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return;

    List<int> sorted = List.from(nums);
    sorted.sort();
    int median = sorted[n ~/ 2];

    int newIndex(int i) => (1 + 2 * i) % (n | 1);

    int left = 0, i = 0, right = n - 1;
    while (i <= right) {
      int vi = newIndex(i);
      if (nums[vi] > median) {
        int vleft = newIndex(left);
        int tmp = nums[vi];
        nums[vi] = nums[vleft];
        nums[vleft] = tmp;
        left++;
        i++;
      } else if (nums[vi] < median) {
        int vright = newIndex(right);
        int tmp = nums[vi];
        nums[vi] = nums[vright];
        nums[vright] = tmp;
        right--;
      } else {
        i++;
      }
    }
  }
}
```

## Golang

```go
import "sort"

func wiggleSort(nums []int) {
	n := len(nums)
	if n <= 1 {
		return
	}
	// Find median by sorting a copy.
	tmp := make([]int, n)
	copy(tmp, nums)
	sort.Ints(tmp)
	median := tmp[n/2]

	// Virtual index mapping.
	newIdx := func(i int) int { return (1 + 2*i) % (n | 1) }

	left, i, right := 0, 0, n-1
	for i <= right {
		idx := newIdx(i)
		if nums[idx] > median {
			lidx := newIdx(left)
			nums[lidx], nums[idx] = nums[idx], nums[lidx]
			left++
			i++
		} else if nums[idx] < median {
			ridx := newIdx(right)
			nums[ridx], nums[idx] = nums[idx], nums[ridx]
			right--
		} else {
			i++
		}
	}
}
```

## Ruby

```ruby
def wiggle_sort(nums)
  n = nums.length
  return if n <= 1

  median = nums.sort[n / 2]

  index_map = ->(i) { (1 + 2 * i) % (n | 1) }

  left = 0
  i = 0
  right = n - 1

  while i <= right
    vi = index_map.call(i)
    if nums[vi] > median
      vleft = index_map.call(left)
      nums[vi], nums[vleft] = nums[vleft], nums[vi]
      left += 1
      i += 1
    elsif nums[vi] < median
      vright = index_map.call(right)
      nums[vi], nums[vright] = nums[vright], nums[vi]
      right -= 1
    else
      i += 1
    end
  end
end
```

## Scala

```scala
object Solution {
    def wiggleSort(nums: Array[Int]): Unit = {
        val n = nums.length
        if (n <= 1) return

        // Find median using sorting (O(n log n))
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val median = sorted(n / 2)

        // Virtual index mapping
        def newIndex(i: Int): Int = ((1 + 2 * i) % (n | 1))

        var left = 0
        var i = 0
        var right = n - 1

        while (i <= right) {
            val idx = newIndex(i)
            if (nums(idx) > median) {
                val lIdx = newIndex(left)
                val tmp = nums(lIdx)
                nums(lIdx) = nums(idx)
                nums(idx) = tmp
                left += 1
                i += 1
            } else if (nums(idx) < median) {
                val rIdx = newIndex(right)
                val tmp = nums(rIdx)
                nums(rIdx) = nums(idx)
                nums(idx) = tmp
                right -= 1
            } else {
                i += 1
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn wiggle_sort(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n <= 1 {
            return;
        }
        // Find median using quickselect (select_nth_unstable)
        let mut copy = nums.clone();
        let mid = n / 2;
        copy.select_nth_unstable(mid);
        let median = copy[mid];

        // Virtual index mapping
        let new_index = |i: usize| -> usize { (1 + 2 * i) % (n | 1) };

        let mut left = 0usize;
        let mut i = 0usize;
        let mut right = n - 1;

        while i <= right {
            let vi = new_index(i);
            if nums[vi] > median {
                let vleft = new_index(left);
                nums.swap(vleft, vi);
                left += 1;
                i += 1;
            } else if nums[vi] < median {
                let vright = new_index(right);
                nums.swap(vi, vright);
                if right == 0 {
                    break;
                }
                right -= 1;
            } else {
                i += 1;
            }
        }
    }
}
```
