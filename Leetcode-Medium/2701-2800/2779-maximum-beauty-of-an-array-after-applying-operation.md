# 2779. Maximum Beauty of an Array After Applying Operation

## Cpp

```cpp
class Solution {
public:
    int maximumBeauty(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        long long limit = 2LL * k;
        int right = 0, ans = 0;
        for (int left = 0; left < n; ++left) {
            while (right < n && static_cast<long long>(nums[right]) - nums[left] <= limit) {
                ++right;
            }
            ans = std::max(ans, right - left);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumBeauty(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int maxBeauty = 0;
        int right = 0;
        long limit = 2L * k;
        for (int left = 0; left < n; left++) {
            while (right < n && (long) nums[right] - nums[left] <= limit) {
                right++;
            }
            maxBeauty = Math.max(maxBeauty, right - left);
        }
        return maxBeauty;
    }
}
```

## Python

```python
class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        max_beauty = 0
        limit = 2 * k
        for right in range(len(nums)):
            while nums[right] - nums[left] > limit:
                left += 1
            current_len = right - left + 1
            if current_len > max_beauty:
                max_beauty = current_len
        return max_beauty
```

## Python3

```python
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_beauty = 0
        right = 0
        limit = 2 * k
        for left in range(n):
            while right < n and nums[right] - nums[left] <= limit:
                right += 1
            max_beauty = max(max_beauty, right - left)
        return max_beauty
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int maximumBeauty(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    int maxBeauty = 0;
    int right = 0;
    long long limit = 2LL * k; // use long long to avoid overflow
    
    for (int left = 0; left < numsSize; ++left) {
        while (right < numsSize && (long long)nums[right] - (long long)nums[left] <= limit) {
            ++right;
        }
        int currentLen = right - left;
        if (currentLen > maxBeauty) maxBeauty = currentLen;
    }
    
    return maxBeauty;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumBeauty(int[] nums, int k)
    {
        Array.Sort(nums);
        int n = nums.Length;
        int left = 0;
        int maxBeauty = 0;
        long limit = 2L * k;

        for (int right = 0; right < n; ++right)
        {
            while (nums[right] - nums[left] > limit)
                left++;

            int length = right - left + 1;
            if (length > maxBeauty)
                maxBeauty = length;
        }

        return maxBeauty;
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
var maximumBeauty = function(nums, k) {
    nums.sort((a, b) => a - b);
    let left = 0;
    let maxLen = 0;
    const limit = 2 * k;
    for (let right = 0; right < nums.length; right++) {
        while (nums[right] - nums[left] > limit) {
            left++;
        }
        const curLen = right - left + 1;
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
};
```

## Typescript

```typescript
function maximumBeauty(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let maxBeauty = 0;
    let right = 0;
    const limit = 2 * k;
    for (let left = 0; left < n; left++) {
        while (right < n && nums[right] - nums[left] <= limit) {
            right++;
        }
        const currentLen = right - left;
        if (currentLen > maxBeauty) {
            maxBeauty = currentLen;
        }
    }
    return maxBeauty;
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
    function maximumBeauty($nums, $k) {
        sort($nums);
        $n = count($nums);
        $maxBeauty = 0;
        $right = 0;
        $limit = 2 * $k;
        for ($left = 0; $left < $n; $left++) {
            while ($right < $n && $nums[$right] - $nums[$left] <= $limit) {
                $right++;
            }
            $len = $right - $left;
            if ($len > $maxBeauty) {
                $maxBeauty = $len;
            }
        }
        return $maxBeauty;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBeauty(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var maxBeauty = 0
        var right = 0
        let n = sorted.count
        let limit = 2 * k
        
        for left in 0..<n {
            while right < n && sorted[right] - sorted[left] <= limit {
                right += 1
            }
            maxBeauty = max(maxBeauty, right - left)
        }
        
        return maxBeauty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBeauty(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (n == 0) return 0
        nums.sort()
        var maxBeauty = 0
        var right = 0
        val limit = 2L * k
        for (left in 0 until n) {
            while (right < n && nums[right].toLong() - nums[left].toLong() <= limit) {
                right++
            }
            val len = right - left
            if (len > maxBeauty) maxBeauty = len
        }
        return maxBeauty
    }
}
```

## Dart

