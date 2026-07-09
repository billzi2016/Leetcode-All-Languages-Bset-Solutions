# 3487. Maximum Unique Subarray Sum After Deletion

## Cpp

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums) {
        int maxNeg = INT_MIN;
        unordered_set<int> seen;
        long long sum = 0;
        bool hasNonNeg = false;
        for (int x : nums) {
            if (x >= 0) {
                hasNonNeg = true;
                if (seen.insert(x).second) {
                    sum += x;
                }
            } else {
                maxNeg = max(maxNeg, x);
            }
        }
        return hasNonNeg ? static_cast<int>(sum) : maxNeg;
    }
};
```

## Java

```java
class Solution {
    public int maxSum(int[] nums) {
        int max = Integer.MIN_VALUE;
        java.util.Set<Integer> uniquePositives = new java.util.HashSet<>();
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
            if (num >= 0) {
                uniquePositives.add(num);
            }
        }
        if (max < 0) {
            return max;
        }
        int sum = 0;
        for (int val : uniquePositives) {
            sum += val;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find maximum element to handle all-negative case
        max_elem = max(nums)
        if max_elem < 0:
            return max_elem

        seen = set()
        total = 0
        for v in nums:
            if v >= 0 and v not in seen:
                seen.add(v)
                total += v
        return total
```

## Python3

```python
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_elem = max(nums)
        if max_elem < 0:
            return max_elem
        seen = set()
        total = 0
        for x in nums:
            if x >= 0 and x not in seen:
                seen.add(x)
                total += x
        return total
```

## C

```c
int maxSum(int* nums, int numsSize) {
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    if (maxVal < 0) return maxVal;
    
    int seen[101] = {0};
    int sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (v >= 0 && !seen[v]) {
            seen[v] = 1;
            sum += v;
        }
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSum(int[] nums) {
        int max = nums[0];
        foreach (int v in nums) {
            if (v > max) max = v;
        }
        if (max < 0) return max;
        var seen = new HashSet<int>();
        int sum = 0;
        foreach (int v in nums) {
            if (v >= 0 && seen.Add(v)) {
                sum += v;
            }
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    let maxVal = -Infinity;
    for (const v of nums) {
        if (v > maxVal) maxVal = v;
    }
    if (maxVal < 0) return maxVal;
    
    const seen = new Set();
    let sum = 0;
    for (const v of nums) {
        if (v >= 0 && !seen.has(v)) {
            seen.add(v);
            sum += v;
        }
    }
    return sum;
};
```

## Typescript

```typescript
function maxSum(nums: number[]): number {
    let maxVal = nums[0];
    const posSet = new Set<number>();
    for (const x of nums) {
        if (x > maxVal) maxVal = x;
        if (x >= 0) posSet.add(x);
    }
    if (maxVal < 0) return maxVal;
    let sum = 0;
    for (const v of posSet) sum += v;
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSum($nums) {
        $max = $nums[0];
        foreach ($nums as $v) {
            if ($v > $max) {
                $max = $v;
            }
        }
        if ($max < 0) {
            return $max;
        }
        $seen = [];
        $sum = 0;
        foreach ($nums as $v) {
            if ($v >= 0 && !isset($seen[$v])) {
                $seen[$v] = true;
                $sum += $v;
            }
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var maxVal = nums[0]
        var seen = Set<Int>()
        var total = 0
        for v in nums {
            if v > maxVal { maxVal = v }
            if v >= 0 && !seen.contains(v) {
                seen.insert(v)
                total += v
            }
        }
        return maxVal < 0 ? maxVal : total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums: IntArray): Int {
        var maxVal = Int.MIN_VALUE
        val seen = HashSet<Int>()
        var sum = 0
        for (v in nums) {
            if (v > maxVal) maxVal = v
            if (v >= 0 && seen.add(v)) {
                sum += v
            }
        }
        return if (maxVal < 0) maxVal else sum
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<int> nums) {
    int maxVal = nums[0];
    bool hasNonNeg = false;
    final Set<int> seen = {};
    int sum = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
      if (v >= 0) {
        if (!seen.contains(v)) {
          seen.add(v);
          sum += v;
        }
        hasNonNeg = true;
      }
    }
    return hasNonNeg ? sum : maxVal;
  }
}
```

## Golang

```go
func maxSum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    maxVal := nums[0]
    sum := 0
    seen := make(map[int]bool)
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
        if v >= 0 && !seen[v] {
            sum += v
            seen[v] = true
        }
    }
    if sum == 0 && maxVal < 0 {
        return maxVal
    }
    return sum
}
```

## Ruby

```ruby
def max_sum(nums)
  max_val = nums.max
  return max_val if max_val < 0

  seen = {}
  sum = 0
  nums.each do |v|
    if v >= 0 && !seen[v]
      sum += v
      seen[v] = true
    end
  end
  sum
end
```

## Scala

```scala
object Solution {
    def maxSum(nums: Array[Int]): Int = {
        var hasNonNeg = false
        val uniqPos = scala.collection.mutable.HashSet[Int]()
        var maxVal = Int.MinValue
        for (v <- nums) {
            if (v >= 0) {
                hasNonNeg = true
                uniqPos += v
            }
            if (v > maxVal) maxVal = v
        }
        if (hasNonNeg) uniqPos.sum else maxVal
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let mut max_val = i32::MIN;
        let mut uniq = HashSet::new();
        for &v in &nums {
            if v > max_val {
                max_val = v;
            }
            if v >= 0 {
                uniq.insert(v);
            }
        }
        if max_val < 0 {
            max_val
        } else {
            uniq.iter().copied().sum()
        }
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (max-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val (apply max nums))
         (sum 0)
         (seen (make-hash)))
    (for ([x nums])
      (when (>= x 0)
        (unless (hash-has-key? seen x)
          (hash-set! seen x #t)
          (set! sum (+ sum x)))))
    (if (> (hash-count seen) 0)
        sum
        max-val)))
```

## Erlang

```erlang
-spec max_sum(Nums :: [integer()]) -> integer().
max_sum([H|T]) ->
    {InitMax, InitSet} = 
        case H >= 0 of
            true -> {H, maps:put(H, true, #{})};
            false -> {H, #{}}
        end,
    {FinalMax, FinalSet} = lists:foldl(
        fun(N, {CurMax, AccSet}) ->
            NewMax = if N > CurMax -> N; true -> CurMax end,
            case N >= 0 of
                true -> {NewMax, maps:put(N, true, AccSet)};
                false -> {NewMax, AccSet}
            end
        end,
        {InitMax, InitSet},
        T),
    if FinalMax < 0 ->
            FinalMax;
       true ->
            maps:fold(fun(K, _V, Sum) -> Sum + K end, 0, FinalSet)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer]) :: integer
  def max_sum(nums) do
    {set, max_val} =
      Enum.reduce(nums, {MapSet.new(), -101}, fn x, {s, m} ->
        s = if x >= 0, do: MapSet.put(s, x), else: s
        m = if x > m, do: x, else: m
        {s, m}
      end)

    if MapSet.size(set) == 0 do
      max_val
    else
      Enum.reduce(set, 0, &+/2)
    end
  end
end
```
