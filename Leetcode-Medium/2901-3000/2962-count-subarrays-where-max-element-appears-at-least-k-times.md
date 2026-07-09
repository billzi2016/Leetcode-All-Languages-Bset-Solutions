# 2962. Count Subarrays Where Max Element Appears at Least K Times

## Cpp

```cpp
class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k) {
        int n = nums.size();
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> pos;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == mx) pos.push_back(i);
        }
        long long ans = 0;
        int m = pos.size();
        if (m < k) return 0;
        for (int i = 0; i + k - 1 < m; ++i) {
            long long left = pos[i] - (i == 0 ? -1 : pos[i - 1]);
            long long right = n - pos[i + k - 1];
            ans += left * right;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > max) max = num;
        }
        java.util.ArrayList<Integer> positions = new java.util.ArrayList<>();
        long ans = 0L;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == max) {
                positions.add(i);
            }
            int cnt = positions.size();
            if (cnt >= k) {
                ans += (long) positions.get(cnt - k) + 1L;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        idxs = [i for i, v in enumerate(nums) if v == max_val]
        m = len(idxs)
        if k > m:
            return 0
        n = len(nums)
        ans = 0
        for t in range(k - 1, m):
            left_idx = idxs[t - k + 1]
            prev_idx = idxs[t - k] if t - k >= 0 else -1
            start_choices = left_idx - prev_idx
            end_choices = n - idxs[t]
            ans += start_choices * end_choices
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        positions = []
        ans = 0
        for i, v in enumerate(nums):
            if v == max_val:
                positions.append(i)
                cnt = len(positions)
                if cnt >= k:
                    idx = positions[cnt - k]
                    ans += idx + 1
        return ans
```

## C

