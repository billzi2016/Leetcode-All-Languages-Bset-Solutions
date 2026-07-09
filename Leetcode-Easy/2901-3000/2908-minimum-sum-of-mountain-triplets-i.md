# 2908. Minimum Sum of Mountain Triplets I

## Cpp

```cpp
class Solution {
public:
    int minimumSum(vector<int>& nums) {
        const int INF = 1e9;
        int n = nums.size();
        int best = INF;
        for (int j = 1; j < n - 1; ++j) {
            int leftMin = INF, rightMin = INF;
            for (int i = 0; i < j; ++i) {
                if (nums[i] < nums[j]) leftMin = min(leftMin, nums[i]);
            }
            for (int k = j + 1; k < n; ++k) {
                if (nums[k] < nums[j]) rightMin = min(rightMin, nums[k]);
            }
            if (leftMin != INF && rightMin != INF) {
                best = min(best, leftMin + nums[j] + rightMin);
            }
        }
        return best == INF ? -1 : best;
    }
};
```

## Java

```java
class Solution {
    public int minimumSum(int[] nums) {
        int n = nums.length;
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] >= nums[j]) continue;
                for (int k = j + 1; k < n; k++) {
                    if (nums[k] < nums[j]) {
                        int sum = nums[i] + nums[j] + nums[k];
                        if (sum < best) best = sum;
                    }
                }
            }
        }
        return best == Integer.MAX_VALUE ? -1 : best;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        best = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[k] < nums[j]:
                        total = nums[i] + nums[j] + nums[k]
                        if total < best:
                            best = total
        return -1 if best == float('inf') else best
```

## Python3

```python
class Solution:
    def minimumSum(self, nums):
        n = len(nums)
        best = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[k] < nums[j]:
                        total = nums[i] + nums[j] + nums[k]
                        if total < best:
                            best = total
        return -1 if best == float('inf') else best
```

## C

```c
#include <limits.h>

int minimumSum(int* nums, int numsSize) {
    int best = INT_MAX;
    for (int j = 1; j < numsSize - 1; ++j) {
        int leftMin = INT_MAX;
        for (int i = 0; i < j; ++i) {
            if (nums[i] < nums[j] && nums[i] < leftMin) {
                leftMin = nums[i];
            }
        }
        int rightMin = INT_MAX;
        for (int k = j + 1; k < numsSize; ++k) {
            if (nums[k] < nums[j] && nums[k] < rightMin) {
                rightMin = nums[k];
            }
        }
        if (leftMin != INT_MAX && rightMin != INT_MAX) {
            int sum = leftMin + nums[j] + rightMin;
            if (sum < best) best = sum;
        }
    }
    return (best == INT_MAX) ? -1 : best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSum(int[] nums) {
        int n = nums.Length;
        int best = int.MaxValue;
        for (int j = 1; j < n - 1; ++j) {
            int leftMin = int.MaxValue;
            for (int i = 0; i < j; ++i) {
                if (nums[i] < nums[j] && nums[i] < leftMin) {
                    leftMin = nums[i];
                }
            }
            int rightMin = int.MaxValue;
            for (int k = j + 1; k < n; ++k) {
                if (nums[k] < nums[j] && nums[k] < rightMin) {
                    rightMin = nums[k];
                }
            }
            if (leftMin != int.MaxValue && rightMin != int.MaxValue) {
                best = Math.Min(best, leftMin + nums[j] + rightMin);
            }
        }
        return best == int.MaxValue ? -1 : best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSum = function(nums) {
    const n = nums.length;
    let best = Infinity;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (nums[i] >= nums[j]) continue;
            for (let k = j + 1; k < n; ++k) {
                if (nums[k] < nums[j]) {
                    const sum = nums[i] + nums[j] + nums[k];
                    if (sum < best) best = sum;
                }
            }
        }
    }
    return best === Infinity ? -1 : best;
};
```

## Typescript

