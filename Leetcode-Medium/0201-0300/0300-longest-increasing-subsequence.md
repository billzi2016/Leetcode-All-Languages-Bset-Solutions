# 0300. Longest Increasing Subsequence

## Cpp

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        for (int x : nums) {
            auto it = lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) {
                tails.push_back(x);
            } else {
                *it = x;
            }
        }
        return static_cast<int>(tails.size());
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] tails = new int[n];
        int size = 0;
        for (int x : nums) {
            int i = Arrays.binarySearch(tails, 0, size, x);
            if (i < 0) i = -(i + 1);
            tails[i] = x;
            if (i == size) {
                size++;
            }
        }
        return size;
    }
}
```

## Python

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
```

## Python3

```python
from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
```

## C

```c
#include <stdlib.h>

int lengthOfLIS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *tails = (int *)malloc(numsSize * sizeof(int));
    int size = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int l = 0, r = size;
        while (l < r) {
            int m = (l + r) / 2;
            if (tails[m] < x)
                l = m + 1;
            else
                r = m;
        }
        tails[l] = x;
        if (l == size) ++size;
    }
    free(tails);
    return size;
}
```

## Csharp

```csharp
public class Solution
{
    public int LengthOfLIS(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;

        int[] tails = new int[nums.Length];
        int size = 0;

        foreach (int x in nums)
        {
            int i = System.Array.BinarySearch(tails, 0, size, x);
            if (i < 0) i = ~i; // insertion point
            tails[i] = x;
            if (i == size) size++;
        }

        return size;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const tails = [];
    for (const x of nums) {
        let left = 0, right = tails.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (tails[mid] < x) left = mid + 1;
            else right = mid;
        }
        if (left === tails.length) tails.push(x);
        else tails[left] = x;
    }
    return tails.length;
};
```

## Typescript

```typescript
function lengthOfLIS(nums: number[]): number {
    const tails: number[] = [];
    for (const num of nums) {
        let left = 0, right = tails.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (tails[mid] < num) left = mid + 1;
            else right = mid;
        }
        if (left === tails.length) tails.push(num);
        else tails[left] = num;
    }
    return tails.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function lengthOfLIS($nums) {
        $tails = [];
        foreach ($nums as $num) {
            $left = 0;
            $right = count($tails);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($tails[$mid] < $num) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            if ($left == count($tails)) {
                $tails[] = $num;
            } else {
                $tails[$left] = $num;
            }
        }
        return count($tails);
    }
}
```

## Swift

```swift
class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var tails = [Int]()
        for num in nums {
            var left = 0
            var right = tails.count
            while left < right {
                let mid = (left + right) / 2
                if tails[mid] < num {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if left == tails.count {
                tails.append(num)
            } else {
                tails[left] = num
            }
        }
        return tails.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val tails = IntArray(nums.size)
        var size = 0
        for (x in nums) {
            var l = 0
            var r = size
            while (l < r) {
                val m = (l + r) ushr 1
                if (tails[m] < x) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            tails[l] = x
            if (l == size) size++
        }
        return size
    }
}
```

## Dart

```dart
class Solution {
  int lengthOfLIS(List<int> nums) {
    List<int> tails = [];
    for (int x in nums) {
      int left = 0;
      int right = tails.length;
      while (left < right) {
        int mid = (left + right) >> 1;
        if (tails[mid] < x) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
      if (left == tails.length) {
        tails.add(x);
      } else {
        tails[left] = x;
      }
    }
    return tails.length;
  }
}
```

## Golang

```go
import "sort"

func lengthOfLIS(nums []int) int {
    tails := make([]int, 0)
    for _, x := range nums {
        i := sort.Search(len(tails), func(i int) bool { return tails[i] >= x })
        if i == len(tails) {
            tails = append(tails, x)
        } else {
            tails[i] = x
        }
    }
    return len(tails)
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
  tails = []
  nums.each do |x|
    l = 0
    r = tails.length
    while l < r
      m = (l + r) / 2
      if tails[m] < x
        l = m + 1
      else
        r = m
      end
    end
    if l == tails.length
      tails << x
    else
      tails[l] = x
    end
  end
  tails.length
end
```

