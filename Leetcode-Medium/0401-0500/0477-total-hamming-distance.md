# 0477. Total Hamming Distance

## Cpp

```cpp
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int n = nums.size();
        long long total = 0;
        for (int bit = 0; bit < 32; ++bit) {
            int cnt = 0;
            for (int x : nums) {
                if ((x >> bit) & 1) ++cnt;
            }
            total += static_cast<long long>(cnt) * (n - cnt);
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int totalHammingDistance(int[] nums) {
        int n = nums.length;
        int total = 0;
        for (int bit = 0; bit < 31; ++bit) { // up to 30th bit enough for 1e9, but use 31 bits
            int countOnes = 0;
            for (int num : nums) {
                if (((num >> bit) & 1) == 1) {
                    countOnes++;
                }
            }
            total += countOnes * (n - countOnes);
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for bit in range(32):  # enough for numbers up to 10^9
            count_one = 0
            mask = 1 << bit
            for num in nums:
                if num & mask:
                    count_one += 1
            count_zero = n - count_one
            total += count_one * count_zero
        return total
```

## Python3

```python
from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(32):
            count = sum((num >> i) & 1 for num in nums)
            total += count * (n - count)
        return total
```

## C

```c
int totalHammingDistance(int* nums, int numsSize) {
    int total = 0;
    for (int bit = 0; bit < 32; ++bit) {
        int count = 0;
        for (int i = 0; i < numsSize; ++i) {
            if ((nums[i] >> bit) & 1) {
                ++count;
            }
        }
        total += count * (numsSize - count);
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int TotalHammingDistance(int[] nums) {
        int n = nums.Length;
        long total = 0;
        for (int bit = 0; bit < 31; bit++) {
            int mask = 1 << bit;
            int countOnes = 0;
            foreach (int num in nums) {
                if ((num & mask) != 0) countOnes++;
            }
            total += (long)countOnes * (n - countOnes);
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var totalHammingDistance = function(nums) {
    const n = nums.length;
    let total = 0;
    for (let bit = 0; bit < 32; bit++) {
        let countOnes = 0;
        for (let i = 0; i < n; i++) {
            if ((nums[i] >> bit) & 1) {
                countOnes++;
            }
        }
        total += countOnes * (n - countOnes);
    }
    return total;
};
```

## Typescript

```typescript
function totalHammingDistance(nums: number[]): number {
    const n = nums.length;
    let total = 0;
    for (let i = 0; i < 31; i++) { // sufficient for numbers up to 1e9
        let countOnes = 0;
        for (const num of nums) {
            if ((num >> i) & 1) countOnes++;
        }
        total += countOnes * (n - countOnes);
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function totalHammingDistance($nums) {
        $n = count($nums);
        $total = 0;
        for ($bit = 0; $bit < 31; $bit++) {
            $cnt = 0;
            foreach ($nums as $num) {
                if ((($num >> $bit) & 1) === 1) {
                    $cnt++;
                }
            }
            $total += $cnt * ($n - $cnt);
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func totalHammingDistance(_ nums: [Int]) -> Int {
        let n = nums.count
        var total = 0
        for bit in 0..<32 {
            var countOnes = 0
            for num in nums {
                if ((num >> bit) & 1) == 1 {
                    countOnes += 1
                }
            }
            total += countOnes * (n - countOnes)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalHammingDistance(nums: IntArray): Int {
        val n = nums.size
        var total = 0L
        for (bit in 0 until 31) {
            var ones = 0
            for (num in nums) {
                if ((num shr bit) and 1 == 1) {
                    ones++
                }
            }
            total += ones.toLong() * (n - ones)
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int totalHammingDistance(List<int> nums) {
    int n = nums.length;
    int total = 0;
    for (int i = 0; i < 32; i++) {
      int mask = 1 << i;
      int countOnes = 0;
      for (int num in nums) {
        if ((num & mask) != 0) countOnes++;
      }
      total += countOnes * (n - countOnes);
    }
    return total;
  }
}
```

## Golang

```go
func totalHammingDistance(nums []int) int {
    n := len(nums)
    total := 0
    for i := 0; i < 31; i++ {
        mask := 1 << i
        countOnes := 0
        for _, num := range nums {
            if num&mask != 0 {
                countOnes++
            }
        }
        total += countOnes * (n - countOnes)
    }
    return total
}
```

## Ruby

```ruby
def total_hamming_distance(nums)
  n = nums.length
  total = 0
  (0..31).each do |i|
    mask = 1 << i
    count = 0
    nums.each { |num| count += 1 if (num & mask) != 0 }
    total += count * (n - count)
  end
  total
end
```

## Scala

```scala
object Solution {
    def totalHammingDistance(nums: Array[Int]): Int = {
        val n = nums.length
        var total: Long = 0L
        for (bit <- 0 until 32) {
            var countOnes = 0
            var i = 0
            while (i < n) {
                if (((nums(i) >> bit) & 1) == 1) countOnes += 1
                i += 1
            }
            val zeros = n - countOnes
            total += countOnes.toLong * zeros
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_hamming_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut total: i32 = 0;
        for bit in 0..31 {
            let mut count_one: i32 = 0;
            for &num in &nums {
                if ((num >> bit) & 1) == 1 {
                    count_one += 1;
                }
            }
            let count_zero = n - count_one;
            total += count_one * count_zero;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (total-hamming-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (max-bit 31))
    (for/sum ([bit (in-range 0 (+ max-bit 1))])
      (let* ((mask (arithmetic-shift 1 bit))
             (cnt1 (foldl (lambda (x acc)
                            (+ acc (if (zero? (bitwise-and x mask)) 0 1)))
                          0 nums))
             (cnt0 (- n cnt1)))
        (* cnt1 cnt0)))))
```

## Erlang

```erlang
-module(solution).
-export([total_hamming_distance/1]).

-spec total_hamming_distance(Nums :: [integer()]) -> integer().
total_hamming_distance(Nums) ->
    N = length(Nums),
    total_hamming_distance_bits(Nums, N, 0, 0).

total_hamming_distance_bits(_Nums, _N, Bit, Acc) when Bit >= 32 ->
    Acc;
total_hamming_distance_bits(Nums, N, Bit, Acc) ->
    CountOnes = count_ones_bit(Nums, Bit, 0),
    Contribution = CountOnes * (N - CountOnes),
    total_hamming_distance_bits(Nums, N, Bit + 1, Acc + Contribution).

count_ones_bit([], _Bit, Acc) -> Acc;
count_ones_bit([H|T], Bit, Acc) ->
    case (H bsr Bit) band 1 of
        1 -> count_ones_bit(T, Bit, Acc + 1);
        0 -> count_ones_bit(T, Bit, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec total_hamming_distance(nums :: [integer]) :: integer
  def total_hamming_distance(nums) do
    n = length(nums)

    Enum.reduce(0..31, 0, fn bit, acc ->
      mask = 1 <<< bit
      cnt1 = Enum.count(nums, fn x -> (x &&& mask) != 0 end)
      acc + cnt1 * (n - cnt1)
    end)
  end
end
```
