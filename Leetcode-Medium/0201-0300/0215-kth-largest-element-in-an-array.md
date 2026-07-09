# 0215. Kth Largest Element in an Array

## Cpp

```cpp
class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        int n = nums.size();
        int target = n - k; // index of kth largest in sorted order (0‑based)
        std::mt19937 gen((unsigned)std::chrono::steady_clock::now().time_since_epoch().count());
        int left = 0, right = n - 1;
        while (true) {
            std::uniform_int_distribution<int> dist(left, right);
            int pivotIdx = dist(gen);
            int newPivotIdx = partition(nums, left, right, pivotIdx);
            if (newPivotIdx == target) return nums[newPivotIdx];
            else if (newPivotIdx < target) left = newPivotIdx + 1;
            else right = newPivotIdx - 1;
        }
    }

private:
    int partition(std::vector<int>& a, int left, int right, int pivotIdx) {
        int pivotVal = a[pivotIdx];
        std::swap(a[pivotIdx], a[right]); // move pivot to end
        int storeIdx = left;
        for (int i = left; i < right; ++i) {
            if (a[i] < pivotVal) {
                std::swap(a[storeIdx], a[i]);
                ++storeIdx;
            }
        }
        std::swap(a[storeIdx], a[right]); // move pivot to its final place
        return storeIdx;
    }
};
```

## Java

```java
import java.util.Random;

class Solution {
    private final Random rand = new Random();

    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k; // index of kth largest in sorted order
        return quickSelect(nums, 0, nums.length - 1, target);
    }

    private int quickSelect(int[] a, int left, int right, int idx) {
        while (left <= right) {
            int pivotIdx = left + rand.nextInt(right - left + 1);
            int pivotVal = a[pivotIdx];
            swap(a, pivotIdx, right);
            int storeIdx = left;
            for (int i = left; i < right; i++) {
                if (a[i] < pivotVal) {
                    swap(a, storeIdx, i);
                    storeIdx++;
                }
            }
            swap(a, storeIdx, right);
            if (storeIdx == idx) {
                return a[storeIdx];
            } else if (storeIdx < idx) {
                left = storeIdx + 1;
            } else {
                right = storeIdx - 1;
            }
        }
        return -1; // should never reach here
    }

    private void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}
```

## Python

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
```

## Python3

```python
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[right] = nums[right], nums[store]

            if store == target:
                return nums[store]
            elif store < target:
                left = store + 1
            else:
                right = store - 1
```

## C

```c
#include <stdlib.h>

static void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

static int partition(int *arr, int left, int right) {
    int pivotIdx = left + rand() % (right - left + 1);
    int pivotVal = arr[pivotIdx];
    swap(&arr[pivotIdx], &arr[right]);
    int storeIdx = left;
    for (int i = left; i < right; ++i) {
        if (arr[i] < pivotVal) {
            swap(&arr[storeIdx], &arr[i]);
            ++storeIdx;
        }
    }
    swap(&arr[storeIdx], &arr[right]);
    return storeIdx;
}

int findKthLargest(int* nums, int numsSize, int k) {
    int target = numsSize - k;  // index of the kth largest in sorted order
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int idx = partition(nums, left, right);
        if (idx == target)
            return nums[idx];
        else if (idx < target)
            left = idx + 1;
        else
            right = idx - 1;
    }
    return -1; // should never reach here
}
```

## Csharp

```csharp
public class Solution
{
    private readonly System.Random _rand = new System.Random();

    public int FindKthLargest(int[] nums, int k)
    {
        int target = nums.Length - k;
        int left = 0, right = nums.Length - 1;

        while (true)
        {
            if (left == right) return nums[left];

            int pivotIndex = Partition(nums, left, right);
            if (pivotIndex == target) return nums[pivotIndex];
            else if (pivotIndex < target) left = pivotIndex + 1;
            else right = pivotIndex - 1;
        }
    }