```typescript
function minimumSum(nums: number[]): number {
    const n = nums.length;
    const left = new Array<number>(n).fill(Number.MAX_SAFE_INTEGER);
    const right = new Array<number>(n).fill(Number.MAX_SAFE_INTEGER);

    for (let j = 0; j < n; ++j) {
        let minVal = Number.MAX_SAFE_INTEGER;
        for (let i = 0; i < j; ++i) {
            if (nums[i] < nums[j] && nums[i] < minVal) {
                minVal = nums[i];
            }
        }
        left[j] = minVal;
    }

    for (let j = 0; j < n; ++j) {
        let minVal = Number.MAX_SAFE_INTEGER;
        for (let k = j + 1; k < n; ++k) {
            if (nums[k] < nums[j] && nums[k] < minVal) {
                minVal = nums[k];
            }
        }
        right[j] = minVal;
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < n; ++j) {
        if (left[j] !== Number.MAX_SAFE_INTEGER && right[j] !== Number.MAX_SAFE_INTEGER) {
            const sum = left[j] + nums[j] + right[j];
            if (sum < ans) ans = sum;
        }
    }

    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumSum($nums) {
        $n = count($nums);
        $best = PHP_INT_MAX;
        for ($j = 0; $j < $n; $j++) {
            $leftMin = null;
            for ($i = 0; $i < $j; $i++) {
                if ($nums[$i] < $nums[$j]) {
                    if ($leftMin === null || $nums[$i] < $leftMin) {
                        $leftMin = $nums[$i];
                    }
                }
            }
            if ($leftMin === null) continue;

            $rightMin = null;
            for ($k = $j + 1; $k < $n; $k++) {
                if ($nums[$k] < $nums[$j]) {
                    if ($rightMin === null || $nums[$k] < $rightMin) {
                        $rightMin = $nums[$k];
                    }
                }
            }
            if ($rightMin === null) continue;

            $sum = $leftMin + $nums[$j] + $rightMin;
            if ($sum < $best) {
                $best = $sum;
            }
        }

        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var best = Int.max
        for i in 0..<n {
            for j in (i + 1)..<n where nums[i] < nums[j] {
                for k in (j + 1)..<n where nums[k] < nums[j] {
                    let sum = nums[i] + nums[j] + nums[k]
                    if sum < best {
                        best = sum
                    }
                }
            }
        }
        return best == Int.max ? -1 : best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSum(nums: IntArray): Int {
        var best = Int.MAX_VALUE
        val n = nums.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (nums[i] >= nums[j]) continue
                for (k in j + 1 until n) {
                    if (nums[k] < nums[j]) {
                        val sum = nums[i] + nums[j] + nums[k]
                        if (sum < best) best = sum
                    }
                }
            }
        }
        return if (best == Int.MAX_VALUE) -1 else best
    }
}
```

## Dart

```dart
class Solution {
  int minimumSum(List<int> nums) {
    const int INF = 1 << 60;
    int n = nums.length;
    int ans = INF;
    for (int j = 0; j < n; ++j) {
      int left = INF;
      for (int i = 0; i < j; ++i) {
        if (nums[i] < nums[j] && nums[i] < left) left = nums[i];
      }
      int right = INF;
      for (int k = j + 1; k < n; ++k) {
        if (nums[k] < nums[j] && nums[k] < right) right = nums[k];
      }
      if (left != INF && right != INF) {
        int sum = left + nums[j] + right;
        if (sum < ans) ans = sum;
      }
    }
    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minimumSum(nums []int) int {
    n := len(nums)
    const INF = 1 << 30
    ans := INF

    for j := 1; j < n-1; j++ {
        leftMin := INF
        for i := 0; i < j; i++ {
            if nums[i] < nums[j] && nums[i] < leftMin {
                leftMin = nums[i]
            }
        }
        rightMin := INF
        for k := j + 1; k < n; k++ {
            if nums[k] < nums[j] && nums[k] < rightMin {
                rightMin = nums[k]
            }
        }
        if leftMin != INF && rightMin != INF {
            sum := leftMin + nums[j] + rightMin
            if sum < ans {
                ans = sum
            }
        }
    }

    if ans == INF {
        return -1
    }
    return ans
}
```

