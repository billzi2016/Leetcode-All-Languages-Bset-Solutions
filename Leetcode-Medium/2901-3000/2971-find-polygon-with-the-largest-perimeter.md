# 2971. Find Polygon With the Largest Perimeter

## Cpp

```cpp
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long sum = 0;
        long long ans = -1;
        for (int x : nums) {
            if (x < sum) {
                ans = max(ans, sum + x);
            }
            sum += x;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long sum = 0;
        long ans = -1;
        for (int i = 0; i < nums.length; i++) {
            if (i >= 2 && nums[i] < sum) {
                ans = Math.max(ans, sum + nums[i]);
            }
            sum += nums[i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        ans = -1
        for length in nums:
            if length < total:
                ans = total + length
            total += length
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix = 0
        best = -1
        for i, x in enumerate(nums):
            if i >= 2 and x < prefix:
                best = max(best, prefix + x)
            prefix += x
        return best
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

long long largestPerimeter(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    long long sum = 0;
    long long ans = -1;
    for (int i = 0; i < numsSize; ++i) {
        if (i >= 2 && (long long)nums[i] < sum) {
            ans = sum + nums[i];
        }
        sum += nums[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long LargestPerimeter(int[] nums)
    {
        Array.Sort(nums);
        long prefixSum = 0;
        long best = -1;
        foreach (int length in nums)
        {
            if (prefixSum > length)
            {
                best = prefixSum + length;
            }
            prefixSum += length;
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    nums.sort((a, b) => a - b);
    let sum = 0;
    let ans = -1;
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] < sum) {
            ans = sum + nums[i];
        }
        sum += nums[i];
    }
    return ans;
};
```

## Typescript

```typescript
function largestPerimeter(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let sum = 0;
    let ans = -1;
    for (const len of nums) {
        if (sum > len) {
            ans = sum + len;
        }
        sum += len;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestPerimeter($nums) {
        sort($nums, SORT_NUMERIC);
        $sum = 0;
        $ans = -1;
        foreach ($nums as $num) {
            if ($num < $sum) {
                $ans = $sum + $num;
            }
            $sum += $num;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var prefixSum = 0
        var result = -1
        for num in sortedNums {
            if num < prefixSum {
                result = prefixSum + num
            }
            prefixSum += num
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPerimeter(nums: IntArray): Long {
        nums.sort()
        var sumPrev = 0L
        var answer = -1L
        for (value in nums) {
            val cur = value.toLong()
            if (cur < sumPrev) {
                answer = sumPrev + cur
            }
            sumPrev += cur
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int largestPerimeter(List<int> nums) {
    nums.sort();
    int sum = 0;
    int ans = -1;
    for (int num in nums) {
      if (num < sum) {
        int perim = sum + num;
        if (perim > ans) ans = perim;
      }
      sum += num;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func largestPerimeter(nums []int) int64 {
    sort.Ints(nums)
    var prefix int64 = 0
    var ans int64 = -1
    for _, v := range nums {
        cur := int64(v)
        if cur < prefix {
            perim := prefix + cur
            if perim > ans {
                ans = perim
            }
        }
        prefix += cur
    }
    return ans
}
```

## Ruby

```ruby
def largest_perimeter(nums)
  nums.sort!
  sum = 0
  ans = -1
  nums.each do |len|
    ans = sum + len if len < sum
    sum += len
  end
  ans
end
```

## Scala

```scala
object Solution {
    def largestPerimeter(nums: Array[Int]): Long = {
        val sorted = nums.sorted
        var sum: Long = 0L
        var ans: Long = -1L
        for (x <- sorted) {
            val cur = x.toLong
            if (cur < sum) {
                ans = sum + cur
            }
            sum += cur
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        let mut v: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        v.sort_unstable();
        let mut sum: i64 = 0;
        let mut ans: i64 = -1;
        for &num in &v {
            if num < sum {
                ans = sum + num;
            }
            sum += num;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (largest-perimeter nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <)))
    (let loop ((i 0) (sum 0) (ans -1) (lst sorted))
      (if (null? lst)
          ans
          (let* ((x (car lst))
                 (new-ans (if (and (>= i 2) (< x sum))
                              (+ x sum)
                              ans)))
            (loop (+ i 1) (+ sum x) new-ans (cdr lst)))))))
```

## Erlang

```erlang
-spec largest_perimeter([integer()]) -> integer().
largest_perimeter(Nums) ->
    Sorted = lists:sort(Nums),
    {_, Answer} = lists:foldl(
        fun(Num, {Sum, CurAns}) ->
            NewAns = case Num < Sum of
                true -> Sum + Num;
                false -> CurAns
            end,
            {Sum + Num, NewAns}
        end,
        {0, -1},
        Sorted),
    Answer.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_perimeter(nums :: [integer]) :: integer
  def largest_perimeter(nums) do
    sorted = Enum.sort(nums)

    {ans, _sum, _cnt} =
      Enum.reduce(sorted, {-1, 0, 0}, fn x, {best, sum, cnt} ->
        new_best =
          if cnt >= 2 and sum > x do
            max(best, sum + x)
          else
            best
          end

        {new_best, sum + x, cnt + 1}
      end)

    ans
  end
end
```