    private int Partition(int[] nums, int left, int right)
    {
        int pivotIdx = left + _rand.Next(right - left + 1);
        int pivotVal = nums[pivotIdx];
        Swap(nums, pivotIdx, right);

        int storeIdx = left;
        for (int i = left; i < right; i++)
        {
            if (nums[i] < pivotVal)
            {
                Swap(nums, storeIdx, i);
                storeIdx++;
            }
        }

        Swap(nums, storeIdx, right);
        return storeIdx;
    }

    private void Swap(int[] nums, int i, int j)
    {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const target = nums.length - k; // index of kth largest in sorted order (0‑based)
    let left = 0, right = nums.length - 1;

    while (true) {
        if (left === right) return nums[left];

        // random pivot to avoid worst‑case
        const pivotIdx = Math.floor(Math.random() * (right - left + 1)) + left;
        const newPivotIdx = partition(nums, left, right, pivotIdx);

        if (newPivotIdx === target) {
            return nums[newPivotIdx];
        } else if (newPivotIdx < target) {
            left = newPivotIdx + 1;
        } else {
            right = newPivotIdx - 1;
        }
    }

    function partition(arr, l, r, idx) {
        const pivotVal = arr[idx];
        // move pivot to end
        [arr[idx], arr[r]] = [arr[r], arr[idx]];
        let store = l;
        for (let i = l; i < r; i++) {
            if (arr[i] < pivotVal) {
                [arr[store], arr[i]] = [arr[i], arr[store]];
                store++;
            }
        }
        // place pivot in its final position
        [arr[store], arr[r]] = [arr[r], arr[store]];
        return store;
    }
};
```

## Typescript

```typescript
function findKthLargest(nums: number[], k: number): number {
    const target = nums.length - k;
    let left = 0, right = nums.length - 1;

    while (true) {
        // Random pivot to improve average performance
        const pivotIdx = left + Math.floor(Math.random() * (right - left + 1));
        const newPivotIdx = partition(left, right, pivotIdx);
        if (newPivotIdx === target) return nums[newPivotIdx];
        else if (newPivotIdx < target) left = newPivotIdx + 1;
        else right = newPivotIdx - 1;
    }

    function partition(l: number, r: number, pIdx: number): number {
        const pivotVal = nums[pIdx];
        swap(pIdx, r);
        let store = l;
        for (let i = l; i < r; ++i) {
            if (nums[i] <= pivotVal) {
                swap(i, store);
                ++store;
            }
        }
        swap(store, r);
        return store;
    }

    function swap(i: number, j: number): void {
        const tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function findKthLargest($nums, $k) {
        $n = count($nums);
        $target = $n - $k; // convert to (n-k)-th smallest
        return $this->quickSelect($nums, 0, $n - 1, $target);
    }

    private function quickSelect(&$nums, $left, $right, $kSmallest) {
        if ($left == $right) {
            return $nums[$left];
        }
        $pivotIndex = mt_rand($left, $right);
        $pivotIndex = $this->partition($nums, $left, $right, $pivotIndex);
        if ($kSmallest == $pivotIndex) {
            return $nums[$kSmallest];
        } elseif ($kSmallest < $pivotIndex) {
            return $this->quickSelect($nums, $left, $pivotIndex - 1, $kSmallest);
        } else {
            return $this->quickSelect($nums, $pivotIndex + 1, $right, $kSmallest);
        }
    }

    private function partition(&$nums, $left, $right, $pivotIndex) {
        $pivot = $nums[$pivotIndex];
        // Move pivot to end
        $tmp = $nums[$pivotIndex];
        $nums[$pivotIndex] = $nums[$right];
        $nums[$right] = $tmp;

        $storeIndex = $left;
        for ($i = $left; $i < $right; $i++) {
            if ($nums[$i] < $pivot) {
                // Swap nums[storeIndex] and nums[i]
                $tmp = $nums[$storeIndex];
                $nums[$storeIndex] = $nums[$i];
                $nums[$i] = $tmp;
                $storeIndex++;
            }
        }

        // Move pivot to its final place
        $tmp = $nums[$storeIndex];
        $nums[$storeIndex] = $nums[$right];
        $nums[$right] = $tmp;

        return $storeIndex;
    }
}
```

## Swift

```swift
class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        var arr = nums
        let target = arr.count - k
        var left = 0
        var right = arr.count - 1
        
        while true {
            if left == right { return arr[left] }
            let pivotIndex = partition(&arr, left: left, right: right)
            if pivotIndex == target {
                return arr[pivotIndex]
            } else if pivotIndex < target {
                left = pivotIndex + 1
            } else {
                right = pivotIndex - 1
            }
        }
    }
    