## Scala

```scala
object Solution {
  def lengthOfLIS(nums: Array[Int]): Int = {
    if (nums.isEmpty) return 0
    val dp = new Array[Int](nums.length)
    var len = 0
    for (x <- nums) {
      var i = 0
      var j = len
      while (i < j) {
        val m = (i + j) >>> 1
        if (dp(m) < x) i = m + 1 else j = m
      }
      dp(i) = x
      if (i == len) len += 1
    }
    len
  }
}
```

## Rust

```rust
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut tails: Vec<i32> = Vec::new();
        for num in nums {
            match tails.binary_search(&num) {
                Ok(idx) => tails[idx] = num,
                Err(idx) => {
                    if idx == tails.len() {
                        tails.push(num);
                    } else {
                        tails[idx] = num;
                    }
                }
            }
        }
        tails.len() as i32
    }
}
```

## Racket

```racket
(define/contract (length-of-lis nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (tails (make-vector n 0))
         (size 0))
    (for ([x nums])
      (let loop ((l 0) (r size))
        (if (= l r)
            (begin
              (vector-set! tails l x)
              (when (= l size) (set! size (+ size 1))))
            (let* ((mid (quotient (+ l r) 2))
                   (mid-val (vector-ref tails mid)))
              (if (< mid-val x)
                  (loop (+ mid 1) r)
                  (loop l mid))))))
    size))
```

## Erlang

```erlang
-module(solution).
-export([length_of_lis/1]).

-spec length_of_lis(Nums :: [integer()]) -> integer().
length_of_lis(Nums) ->
    case Nums of
        [] -> 0;
        _ ->
            NumT = list_to_tuple(Nums),
            N = tuple_size(NumT),
            DPInit = erlang:make_tuple(N, 0),
            outer_loop(1, N, NumT, DPInit, 0)
    end.

outer_loop(I, N, _NumT, _DP, Max) when I > N ->
    Max;
outer_loop(I, N, NumT, DP, MaxSoFar) ->
    BestPrev = inner_loop(I, 1, I - 1, NumT, DP, 0),
    NewVal = BestPrev + 1,
    DP2 = setelement(I, DP, NewVal),
    NewMax = if NewVal > MaxSoFar -> NewVal; true -> MaxSoFar end,
    outer_loop(I + 1, N, NumT, DP2, NewMax).

inner_loop(_I, J, End, _NumT, _DP, Max) when J > End ->
    Max;
inner_loop(I, J, End, NumT, DP, Max) ->
    case element(J, NumT) < element(I, NumT) of
        true ->
            Val = element(J, DP),
            NewMax = if Val > Max -> Val; true -> Max end,
            inner_loop(I, J + 1, End, NumT, DP, NewMax);
        false ->
            inner_loop(I, J + 1, End, NumT, DP, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec length_of_lis(nums :: [integer]) :: integer
  def length_of_lis(nums) do
    tails =
      Enum.reduce(nums, [], fn x, tails ->
        pos = lower_bound(tails, x)

        if pos == length(tails) do
          tails ++ [x]
        else
          List.replace_at(tails, pos, x)
        end
      end)

    length(tails)
  end

  defp lower_bound(list, target) do
    lower_bound(list, target, 0, length(list))
  end

  defp lower_bound(_list, _target, lo, hi) when lo >= hi, do: lo

  defp lower_bound(list, target, lo, hi) do
    mid = div(lo + hi, 2)
    val = Enum.at(list, mid)

    if val < target do
      lower_bound(list, target, mid + 1, hi)
    else
      lower_bound(list, target, lo, mid)
    end
  end
end
```
