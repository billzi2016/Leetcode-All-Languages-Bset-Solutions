# 2461. Maximum Sum of Distinct Subarrays With Length K

## Cpp

```cpp
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> lastPos;
        long long curSum = 0;
        long long ans = 0;
        int left = 0;
        int n = nums.size();
        for (int right = 0; right < n; ++right) {
            int val = nums[right];
            // shrink window while duplicate exists or size exceeds k
            while ((lastPos.count(val) && lastPos[val] >= left) || (right - left + 1 > k)) {
                curSum -= nums[left];
                ++left;
            }
            curSum += val;
            lastPos[val] = right;
            if (right - left + 1 == k) {
                ans = max(ans, curSum);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        java.util.Map<Integer, Integer> lastIdx = new java.util.HashMap<>();
        long curSum = 0;
        long ans = 0;
        int left = 0;

        for (int right = 0; right < n; ++right) {
            int val = nums[right];
            Integer prev = lastIdx.get(val);

            while ((prev != null && prev >= left) || (right - left + 1 > k)) {
                curSum -= nums[left];
                left++;
            }

            curSum += val;
            lastIdx.put(val, right);

            if (right - left + 1 == k) {
                ans = Math.max(ans, curSum);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        cur_sum = 0
        left = 0
        ans = 0

        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            cur_sum += val

            # Ensure window has distinct elements and size <= k
            while freq[val] > 1 or (right - left + 1) > k:
                rem = nums[left]
                freq[rem] -= 1
                if freq[rem] == 0:
                    del freq[rem]
                cur_sum -= rem
                left += 1

            # When window size is exactly k, update answer
            if (right - left + 1) == k:
                ans = max(ans, cur_sum)

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        cur_sum = 0
        ans = 0
        last_idx = {}
        for right, val in enumerate(nums):
            # Remove duplicates inside the window
            if val in last_idx and last_idx[val] >= left:
                while left <= last_idx[val]:
                    cur_sum -= nums[left]
                    left += 1
            # Ensure window size does not exceed k
            while right - left + 1 > k:
                cur_sum -= nums[left]
                left += 1
            # Add current element
            cur_sum += val
            last_idx[val] = right
            if right - left + 1 == k:
                ans = max(ans, cur_sum)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

long long maximumSubarraySum(int* nums, int numsSize, int k) {
    const int MAX_VAL = 100000;
    int *last = (int *)malloc((MAX_VAL + 1) * sizeof(int));
    if (!last) return 0;
    memset(last, -1, (MAX_VAL + 1) * sizeof(int));

    long long ans = 0, curSum = 0;
    int left = 0;

    for (int right = 0; right < numsSize; ++right) {
        int val = nums[right];
        int lastIdx = last[val];

        while (left <= lastIdx || right - left + 1 > k) {
            curSum -= nums[left];
            left++;
        }

        last[val] = right;
        curSum += val;

        if (right - left + 1 == k && curSum > ans) {
            ans = curSum;
        }
    }

    free(last);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        var lastIdx = new Dictionary<int, int>();
        long currentSum = 0;
        long ans = 0;
        int left = 0;
        for (int right = 0; right < nums.Length; ++right) {
            int val = nums[right];
            if (lastIdx.TryGetValue(val, out int prev) && prev >= left) {
                while (left <= prev) {
                    currentSum -= nums[left];
                    left++;
                }
            }
            while (right - left + 1 > k) {
                currentSum -= nums[left];
                left++;
            }
            lastIdx[val] = right;
            currentSum += val;
            if (right - left + 1 == k) {
                if (currentSum > ans) ans = currentSum;
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
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    const n = nums.length;
    let left = 0;
    let sum = 0;
    let maxSum = 0;
    const lastIdx = new Map();
    
    for (let right = 0; right < n; ++right) {
        const val = nums[right];
        // Shrink window if duplicate inside or size exceeds k
        while ((lastIdx.has(val) && lastIdx.get(val) >= left) || (right - left + 1 > k)) {
            sum -= nums[left];
            left++;
        }
        sum += val;
        lastIdx.set(val, right);
        if (right - left + 1 === k) {
            if (sum > maxSum) maxSum = sum;
        }
    }
    
    return maxSum;
};
```

## Typescript

