# 0912. Sort an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if (nums.empty()) return nums;
        mt19937 rng((unsigned)chrono::steady_clock::now().time_since_epoch().count());
        quickSort(nums, 0, (int)nums.size() - 1, rng);
        return nums;
    }
private:
    void quickSort(vector<int>& a, int l, int r, mt19937& rng) {
        while (l < r) {
            // random pivot
            int pivotIdx = uniform_int_distribution<int>(l, r)(rng);
            int pivot = a[pivotIdx];
            int i = l, j = r;
            while (i <= j) {
                while (a[i] < pivot) ++i;
                while (a[j] > pivot) --j;
                if (i <= j) {
                    swap(a[i], a[j]);
                    ++i; --j;
                }
            }
            // recurse on smaller partition first to keep stack depth O(log n)
            if (j - l < r - i) {
                quickSort(a, l, j, rng);
                l = i;
            } else {
                quickSort(a, i, r, rng);
                r = j;
            }
        }
    }
};
```

## Java

```java
class Solution {
    private final java.util.Random rand = new java.util.Random();
    
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void quickSort(int[] a, int lo, int hi) {
        if (lo < hi) {
            int p = partition(a, lo, hi);
            quickSort(a, lo, p - 1);
            quickSort(a, p + 1, hi);
        }
    }
    
    private int partition(int[] a, int lo, int hi) {
        int pivotIdx = lo + rand.nextInt(hi - lo + 1);
        swap(a, pivotIdx, hi);
        int pivot = a[hi];
        int i = lo;
        for (int j = lo; j < hi; j++) {
            if (a[j] <= pivot) {
                swap(a, i, j);
                i++;
            }
        }
        swap(a, i, hi);
        return i;
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
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        import random
        # Shuffle to guarantee average O(n log n)
        random.shuffle(nums)

        def quicksort(l, r):
            while l < r:
                i, j = l, r
                pivot = nums[l + (r - l) // 2]
                while i <= j:
                    while nums[i] < pivot:
                        i += 1
                    while nums[j] > pivot:
                        j -= 1
                    if i <= j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1
                # Recurse on smaller partition first to keep stack depth O(log n)
                if j - l < r - i:
                    quicksort(l, j)
                    l = i
                else:
                    quicksort(i, r)
                    r = j

        quicksort(0, len(nums) - 1)
        return nums
```

## Python3

```python
from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [(0, n - 1)]
        while stack:
            l, r = stack.pop()
            if l >= r:
                continue
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            left_size = i - 1 - l
            right_size = r - (i + 1)
            if left_size > right_size:
                stack.append((l, i - 1))
                stack.append((i + 1, r))
            else:
                stack.append((i + 1, r))
                stack.append((l, i - 1))
        return nums
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void heapify(int *arr, int n, int i) {
    while (1) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest != i) {
            int tmp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = tmp;
            i = largest;
        } else {
            break;
        }
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    if (numsSize == 0) return NULL;

    int *arr = (int *)malloc(numsSize * sizeof(int));
    if (!arr) return NULL;
    memcpy(arr, nums, numsSize * sizeof(int));

    // Build max heap
    for (int i = numsSize / 2 - 1; i >= 0; --i) {
        heapify(arr, numsSize, i);
    }

    // Heap sort
    for (int end = numsSize - 1; end > 0; --end) {
        int tmp = arr[0];
        arr[0] = arr[end];
        arr[end] = tmp;
        heapify(arr, end, 0);
    }
    return arr;
}
```

## Csharp

```csharp
public class Solution {
    private static readonly System.Random rng = new System.Random();

    public int[] SortArray(int[] nums) {
        if (nums == null || nums.Length <= 1) return nums;
        QuickSort(nums, 0, nums.Length - 1);
        return nums;
    }

    private void QuickSort(int[] arr, int left, int right) {
        while (left < right) {
            int pivotIndex = Partition(arr, left, right);
            // Recurse on smaller partition first to keep stack depth O(log n)
            if (pivotIndex - left < right - pivotIndex) {
                QuickSort(arr, left, pivotIndex - 1);
                left = pivotIndex + 1;
            } else {
                QuickSort(arr, pivotIndex + 1, right);
                right = pivotIndex - 1;
            }
        }
    }

    private int Partition(int[] arr, int left, int right) {
        // Randomly choose a pivot and move it to the end
        int pivotIdx = left + rng.Next(right - left + 1);
        Swap(arr, pivotIdx, right);
        int pivot = arr[right];
        int i = left;
        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                Swap(arr, i, j);
                i++;
            }
        }
        Swap(arr, i, right);
        return i;
    }

