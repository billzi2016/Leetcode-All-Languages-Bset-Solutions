# 1558. Minimum Numbers of Function Calls to Make Target Array

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        long long ops = 0;
        while (true) {
            bool allZero = true;
            for (int &x : nums) {
                if (x & 1) {
                    x--;
                    ++ops; // increment operation in forward direction
                }
                if (x > 0) allZero = false;
            }
            if (allZero) break;
            for (int &x : nums) {
                x >>= 1; // divide by 2, corresponds to a double operation
            }
            ++ops; // double operation
        }
        return static_cast<int>(ops);
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        long ops = 0;
        int max = 0;
        for (int num : nums) {
            ops += Integer.bitCount(num);
            if (num > max) {
                max = num;
            }
        }
        if (max > 0) {
            int bits = 32 - Integer.numberOfLeadingZeros(max);
            ops += bits - 1;
        }
        return (int) ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = 0
        max_num = 0
        for n in nums:
            inc += bin(n).count('1')
            if n > max_num:
                max_num = n
        doubles = max_num.bit_length() - 1 if max_num else 0
        return inc + doubles
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        inc = 0
        max_len = 0
        for x in nums:
            inc += bin(x).count('1')
            if x:
                bl = x.bit_length()
                if bl > max_len:
                    max_len = bl
        return inc + (max_len - 1 if max_len else 0)
```

## C

```c
int minOperations(int* nums, int numsSize) {
    long long ops = 0;
    while (1) {
        int allZero = 1;
        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] & 1) {
                ops++;
                nums[i]--;
            }
            if (nums[i] != 0) allZero = 0;
        }
        if (allZero) break;
        ops++; // double operation
        for (int i = 0; i < numsSize; ++i) {
            nums[i] >>= 1;
        }
    }
    return (int)ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        long operations = 0;
        bool hasPositive = true;

        while (hasPositive) {
            hasPositive = false;
            // Subtract 1 from all odd elements
            for (int i = 0; i < nums.Length; i++) {
                if ((nums[i] & 1) == 1) {
                    operations++;
                    nums[i]--;
                }
                if (nums[i] > 0) hasPositive = true;
            }

            // If all elements are zero, we're done
            if (!hasPositive) break;

            // Divide all elements by 2 (equivalent to a double operation)
            for (int i = 0; i < nums.Length; i++) {
                nums[i] >>= 1;
            }
            operations++; // count the double operation
        }

        return (int)operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let incCount = 0;
    let maxBits = 0;
    for (let num of nums) {
        let bits = 0;
        while (num > 0) {
            if (num & 1) incCount++;
            num = num >>> 1;
            bits++;
        }
        if (bits > maxBits) maxBits = bits;
    }
    return maxBits === 0 ? 0 : incCount + maxBits - 1;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    let ops = 0;
    const n = nums.length;
    const arr = nums.slice(); // mutable copy

    while (true) {
        let allZero = true;

        for (let i = 0; i < n; i++) {
            if ((arr[i] & 1) === 1) {
                arr[i]--;
                ops++;
            }
            if (arr[i] !== 0) {
                allZero = false;
            }
        }

        if (allZero) break;

        for (let i = 0; i < n; i++) {
            arr[i] >>= 1; // divide by 2
        }
        ops++; // one double operation
    }

    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $ans = 0;
        $n = count($nums);
        while (true) {
            $allZero = true;
            // Decrement odd elements (reverse of increment)
            for ($i = 0; $i < $n; $i++) {
                if ($nums[$i] & 1) {          // odd
                    $nums[$i]--;
                    $ans++;
                }
                if ($nums[$i] != 0) {
                    $allZero = false;
                }
            }
            if ($allZero) {
                break;
            }
            // Divide all elements by 2 (reverse of double)
            for ($i = 0; $i < $n; $i++) {
                $nums[$i] = intdiv($nums[$i], 2);
            }
            $ans++;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var increments = 0
        var maxBits = 0
        
        for num in nums {
            var x = num
            var bits = 0
            while x > 0 {
                if (x & 1) == 1 { increments += 1 }
                x >>= 1
                bits += 1
            }
            if bits > maxBits { maxBits = bits }
        }
        
        let doubles = max(0, maxBits - 1)
        return increments + doubles
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        var increments = 0
        var maxDoublings = 0
        for (num in nums) {
            if (num == 0) continue
            increments += Integer.bitCount(num)
            val bits = 31 - Integer.numberOfLeadingZeros(num)
            if (bits > maxDoublings) maxDoublings = bits
        }
        return increments + maxDoublings
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    List<int> arr = List.from(nums);
    int operations = 0;
    while (true) {
      bool allZero = true;
      // Decrement odd elements
      for (int i = 0; i < arr.length; i++) {
        if ((arr[i] & 1) == 1) {
          arr[i]--;
          operations++;
        }
        if (arr[i] != 0) {
          allZero = false;
        }
      }
      if (allZero) break;
      // Divide all elements by 2
      for (int i = 0; i < arr.length; i++) {
        arr[i] >>= 1;
      }
      operations++;
    }
    return operations;
  }
}
```

## Golang

```go
import "math/bits"

