# 1493. Longest Subarray of 1's After Deleting One Element

## Cpp

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0, zeroCount = 0, best = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            if (nums[right] == 0) ++zeroCount;
            while (zeroCount > 1) {
                if (nums[left] == 0) --zeroCount;
                ++left;
            }
            best = max(best, right - left);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0;
        int zeroCount = 0;
        int longest = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }
            while (zeroCount > 1) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            // window size minus one (the element to delete)
            longest = Math.max(longest, right - left);
        }
        return longest;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_cnt = 0
        best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zero_cnt += 1
            while zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            best = max(best, right - left)
        return best
```

## Python3

```python
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zero_count = 0
        best = 0
        for end, v in enumerate(nums):
            if v == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            best = max(best, end - start)
        return best
```

## C

```c
int longestSubarray(int* nums, int numsSize) {
    int start = 0;
    int zeroCount = 0;
    int longest = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) {
            zeroCount++;
        }
        while (zeroCount > 1) {
            if (nums[start] == 0) {
                zeroCount--;
            }
            start++;
        }
        // window length is (i - start + 1), after deleting one element it becomes minus 1
        int current = i - start; // equivalent to (i - start + 1) - 1
        if (current > longest) {
            longest = current;
        }
    }
    return longest;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestSubarray(int[] nums) {
        int start = 0, zeroCount = 0, maxLen = 0;
        for (int end = 0; end < nums.Length; end++) {
            if (nums[end] == 0) zeroCount++;
            while (zeroCount > 1) {
                if (nums[start] == 0) zeroCount--;
                start++;
            }
            // window size minus one (the element to delete)
            maxLen = Math.Max(maxLen, end - start);
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let left = 0;
    let zeroCount = 0;
    let best = 0;
    for (let right = 0; right < nums.length; ++right) {
        if (nums[right] === 0) zeroCount++;
        while (zeroCount > 1) {
            if (nums[left] === 0) zeroCount--;
            left++;
        }
        // window size is right - left + 1, we delete one element
        best = Math.max(best, right - left);
    }
    return best;
};
```

## Typescript

```typescript
function longestSubarray(nums: number[]): number {
    let start = 0;
    let zeroCount = 0;
    let maxLen = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) zeroCount++;

        while (zeroCount > 1) {
            if (nums[start] === 0) zeroCount--;
            start++;
        }

        // window length minus one element to delete
        maxLen = Math.max(maxLen, i - start);
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubarray($nums) {
        $start = 0;
        $zeroCount = 0;
        $maxLen = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] == 0) {
                $zeroCount++;
            }
            while ($zeroCount > 1) {
                if ($nums[$start] == 0) {
                    $zeroCount--;
                }
                $start++;
            }
            // window size minus one (the element to delete)
            $maxLen = max($maxLen, $i - $start);
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        var left = 0
        var zeroCount = 0
        var result = 0
        
        for right in 0..<nums.count {
            if nums[right] == 0 {
                zeroCount += 1
            }
            while zeroCount > 1 {
                if nums[left] == 0 {
                    zeroCount -= 1
                }
                left += 1
            }
            result = max(result, right - left)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var left = 0
        var zeroCount = 0
        var maxLen = 0
        for (right in nums.indices) {
            if (nums[right] == 0) zeroCount++
            while (zeroCount > 1) {
                if (nums[left] == 0) zeroCount--
                left++
            }
            // length of window minus one element to delete
            maxLen = kotlin.math.max(maxLen, right - left)
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestSubarray(List<int> nums) {
    int start = 0;
    int zeroCount = 0;
    int maxLen = 0;

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 0) zeroCount++;

      while (zeroCount > 1) {
        if (nums[start] == 0) zeroCount--;
        start++;
      }

      int current = i - start; // window size minus one (the deleted element)
      if (current > maxLen) maxLen = current;
    }

    return maxLen;
  }
}
```

## Golang

```go
func longestSubarray(nums []int) int {
    start, zeroCount, ans := 0, 0, 0
    for end, v := range nums {
        if v == 0 {
            zeroCount++
        }
        for zeroCount > 1 {
            if nums[start] == 0 {
                zeroCount--
            }
            start++
        }
        if cur := end - start; cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_subarray(nums)
  start = 0
  zero_count = 0
  max_len = 0
  nums.each_with_index do |num, i|
    zero_count += 1 if num == 0
    while zero_count > 1
      zero_count -= 1 if nums[start] == 0
      start += 1
    end
    max_len = [max_len, i - start].max
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestSubarray(nums: Array[Int]): Int = {
        var zeroCount = 0
        var left = 0
        var ans = 0
        for (right <- nums.indices) {
            if (nums(right) == 0) zeroCount += 1
            while (zeroCount > 1) {
                if (nums(left) == 0) zeroCount -= 1
                left += 1
            }
            ans = math.max(ans, right - left)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut start = 0usize;
        let mut zero_count = 0i32;
        let mut best = 0usize;

        for (i, &v) in nums.iter().enumerate() {
            if v == 0 {
                zero_count += 1;
            }
            while zero_count > 1 {
                if nums[start] == 0 {
                    zero_count -= 1;
                }
                start += 1;
            }
            // window size minus one (the element to delete)
            let len = i - start;
            if len > best {
                best = len;
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (longest-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    ;; shrink window until at most one zero remains
    (define (shrink start zero-count)
      (if (<= zero-count 1)
          (values start zero-count)
          (let ((new-zero-count (if (= (vector-ref v start) 0)
                                   (- zero-count 1)
                                   zero-count)))
            (shrink (+ start 1) new-zero-count))))
    ;; main sliding‑window loop
    (let loop ((i 0) (start 0) (zero-count 0) (best 0))
      (if (= i n)
          best
          (let* ((zc (if (= (vector-ref v i) 0)
                         (+ zero-count 1)
                         zero-count))
                 (values (shrink start zc)))
            (let-values ([(new-start new-zero-count) values])
              (let ((new-best (max best (- i new-start))))
                (loop (+ i 1) new-start new-zero-count new-best))))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_subarray/1]).
 
-spec longest_subarray(Nums :: [integer()]) -> integer().
longest_subarray(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    loop(0, Len, Tuple, 0, 0, 0).
 
loop(I, Len, _Tuple, _Start, _ZeroCount, Max) when I == Len ->
    Max;
loop(I, Len, Tuple, Start, ZeroCount, Max) ->
    Elem = element(I + 1, Tuple),
    ZC1 = case Elem of
        0 -> ZeroCount + 1;
        _ -> ZeroCount
    end,
    {NewStart, NewZero} =
        if ZC1 > 1 ->
                shrink(Tuple, Start, ZC1);
           true ->
                {Start, ZC1}
        end,
    CurrLen = I - NewStart,
    NewMax = case CurrLen > Max of
        true -> CurrLen;
        false -> Max
    end,
    loop(I + 1, Len, Tuple, NewStart, NewZero, NewMax).
 
shrink(Tuple, Start, ZeroCount) when ZeroCount =< 1 ->
    {Start, ZeroCount};
shrink(Tuple, Start, ZeroCount) ->
    Elem = element(Start + 1, Tuple),
    NZC = case Elem of
        0 -> ZeroCount - 1;
        _ -> ZeroCount
    end,
    shrink(Tuple, Start + 1, NZC).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer]) :: integer
  def longest_subarray(nums) do
    {runs_rev, cur} =
      Enum.reduce(nums, {[], 0}, fn
        1, {runs, cnt} -> {runs, cnt + 1}
        0, {runs, cnt} -> {[cnt | runs], 0}
      end)

    runs = Enum.reverse([cur | runs_rev])

    case length(runs) do
      1 ->
        max(0, hd(runs) - 1)

      _ ->
        runs
        |> Enum.chunk_every(2, 1, :discard)
        |> Enum.map(fn [a, b] -> a + b end)
        |> Enum.max()
    end
  end
end
```
