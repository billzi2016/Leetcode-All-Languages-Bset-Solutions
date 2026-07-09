# 3452. Sum of Good Numbers

## Cpp

```cpp
class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int n = nums.size();
        int total = 0;
        for (int i = 0; i < n; ++i) {
            bool good = true;
            if (i - k >= 0 && nums[i] <= nums[i - k]) good = false;
            if (i + k < n && nums[i] <= nums[i + k]) good = false;
            if (good) total += nums[i];
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int n = nums.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            boolean leftOk = true;
            boolean rightOk = true;
            int leftIdx = i - k;
            int rightIdx = i + k;
            if (leftIdx >= 0) {
                leftOk = nums[i] > nums[leftIdx];
            }
            if (rightIdx < n) {
                rightOk = nums[i] > nums[rightIdx];
            }
            // If both neighboring indices exist, need both conditions true.
            // If only one exists, that condition must be true.
            // If none exist, it's automatically good (both flags remain true).
            if (leftOk && rightOk) {
                sum += nums[i];
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(n):
            good = True
            left = i - k
            right = i + k
            if left >= 0 and not (nums[i] > nums[left]):
                good = False
            if right < n and not (nums[i] > nums[right]):
                good = False
            if good:
                total += nums[i]
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i, val in enumerate(nums):
            good = True
            left = i - k
            if left >= 0 and not (val > nums[left]):
                good = False
            right = i + k
            if right < n and not (val > nums[right]):
                good = False
            if good:
                total += val
        return total
```

## C

```c
int sumOfGoodNumbers(int* nums, int numsSize, int k) {
    int sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        int good = 1;
        if (i - k >= 0 && !(nums[i] > nums[i - k])) good = 0;
        if (i + k < numsSize && !(nums[i] > nums[i + k])) good = 0;
        if (good) sum += nums[i];
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfGoodNumbers(int[] nums, int k) {
        int n = nums.Length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            bool leftOk = true;
            bool rightOk = true;
            if (i - k >= 0) {
                leftOk = nums[i] > nums[i - k];
            }
            if (i + k < n) {
                rightOk = nums[i] > nums[i + k];
            }
            if (leftOk && rightOk) {
                sum += nums[i];
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
 * @param {number} k
 * @return {number}
 */
var sumOfGoodNumbers = function(nums, k) {
    let n = nums.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        let good = true;
        const left = i - k;
        const right = i + k;
        if (left >= 0 && !(nums[i] > nums[left])) good = false;
        if (right < n && !(nums[i] > nums[right])) good = false;
        if (good) total += nums[i];
    }
    return total;
};
```

## Typescript

```typescript
function sumOfGoodNumbers(nums: number[], k: number): number {
    let sum = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const leftIdx = i - k;
        const rightIdx = i + k;
        let good = true;
        if (leftIdx >= 0 && !(nums[i] > nums[leftIdx])) {
            good = false;
        }
        if (rightIdx < n && !(nums[i] > nums[rightIdx])) {
            good = false;
        }
        if (good) sum += nums[i];
    }
    return sum;
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
    function sumOfGoodNumbers($nums, $k) {
        $n = count($nums);
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $good = true;
            $left = $i - $k;
            if ($left >= 0 && $nums[$i] <= $nums[$left]) {
                $good = false;
            }
            $right = $i + $k;
            if ($right < $n && $nums[$i] <= $nums[$right]) {
                $good = false;
            }
            if ($good) {
                $sum += $nums[$i];
            }
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfGoodNumbers(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var sum = 0
        for i in 0..<n {
            var good = true
            if i - k >= 0 && !(nums[i] > nums[i - k]) {
                good = false
            }
            if i + k < n && !(nums[i] > nums[i + k]) {
                good = false
            }
            if good {
                sum += nums[i]
            }
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfGoodNumbers(nums: IntArray, k: Int): Int {
        var sum = 0
        val n = nums.size
        for (i in 0 until n) {
            var good = true
            val left = i - k
            if (left >= 0 && nums[i] <= nums[left]) good = false
            val right = i + k
            if (right < n && nums[i] <= nums[right]) good = false
            if (good) sum += nums[i]
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int sumOfGoodNumbers(List<int> nums, int k) {
    int n = nums.length;
    int sum = 0;
    for (int i = 0; i < n; i++) {
      bool leftOk = true;
      if (i - k >= 0) {
        leftOk = nums[i] > nums[i - k];
      }
      bool rightOk = true;
      if (i + k < n) {
        rightOk = nums[i] > nums[i + k];
      }
      if (leftOk && rightOk) {
        sum += nums[i];
      }
    }
    return sum;
  }
}
```

