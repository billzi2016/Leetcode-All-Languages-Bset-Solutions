# 2202. Maximize the Topmost Element After K Moves

## Cpp

```cpp
class Solution {
public:
    int maximumTop(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 0) return nums[0];
        if (n == 1) {
            // With one element, we can only end up with it on top if k is even
            return (k % 2 == 0) ? nums[0] : -1;
        }
        long long ans = -1;
        // Case: pop exactly k times, no push
        if (k < n) {
            ans = max(ans, (long long)nums[k]);
        }
        // Case: perform at most k-1 pops then a push of any popped element
        int limit = min(n, k - 1);
        int mx = INT_MIN;
        for (int i = 0; i < limit; ++i) {
            mx = max(mx, nums[i]);
        }
        ans = max(ans, (long long)mx);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumTop(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) return nums[0];
        if (n == 1) {
            // With one element, we can only end up with a non‑empty pile if k is even
            return (k % 2 == 1) ? -1 : nums[0];
        }
        int max = Integer.MIN_VALUE;
        int limit = Math.min(k - 1, n);
        for (int i = 0; i < limit; i++) {
            if (nums[i] > max) max = nums[i];
        }
        if (k < n) {
            // We could also just pop k times and leave nums[k] on top
            if (nums[k] > max) max = nums[k];
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            # With a single element, we can only end with it if we perform an even number of moves.
            return -1 if k % 2 == 1 else nums[0]
        if k > n:
            return max(nums)
        if k == n:
            return -1
        # k < n
        best = float('-inf')
        if k - 1 > 0:
            best = max(nums[:k-1])
        # after popping exactly k elements, the new top is nums[k]
        best = max(best, nums[k])
        return best
```

## Python3

```python
from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            # With a single element, we can only end up with it on top after an even number of moves
            return -1 if k % 2 == 1 else nums[0]
        if k == 1:
            # Must pop once; the new top is the second element
            return nums[1]

        limit = min(k - 1, n)
        max_candidate = max(nums[:limit])

        if k < n:
            max_candidate = max(max_candidate, nums[k])

        return max_candidate
```

## C

```c
#include <limits.h>

int maximumTop(int* nums, int numsSize, int k) {
    if (k == 0) return nums[0];
    if (numsSize == 1) {
        return (k % 2 ? -1 : nums[0]);
    }
    if (k == 1) {
        return nums[1];
    }

    int limit = k - 1;
    if (limit > numsSize) limit = numsSize;

    int maxVal = INT_MIN;
    for (int i = 0; i < limit; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    int ans = maxVal;
    if (k < numsSize && nums[k] > ans) {
        ans = nums[k];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumTop(int[] nums, int k) {
        int n = nums.Length;
        if (k == 0) return nums[0];
        if (n == 1) {
            // With a single element, we can only end up with it after an even number of moves.
            return (k % 2 == 0) ? nums[0] : -1;
        }
        if (k == 1) {
            // Must pop the top once.
            return nums[1];
        }

        int maxVal = int.MinValue;
        int limit = Math.Min(k - 1, n);
        for (int i = 0; i < limit; i++) {
            if (nums[i] > maxVal) maxVal = nums[i];
        }

        int candidate = -1;
        if (k < n) {
            candidate = nums[k];
        }

        return Math.Max(maxVal, candidate);
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
var maximumTop = function(nums, k) {
    const n = nums.length;
    if (k === 0) return nums[0];
    if (n === 1) {
        // With a single element, odd moves leave the pile empty.
        return (k % 2 === 1) ? -1 : nums[0];
    }
    
    let maxVal = -Infinity;
    const limit = Math.min(k - 1, n);
    for (let i = 0; i < limit; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    if (k < n) {
        // We can pop exactly k elements and the next one becomes top.
        if (nums[k] > maxVal) maxVal = nums[k];
    }
    
    return maxVal === -Infinity ? -1 : maxVal;
};
```

