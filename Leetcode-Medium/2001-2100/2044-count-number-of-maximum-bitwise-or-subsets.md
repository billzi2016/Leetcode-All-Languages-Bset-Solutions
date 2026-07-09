# 2044. Count Number of Maximum Bitwise-OR Subsets

## Cpp

```cpp
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int maxOr = 0;
        for (int x : nums) maxOr |= x;
        int total = 1 << n;
        int cnt = 0;
        for (int mask = 1; mask < total; ++mask) {
            int cur = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) cur |= nums[i];
            }
            if (cur == maxOr) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countMaxOrSubsets(int[] nums) {
        int n = nums.length;
        int maxOr = 0;
        for (int num : nums) {
            maxOr |= num;
        }
        int totalMasks = 1 << n;
        int count = 0;
        for (int mask = 1; mask < totalMasks; ++mask) {
            int cur = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    cur |= nums[i];
                }
            }
            if (cur == maxOr) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num

        n = len(nums)
        total_masks = 1 << n
        ans = 0
        for mask in range(1, total_masks):
            cur = 0
            m = mask
            i = 0
            while m:
                if m & 1:
                    cur |= nums[i]
                i += 1
                m >>= 1
            if cur == max_or:
                ans += 1
        return ans
```

## Python3

```python
class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        for v in nums:
            max_or |= v
        n = len(nums)
        cnt = 0
        for mask in range(1, 1 << n):
            cur = 0
            m = mask
            i = 0
            while m:
                if m & 1:
                    cur |= nums[i]
                i += 1
                m >>= 1
            if cur == max_or:
                cnt += 1
        return cnt
```

## C

```c
#include <stddef.h>

int countMaxOrSubsets(int* nums, int numsSize) {
    int maxOr = 0;
    for (int i = 0; i < numsSize; ++i) {
        maxOr |= nums[i];
    }
    
    unsigned int total = 1U << numsSize;
    int ans = 0;
    
    for (unsigned int mask = 1; mask < total; ++mask) {
        int cur = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (mask & (1U << i)) {
                cur |= nums[i];
            }
        }
        if (cur == maxOr) {
            ++ans;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int CountMaxOrSubsets(int[] nums) {
        int target = 0;
        foreach (int v in nums) {
            target |= v;
        }
        int n = nums.Length;
        int totalMasks = 1 << n;
        int count = 0;
        for (int mask = 1; mask < totalMasks; ++mask) {
            int curOr = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i & 1) == 1) {
                    curOr |= nums[i];
                }
            }
            if (curOr == target) {
                ++count;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function(nums) {
    const n = nums.length;
    let maxOr = 0;
    for (const v of nums) {
        maxOr |= v;
    }
    const totalMasks = 1 << n; // 2^n
    let count = 0;
    for (let mask = 1; mask < totalMasks; ++mask) { // skip empty subset
        let cur = 0;
        for (let i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                cur |= nums[i];
            }
        }
        if (cur === maxOr) {
            ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countMaxOrSubsets(nums: number[]): number {
    const n = nums.length;
    let maxOr = 0;
    for (const v of nums) {
        maxOr |= v;
    }
    let count = 0;
    const totalMasks = 1 << n;
    for (let mask = 1; mask < totalMasks; ++mask) {
        let cur = 0;
        for (let i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                cur |= nums[i];
            }
        }
        if (cur === maxOr) {
            ++count;
        }
    }
    return count;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countMaxOrSubsets($nums) {
        $maxOr = 0;
        foreach ($nums as $num) {
            $maxOr |= $num;
        }
        $n = count($nums);
        $total = 1 << $n; // total subsets including empty
        $count = 0;
        for ($mask = 1; $mask < $total; $mask++) { // skip empty subset
            $cur = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($mask & (1 << $i)) {
                    $cur |= $nums[$i];
                }
            }
            if ($cur === $maxOr) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countMaxOrSubsets(_ nums: [Int]) -> Int {
        // Compute the maximum possible OR value (OR of all elements)
        var maxOr = 0
        for num in nums {
            maxOr |= num
        }
        
        // dp[v] = number of subsets whose OR equals v
        var dp = [Int](repeating: 0, count: maxOr + 1)
        dp[0] = 1   // empty subset
        
        var curMax = 0
        for num in nums {
            // Update dp in reverse to avoid using newly updated values in the same iteration
            for i in stride(from: curMax, through: 0, by: -1) {
                if dp[i] != 0 {
                    let newVal = i | num
                    dp[newVal] += dp[i]
                }
            }
            curMax |= num
        }
        
        // Exclude the empty subset; however, maxOr cannot be 0 given constraints,
        // so dp[maxOr] already counts only non‑empty subsets achieving maxOr.
        return dp[maxOr]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countMaxOrSubsets(nums: IntArray): Int {
        var maxOr = 0
        for (v in nums) {
            maxOr = maxOr or v
        }
        val n = nums.size
        var result = 0
        val total = 1 shl n
        for (mask in 1 until total) { // non‑empty subsets
            var cur = 0
            var m = mask
            var idx = 0
            while (m != 0) {
                if ((m and 1) == 1) {
                    cur = cur or nums[idx]
                }
                idx++
                m = m shr 1
            }
            if (cur == maxOr) {
                result++
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int countMaxOrSubsets(List<int> nums) {
    int n = nums.length;
    int maxOr = 0;
    for (int v in nums) {
      maxOr |= v;
    }
    int total = 1 << n;
    int count = 0;
    for (int mask = 1; mask < total; ++mask) {
      int cur = 0;
      for (int i = 0; i < n; ++i) {
        if ((mask & (1 << i)) != 0) {
          cur |= nums[i];
        }
      }
      if (cur == maxOr) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countMaxOrSubsets(nums []int) int {
    n := len(nums)
    maxOr := 0
    for _, v := range nums {
        maxOr |= v
    }
    total := 1 << n
    cnt := 0
    for mask := 1; mask < total; mask++ {
        cur := 0
        for i, v := range nums {
            if (mask>>i)&1 == 1 {
                cur |= v
            }
        }
        if cur == maxOr {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_max_or_subsets(nums)
  n = nums.length
  max_or = 0
  nums.each { |v| max_or |= v }
  total = 1 << n
  cnt = 0
  (1...total).each do |mask|
    cur = 0
    i = 0
    m = mask
    while m > 0
      if (m & 1) == 1
        cur |= nums[i]
      end
      i += 1
      m >>= 1
    end
    cnt += 1 if cur == max_or
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def countMaxOrSubsets(nums: Array[Int]): Int = {
        val n = nums.length
        var maxOr = 0
        for (v <- nums) maxOr |= v

        var count = 0
        val total = 1 << n
        for (mask <- 1 until total) {
            var cur = 0
            var i = 0
            var m = mask
            while (i < n) {
                if ((m & 1) == 1) cur |= nums(i)
                i += 1
                m >>= 1
            }
            if (cur == maxOr) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_max_or_subsets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_or = 0i32;
        for &v in &nums {
            max_or |= v;
        }
        let total = 1usize << n;
        let mut cnt = 0i32;
        for mask in 1..total {
            let mut cur = 0i32;
            let mut m = mask;
            let mut idx = 0usize;
            while m > 0 {
                if (m & 1) == 1 {
                    cur |= nums[idx];
                }
                idx += 1;
                m >>= 1;
            }
            if cur == max_or {
                cnt += 1;
            }
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (count-max-or-subsets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (max-or (let loop ((i 0) (acc 0))
                   (if (= i n)
                       acc
                       (loop (+ i 1) (bitwise-ior acc (vector-ref vec i))))))
         (dfs (letrec ((f (lambda (idx cur)
                            (if (= idx n)
                                (if (= cur max-or) 1 0)
                                (+ (f (+ idx 1) cur)
                                   (f (+ idx 1) (bitwise-ior cur (vector-ref vec idx))))))))
                f)))
    (dfs 0 0)))
```

