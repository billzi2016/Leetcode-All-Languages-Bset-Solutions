# 0137. Single Number II

## Cpp

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            twos |= ones & num;      // add to twos bits that are set in both ones and current number
            ones ^= num;             // toggle bits in ones with current number
            int common = ~(ones & twos); // bits appearing three times
            ones &= common;
            twos &= common;
        }
        return ones;
    }
};
```

## Java

```java
class Solution {
    public int singleNumber(int[] nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            // add current number to 'twos' if it was already in 'ones'
            twos |= ones & num;
            // XOR the current number with 'ones'
            ones ^= num;
            // common bits that appear three times
            int commonMask = ~(ones & twos);
            // remove common bits from 'ones' and 'twos'
            ones &= commonMask;
            twos &= commonMask;
        }
        return ones;
    }
}
```

## Python

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            bit_sum = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    bit_sum += 1
            if bit_sum % 3:
                result |= mask
        # convert to signed integer
        if result >= 2 ** 31:
            result -= 2 ** 32
        return result
```

## Python3

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0xFFFFFFFF
        ones = twos = 0
        for num in nums:
            num &= mask
            twos |= ones & num
            ones ^= num
            common = ones & twos
            ones &= ~common
            twos &= ~common
        # convert to signed integer
        if ones & (1 << 31):
            return ones - (1 << 32)
        return ones
```

## C

```c
int singleNumber(int* nums, int numsSize) {
    int ones = 0, twos = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        twos |= ones & x;
        ones ^= x;
        int common = ~(ones & twos);
        ones &= common;
        twos &= common;
    }
    return ones;
}
```

## Csharp

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        int ones = 0, twos = 0;
        foreach (int num in nums) {
            // Add it to 'twos' if it's already in 'ones'
            twos |= ones & num;
            // XOR adds it to 'ones' or removes if already there
            ones ^= num;
            // common bits that appear three times
            int commonMask = ~(ones & twos);
            // Remove common bits from 'ones' and 'twos'
            ones &= commonMask;
            twos &= commonMask;
        }
        return ones;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ones = 0, twos = 0;
    for (let num of nums) {
        // add bits to twos where they appear second time
        twos |= ones & num;
        // toggle bits in ones
        ones ^= num;
        // common bits that appeared three times
        const commonMask = ~(ones & twos);
        // remove common bits from ones and twos
        ones &= commonMask;
        twos &= commonMask;
    }
    return ones;
};
```

## Typescript

```typescript
function singleNumber(nums: number[]): number {
    let ones = 0, twos = 0;
    for (const num of nums) {
        // add current number to 'twos' if it is already in 'ones'
        twos |= ones & num;
        // XOR the current number with 'ones'
        ones ^= num;
        // common bits that appear three times
        const commonMask = ~(ones & twos);
        // remove common bits from 'ones' and 'twos'
        ones &= commonMask;
        twos &= commonMask;
    }
    return ones;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber($nums) {
        $ones = 0;
        $twos = 0;
        foreach ($nums as $num) {
            // add it to twos if it's already in ones
            $twos |= ($ones & $num);
            // XOR adds it to ones or removes it if present twice
            $ones ^= $num;
            // common bits that appear three times
            $commonMask = ~($ones & $twos);
            // remove common bits from ones and twos
            $ones &= $commonMask;
            $twos &= $commonMask;
        }
        return $ones;
    }
}
```

## Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var ones = 0
        var twos = 0
        for num in nums {
            let updatedTwos = twos | (ones & num)
            let updatedOnes = ones ^ num
            let commonMask = ~(updatedOnes & updatedTwos)
            ones = updatedOnes & commonMask
            twos = updatedTwos & commonMask
        }
        return ones
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun singleNumber(nums: IntArray): Int {
        var ones = 0
        var twos = 0
        for (num in nums) {
            // Add it to twos if it's already in ones
            twos = twos or (ones and num)
            // XOR adds bits to ones, removing those that appear twice
            ones = ones xor num
            // common bits that appeared three times
            val commonMask = ones and twos
            // remove common bits from both ones and twos
            ones = ones and commonMask.inv()
            twos = twos and commonMask.inv()
        }
        return ones
    }
}
```

## Dart

```dart
class Solution {
  int singleNumber(List<int> nums) {
    int ones = 0;
    int twos = 0;
    for (int num in nums) {
      int newOnes = (ones ^ num) & ~twos;
      int newTwos = (twos ^ num) & ~newOnes;
      ones = newOnes;
      twos = newTwos;
    }
    return ones;
  }
}
```

## Golang

```go
func singleNumber(nums []int) int {
	var ones, twos int
	for _, num := range nums {
		twos |= ones & num
		ones ^= num
		common := ones & twos
		ones &= ^common
		twos &= ^common
	}
	return ones
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  result = 0
  (0...32).each do |i|
    sum = 0
    nums.each do |num|
      sum += (num >> i) & 1
    end
    if (sum % 3) != 0
      result |= (1 << i)
    end
  end
  # convert to signed 32-bit integer if needed
  result >= (1 << 31) ? result - (1 << 32) : result
end
```

## Scala

```scala
object Solution {
    def singleNumber(nums: Array[Int]): Int = {
        var ones = 0
        var twos = 0
        for (num <- nums) {
            val newTwos = twos | (ones & num)
            val newOnes = ones ^ num
            val commonMask = ~(newOnes & newTwos)
            ones = newOnes & commonMask
            twos = newTwos & commonMask
        }
        ones
    }
}
```

## Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut ones: i32 = 0;
        let mut twos: i32 = 0;
        for num in nums {
            twos |= ones & num;
            ones ^= num;
            let common = !(ones & twos);
            ones &= common;
            twos &= common;
        }
        ones
    }
}
```

## Racket

```racket
(define/contract (single-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (ones 0) (twos 0))
    (if (null? lst)
        ones
        (let* ((x (car lst))
               (new-twos (bitwise-ior twos (bitwise-and ones x)))
               (new-ones (bitwise-xor ones x))
               (common-mask (bitwise-not (bitwise-and new-ones new-twos)))
               (final-ones (bitwise-and new-ones common-mask))
               (final-twos (bitwise-and new-twos common-mask)))
          (loop (cdr lst) final-ones final-twos)))))
```

## Erlang

```erlang
-spec single_number([integer()]) -> integer().
single_number(Nums) ->
    Mask = 16#FFFFFFFF,
    {Ones, _Twos} = lists:foldl(
        fun(N, {O, T}) ->
            O1 = (O bxor N) band Mask,
            T1 = (T bor (O band N)) band Mask,
            Common = bnot (O1 band T1) band Mask,
            O2 = O1 band Common,
            T2 = T1 band Common,
            {O2, T2}
        end,
        {0, 0},
        Nums
    ),
    if
        Ones >= 16#80000000 ->
            Ones - 16#100000000;
        true ->
            Ones
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec single_number(nums :: [integer]) :: integer
  def single_number(nums) do
    {ones, _twos} =
      Enum.reduce(nums, {0, 0}, fn num, {ones, twos} ->
        n = Bitwise.band(num, 0xFFFFFFFF)
        new_twos = Bitwise.bor(twos, Bitwise.band(ones, n))
        new_ones = Bitwise.bxor(ones, n)
        common_mask =
          Bitwise.bnot(Bitwise.band(new_ones, new_twos))
          |> Bitwise.band(0xFFFFFFFF)

        final_ones = Bitwise.band(new_ones, common_mask)
        final_twos = Bitwise.band(new_twos, common_mask)
        {final_ones, final_twos}
      end)

    if ones > 0x7FFFFFFF do
      ones - 0x100000000
    else
      ones
    end
  end
end
```
