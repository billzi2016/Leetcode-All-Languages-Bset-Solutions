# 2932. Maximum Strong Pair XOR I

## Cpp

```cpp
class Solution {
public:
    int maximumStrongPairXor(vector<int>& nums) {
        int n = nums.size();
        int best = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int a = min(nums[i], nums[j]);
                int b = max(nums[i], nums[j]);
                if (b <= 2 * a) {
                    best = max(best, nums[i] ^ nums[j]);
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maximumStrongPairXor(int[] nums) {
        int n = nums.length;
        int maxXor = 0;
        int[] msb = new int[n];
        for (int i = 0; i < n; i++) {
            msb[i] = 31 - Integer.numberOfLeadingZeros(nums[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (Math.abs(msb[i] - msb[j]) <= 1) {
                    int xor = nums[i] ^ nums[j];
                    if (xor > maxXor) maxXor = xor;
                }
            }
        }
        return maxXor;
    }
}
```

## Python

```python
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i, n):
                b = nums[j]
                mn = a if a < b else b
                mx = b if a < b else a
                if mx <= 2 * mn:
                    cur = a ^ b
                    if cur > max_xor:
                        max_xor = cur
        return max_xor
```

## Python3

```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                a, b = nums[i], nums[j]
                if max(a, b) <= 2 * min(a, b):
                    xor_val = a ^ b
                    if xor_val > ans:
                        ans = xor_val
        return ans
```

## C

```c
int maximumStrongPairXor(int* nums, int numsSize) {
    int maxXor = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i; j < numsSize; ++j) {
            int a = nums[i];
            int b = nums[j];
            int small = a < b ? a : b;
            int large = a > b ? a : b;
            if (large <= 2 * small) { // strong pair condition
                int cur = a ^ b;
                if (cur > maxXor) maxXor = cur;
            }
        }
    }
    return maxXor;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumStrongPairXor(int[] nums) {
        int n = nums.Length;
        int maxXor = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int a = nums[i];
                int b = nums[j];
                int mn = Math.Min(a, b);
                int mx = Math.Max(a, b);
                if (mx <= 2 * mn) {
                    int xorVal = a ^ b;
                    if (xorVal > maxXor) maxXor = xorVal;
                }
            }
        }
        return maxXor;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumStrongPairXor = function(nums) {
    let n = nums.length;
    let maxXor = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            const a = nums[i];
            const b = nums[j];
            const mn = Math.min(a, b);
            const mx = Math.max(a, b);
            if (mx <= 2 * mn) {
                const xorVal = a ^ b;
                if (xorVal > maxXor) maxXor = xorVal;
            }
        }
    }
    return maxXor;
};
```

## Typescript

```typescript
function maximumStrongPairXor(nums: number[]): number {
    let maxXor = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            const x = nums[i];
            const y = nums[j];
            const diff = Math.abs(x - y);
            const mn = Math.min(x, y);
            if (diff <= mn) {
                const xorVal = x ^ y;
                if (xorVal > maxXor) maxXor = xorVal;
            }
        }
    }
    return maxXor;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumStrongPairXor($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                $a = $nums[$i];
                $b = $nums[$j];
                $mn = min($a, $b);
                $mx = max($a, $b);
                if ($mx <= 2 * $mn) {
                    $xor = $a ^ $b;
                    if ($xor > $ans) {
                        $ans = $xor;
                    }
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumStrongPairXor(_ nums: [Int]) -> Int {
        var maxXor = 0
        let n = nums.count
        for i in 0..<n {
            for j in i..<n {
                let a = nums[i]
                let b = nums[j]
                let mn = min(a, b)
                let mx = max(a, b)
                if mx - mn <= mn {
                    maxXor = max(maxXor, a ^ b)
                }
            }
        }
        return maxXor
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumStrongPairXor(nums: IntArray): Int {
        var maxXor = 0
        val n = nums.size
        for (i in 0 until n) {
            for (j in i until n) {
                val a = nums[i]
                val b = nums[j]
                val minVal = if (a < b) a else b
                val maxVal = if (a > b) a else b
                if (maxVal <= 2 * minVal) {
                    val xor = a xor b
                    if (xor > maxXor) maxXor = xor
                }
            }
        }
        return maxXor
    }
}
```

## Dart

