# 2091. Removing Minimum and Maximum From Array

## Cpp

```cpp
class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        int minIdx = 0, maxIdx = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }
        int left = min(minIdx, maxIdx);
        int right = max(minIdx, maxIdx);
        int option1 = right + 1;               // delete from front only
        int option2 = n - left;                // delete from back only
        int option3 = (left + 1) + (n - right); // delete from both ends
        return min({option1, option2, option3});
    }
};
```

## Java

```java
class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        int minIdx = 0, maxIdx = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }
        int frontBoth = Math.max(minIdx, maxIdx) + 1;
        int backBoth = n - Math.min(minIdx, maxIdx);
        int mixed1 = minIdx + 1 + (n - maxIdx);
        int mixed2 = maxIdx + 1 + (n - minIdx);
        int mixed = Math.min(mixed1, mixed2);
        return Math.min(frontBoth, Math.min(backBoth, mixed));
    }
}
```

## Python

```python
class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_idx = max_idx = 0
        for i, v in enumerate(nums):
            if v < nums[min_idx]:
                min_idx = i
            if v > nums[max_idx]:
                max_idx = i

        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        # Remove both from front
        option1 = b + 1
        # Remove both from back
        option2 = n - a
        # Remove one from front and the other from back
        option3 = (a + 1) + (n - b)

        return min(option1, option2, option3)
```

## Python3

```python
from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = max_idx = 0
        for i, v in enumerate(nums):
            if v < nums[min_idx]:
                min_idx = i
            if v > nums[max_idx]:
                max_idx = i
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        opt1 = b + 1               # delete only from front
        opt2 = n - a               # delete only from back
        opt3 = (a + 1) + (n - b)   # delete from both ends
        return min(opt1, opt2, opt3)
```

## C

```c
int minimumDeletions(int* nums, int numsSize) {
    int minIdx = 0, maxIdx = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    int left = minIdx, right = maxIdx;
    if (left > right) {
        int tmp = left;
        left = right;
        right = tmp;
    }
    int opt1 = right + 1;                 // delete only from front
    int opt2 = numsSize - left;           // delete only from back
    int opt3 = (left + 1) + (numsSize - right); // delete from both ends
    int ans = opt1;
    if (opt2 < ans) ans = opt2;
    if (opt3 < ans) ans = opt3;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumDeletions(int[] nums) {
        int n = nums.Length;
        if (n == 0) return 0;

        int minIdx = 0, maxIdx = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }

        // Option 1: delete from front only
        int option1 = Math.Max(minIdx, maxIdx) + 1;

        // Option 2: delete from back only
        int option2 = n - Math.Min(minIdx, maxIdx);

        // Option 3: delete from both ends
        int option3a = (minIdx + 1) + (n - maxIdx); // min from front, max from back
        int option3b = (maxIdx + 1) + (n - minIdx); // max from front, min from back
        int option3 = Math.Min(option3a, option3b);

        return Math.Min(option1, Math.Min(option2, option3));
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeletions = function(nums) {
    const n = nums.length;
    let minIdx = 0, maxIdx = 0;
    for (let i = 1; i < n; ++i) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    // Ensure minIdx <= maxIdx for easier calculations
    let left = Math.min(minIdx, maxIdx);
    let right = Math.max(minIdx, maxIdx);
    
    const deleteFrontBoth = right + 1;               // remove up to the farther one from front
    const deleteBackBoth = n - left;                 // remove from back up to the nearer one
    const deleteMixed = (left + 1) + (n - right);   // front for left, back for right
    
    return Math.min(deleteFrontBoth, deleteBackBoth, deleteMixed);
};
```

## Typescript

