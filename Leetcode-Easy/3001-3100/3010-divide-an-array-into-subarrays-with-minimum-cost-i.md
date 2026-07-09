# 3010. Divide an Array Into Subarrays With Minimum Cost I

## Cpp

```cpp
class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int n = nums.size();
        int min1 = INT_MAX, min2 = INT_MAX;
        for (int i = 1; i < n; ++i) {
            int v = nums[i];
            if (v < min1) {
                min2 = min1;
                min1 = v;
            } else if (v < min2) {
                min2 = v;
            }
        }
        return nums[0] + min1 + min2;
    }
};
```

## Java

```java
class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length;
        // Minimum sum of first elements of the second and third subarrays
        int minPrev = nums[1];
        int bestPairSum = Integer.MAX_VALUE;
        for (int q = 2; q < n; ++q) {
            bestPairSum = Math.min(bestPairSum, minPrev + nums[q]);
            minPrev = Math.min(minPrev, nums[q]);
        }
        return nums[0] + bestPairSum;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_first = float('inf')
        best_pair = float('inf')
        for i in range(1, n):
            if min_first != float('inf'):
                best_pair = min(best_pair, min_first + nums[i])
            min_first = min(min_first, nums[i])
        return nums[0] + best_pair
```

## Python3

```python
from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        # suffix minima: min value from each position to the end
        suffix_min = [0] * n
        cur_min = float('inf')
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, nums[i])
            suffix_min[i] = cur_min

        ans = float('inf')
        # choose first cut at i (i >= 1) and second cut after i
        for i in range(1, n - 1):  # i up to n-2 inclusive
            total = nums[0] + nums[i] + suffix_min[i + 1]
            if total < ans:
                ans = total
        return ans
```

## C

```c
#include <limits.h>

int minimumCost(int* nums, int numsSize) {
    int minSum = INT_MAX;
    for (int i = 1; i < numsSize - 1; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            int cur = nums[i] + nums[j];
            if (cur < minSum) minSum = cur;
        }
    }
    return nums[0] + minSum;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumCost(int[] nums) {
        int n = nums.Length;
        int minLeft = nums[1];
        int bestPair = int.MaxValue;
        for (int j = 2; j < n; j++) {
            bestPair = Math.Min(bestPair, minLeft + nums[j]);
            if (nums[j] < minLeft) minLeft = nums[j];
        }
        return nums[0] + bestPair;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    const n = nums.length;
    // suffixMin[i] = min value in nums[i..n-1]
    const suffixMin = new Array(n);
    suffixMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }
    let best = Infinity;
    // choose start of second subarray at i (1 <= i <= n-2)
    for (let i = 1; i <= n - 2; ++i) {
        const candidate = nums[i] + suffixMin[i + 1]; // start of third subarray is after i
        if (candidate < best) best = candidate;
    }
    return nums[0] + best;
};
```

## Typescript

```typescript
function minimumCost(nums: number[]): number {
    const n = nums.length;
    const suffixMin = new Array<number>(n);
    suffixMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }
    let best = Infinity;
    for (let i = 1; i <= n - 2; ++i) {
        const candidate = nums[i] + suffixMin[i + 1];
        if (candidate < best) best = candidate;
    }
    return nums[0] + best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumCost($nums) {
        $n = count($nums);
        // suffix minima of nums
        $suffixMin = array_fill(0, $n, 0);
        $suffixMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suffixMin[$i] = min($nums[$i], $suffixMin[$i + 1]);
        }

        $best = PHP_INT_MAX;
        // choose the start of second subarray (i) and third subarray (j)
        for ($i = 1; $i <= $n - 2; $i++) {
            $candidate = $nums[$i] + $suffixMin[$i + 1];
            if ($candidate < $best) {
                $best = $candidate;
            }
        }

        return $nums[0] + $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        let n = nums.count
        var suffixMin = Array(repeating: Int.max, count: n)
        suffixMin[n - 1] = nums[n - 1]
        if n > 1 {
            for idx in stride(from: n - 2, through: 0, by: -1) {
                suffixMin[idx] = min(nums[idx], suffixMin[idx + 1])
            }
        }
        var best = Int.max
        for i in 1..<(n - 1) {
            let sum = nums[i] + suffixMin[i + 1]
            if sum < best { best = sum }
        }
        return nums[0] + best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(nums: IntArray): Int {
        var min1 = Int.MAX_VALUE
        var min2 = Int.MAX_VALUE
        for (i in 1 until nums.size) {
            val v = nums[i]
            if (v < min1) {
                min2 = min1
                min1 = v
            } else if (v < min2) {
                min2 = v
            }
        }
        return nums[0] + min1 + min2
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> nums) {
    int n = nums.length;
    int best = 1 << 30;
    for (int i = 0; i <= n - 3; ++i) {
      for (int j = i + 1; j <= n - 2; ++j) {
        int cost = nums[0] + nums[i + 1] + nums[j + 1];
        if (cost < best) best = cost;
      }
    }
    return best;
  }
}
```

