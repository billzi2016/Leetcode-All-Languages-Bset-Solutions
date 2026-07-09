# 3101. Count Alternating Subarrays

## Cpp

```cpp
class Solution {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        long long ans = 0;
        int cur = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i > 0 && nums[i] != nums[i - 1])
                ++cur;
            else
                cur = 1;
            ans += cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        long total = 0L;
        int prevLen = 0;
        for (int i = 0; i < nums.length; i++) {
            int curLen;
            if (i == 0 || nums[i] == nums[i - 1]) {
                curLen = 1;
            } else {
                curLen = prevLen + 1;
            }
            total += curLen;
            prevLen = curLen;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cur_len = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                cur_len += 1
            else:
                cur_len = 1
            total += cur_len
        return total
```

## Python3

```python
from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        total = 0
        prev_len = 0
        for i, val in enumerate(nums):
            if i > 0 and val != nums[i - 1]:
                prev_len += 1
            else:
                prev_len = 1
            total += prev_len
        return total
```

## C

```c
long long countAlternatingSubarrays(int* nums, int numsSize) {
    long long total = 0;
    long long cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i > 0 && nums[i] != nums[i - 1])
            cur += 1;
        else
            cur = 1;
        total += cur;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long CountAlternatingSubarrays(int[] nums) {
        long total = 0;
        long current = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (i > 0 && nums[i] != nums[i - 1]) {
                current += 1;
            } else {
                current = 1;
            }
            total += current;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countAlternatingSubarrays = function(nums) {
    let total = 0;
    let prevLen = 0; // dp[i-1]
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] !== nums[i - 1]) {
            prevLen += 1;
        } else {
            prevLen = 1;
        }
        total += prevLen;
    }
    return total;
};
```

## Typescript

```typescript
function countAlternatingSubarrays(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    let total = 1; // subarray consisting of the first element
    let cur = 1;   // length of current alternating suffix ending at i
    for (let i = 1; i < n; ++i) {
        if (nums[i] !== nums[i - 1]) {
            cur += 1;
        } else {
            cur = 1;
        }
        total += cur;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countAlternatingSubarrays($nums) {
        $n = count($nums);
        $ans = 0;
        $prevLen = 0; // dp for previous index

        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $nums[$i] != $nums[$i - 1]) {
                $curr = $prevLen + 1;
            } else {
                $curr = 1;
            }
            $ans += $curr;
            $prevLen = $curr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countAlternatingSubarrays(_ nums: [Int]) -> Int {
        var total = 0
        var currentLength = 0
        for i in 0..<nums.count {
            if i > 0 && nums[i] != nums[i - 1] {
                currentLength += 1
            } else {
                currentLength = 1
            }
            total += currentLength
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countAlternatingSubarrays(nums: IntArray): Long {
        var total = 0L
        var prevLen = 0L
        for (i in nums.indices) {
            if (i > 0 && nums[i] != nums[i - 1]) {
                prevLen += 1
            } else {
                prevLen = 1
            }
            total += prevLen
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int countAlternatingSubarrays(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;
    int prevCount = 1; // dp for previous index
    int total = 1; // include subarray of first element

    for (int i = 1; i < n; ++i) {
      if (nums[i] != nums[i - 1]) {
        prevCount = prevCount + 1;
      } else {
        prevCount = 1;
      }
      total += prevCount;
    }

    return total;
  }
}
```

## Golang

```go
func countAlternatingSubarrays(nums []int) int64 {
	var total int64
	var cur int64
	for i, v := range nums {
		if i > 0 && v != nums[i-1] {
			cur++
		} else {
			cur = 1
		}
		total += cur
	}
	return total
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_alternating_subarrays(nums)
  total = 0
  cur_len = 0
  nums.each_with_index do |v, i|
    if i > 0 && v != nums[i - 1]
      cur_len += 1
    else
      cur_len = 1
    end
    total += cur_len
  end
  total
end
```

## Scala

```scala
object Solution {
    def countAlternatingSubarrays(nums: Array[Int]): Long = {
        var total: Long = 0L
        var curLen: Int = 0
        for (i <- nums.indices) {
            if (i == 0 || nums(i) != nums(i - 1)) {
                curLen += 1
            } else {
                curLen = 1
            }
            total += curLen.toLong
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        let mut total: i64 = 0;
        let mut cur_len: i64 = 0;
        let mut prev: i32 = -1; // sentinel different from 0 and 1
        for &v in nums.iter() {
            if v != prev {
                cur_len += 1;
            } else {
                cur_len = 1;
            }
            total += cur_len;
            prev = v;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (count-alternating-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (prev #f) (cur-dp 0) (total 0))
    (if (null? lst)
        total
        (let* ((x (car lst))
               (new-dp (if (and (not (eq? prev #f)) (= x prev))
                           1
                           (+ cur-dp 1))))
          (loop (cdr lst) x new-dp (+ total new-dp))))))
```

## Erlang

```erlang
-module(solution).
-export([count_alternating_subarrays/1]).

-spec count_alternating_subarrays(Nums :: [integer()]) -> integer().
count_alternating_subarrays(Nums) ->
    count_alternating_subarrays(Nums, undefined, 0, 0).

count_alternating_subarrays([], _Prev, _CurrLen, Acc) ->
    Acc;
count_alternating_subarrays([H|T], Prev, CurrLen, Acc) ->
    NewLen = case Prev of
        undefined -> 1;
        _ when H =/= Prev -> CurrLen + 1;
        _ -> 1
    end,
    count_alternating_subarrays(T, H, NewLen, Acc + NewLen).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_alternating_subarrays(nums :: [integer]) :: integer
  def count_alternating_subarrays(nums) do
    case nums do
      [] -> 0
      [first | rest] ->
        {_prev_val, _prev_dp, total} =
          Enum.reduce(rest, {first, 1, 1}, fn cur, {prev_val, prev_dp, acc} ->
            dp = if cur != prev_val, do: prev_dp + 1, else: 1
            {cur, dp, acc + dp}
          end)

        total
    end
  end
end
```
