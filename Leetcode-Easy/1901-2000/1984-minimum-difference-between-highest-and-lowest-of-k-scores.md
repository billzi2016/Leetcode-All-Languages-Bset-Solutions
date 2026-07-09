# 1984. Minimum Difference Between Highest and Lowest of K Scores

## Cpp

```cpp
class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 0; i + k - 1 < (int)nums.size(); ++i) {
            ans = min(ans, nums[i + k - 1] - nums[i]);
        }
        return ans == INT_MAX ? 0 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumDifference(int[] nums, int k) {
        if (k == 1) return 0;
        java.util.Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i + k - 1 < nums.length; i++) {
            int diff = nums[i + k - 1] - nums[i];
            if (diff < minDiff) minDiff = diff;
        }
        return minDiff;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
```

## Python3

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff if min_diff != float('inf') else 0
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int minimumDifference(int* nums, int numsSize, int k) {
    if (k <= 1) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int minDiff = INT_MAX;
    for (int i = 0; i + k - 1 < numsSize; ++i) {
        int diff = nums[i + k - 1] - nums[i];
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        if (k <= 1) return 0;
        Array.Sort(nums);
        int minDiff = int.MaxValue;
        for (int i = 0; i + k - 1 < nums.Length; i++) {
            int diff = nums[i + k - 1] - nums[i];
            if (diff < minDiff) minDiff = diff;
        }
        return minDiff;
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
var minimumDifference = function(nums, k) {
    if (k === 1) return 0;
    nums.sort((a, b) => a - b);
    let minDiff = Infinity;
    for (let i = 0; i + k - 1 < nums.length; ++i) {
        const diff = nums[i + k - 1] - nums[i];
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
};
```

## Typescript

```typescript
function minimumDifference(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let minDiff = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i + k - 1 < nums.length; i++) {
        const diff = nums[i + k - 1] - nums[i];
        if (diff < minDiff) minDiff = diff;
    }
    return minDiff === Number.MAX_SAFE_INTEGER ? 0 : minDiff;
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
    function minimumDifference($nums, $k) {
        sort($nums);
        $n = count($nums);
        $minDiff = PHP_INT_MAX;
        for ($i = 0; $i <= $n - $k; $i++) {
            $diff = $nums[$i + $k - 1] - $nums[$i];
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
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        let sortedNums = nums.sorted()
        var minDiff = Int.max
        for i in 0...(sortedNums.count - k) {
            let diff = sortedNums[i + k - 1] - sortedNums[i]
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
    fun minimumDifference(nums: IntArray, k: Int): Int {
        if (k == 1) return 0
        nums.sort()
        var minDiff = Int.MAX_VALUE
        for (i in 0..nums.size - k) {
            val diff = nums[i + k - 1] - nums[i]
            if (diff < minDiff) minDiff = diff
        }
        return minDiff
    }
}
```

## Dart

```dart
class Solution {
  int minimumDifference(List<int> nums, int k) {
    if (k == 1) return 0;
    nums.sort();
    int minDiff = 1 << 30;
    for (int i = 0; i + k - 1 < nums.length; ++i) {
      int diff = nums[i + k - 1] - nums[i];
      if (diff < minDiff) minDiff = diff;
    }
    return minDiff;
  }
}
```

## Golang

```go
func minimumDifference(nums []int, k int) int {
    if k <= 1 {
        return 0
    }
    sort.Ints(nums)
    minDiff := nums[k-1] - nums[0]
    for i := 1; i+ k-1 < len(nums); i++ {
        diff := nums[i+k-1] - nums[i]
        if diff < minDiff {
            minDiff = diff
        }
    }
    return minDiff
}
```

## Ruby

```ruby
def minimum_difference(nums, k)
  return 0 if k <= 1
  nums.sort!
  min_diff = Float::INFINITY
  (0..nums.length - k).each do |i|
    diff = nums[i + k - 1] - nums[i]
    min_diff = diff if diff < min_diff
  end
  min_diff
end
```

## Scala

```scala
object Solution {
    def minimumDifference(nums: Array[Int], k: Int): Int = {
        val sorted = nums.sorted
        var minDiff = Int.MaxValue
        for (i <- 0 to sorted.length - k) {
            val diff = sorted(i + k - 1) - sorted(i)
            if (diff < minDiff) minDiff = diff
        }
        minDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let k = k as usize;
        if k <= 1 {
            return 0;
        }
        let mut ans = i32::MAX;
        for i in 0..=nums.len() - k {
            let diff = nums[i + k - 1] - nums[i];
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
(define/contract (minimum-difference nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (limit (+ 1 (- n k))))
    (apply min
           (for/list ([i (in-range 0 limit)])
             (- (list-ref sorted (+ i k -1))
                (list-ref sorted i))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_difference/2]).

-spec minimum_difference(Nums :: [integer()], K :: integer()) -> integer().
minimum_difference(Nums, K) ->
    Sorted = lists:sort(Nums),
    min_diff(Sorted, K, erlang:system_info(max_integer)).

min_diff(List, K, CurrentMin) when length(List) < K ->
    CurrentMin;
min_diff([_|Tail]=List, K, CurrentMin) ->
    {Window, _} = split_at(K, List),
    Diff = lists:last(Window) - hd(Window),
    NewMin = if Diff < CurrentMin -> Diff; true -> CurrentMin end,
    min_diff(Tail, K, NewMin).

split_at(0, L) -> {[], L};
split_at(N, []) -> {[], []};
split_at(N, [H|T]) when N > 0 ->
    {RestK, Rest} = split_at(N-1, T),
    {[H|RestK], Rest}.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_difference(nums :: [integer], k :: integer) :: integer
  def minimum_difference(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    len = tuple_size(arr)
    max_start = len - k

    init_diff = elem(arr, k - 1) - elem(arr, 0)

    Enum.reduce(1..max_start, init_diff, fn i, acc ->
      diff = elem(arr, i + k - 1) - elem(arr, i)
      if diff < acc, do: diff, else: acc
    end)
  end
end
```