## Golang

```go
func minimumCost(nums []int) int {
    first := nums[0]
    const INF = 51 // greater than max possible value (50)
    min1, min2 := INF, INF
    for i := 1; i < len(nums); i++ {
        v := nums[i]
        if v < min1 {
            min2 = min1
            min1 = v
        } else if v < min2 {
            min2 = v
        }
    }
    return first + min1 + min2
}
```

## Ruby

```ruby
def minimum_cost(nums)
  n = nums.length
  suffix_min = Array.new(n)
  suffix_min[n - 1] = nums[n - 1]
  (n - 2).downto(0) do |i|
    suffix_min[i] = nums[i] < suffix_min[i + 1] ? nums[i] : suffix_min[i + 1]
  end
  best = Float::INFINITY
  (1..n - 2).each do |i|
    sum = nums[i] + suffix_min[i + 1]
    best = sum if sum < best
  end
  nums[0] + best
end
```

## Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int]): Int = {
        val n = nums.length
        var minFirst = Int.MaxValue
        var answer = Int.MaxValue
        for (j <- 2 until n) {
            // consider i = j-1 as a possible new first cut
            if (nums(j - 1) < minFirst) minFirst = nums(j - 1)
            val total = nums(0) + minFirst + nums(j)
            if (total < answer) answer = total
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // suffix minima of nums
        let mut suffix_min = vec![0; n];
        suffix_min[n - 1] = nums[n - 1];
        for idx in (0..n - 1).rev() {
            suffix_min[idx] = std::cmp::min(nums[idx], suffix_min[idx + 1]);
        }

        let mut best = i32::MAX;
        // choose start of second subarray at i, third starts after i
        for i in 1..=n - 2 {
            let candidate = nums[i] + suffix_min[i + 1];
            if candidate < best {
                best = candidate;
            }
        }

        nums[0] + best
    }
}
```

## Racket

```racket
(define/contract (minimum-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (< n 3)
        0
        (begin
          ;; suffix minima
          (define suff (make-vector n))
          (vector-set! suff (- n 1) (vector-ref v (- n 1)))
          (for ([i (in-range (- n 2) -1 -1)])
            (vector-set! suff i (min (vector-ref v i)
                                     (vector-ref suff (+ i 1)))))
          ;; find minimal pair nums[i] + min_{j>i} nums[j]
          (define best
            (for/fold ([best (expt 2 30)]) ([i (in-range 1 (- n 1))])
              (let* ([cand (+ (vector-ref v i)
                              (vector-ref suff (+ i 1)))])
                (min best cand))))
          (+ (vector-ref v 0) best))))))
```

## Erlang

```erlang
-spec minimum_cost(Nums :: [integer()]) -> integer().
minimum_cost([First|Rest]) ->
    {Min1, Min2} = find_two_min(Rest, 1000, 1000),
    First + Min1 + Min2.

find_two_min([], Min1, Min2) ->
    {Min1, Min2};
find_two_min([X|Xs], Min1, Min2) when X =< Min1 ->
    find_two_min(Xs, X, Min1);
find_two_min([X|Xs], Min1, Min2) when X =< Min2 ->
    find_two_min(Xs, Min1, X);
find_two_min([_|Xs], Min1, Min2) ->
    find_two_min(Xs, Min1, Min2).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost(nums) do
    n = length(nums)

    suffix_min =
      nums
      |> Enum.reverse()
      |> Enum.reduce([], fn x, acc ->
        min_val =
          case acc do
            [] -> x
            [prev | _] -> if x < prev, do: x, else: prev
          end

        [min_val | acc]
      end)

    first = hd(nums)

    1..(n - 2)
    |> Enum.reduce(:infinity, fn i, best ->
      total = first + Enum.at(nums, i) + Enum.at(suffix_min, i + 1)
      if total < best, do: total, else: best
    end)
  end
end
```