```dart
class Solution {
  int maximumBeauty(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    int left = 0;
    int maxBeauty = 0;
    for (int right = 0; right < n; ++right) {
      while (nums[right] - nums[left] > 2 * k) {
        left++;
      }
      int len = right - left + 1;
      if (len > maxBeauty) {
        maxBeauty = len;
      }
    }
    return maxBeauty;
  }
}
```

## Golang

```go
import "sort"

func maximumBeauty(nums []int, k int) int {
    sort.Ints(nums)
    n := len(nums)
    maxBeauty := 0
    right := 0
    limit := 2 * k
    for left := 0; left < n; left++ {
        for right < n && nums[right]-nums[left] <= limit {
            right++
        }
        if cur := right - left; cur > maxBeauty {
            maxBeauty = cur
        }
    }
    return maxBeauty
}
```

## Ruby

```ruby
def maximum_beauty(nums, k)
  nums.sort!
  left = 0
  max_beauty = 0
  nums.each_with_index do |val, right|
    while val - nums[left] > 2 * k
      left += 1
    end
    cur_len = right - left + 1
    max_beauty = cur_len if cur_len > max_beauty
  end
  max_beauty
end
```

## Scala

```scala
object Solution {
  def maximumBeauty(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    var maxBeauty = 0
    var right = 0
    val n = sorted.length
    var left = 0
    while (left < n) {
      while (right < n && sorted(right).toLong - sorted(left).toLong <= 2L * k) {
        right += 1
      }
      maxBeauty = math.max(maxBeauty, right - left)
      left += 1
    }
    maxBeauty
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_beauty(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut max_beauty = 0usize;
        let mut right = 0usize;
        let limit = 2 * k;
        for left in 0..n {
            while right < n && nums[right] - nums[left] <= limit {
                right += 1;
            }
            let len = right - left;
            if len > max_beauty {
                max_beauty = len;
            }
        }
        max_beauty as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-beauty nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (vec (list->vector sorted)))
    (let loop ((left 0) (right 0) (ans 0))
      (if (= left n)
          ans
          (let ((new-right
                 (let recur ((r right))
                   (if (and (< r n)
                            (<= (- (vector-ref vec r)
                                   (vector-ref vec left))
                                (* 2 k)))
                       (recur (+ r 1))
                       r))))
            (let ((len (- new-right left)))
              (loop (+ left 1) new-right (if (> len ans) len ans))))))))
```

## Erlang

```erlang
-spec maximum_beauty([integer()], integer()) -> integer().
maximum_beauty(Nums, K) ->
    Sorted = lists:sort(Nums),
    Tuple = list_to_tuple(Sorted),
    Len = tuple_size(Tuple),
    loop(1, 1, Len, Tuple, 0, K).

loop(Left, _Right, Len, _Tuple, Max, _K) when Left > Len ->
    Max;
loop(Left, Right, Len, Tuple, Max, K) ->
    NewRight = expand(Right, Left, Len, Tuple, K),
    CurrLen = NewRight - Left + 1,
    NewMax = if CurrLen > Max -> CurrLen; true -> Max end,
    loop(Left + 1, NewRight, Len, Tuple, NewMax, K).

expand(Right, Left, Len, Tuple, K) when Right < Len ->
    NextVal = element(Right + 1, Tuple),
    LeftVal = element(Left, Tuple),
    if
        NextVal - LeftVal =< 2 * K -> expand(Right + 1, Left, Len, Tuple, K);
        true -> Right
    end;
expand(Right, _Left, _Len, _Tuple, _K) ->
    Right.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(nums :: [integer], k :: integer) :: integer
  def maximum_beauty(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    n = tuple_size(arr)
    limit = 2 * k
    max_beauty(0, 0, 0, arr, limit, n)
  end

  defp max_beauty(left, right, best, _arr, _limit, n) when left >= n do
    best
  end

  defp max_beauty(left, right, best, arr, limit, n) do
    new_right = expand(right, left, arr, limit, n)
    new_best = if new_right - left > best, do: new_right - left, else: best
    max_beauty(left + 1, new_right, new_best, arr, limit, n)
  end

  defp expand(right, left, _arr, _limit, n) when right >= n, do: right

  defp expand(right, left, arr, limit, n) do
    if elem(arr, right) - elem(arr, left) <= limit do
      expand(right + 1, left, arr, limit, n)
    else
      right
    end
  end
end
```
