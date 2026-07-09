# 0581. Shortest Unsorted Continuous Subarray

## Cpp

```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int start = -1, end = -2; // ensures length 0 when already sorted
        int maxSeen = nums[0];
        for (int i = 1; i < n; ++i) {
            maxSeen = max(maxSeen, nums[i]);
            if (nums[i] < maxSeen) end = i;
        }
        int minSeen = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            minSeen = min(minSeen, nums[i]);
            if (nums[i] > minSeen) start = i;
        }
        return end - start + 1;
    }
};
```

## Java

```java
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int left = n, right = -1;
        int maxSeen = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            maxSeen = Math.max(maxSeen, nums[i]);
            if (nums[i] < maxSeen) {
                right = i;
            }
        }
        int minSeen = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            minSeen = Math.min(minSeen, nums[i]);
            if (nums[i] > minSeen) {
                left = i;
            }
        }
        return right == -1 ? 0 : right - left + 1;
    }
}
```

## Python

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        # Find the first index from left where order breaks
        l = 0
        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        if l == n - 1:  # already sorted
            return 0

        # Find the first index from right where order breaks
        r = n - 1
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        sub_min = min(nums[l:r + 1])
        sub_max = max(nums[l:r + 1])

        # Expand the left boundary if needed
        while l > 0 and nums[l - 1] > sub_min:
            l -= 1

        # Expand the right boundary if needed
        while r < n - 1 and nums[r + 1] < sub_max:
            r += 1

        return r - l + 1
```

## Python3

```python
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:  # already sorted
            return 0

        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        sub_min = min(nums[left:right + 1])
        sub_max = max(nums[left:right + 1])

        while left > 0 and nums[left - 1] > sub_min:
            left -= 1
        while right < n - 1 and nums[right + 1] < sub_max:
            right += 1

        return right - left + 1
```

## C

```c
int findUnsortedSubarray(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    int start = -1, end = -2; // ensures length 0 when already sorted
    int maxSeen = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < maxSeen) {
            end = i;
        } else {
            maxSeen = nums[i];
        }
    }
    int minSeen = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        if (nums[i] > minSeen) {
            start = i;
        } else {
            minSeen = nums[i];
        }
    }
    return end - start + 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindUnsortedSubarray(int[] nums)
    {
        int n = nums.Length;
        int left = n, right = -1;

        int maxSeen = int.MinValue;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] >= maxSeen)
                maxSeen = nums[i];
            else
                right = i;
        }

        int minSeen = int.MaxValue;
        for (int i = n - 1; i >= 0; i--)
        {
            if (nums[i] <= minSeen)
                minSeen = nums[i];
            else
                left = i;
        }

        return right == -1 ? 0 : right - left + 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
    const n = nums.length;
    if (n <= 1) return 0;

    let start = -1, end = -2; // default for already sorted array
    let maxSeen = nums[0];
    let minSeen = nums[n - 1];

    for (let i = 1; i < n; i++) {
        if (nums[i] >= maxSeen) {
            maxSeen = nums[i];
        } else {
            end = i;
        }
    }

    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= minSeen) {
            minSeen = nums[i];
        } else {
            start = i;
        }
    }

    return end - start + 1;
};
```

## Typescript

```typescript
function findUnsortedSubarray(nums: number[]): number {
    const n = nums.length;
    if (n <= 1) return 0;

    let start = -1, end = -2; // default length 0 when already sorted
    let maxSeen = nums[0];
    for (let i = 1; i < n; i++) {
        maxSeen = Math.max(maxSeen, nums[i]);
        if (nums[i] < maxSeen) {
            end = i;
        }
    }

    let minSeen = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        minSeen = Math.min(minSeen, nums[i]);
        if (nums[i] > minSeen) {
            start = i;
        }
    }

    return end - start + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findUnsortedSubarray($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return 0;
        }

        $max = $nums[0];
        $end = -1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $max) {
                $end = $i;
            } else {
                $max = $nums[$i];
            }
        }

        $min = $nums[$n - 1];
        $start = -1;
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] > $min) {
                $start = $i;
            } else {
                $min = $nums[$i];
            }
        }

        if ($end == -1) { // already sorted
            return 0;
        }

        return $end - $start + 1;
    }
}
```

## Swift

```swift
class Solution {
    func findUnsortedSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var left = 0
        while left < n - 1 && nums[left] <= nums[left + 1] {
            left += 1
        }
        if left == n - 1 { return 0 }
        
        var right = n - 1
        while right > 0 && nums[right] >= nums[right - 1] {
            right -= 1
        }
        
        var subMin = Int.max
        var subMax = Int.min
        for i in left...right {
            if nums[i] < subMin { subMin = nums[i] }
            if nums[i] > subMax { subMax = nums[i] }
        }
        