```dart
class Solution {
  int maximumStrongPairXor(List<int> nums) {
    int n = nums.length;
    int maxXor = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        int a = nums[i];
        int b = nums[j];
        int mn = a < b ? a : b;
        int mx = a > b ? a : b;
        if (mx <= 2 * mn) {
          int xorVal = a ^ b;
          if (xorVal > maxXor) {
            maxXor = xorVal;
          }
        }
      }
    }
    return maxXor;
  }
}
```

## Golang

```go
func maximumStrongPairXor(nums []int) int {
    maxXor := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            a, b := nums[i], nums[j]
            mn, mx := a, b
            if mn > mx {
                mn, mx = mx, mn
            }
            if mx <= 2*mn {
                xorVal := a ^ b
                if xorVal > maxXor {
                    maxXor = xorVal
                }
            }
        }
    }
    return maxXor
}
```

## Ruby

```ruby
def maximum_strong_pair_xor(nums)
  groups = Hash.new { |h, k| h[k] = [] }
  nums.each do |num|
    len = num.to_s.length
    groups[len] << num
  end

  max_xor = 0
  groups.each_value do |arr|
    n = arr.size
    (0...n).each do |i|
      (i...n).each do |j|
        xor_val = arr[i] ^ arr[j]
        max_xor = xor_val if xor_val > max_xor
      end
    end
  end

  max_xor
end
```

## Scala

```scala
object Solution {
    def maximumStrongPairXor(nums: Array[Int]): Int = {
        var maxXor = 0
        val n = nums.length
        for (i <- 0 until n) {
            for (j <- i until n) {
                val a = nums(i)
                val b = nums(j)
                if (math.abs(a - b) <= math.min(a, b)) {
                    val xorVal = a ^ b
                    if (xorVal > maxXor) maxXor = xorVal
                }
            }
        }
        maxXor
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        let mut max_xor = 0;
        let n = nums.len();
        for i in 0..n {
            for j in i..n {
                let a = nums[i];
                let b = nums[j];
                let (min_val, max_val) = if a < b { (a, b) } else { (b, a) };
                if max_val <= 2 * min_val {
                    max_xor = max_xor.max(a ^ b);
                }
            }
        }
        max_xor
    }
}
```

## Racket

```racket
(define/contract (maximum-strong-pair-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (maxxor 0))
    (for ([i (in-range n)])
      (for ([j (in-range i n)])
        (let* ((x (list-ref nums i))
               (y (list-ref nums j))
               (diff (abs (- x y)))
               (minxy (if (< x y) x y)))
          (when (<= diff minxy)
            (let ((xorval (bitwise-xor x y)))
              (when (> xorval maxxor)
                (set! maxxor xorval)))))))
    maxxor))
```

## Erlang

```erlang
-spec maximum_strong_pair_xor(Nums :: [integer()]) -> integer().
maximum_strong_pair_xor(Nums) ->
    max_xor_pairs(Nums, 0).

max_xor_pairs([], Max) -> Max;
max_xor_pairs([H|T], MaxSoFar) ->
    NewMax = max_with_element(H, T, MaxSoFar),
    max_xor_pairs(T, NewMax).

max_with_element(_, [], Max) -> Max;
max_with_element(Elem, [Y|Ys], Max) ->
    Updated = case is_strong_pair(Elem, Y) of
                  true  -> erlang:max(Max, Elem bxor Y);
                  false -> Max
              end,
    max_with_element(Elem, Ys, Updated).

is_strong_pair(A, B) ->
    Min = erlang:min(A, B),
    MaxV = erlang:max(A, B),
    MaxV =< 2 * Min.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_strong_pair_xor(nums :: [integer]) :: integer
  def maximum_strong_pair_xor(nums) do
    len = length(nums)

    Enum.reduce(0..len - 1, 0, fn i, acc ->
      Enum.reduce(i..len - 1, acc, fn j, acc2 ->
        x = Enum.at(nums, i)
        y = Enum.at(nums, j)

        minv = if x < y, do: x, else: y
        maxv = if x > y, do: x, else: y

        if maxv <= 2 * minv do
          xor = Bitwise.bxor(x, y)
          if xor > acc2, do: xor, else: acc2
        else
          acc2
        end
      end)
    end)
  end
end
```
