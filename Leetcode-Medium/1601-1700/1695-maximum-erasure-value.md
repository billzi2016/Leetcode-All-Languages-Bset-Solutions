# 1695. Maximum Erasure Value

## Cpp

```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> cnt;
        long long curSum = 0, maxSum = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            while (cnt[nums[right]] > 0) {
                cnt[nums[left]]--;
                curSum -= nums[left];
                ++left;
            }
            cnt[nums[right]]++;
            curSum += nums[right];
            if (curSum > maxSum) maxSum = curSum;
        }
        return (int)maxSum;
    }
};
```

## Java

```java
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int maxVal = 10000;
        int[] freq = new int[maxVal + 1];
        long sum = 0;
        int left = 0;
        int best = 0;
        for (int right = 0; right < nums.length; right++) {
            while (freq[nums[right]] > 0) {
                freq[nums[left]]--;
                sum -= nums[left];
                left++;
            }
            freq[nums[right]] = 1;
            sum += nums[right];
            if (sum > best) {
                best = (int) sum;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        cur_sum = 0
        max_sum = 0
        seen = set()
        for right, val in enumerate(nums):
            while val in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
            seen.add(val)
            cur_sum += val
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
```

## Python3

```python
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        max_sum = 0
        seen = set()
        for right, val in enumerate(nums):
            while val in seen:
                removed = nums[left]
                seen.remove(removed)
                cur_sum -= removed
                left += 1
            seen.add(val)
            cur_sum += val
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
```

## C

```c
#include <stddef.h>

int maximumUniqueSubarray(int* nums, int numsSize) {
    const int MAX_VAL = 10000;
    char seen[10001] = {0}; // boolean array for values up to 10000
    int left = 0;
    long long curSum = 0;
    long long best = 0;

    for (int right = 0; right < numsSize; ++right) {
        int val = nums[right];
        while (seen[val]) {
            // remove nums[left] from window
            seen[nums[left]] = 0;
            curSum -= nums[left];
            ++left;
        }
        // add current value
        seen[val] = 1;
        curSum += val;
        if (curSum > best) best = curSum;
    }

    return (int)best;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumUniqueSubarray(int[] nums)
    {
        var freq = new Dictionary<int, int>();
        long curSum = 0;
        long maxSum = 0;
        int left = 0;

        for (int right = 0; right < nums.Length; right++)
        {
            int val = nums[right];
            while (freq.ContainsKey(val))
            {
                int leftVal = nums[left];
                curSum -= leftVal;
                if (freq[leftVal] == 1)
                    freq.Remove(leftVal);
                else
                    freq[leftVal]--;
                left++;
            }

            freq[val] = 1;
            curSum += val;
            if (curSum > maxSum) maxSum = curSum;
        }

        return (int)maxSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
    const seen = new Set();
    let left = 0;
    let curSum = 0;
    let maxSum = 0;
    
    for (let right = 0; right < nums.length; right++) {
        while (seen.has(nums[right])) {
            seen.delete(nums[left]);
            curSum -= nums[left];
            left++;
        }
        seen.add(nums[right]);
        curSum += nums[right];
        if (curSum > maxSum) maxSum = curSum;
    }
    
    return maxSum;
};
```

## Typescript

```typescript
function maximumUniqueSubarray(nums: number[]): number {
    const seen = new Set<number>();
    let left = 0;
    let currentSum = 0;
    let maxSum = 0;

    for (let right = 0; right < nums.length; right++) {
        while (seen.has(nums[right])) {
            seen.delete(nums[left]);
            currentSum -= nums[left];
            left++;
        }
        seen.add(nums[right]);
        currentSum += nums[right];
        if (currentSum > maxSum) {
            maxSum = currentSum;
        }
    }

    return maxSum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumUniqueSubarray($nums) {
        $left = 0;
        $currentSum = 0;
        $maxSum = 0;
        $seen = [];

        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $val = $nums[$right];
            while (isset($seen[$val])) {
                $leftVal = $nums[$left];
                unset($seen[$leftVal]);
                $currentSum -= $leftVal;
                $left++;
            }
            $seen[$val] = true;
            $currentSum += $val;
            if ($currentSum > $maxSum) {
                $maxSum = $currentSum;
            }
        }

        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func maximumUniqueSubarray(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var left = 0
        var currentSum = 0
        var maxSum = 0
        
        for right in 0..<nums.count {
            let val = nums[right]
            while seen.contains(val) {
                let leftVal = nums[left]
                seen.remove(leftVal)
                currentSum -= leftVal
                left += 1
            }
            seen.insert(val)
            currentSum += val
            if currentSum > maxSum {
                maxSum = currentSum
            }
        }
        return maxSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumUniqueSubarray(nums: IntArray): Int {
        val seen = HashSet<Int>()
        var left = 0
        var currentSum = 0L
        var maxSum = 0L
        for (right in nums.indices) {
            while (!seen.add(nums[right])) {
                seen.remove(nums[left])
                currentSum -= nums[left].toLong()
                left++
            }
            currentSum += nums[right].toLong()
            if (currentSum > maxSum) maxSum = currentSum
        }
        return maxSum.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumUniqueSubarray(List<int> nums) {
    int left = 0;
    int curSum = 0;
    int best = 0;
    final Set<int> seen = <int>{};

    for (int right = 0; right < nums.length; right++) {
      while (seen.contains(nums[right])) {
        seen.remove(nums[left]);
        curSum -= nums[left];
        left++;
      }
      seen.add(nums[right]);
      curSum += nums[right];
      if (curSum > best) best = curSum;
    }

    return best;
  }
}
```

