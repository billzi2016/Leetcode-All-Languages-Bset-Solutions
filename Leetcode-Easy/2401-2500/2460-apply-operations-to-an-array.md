# 2460. Apply Operations to an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                nums[i] <<= 1;          // double the value
                nums[i + 1] = 0;
            }
        }
        int pos = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] != 0) {
                nums[pos++] = nums[i];
            }
        }
        while (pos < n) {
            nums[pos++] = 0;
        }
        return nums;
    }
};
```

## Java

```java
class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        // Apply the merging operations
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] <<= 1; // double the value
                nums[i + 1] = 0;
            }
        }
        // Shift non-zero elements forward
        int write = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[write++] = nums[i];
            }
        }
        // Fill the rest with zeros
        while (write < n) {
            nums[write++] = 0;
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] <<= 1  # double the value
                nums[i + 1] = 0
        non_zero = [x for x in nums if x != 0]
        non_zero.extend([0] * (n - len(non_zero)))
        return non_zero
```

## Python3

```python
from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] <<= 1
                nums[i + 1] = 0
        write = 0
        for v in nums:
            if v != 0:
                nums[write] = v
                write += 1
        while write < n:
            nums[write] = 0
            write += 1
        return nums
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* applyOperations(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    
    // Apply the merging operations
    for (int i = 0; i < numsSize - 1; ++i) {
        if (nums[i] == nums[i + 1]) {
            nums[i] <<= 1;      // double the value
            nums[i + 1] = 0;    // set next to zero
        }
    }
    
    // Allocate result array and shift non‑zeros forward
    int* res = (int*)malloc(numsSize * sizeof(int));
    int idx = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) {
            res[idx++] = nums[i];
        }
    }
    while (idx < numsSize) {
        res[idx++] = 0;
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ApplyOperations(int[] nums)
    {
        int n = nums.Length;
        for (int i = 0; i < n - 1; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                nums[i] <<= 1; // multiply by 2
                nums[i + 1] = 0;
            }
        }

        int write = 0;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] != 0)
            {
                nums[write++] = nums[i];
            }
        }
        while (write < n)
        {
            nums[write++] = 0;
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
var applyOperations = function(nums) {
    const n = nums.length;
    // Apply the pairwise operations
    for (let i = 0; i < n - 1; ++i) {
        if (nums[i] === nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }
    // Shift non-zero elements forward
    let writeIdx = 0;
    for (let i = 0; i < n; ++i) {
        if (nums[i] !== 0) {
            nums[writeIdx++] = nums[i];
        }
    }
    // Fill the rest with zeros
    while (writeIdx < n) {
        nums[writeIdx++] = 0;
    }
    return nums;
};
```

## Typescript

```typescript
function applyOperations(nums: number[]): number[] {
    const n = nums.length;
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }
    const result: number[] = [];
    for (const v of nums) {
        if (v !== 0) result.push(v);
    }
    while (result.length < n) {
        result.push(0);
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
    function applyOperations($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] == $nums[$i + 1]) {
                $nums[$i] *= 2;
                $nums[$i + 1] = 0;
            }
        }

        $result = [];
        foreach ($nums as $val) {
            if ($val != 0) {
                $result[] = $val;
            }
        }
        while (count($result) < $n) {
            $result[] = 0;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func applyOperations(_ nums: [Int]) -> [Int] {
        var arr = nums
        let n = arr.count
        if n > 1 {
            for i in 0..<(n - 1) {
                if arr[i] == arr[i + 1] {
                    arr[i] *= 2
                    arr[i + 1] = 0
                }
            }
        }
        var writeIdx = 0
        for i in 0..<n {
            if arr[i] != 0 {
                arr[writeIdx] = arr[i]
                writeIdx += 1
            }
        }
        while writeIdx < n {
            arr[writeIdx] = 0
            writeIdx += 1
        }
        return arr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun applyOperations(nums: IntArray): IntArray {
        val n = nums.size
        for (i in 0 until n - 1) {
            if (nums[i] == nums[i + 1]) {
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            }
        }
        var idx = 0
        for (i in 0 until n) {
            if (nums[i] != 0) {
                nums[idx++] = nums[i]
            }
        }
        while (idx < n) {
            nums[idx++] = 0
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> applyOperations(List<int> nums) {
    int n = nums.length;
    for (int i = 0; i < n - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
    }
    int writeIdx = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] != 0) {
        nums[writeIdx++] = nums[i];
      }
    }
    while (writeIdx < n) {
      nums[writeIdx++] = 0;
    }
    return nums;
  }
}
```

## Golang

```go
func applyOperations(nums []int) []int {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		if nums[i] == nums[i+1] {
			nums[i] <<= 1
			nums[i+1] = 0
		}
	}
	pos := 0
	for _, v := range nums {
		if v != 0 {
			nums[pos] = v
			pos++
		}
	}
	for ; pos < n; pos++ {
		nums[pos] = 0
	}
	return nums
}
```

## Ruby

```ruby
def apply_operations(nums)
  n = nums.length
  (0...n - 1).each do |i|
    if nums[i] == nums[i + 1]
      nums[i] <<= 1
      nums[i + 1] = 0
    end
  end

  write_idx = 0
  nums.each do |v|
    if v != 0
      nums[write_idx] = v
      write_idx += 1
    end
  end

  while write_idx < n
    nums[write_idx] = 0
    write_idx += 1
  end

  nums
