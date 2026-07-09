# 2740. Find the Value of the Partition

## Cpp

```cpp
class Solution {
public:
    int findValueOfPartition(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 0; i + 1 < nums.size(); ++i) {
            ans = min(ans, nums[i + 1] - nums[i]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 1; i++) {
            int diff = nums[i + 1] - nums[i];
            if (diff < minDiff) {
                minDiff = diff;
            }
        }
        return minDiff;
    }
}
```

## Python

```python
class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
```

## Python3

```python
class Solution:
    def findValueOfPartition(self, nums):
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

int findValueOfPartition(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int minDiff = INT_MAX;
    for (int i = 0; i < numsSize - 1; ++i) {
        int diff = nums[i + 1] - nums[i];
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
}
```

## Csharp

```csharp
public class Solution {
    public int FindValueOfPartition(int[] nums) {
        System.Array.Sort(nums);
        int minDiff = int.MaxValue;
        for (int i = 0; i < nums.Length - 1; i++) {
            int diff = nums[i + 1] - nums[i];
            if (diff < minDiff) {
                minDiff = diff;
            }
        }
        return minDiff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findValueOfPartition = function(nums) {
    nums.sort((a, b) => a - b);
    let minDiff = Infinity;
    for (let i = 0; i < nums.length - 1; ++i) {
        const diff = nums[i + 1] - nums[i];
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
};
```

## Typescript

```typescript
function findValueOfPartition(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let minDiff = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < nums.length - 1; ++i) {
        const diff = Math.abs(nums[i + 1] - nums[i]);
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findValueOfPartition($nums) {
        sort($nums, SORT_NUMERIC);
        $minDiff = PHP_INT_MAX;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            $diff = $nums[$i + 1] - $nums[$i];
            if ($diff < $minDiff) {
                $minDiff = $diff;
            }
        }
        return $minDiff;
    }
}
```

## Swift

```swift
class Solution {
    func findValueOfPartition(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var minDiff = Int.max
        for i in 0..<(sortedNums.count - 1) {
            let diff = sortedNums[i + 1] - sortedNums[i]
            if diff < minDiff {
                minDiff = diff
            }
        }
        return minDiff
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findValueOfPartition(nums: IntArray): Int {
        nums.sort()
        var minDiff = Int.MAX_VALUE
        for (i in 0 until nums.size - 1) {
            val diff = nums[i + 1] - nums[i]
            if (diff < minDiff) minDiff = diff
        }
        return minDiff
    }
}
```

## Dart

```dart
class Solution {
  int findValueOfPartition(List<int> nums) {
    nums.sort();
    int minDiff = nums[1] - nums[0];
    for (int i = 1; i < nums.length - 1; i++) {
      int diff = nums[i + 1] - nums[i];
      if (diff < minDiff) {
        minDiff = diff;
      }
    }
    return minDiff;
  }
}
```

## Golang

```go
import "sort"

func findValueOfPartition(nums []int) int {
	sort.Ints(nums)
	minDiff := nums[1] - nums[0]
	for i := 1; i < len(nums)-1; i++ {
		if d := nums[i+1] - nums[i]; d < minDiff {
			minDiff = d
		}
	}
	return minDiff
}
```

## Ruby

```ruby
def find_value_of_partition(nums)
  nums.sort!
  min_diff = Float::INFINITY
  (0...nums.size - 1).each do |i|
    diff = nums[i + 1] - nums[i]
    min_diff = diff if diff < min_diff
  end
  min_diff.to_i
end
```

## Scala

```scala
object Solution {
    def findValueOfPartition(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        var minDiff = Int.MaxValue
        var i = 0
        while (i < sorted.length - 1) {
            val diff = sorted(i + 1) - sorted(i)
            if (diff < minDiff) minDiff = diff
            i += 1
        }
        minDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_value_of_partition(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut ans = i32::MAX;
        for i in 0..nums.len() - 1 {
            let diff = nums[i + 1] - nums[i];
            if diff < ans {
                ans = diff;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-value-of-partition nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sorted (sort nums <)))
    (let loop ((prev (first sorted))
               (rest (rest sorted))
               (best (expt 2 60))) ; sufficiently large integer
      (if (null? rest)
          best
          (let* ((curr (first rest))
                 (diff (- curr prev))
                 (new-best (if (< diff best) diff best)))
            (loop curr (rest rest) new-best))))))
```

## Erlang

```erlang
-spec find_value_of_partition(Nums :: [integer()]) -> integer().
find_value_of_partition(Nums) ->
    Sorted = lists:sort(Nums),
    case Sorted of
        [A, B | Rest] ->
            Initial = B - A,
            min_diff_loop(Rest, B, Initial);
        _ -> 0
    end.

min_diff_loop([], _, Min) -> Min;
min_diff_loop([C | Rest], Prev, Min) ->
    Diff = C - Prev,
    NewMin = if Diff < Min -> Diff; true -> Min end,
    min_diff_loop(Rest, C, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_value_of_partition(nums :: [integer]) :: integer
  def find_value_of_partition(nums) do
    nums
    |> Enum.sort()
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.map(fn [a, b] -> b - a end)
    |> Enum.min()
  end
end
```
