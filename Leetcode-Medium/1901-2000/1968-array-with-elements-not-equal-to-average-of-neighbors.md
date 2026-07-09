# 1968. Array With Elements Not Equal to Average of Neighbors

## Cpp

```cpp
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int mid = (n + 1) / 2;
        vector<int> ans;
        ans.reserve(n);
        for (int i = 0; i < mid; ++i) {
            ans.push_back(nums[i]);
            if (i + mid < n) ans.push_back(nums[i + mid]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        int[] res = new int[n];
        int mid = n / 2;
        int evenIdx = 0;
        for (int i = mid; i < n; i++) {
            res[evenIdx] = sorted[i];
            evenIdx += 2;
        }
        int oddIdx = 1;
        for (int i = 0; i < mid; i++) {
            res[oddIdx] = sorted[i];
            oddIdx += 2;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        i = 0
        while i + 1 < n:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        return nums
```

## Python3

```python
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        res = [0] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[i // 2]
            else:
                res[i] = nums[mid + i // 2]
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

/**
 * Rearrange the array so that no element equals the average of its neighbors.
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int *res = (int *)malloc(numsSize * sizeof(int));
    int left = 0;
    int right = numsSize - 1;
    
    for (int i = 0; i < numsSize; ++i) {
        if ((i & 1) == 0) {          // even index: place larger elements
            res[i] = nums[right--];
        } else {                     // odd index: place smaller elements
            res[i] = nums[left++];
        }
    }
    
    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] RearrangeArray(int[] nums) {
        Array.Sort(nums);
        for (int i = 0; i + 1 < nums.Length; i += 2) {
            int tmp = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = tmp;
        }
        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const mid = Math.floor(n / 2);
    const res = [];
    let i = 0, j = mid;
    while (i < mid && j < n) {
        res.push(nums[i]);
        res.push(nums[j]);
        i++;
        j++;
    }
    while (i < mid) {
        res.push(nums[i++]);
    }
    while (j < n) {
        res.push(nums[j++]);
    }
    return res;
};
```

## Typescript

```typescript
function rearrangeArray(nums: number[]): number[] {
    nums.sort((a, b) => a - b);
    for (let i = 1; i + 1 < nums.length; i += 2) {
        const tmp = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = tmp;
    }
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
    function rearrangeArray($nums) {
        sort($nums, SORT_NUMERIC);
        $n = count($nums);
        $mid = intdiv($n, 2);
        $small = array_slice($nums, 0, $mid);
        $large = array_slice($nums, $mid);
        $res = [];
        for ($i = 0; $i < $mid; $i++) {
            $res[] = $large[$i];
            $res[] = $small[$i];
        }
        if (count($large) > $mid) {
            $res[] = $large[$mid];
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        var arr = nums.sorted()
        var i = 0
        while i + 1 < arr.count {
            arr.swapAt(i, i + 1)
            i += 2
        }
        return arr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rearrangeArray(nums: IntArray): IntArray {
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val n = sorted.size
        val mid = n / 2
        val res = IntArray(n)
        var idx = 0
        var i = 0
        var j = mid
        while (i < mid && j < n) {
            res[idx++] = sorted[i]
            if (idx < n) {
                res[idx++] = sorted[j]
            }
            i++
            j++
        }
        while (i < mid) {
            res[idx++] = sorted[i++]
        }
        while (j < n) {
            res[idx++] = sorted[j++]
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> rearrangeArray(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int mid = (n + 1) >> 1; // ceil(n/2)
    List<int> res = List.filled(n, 0);
    int idx = 0;
    int i = 0, j = mid;
    while (i < mid && j < n) {
      res[idx++] = nums[i++];
      if (idx < n) {
        res[idx++] = nums[j++];
      }
    }
    while (i < mid) {
      res[idx++] = nums[i++];
    }
    while (j < n) {
      res[idx++] = nums[j++];
    }
    return res;
  }
}
```

## Golang

```go
import "sort"

func rearrangeArray(nums []int) []int {
	sort.Ints(nums)
	n := len(nums)
	res := make([]int, n)
	i, j := 0, n/2
	for k := 0; k < n; k++ {
		if k%2 == 0 {
			res[k] = nums[i]
			i++
		} else {
			res[k] = nums[j]
			j++
		}
	}
	return res
}
```

## Ruby

```ruby
def rearrange_array(nums)
  nums.sort!
  n = nums.length
  mid = (n + 1) / 2
  left = nums[0...mid]
  right = nums[mid..-1] || []
  res = []
  i = 0
  while i < left.size || i < right.size
    res << left[i] if i < left.size
    res << right[i] if i < right.size
    i += 1
  end
  res
end
```

## Scala

```scala
object Solution {
    def rearrangeArray(nums: Array[Int]): Array[Int] = {
        val sorted = nums.sorted
        val n = sorted.length
        val res = new Array[Int](n)
        val mid = (n + 1) / 2
        var i = 0
        while (i < n) {
            if ((i & 1) == 0) {
                res(i) = sorted(i / 2)
            } else {
                res(i) = sorted(mid + i / 2)
            }
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rearrange_array(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let n = nums.len();
        let mid = n / 2;
        let mut res = vec![0; n];
        // place the smaller half at odd indices
        for i in 0..mid {
            res[2 * i + 1] = nums[i];
        }
        // place the larger half at even indices
        for i in 0..(n - mid) {
            res[2 * i] = nums[mid + i];
        }
        res
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (rearrange-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (k (quotient n 2))
         (small (take sorted k))
         (large (drop sorted k)))
    (let loop ((i 0) (s small) (l large) (acc '()))
      (if (= i n)
          (reverse acc)
          (if (odd? i)
              (loop (+ i 1) (rest s) l (cons (first s) acc))
              (loop (+ i 1) s (rest l) (cons (first l) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([rearrange_array/1]).

-spec rearrange_array([integer()]) -> [integer()].
rearrange_array(Nums) ->
    Sorted = lists:sort(Nums),
    swap_adjacent(Sorted).

swap_adjacent([]) -> [];
swap_adjacent([X]) -> [X];
swap_adjacent([A, B | Rest]) ->
    [B, A | swap_adjacent(Rest)].
```

## Elixir

```elixir
defmodule Solution do
  @spec rearrange_array(nums :: [integer]) :: [integer]
  def rearrange_array(nums) do
    nums
    |> Enum.sort()
    |> swap_pairs()
  end

  defp swap_pairs([a, b | rest]), do: [b, a | swap_pairs(rest)]
  defp swap_pairs([last]), do: [last]
  defp swap_pairs([]), do: []
end
```