## Typescript

```typescript
function maximumTop(nums: number[], k: number): number {
    const n = nums.length;
    if (k === 0) return nums[0];
    if (n === 1) {
        // With a single element, we can only end up with it if k is even.
        return k % 2 === 1 ? -1 : nums[0];
    }
    if (k > n) {
        let mx = -Infinity;
        for (let i = 0; i < n; ++i) {
            if (nums[i] > mx) mx = nums[i];
        }
        return mx;
    }
    if (k === n) {
        // After removing all elements we have no moves left to push.
        let mx = -Infinity;
        for (let i = 0; i < n - 1; ++i) {
            if (nums[i] > mx) mx = nums[i];
        }
        return mx;
    }
    // k < n
    let mx = -Infinity;
    // max among first k-1 elements (indices 0 .. k-2)
    for (let i = 0; i < k - 1; ++i) {
        if (nums[i] > mx) mx = nums[i];
    }
    // also consider the element at index k (after popping k times)
    if (nums[k] > mx) mx = nums[k];
    return mx;
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
    function maximumTop($nums, $k) {
        $n = count($nums);
        if ($k == 0) {
            return $nums[0];
        }
        if ($n == 1) {
            return ($k % 2 == 0) ? $nums[0] : -1;
        }
        if ($k == 1) {
            return $n > 1 ? $nums[1] : -1;
        }
        $maxVal = PHP_INT_MIN;
        $limit = min($n, $k - 1);
        for ($i = 0; $i < $limit; $i++) {
            if ($nums[$i] > $maxVal) {
                $maxVal = $nums[$i];
            }
        }
        if ($k < $n) {
            $candidate = $nums[$k];
            if ($candidate > $maxVal) {
                $maxVal = $candidate;
            }
        }
        return $maxVal;
    }
}
```

## Swift

```swift
class Solution {
    func maximumTop(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return nums[0] }
        if n == 1 {
            return (k % 2 == 1) ? -1 : nums[0]
        }
        var maxVal = Int.min
        let limit = min(k - 1, n)
        if limit > 0 {
            for i in 0..<limit {
                if nums[i] > maxVal {
                    maxVal = nums[i]
                }
            }
        }
        if k < n {
            if nums[k] > maxVal {
                maxVal = nums[k]
            }
        }
        return maxVal == Int.min ? -1 : maxVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTop(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (k == 0) return nums[0]
        if (n == 1) {
            return if (k % 2 == 1) -1 else nums[0]
        }
        var maxVal = Int.MIN_VALUE
        val limit = kotlin.math.min(k - 1, n)
        for (i in 0 until limit) {
            if (nums[i] > maxVal) maxVal = nums[i]
        }
        if (k < n) {
            if (nums[k] > maxVal) maxVal = nums[k]
        }
        return maxVal
    }
}
```

## Dart

```dart
class Solution {
  int maximumTop(List<int> nums, int k) {
    int n = nums.length;
    if (k == 0) return nums[0];
    if (n == 1) {
      return (k % 2 == 0) ? nums[0] : -1;
    }
    if (k == 1) {
      return nums[1];
    }

    int limit = k - 1;
    if (limit > n) limit = n;

    int maxVal = 0;
    for (int i = 0; i < limit; ++i) {
      if (nums[i] > maxVal) maxVal = nums[i];
    }

    if (k < n) {
      return maxVal > nums[k] ? maxVal : nums[k];
    } else {
      return maxVal;
    }
  }
}
```

## Golang

```go
func maximumTop(nums []int, k int) int {
    n := len(nums)
    if k == 0 {
        return nums[0]
    }
    if n == 1 {
        if k%2 == 1 {
            return -1
        }
        return nums[0]
    }

    limit := k - 1
    if limit > n {
        limit = n
    }
    maxVal := -1
    for i := 0; i < limit; i++ {
        if nums[i] > maxVal {
            maxVal = nums[i]
        }
    }

    if k < n && nums[k] > maxVal {
        maxVal = nums[k]
    }
    return maxVal
}
```

