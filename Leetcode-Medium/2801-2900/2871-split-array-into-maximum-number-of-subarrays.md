# 2871. Split Array Into Maximum Number of Subarrays

## Cpp

```cpp
class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
        int total_and = nums[0];
        for (int i = 1; i < (int)nums.size(); ++i) total_and &= nums[i];
        if (total_and != 0) return 1;
        int ans = 0;
        int cur = ~0; // all bits set
        for (int x : nums) {
            cur &= x;
            if (cur == 0) {
                ++ans;
                cur = ~0;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSubarrays(int[] nums) {
        int totalAnd = nums[0];
        for (int i = 1; i < nums.length; i++) {
            totalAnd &= nums[i];
        }
        if (totalAnd != 0) return 1;
        int count = 0;
        int cur = -1; // all bits set
        for (int num : nums) {
            cur &= num;
            if (cur == 0) {
                count++;
                cur = -1;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall = nums[0]
        for x in nums[1:]:
            overall &= x
        if overall != 0:
            return 1

        ans = 0
        cur = -1  # all bits set
        for x in nums:
            cur &= x
            if cur == 0:
                ans += 1
                cur = -1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total = nums[0]
        for v in nums[1:]:
            total &= v
        if total != 0:
            return 1
        ans = 0
        mask = (1 << 20) - 1  # sufficient for nums[i] <= 10^6
        cur = mask
        for x in nums:
            cur &= x
            if cur == 0:
                ans += 1
                cur = mask
        return ans
```

## C

```c
int maxSubarrays(int* nums, int numsSize) {
    int totalAnd = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        totalAnd &= nums[i];
    }
    if (totalAnd != 0) return 1;
    int ans = 0;
    int cur = ~0; // all bits set
    for (int i = 0; i < numsSize; ++i) {
        cur &= nums[i];
        if (cur == 0) {
            ++ans;
            cur = ~0;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSubarrays(int[] nums) {
        int totalAnd = nums[0];
        foreach (int v in nums) {
            totalAnd &= v;
        }
        if (totalAnd != 0) return 1;

        int ans = 0;
        int cur = -1; // all bits set
        foreach (int v in nums) {
            cur &= v;
            if (cur == 0) {
                ans++;
                cur = -1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarrays = function(nums) {
    // Compute overall AND of the array
    let totalAnd = -1; // all bits set for 32-bit signed int
    for (let v of nums) {
        totalAnd &= v;
    }
    // If minimum possible score is non-zero, only one subarray works
    if (totalAnd !== 0) return 1;

    // Otherwise, split greedily whenever current prefix AND becomes zero
    let ans = 0;
    let cur = -1; // reset to all bits set
    for (let v of nums) {
        cur &= v;
        if (cur === 0) {
            ans++;
            cur = -1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxSubarrays(nums: number[]): number {
    let overall = nums[0];
    for (let i = 1; i < nums.length; ++i) {
        overall &= nums[i];
    }
    if (overall !== 0) return 1;

    let cur = -1;
    let ans = 0;
    for (const v of nums) {
        cur &= v;
        if (cur === 0) {
            ++ans;
            cur = -1;
        }
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
    function maxSubarrays($nums) {
        $globalAnd = $nums[0];
        foreach ($nums as $v) {
            $globalAnd &= $v;
        }
        if ($globalAnd != 0) {
            return 1;
        }
        $cnt = 0;
        $cur = -1; // all bits set
        foreach ($nums as $v) {
            $cur &= $v;
            if ($cur == 0) {
                $cnt++;
                $cur = -1;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarrays(_ nums: [Int]) -> Int {
        var totalAnd = nums[0]
        for i in 1..<nums.count {
            totalAnd &= nums[i]
        }
        if totalAnd != 0 { return 1 }
        
        var ans = 0
        var cur = ~0   // all bits set (i.e., -1)
        for num in nums {
            cur &= num
            if cur == 0 {
                ans += 1
                cur = ~0
            }
        }
        return ans == 0 ? 1 : ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubarrays(nums: IntArray): Int {
        var totalAnd = nums[0]
        for (i in 1 until nums.size) {
            totalAnd = totalAnd and nums[i]
        }
        if (totalAnd != 0) return 1
        var cur = -1
        var count = 0
        for (v in nums) {
            cur = cur and v
            if (cur == 0) {
                count++
                cur = -1
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maxSubarrays(List<int> nums) {
    int overall = nums[0];
    for (int i = 1; i < nums.length; i++) {
      overall &= nums[i];
    }
    if (overall != 0) return 1;

    int count = 0;
    int cur = -1; // all bits set
    for (int v in nums) {
      cur &= v;
      if (cur == 0) {
        count++;
        cur = -1;
      }
    }
    return count;
  }
}
```

