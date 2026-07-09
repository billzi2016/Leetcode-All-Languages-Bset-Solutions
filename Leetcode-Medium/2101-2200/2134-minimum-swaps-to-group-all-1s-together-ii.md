# 2134. Minimum Swaps to Group All 1's Together II

## Cpp

```cpp
class Solution {
public:
    int minSwaps(std::vector<int>& nums) {
        int n = nums.size();
        int totalOnes = 0;
        for (int v : nums) totalOnes += v;
        if (totalOnes == 0 || totalOnes == n) return 0;

        int curOnes = 0;
        for (int i = 0; i < totalOnes; ++i) curOnes += nums[i];
        int maxOnes = curOnes;

        for (int start = 1; start < n; ++start) {
            curOnes -= nums[start - 1];
            curOnes += nums[(start + totalOnes - 1) % n];
            if (curOnes > maxOnes) maxOnes = curOnes;
        }
        return totalOnes - maxOnes;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int totalOnes = 0;
        for (int num : nums) {
            if (num == 1) totalOnes++;
        }
        // If there are no ones or all are ones, no swaps needed
        if (totalOnes == 0 || totalOnes == n) return 0;

        int current = 0;
        for (int i = 0; i < totalOnes; i++) {
            current += nums[i];
        }
        int maxOnesInWindow = current;

        for (int start = 1; start < n; start++) {
            int outIdx = start - 1;
            int inIdx = (start + totalOnes - 1) % n;
            current -= nums[outIdx];
            current += nums[inIdx];
            if (current > maxOnesInWindow) {
                maxOnesInWindow = current;
            }
        }

        return totalOnes - maxOnesInWindow;
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_ones = sum(nums)
        n = len(nums)
        if total_ones == 0 or total_ones == n:
            return 0

        # Duplicate the array to handle circular windows
        extended = nums * 2

        # Count ones in the initial window
        current = sum(extended[:total_ones])
        max_ones_in_window = current

        # Slide the window across the original length positions
        for start in range(1, n):
            # Remove element exiting the window and add new entering element
            current -= extended[start - 1]
            current += extended[start + total_ones - 1]
            if current > max_ones_in_window:
                max_ones_in_window = current

        return total_ones - max_ones_in_window
```

## Python3

```python
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        if total_ones <= 1 or total_ones == len(nums):
            return 0
        
        n = len(nums)
        # count ones in the initial window
        current = sum(nums[:total_ones])
        max_in_window = current
        
        for i in range(1, n):
            # slide window: remove leftmost, add new rightmost (circularly)
            current -= nums[i - 1]
            current += nums[(i + total_ones - 1) % n]
            if current > max_in_window:
                max_in_window = current
        
        return total_ones - max_in_window
```

## C

```c
int minSwaps(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int totalOnes = 0;
    for (int i = 0; i < numsSize; ++i) {
        totalOnes += nums[i];
    }
    if (totalOnes <= 1) return 0; // zero or one '1' needs no swaps

    int currentOnes = 0;
    for (int i = 0; i < totalOnes; ++i) {
        currentOnes += nums[i];
    }
    int maxOnesInWindow = currentOnes;

    for (int start = 1; start < numsSize; ++start) {
        // element leaving the window
        currentOnes -= nums[start - 1];
        // element entering the window
        int idx = (start + totalOnes - 1) % numsSize;
        currentOnes += nums[idx];
        if (currentOnes > maxOnesInWindow) {
            maxOnesInWindow = currentOnes;
        }
    }

    return totalOnes - maxOnesInWindow;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSwaps(int[] nums)
    {
        int n = nums.Length;
        int totalOnes = 0;
        foreach (int num in nums)
            if (num == 1) totalOnes++;

        // No swaps needed if there are no 1's or all elements are 1
        if (totalOnes == 0 || totalOnes == n)
            return 0;

        int currentOnes = 0;
        for (int i = 0; i < totalOnes; i++)
            if (nums[i] == 1) currentOnes++;

        int maxOnes = currentOnes;

        for (int start = 1; start < n; start++)
        {
            // element leaving the window
            if (nums[start - 1] == 1) currentOnes--;

            // element entering the window
            int endIdx = (start + totalOnes - 1) % n;
            if (nums[endIdx] == 1) currentOnes++;

            if (currentOnes > maxOnes) maxOnes = currentOnes;
        }

        return totalOnes - maxOnes;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function(nums) {
    const n = nums.length;
    let totalOnes = 0;
    for (let i = 0; i < n; ++i) totalOnes += nums[i];
    if (totalOnes === 0 || totalOnes === n) return 0;

    // initial window
    let current = 0;
    for (let i = 0; i < totalOnes; ++i) {
        current += nums[i];
    }
    let maxOnes = current;

    // slide the window around the circular array
    for (let start = 1; start < n; ++start) {
        current -= nums[start - 1];
        const addIdx = (start + totalOnes - 1) % n;
        current += nums[addIdx];
        if (current > maxOnes) maxOnes = current;
    }

    return totalOnes - maxOnes;
};
```

## Typescript