## Ruby

```ruby
def maximum_top(nums, k)
  n = nums.length
  return nums[0] if k == 0
  return -1 if n == 1 && (k & 1) == 1
  return nums[0] if n == 1

  max_val = -1

  limit = [k - 1, n].min
  if limit > 0
    upto = limit - 1
    upto = n - 1 if upto > n - 1
    (0..upto).each do |i|
      v = nums[i]
      max_val = v if v > max_val
    end
  end

  if k < n
    v = nums[k]
    max_val = v if v > max_val
  end

  max_val
end
```

## Scala

```scala
object Solution {
    def maximumTop(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        if (k == 0) return nums(0)
        if (n == 1) {
            if ((k & 1) == 1) -1 else nums(0)
        } else {
            var ans = Int.MinValue
            val limit = math.min(k - 1, n)
            var i = 0
            while (i < limit) {
                if (nums(i) > ans) ans = nums(i)
                i += 1
            }
            if (k < n && nums(k) > ans) ans = nums(k)
            ans
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_top(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if k == 0 {
            return nums[0];
        }
        if n == 1 {
            // With a single element, we can only end up with an empty pile after odd moves.
            return if k % 2 == 1 { -1 } else { nums[0] };
        }

        let mut ans = i32::MIN;
        // Consider the maximum among the first min(k-1, n) elements.
        let limit = std::cmp::min((k as usize).saturating_sub(1), n);
        for i in 0..limit {
            if nums[i] > ans {
                ans = nums[i];
            }
        }

        // If we can pop exactly k elements and still have a top element.
        if (k as usize) < n {
            let val = nums[k as usize];
            if val > ans {
                ans = val;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-top nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)])
    (cond
      [(zero? k) (first nums)]
      [(= n 1)
       (if (odd? k) -1 (first nums))]
      [(> k n)
       (apply max nums)]
      [(= k n) -1]
      [else
       (define prefix-max
         (let loop ((lst nums) (i 0) (mx -1))
           (if (or (= i (- k 1)) (null? lst))
               mx
               (loop (cdr lst) (+ i 1) (max mx (car lst))))))
       (define candidate2 (list-ref nums k))
       (max prefix-max candidate2)])))
```

## Erlang

```erlang
-module(solution).
-export([maximum_top/2]).

-spec maximum_top(Nums :: [integer()], K :: integer()) -> integer().
maximum_top(Nums, K) ->
    case K of
        0 ->
            hd(Nums);
        _ ->
            N = length(Nums),
            case N of
                1 ->
                    if K rem 2 =:= 1 -> -1; true -> hd(Nums) end;
                _ ->
                    Limit = min(K-1, N),
                    MaxPrefix = max_prefix(Nums, Limit, -1),
                    MaxVal =
                        if K < N ->
                                ElemK = lists:nth(K+1, Nums),
                                max(MaxPrefix, ElemK);
                           true -> MaxPrefix
                        end,
                    MaxVal
            end
    end.

max_prefix(_, 0, Max) -> Max;
max_prefix([H|T], Count, Max) ->
    NewMax = if H > Max -> H; true -> Max end,
    max_prefix(T, Count-1, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_top(nums :: [integer], k :: integer) :: integer
  def maximum_top(nums, k) do
    n = length(nums)

    cond do
      k == 0 ->
        hd(nums)

      n == 1 ->
        if rem(k, 2) == 1, do: -1, else: hd(nums)

      true ->
        limit = min(k - 1, n)

        max_pop =
          if limit > 0 do
            nums |> Enum.take(limit) |> Enum.max()
          else
            -1
          end

        if k < n do
          Enum.at(nums, k)
          |> max(max_pop)
        else
          max_pop
        end
    end
  end
end
```