```typescript
function maximumSubarraySum(nums: number[], k: number): number {
    const lastIdx = new Map<number, number>();
    let left = 0;
    let curSum = 0;
    let ans = 0;

    for (let right = 0; right < nums.length; right++) {
        const val = nums[right];

        // Remove duplicates
        while (lastIdx.has(val) && (lastIdx.get(val)! >= left)) {
            curSum -= nums[left];
            left++;
        }

        // Add current element
        curSum += val;
        lastIdx.set(val, right);

        // Ensure window size does not exceed k
        while (right - left + 1 > k) {
            curSum -= nums[left];
            left++;
        }

        if (right - left + 1 === k) {
            ans = Math.max(ans, curSum);
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
     * @param Integer $k
     * @return Integer
     */
    function maximumSubarraySum($nums, $k) {
        $n = count($nums);
        $freq = [];
        $left = 0;
        $sum = 0;
        $max = 0;

        for ($right = 0; $right < $n; $right++) {
            $val = $nums[$right];
            if (!isset($freq[$val])) {
                $freq[$val] = 0;
            }
            $freq[$val]++;
            $sum += $val;

            while ($freq[$val] > 1 || $right - $left + 1 > $k) {
                $remove = $nums[$left];
                $freq[$remove]--;
                if ($freq[$remove] == 0) {
                    unset($freq[$remove]);
                }
                $sum -= $remove;
                $left++;
            }

            if ($right - $left + 1 == $k && $sum > $max) {
                $max = $sum;
            }
        }

        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        var lastIndex = [Int: Int]()
        var left = 0
        var currentSum = 0
        var answer = 0
        
        for right in 0..<nums.count {
            let value = nums[right]
            
            if let prev = lastIndex[value], left <= prev {
                while left <= prev {
                    currentSum -= nums[left]
                    left += 1
                }
            }
            
            while right - left + 1 > k {
                currentSum -= nums[left]
                left += 1
            }
            
            lastIndex[value] = right
            currentSum += value
            
            if right - left + 1 == k {
                answer = max(answer, currentSum)
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSubarraySum(nums: IntArray, k: Int): Long {
        val lastIdx = HashMap<Int, Int>()
        var left = 0
        var sum = 0L
        var answer = 0L

        for (right in nums.indices) {
            val cur = nums[right]
            val prev = lastIdx[cur]

            // If duplicate inside current window, shrink left past it
            if (prev != null && prev >= left) {
                while (left <= prev) {
                    sum -= nums[left].toLong()
                    left++
                }
            }

            // Ensure window size does not exceed k
            while (right - left + 1 > k) {
                sum -= nums[left].toLong()
                left++
            }

            lastIdx[cur] = right
            sum += cur.toLong()

            if (right - left + 1 == k) {
                answer = kotlin.math.max(answer, sum)
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumSubarraySum(List<int> nums, int k) {
    final Map<int, int> freq = {};
    int left = 0;
    int curSum = 0;
    int ans = 0;

    for (int right = 0; right < nums.length; ++right) {
      final int val = nums[right];
      curSum += val;
      freq[val] = (freq[val] ?? 0) + 1;

      while ((freq[val] ?? 0) > 1 || (right - left + 1) > k) {
        final int leftVal = nums[left];
        curSum -= leftVal;
        final int cnt = freq[leftVal]!;
        if (cnt == 1) {
          freq.remove(leftVal);
        } else {
          freq[leftVal] = cnt - 1;
        }
        left++;
      }

      if ((right - left + 1) == k) {
        if (curSum > ans) ans = curSum;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maximumSubarraySum(nums []int, k int) int64 {
    lastIdx := make(map[int]int)
    var curSum int64
    var ans int64
    left := 0

    for right, val := range nums {
        if idx, ok := lastIdx[val]; ok && idx >= left {
            // remove elements up to the previous occurrence
            for left <= idx {
                curSum -= int64(nums[left])
                left++
            }
        }

        // keep window size within k
        for right-left+1 > k {
            curSum -= int64(nums[left])
            left++
        }

        lastIdx[val] = right
        curSum += int64(val)

        if right-left+1 == k && curSum > ans {
            ans = curSum
        }
    }

    return ans
}
```

## Ruby

