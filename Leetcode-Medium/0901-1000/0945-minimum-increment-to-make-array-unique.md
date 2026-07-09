# 0945. Minimum Increment to Make Array Unique

## Cpp

```cpp
class Solution {
public:
    int minIncrementForUnique(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        std::sort(nums.begin(), nums.end());
        long long moves = 0;
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] <= nums[i - 1]) {
                int needed = nums[i - 1] + 1 - nums[i];
                moves += needed;
                nums[i] = nums[i - 1] + 1;
            }
        }
        return static_cast<int>(moves);
    }
};
```

## Java

```java
class Solution {
    public int minIncrementForUnique(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        java.util.Arrays.sort(nums);
        long moves = 0;
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int cur = nums[i];
            if (cur <= prev) {
                moves += (prev + 1L - cur);
                prev = prev + 1;
            } else {
                prev = cur;
            }
        }
        return (int) moves;
    }
}
```

## Python

```python
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        moves = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= prev:
                inc = prev + 1 - cur
                moves += inc
                prev = prev + 1
            else:
                prev = cur
        return moves
```

## Python3

```python
from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                inc = nums[i - 1] + 1 - nums[i]
                moves += inc
                nums[i] = nums[i - 1] + 1
        return moves
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int minIncrementForUnique(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    long long moves = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] <= nums[i - 1]) {
            int inc = nums[i - 1] + 1 - nums[i];
            moves += inc;
            nums[i] = nums[i - 1] + 1;
        }
    }
    return (int)moves;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinIncrementForUnique(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;
        Array.Sort(nums);
        long moves = 0;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] <= nums[i - 1])
            {
                int target = nums[i - 1] + 1;
                moves += target - nums[i];
                nums[i] = target;
            }
        }
        return (int)moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    nums.sort((a, b) => a - b);
    let moves = 0;
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] <= nums[i - 1]) {
            const inc = nums[i - 1] + 1 - nums[i];
            moves += inc;
            nums[i] = nums[i - 1] + 1;
        }
    }
    return moves;
};
```

## Typescript

```typescript
function minIncrementForUnique(nums: number[]): number {
    if (nums.length === 0) return 0;
    nums.sort((a, b) => a - b);
    let moves = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) {
            const inc = nums[i - 1] + 1 - nums[i];
            moves += inc;
            nums[i] = nums[i - 1] + 1;
        }
    }
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minIncrementForUnique($nums) {
        if (empty($nums)) {
            return 0;
        }
        sort($nums, SORT_NUMERIC);
        $moves = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] <= $nums[$i - 1]) {
                $increment = $nums[$i - 1] + 1 - $nums[$i];
                $moves += $increment;
                $nums[$i] = $nums[$i - 1] + 1;
            }
        }
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minIncrementForUnique(_ nums: [Int]) -> Int {
        var arr = nums.sorted()
        var moves = 0
        for i in 1..<arr.count {
            if arr[i] <= arr[i - 1] {
                let target = arr[i - 1] + 1
                moves += target - arr[i]
                arr[i] = target
            }
        }
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minIncrementForUnique(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        nums.sort()
        var moves = 0L
        var prev = nums[0]
        for (i in 1 until nums.size) {
            val cur = nums[i]
            if (cur <= prev) {
                val inc = prev + 1 - cur
                moves += inc
                prev = prev + 1
            } else {
                prev = cur
            }
        }
        return moves.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minIncrementForUnique(List<int> nums) {
    if (nums.isEmpty) return 0;
    nums.sort();
    int moves = 0;
    for (int i = 1; i < nums.length; ++i) {
      if (nums[i] <= nums[i - 1]) {
        int needed = nums[i - 1] + 1 - nums[i];
        moves += needed;
        nums[i] = nums[i - 1] + 1;
      }
    }
    return moves;
  }
}
```

## Golang

```go
import "sort"

func minIncrementForUnique(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	sort.Ints(nums)
	moves := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] <= nums[i-1] {
			inc := nums[i-1] + 1 - nums[i]
			moves += inc
			nums[i] = nums[i-1] + 1
		}
	}
	return moves
}
```

## Ruby

```ruby
def min_increment_for_unique(nums)
  nums.sort!
  moves = 0
  (1...nums.length).each do |i|
    if nums[i] <= nums[i - 1]
      inc = nums[i - 1] + 1 - nums[i]
      moves += inc
      nums[i] = nums[i - 1] + 1
    end
  end
  moves
end
```

## Scala

```scala
object Solution {
    def minIncrementForUnique(nums: Array[Int]): Int = {
        java.util.Arrays.sort(nums)
        var moves: Long = 0L
        for (i <- 1 until nums.length) {
            if (nums(i) <= nums(i - 1)) {
                val inc = nums(i - 1) + 1 - nums(i)
                moves += inc
                nums(i) = nums(i - 1) + 1
            }
        }
        moves.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_increment_for_unique(nums: Vec<i32>) -> i32 {
        let mut arr = nums;
        if arr.is_empty() {
            return 0;
        }
        arr.sort_unstable();
        let mut moves: i64 = 0;
        for i in 1..arr.len() {
            if arr[i] <= arr[i - 1] {
                let inc = (arr[i - 1] as i64 + 1) - arr[i] as i64;
                moves += inc;
                arr[i] = arr[i - 1] + 1;
            }
        }
        moves as i32
    }
}
```

## Racket

```racket
(define/contract (min-increment-for-unique nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sorted (sort nums <)))
    (if (null? sorted)
        0
        (let loop ((rest (cdr sorted))
                   (prev (car sorted))
                   (moves 0))
          (if (null? rest)
              moves
              (let* ((curr (car rest))
                     (new-prev (if (> curr prev) curr (+ prev 1)))
                     (add (if (> curr prev) 0 (- (+ prev 1) curr))))
                (loop (cdr rest) new-prev (+ moves add))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_increment_for_unique/1]).

-spec min_increment_for_unique(Nums :: [integer()]) -> integer().
min_increment_for_unique(Nums) ->
    Sorted = lists:sort(Nums),
    go(Sorted, 0, none).

go([], Moves, _) -> Moves;
go([H|T], Moves, none) ->
    go(T, Moves, H);
go([H|T], Moves, Prev) when H > Prev ->
    go(T, Moves, H);
go([H|T], Moves, Prev) ->
    Increment = Prev + 1 - H,
    go(T, Moves + Increment, Prev + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_increment_for_unique(nums :: [integer]) :: integer
  def min_increment_for_unique(nums) do
    case Enum.sort(nums) do
      [] -> 
        0

      [first | rest] ->
        {_last, moves} =
          Enum.reduce(rest, {first, 0}, fn x, {prev, acc} ->
            if x > prev do
              {x, acc}
            else
              inc = prev + 1 - x
              {prev + 1, acc + inc}
            end
          end)

        moves
    end
  end
end
```