## Golang

```go
func maxSubarrays(nums []int) int {
    // Compute overall AND of all elements
    totalAnd := ^0
    for _, v := range nums {
        totalAnd &= v
    }
    if totalAnd != 0 {
        return 1
    }

    count := 0
    cur := ^0
    for _, v := range nums {
        cur &= v
        if cur == 0 {
            count++
            cur = ^0
        }
    }
    // At least one subarray will be formed when totalAnd == 0
    return count
}
```

## Ruby

```ruby
def max_subarrays(nums)
  overall = nums.reduce { |a, b| a & b }
  return 1 if overall != 0

  ans = 0
  cur = -1
  nums.each do |v|
    cur &= v
    if cur == 0
      ans += 1
      cur = -1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxSubarrays(nums: Array[Int]): Int = {
        val overallAnd = nums.foldLeft(-1) { (acc, v) => acc & v }
        if (overallAnd != 0) return 1
        var ans = 0
        var cur = -1
        for (v <- nums) {
            cur &= v
            if (cur == 0) {
                ans += 1
                cur = -1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_subarrays(nums: Vec<i32>) -> i32 {
        // Compute the AND of all elements
        let total_and = nums.iter().fold(-1_i32, |acc, &x| acc & x);
        if total_and != 0 {
            return 1;
        }
        let mut cnt = 0i32;
        let mut cur = -1_i32; // all bits set
        for &x in nums.iter() {
            cur &= x;
            if cur == 0 {
                cnt += 1;
                cur = -1_i32;
            }
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (max-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((total-and (foldl bitwise-and -1 nums)))
    (if (not (= total-and 0))
        1
        (let loop ((lst nums) (cur -1) (cnt 0))
          (cond
            [(null? lst) cnt]
            [else
             (define new-cur (bitwise-and cur (car lst)))
             (if (= new-cur 0)
                 (loop (cdr lst) -1 (+ cnt 1))
                 (loop (cdr lst) new-cur cnt))])))))
```

## Erlang

```erlang
-module(solution).
-export([max_subarrays/1]).

-spec max_subarrays(Nums :: [integer()]) -> integer().
max_subarrays(Nums) ->
    case Nums of
        [] -> 0;
        [H|T] ->
            OverallAnd = lists:foldl(fun(X, Acc) -> Acc band X end, H, T),
            if OverallAnd =/= 0 ->
                    1;
               true ->
                    split_count(Nums)
            end
    end.

split_count(List) -> split_count(List, 0, none).

split_count([], Count, _) -> Count;
split_count([H|Rest], Count, none) ->
    if H == 0 ->
            split_count(Rest, Count + 1, none);
       true ->
            split_count(Rest, Count, H)
    end;
split_count([H|Rest], Count, CurAnd) ->
    NewCur = CurAnd band H,
    if NewCur == 0 ->
            split_count(Rest, Count + 1, none);
       true ->
            split_count(Rest, Count, NewCur)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_subarrays(nums :: [integer]) :: integer
  def max_subarrays(nums) do
    total_and = Enum.reduce(nums, -1, fn x, acc -> band(acc, x) end)

    if total_and != 0 do
      1
    else
      {count, _} =
        Enum.reduce(nums, {0, -1}, fn x, {cnt, cur} ->
          new_cur = band(cur, x)

          if new_cur == 0 do
            {cnt + 1, -1}
          else
            {cnt, new_cur}
          end
        end)

      count
    end
  end
end
```
