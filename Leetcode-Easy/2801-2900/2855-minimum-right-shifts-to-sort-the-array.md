# 2855. Minimum Right Shifts to Sort the Array

## Cpp

```cpp
class Solution {
public:
    int minimumRightShifts(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int minIdx = min_element(nums.begin(), nums.end()) - nums.begin();

        // Verify that rotating left by minIdx yields a sorted array
        for (int i = 1; i < n; ++i) {
            int curIdx = (minIdx + i) % n;
            int prevIdx = (minIdx + i - 1) % n;
            if (nums[curIdx] < nums[prevIdx]) return -1;
        }
        // Number of right shifts needed
        return (n - minIdx) % n;
    }
};
```

## Java

```java
class Solution {
    public int minimumRightShifts(java.util.List<Integer> nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int breakIdx = -1;
        int breaks = 0;
        for (int i = 1; i < n; i++) {
            if (nums.get(i) < nums.get(i - 1)) {
                breaks++;
                breakIdx = i;
                if (breaks > 1) return -1;
            }
        }
        if (breaks == 0) {
            // already sorted
            return 0;
        }
        // exactly one break point; need to ensure rotation is valid
        if (nums.get(0) > nums.get(n - 1)) {
            return n - breakIdx;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        cnt = 0
        idx = -1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                idx = i
                if cnt > 1:
                    return -1

        if cnt == 0:
            return 0

        # exactly one breakpoint; check wrap condition
        if nums[0] >= nums[-1]:
            return (n - idx) % n
        else:
            return -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        idx = -1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                idx = i
        if cnt == 0:
            return 0
        if cnt > 1 or nums[-1] >= nums[0]:
            return -1
        return n - idx
```

## C

```c
int minimumRightShifts(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    int cnt = 0, pivot = -1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < nums[i - 1]) {
            ++cnt;
            pivot = i;
        }
    }
    if (cnt == 0) return 0;
    if (cnt > 1) return -1;
    // exactly one drop point
    if (nums[numsSize - 1] > nums[0]) return -1;
    return numsSize - pivot;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumRightShifts(IList<int> nums) {
        int n = nums.Count;
        if (n <= 1) return 0;

        int breakCount = 0;
        int startIdx = 0; // index where the sorted array should begin

        for (int i = 0; i < n; i++) {
            int next = (i + 1) % n;
            if (nums[next] < nums[i]) {
                breakCount++;
                startIdx = next;
                if (breakCount > 1) return -1;
            }
        }

        if (breakCount == 0) return 0;

        // Minimum right shifts to bring element at startIdx to index 0
        int shifts = (n - startIdx) % n;
        return shifts;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumRightShifts = function(nums) {
    const n = nums.length;
    if (n <= 1) return 0;

    let cnt = 0, idx = -1;
    for (let i = 1; i < n; ++i) {
        if (nums[i] < nums[i - 1]) {
            cnt++;
            idx = i;
        }
    }

    if (cnt === 0) return 0;
    if (cnt > 1) return -1;

    const k = n - idx; // number of right shifts
    const rotated = nums.slice(-k).concat(nums.slice(0, n - k));

    for (let i = 1; i < n; ++i) {
        if (rotated[i] <= rotated[i - 1]) return -1;
    }

    return k;
};
```

## Typescript

```typescript
function minimumRightShifts(nums: number[]): number {
    const n = nums.length;
    let breakIdx = -1;
    let cnt = 0;

    for (let i = 0; i < n; i++) {
        const prev = (i - 1 + n) % n;
        if (nums[i] < nums[prev]) {
            cnt++;
            breakIdx = i;
            if (cnt > 1) return -1;
        }
    }

    if (cnt === 0) return 0; // already sorted

    // verify the array is strictly increasing when traversed from breakIdx
    for (let j = 1; j < n; j++) {
        const curIdx = (breakIdx + j) % n;
        const prevIdx = (breakIdx + j - 1) % n;
        if (nums[curIdx] <= nums[prevIdx]) return -1;
    }

    // number of right shifts to bring element at breakIdx to index 0
    return (n - breakIdx) % n;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumRightShifts($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return 0;
        }
        $drops = 0;
        $dropIdx = -1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $nums[$i - 1]) {
                $drops++;
                $dropIdx = $i;
            }
        }
        if ($drops === 0) {
            return 0;
        }
        if ($drops > 1) {
            return -1;
        }
        // exactly one drop
        if ($nums[$n - 1] < $nums[0]) {
            return $n - $dropIdx;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumRightShifts(_ nums: [Int]) -> Int {
        let n = nums.count
        var dropCount = 0
        var dropIndex = -1
        
        for i in 1..<n {
            if nums[i] < nums[i - 1] {
                dropCount += 1
                dropIndex = i
            }
        }
        
        if dropCount == 0 {
            return 0
        }
        if dropCount > 1 {
            return -1
        }
        // Exactly one drop
        if nums[n - 1] > nums[0] {
            return -1
        }
        return (n - dropIndex) % n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumRightShifts(nums: List<Int>): Int {
        val n = nums.size
        var count = 0
        var idx = -1
        for (i in 1 until n) {
            if (nums[i] < nums[i - 1]) {
                count++
                idx = i
            }
        }
        return when {
            count == 0 -> 0
            count > 1 -> -1
            nums[n - 1] > nums[0] -> -1
            else -> n - idx
        }
    }
}
```