    private func partition(_ nums: inout [Int], left: Int, right: Int) -> Int {
        let pivotIdx = Int.random(in: left...right)
        nums.swapAt(pivotIdx, right)
        let pivot = nums[right]
        var storeIndex = left
        for i in left..<right {
            if nums[i] < pivot {
                nums.swapAt(i, storeIndex)
                storeIndex += 1
            }
        }
        nums.swapAt(storeIndex, right)
        return storeIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        val target = nums.size - k
        var left = 0
        var right = nums.lastIndex
        while (true) {
            if (left == right) return nums[left]
            val pivotIdx = left + kotlin.random.Random.nextInt(right - left + 1)
            val newPivotIdx = partition(nums, left, right, pivotIdx)
            when {
                newPivotIdx == target -> return nums[newPivotIdx]
                newPivotIdx < target -> left = newPivotIdx + 1
                else -> right = newPivotIdx - 1
            }
        }
    }

    private fun partition(arr: IntArray, left: Int, right: Int, pivotIndex: Int): Int {
        val pivotValue = arr[pivotIndex]
        swap(arr, pivotIndex, right)
        var storeIndex = left
        for (i in left until right) {
            if (arr[i] < pivotValue) {
                swap(arr, storeIndex, i)
                storeIndex++
            }
        }
        swap(arr, storeIndex, right)
        return storeIndex
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  final Random _rand = Random();

  int findKthLargest(List<int> nums, int k) {
    int target = nums.length - k;
    int left = 0, right = nums.length - 1;
    while (true) {
      int pivotIndex = _partition(nums, left, right);
      if (pivotIndex == target) return nums[pivotIndex];
      if (pivotIndex < target) {
        left = pivotIndex + 1;
      } else {
        right = pivotIndex - 1;
      }
    }
  }

  int _partition(List<int> arr, int left, int right) {
    int pivotIdx = left + _rand.nextInt(right - left + 1);
    int pivotVal = arr[pivotIdx];
    // Move pivot to end
    int tmp = arr[pivotIdx];
    arr[pivotIdx] = arr[right];
    arr[right] = tmp;

    int storeIndex = left;
    for (int i = left; i < right; i++) {
      if (arr[i] < pivotVal) {
        int t = arr[i];
        arr[i] = arr[storeIndex];
        arr[storeIndex] = t;
        storeIndex++;
      }
    }

    // Move pivot to its final place
    tmp = arr[storeIndex];
    arr[storeIndex] = arr[right];
    arr[right] = tmp;

    return storeIndex;
  }
}
```

## Golang

```go
import (
	"math/rand"
	"time"
)

func findKthLargest(nums []int, k int) int {
	n := len(nums)
	target := n - k

	rand.Seed(time.Now().UnixNano())
	left, right := 0, n-1
	for {
		if left == right {
			return nums[left]
		}
		pivotIdx := left + rand.Intn(right-left+1)
		nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]

		i := left
		for j := left; j < right; j++ {
			if nums[j] <= nums[right] {
				nums[i], nums[j] = nums[j], nums[i]
				i++
			}
		}
		nums[i], nums[right] = nums[right], nums[i]

		if i == target {
			return nums[i]
		} else if i < target {
			left = i + 1
		} else {
			right = i - 1
		}
	}
}
```

## Ruby

```ruby
def find_kth_largest(nums, k)
  target = nums.length - k
  left = 0
  right = nums.length - 1
  loop do
    pivot_index = rand(left..right)
    new_pivot = partition_(nums, left, right, pivot_index)
    return nums[new_pivot] if new_pivot == target
    if new_pivot < target
      left = new_pivot + 1
    else
      right = new_pivot - 1
    end
  end