```c
#include <stdlib.h>

long long countSubarrays(int* nums, int numsSize, int k) {
    if (numsSize == 0 || k <= 0) return 0;
    
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    int *pos = (int *)malloc(sizeof(int) * numsSize);
    int cnt = 0;
    long long ans = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == maxVal) {
            pos[cnt++] = i;
            if (cnt >= k) {
                ans += (long long)(pos[cnt - k] + 1);
            }
        }
    }
    
    free(pos);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        int maxVal = int.MinValue;
        foreach (int v in nums) {
            if (v > maxVal) maxVal = v;
        }

        var positions = new System.Collections.Generic.List<int>();
        long ans = 0;

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == maxVal) {
                positions.Add(i);
            }
            int cnt = positions.Count;
            if (cnt >= k) {
                ans += positions[cnt - k] + 1L;
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
var countSubarrays = function(nums, k) {
    // Find the global maximum value
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    const idx = []; // positions of maxVal
    let ans = 0;
    
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === maxVal) idx.push(i);
        if (idx.length >= k) {
            // earliest start index that still includes at least k max elements
            ans += idx[idx.length - k] + 1;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[], k: number): number {
    // Find the global maximum value
    let maxVal = nums[0];
    for (const v of nums) {
        if (v > maxVal) maxVal = v;
    }

    const positions: number[] = [];
    let ans = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === maxVal) {
            positions.push(i);
        }
        if (positions.length >= k) {
            // Index of the occurrence that is k-th from the end
            const idx = positions[positions.length - k];
            ans += idx + 1;
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
    function countSubarrays($nums, $k) {
        $max = max($nums);
        $indices = [];
        $ans = 0;
        foreach ($nums as $i => $val) {
            if ($val === $max) {
                $indices[] = $i;
            }
            $cnt = count($indices);
            if ($cnt >= $k) {
                $idx = $indices[$cnt - $k];
                $ans += $idx + 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        guard let maxVal = nums.max() else { return 0 }
        var positions = [Int]()
        var result: Int64 = 0
        for (i, v) in nums.enumerated() {
            if v == maxVal {
                positions.append(i)
            }
            if positions.count >= k {
                let idx = positions[positions.count - k]
                result += Int64(idx + 1)
            }
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Long {
        val maxVal = nums.maxOrNull() ?: 0
        val positions = mutableListOf<Int>()
        var ans = 0L
        for (i in nums.indices) {
            if (nums[i] == maxVal) {
                positions.add(i)
            }
            if (positions.size >= k) {
                val idx = positions[positions.size - k]
                ans += (idx + 1).toLong()
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int k) {
    int maxVal = nums[0];
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    List<int> positions = [];
    int ans = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == maxVal) {
        positions.add(i);
      }
      if (positions.length >= k) {
        ans += positions[positions.length - k] + 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countSubarrays(nums []int, k int) int64 {
    if len(nums) == 0 {
        return 0
    }
    maxVal := nums[0]
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    positions := make([]int, 0)
    var ans int64

    for i, v := range nums {
        if v == maxVal {
            positions = append(positions, i)
        }
        if len(positions) >= k {
            idx := positions[len(positions)-k]
            ans += int64(idx + 1)
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_subarrays(nums, k)
  max_val = nums.max
  positions = []
  ans = 0
  nums.each_with_index do |v, i|
    positions << i if v == max_val
    if positions.size >= k
      ans += positions[positions.size - k] + 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        var maxVal = Int.MinValue
        for (v <- nums) if (v > maxVal) maxVal = v

        val total: Long = n.toLong * (n + 1L) / 2L
        if (k <= 0) return total

        var left = 0
        var cntM = 0
        var atMost: Long = 0L
        for (right <- 0 until n) {
            if (nums(right) == maxVal) cntM += 1
            while (cntM > k - 1) {
                if (nums(left) == maxVal) cntM -= 1
                left += 1
            }
            atMost += (right - left + 1).toLong
        }

        total - atMost
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // Find the maximum element in the array.
        let mut max_val = nums[0];
        for &v in nums.iter().skip(1) {
            if v > max_val {
                max_val = v;
            }
        }

        let k_usize = k as usize;
        let mut positions: Vec<usize> = Vec::new();
        let mut ans: i64 = 0;

        for (i, &v) in nums.iter().enumerate() {
            if v == max_val {
                positions.push(i);
            }
            let cnt = positions.len();
            if cnt >= k_usize {
                // The earliest start index that still keeps at least k maximums
                // is positions[cnt - k] (0‑based). All starts from 0..=that index are valid.
                ans += (positions[cnt - k_usize] + 1) as i64;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((max-el (apply max nums))
         (n (length nums))
         (posvec (make-vector n))
         (m 0)
         (ans 0))
    (for ([x nums] [i (in-naturals)])
      (when (= x max-el)
        (vector-set! posvec m i)
        (set! m (+ m 1))
        (when (>= m k)
          (let ((pos (vector-ref posvec (- m k))))
            (set! ans (+ ans (+ pos 1)))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_subarrays/2]).

-spec count_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_subarrays(Nums, K) ->
    Max = lists:max(Nums),
    Indices = lists:seq(0, length(Nums) - 1),
    {Ans, _Arr, _Count} =
        lists:foldl(
            fun({Val, Idx}, {Acc, Arr, Count}) ->
                case Val == Max of
                    true ->
                        NewArr = array:set(Count, Idx, Arr),
                        NewCount = Count + 1,
                        Add = if NewCount >= K ->
                                    EarlierPos = array:get(NewCount - K, NewArr),
                                    EarlierPos + 1;
                                true -> 0
                              end,
                        {Acc + Add, NewArr, NewCount};
                    false ->
                        {Acc, Arr, Count}
                end
            end,
            {0, array:new(), 0},
            lists:zip(Nums, Indices)
        ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], k :: integer) :: integer
  def count_subarrays(nums, k) do
    max_val = Enum.max(nums)

    {ans, _cnt, _queue} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0, :queue.new()}, fn {val, idx}, {ans_acc, cnt, queue} ->
        {new_cnt, new_queue} =
          if val == max_val do
            cnt1 = cnt + 1
            q1 = :queue.in(idx, queue)

            if cnt1 > k do
              {{:value, _old}, q2} = :queue.out(q1)
              {cnt1, q2}
            else
              {cnt1, q1}
            end
          else
            {cnt, queue}
          end

        ans_new =
          if new_cnt >= k do
            {:value, front_idx} = :queue.peek(new_queue)
            ans_acc + front_idx + 1
          else
            ans_acc
          end

        {ans_new, new_cnt, new_queue}
      end)

    ans
  end
end
```
