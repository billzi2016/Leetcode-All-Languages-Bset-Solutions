# 0462. Minimum Moves to Equal Array Elements II

## Cpp

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int median = nums[n / 2];
        long long moves = 0;
        for (int x : nums) {
            moves += llabs((long long)x - median);
        }
        return static_cast<int>(moves);
    }
};
```

## Java

```java
class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int median = nums[nums.length / 2];
        long moves = 0;
        for (int num : nums) {
            moves += Math.abs((long) num - median);
        }
        return (int) moves;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)
```

## Python3

```python
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

int minMoves2(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    int median = nums[numsSize / 2];
    long long moves = 0;
    for (int i = 0; i < numsSize; ++i) {
        moves += llabs((long long)nums[i] - median);
    }
    return (int)moves;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMoves2(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int median = nums[n / 2];
        long moves = 0;
        foreach (int num in nums) {
            moves += Math.Abs((long)num - median);
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
var minMoves2 = function(nums) {
    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let moves = 0;
    for (let i = 0; i < nums.length; ++i) {
        moves += Math.abs(nums[i] - median);
    }
    return moves;
};
```

## Typescript

```typescript
function minMoves2(nums: number[]): number {
    const sorted = nums.slice().sort((a, b) => a - b);
    const median = sorted[Math.floor(sorted.length / 2)];
    let moves = 0;
    for (const v of nums) {
        moves += Math.abs(v - median);
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
    function minMoves2($nums) {
        sort($nums);
        $n = count($nums);
        $median = $nums[intval($n / 2)];
        $moves = 0;
        foreach ($nums as $v) {
            $moves += abs($v - $median);
        }
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves2(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let median = sorted[sorted.count / 2]
        var total: Int64 = 0
        for num in sorted {
            total += Int64(abs(num - median))
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves2(nums: IntArray): Int {
        nums.sort()
        val median = nums[nums.size / 2]
        var moves = 0L
        for (v in nums) {
            moves += kotlin.math.abs(v - median).toLong()
        }
        return moves.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minMoves2(List<int> nums) {
    nums.sort();
    int median = nums[nums.length ~/ 2];
    int moves = 0;
    for (int num in nums) {
      moves += (num - median).abs();
    }
    return moves;
  }
}
```

## Golang

```go
import "sort"

func minMoves2(nums []int) int {
    sort.Ints(nums)
    median := nums[len(nums)/2]
    var moves int64
    for _, v := range nums {
        diff := v - median
        if diff < 0 {
            diff = -diff
        }
        moves += int64(diff)
    }
    return int(moves)
}
```

## Ruby

```ruby
def min_moves2(nums)
  nums.sort!
  median = nums[nums.length / 2]
  moves = 0
  nums.each { |v| moves += (v - median).abs }
  moves
end
```

## Scala

```scala
object Solution {
    def minMoves2(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val median = sorted(sorted.length / 2)
        var moves: Long = 0L
        for (v <- nums) {
            moves += math.abs(v - median).toLong
        }
        moves.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let median = nums[nums.len() / 2];
        let mut moves: i64 = 0;
        for &v in &nums {
            moves += (v - median).abs() as i64;
        }
        moves as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (min-moves2 nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (len (length sorted))
         (mid-idx (quotient len 2))
         (median (list-ref sorted mid-idx)))
    (for/sum ([x sorted]) (abs (- x median)))))
```

## Erlang

```erlang
-module(solution).
-export([min_moves2/1]).

-spec min_moves2(Nums :: [integer()]) -> integer().
min_moves2(Nums) ->
    Sorted = lists:sort(Nums),
    Len = length(Sorted),
    MedianIdx = Len div 2,
    Median = lists:nth(MedianIdx + 1, Sorted),
    sum_abs_diff(Sorted, Median, 0).

sum_abs_diff([], _M, Acc) -> Acc;
sum_abs_diff([H|T], M, Acc) ->
    sum_abs_diff(T, M, Acc + erlang:abs(H - M)).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves2(nums :: [integer]) :: integer
  def min_moves2(nums) do
    sorted = Enum.sort(nums)
    len = length(sorted)
    median = Enum.at(sorted, div(len, 2))

    Enum.reduce(sorted, 0, fn x, acc -> acc + abs(x - median) end)
  end
end
```