## Golang

```go
func maximumUniqueSubarray(nums []int) int {
    seen := make(map[int]bool)
    left, curSum, maxSum := 0, 0, 0
    for right, v := range nums {
        for seen[v] {
            seen[nums[left]] = false
            curSum -= nums[left]
            left++
        }
        seen[v] = true
        curSum += v
        if curSum > maxSum {
            maxSum = curSum
        }
    }
    return maxSum
}
```

## Ruby

```ruby
def maximum_unique_subarray(nums)
  last_index = {}
  left = 0
  cur_sum = 0
  max_sum = 0

  nums.each_with_index do |val, right|
    while last_index.key?(val) && last_index[val] >= left
      cur_sum -= nums[left]
      left += 1
    end
    cur_sum += val
    last_index[val] = right
    max_sum = cur_sum if cur_sum > max_sum
  end

  max_sum
end
```

## Scala

```scala
object Solution {
  def maximumUniqueSubarray(nums: Array[Int]): Int = {
    import scala.collection.mutable
    val seen = mutable.HashSet[Int]()
    var left = 0
    var curSum: Long = 0L
    var maxSum: Long = 0L

    for (right <- nums.indices) {
      val v = nums(right)
      while (seen.contains(v)) {
        seen.remove(nums(left))
        curSum -= nums(left)
        left += 1
      }
      seen.add(v)
      curSum += v
      if (curSum > maxSum) maxSum = curSum
    }

    maxSum.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        let max_val = 10000usize;
        let mut freq = vec![0i32; max_val + 1];
        let mut left = 0usize;
        let mut cur_sum: i64 = 0;
        let mut max_sum: i64 = 0;

        for right in 0..nums.len() {
            let val = nums[right] as usize;
            while freq[val] > 0 {
                let left_val = nums[left] as usize;
                freq[left_val] -= 1;
                cur_sum -= nums[left] as i64;
                left += 1;
            }
            freq[val] += 1;
            cur_sum += nums[right] as i64;
            if cur_sum > max_sum {
                max_sum = cur_sum;
            }
        }

        max_sum as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (maximum-unique-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ((right 0) (left 0) (sum 0) (max-sum 0) (set (make-hash)))
      (if (= right n)
          max-sum
          (let ([val (vector-ref v right)])
            (define-values (new-left new-sum)
              (let loop2 ((l left) (s sum))
                (if (hash-has-key? set val)
                    (let* ([lv (vector-ref v l)]
                           (_ (hash-remove! set lv)))
                      (loop2 (+ l 1) (- s lv)))
                    (values l s))))
            (hash-set! set val #t)
            (define new-total (+ new-sum val))
            (define new-max (if (> new-total max-sum) new-total max-sum))
            (loop (+ right 1) new-left new-total new-max set))))))
```

## Erlang

```erlang
-spec maximum_unique_subarray(Nums :: [integer()]) -> integer().
maximum_unique_subarray(Nums) ->
    Arr = array:from_list(Nums),
    loop(1, 1, 0, 0, #{}, Arr).

loop(I, Left, CurrSum, MaxSum, Map, Arr) when I > array:size(Arr) ->
    MaxSum;
loop(I, Left, CurrSum, MaxSum, Map, Arr) ->
    Num = array:get(I, Arr),
    case maps:is_key(Num, Map) of
        true ->
            PrevIdx = maps:get(Num, Map),
            {NewLeft, NewSum, NewMap} = shrink_until(Left, PrevIdx, CurrSum, Map, Arr);
        false ->
            {NewLeft, NewSum, NewMap} = {Left, CurrSum, Map}
    end,
    UpdatedCurrSum = NewSum + Num,
    UpdatedMap = maps:put(Num, I, NewMap),
    UpdatedMax = if UpdatedCurrSum > MaxSum -> UpdatedCurrSum; true -> MaxSum end,
    loop(I + 1, NewLeft, UpdatedCurrSum, UpdatedMax, UpdatedMap, Arr).

shrink_until(L, TargetIdx, Sum, Map, Arr) when L =< TargetIdx ->
    Val = array:get(L, Arr),
    NewMap = maps:remove(Val, Map),
    shrink_until(L + 1, TargetIdx, Sum - Val, NewMap, Arr);
shrink_until(L, _TargetIdx, Sum, Map, _Arr) ->
    {L, Sum, Map}.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_unique_subarray(nums :: [integer]) :: integer
  def maximum_unique_subarray(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    {_, _, _, max_sum} =
      Enum.reduce(0..(n - 1), {%{}, 0, 0, 0}, fn right,
                                                {counts, left, cur_sum, max_sum} ->
        val = elem(arr, right)
        counts = Map.update(counts, val, 1, &(&1 + 1))
        cur_sum = cur_sum + val

        {counts, left, cur_sum} =
          if Map.get(counts, val) > 1 do
            shrink(arr, counts, left, cur_sum, val)
          else
            {counts, left, cur_sum}
          end

        max_sum = if cur_sum > max_sum, do: cur_sum, else: max_sum
        {counts, left, cur_sum, max_sum}
      end)

    max_sum
  end

  defp shrink(arr, counts, left, cur_sum, dup_val) do
    if Map.get(counts, dup_val) <= 1 do
      {counts, left, cur_sum}
    else
      left_val = elem(arr, left)

      counts =
        case Map.get(counts, left_val) do
          1 -> Map.delete(counts, left_val)
          n when n > 1 -> Map.put(counts, left_val, n - 1)
        end

      cur_sum = cur_sum - left_val
      shrink(arr, counts, left + 1, cur_sum, dup_val)
    end
  end
end
```