func minOperations(nums []int) int {
    total := 0
    maxLen := 0
    for _, v := range nums {
        if v == 0 {
            continue
        }
        total += bits.OnesCount(uint(v))
        l := bits.Len(uint(v))
        if l > maxLen {
            maxLen = l
        }
    }
    if maxLen > 0 {
        total += maxLen - 1
    }
    return total
}
```

## Ruby

```ruby
def min_operations(nums)
  ops = 0
  loop do
    nums.each_index do |i|
      if nums[i].odd?
        ops += 1
        nums[i] -= 1
      end
    end
    break if nums.all?(&:zero?)
    nums.map! { |v| v / 2 }
    ops += 1
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var totalInc = 0
        var maxBit = 0
        for (num <- nums) {
            totalInc += Integer.bitCount(num)
            if (num != 0) {
                val msb = 31 - Integer.numberOfLeadingZeros(num)
                if (msb > maxBit) maxBit = msb
            }
        }
        totalInc + maxBit
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut a = nums.clone();
        let mut ops: i64 = 0;
        loop {
            if !a.iter().any(|&x| x > 0) {
                break;
            }
            // Increment operations for odd elements
            for v in &mut a {
                if *v % 2 == 1 {
                    ops += 1;
                    *v -= 1;
                }
            }
            // If all become zero after handling odds, we're done
            if !a.iter().any(|&x| x > 0) {
                break;
            }
            // Double operation (divide by 2 for reverse process)
            for v in &mut a {
                *v /= 2;
            }
            ops += 1;
        }
        ops as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (ops 0))
    (let loop ()
      ;; process odd increments
      (for ([i (in-range n)])
        (let ([val (vector-ref arr i)])
          (when (odd? val)
            (set! ops (+ ops 1))
            (vector-set! arr i (- val 1)))))
      ;; check if any element is still positive
      (define still-positive? #f)
      (for ([i (in-range n)])
        (when (> (vector-ref arr i) 0)
          (set! still-positive? #t)))
      (when still-positive?
        ;; divide all by 2 (right shift)
        (for ([i (in-range n)])
          (let ([val (vector-ref arr i)])
            (vector-set! arr i (arithmetic-shift val -1))))
        (set! ops (+ ops 1))
        (loop)))
    ops))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    {TotalInc, MaxLen} = lists:foldl(fun(N, {IncAcc, LenAcc}) ->
        {Pop, Len} = popcount_len(N, 0, 0),
        {IncAcc + Pop, erlang:max(LenAcc, Len)}
    end, {0,0}, Nums),
    case MaxLen of
        0 -> 0;
        _ -> TotalInc + MaxLen - 1
    end.

popcount_len(0, Pop, Len) ->
    {Pop, Len};
popcount_len(N, Pop, Len) ->
    Bit = N band 1,
    NewPop = case Bit of
        1 -> Pop + 1;
        _ -> Pop
    end,
    popcount_len(N bsr 1, NewPop, Len + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    max_num = Enum.max(nums)

    if max_num == 0 do
      0
    else
      total_ones = Enum.reduce(nums, 0, fn x, acc -> acc + bit_count(x) end)
      bits = msb_pos(max_num)
      total_ones + bits - 1
    end
  end

  defp bit_count(0), do: 0

  defp bit_count(n, acc \\ 0)

  defp bit_count(0, acc), do: acc

  defp bit_count(n, acc) do
    bit = n &&& 1
    bit_count(n >>> 1, acc + bit)
  end

  defp msb_pos(0), do: 0

  defp msb_pos(n, pos \\ 0)

  defp msb_pos(0, pos), do: pos

  defp msb_pos(n, pos) do
    msb_pos(n >>> 1, pos + 1)
  end
end
```