## Golang

```go
func sumOfGoodNumbers(nums []int, k int) int {
	sum := 0
	n := len(nums)
	for i, v := range nums {
		good := true
		if i-k >= 0 && !(v > nums[i-k]) {
			good = false
		}
		if i+k < n && !(v > nums[i+k]) {
			good = false
		}
		if good {
			sum += v
		}
	}
	return sum
}
```

## Ruby

```ruby
def sum_of_good_numbers(nums, k)
  n = nums.length
  total = 0
  (0...n).each do |i|
    good = true
    left = i - k
    right = i + k
    good &&= nums[i] > nums[left] if left >= 0
    good &&= nums[i] > nums[right] if right < n
    total += nums[i] if good
  end
  total
end
```

## Scala

```scala
object Solution {
    def sumOfGoodNumbers(nums: Array[Int], k: Int): Int = {
        var sum = 0
        val n = nums.length
        for (i <- 0 until n) {
            var good = true
            if (i - k >= 0 && !(nums(i) > nums(i - k))) good = false
            if (i + k < n && !(nums(i) > nums(i + k))) good = false
            if (good) sum += nums(i)
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_good_numbers(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        let mut sum = 0;
        for i in 0..n {
            let val = nums[i];
            let left_ok = if i >= k_usize {
                val > nums[i - k_usize]
            } else {
                true
            };
            let right_ok = if i + k_usize < n {
                val > nums[i + k_usize]
            } else {
                true
            };
            if left_ok && right_ok {
                sum += val;
            }
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (sum-of-good-numbers nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums)))
    (let loop ((i 0) (acc 0))
      (if (= i n)
          acc
          (let* ((v (list-ref nums i))
                 (left-ok (if (>= (- i k) 0)
                              (> v (list-ref nums (- i k)))
                              #t))
                 (right-ok (if (< (+ i k) n)
                               (> v (list-ref nums (+ i k)))
                               #t))
                 (good? (and left-ok right-ok)))
            (loop (add1 i) (if good? (+ acc v) acc)))))))
```

## Erlang

```erlang
-spec sum_of_good_numbers(Nums :: [integer()], K :: integer()) -> integer().
sum_of_good_numbers(Nums, K) ->
    N = length(Nums),
    loop(Nums, K, N, 0, 0).

loop(_Nums, _K, N, Index, Acc) when Index >= N ->
    Acc;
loop(Nums, K, N, Index, Acc) ->
    H = lists:nth(Index + 1, Nums),
    LeftIdx = Index - K,
    RightIdx = Index + K,
    Good =
        case {LeftIdx >= 0, RightIdx < N} of
            {true, true} ->
                L = lists:nth(LeftIdx + 1, Nums),
                R = lists:nth(RightIdx + 1, Nums),
                H > L andalso H > R;
            {true, false} ->
                L = lists:nth(LeftIdx + 1, Nums),
                H > L;
            {false, true} ->
                R = lists:nth(RightIdx + 1, Nums),
                H > R;
            {false, false} -> true
        end,
    NewAcc = if Good -> Acc + H; true -> Acc end,
    loop(Nums, K, N, Index + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_good_numbers(nums :: [integer], k :: integer) :: integer
  def sum_of_good_numbers(nums, k) do
    len = length(nums)

    nums
    |> Enum.with_index()
    |> Enum.reduce(0, fn {val, i}, acc ->
      left_idx = i - k
      right_idx = i + k

      left_val = if left_idx >= 0, do: Enum.at(nums, left_idx), else: nil
      right_val = if right_idx < len, do: Enum.at(nums, right_idx), else: nil

      good? =
        (left_val == nil or val > left_val) and
          (right_val == nil or val > right_val)

      if good?, do: acc + val, else: acc
    end)
  end
end
```