end
```

## Scala

```scala
object Solution {
    def applyOperations(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        for (i <- 0 until n - 1) {
            if (nums(i) == nums(i + 1)) {
                nums(i) = nums(i) * 2
                nums(i + 1) = 0
            }
        }
        val result = new Array[Int](n)
        var idx = 0
        for (v <- nums) {
            if (v != 0) {
                result(idx) = v
                idx += 1
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn apply_operations(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        let n = nums.len();
        for i in 0..n - 1 {
            if nums[i] == nums[i + 1] {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

        let mut write = 0usize;
        for i in 0..n {
            if nums[i] != 0 {
                nums[write] = nums[i];
                write += 1;
            }
        }
        while write < n {
            nums[write] = 0;
            write += 1;
        }

        nums
    }
}
```

## Racket

```racket
(define/contract (apply-operations nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (v (list->vector nums)))
    ;; Apply the merging operations
    (for ([i (in-range (- n 1))])
      (when (= (vector-ref v i) (vector-ref v (+ i 1)))
        (vector-set! v i (* 2 (vector-ref v i)))
        (vector-set! v (+ i 1) 0)))
    ;; Collect non‑zero elements preserving order
    (let loop ((idx 0) (acc '()))
      (if (= idx n)
          (let* ((nonzeros (reverse acc))
                 (zero-count (- n (length nonzeros))))
            (append nonzeros (make-list zero-count 0)))
          (let ((val (vector-ref v idx)))
            (loop (+ idx 1) (if (zero? val) acc (cons val acc)))))))
```

## Erlang

```erlang
-spec apply_operations([integer()]) -> [integer()].
apply_operations(Nums) ->
    MergedRev = merge(Nums, []),
    Merged = lists:reverse(MergedRev),
    NonZeros = [X || X <- Merged, X =/= 0],
    ZerosCount = length(Nums) - length(NonZeros),
    NonZeros ++ lists:duplicate(ZerosCount, 0).

merge([], Acc) -> Acc;
merge([X], Acc) -> [X|Acc];
merge([A,B|Rest], Acc) ->
    case (A =:= B andalso A =/= 0) of
        true ->
            NewA = A * 2,
            NewB = 0,
            merge([NewB | Rest], [NewA | Acc]);
        false ->
            merge([B | Rest], [A | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec apply_operations(nums :: [integer]) :: [integer]
  def apply_operations(nums) do
    merged = merge(nums)
    nonzeros = Enum.filter(merged, fn x -> x != 0 end)
    zeros_needed = length(nums) - length(nonzeros)
    nonzeros ++ List.duplicate(0, zeros_needed)
  end

  defp merge([]), do: []
  defp merge([_]=list), do: list
  defp merge([a, b | rest]) do
    if a == b do
      [a * 2, 0 | merge(rest)]
    else
      [a | merge([b | rest])]
    end
  end
end
```