```typescript
function minSwaps(nums: number[]): number {
    const n = nums.length;
    let totalOnes = 0;
    for (const v of nums) {
        if (v === 1) totalOnes++;
    }
    if (totalOnes === 0 || totalOnes === n) return 0;

    // initial window sum
    let current = 0;
    for (let i = 0; i < totalOnes; i++) {
        current += nums[i];
    }
    let maxOnes = current;

    for (let start = 1; start < n; start++) {
        // element leaving the window
        current -= nums[start - 1];
        // element entering the window
        const addIdx = (start + totalOnes - 1) % n;
        current += nums[addIdx];
        if (current > maxOnes) maxOnes = current;
    }

    return totalOnes - maxOnes;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minSwaps($nums) {
        $n = count($nums);
        $totalOnes = array_sum($nums);
        
        // If there are no 1's or all are 1's, no swaps needed.
        if ($totalOnes == 0 || $totalOnes == $n) {
            return 0;
        }
        
        // Count ones in the initial window of size totalOnes
        $current = 0;
        for ($i = 0; $i < $totalOnes; $i++) {
            $current += $nums[$i];
        }
        $maxOnes = $current;
        
        // Slide the window across the circular array
        for ($start = 1; $start < $n; $start++) {
            // Remove the element leaving the window
            $current -= $nums[$start - 1];
            // Add the new element entering the window
            $addIdx = ($start + $totalOnes - 1) % $n;
            $current += $nums[$addIdx];
            
            if ($current > $maxOnes) {
                $maxOnes = $current;
            }
        }
        
        // Minimum swaps needed is the number of zeros inside the best window
        return $totalOnes - $maxOnes;
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        let totalOnes = nums.reduce(0, +)
        if totalOnes == 0 || totalOnes == n { return 0 }
        
        var currentOnes = 0
        for i in 0..<totalOnes {
            if nums[i] == 1 { currentOnes += 1 }
        }
        var maxOnesInWindow = currentOnes
        
        for start in 1..<n {
            if nums[start - 1] == 1 { currentOnes -= 1 }
            let endIdx = (start + totalOnes - 1) % n
            if nums[endIdx] == 1 { currentOnes += 1 }
            if currentOnes > maxOnesInWindow {
                maxOnesInWindow = currentOnes
            }
        }
        
        return totalOnes - maxOnesInWindow
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(nums: IntArray): Int {
        val n = nums.size
        var totalOnes = 0
        for (v in nums) if (v == 1) totalOnes++
        if (totalOnes <= 1) return 0

        var currentOnes = 0
        // initial window
        for (i in 0 until totalOnes) {
            if (nums[i % n] == 1) currentOnes++
        }
        var maxOnes = currentOnes

        for (start in 1 until n) {
            // element leaving the window
            if (nums[(start - 1) % n] == 1) currentOnes--
            // element entering the window
            val endIdx = (start + totalOnes - 1) % n
            if (nums[endIdx] == 1) currentOnes++
            if (currentOnes > maxOnes) maxOnes = currentOnes
        }
        return totalOnes - maxOnes
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(List<int> nums) {
    int n = nums.length;
    int totalOnes = 0;
    for (int v in nums) {
      totalOnes += v;
    }
    if (totalOnes == 0 || totalOnes == n) return 0;

    int onesInWindow = 0;
    for (int i = 0; i < totalOnes; ++i) {
      if (nums[i] == 1) onesInWindow++;
    }
    int maxOnes = onesInWindow;

    for (int start = 1; start < n; ++start) {
      // element leaving the window
      if (nums[start - 1] == 1) onesInWindow--;
      // element entering the window
      int endIdx = (start + totalOnes - 1) % n;
      if (nums[endIdx] == 1) onesInWindow++;
      if (onesInWindow > maxOnes) maxOnes = onesInWindow;
    }

    return totalOnes - maxOnes;
  }
}
```

## Golang

```go
func minSwaps(nums []int) int {
    n := len(nums)
    totalOnes := 0
    for _, v := range nums {
        if v == 1 {
            totalOnes++
        }
    }
    if totalOnes == 0 || totalOnes == n {
        return 0
    }

    // Count ones in the initial window of size totalOnes
    currentOnes := 0
    for i := 0; i < totalOnes; i++ {
        if nums[i] == 1 {
            currentOnes++
        }
    }
    maxOnes := currentOnes

    // Slide the window around the circular array
    for start := 1; start < n; start++ {
        // element exiting the window
        if nums[start-1] == 1 {
            currentOnes--
        }
        // element entering the window
        idx := (start + totalOnes - 1) % n
        if nums[idx] == 1 {
            currentOnes++
        }
        if currentOnes > maxOnes {
            maxOnes = currentOnes
        }
    }

    return totalOnes - maxOnes
}
```

## Ruby

```ruby
def min_swaps(nums)
  n = nums.length
  total_ones = nums.sum
  return 0 if total_ones == 0 || total_ones == n

  # initial window
  current = 0
  (0...total_ones).each { |i| current += nums[i] }
  max_ones = current

  (1...n).each do |start|
    current -= nums[start - 1]
    idx = (start + total_ones - 1) % n
    current += nums[idx]
    max_ones = [max_ones, current].max
  end

  total_ones - max_ones
end
```