## Ruby

```ruby
def minimum_sum(nums)
  n = nums.length
  min_sum = Float::INFINITY
  (0...n).each do |i|
    (i + 1...n - 1).each do |j|
      next unless nums[i] < nums[j]
      (j + 1...n).each do |k|
        if nums[k] < nums[j]
          sum = nums[i] + nums[j] + nums[k]
          min_sum = sum if sum < min_sum
        end
      end
    end
  end
  min_sum == Float::INFINITY ? -1 : min_sum
end
```

## Scala

```scala
object Solution {
    def minimumSum(nums: Array[Int]): Int = {
        val n = nums.length
        var best = Int.MaxValue
        for (j <- 1 until n - 1) {
            var leftMin = Int.MaxValue
            for (i <- 0 until j) {
                if (nums(i) < nums(j) && nums(i) < leftMin) leftMin = nums(i)
            }
            var rightMin = Int.MaxValue
            for (k <- j + 1 until n) {
                if (nums(k) < nums(j) && nums(k) < rightMin) rightMin = nums(k)
            }
            if (leftMin != Int.MaxValue && rightMin != Int.MaxValue) {
                val sum = leftMin + nums(j) + rightMin
                if (sum < best) best = sum
            }
        }
        if (best == Int.MaxValue) -1 else best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut best = i32::MAX;
        for j in 1..n - 1 {
            let mid = nums[j];
            // find smallest left element less than mid
            let mut left_min = i32::MAX;
            for i in 0..j {
                if nums[i] < mid && nums[i] < left_min {
                    left_min = nums[i];
                }
            }
            if left_min == i32::MAX {
                continue;
            }
            // find smallest right element less than mid
            let mut right_min = i32::MAX;
            for k in j + 1..n {
                if nums[k] < mid && nums[k] < right_min {
                    right_min = nums[k];
                }
            }
            if right_min == i32::MAX {
                continue;
            }
            let sum = left_min + mid + right_min;
            if sum < best {
                best = sum;
            }
        }
        if best == i32::MAX { -1 } else { best }
    }
}
```

## Racket

```racket
(define/contract (minimum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums)))
    (define best
      (for/fold ([best #f]) ([j (in-range 1 (- n 1))])
        (for/fold ([best best]) ([i (in-range 0 j)])
          (if (< (vector-ref v i) (vector-ref v j))
              (for/fold ([best best]) ([k (in-range (+ j 1) n)])
                (if (< (vector-ref v k) (vector-ref v j))
                    (let ([s (+ (vector-ref v i)
                                (vector-ref v j)
                                (vector-ref v k))])
                      (if (or (not best) (< s best)) s best))
                    best))
              best))))
    (if best best -1)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_sum/1]).

-spec minimum_sum(Nums :: [integer()]) -> integer().
minimum_sum(Nums) ->
    N = length(Nums),
    Sums = [NumI + NumJ + NumK ||
                I <- lists:seq(0, N-3),
                J <- lists:seq(I+1, N-2),
                K <- lists:seq(J+1, N-1),
                NumI = lists:nth(I+1, Nums),
                NumJ = lists:nth(J+1, Nums),
                NumK = lists:nth(K+1, Nums),
                NumI < NumJ,
                NumK < NumJ],
    case Sums of
        [] -> -1;
        _  -> lists:min(Sums)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(nums :: [integer]) :: integer
  def minimum_sum(nums) do
    n = length(nums)

    combos =
      for i <- 0..(n - 3),
          j <- (i + 1)..(n - 2),
          k <- (j + 1)..(n - 1),
          do: {i, j, k}

    min_sum =
      Enum.reduce(combos, :infinity, fn {i, j, k}, acc ->
        a = Enum.at(nums, i)
        b = Enum.at(nums, j)
        c = Enum.at(nums, k)

        if a < b and c < b do
          sum = a + b + c
          if sum < acc, do: sum, else: acc
        else
          acc
        end
      end)

    case min_sum do
      :infinity -> -1
      _ -> min_sum
    end
  end
end
```
