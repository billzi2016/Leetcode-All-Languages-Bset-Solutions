# 2444. Count Subarrays With Fixed Bounds

## Cpp

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        int lastInvalid = -1;   // index of most recent element outside [minK, maxK]
        int lastMin = -1;       // most recent index where value == minK
        int lastMax = -1;       // most recent index where value == maxK
        
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] < minK || nums[i] > maxK) {
                lastInvalid = i;
                // reset positions; they won't contribute across the invalid boundary
                lastMin = -1;
                lastMax = -1;
            }
            if (nums[i] == minK) lastMin = i;
            if (nums[i] == maxK) lastMax = i;
            
            int validStart = min(lastMin, lastMax);
            if (validStart > lastInvalid) {
                ans += (long long)(validStart - lastInvalid);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long ans = 0;
        int lastMin = -1, lastMax = -1, lastInvalid = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < minK || nums[i] > maxK) {
                lastInvalid = i;
            }
            if (nums[i] == minK) {
                lastMin = i;
            }
            if (nums[i] == maxK) {
                lastMax = i;
            }
            int validStart = Math.min(lastMin, lastMax);
            if (validStart > lastInvalid) {
                ans += validStart - lastInvalid;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        last_invalid = -1   # index of most recent element outside [minK, maxK]
        last_min = -1       # most recent index where value == minK
        last_max = -1       # most recent index where value == maxK
        ans = 0
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                last_invalid = i
                continue
            if v == minK:
                last_min = i
            if v == maxK:
                last_max = i
            valid_start = min(last_min, last_max)
            if valid_start > last_invalid:
                ans += valid_start - last_invalid
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_invalid = -1
        last_min = -1
        last_max = -1
        ans = 0
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                last_invalid = i
            if v == minK:
                last_min = i
            if v == maxK:
                last_max = i
            valid_start = min(last_min, last_max)
            if valid_start > last_invalid:
                ans += valid_start - last_invalid
        return ans
```

## C

```c
long long countSubarrays(int* nums, int numsSize, int minK, int maxK) {
    long long ans = 0;
    int lastInvalid = -1;
    int lastMin = -1;
    int lastMax = -1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < minK || nums[i] > maxK) {
            lastInvalid = i;
        }
        if (nums[i] == minK) lastMin = i;
        if (nums[i] == maxK) lastMax = i;
        int validStart = lastMin < lastMax ? lastMin : lastMax;
        if (validStart > lastInvalid) {
            ans += (long long)(validStart - lastInvalid);
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, int minK, int maxK) {
        long ans = 0;
        int lastInvalid = -1;
        int lastMin = -1;
        int lastMax = -1;

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] < minK || nums[i] > maxK) {
                lastInvalid = i;
            }
            if (nums[i] == minK) lastMin = i;
            if (nums[i] == maxK) lastMax = i;

            int validStart = Math.Min(lastMin, lastMax);
            if (validStart > lastInvalid) {
                ans += validStart - lastInvalid;
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
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    let lastMin = -1;
    let lastMax = -1;
    let lastInvalid = -1;
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];
        if (v < minK || v > maxK) {
            lastInvalid = i;
        }
        if (v === minK) lastMin = i;
        if (v === maxK) lastMax = i;
        const validStart = Math.min(lastMin, lastMax);
        if (validStart > lastInvalid) {
            ans += validStart - lastInvalid;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let lastInvalid = -1;
    let lastMin = -1;
    let lastMax = -1;
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (x < minK || x > maxK) {
            lastInvalid = i;
        }
        if (x === minK) lastMin = i;
        if (x === maxK) lastMax = i;
        const validStart = Math.min(lastMin, lastMax);
        if (validStart > lastInvalid) {
            ans += validStart - lastInvalid;
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
     * @param Integer $minK
     * @param Integer $maxK
     * @return Integer
     */
    function countSubarrays($nums, $minK, $maxK) {
        $lastInvalid = -1;
        $lastMin = -1;
        $lastMax = -1;
        $result = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $val = $nums[$i];
            if ($val < $minK || $val > $maxK) {
                $lastInvalid = $i;
            }
            if ($val == $minK) {
                $lastMin = $i;
            }
            if ($val == $maxK) {
                $lastMax = $i;
            }
            $validStart = min($lastMin, $lastMax);
            if ($validStart > $lastInvalid) {
                $result += $validStart - $lastInvalid;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ minK: Int, _ maxK: Int) -> Int {
        var lastInvalid = -1
        var lastMin = -1
        var lastMax = -1
        var result: Int64 = 0
        
        for i in 0..<nums.count {
            let v = nums[i]
            if v < minK || v > maxK {
                lastInvalid = i
            }
            if v == minK {
                lastMin = i
            }
            if v == maxK {
                lastMax = i
            }
            let validStart = min(lastMin, lastMax)
            if validStart > lastInvalid {
                result += Int64(validStart - lastInvalid)
            }
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, minK: Int, maxK: Int): Long {
        var left = -1          // last index with value out of [minK, maxK]
        var lastMin = -1       // last index where nums[i] == minK
        var lastMax = -1       // last index where nums[i] == maxK
        var result = 0L

        for (i in nums.indices) {
            val v = nums[i]
            if (v < minK || v > maxK) {
                left = i
            }
            if (v == minK) lastMin = i
            if (v == maxK) lastMax = i

            val validStart = kotlin.math.min(lastMin, lastMax)
            if (validStart > left) {
                result += (validStart - left).toLong()
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int minK, int maxK) {
    int left = -1;      // last index of element out of [minK, maxK]
    int lastMin = -1;   // last index where value == minK
    int lastMax = -1;   // last index where value == maxK
    int ans = 0;

    for (int i = 0; i < nums.length; i++) {
      int v = nums[i];
      if (v < minK || v > maxK) {
        left = i;
      }
      if (v == minK) lastMin = i;
      if (v == maxK) lastMax = i;

      int validStart = lastMin < lastMax ? lastMin : lastMax;
      if (validStart > left) {
        ans += validStart - left;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countSubarrays(nums []int, minK int, maxK int) int64 {
    leftBound := -1
    lastMin := -1
    lastMax := -1
    var ans int64 = 0

    for i, v := range nums {
        if v < minK || v > maxK {
            leftBound = i
        }
        if v == minK {
            lastMin = i
        }
        if v == maxK {
            lastMax = i
        }

        // earliest position where both minK and maxK have appeared up to i
        minPos := lastMin
        if lastMax < minPos {
            minPos = lastMax
        }

        if minPos > leftBound {
            ans += int64(minPos - leftBound)
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_subarrays(nums, min_k, max_k)
  last_invalid = -1
  last_min = -1
  last_max = -1
  ans = 0

  nums.each_with_index do |x, i|
    if x < min_k || x > max_k
      last_invalid = i
    end
    last_min = i if x == min_k
    last_max = i if x == max_k

    valid_start = [last_min, last_max].min
    ans += [0, valid_start - last_invalid].max
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], minK: Int, maxK: Int): Long = {
        var lastMin = -1
        var lastMax = -1
        var lastInvalid = -1
        var ans: Long = 0L

        for (i <- nums.indices) {
            val v = nums(i)
            if (v < minK || v > maxK) {
                lastInvalid = i
            }
            if (v == minK) lastMin = i
            if (v == maxK) lastMax = i

            val validStart = Math.min(lastMin, lastMax)
            if (validStart > lastInvalid) {
                ans += (validStart - lastInvalid).toLong
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut ans: i64 = 0;
        let mut last_invalid: isize = -1;
        let mut last_min: isize = -1;
        let mut last_max: isize = -1;

        for (i, &v) in nums.iter().enumerate() {
            if v < min_k || v > max_k {
                last_invalid = i as isize;
            }
            if v == min_k {
                last_min = i as isize;
            }
            if v == max_k {
                last_max = i as isize;
            }

            let valid_start = std::cmp::min(last_min, last_max);
            if valid_start > last_invalid {
                ans += (valid_start - last_invalid) as i64;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-subarrays nums minK maxK)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let loop ((lst nums) 
             (i -1)                ; current index
             (last-invalid -1)    ; last position of element outside [minK, maxK]
             (last-min -1)        ; last position where value == minK
             (last-max -1)        ; last position where value == maxK
             (ans 0))              ; accumulated answer
    (if (null? lst)
        ans
        (let* ((x (car lst))
               (i+1 (+ i 1))
               (new-last-invalid (if (or (< x minK) (> x maxK)) i+1 last-invalid))
               (new-last-min (if (= x minK) i+1 last-min))
               (new-last-max (if (= x maxK) i+1 last-max))
               (valid-start (min new-last-min new-last-max))
               (add (if (> valid-start new-last-invalid)
                        (- valid-start new-last-invalid)
                        0)))
          (loop (cdr lst) 
                i+1 
                new-last-invalid 
                new-last-min 
                new-last-max 
                (+ ans add)))))))
```

## Erlang

```erlang
-spec count_subarrays(Nums :: [integer()], MinK :: integer(), MaxK :: integer()) -> integer().
count_subarrays(Nums, MinK, MaxK) ->
    loop(Nums, 0, -1, -1, -1, 0, MinK, MaxK).

loop([], _Idx, _LastInv, _LastMin, _LastMax, Acc, _MinK, _MaxK) ->
    Acc;
loop([Num | Rest], Idx, LastInv, LastMin, LastMax, Acc, MinK, MaxK) ->
    NewLastInv = if Num < MinK orelse Num > MaxK -> Idx; true -> LastInv end,
    NewLastMin = if Num == MinK -> Idx; true -> LastMin end,
    NewLastMax = if Num == MaxK -> Idx; true -> LastMax end,
    MinPos = erlang:min(NewLastMin, NewLastMax),
    Add = case MinPos - NewLastInv of
        X when X > 0 -> X;
        _ -> 0
    end,
    loop(Rest, Idx + 1, NewLastInv, NewLastMin, NewLastMax, Acc + Add, MinK, MaxK).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], min_k :: integer, max_k :: integer) :: integer
  def count_subarrays(nums, min_k, max_k) do
    {_invalid, _min_pos, _max_pos, total} =
      Enum.with_index(nums)
      |> Enum.reduce({-1, -1, -1, 0}, fn {num, idx},
          {last_invalid, last_min, last_max, acc} ->
        if num < min_k or num > max_k do
          {idx, last_min, last_max, acc}
        else
          new_last_min = if num == min_k, do: idx, else: last_min
          new_last_max = if num == max_k, do: idx, else: last_max

          valid_start = min(new_last_min, new_last_max)

          add =
            if valid_start > last_invalid do
              valid_start - last_invalid
            else
              0
            end

          {last_invalid, new_last_min, new_last_max, acc + add}
        end
      end)

    total
  end
end
```