        while left > 0 && nums[left - 1] > subMin {
            left -= 1
        }
        while right < n - 1 && nums[right + 1] < subMax {
            right += 1
        }
        
        return right - left + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findUnsortedSubarray(nums: IntArray): Int {
        val n = nums.size
        var left = n
        var right = -1
        var maxSeen = Int.MIN_VALUE
        for (i in 0 until n) {
            if (nums[i] >= maxSeen) {
                maxSeen = nums[i]
            } else {
                right = i
            }
        }
        var minSeen = Int.MAX_VALUE
        for (i in n - 1 downTo 0) {
            if (nums[i] <= minSeen) {
                minSeen = nums[i]
            } else {
                left = i
            }
        }
        return if (right == -1) 0 else right - left + 1
    }
}
```

## Dart

```dart
class Solution {
  int findUnsortedSubarray(List<int> nums) {
    int n = nums.length;
    int left = n, right = -1;

    int maxSeen = nums[0];
    for (int i = 0; i < n; ++i) {
      if (nums[i] > maxSeen) {
        maxSeen = nums[i];
      }
      if (nums[i] < maxSeen) {
        right = i;
      }
    }

    int minSeen = nums[n - 1];
    for (int i = n - 1; i >= 0; --i) {
      if (nums[i] < minSeen) {
        minSeen = nums[i];
      }
      if (nums[i] > minSeen) {
        left = i;
      }
    }

    return right == -1 ? 0 : right - left + 1;
  }
}
```

## Golang

```go
func findUnsortedSubarray(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return 0
	}
	left := 0
	for left < n-1 && nums[left] <= nums[left+1] {
		left++
	}
	if left == n-1 { // already sorted
		return 0
	}
	right := n - 1
	for right > 0 && nums[right] >= nums[right-1] {
		right--
	}
	subMin, subMax := nums[left], nums[left]
	for i := left; i <= right; i++ {
		if nums[i] < subMin {
			subMin = nums[i]
		}
		if nums[i] > subMax {
			subMax = nums[i]
		}
	}
	for left > 0 && nums[left-1] > subMin {
		left--
	}
	for right < n-1 && nums[right+1] < subMax {
		right++
	}
	return right - left + 1
}
```

## Ruby

```ruby
def find_unsorted_subarray(nums)
  n = nums.length
  max_val = -Float::INFINITY
  min_val = Float::INFINITY
  left = n
  right = -1

  (0...n).each do |i|
    if nums[i] >= max_val
      max_val = nums[i]
    else
      right = i
    end
  end

  (n - 1).downto(0) do |i|
    if nums[i] <= min_val
      min_val = nums[i]
    else
      left = i
    end
  end

  return 0 if right == -1
  right - left + 1
end
```

## Scala

```scala
object Solution {
    def findUnsortedSubarray(nums: Array[Int]): Int = {
        val n = nums.length
        var left = n
        var right = -1
        var maxSeen = Int.MinValue
        for (i <- 0 until n) {
            if (nums(i) >= maxSeen) {
                maxSeen = nums(i)
            } else {
                right = i
            }
        }
        var minSeen = Int.MaxValue
        for (i <- (n - 1) to 0 by -1) {
            if (nums(i) <= minSeen) {
                minSeen = nums(i)
            } else {
                left = i
            }
        }
        if (right == -1) 0 else right - left + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }

        let mut left = n;
        let mut right = 0usize;

        // Forward pass to find the right boundary
        let mut max_seen = nums[0];
        for i in 1..n {
            if nums[i] >= max_seen {
                max_seen = nums[i];
            } else {
                right = i;
            }
        }

        // Backward pass to find the left boundary
        let mut min_seen = nums[n - 1];
        for i in (0..n - 1).rev() {
            if nums[i] <= min_seen {
                min_seen = nums[i];
            } else {
                left = i;
            }
        }

        if right == 0 && left == n {
            0
        } else {
            (right - left + 1) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (find-unsorted-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (= n 0)
        0
        (let ([right -1]
              [max-sofar (vector-ref v 0)])
          (for ([i (in-range 1 n)])
            (define val (vector-ref v i))
            (when (< val max-sofar)
              (set! right i))
            (when (> val max-sofar)
              (set! max-sofar val)))
          (let ([left -1]
                [min-sofar (vector-ref v (- n 1))])
            (for ([j (in-range (- n 2) -1 -1)])
              (define val (vector-ref v j))
              (when (> val min-sofar)
                (set! left j))
              (when (< val min-sofar)
                (set! min-sofar val)))
            (if (= right -1) 0 (+ 1 (- right left))))))))