## Dart

```dart
class Solution {
  int minimumRightShifts(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return 0;

    int pivot = -1;
    for (int i = 0; i < n; i++) {
      int prev = (i - 1 + n) % n;
      if (nums[i] < nums[prev]) {
        if (pivot != -1) return -1;
        pivot = i;
      }
    }

    if (pivot == -1) return 0;

    for (int cnt = 1; cnt < n; cnt++) {
      int curIdx = (pivot + cnt) % n;
      int prevIdx = (pivot + cnt - 1) % n;
      if (nums[curIdx] < nums[prevIdx]) return -1;
    }

    return (n - pivot) % n;
  }
}
```

## Golang

```go
func minimumRightShifts(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return 0
	}
	drops := 0
	pivot := -1
	for i := 1; i < n; i++ {
		if nums[i] < nums[i-1] {
			drops++
			pivot = i
		}
	}
	if drops == 0 {
		return 0
	}
	if drops > 1 {
		return -1
	}
	for i := pivot + 1; i < n; i++ {
		if nums[i] < nums[i-1] {
			return -1
		}
	}
	for i := 1; i < pivot; i++ {
		if nums[i] < nums[i-1] {
			return -1
		}
	}
	if nums[n-1] > nums[0] {
		return -1
	}
	return n - pivot
}
```

## Ruby

```ruby
def minimum_right_shifts(nums)
  n = nums.length
  cnt = 0
  pivot = -1
  (1...n).each do |i|
    if nums[i] < nums[i - 1]
      cnt += 1
      pivot = i
    end
  end
  return 0 if cnt == 0
  return -1 if cnt > 1
  return -1 unless nums[-1] < nums[0]
  (n - pivot) % n
end
```

## Scala

```scala
object Solution {
    def minimumRightShifts(nums: List[Int]): Int = {
        val n = nums.length
        if (n <= 1) return 0
        var breaks = 0
        var pivot = -1
        for (i <- 0 until n) {
            val prev = (i - 1 + n) % n
            if (nums(i) < nums(prev)) {
                breaks += 1
                pivot = i
            }
        }
        if (breaks == 0) 0
        else if (breaks == 1) (n - pivot) % n
        else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_right_shifts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        let mut pivot_idx: Option<usize> = None;
        for i in 1..n {
            if nums[i] < nums[i - 1] {
                if pivot_idx.is_some() {
                    return -1; // more than one decreasing point
                }
                pivot_idx = Some(i);
            }
        }
        match pivot_idx {
            None => 0, // already sorted
            Some(p) => {
                let k = n - p; // number of right shifts needed
                // verify that after rotating right by k the array is strictly increasing
                for i in 0..n - 1 {
                    let cur = nums[(i + n - k) % n];
                    let nxt = nums[((i + 1) + n - k) % n];
                    if cur >= nxt {
                        return -1;
                    }
                }
                k as i32
            }
        }
    }
}
```

## Racket

```racket
(define/contract (minimum-right-shifts nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (cnt-pos
          (let loop ((i 1) (cnt 0) (pos -1))
            (if (= i n)
                (cons cnt pos)
                (if (< (list-ref nums i) (list-ref nums (- i 1)))
                    (loop (+ i 1) (+ cnt 1) i)
                    (loop (+ i 1) cnt pos)))))
         (cnt (car cnt-pos))
         (pos (cdr cnt-pos)))
    (cond
      [(= cnt 0) 0]
      [(> cnt 1) -1]
      [else
       (if (> (list-ref nums 0) (list-ref nums (- n 1)))
           (- n pos)
           -1)])))
```

## Erlang

```erlang
-spec minimum_right_shifts(Nums :: [integer()]) -> integer().
minimum_right_shifts(Nums) ->
    N = length(Nums),
    {Count, BreakIdx} = count_breaks(Nums),
    case Count of
        0 -> 0;
        1 ->
            First = hd(Nums),
            Last = lists:last(Nums),
            if
                Last < First -> N - BreakIdx;
                true -> -1
            end;
        _ -> -1
    end.

count_breaks([]) -> {0, undefined};
count_breaks([_]) -> {0, undefined};
count_breaks(Nums) ->
    N = length(Nums),
    Indexed = lists:zip(lists:seq(0, N-1), Nums),
    [{0, First}|Rest] = Indexed,
    FoldFun = fun({Idx, Val}, {PrevVal, Count, BreakIdx}) ->
        if
            Val < PrevVal -> {Val, Count + 1, Idx};
            true -> {Val, Count, BreakIdx}
        end
    end,
    {_LastVal, Count, BreakIdx} = lists:foldl(FoldFun, {First, 0, undefined}, Rest),
    {Count, BreakIdx}.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_right_shifts(nums :: [integer]) :: integer
  def minimum_right_shifts(nums) do
    n = length(nums)

    case n do
      0 -> 0
      1 -> 0
      _ ->
        drops =
          Enum.reduce(1..(n - 1), [], fn i, acc ->
            if Enum.at(nums, i) < Enum.at(nums, i - 1), do: [i | acc], else: acc
          end)
          |> Enum.reverse()

        case drops do
          [] -> 0
          [idx] ->
            if Enum.at(nums, n - 1) < Enum.at(nums, 0) do
              n - idx
            else
              -1
            end

          _ -> -1
        end
    end
  end
end
```