```ruby
def maximum_subarray_sum(nums, k)
  freq = Hash.new(0)
  sum = 0
  left = 0
  max_sum = 0

  nums.each_with_index do |num, right|
    freq[num] += 1
    sum += num

    while freq[num] > 1 || (right - left + 1) > k
      removed = nums[left]
      freq[removed] -= 1
      sum -= removed
      left += 1
    end

    if (right - left + 1) == k
      max_sum = [max_sum, sum].max
    end
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
        var begin = 0
        var sum: Long = 0L
        var ans: Long = 0L
        val lastIdx = scala.collection.mutable.Map[Int, Int]()
        for (end <- nums.indices) {
            val cur = nums(end)
            val last = lastIdx.getOrElse(cur, -1)
            while (begin <= last || end - begin + 1 > k) {
                sum -= nums(begin).toLong
                begin += 1
            }
            sum += cur.toLong
            lastIdx(cur) = end
            if (end - begin + 1 == k && sum > ans) {
                ans = sum
            }
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if k as usize > n {
            return 0;
        }
        let mut last_idx: HashMap<i32, usize> = HashMap::new();
        let mut left: usize = 0;
        let mut cur_sum: i64 = 0;
        let mut ans: i64 = 0;

        for right in 0..n {
            let val = nums[right];
            // Remove elements from the left until there is no duplicate of val
            while let Some(&prev) = last_idx.get(&val) {
                if prev < left {
                    break;
                }
                cur_sum -= nums[left] as i64;
                left += 1;
            }

            // Ensure window size does not exceed k
            while right + 1 - left > k as usize {
                cur_sum -= nums[left] as i64;
                left += 1;
            }

            // Add current element
            last_idx.insert(val, right);
            cur_sum += val as i64;

            if right + 1 - left == k as usize {
                ans = ans.max(cur_sum);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let ([ht (make-hash)]
          [begin 0]
          [cur-sum 0]
          [ans 0])
      (for ([end (in-range n)])
        (define curr (vector-ref v end))
        (define last-occurrence (hash-ref ht curr -1))
        ;; shrink window while duplicate exists or size exceeds k
        (let loop ()
          (when (or (>= last-occurrence begin)
                    (> (- end begin) (sub1 k)))
            (set! cur-sum (- cur-sum (vector-ref v begin)))
            (set! begin (+ begin 1))
            (loop)))
        (hash-set! ht curr end)
        (set! cur-sum (+ cur-sum curr))
        ;; when window size equals k, possibly update answer
        (when (= (- end begin) (sub1 k))
          (when (> cur-sum ans) (set! ans cur-sum))))
      ans)))
```

## Erlang

```erlang
-spec maximum_subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
maximum_subarray_sum(Nums, K) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    loop(0, 0, 0, 0, #{}, Tuple, K, N).

%% Loop over the array
loop(Index, Beg, Sum, MaxAns, Map, Tuple, K, N) when Index == N ->
    MaxAns;
loop(Index, Beg, Sum, MaxAns, Map, Tuple, K, N) ->
    Val = element(Index + 1, Tuple),
    LastIdx = maps:get(Val, Map, -1),
    {Beg2, Sum2} = shrink(Beg, Sum, Index, LastIdx, Tuple, K),
    NewSum = Sum2 + Val,
    NewMap = maps:put(Val, Index, Map),
    WindowSize = Index - Beg2 + 1,
    NewMax = if
        WindowSize == K -> erlang:max(MaxAns, NewSum);
        true -> MaxAns
    end,
    loop(Index + 1, Beg2, NewSum, NewMax, NewMap, Tuple, K, N).

%% Shrink the window while duplicate exists or size exceeds K
shrink(Beg, Sum, Index, LastIdx, Tuple, K) ->
    case (LastIdx >= Beg) orelse (Index - Beg + 1 > K) of
        true ->
            FrontVal = element(Beg + 1, Tuple),
            shrink(Beg + 1, Sum - FrontVal, Index, LastIdx, Tuple, K);
        false ->
            {Beg, Sum}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_subarray_sum(nums :: [integer], k :: integer) :: integer
  def maximum_subarray_sum(nums, k) do
    {max_sum, _freq, _queue, _cur_sum} =
      Enum.reduce(nums, {0, %{}, :queue.new(), 0}, fn num,
                                                    {max_sum, freq, queue, cur_sum} ->
        # add current number to window
        queue = :queue.in(num, queue)
        cur_sum = cur_sum + num
        freq = Map.update(freq, num, 1, &(&1 + 1))

        # shrink while duplicate exists or size exceeds k
        {freq, queue, cur_sum} = shrink(freq, queue, cur_sum, k, num)

        # update answer if window size equals k
        max_sum =
          if :queue.len(queue) == k and cur_sum > max_sum do
            cur_sum
          else
            max_sum
          end

        {max_sum, freq, queue, cur_sum}
      end)

    max_sum
  end

  defp shrink(freq, queue, cur_sum, k, added_num) do
    if (Map.get(freq, added_num, 0) > 1) or (:queue.len(queue) > k) do
      {{:value, out_val}, queue} = :queue.out(queue)
      cur_sum = cur_sum - out_val

      freq =
        case Map.get(freq, out_val) do
          1 -> Map.delete(freq, out_val)
          c when c > 1 -> Map.put(freq, out_val, c - 1)
        end

      shrink(freq, queue, cur_sum, k, added_num)
    else
      {freq, queue, cur_sum}
    end
  end
end
```