```typescript
function minimumDeletions(nums: number[]): number {
    const n = nums.length;
    let minIdx = 0, maxIdx = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    const frontOnly = Math.max(minIdx, maxIdx) + 1;
    const backOnly = n - Math.min(minIdx, maxIdx);
    const cross1 = (minIdx + 1) + (n - maxIdx);
    const cross2 = (maxIdx + 1) + (n - minIdx);
    return Math.min(frontOnly, backOnly, cross1, cross2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDeletions($nums) {
        $n = count($nums);
        if ($n == 0) return 0;

        $minVal = PHP_INT_MAX;
        $maxVal = PHP_INT_MIN;
        $minIdx = -1;
        $maxIdx = -1;

        foreach ($nums as $idx => $val) {
            if ($val < $minVal) {
                $minVal = $val;
                $minIdx = $idx;
            }
            if ($val > $maxVal) {
                $maxVal = $val;
                $maxIdx = $idx;
            }
        }

        // Option 1: delete from front only
        $option1 = max($minIdx, $maxIdx) + 1;

        // Option 2: delete from back only
        $option2 = $n - min($minIdx, $maxIdx);

        // Option 3a: remove min from front, max from back
        $option3a = ($minIdx + 1) + ($n - $maxIdx);

        // Option 3b: remove max from front, min from back
        $option3b = ($maxIdx + 1) + ($n - $minIdx);

        return min($option1, $option2, $option3a, $option3b);
    }
}
```

## Swift

```swift
class Solution {
    func minimumDeletions(_ nums: [Int]) -> Int {
        let n = nums.count
        var minIdx = 0
        var maxIdx = 0
        
        for (i, v) in nums.enumerated() {
            if v < nums[minIdx] { minIdx = i }
            if v > nums[maxIdx] { maxIdx = i }
        }
        
        let bothFront = max(minIdx, maxIdx) + 1
        let bothBack = n - min(minIdx, maxIdx)
        let mixed = (min(minIdx, maxIdx) + 1) + (n - max(minIdx, maxIdx))
        
        return min(bothFront, min(bothBack, mixed))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDeletions(nums: IntArray): Int {
        val n = nums.size
        var minIdx = 0
        var maxIdx = 0
        for (i in nums.indices) {
            if (nums[i] < nums[minIdx]) minIdx = i
            if (nums[i] > nums[maxIdx]) maxIdx = i
        }
        val option1 = kotlin.math.max(minIdx, maxIdx) + 1
        val option2 = n - kotlin.math.min(minIdx, maxIdx)
        val option3a = (minIdx + 1) + (n - maxIdx)
        val option3b = (maxIdx + 1) + (n - minIdx)
        return minOf(option1, option2, option3a, option3b)
    }
}
```

## Dart

```dart
class Solution {
  int minimumDeletions(List<int> nums) {
    int n = nums.length;
    int minIdx = 0, maxIdx = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] < nums[minIdx]) minIdx = i;
      if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    int left = minIdx, right = maxIdx;
    if (left > right) {
      int temp = left;
      left = right;
      right = temp;
    }
    int option1 = right + 1;          // delete only from front
    int option2 = n - left;           // delete only from back
    int option3 = (left + 1) + (n - right); // delete from both ends
    int ans = option1;
    if (option2 < ans) ans = option2;
    if (option3 < ans) ans = option3;
    return ans;
  }
}
```

## Golang

```go
func minimumDeletions(nums []int) int {
	n := len(nums)
	minIdx, maxIdx := 0, 0
	for i, v := range nums {
		if v < nums[minIdx] {
			minIdx = i
		}
		if v > nums[maxIdx] {
			maxIdx = i
		}
	}
	// deletions removing both from front only
	front := max(minIdx, maxIdx) + 1
	// deletions removing both from back only
	back := n - min(minIdx, maxIdx)
	// deletions mixing front and back
	mixed1 := minIdx + 1 + (n - maxIdx)
	mixed2 := maxIdx + 1 + (n - minIdx)
	mixed := min(mixed1, mixed2)

	ans := front
	if back < ans {
		ans = back
	}
	if mixed < ans {
		ans = mixed
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def minimum_deletions(nums)
  n = nums.length
  min_idx = nums.each_with_index.min_by { |v, _| v }[1]
  max_idx = nums.each_with_index.max_by { |v, _| v }[1]

  front_only = [min_idx, max_idx].max + 1
  back_only = n - [min_idx, max_idx].min

  both1 = min_idx + 1 + (n - max_idx)
  both2 = max_idx + 1 + (n - min_idx)

  [front_only, back_only, both1, both2].min
end
```