## Erlang

```erlang
-spec count_max_or_subsets(Nums :: [integer()]) -> integer().
count_max_or_subsets(Nums) ->
    MaxOr = lists:foldl(fun(N, Acc) -> N bor Acc end, 0, Nums),
    Len = length(Nums),
    Total = 1 bsl Len,
    loop(1, Total, Nums, MaxOr, 0).

loop(Mask, Limit, _Nums, _MaxOr, Acc) when Mask >= Limit ->
    Acc;
loop(Mask, Limit, Nums, MaxOr, Acc) ->
    OrVal = or_mask(Nums, 0, Mask, 0),
    NewAcc = case OrVal == MaxOr of
        true -> Acc + 1;
        false -> Acc
    end,
    loop(Mask + 1, Limit, Nums, MaxOr, NewAcc).

or_mask([], _Index, _Mask, Acc) ->
    Acc;
or_mask([H|T], Index, Mask, Acc) ->
    case (Mask bsr Index) band 1 of
        1 -> or_mask(T, Index + 1, Mask, Acc bor H);
        _ -> or_mask(T, Index + 1, Mask, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_max_or_subsets(nums :: [integer]) :: integer
  def count_max_or_subsets(nums) do
    target = Enum.reduce(nums, 0, fn x, acc -> acc ||| x end)
    n = length(nums)
    max_mask = 1 <<< n

    Enum.reduce(1..(max_mask - 1), 0, fn mask, cnt ->
      cur = or_of_mask(mask, nums, 0)

      if cur == target do
        cnt + 1
      else
        cnt
      end
    end)
  end

  defp or_of_mask(0, _list, acc), do: acc

  defp or_of_mask(mask, [h | t], acc) do
    new_acc = if (mask &&& 1) == 1, do: acc ||| h, else: acc
    or_of_mask(mask >>> 1, t, new_acc)
  end
end
```