    private void Swap(int[] arr, int i, int j) {
        if (i == j) return;
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    if (nums.length <= 1) return nums;
    
    const quickSort = (arr, left, right) => {
        while (left < right) {
            const pivotIdx = partition(arr, left, right);
            // Recurse on smaller subarray first to keep stack depth O(log n)
            if (pivotIdx - left < right - pivotIdx) {
                quickSort(arr, left, pivotIdx - 1);
                left = pivotIdx + 1;
            } else {
                quickSort(arr, pivotIdx + 1, right);
                right = pivotIdx - 1;
            }
        }
    };
    
    const partition = (arr, left, right) => {
        // Randomized pivot to avoid worst‑case
        const randIdx = left + Math.floor(Math.random() * (right - left + 1));
        [arr[left], arr[randIdx]] = [arr[randIdx], arr[left]];
        const pivot = arr[left];
        let i = left + 1;
        for (let j = left + 1; j <= right; ++j) {
            if (arr[j] < pivot) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
                ++i;
            }
        }
        // Place pivot in its final position
        [arr[left], arr[i - 1]] = [arr[i - 1], arr[left]];
        return i - 1;
    };
    
    quickSort(nums, 0, nums.length - 1);
    return nums;
};
```

## Typescript

```typescript
function sortArray(nums: number[]): number[] {
    const n = nums.length;
    if (n <= 1) return nums;

    const swap = (i: number, j: number): void => {
        const tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    };

    const quickSort = (left: number, right: number): void => {
        if (left >= right) return;

        // Random pivot to avoid worst‑case
        const pivotIdx = left + Math.floor(Math.random() * (right - left + 1));
        swap(left, pivotIdx);
        const pivot = nums[left];

        let i = left + 1;
        let j = right;

        while (true) {
            while (i <= right && nums[i] <= pivot) i++;
            while (j >= left + 1 && nums[j] > pivot) j--;
            if (i > j) break;
            swap(i, j);
        }

        swap(left, j);

        quickSort(left, j - 1);
        quickSort(j + 1, right);
    };

    quickSort(0, n - 1);
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortArray($nums) {
        if (empty($nums)) return $nums;
        $this->quickSort($nums, 0, count($nums) - 1);
        return $nums;
    }

    private function quickSort(&$arr, $left, $right) {
        if ($left >= $right) {
            return;
        }
        // Random pivot selection
        $pivotIndex = rand($left, $right);
        $pivot = $arr[$pivotIndex];
        // Move pivot to end
        $tmp = $arr[$pivotIndex];
        $arr[$pivotIndex] = $arr[$right];
        $arr[$right] = $tmp;

        $storeIndex = $left;
        for ($i = $left; $i < $right; $i++) {
            if ($arr[$i] < $pivot) {
                // swap arr[i] and arr[storeIndex]
                $t = $arr[$i];
                $arr[$i] = $arr[$storeIndex];
                $arr[$storeIndex] = $t;
                $storeIndex++;
            }
        }
        // Move pivot to its final place
        $t = $arr[$storeIndex];
        $arr[$storeIndex] = $arr[$right];
        $arr[$right] = $t;

        $this->quickSort($arr, $left, $storeIndex - 1);
        $this->quickSort($arr, $storeIndex + 1, $right);
    }
}
```

## Swift

```swift
class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        var arr = nums
        if !arr.isEmpty {
            quickSort(&arr, 0, arr.count - 1)
        }
        return arr
    }
    
    private func quickSort(_ nums: inout [Int], _ left: Int, _ right: Int) {
        if left >= right { return }
        let pivotIdx = Int.random(in: left...right)
        nums.swapAt(pivotIdx, right)
        let pivot = nums[right]
        var i = left
        for j in left..<right {
            if nums[j] < pivot {
                nums.swapAt(i, j)
                i += 1
            }
        }
        nums.swapAt(i, right)
        quickSort(&nums, left, i - 1)
        quickSort(&nums, i + 1, right)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortArray(nums: IntArray): IntArray {
        if (nums.size > 1) quickSort(nums, 0, nums.lastIndex)
        return nums
    }

    private fun quickSort(arr: IntArray, low: Int, high: Int) {
        var left = low
        var right = high
        val pivot = arr[low + (high - low) / 2]
        while (left <= right) {
            while (arr[left] < pivot) left++
            while (arr[right] > pivot) right--
            if (left <= right) {
                val tmp = arr[left]
                arr[left] = arr[right]
                arr[right] = tmp
                left++
                right--
            }
        }
        if (low < right) quickSort(arr, low, right)
        if (left < high) quickSort(arr, left, high)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<int> sortArray(List<int> nums) {
    _quickSort(nums, 0, nums.length - 1);
    return nums;
  }

  void _quickSort(List<int> arr, int left, int right) {
    if (left >= right) return;

    // Randomized pivot selection
    int pivotIdx = left + Random().nextInt(right - left + 1);
    int pivot = arr[pivotIdx];

    // Move pivot to end
    _swap(arr, pivotIdx, right);

    int storeIdx = left;
    for (int i = left; i < right; i++) {
      if (arr[i] < pivot) {
        _swap(arr, i, storeIdx);
        storeIdx++;
      }
    }

    // Place pivot in its final position
    _swap(arr, storeIdx, right);

    _quickSort(arr, left, storeIdx - 1);
    _quickSort(arr, storeIdx + 1, right);
  }

  void _swap(List<int> arr, int i, int j) {
    if (i == j) return;
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}
```

## Golang

```go
import (
	"math/rand"
	"time"
)

func sortArray(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	rand.Seed(time.Now().UnixNano())
	quickSort(nums, 0, len(nums)-1)
	return nums
}

func quickSort(a []int, left, right int) {
	if left >= right {
		return
	}
	// Random pivot selection
	pivotIdx := left + rand.Intn(right-left+1)
	a[left], a[pivotIdx] = a[pivotIdx], a[left]
	pivot := a[left]

	i, j := left+1, right
	for i <= j {
		if a[i] <= pivot {
			i++
		} else {
			a[i], a[j] = a[j], a[i]
			j--
		}
	}
	// Place pivot in its final position
	a[left], a[j] = a[j], a[left]

	quickSort(a, left, j-1)
	quickSort(a, j+1, right)
}
```

## Ruby

```ruby
def quick_sort(arr, left, right)
  return if left >= right
  pivot_index = rand(left..right)
  arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
  i = left
  (left...right).each do |j|
    if arr[j] <= arr[right]
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
    end
  end
  arr[i], arr[right] = arr[right], arr[i]
  quick_sort(arr, left, i - 1)
  quick_sort(arr, i + 1, right)
end

def sort_array(nums)
  quick_sort(nums, 0, nums.length - 1) if nums && !nums.empty?
  nums
end
```

## Scala

```scala
object Solution {
    def sortArray(nums: Array[Int]): Array[Int] = {
        import scala.util.Random
        val rnd = new Random()
        def swap(i: Int, j: Int): Unit = {
            val tmp = nums(i)
            nums(i) = nums(j)
            nums(j) = tmp
        }
        def quickSort(l: Int, r: Int): Unit = {
            if (l < r) {
                val pivotIdx = l + rnd.nextInt(r - l + 1)
                swap(pivotIdx, r)
                val pivot = nums(r)
                var i = l
                for (j <- l until r) {
                    if (nums(j) <= pivot) {
                        swap(i, j)
                        i += 1
                    }
                }
                swap(i, r)
                quickSort(l, i - 1)
                quickSort(i + 1, r)
            }
        }
        quickSort(0, nums.length - 1)
        nums
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        fn quick_sort(arr: &mut [i32]) {
            let len = arr.len();
            if len <= 1 {
                return;
            }
            let mut i: usize = 0;
            let mut j: usize = len - 1;
            let pivot = arr[len / 2];
            while i <= j {
                while arr[i] < pivot {
                    i += 1;
                }
                while arr[j] > pivot {
                    if j == 0 {
                        break;
                    }
                    j -= 1;
                }
                if i <= j {
                    arr.swap(i, j);
                    i += 1;
                    if j == 0 {
                        break;
                    }
                    j -= 1;
                }
            }
            if j > 0 {
                quick_sort(&mut arr[0..=j]);
            }
            quick_sort(&mut arr[i..len]);
        }

        let mut v = nums;
        quick_sort(&mut v);
        v
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (sort-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (letrec ((merge
            (lambda (left right)
              (cond [(null? left) right]
                    [(null? right) left]
                    [else (if (<= (car left) (car right))
                              (cons (car left) (merge (cdr left) right))
                              (cons (car right) (merge left (cdr right))))])))
           (merge-sort
            (lambda (lst)
              (if (or (null? lst) (null? (cdr lst)))
                  lst
                  (let* ((len (length lst))
                         (mid (quotient len 2))
                         (left (take lst mid))
                         (right (drop lst mid)))
                    (merge (merge-sort left) (merge-sort right)))))))
    (merge-sort nums)))
```

## Erlang

```erlang
-spec sort_array(Nums :: [integer()]) -> [integer()].
sort_array(Nums) ->
    merge_sort(Nums).

merge_sort([]) -> [];
merge_sort([X]) -> [X];
merge_sort(L) ->
    {Left, Right} = split(L),
    merge(merge_sort(Left), merge_sort(Right)).

split(List) ->
    split(List, [], []).

split([], LAcc, RAcc) ->
    {lists:reverse(LAcc), lists:reverse(RAcc)};
split([X], LAcc, RAcc) ->
    {lists:reverse([X|LAcc]), lists:reverse(RAcc)};
split([X,Y|Rest], LAcc, RAcc) ->
    split(Rest, [X|LAcc], [Y|RAcc]).

merge([], R) -> R;
merge(L, []) -> L;
merge([H1|T1]=L1, [H2|T2]=R1) when H1 =< H2 ->
    [H1 | merge(T1, R1)];
merge(L1, [H2|T2]) ->
    [H2 | merge(L1, T2)].
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_array(nums :: [integer]) :: [integer]
  def sort_array(nums) do
    merge_sort(nums)
  end

  defp merge_sort([]), do: []
  defp merge_sort([_]=list), do: list
  defp merge_sort(list) do
    len = length(list)
    if len <= 1 do
      list
    else
      mid = div(len, 2)
      {left, right} = :lists.split(mid, list)
      merge(merge_sort(left), merge_sort(right))
    end
  end

  defp merge([], r), do: r
  defp merge(l, []), do: l
  defp merge([h1 | t1] = left, [h2 | t2] = right) do
    if h1 <= h2 do
      [h1 | merge(t1, right)]
    else
      [h2 | merge(left, t2)]
    end
  end
end
```