## Scala

```scala
object Solution {
    def minimumDeletions(nums: Array[Int]): Int = {
        val n = nums.length
        var minIdx = 0
        var maxIdx = 0
        for (i <- 1 until n) {
            if (nums(i) < nums(minIdx)) minIdx = i
            if (nums(i) > nums(maxIdx)) maxIdx = i
        }
        val a = math.min(minIdx, maxIdx)
        val b = math.max(minIdx, maxIdx)

        val option1 = b + 1                 // delete only from front
        val option2 = n - a                 // delete only from back
        val option3 = (a + 1) + (n - b)     // delete from both ends

        math.min(option1, math.min(option2, option3))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut min_idx = 0usize;
        let mut max_idx = 0usize;
        for (i, &v) in nums.iter().enumerate() {
            if v < nums[min_idx] {
                min_idx = i;
            }
            if v > nums[max_idx] {
                max_idx = i;
            }
        }
        let left = std::cmp::min(min_idx, max_idx) as i32;
        let right = std::cmp::max(min_idx, max_idx) as i32;

        let option1 = right + 1;          // delete from front only
        let option2 = n - left;           // delete from back only
        let option3 = (left + 1) + (n - right); // delete from both ends

        *[option1, option2, option3].iter().min().unwrap()
    }
}
```

## Racket

```racket
(define/contract (minimum-deletions nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (first-val (car nums)))
    (let loop ((lst (cdr nums)) (idx 1) (min-val first-val) (max-val first-val) (min-idx 0) (max-idx 0))
      (if (null? lst)
          (let* ((i min-idx)
                 (j max-idx)
                 (front-only (+ (max i j) 1))
                 (back-only (- n (min i j)))
                 (front-min-back-max (+ (+ i 1) (- n j)))
                 (front-max-back-min (+ (+ j 1) (- n i))))
            (apply min (list front-only back-only front-min-back-max front-max-back-min)))
          (let* ((x (car lst))
                 (new-min-val (if (< x min-val) x min-val))
                 (new-max-val (if (> x max-val) x max-val))
                 (new-min-idx (if (< x min-val) idx min-idx))
                 (new-max-idx (if (> x max-val) idx max-idx)))
            (loop (cdr lst) (+ idx 1) new-min-val new-max-val new-min-idx new-max-idx))))))
```

## Erlang

```erlang
-spec minimum_deletions(Nums :: [integer()]) -> integer().
minimum_deletions(Nums) ->
    case Nums of
        [] -> 0;
        [H|T] ->
            {_, MinI, _, MaxI} = find_min_max(T, H, 0, H, 0, 1),
            N = length(Nums),
            Left = erlang:min(MinI, MaxI),
            Right = erlang:max(MinI, MaxI),
            Option1 = Right + 1,
            Option2 = N - Left,
            Option3 = Left + 1 + (N - Right),
            lists:min([Option1, Option2, Option3])
    end.

find_min_max([], MinV, MinI, MaxV, MaxI, _Idx) ->
    {MinV, MinI, MaxV, MaxI};
find_min_max([H|T], MinV, MinI, MaxV, MaxI, Idx) ->
    {NewMinV, NewMinI} = if H < MinV -> {H, Idx}; true -> {MinV, MinI} end,
    {NewMaxV, NewMaxI} = if H > MaxV -> {H, Idx}; true -> {MaxV, MaxI} end,
    find_min_max(T, NewMinV, NewMinI, NewMaxV, NewMaxI, Idx + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_deletions(nums :: [integer]) :: integer
  def minimum_deletions(nums) do
    n = length(nums)

    min_val = Enum.min(nums)
    max_val = Enum.max(nums)

    min_idx = Enum.find_index(nums, fn x -> x == min_val end)
    max_idx = Enum.find_index(nums, fn x -> x == max_val end)

    i = min_idx
    j = max_idx

    front = max(i, j) + 1
    back = n - min(i, j)
    both = min(i, j) + 1 + (n - max(i, j))

    Enum.min([front, back, both])
  end
end
```
