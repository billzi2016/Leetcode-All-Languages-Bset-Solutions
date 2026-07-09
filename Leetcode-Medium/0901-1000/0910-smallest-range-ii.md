# 0910. Smallest Range II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int smallestRangeII(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = nums.back() - nums.front(); // no changes
        for (int i = 0; i < n - 1; ++i) {
            int high = max(nums[i] + k, nums.back() - k);
            int low  = min(nums[0] + k, nums[i + 1] - k);
            ans = min(ans, high - low);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int smallestRangeII(int[] nums, int k) {
        int n = nums.length;
        if (n == 1) return 0;
        java.util.Arrays.sort(nums);
        int ans = nums[n - 1] - nums[0];
        for (int i = 0; i < n - 1; i++) {
            int high = Math.max(nums[i] + k, nums[n - 1] - k);
            int low = Math.min(nums[0] + k, nums[i + 1] - k);
            ans = Math.min(ans, high - low);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # initial range without any changes
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            low = min(nums[0] + k, nums[i + 1] - k)
            high = max(nums[-1] - k, nums[i] + k)
            ans = min(ans, high - low)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int smallestRangeII(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int ans = nums[numsSize - 1] - nums[0];
    for (int i = 0; i < numsSize - 1; ++i) {
        int high = nums[i] + k;
        int low  = nums[i + 1] - k;
        
        int curMax = high > (nums[numsSize - 1] - k) ? high : (nums[numsSize - 1] - k);
        int curMin = low  < (nums[0] + k)       ? low  : (nums[0] + k);
        
        int diff = curMax - curMin;
        if (diff < ans) ans = diff;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestRangeII(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length;
        int answer = nums[n - 1] - nums[0];
        for (int i = 0; i < n - 1; ++i) {
            int high = Math.Max(nums[i] + k, nums[n - 1] - k);
            int low = Math.Min(nums[0] + k, nums[i + 1] - k);
            answer = Math.Min(answer, high - low);
        }
        return answer;
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
var smallestRangeII = function(nums, k) {
    const n = nums.length;
    if (n === 1) return 0;
    nums.sort((a, b) => a - b);
    let ans = nums[n - 1] - nums[0];
    for (let i = 0; i < n - 1; ++i) {
        const high = Math.max(nums[i] + k, nums[n - 1] - k);
        const low = Math.min(nums[0] + k, nums[i + 1] - k);
        ans = Math.min(ans, high - low);
    }
    return ans;
};
```

## Typescript

```typescript
function smallestRangeII(nums: number[], k: number): number {
    const n = nums.length;
    if (n === 0) return 0;
    nums.sort((a, b) => a - b);
    let ans = nums[n - 1] - nums[0];
    for (let i = 0; i < n - 1; i++) {
        const high = Math.max(nums[i] + k, nums[n - 1] - k);
        const low = Math.min(nums[0] + k, nums[i + 1] - k);
        ans = Math.min(ans, high - low);
    }
    return ans;
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
    function smallestRangeII($nums, $k) {
        sort($nums);
        $n = count($nums);
        if ($n == 1) return 0;
        $ans = $nums[$n - 1] - $nums[0];
        for ($i = 0; $i < $n - 1; $i++) {
            $high = max($nums[$i] + $k, $nums[$n - 1] - $k);
            $low = min($nums[0] + $k, $nums[$i + 1] - $k);
            $ans = min($ans, $high - $low);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func smallestRangeII(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        var answer = sorted[n - 1] - sorted[0]
        if k == 0 { return answer }
        for i in 0..<(n - 1) {
            let high = max(sorted[i] + k, sorted[n - 1] - k)
            let low = min(sorted[0] + k, sorted[i + 1] - k)
            answer = min(answer, high - low)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestRangeII(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (n == 1) return 0
        nums.sort()
        var answer = nums[n - 1] - nums[0]
        for (i in 0 until n - 1) {
            val high = maxOf(nums[i] + k, nums[n - 1] - k)
            val low = minOf(nums[0] + k, nums[i + 1] - k)
            answer = minOf(answer, high - low)
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int smallestRangeII(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    int ans = nums[n - 1] - nums[0];
    for (int i = 0; i < n - 1; ++i) {
      int high = max(nums[i] + k, nums[n - 1] - k);
      int low = min(nums[0] + k, nums[i + 1] - k);
      ans = min(ans, high - low);
    }
    return ans;
  }
}
```

## Golang

```go
func smallestRangeII(nums []int, k int) int {
    if len(nums) == 0 {
        return 0
    }
    sort.Ints(nums)
    n := len(nums)
    ans := nums[n-1] - nums[0]
    for i := 0; i < n-1; i++ {
        high := max(nums[n-1]-k, nums[i]+k)
        low := min(nums[0]+k, nums[i+1]-k)
        if diff := high - low; diff < ans {
            ans = diff
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def smallest_range_ii(nums, k)
  nums.sort!
  n = nums.length
  return 0 if n == 1
  ans = nums[-1] - nums[0]
  (0...n-1).each do |i|
    high = [nums[i] + k, nums[-1] - k].max
    low = [nums[0] + k, nums[i+1] - k].min
    ans = [ans, high - low].min
  end
  ans
end
```

## Scala

```scala
object Solution {
    def smallestRangeII(nums: Array[Int], k: Int): Int = {
        val a = nums.sorted
        val n = a.length
        var ans = a(n - 1) - a(0)
        for (i <- 0 until n - 1) {
            val high = Math.max(a(i) + k, a(n - 1) - k)
            val low = Math.min(a(0) + k, a(i + 1) - k)
            ans = Math.min(ans, high - low)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_range_ii(mut nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        nums.sort_unstable();
        let mut ans = nums[n - 1] - nums[0];
        for i in 0..n - 1 {
            let high = std::cmp::max(nums[i] + k, nums[n - 1] - k);
            let low = std::cmp::min(nums[0] + k, nums[i + 1] - k);
            ans = ans.min(high - low);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (smallest-range-ii nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted-list (sort nums <))
         (sorted (list->vector sorted-list))
         (n (vector-length sorted)))
    (if (= n 1)
        0
        (let loop ((i 0)
                   (ans (- (vector-ref sorted (sub1 n)) (vector-ref sorted 0))))
          (if (> i (- n 2))
              ans
              (let* ((high (max (+ (vector-ref sorted i) k)
                                (- (vector-ref sorted (sub1 n)) k)))
                     (low  (min (+ (vector-ref sorted 0) k)
                                (- (vector-ref sorted (+ i 1)) k)))
                     (new-ans (min ans (- high low))))
                (loop (+ i 1) new-ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_range_ii/2]).

-spec smallest_range_ii(Nums :: [integer()], K :: integer()) -> integer().
smallest_range_ii(Nums, K) ->
    Sorted = lists:sort(Nums),
    case Sorted of
        [] -> 0;
        [_] -> 0;
        _ ->
            Min = hd(Sorted),
            Max = lists:last(Sorted),
            InitialAns = Max - Min,
            MinPlusK = Min + K,
            MaxMinusK = Max - K,
            [Prev | Rest] = Sorted,
            loop(Prev, Rest, MinPlusK, MaxMinusK, K, InitialAns)
    end.

loop(_Prev, [], _MinPlusK, _MaxMinusK, _K, Ans) ->
    Ans;
loop(Prev, [Next | Tail], MinPlusK, MaxMinusK, K, CurrentAns) ->
    CurMax = erlang:max(Prev + K, MaxMinusK),
    CurMin = erlang:min(MinPlusK, Next - K),
    Diff = CurMax - CurMin,
    NewAns = if Diff < CurrentAns -> Diff; true -> CurrentAns end,
    loop(Next, Tail, MinPlusK, MaxMinusK, K, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_range_ii(nums :: [integer], k :: integer) :: integer
  def smallest_range_ii(nums, k) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    if n <= 1 do
      0
    else
      min_val = hd(sorted)
      max_val = List.last(sorted)
      init = max_val - min_val

      0..(n - 2)
      |> Enum.reduce(init, fn i, acc ->
        high = max(Enum.at(sorted, i) + k, max_val - k)
        low = min(min_val + k, Enum.at(sorted, i + 1) - k)
        range = high - low
        if range < acc, do: range, else: acc
      end)
    end
  end
end
```