end

def partition_(nums, left, right, pivot_index)
  pivot_value = nums[pivot_index]
  nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
  store_index = left
  i = left
  while i < right
    if nums[i] < pivot_value
      nums[store_index], nums[i] = nums[i], nums[store_index]
      store_index += 1
    end
    i += 1
  end
  nums[right], nums[store_index] = nums[store_index], nums[right]
  store_index
end
```

## Scala

```scala
object Solution {
  import scala.util.Random

  private def swap(arr: Array[Int], i: Int, j: Int): Unit = {
    val tmp = arr(i)
    arr(i) = arr(j)
    arr(j) = tmp
  }

  def findKthLargest(nums: Array[Int], k: Int): Int = {
    var left = 0
    var right = nums.length - 1
    val target = nums.length - k
    val rand = new Random()
    while (left <= right) {
      val pivotIdx = left + rand.nextInt(right - left + 1)
      val pivotVal = nums(pivotIdx)
      swap(nums, pivotIdx, right)
      var storeIdx = left
      var i = left
      while (i < right) {
        if (nums(i) < pivotVal) {
          swap(nums, storeIdx, i)
          storeIdx += 1
        }
        i += 1
      }
      swap(nums, storeIdx, right)

      if (storeIdx == target) return nums(storeIdx)
      else if (storeIdx < target) left = storeIdx + 1
      else right = storeIdx - 1
    }
    Int.MinValue
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        let n = nums.len();
        let target = n - k as usize;
        quickselect(&mut nums, 0, n - 1, target);
        nums[target]
    }
}

fn quickselect(nums: &mut Vec<i32>, mut left: usize, mut right: usize, kth: usize) {
    while left <= right {
        let pivot_index = partition(nums, left, right);
        if pivot_index == kth {
            return;
        } else if pivot_index < kth {
            left = pivot_index + 1;
        } else {
            if pivot_index == 0 { break; }
            right = pivot_index - 1;
        }
    }
}

fn partition(nums: &mut Vec<i32>, left: usize, right: usize) -> usize {
    let pivot = nums[right];
    let mut i = left;
    for j in left..right {
        if nums[j] <= pivot {
            nums.swap(i, j);
            i += 1;
        }
    }
    nums.swap(i, right);
    i
}
```

## Racket

```racket
(define/contract (find-kth-largest nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (target (- n k))               ; index of kth largest in ascending order
         (vec (list->vector nums)))
    (define (swap! i j)
      (let ((tmp (vector-ref vec i)))
        (vector-set! vec i (vector-ref vec j))
        (vector-set! vec j tmp)))
    (define (partition lo hi)
      (let* ((pivot-index (+ lo (random (add1 (- hi lo))))) ; random index in [lo,hi]
             (pivot-val (vector-ref vec pivot-index)))
        (swap! pivot-index hi)               ; move pivot to end
        (let loop ((i lo) (store lo))
          (if (= i hi)
              (begin
                (swap! store hi)            ; place pivot in its final position
                store)
              (if (<= (vector-ref vec i) pivot-val)
                  (begin
                    (swap! i store)
                    (loop (+ i 1) (+ store 1)))
                  (loop (+ i 1) store))))))
    (let rec ((lo 0) (hi (sub1 n)))
      (let ((p (partition lo hi)))
        (cond [(= p target) (vector-ref vec p)]
              [(< p target) (rec (+ p 1) hi)]
              [else          (rec lo (- p 1))])))))
```

## Erlang

```erlang
-module(solution).
-export([find_kth_largest/2]).

-spec find_kth_largest(Nums :: [integer()], K :: integer()) -> integer().
find_kth_largest(Nums, K) ->
    Sorted = lists:sort(Nums),
    Index = length(Sorted) - K + 1,
    lists:nth(Index, Sorted).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_kth_largest(nums :: [integer], k :: integer) :: integer
  def find_kth_largest(nums, k) do
    nums
    |> Enum.sort(&>=/2)
    |> Enum.at(k - 1)
  end
end
```