## Scala

```scala
object Solution {
    def minSwaps(nums: Array[Int]): Int = {
        val n = nums.length
        var totalOnes = 0
        for (v <- nums) if (v == 1) totalOnes += 1

        if (totalOnes == 0 || totalOnes == n) return 0

        var current = 0
        for (i <- 0 until totalOnes) {
            if (nums(i % n) == 1) current += 1
        }
        var maxOnes = current

        for (start <- 1 until n) {
            // element leaving the window
            if (nums((start - 1) % n) == 1) current -= 1
            // element entering the window
            val endIdx = (start + totalOnes - 1) % n
            if (nums(endIdx) == 1) current += 1

            if (current > maxOnes) maxOnes = current
        }

        totalOnes - maxOnes
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total_ones = nums.iter().filter(|&&x| x == 1).count();
        if total_ones == 0 || total_ones == n {
            return 0;
        }

        // Count ones in the initial window [0, total_ones)
        let mut current: usize = (0..total_ones)
            .map(|i| if nums[i] == 1 { 1 } else { 0 })
            .sum();
        let mut max_ones = current;

        for i in 1..n {
            // element leaving the window
            if nums[i - 1] == 1 {
                current -= 1;
            }
            // element entering the window
            let idx = (i + total_ones - 1) % n;
            if nums[idx] == 1 {
                current += 1;
            }
            if current > max_ones {
                max_ones = current;
            }
        }

        (total_ones - max_ones) as i32
    }
}
```

## Racket

```racket
(define/contract (min-swaps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let ((total-ones
           (for/sum ([i (in-range n)])
             (if (= (vector-ref v i) 1) 1 0))))
      (if (or (= total-ones 0) (= total-ones n))
          0
          (let* ((init-sum
                  (let loop ((i 0) (s 0))
                    (if (= i total-ones)
                        s
                        (loop (add1 i)
                              (+ s (if (= (vector-ref v i) 1) 1 0))))))
                 (max-ones
                  (let loop ((start 1) (curr init-sum) (best init-sum))
                    (if (= start n)
                        best
                        (let* ((out-index (sub1 start))
                               (in-index (modulo (+ start total-ones -1) n))
                               (out-val (if (= (vector-ref v out-index) 1) 1 0))
                               (in-val (if (= (vector-ref v in-index) 1) 1 0))
                               (new-curr (+ (- curr out-val) in-val)))
                          (loop (add1 start) new-curr (max best new-curr)))))))
            (- total-ones max-ones)))))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps/1]).

-spec min_swaps(Nums :: [integer()]) -> integer().
min_swaps(Nums) ->
    K = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    N = length(Nums),
    case K of
        0 -> 0;
        _ when K == N -> 0;
        _ ->
            Tuple = list_to_tuple(Nums),
            InitialSum = sum_first(K, Tuple, 1),
            MinZeros = K - InitialSum,
            loop(1, N, K, Tuple, InitialSum, MinZeros)
    end.

%% Sum of first Len elements starting from Index (1‑based) in the tuple
-spec sum_first(integer(), tuple(), integer()) -> integer().
sum_first(0, _Tuple, _Idx) ->
    0;
sum_first(Len, Tuple, Idx) ->
    Elem = element(Idx, Tuple),
    Elem + sum_first(Len - 1, Tuple, Idx + 1).

%% Sliding window over the circular array
-spec loop(integer(), integer(), integer(), tuple(), integer(), integer()) -> integer().
loop(I, N, K, Tuple, CurrSum, Min) when I == N ->
    Min;
loop(I, N, K, Tuple, CurrSum, Min) ->
    OutIdx = I - 1,
    InIdx = I + K - 1,
    OutVal = element((OutIdx rem N) + 1, Tuple),
    InVal = element((InIdx rem N) + 1, Tuple),
    NewSum = CurrSum - OutVal + InVal,
    Zeros = K - NewSum,
    NewMin = if Zeros < Min -> Zeros; true -> Min end,
    loop(I + 1, N, K, Tuple, NewSum, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(nums :: [integer]) :: integer
  def min_swaps(nums) do
    n = length(nums)
    total_ones = Enum.count(nums, fn x -> x == 1 end)

    cond do
      total_ones <= 1 or total_ones == 0 or total_ones == n ->
        0

      true ->
        t = List.to_tuple(nums)

        get = fn idx ->
          :erlang.element(rem(idx, n) + 1, t)
        end

        init_sum =
          Enum.reduce(0..(total_ones - 1), 0, fn i, acc -> acc + get.(i) end)

        {max_ones, _} =
          Enum.reduce(1..(n - 1), {init_sum, init_sum}, fn start, {max_sofar, cur} ->
            out_idx = start - 1
            in_idx = start + total_ones - 1

            cur2 = cur - get.(out_idx) + get.(in_idx)
            max_new = if cur2 > max_sofar, do: cur2, else: max_sofar
            {max_new, cur2}
          end)

        total_ones - max_ones
    end
  end
end
```