```

## Erlang

```erlang
-spec find_unsorted_subarray([integer()]) -> integer().
find_unsorted_subarray(Nums) ->
    Len = length(Nums),
    case Len of
        0 -> 0;
        _ ->
            Tuple = list_to_tuple(Nums),
            Left = find_left(Tuple, Len, 1),
            case Left of
                0 -> 0; % already sorted
                _ ->
                    Right = find_right(Tuple, Len, Len),
                    {SubMin, SubMax} = min_max_range(Tuple, Left, Right),
                    NewLeft = expand_left(Tuple, Left, SubMin),
                    NewRight = expand_right(Tuple, Right, SubMax, Len),
                    NewRight - NewLeft + 1
            end
    end.

%% find first index where nums[i] > nums[i+1]
find_left(_Tuple, Len, I) when I >= Len -> 0;
find_left(Tuple, _Len, I) ->
    Curr = element(I, Tuple),
    Next = element(I + 1, Tuple),
    if
        Curr > Next -> I;
        true -> find_left(Tuple, _Len, I + 1)
    end.

%% find last index where nums[i-1] > nums[i]
find_right(_Tuple, _Len, I) when I =< 1 -> 0;
find_right(Tuple, _Len, I) ->
    Prev = element(I - 1, Tuple),
    Curr = element(I, Tuple),
    if
        Prev > Curr -> I;
        true -> find_right(Tuple, _Len, I - 1)
    end.

%% compute min and max in range [L,R]
min_max_range(Tuple, L, R) ->
    First = element(L, Tuple),
    min_max_range(Tuple, L + 1, R, First, First).

min_max_range(_Tuple, I, R, MinAcc, MaxAcc) when I > R -> {MinAcc, MaxAcc};
min_max_range(Tuple, I, R, MinAcc, MaxAcc) ->
    Val = element(I, Tuple),
    NewMin = if Val < MinAcc -> Val; true -> MinAcc end,
    NewMax = if Val > MaxAcc -> Val; true -> MaxAcc end,
    min_max_range(Tuple, I + 1, R, NewMin, NewMax).

%% expand left boundary
expand_left(_Tuple, Left, _SubMin) when Left =< 1 -> Left;
expand_left(Tuple, Left, SubMin) ->
    PrevIdx = Left - 1,
    PrevVal = element(PrevIdx, Tuple),
    if
        PrevVal > SubMin -> expand_left(Tuple, PrevIdx, SubMin);
        true -> Left
    end.

%% expand right boundary
expand_right(_Tuple, Right, _SubMax, Len) when Right >= Len -> Right;
expand_right(Tuple, Right, SubMax, Len) ->
    NextIdx = Right + 1,
    NextVal = element(NextIdx, Tuple),
    if
        NextVal < SubMax -> expand_right(Tuple, NextIdx, SubMax, Len);
        true -> Right
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_unsorted_subarray(nums :: [integer]) :: integer
  def find_unsorted_subarray(nums) do
    n = length(nums)

    if n <= 1 do
      0
    else
      t = List.to_tuple(nums)
      left = find_left(t, n, 0)

      if left == n - 1 do
        0
      else
        right = find_right(t, n - 1)

        sublist = Enum.slice(nums, left..right)
        sub_min = Enum.min(sublist)
        sub_max = Enum.max(sublist)

        left2 = expand_left(t, left, sub_min)
        right2 = expand_right(t, n, right, sub_max)

        right2 - left2 + 1
      end
    end
  end

  defp elem_at(t, i), do: :erlang.element(i + 1, t)

  # find first index where order breaks from the left
  defp find_left(_t, n, i) when i >= n - 1, do: i

  defp find_left(t, n, i) do
    if elem_at(t, i + 1) >= elem_at(t, i) do
      find_left(t, n, i + 1)
    else
      i
    end
  end

  # find first index where order breaks from the right
  defp find_right(_t, i) when i <= 0, do: i

  defp find_right(t, i) do
    if elem_at(t, i - 1) <= elem_at(t, i) do
      find_right(t, i - 1)
    else
      i
    end
  end

  # expand left boundary if needed
  defp expand_left(_t, 0, _sub_min), do: 0

  defp expand_left(t, left, sub_min) do
    if elem_at(t, left - 1) > sub_min do
      expand_left(t, left - 1, sub_min)
    else
      left
    end
  end

  # expand right boundary if needed
  defp expand_right(_t, n, right, _sub_max) when right >= n - 1, do: right

  defp expand_right(t, n, right, sub_max) do
    if elem_at(t, right + 1) < sub_max do
      expand_right(t, n, right + 1, sub_max)
    else
      right
    end
  end
end
```
